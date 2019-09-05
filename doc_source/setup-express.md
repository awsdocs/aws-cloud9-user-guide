# Individual User Setup for AWS Cloud9<a name="setup-express"></a>

This topic explains how to set up to use AWS Cloud9 as the only individual in your AWS account, and you are not a student\. To set up to use AWS Cloud9 for any other usage pattern, see [Setting Up AWS Cloud9](setting-up.md) for the correct instructions\. To learn about who qualifies as a student, see [Who can join AWS Educate](https://www.awseducate.com/faqs#fa0Po00000043dVcEAI) on the *AWS Educate Frequently Asked Questions* website\.

To use AWS Cloud9 as the only individual in your AWS account, create an AWS account if you don't already have one, and then sign in to the AWS Cloud9 console\.

## Step 1: Create an AWS Account<a name="setup-express-create-account"></a>

If you already have an AWS account, skip ahead to [Step 2: Sign in to the AWS Cloud9 Console with the AWS Account Root User](#setup-express-sign-in-ide)\.

To watch a 4\-minute video related to the following procedure, see [Creating an Amazon Web Services Account](https://www.youtube.com/watch?v=WviHsoz8yHk) on the YouTube website\.

**To create an AWS account**

1. Go to [https://aws\.amazon\.com](https://aws.amazon.com)\.

1. Choose **Sign In to the Console**\.

1. Choose **Create a new AWS account**\.

1. Complete the process by following the on\-screen directions\. This includes giving AWS your email address and credit card information\. You must also use your phone to enter a code that AWS gives you\.

After you finish creating the account, AWS will send you a confirmation email\. Do not go to the next step until you get this confirmation\.

## Step 2: Sign In to the AWS Cloud9 Console with the AWS Account Root User<a name="setup-express-sign-in-ide"></a>

After you complete the previous step, you're ready to sign in to the AWS Cloud9 console with an AWS account root user and start using AWS Cloud9\.

1. Open the AWS Cloud9 console, at [https://console\.aws\.amazon\.com/cloud9/](https://console.aws.amazon.com/cloud9/)\.

1. Enter the email address for your AWS account, and then choose **Next**\.
**Note**  
If an email address is already displayed and it's the wrong one, choose **Sign in to a different account**\. Enter the correct email address, and then choose **Next**\.

1. Enter the password for your AWS account, and then choose **Sign In**\.

The AWS Cloud9 console is displayed, and you can now start using AWS Cloud9\.

**Important**  
Although you can sign in to the AWS Cloud9 console with the email address and password that you used when you created your AWS account \(we call this an AWS account *root user*\), this isn't an AWS security best practice\. In the future, we recommend that you sign in as an administrator user in AWS Identity and Access Management \(IAM\) in your AWS account instead\. For more information, see [Creating Your First IAM Admin User and Group](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html) in the *IAM User Guide* and [AWS Tasks That Require AWS Account Root User Credentials](https://docs.aws.amazon.com/general/latest/gr/aws_tasks-that-require-root.html) in the *Amazon Web Services General Reference*\.

## Next Steps<a name="setup-express-next-steps"></a>


****  

|  **Task for learning**  |  **See this topic**  | 
| --- | --- | 
|  Learn how to use the AWS Cloud9 IDE\.  |   [Getting Started: Basic Tutorials](tutorials-basic.md) and [Working with the IDE](ide.md)   | 


****  

|  **More advanced task**  |  **See this topic**  | 
| --- | --- | 
|  Create an AWS Cloud9 development environment, and then use the AWS Cloud9 IDE to work with code in your new environment\.  |   [Creating an Environment](create-environment.md)   | 
|  Invite others to use your new environment along with you, in real time and with text chat support\.  |   [Working with Shared Environments](share-environment.md)   | 