# Creating an EC2 Environment<a name="create-environment-main"></a>

**Note**  
Completing this procedure might result in charges to your AWS account\. This includes possible charges for Amazon EC2\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/)\.

In this procedure, AWS Cloud9 creates an EC2 environment and a new Amazon EC2 instance, and connects the environment to this instance\. AWS Cloud9 manages the lifecycle of this instance, including starting, stopping, and restarting the instance as needed\. If you ever delete this environment, AWS Cloud9 automatically terminates this instance\.

You can create an AWS Cloud9 EC2 development environment in the [AWS Cloud9 console](#create-environment-console) or with [code](#create-environment-code)\.

## Prerequisites<a name="create-env-ec2-prereq"></a>

Complete the steps in [Setting up AWS Cloud9](setting-up.md) so that you can sign in to the AWS Cloud9 console and create environments\.

## Create an EC2 environment with the console<a name="create-environment-console"></a>

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

1. To add a description to your environment, enter it in the **Description** field\.

1. For **Environment type**, choose **New EC2 instance** to create an Amazon EC2 environment:
   + **New EC2 instance** – Launches a new Amazon EC2 instance that AWS Cloud9 can connect to directly over SSH\. You can use the Systems Manager to interact with new Amazon EC2 instances, for more information, see [Accessing no\-ingress EC2 instances with AWS Systems Manager](ec2-ssm.md)\. 
   + ** Existing compute ** – Launches an existing Amazon EC2 instance that requires SSH login details for which the Amazon EC2 instance must have an inbound security group rule\.
     + If you select the **Existing compute** option, a service role is automatically created\.  You can view the name of the service role in a note at the bottom of the setup screen\. 
**Warning**  
Creating an EC2 instance for your environment might result in possible charges to your AWS account for Amazon EC2\. There's no additional cost to use Systems Manager to manage connections to your EC2 instance\.

1. For **Instance type**, choose an instance type with the amount of RAM and vCPUs that you think you need for the kinds of tasks that you want to do\.
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

1. <a name="create-environment-vpc-step"></a>Choose **VPC Settings** to display the Amazon Virtual Private Cloud and Subnet for your environment\. AWS Cloud9 uses Amazon Virtual Private Cloud \(Amazon VPC\) to communicate with the newly created Amazon EC2 instance\. For this tutorial, we recommend that you don't change the preselected default settings\. With the default settings, AWS Cloud9 attempts to use the default VPC with its single subnet in the same AWS account and Region as the new environment\. Depending on how Amazon VPC is set up, follow one of the following set of instructions\.  
****    
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment-main.html)
**Important**  
If you selected **Existing compute** as your environment type, you can launch your instance into a public or private subnet\.  
**Public subnet**: Attach an internet gateway to the subnet to allow the instance SSM agent to communicate with Systems Manager\.
**Private subnet**: Create a NAT gateway to enable the instance to communicate with the internet and other AWS services\.
Currently, you can't use [AWS managed temporary credentials](security-iam.md#auth-and-access-control-temporary-managed-credentials) to allow the EC2 environment to access an AWS service on behalf of an AWS entity, such as an IAM user\.  
 For more information about configuring subnets, see [VPC settings for AWS Cloud9 Development Environments](vpc-settings.md)\.  
****    
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment-main.html)

   For more information about these choices, see [VPC settings for AWS Cloud9 Development Environments](vpc-settings.md)\.

1. Add up to 50 tags by supplying a **Key** and **Value** for each tag\. Do so by selecting **Add new tag**\. The tags are attached to the AWS Cloud9 environment as resource tags, and are propagated to the following underlying resources: the AWS CloudFormation stack, the Amazon EC2 instance, and Amazon EC2 security groups\. To learn more about tags, see [Control Access Using AWS Resource Tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) in the *[IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)* and [advanced information](tags.md) in this guide\.
**Warning**  
If you update these tags after you create them, the changes aren't propagated to the underlying resources\. For more information, see [Propagating tag updates to underlying resources](tags.md#tags-propagate) in the advanced information about [tags](tags.md)\.

1. Choose **Create** to create your environment, and then you're redirected to the home page\. If the account is successfully created, a green flash bar appears at the top of the AWS Cloud9 console\. You can select the new environment and choose **Open in Cloud9** to launch the IDE\.  
![\[AWS Cloud9 IDE selector in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/cloud9-ide-open.png)

   If the account fails to create, a red flash bar appears at the top of the AWS Cloud9 console\. Your account might fail to create because of a problem with your web browser, your AWS access permissions, the instance, or the associated network\. You can find information about possible fixes in the [AWS Cloud9 Troubleshooting section\.](troubleshooting.md#troubleshooting-env-loading)

**Note**  
If your environment is using a proxy to access the internet, you must provide proxy details to AWS Cloud9 so it can install dependencies\. For more information, see [Notice: Failed to install dependencies for collaboration support](troubleshooting.md#proxy-failed-dependencies)\.

## Creating an environment with code<a name="create-environment-code"></a>

To use code to create an EC2 environment in AWS Cloud9, call the AWS Cloud9 create EC2 environment operation, as follows\.


****  

|  |  | 
| --- |--- |
|  AWS CLI  |   [create\-environment\-ec2](https://docs.aws.amazon.com/cli/latest/reference/cloud9/create-environment-ec2.html)   | 
|  AWS SDK for C\+\+  |   [CreateEnvironmentEC2Request](https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_create_environment_e_c2_request.html), [CreateEnvironmentEC2Result](https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_create_environment_e_c2_result.html)   | 
|  AWS SDK for Go  |   [CreateEnvironmentEC2](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.CreateEnvironmentEC2), [CreateEnvironmentEC2Request](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.CreateEnvironmentEC2Request), [CreateEnvironmentEC2WithContext](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.CreateEnvironmentEC2WithContext)   | 
|  AWS SDK for Java  |   [CreateEnvironmentEC2Request](https://docs.aws.amazon.com/sdk-for-java/latest/reference/com/amazonaws/services/cloud9/model/CreateEnvironmentEC2Request.html), [CreateEnvironmentEC2Result](https://docs.aws.amazon.com/sdk-for-java/latest/reference/com/amazonaws/services/cloud9/model/CreateEnvironmentEC2Result.html)   | 
|  AWS SDK for JavaScript  |   [createEnvironmentEC2](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Cloud9.html#createEnvironmentEC2-property)   | 
|  AWS SDK for \.NET  |   [CreateEnvironmentEC2Request](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TCreateEnvironmentEC2Request.html), [CreateEnvironmentEC2Response](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TCreateEnvironmentEC2Response.html)   | 
|  AWS SDK for PHP  |   [createEnvironmentEC2](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-cloud9-2017-09-23.html#createenvironmentec2)   | 
|  AWS SDK for Python \(Boto\)  |   [create\_environment\_ec2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Client.create_environment_ec2)   | 
|  AWS SDK for Ruby  |   [create\_environment\_ec2](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Cloud9/Client.html#create_environment_ec2-instance_method)   | 
|  AWS Tools for Windows PowerShell  |   [New\-C9EnvironmentEC2](https://docs.aws.amazon.com/powershell/latest/reference/items/New-C9EnvironmentEC2.html)   | 
|  AWS Cloud9 API  |   [CreateEnvironmentEC2](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_CreateEnvironmentEC2.html)   | 

**Note**  
If your environment is using a proxy to access the internet, you must provide proxy details to AWS Cloud9 so it can install dependencies\. For more information, see [Notice: Failed to install dependencies for collaboration support](troubleshooting.md#proxy-failed-dependencies)\.