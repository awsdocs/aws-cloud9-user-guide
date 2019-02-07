# Creating an Environment in AWS Cloud9<a name="create-environment"></a>

To create an AWS Cloud9 development environment, follow one of these sets of procedures, depending on how you plan to use AWS Cloud9\.


****  

|  | 
| --- |
|  If you're not sure what to choose, we recommend [creating an EC2 environment](#create-environment-main)\. Creating an EC2 environment is the easiest option\. AWS Cloud9 automatically creates and sets up a new Amazon EC2 instance in your AWS account\. AWS Cloud9 then automatically connects that new instance to the environment for you\.  | 


****  

|  **Source code provided by**  |  **Development environment host provided by**  |  **Follow these procedures**  | 
| --- | --- | --- | 
|  You  |  AWS Cloud9  |  This topic \([create an EC2 environment](#create-environment-main)\)  | 
|  You  |  You  |  This topic \([create an SSH environment](#create-environment-ssh)\)  | 
|   [Amazon Lightsail](https://aws.amazon.com/lightsail) or you  |  You, by using Lightsail  |   [Working with Amazon Lightsail Instances](lightsail-instances.md)   | 
|   [AWS CodeStar](https://aws.amazon.com/codestar) or you  |  AWS Cloud9, by using AWS CodeStar  |   [Working with AWS CodeStar Projects](codestar-projects.md)   | 
|  You, by using [AWS CodePipeline](https://aws.amazon.com/codepipeline)   |  AWS Cloud9 or you  |  This topic \(create an [EC2](#create-environment-main) or [SSH](#create-environment-ssh) environment\), and then see [Working with AWS CodePipeline](codepipeline-repos.md)   | 
|  You, by using [AWS CodeCommit](https://aws.amazon.com/codecommit)   |  AWS Cloud9 or you  |   [AWS CodeCommit Sample](sample-codecommit.md)   | 
|  You, by using [GitHub](https://github.com/)   |  AWS Cloud9 or you  |  This topic \(create an [EC2](#create-environment-main) or [SSH](#create-environment-ssh) environment\), and then see the [GitHub Sample](sample-github.md)   | 

## Creating an EC2 Environment<a name="create-environment-main"></a>

**Note**  
Completing this procedure might result in charges to your AWS account\. These include possible charges for Amazon EC2\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/)\.

In this procedure, AWS Cloud9 creates an EC2 environment, creates a new Amazon EC2 instance, and then connects the environment to this newly\-created instance\. AWS Cloud9 manages this instance's lifecycle, including starting, stopping, and restarting the instance as needed\. If you ever delete this environment, AWS Cloud9 automatically terminates this instance\.

You can create an AWS Cloud9 EC2 development environment with the [AWS Cloud9 console](#create-environment-console) or with [code](#create-environment-code)\.

### Creating an EC2 Environment with the Console<a name="create-environment-console"></a>

1. Make sure you completed the steps in [Getting Started](get-started.md) first, so that you can sign in to the AWS Cloud9 console and create environments\.

1. Sign in to the AWS Cloud9 console as follows:
   + If you're the only individual using your AWS account or you are an IAM user in a single AWS account, go to [https://console\.aws\.amazon\.com/cloud9/](https://console.aws.amazon.com/cloud9/)\.
   + If your organization uses AWS Single Sign\-On \(SSO\), see your AWS account administrator for sign\-in instructions\.
   + If you're using an AWS Educate Starter Account, see [Step 2: Sign in to the AWS Cloud9 Console](setup-student.md#setup-student-sign-in-ide) in *Individual Student Signup*\.
   + If you're a student in a classroom, see your instructor for sign\-in instructions\.

1. After you sign in to the AWS Cloud9 console, in the top navigation bar, choose an AWS Region to create the environment in\. For a list of available AWS Regions, see [AWS Cloud9](https://docs.aws.amazon.com/general/latest/gr/rande.html#cloud9_region) in the *Amazon Web Services General Reference*\.  
![\[AWS Region selector in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-region.png)

1. If a welcome page is displayed, for **New AWS Cloud9 environment**, choose **Create environment**\. Otherwise, choose **Create environment**\.  
![\[Choosing the Next step button if welcome page is displayed\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-welcome-new-env.png)

   Or:  
![\[Choosing the Create environment button if welcome page is not displayed\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-new-env.png)

1. On the **Name environment** page, for **Name**, type a name for your environment\.

1. To add a description to your environment, type it in **Description**\.

1. Choose **Next step**\.

1. On the **Configure settings** page, for **Environment type**, choose **Create a new instance for environment \(EC2\)**\.

1. For **Instance type**, choose an instance type with the amount of RAM and vCPUs you think you need for the kinds of tasks you want to do\. Or leave the default choice\.
**Note**  
Choosing instance types with more RAM and vCPUs might result in additional charges to your AWS account for Amazon EC2\.

1. For **Cost\-saving setting**, choose the amount of time until AWS Cloud9 shuts down the Amazon EC2 instance for the environment after all web browser instances that are connect to the IDE for the environment have been closed\. Or leave the default choice\.
**Note**  
Choosing a shorter time period might result in fewer charges to your AWS account\. Likewise, choosing a longer time might result in more charges\.

1. Expand **Network settings \(advanced\)**\.

1. AWS Cloud9 uses Amazon Virtual Private Cloud \(Amazon VPC\) to communicate with the Amazon EC2 instance that AWS Cloud9 creates for this environment\. Depending on how Amazon VPC is set up, do one of the following\.  
****    
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment.html)  
****    
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment.html)

   For more information about these choices, see [Amazon VPC Settings](vpc-settings.md)\.

1. Choose **Next step**\.

1. On the **Review** page, choose **Create environment**\. Wait while AWS Cloud9 creates your environment\. This can take several minutes\.

After AWS Cloud9 creates your environment, it displays the AWS Cloud9 IDE for the environment\.

If AWS Cloud9 doesn't display the IDE after at least five minutes, there might be a problem with your web browser, your AWS access permissions, the instance, or the associated virtual private cloud \(VPC\)\. For possible fixes, see [Cannot Open an Environment](troubleshooting.md#troubleshooting-env-loading) in *Troubleshooting*\.

### Creating an EC2 Environment with Code<a name="create-environment-code"></a>

To use code to create an EC2 environment in AWS Cloud9, call the AWS Cloud9 create EC2 environment operation, as follows\.

**Note**  
Make sure you completed the steps in [Express Setup](setup-express.md) or [Team Setup](setup.md) first, so that you can create environments\.


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
|  AWS SDK for Python \(Boto\)  |   [create\_environment\_ec2](https://boto3.readthedocs.io/en/latest/reference/services/cloud9.html#Cloud9.Client.create_environment_ec2)   | 
|  AWS SDK for Ruby  |   [create\_environment\_ec2](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Cloud9/Client.html#create_environment_ec2-instance_method)   | 
|  AWS Tools for Windows PowerShell  |   [New\-C9EnvironmentEC2](https://docs.aws.amazon.com/powershell/latest/reference/items/New-C9EnvironmentEC2.html)   | 
|  AWS Cloud9 API  |   [CreateEnvironmentEC2](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_CreateEnvironmentEC2.html)   | 

## Creating an SSH Environment<a name="create-environment-ssh"></a>

You create an AWS Cloud9 SSH development environment with the AWS Cloud9 console\. \(You cannot create an SSH environment with code\.\)

### Prerequisites<a name="prerequisites"></a>
+ Make sure you completed the steps in [Express Setup](setup-express.md) or [Team Setup](setup.md), so that you can sign in to the AWS Cloud9 console and create environments\.
+ Identify an existing cloud compute instance \(for example an Amazon EC2 instance in your AWS account\), or your own server, that you want AWS Cloud9 to connect to the environment\.
+ Make sure that the existing instance or your own server meets all of the [SSH Host Requirements](ssh-settings.md#ssh-settings-requirements)\. This includes having specific versions of Python, Node\.js, and other components installed; setting specific permissions on the directory that you want AWS Cloud9 to start from after login; and setting up any associated Amazon Virtual Private Cloud\.

### Create the SSH Environment<a name="create-the-envsshtitle"></a>

1. Make sure you completed the preceding prerequisites\.

1. Connect to your existing instance or your own server by using an SSH client, if you are not already connected to it\. You must do this so that you can add the necessary public SSH key value to the instance or server, as described later in this procedure\.
**Note**  
To connect to an existing AWS cloud compute instance, see one or more of the following resources:  
For Amazon EC2, see [Connect to Your Linux Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html) in the *Amazon EC2 User Guide for Linux Instances*\.
For Amazon Lightsail, see [Connect to your Linux/Unix\-based Lightsail instance](https://lightsail.aws.amazon.com/ls/docs/how-to/article/lightsail-how-to-connect-to-your-instance-virtual-private-server) in the *Amazon Lightsail Documentation*\.
For AWS Elastic Beanstalk, see [Listing and Connecting to Server Instances](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.ec2connect.html) in the *AWS Elastic Beanstalk Developer Guide*\.
For AWS OpsWorks, see [Using SSH to Log In to a Linux Instance](https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-ssh.html) in the *AWS OpsWorks User Guide*\.
For other AWS services, see the service's [documentation](https://aws.amazon.com/documentation/)\.
To connect to your own server, you could search the internet using a phrase such as "connect to a server by using the ssh command" \(from macOS or Linux\) or "connect to a server by using PuTTY" \(from Windows\)\.

1. Sign in to the AWS Cloud9 console, at [https://console\.aws\.amazon\.com/cloud9/](https://console.aws.amazon.com/cloud9/)\.

1. After you sign in to the AWS Cloud9 console, in the top navigation bar, choose an AWS Region to create the environment in\. For a list of available AWS Regions, see [AWS Cloud9](https://docs.aws.amazon.com/general/latest/gr/rande.html#cloud9_region) in the *Amazon Web Services General Reference*\.  
![\[AWS Region selector in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-region.png)

1. If a welcome page is displayed, for **New AWS Cloud9 environment**, choose **Create environment**\. Otherwise, choose **Create environment**\.  
![\[Choosing the Next step button if welcome page is displayed\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-welcome-new-env.png)

   Or:  
![\[Choosing the Create environment button if welcome page is not displayed\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-new-env.png)

1. On the **Name environment** page, for **Name**, type a name for your environment\.

1. To add a description to your environment, type it in **Description**\.

1. Choose **Next step**\.

1. For **Environment type:**, choose **Connect and run in remote server \(SSH\)**\.

1. For **User**, type the login name you used to connect to the instance or server earlier in this procedure\. For example, for an AWS cloud compute instance, it might be `ec2-user`, `ubuntu`, or `root`\.
**Note**  
For best results, we recommend that the login name is associated with administrative privileges or an administrator user on the instance or server\. Specifically, this login name should own the Node\.js installation on the instance or server\. To check this, from your instance's or server's terminal, run the command ** `ls -l $(which node)` ** \(or ** `ls -l $(nvm which node)` ** if you're using nvm\)\. This command displays the Node\.js installation's owner's name \(along with the installation's permissions, group name, and location\)\.

1. For **Host**, type the public IP address \(preferred\) or the hostname of the instance or server\.

1. For **Port**, type the port that you want AWS Cloud9 to use to try to connect to the instance or server, or leave the default port\.

1. To specify the path to the directory on the instance or server that you want AWS Cloud9 to start from after login, which you identified earlier in this procedure's prerequisites, expand **Advanced settings**, and then type the path in **Environment path**\. If you leave this blank, AWS Cloud9 uses the directory that your instance or server typically starts with after login\. This is usually a home or default directory\.

1. To specify the path to the Node\.js binary on the instance or server, expand **Advanced settings**, and then type the path in **Node\.js binary path**\. To get the path, you can run the command ** `which node` ** \(or ** `nvm which node` ** if you're using nvm\) on your instance or server\. For example, the path might be `/usr/bin/node`\. If you leave this blank, AWS Cloud9 will try to guess where the Node\.js binary is when it tries to connect\.

1. To specify a jump host that the instance or server uses, expand **Advanced settings**, and then type information about the jump host in **SSH jump host**, using the format `USER_NAME@HOSTNAME:PORT_NUMBER` \(for example, `ec2-user@:ip-192-0-2-0:22`\)

   The jump host must meet the following requirements\.
   + It must be reachable over the public Internet using SSH\.
   + It must allow inbound access by any IP address over the specified port\.
   + The public SSH key value that was copied into the `~/.ssh/authorized_keys` file on the existing instance or server must also be copied into the `~/.ssh/authorized_keys` file on the jump host\.

1. Choose **Copy key to clipboard**\. \(This is between **View public SSH key** and **Advanced settings**\.\) Paste the public SSH key value that was copied, into the `~/.ssh/authorized_keys` file on the existing instance or server that you connected to earlier in this procedure\. \(`~` represents the home directory for the login name that you specified for **User** earlier in this procedure\.\)
**Note**  
To see the public SSH key value that was copied, expand **View public SSH key**\.

1. Choose **Next step**\.

1. On the **Review** page, choose **Create environment**\. Wait while AWS Cloud9 creates your environment\. This can take several minutes\.

If AWS Cloud9 doesn't display the IDE after at least five minutes, there might be a problem with your web browser, your AWS access permissions, the instance, or the associated network\. For possible fixes, see [Cannot Open an Environment](troubleshooting.md#troubleshooting-env-loading) in *Troubleshooting*\.