# Creating an EC2 Environment<a name="create-environment-main"></a>

**Note**  
Completing this procedure might result in charges to your AWS account\. These include possible charges for Amazon EC2\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/)\.

In this procedure, AWS Cloud9 creates an EC2 environment, creates a new Amazon EC2 instance, and then connects the environment to this newly\-created instance\. AWS Cloud9 manages this instance's lifecycle, including starting, stopping, and restarting the instance as needed\. If you ever delete this environment, AWS Cloud9 automatically terminates this instance\.

You can create an AWS Cloud9 EC2 development environment with the [AWS Cloud9 console](#create-environment-console) or with [code](#create-environment-code)\.

## Prerequisites<a name="create-env-ec2-prereq"></a>

Complete the steps in [Setting Up AWS Cloud9](setting-up.md) so that you can sign in to the AWS Cloud9 console and create environments\.

## Create an EC2 Environment with the Console<a name="create-environment-console"></a>

1. Sign in to the AWS Cloud9 console as follows:
   + If you're the only individual using your AWS account or you are an IAM user in a single AWS account, go to [https://console\.aws\.amazon\.com/cloud9/](https://console.aws.amazon.com/cloud9/)\.
   + If your organization uses AWS Single Sign\-On \(AWS SSO\), see your AWS account administrator for sign\-in instructions\.
   + If you're using an AWS Educate Starter Account, see [Step 2: Sign In to the AWS Cloud9 Console](setup-student.md#setup-student-sign-in-ide) in *Individual Student Signup*\.
   + If you're a student in a classroom, see your instructor for sign\-in instructions\.

1. After you sign in to the AWS Cloud9 console, in the top navigation bar, choose an AWS Region to create the environment in\. For a list of available AWS Regions, see [AWS Cloud9](https://docs.aws.amazon.com/general/latest/gr/rande.html#cloud9_region) in the *AWS General Reference*\.  
![\[AWS Region selector in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-region.png)

1. Choose the large **Create environment** button in one of the locations shown below\.

   If you have no AWS Cloud9 environments yet, the button is shown on a welcome page\.  
![\[Welcome page in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-welcome-new-env.png)

   If you already have AWS Cloud9 environments, the button is shown as follows\.  
![\[Create environment button in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-new-env.png)

1. On the **Name environment** page, for **Name**, enter a name for your environment\.

1. To add a description to your environment, enter it in **Description**\.

1. Choose **Next step**\.

1. On the **Configure settings** page, for **Environment type**, choose **Create a new instance for environment \(EC2\)**\.
**Warning**  
Choosing **Create a new instance for environment \(EC2\)** might result in possible charges to your AWS account for Amazon EC2\.

1. For **Instance type**, choose an instance type with the amount of RAM and vCPUs you think you need for the kinds of tasks you want to do\.
**Warning**  
Choosing instance types with more RAM and vCPUs might result in additional charges to your AWS account for Amazon EC2\.

1. For **Platform**, choose the type of Amazon EC2 instance that you want: **Amazon Linux** or **Ubuntu**\. AWS Cloud9 creates the instance and then connects the environment to it\.

1. Choose a value for **Cost\-saving setting**\. When all web browser instances that are connected to the IDE for the environment are closed, AWS Cloud9 waits this amount of time and then shuts down the Amazon EC2 instance for the environment\. 
**Warning**  
Choosing a longer time period might result in more charges to your AWS account\.

1. Expand **Network settings \(advanced\)**\.

1. AWS Cloud9 uses Amazon Virtual Private Cloud \(Amazon VPC\) to communicate with the newly created Amazon EC2 instance\. Depending on how Amazon VPC is set up, do one of the following\.  
****    
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment-main.html)  
****    
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment-main.html)

   For more information about these choices, see [VPC Settings for AWS Cloud9 Development Environments](vpc-settings.md)\.

1. Choose **Next step**\.

1. On the **Review** page, choose **Create environment**\. Wait while AWS Cloud9 creates your environment\. This can take several minutes\.

After AWS Cloud9 creates your environment, it displays the AWS Cloud9 IDE for the environment\.

If AWS Cloud9 doesn't display the IDE after at least five minutes, there might be a problem with your web browser, your AWS access permissions, the instance, or the associated virtual private cloud \(VPC\)\. For possible fixes, see [Cannot Open an Environment](troubleshooting.md#troubleshooting-env-loading) in *Troubleshooting*\.

## Creating an EC2 Environment with Code<a name="create-environment-code"></a>

To use code to create an EC2 environment in AWS Cloud9, call the AWS Cloud9 create EC2 environment operation, as follows\.

**Note**  
Currently, you cannot use code to create an Ubuntu Server\-based EC2 environment, for example by using the AWS CLI, AWS CloudFormation, the AWS SDKs, the Tools for Windows PowerShell, or the AWS Cloud9 API\. Currently, you can only use code to create an EC2 environment that is connected to Amazon Linux\. Using code to create an Ubuntu Server\-based EC2 environment is expected in the future\.


****  

|  |  | 
| --- |--- |
|  AWS CLI  |   [create\-environment\-ec2](https://docs.aws.amazon.com/cli/latest/reference/cloud9/create-environment-ec2.html)   | 
|  AWS SDK for C\+\+  |   [CreateEnvironmentEC2Request](https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_create_environment_e_c2_request.html), [CreateEnvironmentEC2Result](https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_create_environment_e_c2_result.html)   | 
|  AWS SDK for Go  |   [CreateEnvironmentEC2](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.CreateEnvironmentEC2), [CreateEnvironmentEC2Request](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.CreateEnvironmentEC2Request), [CreateEnvironmentEC2WithContext](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.CreateEnvironmentEC2WithContext)   | 
|  AWS SDK for Java  |   [CreateEnvironmentEC2Request](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/CreateEnvironmentEC2Request.html), [CreateEnvironmentEC2Result](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/CreateEnvironmentEC2Result.html)   | 
|  AWS SDK for JavaScript  |   [createEnvironmentEC2](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Cloud9.html#createEnvironmentEC2-property)   | 
|  AWS SDK for \.NET  |   [CreateEnvironmentEC2Request](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TCreateEnvironmentEC2Request.html), [CreateEnvironmentEC2Response](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TCreateEnvironmentEC2Response.html)   | 
|  AWS SDK for PHP  |   [createEnvironmentEC2](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-cloud9-2017-09-23.html#createenvironmentec2)   | 
|  AWS SDK for Python \(Boto\)  |   [create\_environment\_ec2](http://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloud9.html#Cloud9.Client.create_environment_ec2)   | 
|  AWS SDK for Ruby  |   [create\_environment\_ec2](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Cloud9/Client.html#create_environment_ec2-instance_method)   | 
|  AWS Tools for Windows PowerShell  |   [New\-C9EnvironmentEC2](https://docs.aws.amazon.com/powershell/latest/reference/items/New-C9EnvironmentEC2.html)   | 
|  AWS Cloud9 API  |   [CreateEnvironmentEC2](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_CreateEnvironmentEC2.html)   | 