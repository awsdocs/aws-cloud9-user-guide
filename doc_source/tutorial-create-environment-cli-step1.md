# Step 1: Create an environment<a name="tutorial-create-environment-cli-step1"></a>

\(First step of [Tutorial: Hello AWS Cloud9 \(CLI\)](tutorial-basic-cli.md)\)

In this step, you use the AWS CLI to create an AWS Cloud9 development environment\.

In AWS Cloud9, a *development environment* \(or only an *environment*\) is a place where you store your development project's files and where you run the tools to develop your applications\. In this tutorial, you create a special kind of environment called an *EC2 environment*, and then work with the files and tools in that environment\.

## Create an EC2 environment with the AWS CLI<a name="tutorial-create-environment-cli"></a>

**Important**  
Currently, only environments connected to Amazon Linux can be created with the AWS CLI\. You can't use the AWS CLI to create an Amazon Linux 2\-based or an Ubuntu Server\-based environment\.   
We're planning to support Amazon Linux 2 and are evaluating support for Ubuntu Server\. In the meantime, for EC2 environments backed by Amazon Linux 2 or Ubuntu Server, use the [console option](create-environment-main.md#create-environment-console)\.

1. Install and configure the AWS CLI, if you have not done so already\. To do this, see the following in the *AWS Command Line Interface User Guide*:
   +  [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/installing.html) 
   +  [Quick configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-quick-configuration) 

   You can configure the AWS CLI using credentials for one of the following:
   + The IAM user you created in [Team setup for AWS Cloud9](setup.md)\.
   + An IAM administrator in your AWS account, if you will be working regularly with AWS Cloud9 resources for multiple users across the account\. If you cannot configure the AWS CLI as an IAM administrator, check with your AWS account administrator\. For more information, see [Creating your first IAM admin user and group](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html) in the *IAM User Guide*\.
   + An AWS account root user, but only if you will always be the only one using your own AWS account, and you don't need to share your environments with anyone else\. We don't recommend this option as it isn't an AWS security best practice\. For more information, see [Creating, Disabling, and Deleting Access Keys for Your AWS Account](https://docs.aws.amazon.com/general/latest/gr/managing-aws-access-keys.html#create-aws-access-key) in the *Amazon Web Services General Reference*\.
   + For other options, see your AWS account administrator or classroom instructor\.

1. In the following AWS Cloud9 command, provide a value for `--region` and `--subnet-id`\. Then run the command and make a note of the `"environmentId"` value for later cleanup\.

   ```
   aws cloud9 create-environment-ec2 --name my-demo-environment --description "This environment is for the AWS Cloud9 tutorial." --instance-type t2.micro --region MY-REGION --connection-type CONNECT_SSM --subnet-id subnet-12a3456b
   ```

   In the preceding command:
   +  `--name` represents the name of the environment\. In this tutorial, we use the name `my-demo-environment`\.
   +  `--description` represents an optional description for the environment\.
   +  `--instance-type` represents the type of Amazon EC2 instance AWS Cloud9 will launch and connect to the new environment\. This example specifies `t2.micro`, which has relatively low RAM and vCPUs and is sufficient for this tutorial\. Specifying instance types with more RAM and vCPUs might result in additional charges to your AWS account for Amazon EC2\. For a list of available instance types, see the create environment wizard in the AWS Cloud9 console\.
   +  `--region` represents the ID of the AWS Region for AWS Cloud9 to create the environment in\. For a list of available AWS Regions, see [AWS Cloud9](https://docs.aws.amazon.com/general/latest/gr/rande.html#cloud9_region) in the *Amazon Web Services General Reference*\.
   +  `--connection-type CONNECT_SSM` specifies that AWS Cloud9 connects to its Amazon EC2 instance through Systems Manager\. This option ensures no inbound traffic to the instance is allowed\. For more information, see [Accessing no\-ingress EC2 instances with AWS Systems Manager](ec2-ssm.md)\. 
   +  `--subnet-id` represents the subnet you want AWS Cloud9 to use\. Replace `subnet-12a3456b` with the ID of the subnet of an Amazon Virtual Private Cloud \(VPC\), which must be compatible with AWS Cloud9\. For more information, see [Create an Amazon VPC for AWS Cloud9](vpc-settings.md#vpc-settings-create-vpc) in *[VPC settings for AWS Cloud9 Development Environments](vpc-settings.md)*\.
   + By default, AWS Cloud9 shuts down the Amazon EC2 instance for the environment 30 minutes after all web browser instances that are connected to the IDE for the environment have been closed\. To change this, add `--automatic-stop-time-minutes` and the number of minutes\. A shorter time period might result in fewer charges to your AWS account\. Likewise, a longer time might result in more charges\.
   + By default, the entity that calls this command owns the environment\. To change this, add `--owner-id` and the Amazon Resource Name \(ARN\) of the owning entity\.

1. After you successfully run this command, open the AWS Cloud9 IDE for the newly created environment\. To do this, see [Opening an environment in AWS Cloud9](open-environment.md)\. Then return to this topic and continue with [Step 2: Basic tour of the IDE](tutorial-tour-ide.md) to learn how to use the AWS Cloud9 IDE to work with your new environment\.

   If you try to open the environment, but AWS Cloud9 doesn't display the IDE after at least five minutes, there might be a problem with your web browser, your AWS access permissions, the instance, or the associated VPC\. For possible fixes, see [Cannot open an environment](troubleshooting.md#troubleshooting-env-loading)\.

## Next Step<a name="tutorial-create-environment-cli-step1-next"></a>

[Step 2: Basic Tour of the IDE](tutorial-tour-ide-cli-step2.md)