# Authenticating with identities<a name="sec-auth-identities"></a>

You can access AWS as any of the following types of identities\.

 **AWS account root user** 

When you sign up for AWS, you provide an email address and password that is associated with your AWS account\. These are your root credentials, and they provide complete access to all of your AWS resources\.

**Important**  
As an AWS security best practice, we recommend that you use the root credentials only to create an IAM *administrator group* with an IAM *administrator user*\. This is a group that gives the user full permissions to your AWS account\. Then you can use this administrator user to create other IAM users and roles with limited permissions\. For more information, see [Create Individual IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#create-iam-users) and [Creating Your First IAM Admin User and Group](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html) in the *IAM User Guide*\.

 **IAM user** 

An *IAM user* is simply an identity within your AWS account that has specific custom permissions \(for example, permissions to create an AWS Cloud9 development environment\)\. You can use an IAM user name and password to sign in to secure AWS webpages like the AWS Cloud9 console, AWS Management Console, AWS Discussion Forums, and AWS Support Center\.

In addition to a user name and password, you can also generate access keys for each user\. You can use these keys when you access AWS services programmatically, either through one of the several AWS SDKs or by using the AWS Command Line Interface \(AWS CLI\) or the aws\-shell\. The AWS SDKs, the AWS CLI, and the aws\-shell use these access keys to cryptographically sign your request\. If you don't use these tools, you must sign the request yourself\. AWS Cloud9 supports Signature Version 4, a protocol for authenticating inbound API requests\. For more information about authenticating requests, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon Web Services General Reference*\.

 **IAM role** 

An *IAM role* is another IAM identity you can create in your account that has specific permissions\. It's similar to an IAM user, but it isn't associated with a specific person\. An IAM role enables you to obtain temporary access keys that can be used to access AWS services and resources\. IAM roles with temporary credentials are useful in the following situations\.

 **AWS service access** 

You can use an IAM role in your account to grant an AWS service permissions to access your account's resources\. For example, you can create a role that allows AWS Lambda to access an Amazon S3 bucket on your behalf, and then load data stored in the bucket into an Amazon Redshift data warehouse\. For more information, see [Creating a Role to Delegate Permissions to an AWS Service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*\.

 **Applications running on Amazon EC2** 

Instead of storing access keys within an Amazon EC2 instance for use by applications running on the instance and making AWS API requests, you can use an IAM role to manage temporary credentials for these applications\. To assign an AWS role to an Amazon EC2 instance and make it available to all of its applications, you can create an *instance profile* that is attached to the instance\. An instance profile contains the role and enables programs running on the Amazon EC2 instance to get temporary credentials\. For more information, see [Create and Use an Instance Profile to Manage Temporary Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/credentials.html#credentials-temporary) and [Using an IAM Role to Grant Permissions to Applications Running on Amazon EC2 Instances](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html) in the *IAM User Guide*\.

**Note**  
Instead of attaching an instance profile to an Amazon EC2 instance that connects to an environment, AWS Cloud9 can automatically set up and manage temporary credentials on your behalf in an EC2 environment\. For more information, see [AWS managed temporary credentials](how-cloud9-with-iam.md#sec-auth-and-access-control-temporary-managed-credentials)\.

 **Federated user access** 

Instead of creating an IAM user, you can use pre\-existing user identities from AWS Directory Service, your enterprise user directory, or a web identity provider\. These are known as *federated users*\. AWS assigns a role to a federated user when access is requested through an identity provider\. For more information, see [Federated Users and Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_access-management.html#intro-access-roles) in the *IAM User Guide*\.