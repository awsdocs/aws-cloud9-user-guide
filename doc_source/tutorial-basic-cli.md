# CLI Supplement for Tutorial: First Look at the AWS Cloud9 IDE<a name="tutorial-basic-cli"></a>

In [Tutorial: First Look at the AWS Cloud9 IDE](tutorial.md), you use the AWS Cloud9 console to set up an AWS Cloud9 environment, tour the AWS Cloud9 IDE, and then delete the environment;\. As an alternative, environment setup and deletion can also be accomplished using the AWS CLI\.

**Warning**  
Completing this tutorial might result in charges to your AWS account\. These include possible charges for Amazon EC2\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/)\.

**Topics**
+ [Prerequisites](#tutorial-prereqs-cli)
+ [Step 1: Create an Environment](#tutorial-create-environment-cli-step1)
+ [Step 2: Tour the IDE](#tutorial-tour-ide-cli-step2)
+ [Step 3: Clean Up](#tutorial-clean-up-cli-step3)

## Prerequisites<a name="tutorial-prereqs-cli"></a>

See the [prerequisites](tutorial.md#tutorial-prereqs) in *[Tutorial: First Look at the IDE](tutorial.md)*\.

## Step 1: Create an Environment<a name="tutorial-create-environment-cli-step1"></a>

Corresponds to [Step 1: Create an Environment](tutorial-create-environment.md) in *[Tutorial: First Look at the IDE](tutorial.md)*\.

### Create an EC2 Environment with the AWS CLI<a name="tutorial-create-environment-cli"></a>

**Note**  
Currently, you cannot use the AWS CLI to create an Ubuntu Server\-based EC2 environment—only Amazon Linux\. Support for Ubuntu Server is expected in the future\.

1. Install and configure the AWS CLI, if you have not done so already\. To do this, see the following in the *AWS Command Line Interface User Guide*\.
   +  [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/installing.html) 
   +  [Quick Configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-quick-configuration) 

   We recommend you configure the AWS CLI using credentials for one of the following\.
   + The IAM user you created in [Team Setup for AWS Cloud9](setup.md)\.
   + An IAM administrator user in your AWS account, if you will be working regularly with AWS Cloud9 resources for multiple users across the account\. If you cannot configure the AWS CLI as an IAM administrator user, check with your AWS account administrator\. For more information, see [Creating Your First IAM Admin User and Group](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html) in the *IAM User Guide*\.
   + An AWS account root user, but only if you will always be the only one using your own AWS account, and you don't need to share your environments with anyone else\. For more information, see [Creating, Disabling, and Deleting Access Keys for Your AWS Account](https://docs.aws.amazon.com/general/latest/gr/managing-aws-access-keys.html#create-aws-access-key) in the *Amazon Web Services General Reference*\.
   + For other options, see your AWS account administrator or classroom instructor\.

1. Run the AWS Cloud9 `create-environment-ec2` command\.

   ```
   aws cloud9 create-environment-ec2 --name my-demo-environment --description "This environment is for the AWS Cloud9 tutorial." --instance-type t2.micro --region us-east-1 --subnet-id subnet-12a3456b
   ```

   In the preceding command:
   +  `--name` represents the name of the environment\. In this tutorial, we use the name `my-demo-environment`\.
   +  `--description` represents an optional description for the environment\.
   +  `--instance-type` represents the type of Amazon EC2 instance AWS Cloud9 will launch and connect to the new environment\. This example specifies `t2.micro`, which has relatively low RAM and vCPUs and is sufficient for this tutorial\. Specifying instance types with more RAM and vCPUs might result in additional charges to your AWS account for Amazon EC2\. For a list of available instance types, see the create environment wizard in the AWS Cloud9 console\.
   +  `--region` represents the ID of the AWS Region for AWS Cloud9 to create the environment in\. For a list of available AWS Regions, see [AWS Cloud9](https://docs.aws.amazon.com/general/latest/gr/rande.html#cloud9_region) in the *Amazon Web Services General Reference*\.
   +  `--subnet-id` represents the subnet you want AWS Cloud9 to use\. Replace `subnet-12a3456b` with the ID of the subnet, which must be compatible with AWS Cloud9\. For more information, see [VPC Settings for AWS Cloud9 Development Environments](vpc-settings.md)\.
   + By default, AWS Cloud9 shuts down the Amazon EC2 instance for the environment 30 minutes after all web browser instances that are connect to the IDE for the environment have been closed\. To change this, add `--automatic-stop-time-minutes` along with the number of minutes\. A shorter time period might result in fewer charges to your AWS account\. Likewise, a longer time might result in more charges\.
   + By default, the entity that calls this command owns the environment\. To change this, add `--owner-id` along with the Amazon Resource Name \(ARN\) of the owning entity\.

After you successfully run this command, open the AWS Cloud9 IDE for the newly\-created environment\. To do this, see [Opening an Environment in AWS Cloud9](open-environment.md)\. Then return to this topic and continue on with [Step 2: Tour the IDE](tutorial-tour-ide.md) to learn how to use the AWS Cloud9 IDE to work with your new environment\.

If you try to open the environment, but AWS Cloud9 doesn't display the IDE after at least five minutes, there might be a problem with your web browser, your AWS access permissions, the instance, or the associated virtual private cloud \(VPC\)\. For possible fixes, see [Cannot Open an Environment](troubleshooting.md#troubleshooting-env-loading) in *Troubleshooting*\.

To learn more about what you can do with an environment after you finish this tutorial, see [Working with Environments in AWS Cloud9](environments.md)\.

## Step 2: Tour the IDE<a name="tutorial-tour-ide-cli-step2"></a>

See [Step 2: Tour the IDE](tutorial-tour-ide.md) in *[Tutorial: First Look at the IDE](tutorial.md)*\.

## Step 3: Clean Up<a name="tutorial-clean-up-cli-step3"></a>

Corresponds to [Step 3: Clean Up](tutorial-clean-up.md) in *[Tutorial: First Look at the IDE](tutorial.md)*\.

To prevent ongoing charges to your AWS account related to this tutorial, you should delete the environment\.

**Warning**  
Deleting an environment cannot be undone\.

### Delete the Environment with the AWS CLI<a name="tutorial-clean-up-cli"></a>

Run the AWS Cloud9 `delete-environment` command, specifying the ID of the environment to delete\.

```
aws cloud9 delete-environment --environment-id 12a34567b8cd9012345ef67abcd890e1
```

In the preceding command, replace `12a34567b8cd9012345ef67abcd890e1` with the ID of the environment to delete\.