# AWS Toolkit<a name="toolkit-welcome"></a>

## Why use the AWS Toolkit?<a name="toolkit-why"></a>

The AWS Toolkit is an extension for the AWS Cloud9 integrated development environment \(IDE\)\. This extension makes it easier for developers to access and work with a wide range of AWS services\.

**Note**  
Support for the AWS Toolkit is provided as an integrated feature that's managed by AWS Cloud9\. Currently, customers cannot customize the AWS Cloud9 IDE by installing third\-party extensions\.

At present, the following AWS services and resources can be accessed through the AWS Toolkit extension:
+ [API Gateway](api-gateway-toolkit.md)
+ [AWS CloudFormation stacks](cloudformation-toolkit.md)
+ [AWS Lambda\*](lambda-toolkit.md)
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
+ [Working with API Gateway using the AWS Toolkit](api-gateway-toolkit.md)
+ [Working with AWS CloudFormation stacks using AWS Toolkit](cloudformation-toolkit.md)
+ [Working with AWS Lambda functions using the AWS Toolkit](lambda-toolkit.md)
+ [Working with Amazon S3 using AWS Toolkit](s3-toolkit.md)
+ [Working with AWS serverless applications using the AWS Toolkit](serverless-apps-toolkit.md)