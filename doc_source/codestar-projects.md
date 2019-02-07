# Working with AWS CodeStar Projects in the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="codestar-projects"></a>

You can use the AWS Cloud9 IDE to work with code in AWS CodeStar projects\.

AWS CodeStar is a cloud\-based service for creating, managing, and working with software development projects on AWS\. You can quickly develop, build, and deploy applications on AWS with an AWS CodeStar project\. An AWS CodeStar project creates and integrates AWS services for your project development toolchain\. Depending on your choice of AWS CodeStar project template, that toolchain might include source control, build, deployment, virtual servers or serverless resources, and more\. For more information, see the [AWS CodeStar User Guide](https://docs.aws.amazon.com/codestar/latest/userguide/welcome.html)\.

**Note**  
Completing these procedures might result in charges to your AWS account\. These include possible charges for services such as Amazon EC2, AWS CodeStar, and AWS services supported by AWS CodeStar\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/), [AWS CodeStar Pricing](https://aws.amazon.com/codestar/pricing/), and [Cloud Services Pricing](https://aws.amazon.com/pricing/services/)\.  
To use the AWS Cloud9 IDE to work with a newly\-launched Amazon EC2 instance preconfigured with a popular app or framework such as WordPress, MySQL, PHP, Node\.js, Nginx, Drupal, or Joomla, or a Linux distribution such as Ubuntu, Debian, FreeBSD, or openSUSE, you can use Amazon Lightsail along with AWS Cloud9\. To do this, skip the rest of this topic, and see [Working with Amazon Lightsail Instances](lightsail-instances.md) instead\.  
To use the AWS Cloud9 IDE to work with a newly\-launched Amazon EC2 instance running Amazon Linux that contains no sample code, skip the rest of this topic, and see the [IDE Tutorial](tutorial.md) instead\.
+  [Step 1: Prepare to Work with AWS CodeStar Projects](#codestar-projects-setup) 
+  [Step 2: Create a Project in AWS CodeStar](#codestar-projects-create-project) 
+  [Step 3: Create an AWS Cloud9 Development Environment and Connect It to the Project](#codestar-projects-connect-to-project) 

## Step 1: Prepare to Work with AWS CodeStar Projects<a name="codestar-projects-setup"></a>

In this step, you create an AWS CodeStar service role and an Amazon EC2 key pair, so that you can begin creating and working with AWS CodeStar projects\.

If you have used AWS CodeStar before, skip ahead to [Step 2: Create a Project in AWS CodeStar](#codestar-projects-create-project)\.

For this step, follow the instructions in [Setting Up AWS CodeStar](https://docs.aws.amazon.com/codestar/latest/userguide/setting-up.html) in the *AWS CodeStar User Guide*\. Do not create a new AWS account, IAM user, or IAM group as part of those instructions\. Use the ones you created or identified in [Team Setup for AWS Cloud9](setup.md)\. When you finish following those instructions, return to this topic\.

## Step 2: Create a Project in AWS CodeStar<a name="codestar-projects-create-project"></a>

In this step, you create a project in AWS CodeStar\.

If you already have a project in AWS CodeStar you want to use, skip ahead to [Step 3: Create an AWS Cloud9 Development Environment and Connect It to the Project](#codestar-projects-connect-to-project)\.

For this step, follow the instructions in [Create a Project in AWS CodeStar](https://docs.aws.amazon.com/codestar/latest/userguide/how-to-create-project.html) in the *AWS CodeStar User Guide*\. In the AWS CodeStar create project wizard, when you get to the **Set up tools** page or **Connect to your source repository** page, choose **Skip**, and then return to this topic\.

## Step 3: Create an AWS Cloud9 Development Environment and Connect It to the Project<a name="codestar-projects-connect-to-project"></a>

In this step, you create an AWS Cloud9 development environment in the AWS CodeStar or AWS Cloud9 consoles\. You then connect the new environment to an AWS CodeStar project\.

For this step, follow one of the following sets of instructions, depending on the AWS Cloud9 development environment type you want to use and the type of repository where the AWS CodeStar project stores its code\.


****  

|  **Environment type**  |  **Repository type**  |  **Instructions**  | 
| --- | --- | --- | 
|  EC2 environment  |  AWS CodeCommit  |   [Create an AWS Cloud9 Environment for a Project](https://docs.aws.amazon.com/codestar/latest/userguide/setting-up-ide-cloud9.html#setting-up-ide-cloud9-create) in the *AWS CodeStar User Guide*   | 
|  SSH environment  |  AWS CodeCommit  |   [AWS CodeCommit Sample](sample-codecommit.md)   | 
|  EC2 or SSH environment  |  GitHub  |   [Use GitHub with AWS Cloud9](https://docs.aws.amazon.com/codestar/latest/userguide/setting-up-ide-cloud9.html#setting-up-ide-cloud9-github) in the *AWS CodeStar User Guide*   | 