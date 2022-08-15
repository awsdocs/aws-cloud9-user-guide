# Changing environment settings in AWS Cloud9<a name="change-environment"></a>

You can change the preferences or settings for an AWS Cloud9 development environment\.
+  [Change Environment Preferences](#change-environment-single) 
+  [Change Environment Settings with the Console](#change-environment-description) 
+  [Change Environment Settings with Code](#change-environment-description-code) 

## Change environment preferences<a name="change-environment-single"></a>

1. Open the environment you want to change settings for\. To open an environment, see [Opening an Environment](open-environment.md)\.

1. In the AWS Cloud9 IDE, on the menu bar, choose **AWS Cloud9**, **Preferences**\.

1. In the **Preferences** window, choose **Project Settings**\.

1. Change any of the available project settings as you want\. These include settings such as **Code Editor \(Ace\)** and **Find in Files**\.

**Note**  
For more information, see [Project Setting Changes You Can Make](settings-project.md#settings-project-change)\.

## Change environment settings with the console<a name="change-environment-description"></a>

1. Sign in to the AWS Cloud9 console as follows:
   + If you're the only individual using your AWS account or you are an IAM user in a single AWS account, go to [https://console\.aws\.amazon\.com/cloud9/](https://console.aws.amazon.com/cloud9/)\.
   + If your organization uses AWS IAM Identity Center \(successor to AWS Single Sign\-On\), see your AWS account administrator for sign\-in instructions\.

1. In the top navigation bar, choose the AWS Region where the environment is located\.  
![\[AWS Region selector in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-region.png)

1. In the list of environments, for the environment whose settings you want to change, do one of the following\.
   + Choose the title of the card for the environment\. Then choose **Edit** on the next page\.  
![\[Editing environment settings in the environment details page\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-edit-env.png)
   + Select the card for the environment, and then choose the **Edit** button\.  
![\[Editing environment settings in the environments list\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-edit-env-card.png)

1. Make your changes, and then choose **Save changes**\.

   You can use the AWS Cloud9 console to change the following settings\.
   + For EC2 environments, **Name** and **Description**\.
   + For SSH environments: **Name**, **Description**, **User**, **Host**, **Port**, **Environment path**, **Node\.js binary path**, and **SSH jump host**\.

   To change other settings, do the following\.
   + For EC2 environments, do the following\.
     + You cannot change **Type**, **Security groups**, **VPC**, **Subnet**, **Environment path**, or **Environment ARN**\.
     + For **Permissions** or **Number of members**, see [Change the Access Role of an Environment Member](share-environment.md#share-environment-change-access), [Remove Your User](share-environment.md#share-environment-change-access), [Invite an IAM User](share-environment.md#share-environment-invite-user), and [Remove Another Environment Member](share-environment.md#share-environment-delete-member)\.
     + For **EC2 instance type**, **Memory**, or **vCPU**, see [Moving or Resizing an Environment](move-environment.md)\.
   + For SSH environments, do the following\.
     + You cannot change **Type** or **Environment ARN**\.
     + For **Permissions** or **Number of members**, see [Change the Access Role of an Environment Member](share-environment.md#share-environment-change-access), [Remove Your User](share-environment.md#share-environment-change-access), [Invite an IAM User](share-environment.md#share-environment-invite-user), and [Remove Another Environment Member](share-environment.md#share-environment-delete-member)\.

If your environment isn't displayed in the console, try doing one or more of the following actions to have it be displayed\.
+ In the side navigation bar, choose one or more of the following\.
  + Choose **Your environments** to display all environments that your AWS entity owns within the selected AWS Region and AWS account\.
  + Choose **Shared with you** to display all environments your AWS entity has been invited to within the selected AWS Region and AWS account\.
  + Choose **Account environments** to display all environments within the selected AWS Region and AWS account that your AWS entity has permissions to display\.  
![\[Environment list scope in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-env-list.png)
+ Choose the previous arrow, next arrow, or page number button to display more environments in the current scope\.  
![\[Environment list page control in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-find-env.png)
+ If you think you should be a member of an environment, but the environment isn't displayed in the **Shared with you** list, check with the environment owner\.
+ In the top navigation bar, choose a different AWS Region\.  
![\[AWS Region selector in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-region.png)

## Change environment settings with code<a name="change-environment-description-code"></a>

To use code to change the settings of an environment in AWS Cloud9, call the AWS Cloud9 update environment operation, as follows\.


****  

|  |  | 
| --- |--- |
|  AWS CLI  |   [update\-environment](https://docs.aws.amazon.com/cli/latest/reference/cloud9/update-environment.html)   | 
|  AWS SDK for C\+\+  |   [UpdateEnvironmentRequest](https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_update_environment_request.html), [UpdateEnvironmentResult](https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_update_environment_result.html)   | 
|  AWS SDK for Go  |   [UpdateEnvironment](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.UpdateEnvironment), [UpdateEnvironmentRequest](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.UpdateEnvironmentRequest), [UpdateEnvironmentWithContext](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.UpdateEnvironmentWithContext)   | 
|  AWS SDK for Java  |   [UpdateEnvironmentRequest](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/UpdateEnvironmentRequest.html), [UpdateEnvironmentResult](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/UpdateEnvironmentResult.html)   | 
|  AWS SDK for JavaScript  |   [updateEnvironment](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Cloud9.html#updateEnvironment-property)   | 
|  AWS SDK for \.NET  |   [UpdateEnvironmentRequest](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TUpdateEnvironmentRequest.html), [UpdateEnvironmentResponse](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TUpdateEnvironmentResponse.html)   | 
|  AWS SDK for PHP  |   [updateEnvironment](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-cloud9-2017-09-23.html#updateenvironment)   | 
|  AWS SDK for Python \(Boto\)  |   [update\_environment](https://boto3.readthedocs.io/en/latest/reference/services/cloud9.html#Cloud9.Client.update_environment)   | 
|  AWS SDK for Ruby  |   [update\_environment](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Cloud9/Client.html#update_environment-instance_method)   | 
|  AWS Tools for Windows PowerShell  |   [Update\-C9Environment](https://docs.aws.amazon.com/powershell/latest/reference/items/Update-C9Environment.html)   | 
|  AWS Cloud9 API  |   [UpdateEnvironment](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_UpdateEnvironment.html)   | 