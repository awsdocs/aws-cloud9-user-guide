# AWS Toolkit<a name="toolkit-welcome"></a>

## Why use the AWS Toolkit?<a name="toolkit-why"></a>

The AWS Toolkit is an extension for the AWS Cloud9 integrated development environment \(IDE\)\. This extension makes it easier for developers to access and work with a wide range of AWS services\.

**Note**  
Support for the AWS Toolkit is provided as an integrated feature that's managed by AWS Cloud9\. Currently, customers cannot customize the AWS Cloud9 IDE by installing third\-party extensions\.

At present, the following AWS services and resources can be accessed through the AWS Toolkit extension:
+ [AWS App Runner](using-apprunner.md)
+ [API Gateway](api-gateway-toolkit.md)
+ [AWS CloudFormation stacks](cloudformation-toolkit.md)
+ [CloudWatch Logs](cloudwatch-logs-toolkit.md)
+ [AWS Lambda\*](lambda-toolkit.md)
+ [Resources](more-resources.md)
+ [Amazon S3 buckets and objects](s3-toolkit.md)
+ [AWS Serverless Application Model applications](serverless-apps-toolkit.md)

**Important**  
\*The features provided by the AWS Toolkit for working with AWS Lambda functions and serverless applications replace the support previously provided in the **Lambda** section of the **AWS Resources** window\. When it's enabled, the AWS Toolkit is your primary tool for working with Lambda functions, and the **AWS Resources** window isn't available\.

## Enabling AWS Toolkit<a name="access-toolkit"></a>

If the AWS Toolkit isn't available in your environment, you can enable it in the **Preferences** tab\.<a name="enabling-toolkit"></a>

**To enable the AWS Toolkit**

1. Choose **AWS Cloud9**, **Preferences** on the menu bar\. 

1. On the **Preferences** tab, in the side navigation pane, choose **AWS Settings**\. 

1. In the **AWS Resources** pane, turn on **AWS AWS Toolkit** so that it displays a check mark on a green background\. 

   When you enable the AWS Toolkit, the IDE refreshes to show the updated **Enable AWS Toolkit** setting and the AWS Toolkit option at the side of the IDE below the **Environment** option\.

**Important**  
If your AWS Cloud9 environment's EC2 instance doesn't have access to the internet \(no outbound traffic allowed\), a message may display after you turn on AWS Toolkit and relaunch the IDE\. This message states that the dependencies required by AWS Toolkit couldn't be downloaded\. You're also unable to use the AWS Toolkit\.   
To fix this issue, create a VPC endpoint for Amazon S3\. This allows access to an Amazon S3 bucket in your AWS Region that contains the dependencies required to keep your IDE up\-to\-date\.  
For more information, see [Configuring VPC endpoints for Amazon S3 to download dependencies](ec2-ssm.md#configure-s3-endpoint)\.



## Managing access credentials for AWS Toolkit<a name="credentials-for-toolkit"></a>

AWS Toolkit allows you to interact with a wide range of AWS services, so you should ensure that the IAM entity that's used has the necessary permissions to interact with those services\. The easiest way to obtain permissions is to use [AWS managed temporary credentials](security-iam.md#auth-and-access-control-temporary-managed-credentials), which work whenever an EC2 environment accesses an AWS service on behalf of an AWS entity \(for example, an IAM user\)\.

But if you've launched your development environment's EC2 instance into a **private subnet**, AWS managed temporary credentials aren't available\. As an alternative, you can allow AWS Toolkit to access your AWS services by manually creating your own set of credentials called a *profile*\. Profiles feature long\-term credentials called access keys, which you can obtain from the IAM console\.<a name="manual-credentials"></a>

**Create a profile to provide access credential for AWS Toolkit**

1. To get your access keys \(consisting of an *access key ID* and *secret access key*\), go to the IAM console at [ https://console\.aws\.amazon\.com/iam](https://console.aws.amazon.com/iam)\.

1. Choose **Users** from the navigation bar and then choose your AWS user name \(not the check box\)\.

1. Choose the **Security credentials** tab, and then choose **Create access key**\.
**Note**  
If you already have an access key but you can't access your secret key, make the old key inactive and create a new one\.

1. In the dialog box that shows your access key ID and secret access key, choose **Download \.csv file** to store this information in a secure location\.

1. After you've downloaded your access keys, launch an AWS Cloud9 environment and start a terminal session by choosing **Window**, **New Terminal**\. 

1. In the terminal window, run the following command:

   ```
   aws configure --profile toolkituser
   ```

   In this case, `toolkituser` is the profile name being used, but you can choose your own\.

1. At the command line, enter the `AWS Access Key ID` and `AWS Secret Access Key` that you previously downloaded from the IAM console\.
   + For `Default region name`, specify an AWS Region \(`us-east-1`, for example\)\. 
   + For `Default output format`, specify a file format \(`json`, for example\)\. 
**Note**  
For more information on the options when configuring a profile, see [Configuration basics](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) in the *AWS Command Line Interface User Guide*\.

1. After you've successfully created your profile, launch the AWS Toolkit, go to the [**AWS Toolkit menu**](toolkit-navigation.md#toolkit-menu), and choose **Connect to AWS**\.

1. For the **Select an AWS credential profile** field, choose the profile you've just created in the terminal \(`profile:toolkituser`, for example\)\.

If the selected profile contains valid access credentials, the **AWS Explorer** pane refreshes to display the AWS services that you can now access\.

### Using IAM roles to grant permissions to applications on EC2 instances<a name="ec2-instance-credentials"></a>

You can also use an IAM role to manage temporary credentials for applications that run on an EC2 instance\. The role supplies temporary permissions that applications can use when they make calls to other AWS resources\. When you launch an EC2 instance, you specify an IAM role to associate with the instance\. Applications that run on the instance can then use the role\-supplied temporary credentials when making API requests against AWS services\.

After you've created the role, you need to assign this role and its associated permission to the an instance by creating an *instance profile*\. The instance profile is attached to the instance and can provide the role's temporary credentials to an application that runs on the instance\.

For more information, see [Using an IAM role to grant permissions to applications running on Amazon EC2 instances](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html#roles-usingrole-ec2instance-get-started) in the *IAM User Guide*\.

## Identifying AWS Toolkit components<a name="ui-components"></a>

The screenshot below shows three key UI components of the AWS Toolkit:

![\[Labelled screenshot showing key UI components of the AWS Toolkit\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/)

1. **AWS Explorer** window: Enables you to interact with the AWS services that are accessible through the Toolkit\. You can toggle between showing and hiding the **AWS Explorer** using the AWS option at the left side of the IDE\. For more about using this interface component and accessing AWS services for different AWS Regions, see [Using AWS Explorer to work with services and resources in multiple AWS Regions](toolkit-navigation.md#working-with-aws-explorer)\.

1. **Toolkit** menu: Allows you to manage connections to AWS, customize the display of the **AWS Explorer** window, create/deploy serverless applications, work with GitHub repositories, and access documentation\. For more information, see [Accessing and using the AWS Toolkit menu](toolkit-navigation.md#toolkit-menu)\.

1. **AWS Configuration** pane: Lets you customize the behavior of AWS services that you interact with using the Toolkit\. For more information, see [Modifying AWS Toolkit settings using the AWS Configuration pane](toolkit-navigation.md#configuration-options)\. 

## Disabling AWS Toolkit<a name="disable-toolkit"></a>

You can disable the AWS Toolkit in the **Preferences** tab\.<a name="disabling-toolkit"></a>

**To disable the AWS Toolkit**

1. Choose **AWS Cloud9**, **Preferences** on the menu bar\. 

1. On the **Preferences** tab, in the side navigation pane, choose **AWS Settings**\. 

1. In the **AWS Resources** pane, turn off **AWS AWS Toolkit**\. 

   When you disable the AWS Toolkit, the IDE refreshes to remove the AWS Toolkit option at the side of the IDE below the **Environment** option\.



## AWS Toolkit topics<a name="toolkit-resources-info"></a>
+ [Navigating and configuring the AWS Toolkit](toolkit-navigation.md)
+ [Using AWS App Runner with AWS Toolkit](using-apprunner.md)
+ [Working with API Gateway using the AWS Toolkit](api-gateway-toolkit.md)
+ [Working with AWS CloudFormation stacks using AWS Toolkit](cloudformation-toolkit.md)
+ [Working with AWS Lambda functions using the AWS Toolkit](lambda-toolkit.md)
+ [Working with resources](more-resources.md)
+ [Working with Amazon S3 using AWS Toolkit](s3-toolkit.md)
+ [Working with AWS serverless applications using the AWS Toolkit](serverless-apps-toolkit.md)