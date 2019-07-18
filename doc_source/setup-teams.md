# Additional Setup Options for AWS Cloud9<a name="setup-teams"></a>

This topic assumes you have already completed the setup steps in [Team Setup](setup.md) or [Enterprise Setup](setup-enterprise.md)\.

In [Team Setup](setup.md) or [Enterprise Setup](setup-enterprise.md), you created groups and added AWS Cloud9 access permissions directly to those groups, to ensure that users in those groups can access AWS Cloud9\. In this topic, you will add more access permissions to restrict the kinds of environments that users in those groups can create\. This can help control costs related to AWS Cloud9 in AWS accounts and organizations\.

To add these access permissions, you create your own set of policies that define the AWS access permissions you want to enforce\. \(We call each of these a *customer\-managed policy*\.\) Then you attach those customer\-managed policies to the groups that the users belong to\. \(In some scenarios, you must also detach existing AWS managed policies that are already attached to those groups\.\) To set this up, follow the procedures in this topic\.

**Note**  
The following procedures cover attaching and detaching policies for AWS Cloud9 users only\. These procedures assume you already have a separate AWS Cloud9 users group and AWS Cloud9 administrators group and that you have only a limited number of users in the AWS Cloud9 administrators group\. This AWS security best practice can help you better control, track, and troubleshoot issues with AWS resource access\.
+  [Step 1: Create a Customer\-Managed Policy](#setup-teams-create-policy) 
+  [Step 2: Add Customer\-Managed Policies to a Group](#setup-teams-add-policy) 
+  [Customer\-Managed Policy Examples for Teams Using AWS Cloud9](#setup-teams-policy-examples) 

## Step 1: Create a Customer\-Managed Policy<a name="setup-teams-create-policy"></a>

You can create a customer\-managed policy using the [AWS Management Console](#setup-teams-create-policy-console) or the [AWS Command Line Interface \(AWS CLI\)](#setup-teams-create-policy-cli)\.

**Note**  
This step covers creating a customer\-managed policy for IAM groups only\. To create a custom permission set for groups in AWS Single Sign\-On \(SSO\), skip this step and follow the instructions in [Create Permission Set](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsets.html#howtocreatepermissionset) in the *AWS Single Sign\-On User Guide* instead\. In this topic, follow the instructions to create a custom permission set\. For related custom permissions policies, see [Customer\-Managed Policy Examples for Teams Using AWS Cloud9](#setup-teams-policy-examples) later in this topic\.

### Create a Customer\-Managed Policy Using the Console<a name="setup-teams-create-policy-console"></a>

1. Sign in to the AWS Management Console, if you are not already signed in\.

   We recommend you sign in using credentials for an IAM administrator user in your AWS account\. If you cannot do this, check with your AWS account administrator\.

1. Open the IAM console\. To do this, in the console's navigation bar, choose **Services**\. Then choose **IAM**\.

1. In the service's navigation pane, choose **Policies**\.

1. Choose **Create policy**\.

1. In the **JSON** tab, paste one of our suggested [Customer\-Managed Policy Examples](#setup-teams-policy-examples)\.
**Note**  
You can also create your own customer\-managed policies\. For more information, see the [IAM JSON Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html) in the *IAM User Guide* and the AWS services' [documentation](https://aws.amazon.com/documentation/)\.

1. Choose **Review policy**\.

1. On the **Review policy** page, type a **Name** and an optional **Description** for the policy, and then choose **Create policy**\.

Repeat this step for each additional customer\-managed policy that you want to create, then skip ahead to [Add Customer\-Managed Policies to a Group Using the Console](#setup-teams-add-policy-console)\.

### Create a Customer\-Managed Policy Using the AWS CLI<a name="setup-teams-create-policy-cli"></a>

1. On the computer where you run the AWS CLI, create a file to describe the policy \(for example, `policy.json`\)\.

   If you create the file with a different file name, substitute it throughout this procedure\.

1. Paste one of our suggested [Customer\-Managed Policy Examples](#setup-teams-policy-examples) into the `policy.json` file\.
**Note**  
You can also create your own customer\-managed policies\. For more information, see the [IAM JSON Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html) in the *IAM User Guide* and the AWS services' [documentation](https://aws.amazon.com/documentation/)\.

1. From the terminal or command prompt, switch to the directory that contains the `policy.json` file\.

1. Run the IAM `create-policy` command, specifying a name for the policy and the `policy.json` file\.

   ```
   aws iam create-policy --policy-document file://policy.json --policy-name MyPolicy
   ```

   In the preceding command, replace `MyPolicy` with a name for the policy\.

Skip ahead to [Add Customer\-Managed Policies to a Group Using the AWS CLI](#setup-teams-add-policy-cli)\.

## Step 2: Add Customer\-Managed Policies to a Group<a name="setup-teams-add-policy"></a>

You can add customer\-managed policies to a group using the [AWS Management Console](#setup-teams-add-policy-console) or the [AWS Command Line Interface \(AWS CLI\)](#setup-teams-add-policy-cli)\.

**Note**  
This step covers adding customer\-managed policies to IAM groups only\. To add custom permission sets to groups in AWS Single Sign\-On \(SSO\), skip this step and follow the instructions in [Assign User Access](https://docs.aws.amazon.com/singlesignon/latest/userguide/useraccess.html#assignusers) in the *AWS Single Sign\-On User Guide* instead\.

### Add Customer\-Managed Policies to a Group Using the Console<a name="setup-teams-add-policy-console"></a>

1. With the IAM console open from the previous procedure, in the service's navigation pane, choose **Groups**\.

1. Choose the group's name\.

1. On the **Permissions** tab, for **Managed Policies**, choose **Attach Policy**\.

1. In the list of policy names, choose the box next to each customer\-managed policy you want to attach to the group\. \(If you don't see a specific policy name in the list, type the policy name in the **Filter** box to display it\.\)

1. Choose **Attach Policy**\.

### Add Customer\-Managed Policies to a Group Using the AWS CLI<a name="setup-teams-add-policy-cli"></a>

**Note**  
If you're using [AWS managed temporary credentials](auth-and-access-control.md#auth-and-access-control-temporary-managed-credentials), you can't use a terminal session in the AWS Cloud9 IDE to run some or all of the commands in this section\. To address AWS security best practices, AWS managed temporary credentials don’t allow some commands to be run\. Instead, you can run those commands from a separate installation of the AWS Command Line Interface \(AWS CLI\)\.

Run the IAM `attach-group-policy` command, specifying the group's name and the Amazon Resource Name \(ARN\) of the policy\.

```
aws iam attach-group-policy --group-name MyGroup --policy-arn arn:aws:iam::123456789012:policy/MyPolicy
```

In the preceding command, replace `MyGroup` with the name of the group\. Replace `123456789012` with the AWS account ID, and replace `MyPolicy` with the name of the customer\-managed policy\.

## Customer\-Managed Policy Examples for Teams Using AWS Cloud9<a name="setup-teams-policy-examples"></a>

Following are some examples of policies you can use to restrict the kinds of environments that users in a group can create in an AWS account\.
+  [Prevent Users in a Group from Creating Environments](#setup-teams-policy-examples-prevent-environments) 
+  [Prevent Users in a Group from Creating EC2 Environments](#setup-teams-policy-examples-prevent-ec2-environments) 
+  [Allow Users in a Group to Create EC2 Environments Only with Specific Amazon EC2 Instance Types](#setup-teams-policy-examples-specific-instance-types) 
+  [Allow Users in a Group to Create Only a Single EC2 Environment Per AWS Region](#setup-teams-policy-examples-single-ec2-environment) 

### Prevent Users in a Group from Creating Environments<a name="setup-teams-policy-examples-prevent-environments"></a>

The following customer\-managed policy, when attached to an AWS Cloud9 users group, prevents those users from creating environments in an AWS account\. This is useful if you want an IAM administrator user in your AWS account to manage creating environments instead of users in an AWS Cloud9 users group\.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": [
        "cloud9:CreateEnvironmentEC2",
        "cloud9:CreateEnvironmentSSH"
      ],
      "Resource": "*"
    }
  ]
}
```

Note that the preceding customer\-managed policy explicitly overrides `"Effect": "Allow"` for `"Action": "cloud9:CreateEnvironmentEC2"` and `"cloud9:CreateEnvironmentSSH"` on `"Resource": "*"` in the `AWSCloud9User` managed policy that is already attached to the AWS Cloud9 users group\.

### Prevent Users in a Group from Creating EC2 Environments<a name="setup-teams-policy-examples-prevent-ec2-environments"></a>

The following customer\-managed policy, when attached to an AWS Cloud9 users group, prevents those users from creating EC2 environments in an AWS account\. This is useful if you want an IAM administrator user in your AWS account to manage creating EC2 environments instead of users in an AWS Cloud9 users group\. This assumes you haven't also attached a policy that prevents users in that group from creating SSH environments\. Otherwise, those users won't be able to create environments at all\.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "cloud9:CreateEnvironmentEC2",
      "Resource": "*"
    }
  ]
}
```

Note that the preceding customer\-managed policy explicitly overrides `"Effect": "Allow"` for `"Action": "cloud9:CreateEnvironmentEC2"` on `"Resource": "*"` in the `AWSCloud9User` managed policy that is already attached to the AWS Cloud9 users group\.

### Allow Users in a Group to Create EC2 Environments Only with Specific Amazon EC2 Instance Types<a name="setup-teams-policy-examples-specific-instance-types"></a>

The following customer\-managed policy, when attached to an AWS Cloud9 users group, allows those users to create EC2 environments that only use instance types starting with `t2` in an AWS account\. This policy assumes you haven't also attached a policy that prevents users in that group from creating EC2 environments\. Otherwise, those users won't be able to create EC2 environments at all\.

You can replace `"t2.*"` in the following policy with a different instance class \(for example, `"m4.*"`\)\. Or you can restrict it to multiple instance classes or instance types \(for example, `[ "t2.*", "m4.*" ]` or `[ "t2.micro", "m4.large" ]`\)\.

For an AWS Cloud9 users group, detach the `AWSCloud9User` managed policy from the group, and then add the following customer\-managed policy in its place\. \(If you do not detach the `AWSCloud9User` managed policy, the following customer\-managed policy will have no effect\.\)

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "cloud9:CreateEnvironmentSSH",
        "cloud9:ValidateEnvironmentName",
        "cloud9:GetUserPublicKey",
        "cloud9:UpdateUserSettings",
        "cloud9:GetUserSettings",
        "iam:GetUser",
        "iam:ListUsers",
        "ec2:DescribeVpcs",
        "ec2:DescribeSubnets"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": "cloud9:CreateEnvironmentEC2",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "cloud9:InstanceType": "t2.*"
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "cloud9:DescribeEnvironmentMemberships"
      ],
      "Resource": [
        "*"
      ],
      "Condition": {
        "Null": {
          "cloud9:UserArn": "true",
          "cloud9:EnvironmentId": "true"
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "iam:CreateServiceLinkedRole"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "iam:AWSServiceName": "cloud9.amazonaws.com"
        }
      }
    }
  ]
}
```

Note that the preceding customer\-managed policy also allows those users to create SSH environments\. To prevent those users from creating SSH environments altogether, remove `"cloud9:CreateEnvironmentSSH",` from the preceding customer\-managed policy\.

### Allow Users in a Group to Create Only a Single EC2 Environment Per AWS Region<a name="setup-teams-policy-examples-single-ec2-environment"></a>

The following customer\-managed policy, when attached to an AWS Cloud9 users group, allows each of those users to create a maximum of one EC2 environment per AWS Region that AWS Cloud9 is available in\. This is done by restricting the name of the environment to one specific name in that AWS Region \(in this example, `my-demo-environment`\)\.

**Note**  
AWS Cloud9 doesn't enable restricting the creation of environments to specific AWS Regions\. Nor does it enable restricting the overall number of environments that can be created \(other than the published [service limits](limits.md)\)\.

For an AWS Cloud9 users group, detach the `AWSCloud9User` managed policy from the group, and then add the following customer\-managed policy in its place\. \(If you do not detach the `AWSCloud9User` managed policy, the following customer\-managed policy will have no effect\.\)

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "cloud9:CreateEnvironmentSSH",
        "cloud9:ValidateEnvironmentName",
        "cloud9:GetUserPublicKey",
        "cloud9:UpdateUserSettings",
        "cloud9:GetUserSettings",
        "iam:GetUser",
        "iam:ListUsers",
        "ec2:DescribeVpcs",
        "ec2:DescribeSubnets"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "cloud9:CreateEnvironmentEC2"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "cloud9:EnvironmentName": "my-demo-environment"
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "cloud9:DescribeEnvironmentMemberships"
      ],
      "Resource": [
        "*"
      ],
      "Condition": {
        "Null": {
          "cloud9:UserArn": "true",
          "cloud9:EnvironmentId": "true"
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "iam:CreateServiceLinkedRole"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "iam:AWSServiceName": "cloud9.amazonaws.com"
        }
      }
    }
  ]
}
```

Note that the preceding customer\-managed policy allows those users to create SSH environments\. To prevent those users from creating SSH environments altogether, remove `"cloud9:CreateEnvironmentSSH",` from the preceding customer\-managed policy\.

For additional examples, see the [Customer\-Managed Policy Examples](auth-and-access-control.md#auth-and-access-control-customer-policies-examples) in [Authentication and Access Control](auth-and-access-control.md)\.

## Next Steps<a name="setup-teams-next-steps"></a>


****  

|  **Task**  |  **See this topic**  | 
| --- | --- | 
|  Create an AWS Cloud9 development environment, and then use the AWS Cloud9 IDE to work with code in your new environment\.  |   [Creating an Environment](create-environment.md)   | 
|  Learn how to use the AWS Cloud9 IDE\.  |   [IDE Tutorial](tutorial.md)   | 
|  Invite others to use your new environment along with you, in real time and with text chat support\.  |   [Working with Shared Environments](share-environment.md)   | 