# Setting up CodeWhisperer with AWS Cloud9<a name="codewhisperer-setup"></a>

**Topics**
+ [Enabling IAM permissions for CodeWhisperer](#codewhisperer-IAM-policies)
+ [Activating CodeWhisperer within the AWS Cloud9 IDE](#codewhisperer-activation)

## AWS Identity and Access Management permissions for AWS Cloud9<a name="codewhisperer-IAM-policies"></a>

 For CodeWhisperer to provide recommendations in the AWS Cloud9 console, you must enable the correct IAM permissions for either your IAM user or role\. You must add the `codewhisperer:GenerateRecommendations` permission, as outlined in the sample IAM policy below: 

```
{
  "Version": "2012-10-17",
  "Statement": [
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

**Topics**
+ [Enabling IAM permissions for CodeWhisperer](#codewhisperer-IAM-policies)
+ [Activating CodeWhisperer within the AWS Cloud9 IDE](#codewhisperer-activation)

## Activating CodeWhisperer within the AWS Cloud9 IDE<a name="codewhisperer-activation"></a>

Once you have accessed the AWS Cloud9 IDE you need to activate CodeWhisperer\.

1. From the AWS Cloud9 IDE, choose **aws\-explorer **from the AWS Cloud9 IDE sidebar\.

1. From the **Developer Tools **navigation pane, choose **CodeWhisperer \(Preview\)**\.

1. Choose** Enable CodeWhisperer **to accept the Terms of Service and activate CodeWhisperer within AWS Cloud9 IDE\.

![\[Selecting the CodeWhisperer option from AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/codewhisperer-activate.png)