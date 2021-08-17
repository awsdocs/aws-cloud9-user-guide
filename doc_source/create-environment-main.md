# Creating an EC2 Environment<a name="create-environment-main"></a>

**Note**  
Completing this procedure might result in charges to your AWS account\. These include possible charges for Amazon EC2\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/)\.

In this procedure, AWS Cloud9 creates an EC2 environment, creates a new Amazon EC2 instance, and then connects the environment to this newly created instance\. AWS Cloud9 manages the lifecycle of this instance, including starting, stopping, and restarting the instance as needed\. If you ever delete this environment, AWS Cloud9 automatically terminates this instance\.

You can create an AWS Cloud9 EC2 development environment with the [AWS Cloud9 console](#create-environment-console) or with [code](#create-environment-code)\.

## Prerequisites<a name="create-env-ec2-prereq"></a>

Complete the steps in [Setting up AWS Cloud9](setting-up.md) so that you can sign in to the AWS Cloud9 console and create environments\.

## Create an EC2 environment with the console<a name="create-environment-console"></a>

1. Sign in to the AWS Cloud9 console:
   + If you're the only one that using your AWS account or you're an IAM user in a single AWS account, go to [https://console\.aws\.amazon\.com/cloud9/](https://console.aws.amazon.com/cloud9/)\.
   + If your organization uses AWS Single Sign\-On \(AWS SSO\), ask your AWS account administrator for sign\-in instructions\.
   + If you're using an AWS Educate Starter Account, see [Use an AWS Educate Starter Account to sign in to the AWS Cloud9 console](setup-student.md#setup-student-sign-in-ide) in *Individual Student Signup*\.
   + If you're a student in a classroom, ask your instructor for sign\-in instructions\.

1. After you sign in to the AWS Cloud9 console, in the top navigation bar, choose an AWS Region to create the environment in\. For a list of available AWS Regions, see [AWS Cloud9](https://docs.aws.amazon.com/general/latest/gr/rande.html#cloud9_region) in the *AWS General Reference*\.  
![\[AWS Region selector in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-region.png)

1. Choose the large **Create environment** button in one of the locations shown\.

   If you have no AWS Cloud9 environments yet, the button is shown on a welcome page\.  
![\[Welcome page in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-welcome-new-env.png)

   If you already have AWS Cloud9 environments, the button is shown as follows\.  
![\[Create environment button in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-new-env.png)

1. On the **Name environment** page, for **Name**, enter a name for your environment\.

1. To add a description to your environment, enter it in **Description**\.

1. Choose **Next step**\.

1. On the **Configure settings** page, for **Environment type**, choose one of the following options to create an EC2 backed environment:
   + **Create a new EC2 instance for environment \(direct access\)** – Launches an Amazon EC2 instance that AWS Cloud9 can connect to directly over SSH\.
   + **Create a new no\-ingress EC2 instance for environment \(access via Systems Manager\)** – Launches an Amazon EC2 instance that doesn't require any open inbound ports\. AWS Cloud9 connects to the instance through [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)\.
     + If you select the **access via Systems Manager** option, a service role and an IAM instance profile are automatically created to allow Systems Manager to interact with the EC2 instance on your behalf\. You can view the names of both in the **Service role and instance profile for Systems Manager access** section further down the interface\. For more information, see [Accessing no\-ingress EC2 instances with AWS Systems Manager](ec2-ssm.md)\. 
**Warning**  
Creating an EC2 instance for your environment might result in possible charges to your AWS account for Amazon EC2\. There is no additional cost to use Systems Manager to manage connections to your EC2 instance\.

1. For **Instance type**, choose an instance type with the amount of RAM and vCPUs you think you need for the kinds of tasks you want to do\.
**Warning**  
Choosing instance types with more RAM and vCPUs might result in additional charges to your AWS account for Amazon EC2\.

1. For **Platform**, choose the type of Amazon EC2 instance that you want: **Amazon Linux 2**, **Amazon Linux**, or **Ubuntu**\. AWS Cloud9 creates the instance and then connects the environment to it\.
**Important**  
We recommend that you choose the **Amazon Linux 2** option for your EC2 environment\. As well as providing a secure, stable, and high\-performance runtime environment, Amazon Linux 2 AMI includes long\-term support through 2023\.  
Standard support for the previous version of Amazon Linux AMI discontinued on December 31, 2020\. Now this version only receives maintenance support\. For more information, see the [Amazon Linux 2 page](https://aws.amazon.com/amazon-linux-2/)\.

1. Choose a value for **Cost\-saving setting**\. When all web browser instances that are connected to the IDE for the environment are closed, AWS Cloud9 waits the amount of time specified and then shuts down the Amazon EC2 instance for the environment\. 
**Warning**  
Choosing a longer time period might result in more charges to your AWS account\.

1. Expand **Network settings \(advanced\)**\.

1. <a name="create-environment-vpc-step"></a>AWS Cloud9 uses Amazon Virtual Private Cloud \(Amazon VPC\) to communicate with the newly created Amazon EC2 instance\. Depending on how Amazon VPC is set up, follow one of the following set of instructions\.  
****    
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment-main.html)
**Important**  
If you selected **Create a new no\-ingress EC2 instance for environment \(access via Systems Manager\)**, you can launch your instance into a public or private subnet\.  
**Public subnet**: Attach an internet gateway to it to allow the instance SSM agent to communicate with Systems Manager\.
**Private subnet**: Create a NAT gateway to enable the instance to communicate with the internet and other AWS services\.
You should also be aware that currently you can't use [AWS managed temporary credentials](security-iam.md#auth-and-access-control-temporary-managed-credentials) to allow the EC2 environment to access an AWS service on behalf of an AWS entity \(an IAM user, for example\)\.  
 For more information on configuring subnets, see [VPC settings for AWS Cloud9 Development Environments](vpc-settings.md)\.  
****    
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment-main.html)

   For more information about these choices, see [VPC settings for AWS Cloud9 Development Environments](vpc-settings.md)\.

1. Add up to 50 tags by supplying a **Key** and a **Value** for each tag\. The tags are attached to the AWS Cloud9 environment as resource tags, and are propagated to the following underlying resources: the AWS CloudFormation stack, the Amazon EC2 instance, and Amazon EC2 security groups\. You can find information about tags in [Control Access Using AWS Resource Tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) in the *[IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)*\. Also see the [advanced information](tags.md) about tags\.
**Warning**  
If you update these tags after you create them, the changes are not automatically propagated to the underlying resources\. For more information, see [Propagating tag updates to underlying resources](tags.md#tags-propagate) in the advanced information about [tags](tags.md)\.

1. Choose **Next step**\.

1. On the **Review** page, choose **Create environment**\. Wait while AWS Cloud9 creates your environment\. This can take several minutes\.
**Note**  
If account creation fails, a banner is displayed at the top of the console page\. Additionally, the card for the environment, if it exists, indicates that environment creation failed\.

After AWS Cloud9 creates your environment, it displays the AWS Cloud9 IDE for the environment\.

If AWS Cloud9 doesn't display the IDE after at least five minutes, there might be a problem with your web browser, your AWS access permissions, the instance, or the associated virtual private cloud \(VPC\)\. For possible fixes, see [Cannot open an environment](troubleshooting.md#troubleshooting-env-loading) in *Troubleshooting*\.

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