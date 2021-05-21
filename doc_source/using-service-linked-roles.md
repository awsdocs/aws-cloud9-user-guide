# Using service\-linked roles for AWS Cloud9<a name="using-service-linked-roles"></a>

AWS Cloud9 uses AWS Identity and Access Management \(IAM\) [service\-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html)\. A service\-linked role is a unique type of IAM role that's linked directly to AWS Cloud9\. Service\-linked roles are predefined by AWS Cloud9 and include all the permissions that the service requires to call other AWS services on your behalf\.

A service\-linked role makes setting up AWS Cloud9 easier because you don’t have to add the necessary permissions\. AWS Cloud9 defines the permissions of its service\-linked roles, and only AWS Cloud9 can assume its roles\. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity\.

You can delete the roles only after first deleting their related resources\. This protects your AWS Cloud9 resources because you can't inadvertently remove permission to access the resources\.

For information about other services that support service\-linked roles, see [AWS Services That Work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes** in the **Service\-Linked Role** column\. Choose a **Yes** with a link to view the service\-linked role documentation for that service\.
+  [Service\-linked role permissions for AWS Cloud9](#service-linked-role-permissions) 
+  [Creating a service\-linked role for AWS Cloud9](#create-service-linked-role) 
+  [Editing a service\-linked role for AWS Cloud9](#edit-service-linked-role) 
+  [Deleting a service\-linked role for AWS Cloud9](#delete-service-linked-role) 
+  [Supported Regions for AWS Cloud9 service\-linked roles](#slr-regions) 

## Service\-linked role permissions for AWS Cloud9<a name="service-linked-role-permissions"></a>

AWS Cloud9 uses the service\-linked role named AWSServiceRoleForAWSCloud9\. This service\-linked role trusts the service `cloud9.amazonaws.com` to assume the role\.

The permissions policy for this service\-linked role is named **AWSCloud9ServiceRolePolicy**, and it allows AWS Cloud9 to complete the following actions on the specified resources\.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:RunInstances",
                "ec2:CreateSecurityGroup",
                "ec2:DescribeVpcs",
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeInstances",
                "ec2:DescribeInstanceStatus",
                "cloudformation:CreateStack",
                "cloudformation:DescribeStacks",
                "cloudformation:DescribeStackEvents",
                "cloudformation:DescribeStackResources"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:TerminateInstances",
                "ec2:DeleteSecurityGroup",
                "ec2:AuthorizeSecurityGroupIngress"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "cloudformation:DeleteStack"
            ],
            "Resource": "arn:aws:cloudformation:*:*:stack/aws-cloud9-*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateTags"
            ],
            "Resource": [
                "arn:aws:ec2:*:*:instance/*",
                "arn:aws:ec2:*:*:security-group/*"
            ],
            "Condition": {
                "StringLike": {
                    "aws:RequestTag/Name": "aws-cloud9-*"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:StartInstances",
                "ec2:StopInstances"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "ec2:ResourceTag/aws:cloudformation:stack-name": "aws-cloud9-*"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:ListInstanceProfiles",
                "iam:GetInstanceProfile"
            ],
            "Resource": [
                "arn:aws:iam::*:instance-profile/cloud9/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:PassRole"
            ],
            "Resource": [
                "arn:aws:iam::*:role/service-role/AWSCloud9SSMAccessRole"
            ],
            "Condition": {
                "StringLike": {
                    "iam:PassedToService": "ec2.amazonaws.com"
                }
            }
        }
    ]
}
```

You must configure permissions to allow AWS Cloud9 to create a service\-linked role on behalf of an IAM entity \(such as a user, group, or role\)\.

To allow AWS Cloud9 to create the AWSServiceRoleForAWSCloud9 service\-linked role, add the following statement to the permissions policy for the IAM entity on whose behalf AWS Cloud9 needs to create the service\-linked role\.

```
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
```

Alternatively, you can add the AWS managed policies `AWSCloud9User` or `AWSCloud9Administrator` to the IAM entity\.

To allow an IAM entity to delete the AWSServiceRoleForAWSCloud9 service\-linked role, add the following statement to the permissions policy for the IAM entity that needs to delete a service\-linked role\.

```
{
  "Effect": "Allow",
  "Action": [
    "iam:DeleteServiceLinkedRole",
    "iam:GetServiceLinkedRoleDeletionStatus"
  ],
  "Resource": "*",
  "Condition": {
    "StringLike": {
      "iam:AWSServiceName": "cloud9.amazonaws.com"
    }
  }
}
```

## Creating a service\-linked role for AWS Cloud9<a name="create-service-linked-role"></a>

You don't need to create a service\-linked role\. When you create an AWS Cloud9 development environment, AWS Cloud9 creates the service\-linked role for you\.

## Editing a service\-linked role for AWS Cloud9<a name="edit-service-linked-role"></a>

You can't edit the AWSServiceRoleForAWSCloud9 service\-linked role in AWS Cloud9\. For example, after you create a service\-linked role, you can't change the name of the role because various entities might reference the role\. However, you can edit the description of the role using IAM\. For more information, see [Editing a Service\-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*\.

## Deleting a service\-linked role for AWS Cloud9<a name="delete-service-linked-role"></a>

If you no longer need to use a feature or service that requires a service\-linked role, we recommend that you delete that role\. That way you don’t have an unused entity that isn't actively monitored or maintained\.

### Deleting a service\-linked role in IAM<a name="delete-service-linked-role-service-console"></a>

Before you can use IAM to delete a service\-linked role, you must remove any AWS Cloud9 resources used by the role\. To remove AWS Cloud9 resources, see [Deleting an Environment](delete-environment.md)\.

You can use the IAM console to delete the AWSServiceRoleForAWSCloud9 service\-linked role\. For more information, see [Deleting a Service\-Linked Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*\.

## Supported Regions for AWS Cloud9 service\-linked roles<a name="slr-regions"></a>

AWS Cloud9 supports using service\-linked roles in all the Regions where the service is available\. For more information, see [AWS Cloud9](https://docs.aws.amazon.com/general/latest/gr/rande.html#cloud9_region) in the *Amazon Web Services General Reference*\.