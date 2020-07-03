# Moving an environment and resizing/encrypting Amazon EBS volumes<a name="move-environment"></a>

You can move an AWS Cloud9 development environment from one Amazon EC2 instance to another\. For example, you might want to do one of the following\.
+ Transfer an environment from an Amazon EC2 instance that is broken, or behaving in unexpected ways, to a healthy instance\.
+ Transfer an environment from an older instance to an instance that has the latest system updates\.
+ Increase an instance's compute resources, because the environment is over\-utilized on the current instance\.
+ Decrease an instance's compute resources, because the environment is under\-utilized on the current instance\.

You can also resize the Amazon Elastic Block Store \(Amazon EBS\) volume that is associated with an Amazon EC2 instance for an environment\. For example, you might want to do one of the following\.
+ Increase a volume's size, because you are running out of storage space on the instance\.
+ Decrease a volume's size, because you don't want to pay for extra storage space that you aren't using\.

Before you move or resize an environment, you might want to try stopping some running processes in the environment or adding a swap file to the environment\. For more information, see [IDE Warning: "This Environment is Running Low on Memory" or "This Environment Has High CPU Load"](troubleshooting.md#troubleshooting-ide-low-memory) in *Troubleshooting*\.

This topic only covers moving an environment from one Amazon EC2 instance to another or resizing an Amazon EBS volume\. To resize an environment from one of your own servers to another or to change the storage space for one of your own servers, refer to your server's documentation\.

**Topics**
+ [Moving an environment](#move-environment-move)
+ [Resizing an Amazon EBS volume used by an environment](#move-environment-resize)
+ [Encrypt Amazon EBS volumes used by AWS Cloud9](#encrypting-volumes)

## Moving an environment<a name="move-environment-move"></a>

Before you start the move process, note the following\.
+ You cannot move an environment to an Amazon EC2 instance of the same type\. When you move, you must choose a different Amazon EC2 instance type for the new instance\.
+ You must stop the Amazon EC2 instance that is associated with an environment before you can change the instance type\. While the instance is stopped, neither you nor any members will be able to use the environment that are associated with the stopped instance\.
+ We move the instance to new hardware; however, the instance's ID does not change\.
+ If the instance is running in an Amazon VPC and has a public IPv4 address, we release the address and give it a new public IPv4 address\. The instance retains its private IPv4 addresses, any Elastic IP addresses, and any IPv6 addresses\.
+ Ensure that you plan for downtime while your instance is stopped\. The process might take several minutes\.

To move an environment, do the following\.

1. \(Optional\) If the new instance type requires drivers that are not installed on the existing instance, you must connect to your instance and install the drivers first\. For more information, see [Compatibility for Resizing Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html#resize-limitations) in the *Amazon EC2 User Guide for Linux Instances*\.

1. Close all web browser tabs that are currently displaying the environment\.
**Important**  
If you do not close all of the web browser tabs that are currently displaying the environment, AWS Cloud9 might interfere with allowing you to fully complete the procedure\. Specifically, AWS Cloud9 might try at the wrong time during this procedure to restart the Amazon EC2 instance that is associated with the environment\. The instance must stay stopped until the very last step in this procedure\.

1. Sign in to the AWS Management Console, if you are not already signed in, at [https://console\.aws\.amazon\.com](https://console.aws.amazon.com)\.

   We recommend you sign in using credentials for an IAM administrator user in your AWS account\. If you cannot do this, check with your AWS account administrator\.

1. Open the Amazon EC2 console\. To do this, in the **Services** list, choose **EC2**\.

1. In the AWS navigation bar, choose the AWS Region that contains the environment that you want to move \(for example, **US East \(Ohio\)**\)\.

1. In the service navigation pane, expand **Instances** if it is not already expanded, and then choose **Instances**\.

1. In the list of instances, choose the instance that is associated with the environment that you want to move\. For an EC2 environment, the instance name starts with `aws-cloud9-` followed by the environment name\. For example, if the environment is named `my-demo-environment`, the instance name will start with `aws-cloud9-my-demo-environment`\.

1. If the **Instance State** is not **stopped**, choose **Actions, Instance State, Stop**\. When prompted, choose **Yes, Stop**\. It can take a few minutes for the instance to stop\.

1. After the **Instance State** is **stopped**, with the instance still selected, choose **Actions, Instance Settings, Change Instance Type**\.

1. In the **Change Instance Type** dialog box, for **Instance Type**, choose the new instance type that you want the environment to use\.
**Note**  
If the instance type that you want does not appear in the list, then it is not compatible with the instance's configuration \(for example, because of its virtualization type\)\.

1. \(Optional\) If the instance type that you chose supports EBS–optimization, select **EBS\-optimized** to enable EBS–optimization, or clear **EBS\-optimized** to disable EBS–optimization\.
**Note**  
If the instance type that you chose is EBS–optimized by default, **EBS\-optimized** is selected and you can't clear it\.

1. Choose **Apply** to accept the new settings\.
**Note**  
If you did not choose a different instance type for **Instance Type** earlier in this procedure, nothing happens after you choose **Apply**\.

1. Reopen the environment\. For more information, see [Opening an Environment in AWS Cloud9](open-environment.md)\.

For more information about the preceding procedure, see [Changing the Instance Type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html) in the *Amazon EC2 User Guide for Linux Instances*\.

## Resizing an Amazon EBS volume used by an environment<a name="move-environment-resize"></a>

1. Open the environment that's associated with the Amazon EC2 instance for the Amazon EBS volume that you want to resize\.

1. In the AWS Cloud9 IDE for the environment, create a file with the following contents, and then save the file with the extension `.sh` \(`resize.sh`, for example\)\.
**Note**  
This script works for Amazon EBS volumes connected to EC2 instances running Amazon Linux or Ubuntu Server\.  
 The script also resizes Amazon EBS volumes exposed as NVMe block devices on Nitro\-based instances\. For a list of instances based on the Nitro system, see [Nitro\-based Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances) in the *Amazon EC2 User Guide for Linux Instances*\.

   ```
   #!/bin/bash
   
   # Specify the desired volume size in GiB as a command-line argument. If not specified, default to 20 GiB.
   SIZE=${1:-20}
   
   # Get the ID of the environment host Amazon EC2 instance.
   INSTANCEID=$(curl http://169.254.169.254/latest/meta-data//instance-id)
   
   # Get the ID of the Amazon EBS volume associated with the instance.
   VOLUMEID=$(aws ec2 describe-instances \
     --instance-id $INSTANCEID \
     --query "Reservations[0].Instances[0].BlockDeviceMappings[0].Ebs.VolumeId" \
     --output text)
   
   # Resize the EBS volume.
   aws ec2 modify-volume --volume-id $VOLUMEID --size $SIZE
   
   # Wait for the resize to finish.
   while [ \
     "$(aws ec2 describe-volumes-modifications \
       --volume-id $VOLUMEID \
       --filters Name=modification-state,Values="optimizing","completed" \
       --query "length(VolumesModifications)"\
       --output text)" != "1" ]; do
   sleep 1
   done
   
   if [ $(readlink -f /dev/xvda) = "/dev/xvda" ]
   then
     # Rewrite the partition table so that the partition takes up all the space that it can.
     sudo growpart /dev/xvda 1
    
     # Expand the size of the file system.
     sudo resize2fs /dev/xvda1
   
   else
     # Rewrite the partition table so that the partition takes up all the space that it can.
     sudo growpart /dev/nvme0n1 1
   
     # Expand the size of the file system.
     sudo resize2fs /dev/nvme0n1p1
   fi
   ```

1. From a terminal session in the IDE, switch to the directory that contains the `resize.sh` file\. Then run the following command, replacing 20 with the desired size in GiB to resize the Amazon EBS volume to\.

   ```
   sh resize.sh 20
   ```

## Encrypt Amazon EBS volumes used by AWS Cloud9<a name="encrypting-volumes"></a>

With EBS encryption the following types of data are encrypted:
+ Data at rest inside the volume
+ All data moving between the volume and the instance
+ All snapshots created from the volume
+ All volumes created from those snapshots

You have two encryption options for Amazon EBS volumes that are used by AWS Cloud9 EC2 development environments:
+ **Encryption by default**: You can configure your AWS account to enforce the encryption of the new EBS volumes and snapshot copies that you create\. Encryption by default is enabled at the level of an AWS Region, so you cannot enable for individual volumes or snapshots in that Region\. Moreover, because Amazon EBS encrypts the volume that's created when you launch an instance, you must enable this setting before the creation of an EC2 environment\.

  For more information, see [ Encryption by default](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default) in the *Amazon EC2 User Guide for Linux Instances*\. 
+ **Encryption of an existing Amazon EBS volume used by an EC2 environment**: You can encrypt specific Amazon EBS volumes that have already been created for EC2 instances\. This option involves using the AWS Key Management Service to manage access to the encrypted volume\. For the relevant procedure, see [Encrypt an existing Amazon EBS volume used by AWS Cloud9](#encrypting-existing-volume)

### Encrypt an existing Amazon EBS volume used by AWS Cloud9<a name="encrypting-existing-volume"></a>

Encrypting an existing Amazon EBS volume involves using AWS KMS to create a customer master key \(CMK\)\. After creating a snapshot of the volume to be replaced, you then use the CMK to encrypt a copy of the snapshot\. Next, you create a new encrypted volume with that snapshot\. You now replace the unencrypted volume by detaching it from the EC2 instance and attaching the encrypted volume\. Finally, you must update the key policy for the customer\-managed CMK to enable access for the AWS Cloud9 service role\. 

**Note**  
 The following procedure focuses on using a customer managed CMK to encrypt a volume\. You can also use an [AWS managed CMK](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk) for an AWS service in your account \(the alias for Amazon EBS is `aws/ebs`\)\. If you choose this default option for encryption, skip the first step that creates a customer managed CMK\. Also skip the step that updates the key policy \(you cannot change the key policy for an AWS managed CMK\)\.<a name="creating-encrypted-volume"></a>

1. In the AWS Key Management Service console, create a symmetric customer master key \(CMK\)\. For details, see [Creating symmetric CMKs](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk) in the *AWS Key Management Service Developer Guide*\.

1. In the EC2 Console, stop the Amazon EBS\-backed instance used by the environment\. You can [stop the instance using the console or the command line](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html)\.

1. In the navigation pane of the EC2 console, choose **Snapshots** [to create a snapshot of the existing volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-snapshot.html#ebs-create-snapshot) you want to encrypt\.

1. In the navigation pane of the EC2 console, choose **Snapshots** [to copy the snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-copy-snapshot.html)\. In the **Copy snapshot** dialog box, do the following to enable encryption:
   + Enable the **Encrypt this snapshot** setting\. 
   + For **Master Key**, select the CMK you created earlier\. \(If you're using an AWS managed CMK, keep the `(default) aws/ebs` setting\.\)

1. [Create a new volume from the encrypted snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-volume.html#ebs-create-volume-from-snapshot)\. 
**Note**  
New EBS volumes that are created from encrypted snapshots are automatically encrypted\. 

1. [Detach the old Amazon EBS volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-detaching-volume.html) from the Amazon EC2 instance\. 

1. [Attach the new encrypted volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-attaching-volume.html) to the Amazon EC2 instance\.

1. Update the key policy for the CMK [using the AWS Management Console default view, AWS Management Console policy view, or the AWS KMS API](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying.html#key-policy-modifying-how-to)\. Add the key policy statements below to allow the AWS Cloud9 service, `AWSServiceRoleForAWSCloud9`, to access the CMK\.
**Note**  
Skip this step if you're using an AWS managed CMK\.

   ```
   {
       "Sid": "Allow use of the key",
       "Effect": "Allow",
       "Principal": {
           "AWS": "arn:{Partition}:iam::{AccountId}:role/aws-service-role/cloud9.amazonaws.com/AWSServiceRoleForAWSCloud9"
       },
       "Action": [
           "kms:Encrypt",
           "kms:Decrypt",
           "kms:ReEncrypt*",
           "kms:GenerateDataKey*",
           "kms:DescribeKey"
       ],
       "Resource": "*"
      },
      {
       "Sid": "Allow attachment of persistent resources",
       "Effect": "Allow",
       "Principal": {
           "AWS": "arn:{Partition}:iam::{AccountId}:role/aws-service-role/cloud9.amazonaws.com/AWSServiceRoleForAWSCloud9"
       },
       "Action": [
           "kms:CreateGrant",
           "kms:ListGrants",
           "kms:RevokeGrant"
       ],
       "Resource": "*",
       "Condition": {
           "Bool": {
               "kms:GrantIsForAWSResource": "true"
           }
       }
   }
   ```

1. [Restart the EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html)\.