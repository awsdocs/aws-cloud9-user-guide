# Working with AWS Project and User Settings in the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="settings-aws"></a>

AWS service settings, located in the **AWS Settings** pane of the **Preferences** tab, include the following kinds of settings:
+ Which AWS Region to use for the **AWS Resources** window
+ Whether to use AWS managed temporary credentials
+ Whether to display the AWS Serverless Application Model \(AWS SAM\) template editor in plain text or visual mode

To view or change these settings, choose **AWS Cloud9, Preferences** in the menu bar of an IDE for an environment\.

In the following lists, project\-level settings apply only to the current AWS Cloud9 development environment, while user\-level settings apply across each environment associated with your IAM user\. For more information, see [Apply the Current Project Settings for an Environment to Another Environment](settings-project.md#settings-project-apply) and [Share Your User Settings with Another User](settings-user.md#settings-user-share)\.
+  [Project\-Level Settings](#settings-aws-project) 
+  [User\-Level Settings](#settings-aws-user) 

## Project\-Level Settings<a name="settings-aws-project"></a>

** **AWS Region** **  
Which AWS Region to use for the **Lambda** section of the **AWS Resources** window\.

** **AWS managed temporary credentials** **  
If turned on, uses AWS managed temporary credentials when calling AWS services from the AWS CLI, the aws\-shell, or AWS SDK code from an environment\. For more information, see [AWS Managed Temporary Credentials](how-cloud9-with-iam.md#auth-and-access-control-temporary-managed-credentials)\.

## User\-Level Settings<a name="settings-aws-user"></a>

** **Use AWS SAM visual editor** **  
If turned on, displays the AWS Serverless Application Model \(AWS SAM\) template editor in visual mode when using the **Lambda** section of the **AWS Resources** window\. If turned off, displays the editor in text mode\.