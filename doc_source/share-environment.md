# Working with shared environment in AWS Cloud9<a name="share-environment"></a>

A *shared environment* is an AWS Cloud9 development environment that multiple users have been invited to participate in\. This topic provides instructions for sharing an environment in AWS Cloud9 and how to participate in a shared environment\.

To invite a user to participate in an environment you own, follow one of these sets of procedures, depending on the type of user you want to invite\.


****  

|  **User type**  |  **Follow these procedures**  | 
| --- | --- | 
|  A user in the same AWS account as the environment\.  |   [Invite a User in the Same Account as the Environment](#share-environment-invite-user)   | 
|  An AWS Cloud9 administrator in the same AWS account as the environment, specifically the following: [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/share-environment.html)  |  To invite the AWS Cloud9 administrator yourself, see [Invite a User in the Same Account as the Environment](#share-environment-invite-user)\. To have the AWS Cloud9 administrator invite themself \(or others in the same AWS account\), see [Have an AWS Cloud9 Administrator in the Same Account as the Environment Invite Themself or Others](#share-environment-admin-user)\.  | 

## Contents<a name="share-environment-contents"></a>
+  [Shared Environment Usage Scenarios](#share-environment-about) 
+  [About Environment Member Access Roles](#share-environment-member-roles) 
+  [Invite a User in the Same Account as the Environment](#share-environment-invite-user) 
+  [Have an AWS Cloud9 Administrator in the Same Account as the Environment Invite Themself or Others](#share-environment-admin-user) 
+  [Open a Shared Environment](#share-environment-open) 
+  [See a List of Environment Members](#share-environment-members-list) 
+  [Open the Active File of an Environment Member](#share-environment-active-file) 
+  [Open the Open File of an Environment Member](#share-environment-open-file) 
+  [Go to the Active Cursor of an Environment Member](#share-environment-active-cursor) 
+  [Chat with Other Environment Members](#share-environment-chat) 
+  [View Chat Messages in a Shared Environment](#share-environment-chat-view) 
+  [Delete a Chat Message from a Shared Environment](#share-environment-chat-delete) 
+  [Delete All Chat Messages from a Shared Environment](#share-environment-chat-delete-all) 
+  [Change the Access Role of an Environment Member](#share-environment-change-access) 
+  [Remove Your User From a Shared Environment](#share-environment-delete-you) 
+  [Remove Another Environment Member](#share-environment-delete-member) 
+  [Environment Sharing Best Practices](#share-environment-best-practices) 

## Shared Environment use cases<a name="share-environment-about"></a>

A shared environment is good for the following\.
+ Pair programming \(also known as *peer programming*\)\. This is where two users work together on the same code in a single environment\. In pair programming, typically one user writes code while the other user observes the code being written\. The observer gives immediate input and feedback to the code writer\. These positions frequently switch during a project\. Without a shared environment, teams of pair programmers typically sit in front of a single machine, and only one user at a time can write code\. With a shared environment, both users can sit in front of their own machine and can write code at the same time, even if they are in different physical offices\.
+ Computer science classes\. This is useful when teachers or teaching assistants want to access a student's environment to review their homework or fix issues with their environment in real time\. Students can also work together with their classmates on shared homework projects, writing code together in a single environment in real time\. They can do this even though they might be in different locations using different computer operating systems and web browser types\.
+ Any other situation where multiple users need to collaborate on the same code in real time\.

## About environment member access roles<a name="share-environment-member-roles"></a>

Before you share an environment or participate in a shared environment in AWS Cloud9, you should understand the access permission levels for a shared environment\. We call these permission levels *environment member access roles*\.

A shared environment in AWS Cloud9 offers three environment member access roles: *owner*, *read/write*, and *read\-only*\.
+ An owner has full control over an environment\. Each environment has one and only one owner, who is the environment creator\. An owner can do the following actions\.
  + Add, change, and remove members for the environment
  + Open, view, and edit files
  + Run code
  + Change environment settings
  + Chat with other members
  + Delete existing chat messages

  In the AWS Cloud9 IDE, an environment owner is displayed with **Read\+Write** access\.
+ A read/write member can do the following actions\.
  + Open, view, and edit files
  + Run code
  + Change various environment settings from within the AWS Cloud9 IDE
  + Chat with other members
  + Delete existing chat messages

  In the AWS Cloud9 IDE, read/write members are displayed with **Read\+Write** access\.
+ A read\-only member can do the following actions\.
  + Open and view files
  + Chat with other members
  + Delete existing chat messages

  In the AWS Cloud9 IDE, read\-only members are displayed with **Read Only** access\.

Before a user can become an environment owner or member, that user must meet one of the following criteria\.
+ The user is an **AWS account root user**\.
+ The user is an **IAM administrator user**\. For more information, see [Creating Your First IAM Admin User and Group](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html) in the *IAM User Guide*\.
+ The user is a **user who belongs to an IAM group**, a **user who assumes a role**, or a **federated user who assumes a role**, *and* that group or role has the AWS managed policy `AWSCloud9Administrator` or `AWSCloud9User` \(or `AWSCloud9EnvironmentMember`, to be a member only\) attached\. For more information, see [AWS Managed \(Predefined\) Policies](security-iam.md#auth-and-access-control-managed-policies)\.
  + To attach one of the preceding managed policies to an IAM group, you can use the [AWS Management Console](#share-environment-member-roles-console) or the [AWS Command Line Interface \(AWS CLI\)](#share-environment-member-roles-cli) as described in the following procedures\.
  + To create a role in IAM with one of the preceding managed policies for a user or a federated user to assume, see [Creating Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html) in the *IAM User Guide*\. To have a user or a federated user assume the role, see coverage of assuming roles in [Using IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html) in the *IAM User Guide*\.

### Attach an AWS managed policy for AWS Cloud9 to a group using the console<a name="share-environment-member-roles-console"></a>

1. Sign in to the AWS Management Console, if you are not already signed in\.

   For this step, we recommend you sign in using IAM administrator\-level credentials in your AWS account\. If you cannot do this, check with your AWS account administrator\.

1. Open the IAM console\. To do this, in the console navigation bar, choose **Services**\. Then choose **IAM**\.

1. Choose **Groups**\.

1. Choose the name of the group\.

1. On the **Permissions** tab, for **Managed Policies**, choose **Attach Policy**\.

1. In the list of policy names, choose one of the following boxes\.
   +  **AWSCloud9User** \(preferred\) or **AWSCloud9Administrator** to enable each user in the group to be an environment owner
   +  **AWSCloud9EnvironmentMember** to enable each user in the group to be a member only

   \(If you don't see one of these policy names in the list, type the policy name in the **Search** box to display it\.\)

1. Choose **Attach policy**\.

### Attach an AWS managed policy for AWS Cloud9 to a group using the AWS CLI<a name="share-environment-member-roles-cli"></a>

**Note**  
If you're using [AWS managed temporary credentials](security-iam.md#auth-and-access-control-temporary-managed-credentials), you can't use a terminal session in the AWS Cloud9 IDE to run some or all of the commands in this section\. To address AWS security best practices, AWS managed temporary credentials don’t allow some commands to be run\. Instead, you can run those commands from a separate installation of the AWS Command Line Interface \(AWS CLI\)\.

Run the IAM `attach-group-policy` command to attach the AWS managed policy for AWS Cloud9 to the group, specifying the group name and the Amazon Resource Name \(ARN\) of the policy:

```
aws iam attach-group-policy --group-name MyGroup --policy-arn arn:aws:iam::aws:policy/POLICY_NAME
```

In the preceding command, replace `MyGroup` with the name of the group\. Replace `POLICY_NAME` with the name of one of the following AWS managed policies\.
+  `AWSCloud9User` \(preferred\) or `AWSCloud9Administrator` to enable each user in the group to be an environment owner
+  `AWSCloud9EnvironmentMember` to enable each user in the group to be a member only

## Invite a user in the same account as the Environment<a name="share-environment-invite-user"></a>

Use the instructions in this section to share an AWS Cloud9 development environment that you own in your AWS account with a user in that same account\.

1. If the user you want to invite is **not** one of the following types of users, be sure the user you want to invite already has the corresponding environment member access role\. For instructions, see [About Environment Member Access Roles](#share-environment-member-roles)\.
   + The **AWS account root user**\.
   + An **IAM administrator user**\.
   + A **user who belongs to an IAM group**, a **user who assumes a role**, or a **federated user who assumes a role**, *and* that group or role has the AWS managed policy `AWSCloud9Administrator` attached\.

1. Open the environment that you own and want to invite the user to, if the environment isn't already open\.

1. In the menu bar in the AWS Cloud9 IDE, do one of the following\.
   + Choose **Window, Share**\.
   + Choose **Share** \(located next to the **Preferences** gear icon\)\.  
![\[The Share command in the AWS Cloud9 IDE menu bar\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-share.png)

1. In the **Share this environment** dialog box, for **Invite Members**, type one of the following\.
   + To invite an **IAM user**, enter the name of the user\.
   + To invite the **AWS account root user**, type `arn:aws:iam::123456789012:root`, replacing `123456789012` with your AWS account ID\.
   + To invite a **user with an assumed role** or a **federated user with an assumed role**, type `arn:aws:sts::123456789012:assumed-role/MyAssumedRole/MyAssumedRoleSession`, replacing `123456789012` with your AWS account ID, `MyAssumedRole` with the name of the assumed role, and `MyAssumedRoleSession` with the session name for the assumed role\.

1. To make this user a read\-only member, choose **R**\. To make this user read/write, choose **RW**\.

1. Choose **Invite**\.
**Note**  
If you make this user a read/write member, a dialog box is displayed, containing information about possibly putting your AWS security credentials at risk\. The following information provides more background about this issue\.  
You should share an environment only with those you trust\.  
A read/write member may be able to use the AWS CLI, the aws\-shell, or AWS SDK code in your environment to take actions in AWS on your behalf\. Furthermore, if you store your permanent AWS access credentials within the environment, that member could potentially copy those credentials and use them outside of the environment\.  
Removing your permanent AWS access credentials from your environment and using temporary AWS access credentials instead does not fully address this issue\. It lessens the opportunity of the member to copy those temporary credentials and use them outside of the environment \(as those temporary credentials will work only for a limited time\)\. However, temporary credentials still enable a read/write member to take actions in AWS from the environment on your behalf\.

1. Contact the user to let them know they can open this environment and begin using it\.

## Have an AWS Cloud9 administrator in the same account as the Environment invite themself or others<a name="share-environment-admin-user"></a>

**Note**  
If you're using [AWS managed temporary credentials](security-iam.md#auth-and-access-control-temporary-managed-credentials), you can't use a terminal session in the AWS Cloud9 IDE to run some or all of the commands in this section\. To address AWS security best practices, AWS managed temporary credentials don’t allow some commands to be run\. Instead, you can run those commands from a separate installation of the AWS Command Line Interface \(AWS CLI\)\.

The following types of users can invite themselves \(or other users in the same AWS account\) to any environment in the same account\.
+ The **AWS account root user**\.
+ An **IAM administrator user**\.
+ A **user who belongs to an IAM group**, a **user who assumes a role**, or a **federated user who assumes a role**, *and* that group or role has the AWS managed policy `AWSCloud9Administrator` attached\.

If the invited user is **not** one of the preceding types of users, be sure that user already has the corresponding environment member access role\. For instructions, see [About Environment Member Access Roles](#share-environment-member-roles)\.

To invite the user, use the AWS CLI or the aws\-shell to run the AWS Cloud9 `create-environment-membership` command\.

```
aws cloud9 create-environment-membership --environment-id 12a34567b8cd9012345ef67abcd890e1 --user-arn USER_ARN --permissions PERMISSION_LEVEL
```

In the preceding command, replace `12a34567b8cd9012345ef67abcd890e1` with the ID of the environment, and `PERMISSION_LEVEL` with `read-write` or `read-only`\. Replace `USER_ARN` with one of the following:
+ To invite an **IAM user**, type `arn:aws:iam::123456789012:user/MyUser`, replacing `123456789012` with your AWS account ID and `MyUser` with the name of the user\.
+ To invite the **AWS account root user**, type `arn:aws:iam::123456789012:root`, replacing `123456789012` with your AWS account ID\.
+ To invite a **user with an assumed role** or a **federated user with an assumed role**, type `arn:aws:sts::123456789012:assumed-role/MyAssumedRole/MyAssumedRoleSession`, replacing `123456789012` with your AWS account ID, `MyAssumedRole` with the name of the assumed role, and `MyAssumedRoleSession` with the session name for the assumed role\.

For example, to invite the AWS account root user for account ID `123456789012` to an environment with ID `12a34567b8cd9012345ef67abcd890e1` as a read/write member, run the following command\.

```
aws cloud9 create-environment-membership --environment-id 12a34567b8cd9012345ef67abcd890e1 --user-arn arn:aws:iam::123456789012:root --permissions read-write
```

**Note**  
If you're using the aws\-shell, omit the `aws` prefix from the preceding commands\.

## Open a shared Environment<a name="share-environment-open"></a>

To open a shared environment, you use your AWS Cloud9 dashboard\. You then use the AWS Cloud9 IDE to do things in a shared environment such as work with files and chat with other members\.

1. Be sure the corresponding access policy is attached to the group or role for your user\. For more information, see [About Environment Member Access Roles](#share-environment-member-roles)\.

1. Sign in to the AWS Cloud9 console as follows:
   + If you're the only individual using your AWS account or you are an IAM user in a single AWS account, go to [https://console\.aws\.amazon\.com/cloud9/](https://console.aws.amazon.com/cloud9/)\.
   + If your organization uses AWS Single Sign\-On \(SSO\), see your AWS account administrator for sign\-in instructions\.
   + If you're a student in a classroom, see your instructor for sign\-in instructions\.

1. Open the shared environment from your AWS Cloud9 dashboard\. For more information, see [Opening an Environment in AWS Cloud9](open-environment.md)\.

You use the **Collaborate** window to interact with other members, as described in the rest of this topic\.

**Note**  
If the **Collaborate** window isn't visible, choose the **Collaborate** button\. If the **Collaborate** button isn't visible, on the menu bar, choose **Window, Collaborate**\.

![\[The Collaborate window in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-collaborate.png)

## See a list of environment members<a name="share-environment-members-list"></a>

With the shared environment open, in the **Collaborate** window, expand **Environment Members**, if the list of members isn't visible\.

A circle next to each member indicates their online status, as follows\.
+ Active members have a green circle\.
+ Offline members have a gray circle\.
+ Idle members have an orange circle\.

![\[Member online status in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-collaborate-status.png)

To use code to get a list of environment members, call the AWS Cloud9 describe environment memberships operation, as follows\.


****  

|  |  | 
| --- |--- |
|  AWS CLI  |   [describe\-environment\-memberships](https://docs.aws.amazon.com/cli/latest/reference/cloud9/describe-environment-memberships.html)   | 
|  AWS SDK for C\+\+  |   [DescribeEnvironmentMembershipsRequest](https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_describe_environment_memberships_request.html), [DescribeEnvironmentMembershipsResult](https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_describe_environment_memberships_result.html)   | 
|  AWS SDK for Go  |   [DescribeEnvironmentMemberships](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.DescribeEnvironmentMemberships), [DescribeEnvironmentMembershipsRequest](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.DescribeEnvironmentMembershipsRequest), [DescribeEnvironmentMembershipsWithContext](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.DescribeEnvironmentMembershipsWithContext)   | 
|  AWS SDK for Java  |   [DescribeEnvironmentMembershipsRequest](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/DescribeEnvironmentMembershipsRequest.html), [DescribeEnvironmentMembershipsResult](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/DescribeEnvironmentMembershipsResult.html)   | 
|  AWS SDK for JavaScript  |   [describeEnvironmentMemberships](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Cloud9.html#describeEnvironmentMemberships-property)   | 
|  AWS SDK for \.NET  |   [DescribeEnvironmentMembershipsRequest](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TDescribeEnvironmentMembershipsRequest.html), [DescribeEnvironmentMembershipsResponse](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TDescribeEnvironmentMembershipsResponse.html)   | 
|  AWS SDK for PHP  |   [describeEnvironmentMemberships](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-cloud9-2017-09-23.html#describeenvironmentmemberships)   | 
|  AWS SDK for Python \(Boto\)  |   [describe\_environment\_memberships](https://boto3.readthedocs.io/en/latest/reference/services/cloud9.html#Cloud9.Client.describe_environment_memberships)   | 
|  AWS SDK for Ruby  |   [describe\_environment\_memberships](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Cloud9/Client.html#describe_environment_memberships-instance_method)   | 
|  AWS Tools for Windows PowerShell  |   [Get\-C9EnvironmentMembershipList](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-C9EnvironmentMembershipList.html)   | 
|  AWS Cloud9 API  |   [DescribeEnvironmentMemberships](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_DescribeEnvironmentMemberships.html)   | 

## Open the active file of an environment member<a name="share-environment-active-file"></a>

With the shared environment open, in the menu bar, choose the member name\. Then choose **Open Active File**\.

![\[The Open Active File command in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-collaborate-active-file.png)

## Open the open file of an environment member<a name="share-environment-open-file"></a>

1. With the shared environment open, in the **Collaborate** window, expand **Environment Members**, if the list of members isn't visible\.

1. Expand the name of the user whose open file you want to open in your environment\.

1. Double\-click the name of the file you want to open\.

![\[Opening a team member's file in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-collaborate-open-file.png)

## Go to the active cursor of an environment member<a name="share-environment-active-cursor"></a>

1. With the shared environment open, in the **Collaborate** window, expand **Environment Members**, if the list of members isn't visible\.

1. Right\-click the member name, and then choose **Show Location**\.

## Chat with other environment members<a name="share-environment-chat"></a>

With the shared environment open, at the bottom of the **Collaborate** window, for **Enter your message here**, enter your chat message, and then press `Enter`\.

![\[The chat area in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-collaborate-chat.png)

## View chat messages in a shared Environment<a name="share-environment-chat-view"></a>

With the shared environment open, in the **Collaborate** window, expand **Group Chat**, if the list of chat messages is not visible\.

## Delete a chat messages from a shared Environment<a name="share-environment-chat-delete"></a>

With the shared environment open, in the **Collaborate** window, right\-click the chat message in **Group Chat**, and then choose **Delete Message**\.

**Note**  
When you delete a chat message, it is deleted from the environment for all members\.

## Delete all chat messages from a shared Environment<a name="share-environment-chat-delete-all"></a>

With the shared environment open, in the **Collaborate** window, right\-click anywhere in **Group Chat**, and then choose **Clear history**\.

**Note**  
When you delete all chat messages, they are deleted from the environment for all members\.

## Change the access role of an environment member<a name="share-environment-change-access"></a>

1. Open the environment that you own and that contains the member whose access role you want to change, if the environment is not already open\. For more information, see [Opening an Environment in AWS Cloud9](open-environment.md)\.

1. In the **Collaborate** window, expand **Environment Members**, if the list of members isn't visible\.

1. Do one of the following actions:
   + Next to the member name whose access role you want to change, choose **R** or **RW** to make this member read-only or read/write, respectively\.
   + To change a read/write member to read\-only, right\-click the member name, and then choose **Revoke Write Access**\.
   + To change a read\-only member to read/write, right\-click the member name, and then choose **Grant Read\+Write Access**\.
**Note**  
If you make this user a read/write member, a dialog box is displayed, containing information about possibly putting your AWS security credentials at risk\. Don't make a user a read/write member unless you trust that user to take actions in AWS on your behalf\. For more information, see the related note in [Invite a User in the Same Account as the Environment](#share-environment-invite-user)\.

To use code to change the access role of an environment member, call the AWS Cloud9 update environment membership operation, as follows\.


****  

|  |  | 
| --- |--- |
|  AWS CLI  |   [update\-environment\-membership](https://docs.aws.amazon.com/cli/latest/reference/cloud9/update-environment-membership.html)   | 
|  AWS SDK for C\+\+  |   [UpdateEnvironmentMembershipRequest](https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_update_environment_membership_request.html), [UpdateEnvironmentMembershipResult](https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_update_environment_membership_result.html)   | 
|  AWS SDK for Go  |   [UpdateEnvironmentMembership](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.UpdateEnvironmentMembership), [UpdateEnvironmentMembershipRequest](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.UpdateEnvironmentMembershipRequest), [UpdateEnvironmentMembershipWithContext](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.UpdateEnvironmentMembershipWithContext)   | 
|  AWS SDK for Java  |   [UpdateEnvironmentMembershipRequest](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/UpdateEnvironmentMembershipRequest.html), [UpdateEnvironmentMembershipResult](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/UpdateEnvironmentMembershipResult.html)   | 
|  AWS SDK for JavaScript  |   [updateEnvironmentMembership](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Cloud9.html#updateEnvironmentMembership-property)   | 
|  AWS SDK for \.NET  |   [UpdateEnvironmentMembershipRequest](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TUpdateEnvironmentMembershipRequest.html), [UpdateEnvironmentMembershipResponse](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TUpdateEnvironmentMembershipResponse.html)   | 
|  AWS SDK for PHP  |   [updateEnvironmentMembership](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-cloud9-2017-09-23.html#updateenvironmentmembership)   | 
|  AWS SDK for Python \(Boto\)  |   [update\_environment\_membership](https://boto3.readthedocs.io/en/latest/reference/services/cloud9.html#Cloud9.Client.update_environment_membership)   | 
|  AWS SDK for Ruby  |   [update\_environment\_membership](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Cloud9/Client.html#update_environment_membership-instance_method)   | 
|  AWS Tools for Windows PowerShell  |   [Update\-C9EnvironmentMembership](https://docs.aws.amazon.com/powershell/latest/reference/items/Update-C9EnvironmentMembership.html)   | 
|  AWS Cloud9 API  |   [UpdateEnvironmentMembership](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_UpdateEnvironmentMembership.html)   | 

## Remove your user from a shared Environment<a name="share-environment-delete-you"></a>

**Note**  
You cannot remove your user from an environment if you're the environment owner\.  
Removing your user from an environment doesn't remove your user from IAM\.

1. With the shared environment open, in the **Collaborate** window, expand **Environment Members**, if the list of members isn't visible\.

1. Do one of the following actions\.
   + Next to **You**, choose the trash can icon\.
   + Right\-click **You**, and then choose **Leave environment**\.

1. When prompted, choose **Leave**\.

To use code to remove your user from a shared environment, call the AWS Cloud9 delete environment membership operation, as follows\.


****  

|  |  | 
| --- |--- |
|  AWS CLI  |   [delete\-environment\-membership](https://docs.aws.amazon.com/cli/latest/reference/cloud9/delete-environment-membership.html)   | 
|  AWS SDK for C\+\+  |   [DeleteEnvironmentMembershipRequest](https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_delete_environment_membership_request.html), [DeleteEnvironmentMembershipResult](https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_delete_environment_membership_result.html)   | 
|  AWS SDK for Go  |   [DeleteEnvironmentMembership](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.DeleteEnvironmentMembership), [DeleteEnvironmentMembershipRequest](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.DeleteEnvironmentMembershipRequest), [DeleteEnvironmentMembershipWithContext](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.DeleteEnvironmentMembershipWithContext)   | 
|  AWS SDK for Java  |   [DeleteEnvironmentMembershipRequest](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/DeleteEnvironmentMembershipRequest.html), [DeleteEnvironmentMembershipResult](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/DeleteEnvironmentMembershipResult.html)   | 
|  AWS SDK for JavaScript  |   [deleteEnvironmentMembership](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Cloud9.html#deleteEnvironmentMembership-property)   | 
|  AWS SDK for \.NET  |   [DeleteEnvironmentMembershipRequest](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TDeleteEnvironmentMembershipRequest.html), [DeleteEnvironmentMembershipResponse](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TDeleteEnvironmentMembershipResponse.html)   | 
|  AWS SDK for PHP  |   [deleteEnvironmentMembership](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-cloud9-2017-09-23.html#deleteenvironmentmembership)   | 
|  AWS SDK for Python \(Boto\)  |   [delete\_environment\_membership](https://boto3.readthedocs.io/en/latest/reference/services/cloud9.html#Cloud9.Client.delete_environment_membership)   | 
|  AWS SDK for Ruby  |   [delete\_environment\_membership](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Cloud9/Client.html#delete_environment_membership-instance_method)   | 
|  AWS Tools for Windows PowerShell  |   [Remove\-C9EnvironmentMembership](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-C9EnvironmentMembership.html)   | 
|  AWS Cloud9 API  |   [DeleteEnvironmentMembership](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_DeleteEnvironmentMembership.html)   | 

## Remove another environment member<a name="share-environment-delete-member"></a>

**Note**  
To remove any member other than your user from an environment, you must be signed in to AWS Cloud9 using the credentials of the environment owner\.  
Removing a member does not remove the user from IAM\.

1. Open the environment that contains the member you want to remove, if the environment is not already open\. For more information, see [Opening an Environment in AWS Cloud9](open-environment.md)\.

1. In the **Collaborate** window, expand **Environment Members**, if the list of members is not visible\.

1. Do one of the following\.
   + Next to the name of the member you want to delete, choose the trash can icon\.
   + Right\-click the name of the member you want to delete, and then choose **Revoke Access**\.

1. When prompted, choose **Remove Member**\.

To use code to remove a member from an environment, call the AWS Cloud9 delete environment membership operation, as follows\.


****  

|  |  | 
| --- |--- |
|  AWS CLI  |   [delete\-environment\-membership](https://docs.aws.amazon.com/cli/latest/reference/cloud9/delete-environment-membership.html)   | 
|  AWS SDK for C\+\+  |   [DeleteEnvironmentMembershipRequest](https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_delete_environment_membership_request.html), [DeleteEnvironmentMembershipResult](https://sdk.amazonaws.com/cpp/api/LATEST/class_aws_1_1_cloud9_1_1_model_1_1_delete_environment_membership_result.html)   | 
|  AWS SDK for Go  |   [DeleteEnvironmentMembership](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.DeleteEnvironmentMembership), [DeleteEnvironmentMembershipRequest](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.DeleteEnvironmentMembershipRequest), [DeleteEnvironmentMembershipWithContext](https://docs.aws.amazon.com/sdk-for-go/api/service/cloud9/#Cloud9.DeleteEnvironmentMembershipWithContext)   | 
|  AWS SDK for Java  |   [DeleteEnvironmentMembershipRequest](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/DeleteEnvironmentMembershipRequest.html), [DeleteEnvironmentMembershipResult](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/cloud9/model/DeleteEnvironmentMembershipResult.html)   | 
|  AWS SDK for JavaScript  |   [deleteEnvironmentMembership](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Cloud9.html#deleteEnvironmentMembership-property)   | 
|  AWS SDK for \.NET  |   [DeleteEnvironmentMembershipRequest](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TDeleteEnvironmentMembershipRequest.html), [DeleteEnvironmentMembershipResponse](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Cloud9/TDeleteEnvironmentMembershipResponse.html)   | 
|  AWS SDK for PHP  |   [deleteEnvironmentMembership](https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-cloud9-2017-09-23.html#deleteenvironmentmembership)   | 
|  AWS SDK for Python \(Boto\)  |   [delete\_environment\_membership](https://boto3.readthedocs.io/en/latest/reference/services/cloud9.html#Cloud9.Client.delete_environment_membership)   | 
|  AWS SDK for Ruby  |   [delete\_environment\_membership](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Cloud9/Client.html#delete_environment_membership-instance_method)   | 
|  AWS Tools for Windows PowerShell  |   [Remove\-C9EnvironmentMembership](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-C9EnvironmentMembership.html)   | 
|  AWS Cloud9 API  |   [DeleteEnvironmentMembership](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_DeleteEnvironmentMembership.html)   | 

## Environment sharing best practices<a name="share-environment-best-practices"></a>

We recommend the following practices when sharing environments\.
+ Only invite read/write members you trust to your environments\.
+ For EC2 environments, read/write members can use the environment owner's AWS access credentials, instead of their own credentials, to make calls from the environment to AWS services\. To prevent this, the environment owner can disable AWS managed temporary credentials for the environment\. However, this also prevents the environment owner from making calls\. For more information, see [AWS Managed Temporary Credentials](security-iam.md#auth-and-access-control-temporary-managed-credentials)\.
+ Turn on AWS CloudTrail to track activity in your environments\. For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/)\.
+ Do not use your AWS account root user to create and share environments\. Use IAM users in the account instead\. For more information, see [First\-Time Access Only: Your Root User Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_identity-management.html#intro-identity-first-time-access) and [IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_identity-management.html#intro-identity-users) in the *IAM User Guide*\.
