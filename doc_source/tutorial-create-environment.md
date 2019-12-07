# Step 1: Create an Environment<a name="tutorial-create-environment"></a>

\(First step of [Tutorial: Hello AWS Cloud9 \(console\)](tutorial.md)\)

In this step, you use the AWS Cloud9 console to create and then open an AWS Cloud9 development environment\.

**Note**  
If you have already created the environment that you want to use for this tutorial, open that environment and skip ahead to [Step 2: Basic Tour of the IDE](tutorial-tour-ide.md)\.

In AWS Cloud9, a *development environment* \(or just *environment*\) is a place where you store your development project's files and where you run the tools to develop your applications\. In this tutorial, you create a special kind of environment called an *EC2 environment*, and then work with the files and tools in that environment\.

## Create an EC2 Environment with the Console<a name="tutorial-create-environment-console"></a>

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

1. On the **Name environment** page, for **Name**, enter a name for your environment\. For this tutorial, use `my-demo-environment`\.

1. For **Description**, enter something about your environment\. For this tutorial, use `This environment is for the AWS Cloud9 tutorial.`

1. Choose **Next step**\.

1. On the **Configure settings** page, for **Environment type**, choose **Create a new instance for environment \(EC2\)**\.
**Warning**  
Choosing **Create a new instance for environment \(EC2\)** might result in possible charges to your AWS account for Amazon EC2\.

1. For **Instance type**, leave the default choice\. This choice has relatively low RAM and vCPUs, which is sufficient for this tutorial\.
**Warning**  
Choosing instance types with more RAM and vCPUs might result in additional charges to your AWS account for Amazon EC2\.

1. For **Platform**, choose the type of Amazon EC2 instance that you want: **Amazon Linux** or **Ubuntu**\. AWS Cloud9 creates the instance and then connects the environment to it\.

1. Choose a value for **Cost\-saving setting**\. When all web browser instances that are connected to the IDE for the environment are closed, AWS Cloud9 waits this amount of time and then shuts down the Amazon EC2 instance for the environment\. 
**Warning**  
Choosing a longer time period might result in more charges to your AWS account\.

1. Expand **Network settings \(advanced\)**\.

   AWS Cloud9 uses Amazon Virtual Private Cloud \(Amazon VPC\) to communicate with the newly created Amazon EC2 instance\. For this tutorial, we recommend that you don't change the preselected default settings\. With the default settings, AWS Cloud9 attempts to automatically use the default VPC with its single subnet in the same AWS account and AWS Region as the new environment\.

   Find more information about Amazon VPC choices in [Create an EC2 Environment with the Console](create-environment-main.md#create-environment-console) \(step 12\), and in [VPC Settings for AWS Cloud9 Development Environments](vpc-settings.md)\.

1. Choose **Next step**\.

1. On the **Review** page, choose **Create environment**\. Wait while AWS Cloud9 creates your environment\. This can take several minutes\.

After AWS Cloud9 creates your environment, it displays the AWS Cloud9 IDE for the environment\.

If AWS Cloud9 doesn't display the IDE after at least five minutes, there might be a problem with your web browser, your AWS access permissions, the instance, or the associated virtual private cloud \(VPC\)\. For possible fixes, see [Cannot Open an Environment](troubleshooting.md#troubleshooting-env-loading) in *Troubleshooting*\.

## Next Step<a name="tutorial-create-env-next"></a>

[Step 2: Basic Tour of the IDE](tutorial-tour-ide.md)