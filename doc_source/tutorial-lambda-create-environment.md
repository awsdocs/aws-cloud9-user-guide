# Step 1: Create and Open the Environment<a name="tutorial-lambda-create-environment"></a>

\(Par of: [AWS Lambda Tutorial for AWS Cloud9](tutorial-lambda.md)\)

In this step, you use the AWS Cloud9 console to create and then open an AWS Cloud9 development environment\.

If you already have an environment, open it, and then skip ahead to [Step 2: Create the Lambda Function and API](tutorial-lambda-create-function.md)\.

In AWS Cloud9, a *development environment* \(or just *environment*\) is a place where you store your development project's files and where you run the tools to develop your applications\. In this tutorial, you create a special kind of environment called an *EC2 environment*\. For this kind of environment, AWS Cloud9 launches and manages a new Amazon EC2 instance running Amazon Linux or Ubuntu Server, creates the environment, and then connects the environment to the newly\-launched instance\. When you open the environment, AWS Cloud9 displays the AWS Cloud9 IDE that enables you to work with the files and tools in that environment\.

1. Sign in to the AWS Cloud9 console as follows:
   + If you're the only individual using your AWS account or you are an IAM user in a single AWS account, go to [https://console\.aws\.amazon\.com/cloud9/](https://console.aws.amazon.com/cloud9/)\.
   + If your organization uses AWS Single Sign\-On \(AWS SSO\), see your AWS account administrator for sign\-in instructions\.
   + If you're using an AWS Educate Starter Account, see [Step 2: Sign In to the AWS Cloud9 Console](setup-student.md#setup-student-sign-in-ide) in *Individual Student Signup*\.
   + If you're a student in a classroom, see your instructor for sign\-in instructions\.

1. After you sign in to the AWS Cloud9 console, in the top navigation bar, choose an AWS Region to create the environment in\. For a list of available AWS Regions, see [AWS Cloud9](https://docs.aws.amazon.com/general/latest/gr/rande.html#cloud9_region) in the *AWS General Reference*\.  
![\[AWS Region selector in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-region.png)

1. If a welcome page is displayed, for **New AWS Cloud9 environment**, choose **Create environment**\. Otherwise, choose **Create environment**\.  
![\[Welcome page in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-welcome-new-env.png)

   Or:  
![\[Create environment button in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-new-env.png)

1. On the **Name environment** page, for **Name**, type a name for your environment\. For this tutorial, use `my-lambda-environment`\.

1. For **Description**, type something about your environment\. For this tutorial, use `This environment is for the AWS Cloud9 tutorial for Lambda.`

1. Choose **Next step**\.

1. On the **Configure settings** page, for **Environment type**, choose **Create a new instance for environment \(EC2\)**\.
**Warning**  
Choosing **Create a new instance for environment \(EC2\)** might result in possible charges to your AWS account for Amazon EC2\.

1. For **Instance type**, leave the default choice\. This choice has relatively low RAM and vCPUs, which is sufficient for this tutorial\.
**Note**  
Choosing instance types with more RAM and vCPUs might result in additional charges to your AWS account for Amazon EC2\.

1. For **Platform**, choose the type of Amazon EC2 instance that AWS Cloud9 will create and then connect to this environment: **Amazon Linux** or **Ubuntu**\.

1. For **Cost\-saving setting**, choose the amount of time until AWS Cloud9 shuts down the Amazon EC2 instance for the environment after all web browser instances that are connected to the IDE for the environment have been closed\. Or leave the default choice\.
**Note**  
Choosing a longer time period might result in more charges to your AWS account\.

1. Choose **Next step**\.

1. On the **Review** page, choose **Create environment**\. Wait while AWS Cloud9 creates your environment\. This can take several minutes\.

After AWS Cloud9 creates your environment, it displays the AWS Cloud9 IDE for the environment\.

If AWS Cloud9 doesn't display the IDE after at least five minutes, there might be a problem with your web browser, your AWS access permissions, the instance, or the associated virtual private cloud \(VPC\)\. For possible fixes, see [Cannot Open an Environment](troubleshooting.md#troubleshooting-env-loading) in *Troubleshooting*\.

## Next Step<a name="tutorial-lambda-create-env-next"></a>

[Step 2: Create the Lambda Function and API](tutorial-lambda-create-function.md)