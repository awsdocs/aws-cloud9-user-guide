# What Is AWS Cloud9?<a name="welcome"></a>

AWS Cloud9 contains a collection of tools that you use to code, build, run, test, debug, and release software in the cloud\. To work with these tools, you use the AWS Cloud9 integrated development environment, or *IDE*\.

You access the AWS Cloud9 IDE through a web browser\. The IDE offers a rich code\-editing experience with support for several programming languages and runtime debuggers, as well as a built\-in terminal\.

You can configure the IDE to your preferences\. You can switch color themes, bind shortcut keys, enable programming language\-specific syntax coloring and code formatting, and more\.

**Topics**
+ [How Do I Get Started?](#how-to-get-started)
+ [What Can I Do with AWS Cloud9?](#what-can-i-do)
+ [How Does AWS Cloud9 Work?](#how-does-it-work)
+ [Pricing](#pricing)
+ [About Cloud9 Versions](#versions)
+ [I Have Additional Questions or Need Help](#questions-help)

## How Do I Get Started?<a name="how-to-get-started"></a>

Start using AWS Cloud9 by following the steps in [Getting Started with AWS Cloud9](get-started.md)\.

## What Can I Do with AWS Cloud9?<a name="what-can-i-do"></a>

Explore the following resources to learn about using AWS Cloud9 for some common scenarios\.

### Topics in This Guide<a name="topics-in-this-guide"></a>


****  

|  **Scenario**  |  **Resources**  | 
| --- | --- | 
|  Create, run, and debug code in AWS Lambda functions, APIs in Amazon API Gateway, and serverless applications\.  |   [AWS Lambda Tutorial for AWS Cloud9](tutorial-lambda.md), [Advanced AWS Lambda Tutorial for AWS Cloud9](tutorial-lambda-advanced.md), and [Working with AWS Lambda Functions in the AWS Cloud9 Integrated Development Environment \(IDE\)](lambda-functions.md)   | 
|  Work with Amazon Lightsail instances preconfigured with popular apps and frameworks such as WordPress, LAMP \(Linux, Apache, MySQL, and PHP\), Node\.js, Nginx, Drupal, and Joomla, as well as Linux distributions such as Amazon Linux, Ubuntu, Debian, FreeBSD, and openSUSE\.  |   [Working with Amazon Lightsail Instances in the AWS Cloud9 Integrated Development Environment \(IDE\)](lightsail-instances.md)   | 
|  Work with code in AWS software development projects and toolchains in AWS CodeStar\.  |   [Working with AWS CodeStar Projects in the AWS Cloud9 Integrated Development Environment \(IDE\)](codestar-projects.md)   | 
|  Work with code in continuous delivery solutions in AWS CodePipeline\.  |   [Working with AWS CodePipeline in the AWS Cloud9 Integrated Development Environment \(IDE\)](codepipeline-repos.md)   | 
|  Automate AWS services by using the AWS CLI and the aws\-shell\.  |   [AWS Command Line Interface and aws\-shell Sample for AWS Cloud9](sample-aws-cli.md)   | 
|  Work with source code repositories in AWS CodeCommit\.  |   [AWS CodeCommit Sample for AWS Cloud9](sample-codecommit.md)   | 
|  Work with source code repositories in GitHub\.  |   [GitHub Sample for AWS Cloud9](sample-github.md)   | 
|  Work with NoSQL databases in Amazon DynamoDB\.  |   [Amazon DynamoDB Sample for AWS Cloud9](sample-dynamodb.md)   | 
|  Work with LAMP \(Linux, Apache HTTP Server, MySQL, and PHP\) stacks\.  |   [LAMP Sample for AWS Cloud9](sample-lamp.md)   | 
|  Work with WordPress websites\.  |   [WordPress Sample for AWS Cloud9](sample-wordpress.md)   | 
|  Work with code for Java and the AWS SDK for Java\.  |   [Java Sample for AWS Cloud9](sample-java.md)   | 
|  Work with code for C\+\+ and the AWS SDK for C\+\+\.  |   [C\+\+ Sample for AWS Cloud9](sample-cplusplus.md)   | 
|  Work with code for Python and the AWS SDK for Python \(Boto\)\.  |   [Python Sample for AWS Cloud9](sample-python.md)   | 
|  Work with code for \.NET Core and the AWS SDK for \.NET\.  |   [\.NET Core Sample for AWS Cloud9](sample-dotnetcore.md)   | 
|  Work with code for Node\.js and the AWS SDK for JavaScript\.  |   [Node\.js Sample for AWS Cloud9](sample-nodejs.md)   | 
|  Work with code for PHP and the AWS SDK for PHP\.  |   [PHP Sample for AWS Cloud9](sample-php.md)   | 
|  Work with code for Ruby and the AWS SDK for Ruby\.  |   [Ruby Sample for AWS Cloud9](sample-ruby.md)   | 
|  Work with code for Go and the AWS SDK for Go\.  |   [Go Sample for AWS Cloud9](sample-go.md)   | 
|  Work with code for TypeScript and the AWS SDK for JavaScript\.  |   [TypeScript Sample for AWS Cloud9](sample-typescript.md)   | 
|  Work with code for the AWS Cloud Development Kit \(AWS CDK\)\.  |   [AWS CDK Sample for AWS Cloud9](sample-cdk.md)   | 
|  Work with code in a running Docker container\.  |   [Docker Sample for AWS Cloud9](sample-docker.md)   | 
|  Invite others to use an environment along with you, in real time and with text chat support\.  |   [Working with Shared Environments in AWS Cloud9](share-environment.md)   | 
|  Work with code for intelligent robotics applications in AWS RoboMaker\.  |   [Developing with AWS Cloud9](https://docs.aws.amazon.com/robomaker/latest/dg/cloud9.html) in the *AWS RoboMaker Developer Guide*   | 

### Related Videos<a name="related-videos"></a>
+  [AWS re:Invent 2017 \- Introducing AWS Cloud9: Werner Vogels Keynote](https://www.youtube.com/watch?v=fwFoU_Wb-fU) \(9 minutes, YouTube website\)
+  [AWS re:Invent Launchpad 2017 \- AWS Cloud9](https://www.youtube.com/watch?v=NNqVBo9k8n4), \(15 minutes, YouTube website\)
+  [Introducing AWS Cloud9 \- AWS Online Tech Talks](https://www.youtube.com/watch?v=FvclLeg2vEQ) \(33 minutes, YouTube website\)
+  [AWS Sydney Summit 2018: AWS Cloud9 and AWS CodeStar](https://www.youtube.com/watch?v=B-nbl0qYsQg) \(25 minutes, YouTube website\)

### Related Web Pages<a name="related-web-pages"></a>
+  [Introducing AWS Cloud9](https://aws.amazon.com/about-aws/whats-new/2017/11/introducing-aws-cloud9/) \(AWS website\)
+  [AWS Cloud9 – Cloud Developer Environments](http://aws.amazon.com/blogs/aws/aws-cloud9-cloud-developer-environments/) \(AWS website\)
+  [AWS Cloud9 Overview](https://aws.amazon.com/cloud9/) \(AWS website\)
+  [AWS Cloud9 Features](https://aws.amazon.com/cloud9/details/) \(AWS website\)
+  [AWS Cloud9 FAQs](https://aws.amazon.com/cloud9/faqs/) \(AWS website\)

## How Does AWS Cloud9 Work?<a name="how-does-it-work"></a>

The following diagram shows a high\-level overview of how AWS Cloud9 works\.

![\[Diagram that provides an overview of how AWS Cloud9 works\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/arch.png)

You use the AWS Cloud9 IDE, running in a web browser on your local computer, to interact with your environment\. A cloud compute instance \(for example an Amazon EC2 instance\) or your own server connects to the environment\. An *environment* is a place where you store your project's files and where you run the tools to develop your apps\.

You use the AWS Cloud9 IDE to work with files in the environment\. You can:
+ Store these files locally on the instance or server\.
+ Clone a remote code repository—such as a repo in AWS CodeCommit—into your environment\.
+ Work with a combination of local and cloned files in the environment\.

In the background, you can instruct AWS Cloud9 to have Amazon EC2 create an Amazon EC2 instance and then connect the environment to the newly\-created instance\. We call this type of setup an *EC2 environment*\. You can also instruct AWS Cloud9 to connect an environment to an existing cloud compute instance or your own server\. We call this type of setup an *SSH environment*\.

Here are the key similarities and differences between EC2 environments and SSH environments\.


****  

|  **EC2 environments**  |  **SSH environments**  | 
| --- | --- | 
|  AWS Cloud9 creates an associated Amazon EC2 instance and manages that instance's lifecycle \(for example, start, stop, and terminate\)\.  |  You use an existing cloud compute instance or your own server\. You manage that instance's or server's lifecycle\.  | 
|  The instance runs on Amazon Linux or Ubuntu Server\.  |  You can use any cloud compute instance that runs Linux, or your own server running Linux\.  | 
|  AWS Cloud9 automatically sets up the instance to start working with AWS Cloud9\.  |  You must manually configure the instance or your own server to work with AWS Cloud9\.  | 
|  AWS Cloud9 automatically sets up the AWS Command Line Interface \(AWS CLI\) on the instance for you to start using\.  |  If you want to use the AWS CLI on the instance or your own server, you must set it up yourself\.  | 
|  The instance has access to hundreds of useful packages, with some common packages already installed and configured, such as Git, Docker, Node\.js, and Python\.  |  You might need to download, install, and configure additional packages to complete common tasks\.  | 
|  You maintain the instance, for example by periodically applying system updates\.  |  You maintain the instance or your own server\.  | 
|  When you delete the environment, AWS Cloud9 automatically terminates the associated instance\.  |  When you delete the environment, the instance or your own server remains\.  | 

You can create and switch between multiple environments, with each environment set up for a specific development project\. By storing the environment in the cloud, your projects no longer need to be tied to a single computer or server setup\. This enables you to do things such as easily switch between computers and more quickly onboard developers to your team\.

## Pricing<a name="pricing"></a>

There is no additional charge for AWS Cloud9\. If you use an Amazon EC2 instance for your AWS Cloud9 development environment, you pay only for the compute and storage resources \(for example, an Amazon EC2 instance, an Amazon EBS volume\) that are used to run and store your code\. You can also connect your environment to an existing Linux server \(for example, an on\-premises server\) through SSH for no additional charge\.

You only pay for what you use, as you use it; there are no minimum fees and no upfront commitments\. You are charged the normal AWS rates for any AWS resources \(for example, Lambda functions\) that you create or use within your environment\.

New AWS customers who are eligible for the AWS Free Tier can use AWS Cloud9 for free\. If your environment makes use of resources beyond the AWS Free Tier, you are charged the normal AWS rates for those resources\.

For more information, see [AWS Cloud9 Pricing](https://aws.amazon.com/cloud9/pricing/)\. For more details on AWS service pricing, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/), [Amazon EBS Pricing](https://aws.amazon.com/ebs/pricing/), [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/), and [AWS Pricing](https://aws.amazon.com/pricing/)\. For more details on the AWS Free Tier, see [Using the AWS Free Tier](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-free-tier.html) and [Tracking Your Free Tier Usage](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/tracking-free-tier-usage.html) in the *AWS Billing and Cost Management User Guide*\.

For education pricing information, explore the [AWS Educate](https://aws.amazon.com/education/awseducate/) program\.

## About Cloud9 Versions<a name="versions"></a>

There are currently two versions of Cloud9 available: c9\.io and AWS Cloud9\. This *AWS Cloud9 User Guide* only covers AWS Cloud9\.

c9\.io is available only to existing c9\.io users\. For more information, see [Cloud9 now runs on and integrates with AWS](https://c9.io/announcement) on the c9\.io website\.

c9\.io and AWS Cloud9 are not interoperable\. You can't use an account or workspace in c9\.io with an account or environment in AWS Cloud9\.

## I Have Additional Questions or Need Help<a name="questions-help"></a>

To ask questions or seek help from the AWS Cloud9 community, see the [AWS Cloud9 Discussion Forum](https://forums.aws.amazon.com/forum.jspa?forumID=268)\. \(When you enter this forum, AWS might require you to sign in\.\)

See also our [frequently asked questions](https://aws.amazon.com/cloud9/faqs/) \(FAQs\), or [contact us](https://aws.amazon.com/contact-us/) directly\.