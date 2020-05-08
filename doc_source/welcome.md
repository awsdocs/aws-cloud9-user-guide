# What Is AWS Cloud9?<a name="welcome"></a>

AWS Cloud9 is an integrated development environment, or *IDE*\.

The AWS Cloud9 IDE offers a rich code\-editing experience with support for several programming languages and runtime debuggers, and a built\-in terminal\. It contains a collection of tools that you use to code, build, run, test, and debug software, and helps you release software to the cloud\.

You access the AWS Cloud9 IDE through a web browser\. You can configure the IDE to your preferences\. You can switch color themes, bind shortcut keys, enable programming language\-specific syntax coloring and code formatting, and more\.

\(**Got it\!** I'm ready to try AWS Cloud9\. [How Do I Get Started?](#how-to-get-started)\)

## How Does AWS Cloud9 Work?<a name="how-does-it-work"></a>

The following diagram shows a high\-level overview of how AWS Cloud9 works\.

From the diagram \(starting at the bottom\), you use the **AWS Cloud9 IDE**, running in a web browser on **your local computer**, to interact with your **AWS Cloud9 environment**\. A computing resource \(for example, an **Amazon EC2 instance** or **your own server**\) connects to that environment\. Finally, your work is stored in an **AWS CodeCommit repository** or **other type of remote repository**\.

![\[Diagram that provides an overview of how AWS Cloud9 works\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/)

### AWS Cloud9 Environments<a name="w30aab7c13b9"></a>

An *AWS Cloud9 environment* is a place where you store your project's files and where you run the tools to develop your applications\.

Using the AWS Cloud9 IDE, you can:
+ Store your project's files locally on the instance or server\.
+ Clone a remote code repository—such as a repo in AWS CodeCommit—into your environment\.
+ Work with a combination of local and cloned files in the environment\.

You can create and switch between multiple environments, with each environment set up for a specific development project\. By storing the environment in the cloud, your projects no longer need to be tied to a single computer or server setup\. This enables you to do things such as easily switch between computers and more quickly onboard developers to your team\.

### Environments and Computing Resources<a name="env-intro"></a>

Behind the scenes, there are a couple of ways you can connect your environments to computing resources:
+ You can instruct AWS Cloud9 to create an Amazon EC2 instance, and then connect the environment to that newly created EC2 instance\. This type of setup is called an *EC2 environment*\.
+ You can instruct AWS Cloud9 to connect an environment to an existing cloud compute instance or to your own server\. This type of setup is called an *SSH environment*\.

EC2 environments and SSH environments have some similarities and some differences\. If you're new to AWS Cloud9, we recommend that you use an EC2 environment because AWS Cloud9 takes care of much of the configuration for you\. As you learn more about AWS Cloud9, and want to understand these similarities and differences better, see [EC2 Environments versus SSH Environments in AWS Cloud9](ec2-env-versus-ssh-env.md)\.

For more information about how AWS Cloud9 works, see these related [videos](additional-info.md#related-videos) and [webpages](additional-info.md#related-web-pages)\.

## What Can I Do with AWS Cloud9? \(A Summary\)<a name="what-can-i-do-summary"></a>

With AWS Cloud9, you can code, build, run, test, debug, and release software in many exciting scenarios and variations\. These include \(but are not limited to\):
+ Working with code in several programming languages and the AWS Cloud Development Kit \(AWS CDK\)\.
+ Working with code in a running Docker container\.
+ Using online code repositories\.
+ Collaborating with others in real time\.
+ Interacting with various database and website technologies\.
+ Targeting AWS Lambda, Amazon API Gateway, and AWS Serverless Applications\.
+ Taking advantage of other AWS products such as Amazon Lightsail, AWS CodeStar, and AWS CodePipeline\.

For a more detailed list, see [What Can I Do with AWS Cloud9?](what-can-i-do.md)

## How Do I Get Started?<a name="how-to-get-started"></a>

To start using AWS Cloud9, follow the steps in [Setting Up AWS Cloud9](setting-up.md), and then go through the [basic tutorial](tutorials-basic.md)\.

## Additional Topics<a name="welcome-additional-info"></a>
+ [What Can I Do with AWS Cloud9?](what-can-i-do.md)
+ [Additional Information about AWS Cloud9](additional-info.md)