# Step 1: Create an environment<a name="tutorial-create-environment"></a>

\(First step of [Tutorial: Hello AWS Cloud9 \(console\)](tutorial.md)\)

In this step, you use the AWS Cloud9 console to create and then open an AWS Cloud9 development environment\.

**Note**  
If you already created the environment that you want to use for this tutorial, open that environment and skip ahead to [Step 2: Basic tour of the IDE](tutorial-tour-ide.md)\.

In AWS Cloud9, a *development environment*, or *environment*, is somewhere where you store your development project's files and run the tools to develop your applications\. In this tutorial, you create an *EC2 environment*, and work with the files and tools in that environment\.

## Create an EC2 Environment with the console<a name="tutorial-create-environment-console"></a>

1. Sign in to the AWS Cloud9 console:
   + If you're the only one that using your AWS account or you're an IAM user in a single AWS account, go to [https://console\.aws\.amazon\.com/cloud9/](https://console.aws.amazon.com/cloud9/)\.
   + If your organization uses AWS IAM Identity Center \(successor to AWS Single Sign\-On\), ask your AWS account administrator for sign\-in instructions\.
   + If you're a student in a classroom, ask your instructor for sign\-in instructions\.

1. After you sign in to the AWS Cloud9 console, in the top navigation bar choose an AWS Region to create the environment in\. For a list of available AWS Regions, see [AWS Cloud9](https://docs.aws.amazon.com/general/latest/gr/rande.html#cloud9_region) in the *AWS General Reference*\.  
![\[AWS Region selector in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/consolas_region_new_UX.png)

1. Choose the large **Create environment** button in one of the locations shown\.

   If you don't already have AWS Cloud9 environments, the button is shown on a welcome page\.  
![\[Welcome page in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/create_welcome_env_new_UX.png)

   If you already have AWS Cloud9 environments, the button is shown as follows\.  
![\[Create environment button in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console_create_env_new_UX.png)

1. On the **Create environment** page, for **Name**, enter a name for your environment\.

1. For **Description**, enter something about your environment\. For this tutorial, use `This environment is for the AWS Cloud9 tutorial.`

1. For **Environment type**, choose **New EC2 instance** to create an Amazon EC2 environment:
   + **New EC2 instance** – Launches a new Amazon EC2 instance that AWS Cloud9 can connect to directly over SSH\. You can use the Systems Manager to interact with new Amazon EC2 instances, for more information, see [Accessing no\-ingress EC2 instances with AWS Systems Manager](ec2-ssm.md)\. 
   + ** Existing compute ** – Launches an existing Amazon EC2 instance that requires SSH login details for which the Amazon EC2 instance must have an inbound security group rule\.
     + If you select the **Existing compute** option, a service role is automatically created\.  You can view the name of the service role in a note at the bottom of the setup screen\. 
**Warning**  
Creating an EC2 instance for your environment might result in possible charges to your AWS account for Amazon EC2\. There's no additional cost to use Systems Manager to manage connections to your EC2 instance\.

1. On the New EC2 instance panel for **Instance type**, keep the default choice\. This option might have less RAM and fewer vCPUs\. However, this amount of memory is sufficient for this tutorial\.
**Warning**  
Choosing instance types with more RAM and vCPUs might result in additional charges to your AWS account for Amazon EC2\.

1. For **Platform**, choose the type of Amazon EC2 instance that you want: **Amazon Linux 2**, **Amazon Linux**, or **Ubuntu**\. AWS Cloud9 creates the instance and then connects the environment to it\.
**Important**  
We recommend that you choose the **Amazon Linux 2** option for your EC2 environment\. In addition to providing a secure, stable, and high\-performance runtime environment, Amazon Linux 2 AMI includes long\-term support through 2023\.  
Standard support for the previous version of Amazon Linux AMI discontinued on December 31, 2020\. Now this version only receives maintenance support\.  
For more information, see the [Amazon Linux 2 page](https://aws.amazon.com/amazon-linux-2/)\.

1. Choose a time period for **Timeout**\. This option determines how long AWS Cloud9 is inactive before auto\-hibernating\. When all web browser instances that are connected to the IDE for the environment are closed, AWS Cloud9 waits the amount of time specified and then shuts down the Amazon EC2 instance for the environment\. 
**Warning**  
Choosing a longer time period might result in more charges to your AWS account\.

1. On the **Network settings** panel, choose how your environment is accessed from the two following options:
   + **AWS Systems Manager \(SSM\)** – This method accesses the environment using SSM without opening inbound ports\.
   + **Secure Shell \(SSH\)** – This method accesses the environment using SSH and requires open inbound ports\.

1. Choose **VPC Settings** to display the Amazon Virtual Private Cloud and Subnet for your environment\. AWS Cloud9 uses Amazon Virtual Private Cloud \(Amazon VPC\) to communicate with the newly created Amazon EC2 instance\. For this tutorial, we recommend that you don't change the preselected default settings\. With the default settings, AWS Cloud9 attempts to automatically use the default VPC with its single subnet in the same AWS account and Region as the new environment\.

   You can find more information about Amazon VPC choices in [Create an EC2 Environment with the Console](create-environment-main.md#create-environment-vpc-step), and in [VPC settings for AWS Cloud9 Development Environments](vpc-settings.md)\.

1. Add up to 50 tags by supplying a **Key** and **Value** for each tag\. Do so by selecting **Add new tag**\. The tags are attached to the AWS Cloud9 environment as resource tags, and are propagated to the following underlying resources: the AWS CloudFormation stack, the Amazon EC2 instance, and Amazon EC2 security groups\. To learn more about tags, see [Control Access Using AWS Resource Tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) in the *[IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)* and [advanced information](tags.md) in this guide\.
**Warning**  
If you update these tags after you create them, the changes aren't propagated to the underlying resources\. For more information, see [Propagating tag updates to underlying resources](tags.md#tags-propagate) in the advanced information about [tags](tags.md)\.

1. Choose **Create** to create your environment, and then you're redirected to the home page\. If the account is successfully created, a green flash bar appears at the top of the AWS Cloud9 console\. You can select the new environment and choose **Open in Cloud9** to launch the IDE\.  
![\[AWS Cloud9 IDE selector in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/cloud9-ide-open.png)

   If the account fails to create, a red flash bar appears at the top of the AWS Cloud9 console\. Your account might fail to create because of a problem with your web browser, your AWS access permissions, the instance, or the associated network\. You can find information about possible fixes in the [AWS Cloud9 Troubleshooting section\.](troubleshooting.md#troubleshooting-env-loading)

## Next step<a name="tutorial-create-env-next"></a>

[Step 2: Basic tour of the IDE](tutorial-tour-ide.md)