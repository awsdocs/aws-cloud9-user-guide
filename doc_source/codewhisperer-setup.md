# Setting up CodeWhisperer with AWS Cloud9<a name="codewhisperer-setup"></a>

**Topics**
+ [Enabling IAM permissions for CodeWhisperer](#codewhisperer-IAM-policies)
+ [Activate CodeWhisperer](#codewhisperer-setup-activate)
+ [Activating auto\-suggestions](#codewhisperer-setup-activate-suggestion)

## AWS Identity and Access Management permissions for AWS Cloud9<a name="codewhisperer-IAM-policies"></a>

 For CodeWhisperer to provide recommendations in the AWS Cloud9 console, you must enable the correct IAM permissions for either your IAM user or role\. You must add the `codewhisperer:GenerateRecommendations` permission, as outlined in the sample IAM policy below: 

```
{
  "Version": "2012-10-17",
  "Statement": [{
    {
      "Sid": "CodeWhispererPermissions",
      "Effect": "Allow",
      "Action": ["codewhisperer:GenerateRecommendations"],
      "Resource": "*"
    }
  ]
}
```

It is best practice to use IAM policies to grant restrictive permissions to IAM principals\. For details about working with IAM for AWS Cloud9, see [Identity and access management in AWS Cloud9](security-iam.md#security-iam.title)\.

## Activating the CodeWhisperer experimental feature<a name="codewhisperer-setup-activate"></a>

To activate CodeWhisperer, complete the following procedure\.

1. In AWS Cloud9, choose the AWS Toolkit icon from the left nav\.

1. Under **Developer Tools**, choose **CodeWhisperer** \-> **Request access**\.

1. Check back regularly, reloading your browser each time\. When you have been given access, this option will change from **Request access** to **Enable CodeWhisperer**\.

1. Choose **Enable CodeWhisperer**\.

1. A tab will open, displaying the terms of service for the Amazon CodeWhisperer preview\.

   Review the terms, and then choose **Accept and Enable CodeWhisperer**\.

## Activating auto\-suggestions for the AWS Cloud9<a name="codewhisperer-setup-activate-suggestion"></a>

For CodeWhisperer to run in AWS Cloud9, the auto\-suggestions feature must be active in AWS Cloud9\. To activate auto\-suggestions, complete these steps\.

1. In AWS Cloud9, choose the AWS Toolkit icon from the left navigation panel\.

1. Choose **CodeWhisperer** \-> **Activate auto\-suggestions**\.

1. A window will open containing the CodeWhisperer terms of service\. Read them, and if you accept the terms, choose **Accept**\.

1. Under **Developer Tools**, under **CodeWhisperer \(Preview\)**, choose **Enable CodeWhisperer**\.

1. Read the CodeWhisperer terms of service and choose **Accept**\.