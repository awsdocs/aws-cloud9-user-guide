# Moving or Resizing an Environment in AWS Cloud9<a name="move-environment"></a>

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
+ [Moving an Environment](#move-environment-move)
+ [Resizing an Environment](#move-environment-resize)

## Moving an Environment<a name="move-environment-move"></a>

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

## Resizing an Environment<a name="move-environment-resize"></a>

1. Open the environment that is associated with the Amazon EC2 instance for the Amazon EBS volume that you want to resize\.

1. In the AWS Cloud9 IDE for the environment, create a file with the following contents, and then save the file with the extension `.sh`, for example, `resize.sh`\.

   For Amazon Linux:

   ```
   #!/bin/bash -e
   
   # Specify the desired volume size in GiB as a command-line argument. If not specified, default to 20 GiB.
   SIZE=${1:=20}
   
   # Install the jq command-line JSON processor.
   sudo yum -y install jq
   
   # Get the ID of the envrionment host Amazon EC2 instance.
   INSTANCEID=$(curl http://169.254.169.254/latest/meta-data//instance-id)
   
   # Get the ID of the Amazon EBS volume associated with the instance.
   VOLUMEID=$(aws ec2 describe-instances --instance-id $INSTANCEID | jq -r .Reservations[0].Instances[0].BlockDeviceMappings[0].Ebs.VolumeId)
   
   # Resize the EBS volume.
   aws ec2 modify-volume --volume-id $VOLUMEID --size $SIZE
   
   # Wait for the resize to finish.
   while [ "$(aws ec2 describe-volumes-modifications --volume-id $VOLUMEID --filters Name=modification-state,Values="optimizing","completed" | jq '.VolumesModifications | length')" != "1" ]; do
     sleep 1
   done

   # Rewrite the partition table and expand the size of the file system
   if [ -e /dev/nvme0n1p1 ]; then
       sudo growpart /dev/nvme0n1 1
       sudo resize2fs /dev/nvme0n1p1
   else
       sudo growpart /dev/xvda 1
       sudo resize2fs /dev/xvda1
   fi

   # Show the result
   df -h /
   ```

   For Ubuntu Server:

   ```
   #!/bin/bash -e
   
   # Specify the desired volume size in GiB as a command-line argument. If not specified, default to 20 GiB.
   SIZE=${1:=20}
   
   # Install the jq command-line JSON processor.
   sudo apt update
   sudo apt install -y jq
   
   # Get the ID of the envrionment host Amazon EC2 instance.
   INSTANCEID=$(curl http://169.254.169.254/latest/meta-data//instance-id)
   
   # Get the ID of the Amazon EBS volume associated with the instance.
   VOLUMEID=$(aws ec2 describe-instances --instance-id $INSTANCEID | jq -r .Reservations[0].Instances[0].BlockDeviceMappings[0].Ebs.VolumeId)
   
   # Resize the EBS volume.
   aws ec2 modify-volume --volume-id $VOLUMEID --size $SIZE
   
   # Wait for the resize to finish.
   while [ "$(aws ec2 describe-volumes-modifications --volume-id $VOLUMEID --filters Name=modification-state,Values="optimizing","completed" | jq '.VolumesModifications | length')" != "1" ]; do
     sleep 1
   done

   # Rewrite the partition table and expand the size of the file system
   if [ -e /dev/nvme0n1p1 ]; then
       sudo growpart /dev/nvme0n1 1
       sudo resize2fs /dev/nvme0n1p1
   else
       sudo growpart /dev/xvda 1
       sudo resize2fs /dev/xvda1
   fi

   # Show the result
   df -h /
   ```

1. From a terminal session in the IDE, switch to the directory that contains the `resize.sh` file\. Then run the following command, replacing 20 with the desired size in GiB to resize the Amazon EBS volume to\.

   ```
   sh resize.sh 20
   ```
