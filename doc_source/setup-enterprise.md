# Enterprise Setup for AWS Cloud9<a name="setup-enterprise"></a>

This topic explains how to use [AWS Single Sign\-On \(SSO\)](https://aws.amazon.com/single-sign-on/) to enable one or more AWS accounts to use AWS Cloud9 within an enterprise\. To set up to use AWS Cloud9 for any other usage pattern, see [Setting Up AWS Cloud9](setting-up.md) for the correct instructions\.

These instructions assume that you have \(or will have\) administrative access to the organization in AWS Organizations\. If you don't already have administrative access to the organization in AWS Organizations, see your AWS account administrator\. For more information, see the following resources:
+  [Managing Access Permissions for Your AWS Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions_overview.html) in the *AWS Organizations User Guide* \(AWS SSO requires the use of AWS Organizations\)
+  [Overview of Managing Access Permissions to Your AWS SSO Resources](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access-overview.html) in the *AWS Single Sign\-On User Guide* 

For introductory information related to this topic, see the following resources:
+  [What Is AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) in the *AWS Organization User Guide* \(AWS SSO requires the use of AWS Organizations\)
+  [What Is AWS Single Sign\-On](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) in the *AWS Single Sign\-On User Guide* 
+ The 4\-minute video [AWS Knowledge Center Videos: How do I get started with AWS Organizations](https://www.youtube.com/watch?v=mScBPL8VV48) on the YouTube website
+ The 7\-minute video [Manage User Access to Multiple AWS Accounts Using AWS Single Sign\-on](https://www.youtube.com/watch?v=bXrsUEI1V38) on the YouTube website
+ The 9\-minute video [How to Setup AWS Single Sign On for Your On\-Premise Active Directory Users](https://www.youtube.com/watch?v=nuPjljOVZmU) on the YouTube website

The following conceptual diagram shows what you'll end up with\.

![\[Conceptual diagram of setting up an enterprise to use AWS Cloud9\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/enterprise.png)

To enable one or more AWS accounts to start using AWS Cloud9 within an enterprise, start with one of the following steps, depending on which AWS resources you already have\.


****  

|  **Do you have an AWS account that can or does serve as the master account for the organization in AWS Organizations?**  |  **Do you have an organization in AWS Organizations for that master account?**  |  **Are all of the wanted AWS accounts members of that organization?**  |  **Is that organization set up to use AWS SSO?**  |  **Is that organization set up with all of the wanted groups and users who want to use AWS Cloud9?**  |  **Start with this step**  | 
| --- | --- | --- | --- | --- | --- | 
|  No  |  —  |  —  |  —  |  —  |   [Step 1: Create a Master Account for the Organization](#setup-enterprise-create-account)   | 
|  Yes  |  No  |  —  |  —  |  —  |   [Step 2: Create an Organization for the Master Account](#setup-enterprise-create-organization)   | 
|  Yes  |  Yes  |  No  |  —  |  —  |   [Step 3: Add Member Accounts to the Organization](#setup-enterprise-add-to-organization)   | 
|  Yes  |  Yes  |  Yes  |  No  |  —  |   [Step 4: Enable AWS SSO Across the Organization](#setup-enterprise-set-up-sso)   | 
|  Yes  |  Yes  |  Yes  |  Yes  |  No  |   [Step 5\. Set Up Groups and Users Within the Organization](#setup-enterprise-set-up-groups-users)   | 
|  Yes  |  Yes  |  Yes  |  Yes  |  Yes  |   [Step 6\. Enable Groups and Users Within the Organization to Use AWS Cloud9](#setup-enterprise-groups-users-access)   | 

## Step 1: Create a Master Account for the Organization<a name="setup-enterprise-create-account"></a>

**Note**  
Your enterprise might already have a master account set up for you\. If your enterprise has an AWS account administrator, check with that person before starting the following procedure\. If you already have a master account, skip ahead to [Step 2: Create an Organization for the Master Account](#setup-enterprise-create-organization)\.

To use AWS Single Sign\-On \(AWS SSO\), you must have an AWS account that will serve as the master account for an organization in AWS Organizations\. For more information, see the discussion about *master accounts* in [AWS Organizations Terminology and Concepts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) in the *AWS Organizations User Guide*\.

To watch a 4\-minute video related to the following procedure, see [Creating an Amazon Web Services Account](https://www.youtube.com/watch?v=WviHsoz8yHk) on the YouTube website\.

To create a master account:

1. Go to [https://aws\.amazon\.com](https://aws.amazon.com)\.

1. Choose **Sign In to the Console**\.

1. Choose **Create a new AWS account**\.

1. Complete the process by following the on\-screen directions\. This includes giving AWS your email address and credit card information\. You must also use your phone to enter a code that AWS gives you\.

After you finish creating the account, AWS will send you a confirmation email\. Do not go to the next step until you get this confirmation\.

## Step 2: Create an Organization for the Master Account<a name="setup-enterprise-create-organization"></a>

**Note**  
Your enterprise might already have AWS Organizations set up to use the master account\. If your enterprise has an AWS account administrator, check with that person before starting the following procedure\. If you already have AWS Organizations set up to use the master account, skip ahead to [Step 3: Add Member Accounts to the Organization](#setup-enterprise-add-to-organization)\.

To use AWS SSO, you must have an organization in AWS Organizations that uses the master account\. For more information, see the discussion about *organizations* in [AWS Organizations Terminology and Concepts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) in the *AWS Organizations User Guide*\.

To create an organization in AWS Organizations for the master AWS account, follow these instructions in the *AWS Organizations User Guide*:

1.  [Creating an Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_create.html) 

1.  [Enabling All Features in Your Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) 

To watch a 4\-minute video related to these procedures, see [AWS Knowledge Center Videos: How do I get started with AWS Organizations](https://www.youtube.com/watch?v=mScBPL8VV48) on the YouTube website\.

## Step 3: Add Member Accounts to the Organization<a name="setup-enterprise-add-to-organization"></a>

**Note**  
Your enterprise might already have AWS Organizations set up with the wanted member accounts\. If your enterprise has an AWS account administrator, check with that person before starting the following procedure\. If you already have AWS Organizations set up with the wanted member accounts, skip ahead to [Step 4: Enable AWS SSO Across the Organization](#setup-enterprise-set-up-sso)\.

In this step, you add any AWS accounts that will serve as member accounts for the organization in AWS Organizations\. For more information, see the discussion about *member accounts* in [AWS Organizations Terminology and Concepts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) in the *AWS Organizations User Guide*\.

**Note**  
You don't have to add any member accounts to the organization\. You can use AWS SSO with just the single master account in the organization\. Later, you can add member accounts to the organization, if you want\. If you don't want to add any member accounts now, skip ahead to [Step 4: Enable AWS SSO Across the Organization](#setup-enterprise-set-up-sso)\.

To add member accounts to the organization in AWS Organizations, follow one or both of the following sets of instructions in the *AWS Organizations User Guide*\. Repeat these instructions as many times as needed until you have all of the AWS accounts you want as members of the organization:
+  [Creating an AWS Account in Your Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html) 
+  [Inviting an AWS Account to Join Your Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html) 

## Step 4: Enable AWS SSO across the Organization<a name="setup-enterprise-set-up-sso"></a>

**Note**  
Your enterprise might already have AWS Organizations set up to use AWS SSO\. If your enterprise has an AWS account administrator, check with that person before starting the following procedure\. If you already have AWS Organizations set up to use AWS SSO, skip ahead to [Step 5\. Set Up Groups and Users Within the Organization](#setup-enterprise-set-up-groups-users)\.

In this step, you enable the organization in AWS Organizations to use AWS SSO\. To do this, follow these sets of instructions in the *AWS Single Sign\-On User Guide*:

1.  [AWS SSO Prerequisites](https://docs.aws.amazon.com/singlesignon/latest/userguide/prereqs.html) 

1.  [Enable AWS SSO](https://docs.aws.amazon.com/singlesignon/latest/userguide/step1.html) 

## Step 5\. Set Up Groups and Users within the Organization<a name="setup-enterprise-set-up-groups-users"></a>

**Note**  
Your enterprise might already have AWS Organizations set up with groups and users from either an AWS SSO directory or an AWS Managed Microsoft AD or AD Connector directory that is managed in AWS Directory Service\. If your enterprise has an AWS account administrator, check with that person before starting the following procedure\. If you already have AWS Organizations set up with groups and users from either an AWS SSO directory or AWS Directory Service, skip ahead to [Step 6\. Enable Groups and Users within the Organization to Use AWS Cloud9](#setup-enterprise-groups-users-access)\.

In this step, you either create groups and users in an AWS SSO directory for the organization, or you connect to an AWS Managed Microsoft AD or AD Connector directory that is managed in AWS Directory Service for the organization\. In a later step, you give groups the necessary access permissions to use AWS Cloud9\.
+ If you're using an AWS SSO directory for the organization, follow these sets of instructions in the *AWS Single Sign\-On User Guide*\. Repeat these steps as many times as needed until you have all of the groups and users you want:

  1.  [Add Groups](https://docs.aws.amazon.com/singlesignon/latest/userguide/addgroups.html)\. We recommend creating at least one group for any AWS Cloud9 administrators across the organization, and then repeating this step to create another group for all AWS Cloud9 users across the organization\. Optionally, you might also repeat this step to create a third group for all users across the organization with whom you want to share existing AWS Cloud9 development environments, but not allow them to create environments on their own\. For ease of use, we recommend naming these groups `AWSCloud9Administrators`, `AWSCloud9Users`, and `AWSCloud9EnvironmentMembers`, respectively\. For more information, see [AWS Managed \(Predefined\) Policies for AWS Cloud9](auth-and-access-control.md#auth-and-access-control-managed-policies)\.

  1.  [Add Users](https://docs.aws.amazon.com/singlesignon/latest/userguide/addusers.html)\. 

  1.  [Add Users to Groups](https://docs.aws.amazon.com/singlesignon/latest/userguide/adduserstogroups.html)\. Add any AWS Cloud9 administrators to the `AWSCloud9Administrators` group, repeat this step to add AWS Cloud9 users to the `AWSCloud9Users` group, and optionally repeat this step to add any remaining users to the `AWSCloud9EnvironmentMembers` group\. Adding users to groups is an AWS security best practice that can help you better control, track, and troubleshoot issues with AWS resource access\.
+ If you're using an AWS Managed Microsoft AD or AD Connector directory that you manage in AWS Directory Service for the organization, follow the instructions in [Connect to Your Microsoft AD Directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-directory-connected.html) in the *AWS Single Sign\-On User Guide*\.

## Step 6\. Enable Groups and Users within the Organization to Use AWS Cloud9<a name="setup-enterprise-groups-users-access"></a>

By default, most users and groups in an organization in AWS Organizations don't have access to any AWS services, including AWS Cloud9\. In this step, you use AWS SSO to allow groups and users across an organization in AWS Organizations to use AWS Cloud9 within any combination of participating accounts\.

1. In the [AWS SSO console](https://console.aws.amazon.com/singlesignon), choose **AWS accounts** in the service navigation pane\.

1. Choose the **Permission sets** tab\.

1. Choose **Create permission set** set\.

1. Select **Create a custom permission set**\.

1. Enter a **Name** for this permission set\. We recommend creating at least one permission set for any AWS Cloud9 administrators across the organization, and then repeating steps 3 through 10 in this procedure to create another permission set for all AWS Cloud9 users across the organization\. Optionally, you might also repeat steps 3 through 10 in this procedure to create a third permission set for all users across the organization with whom you want to share existing AWS Cloud9 development environments, but not allow them to create environments on their own\. For ease of use, we recommend naming these permission sets `AWSCloud9AdministratorsPerms`, `AWSCloud9UsersPerms`, and `AWSCloud9EnvironmentMembersPerms`, respectively\. For more information, see [AWS Managed \(Predefined\) Policies for AWS Cloud9](auth-and-access-control.md#auth-and-access-control-managed-policies)\.

1. Enter an optional **Description** for the permission set\.

1. Choose a **Session duration** for the permission set, or leave the default session duration of **1 hour**\.

1. Select **Attach AWS managed policies**\.

1. In the list of policies, select one of the following boxes next to the correct **Policy name** entry\. \(Don't choose the policy name itself\. If you don't see a policy name in the list, enter the policy name in the **Search** box to display it\.\)
   + For the `AWSCloud9AdministratorsPerms` permission set, select **AWSCloud9Administrator**\.
   + For the `AWSCloud9UsersPerms` permission set, select **AWSCloud9User**\.
   + Optionally, for the `AWSCloud9EnvironmentMembersPerms` permission set, select **AWSCloud9EnvironmentMember**\.
**Note**  
To learn about policies that you can add in addition to the policies that are required by AWS Cloud9, see [Managed Policies and Inline Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html) and [Understanding Permissions Granted by a Policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_understand.html) in the *IAM User Guide*\.

1. Choose **Create**\.

1. After you finish creating all of the permission sets you want, on the **AWS organization** tab, choose the AWS account that you want to assign AWS Cloud9 access permissions to\. \(If the **AWS organization** tab isn't visible, then in the service navigation pane, choose **AWS accounts**\. This displays the **AWS organization** tab\)\.

1. Choose **Assign users**\.

1. On the **Groups** tab, select the box next to the name of the group that you want to assign AWS Cloud9 access permissions to, as follows\. \(Don't choose the group name itself\.\)
   + If you're using an AWS SSO directory for the organization, you might have a created a group named **AWSCloud9Administrators** for AWS Cloud9 administrators\.
   + If you're using an AWS Managed Microsoft AD or AD Connector directory that you manage in AWS Directory Service for the organization, choose the directory's ID, enter part or all of the group's name, and choose **Search connected directory**\. Then select the box next to the name of the group that you want to assign AWS Cloud9 access permissions to\.
**Note**  
We recommend assigning AWS Cloud9 access permissions to groups instead of to individual users\. This AWS security best practice can help you better control, track, and troubleshoot issues with AWS resource access\.

1. Choose **Next: Permission sets**\.

1. Select the box next to the name of the permission set that you want to assign to this group, for example, **AWSCloud9AdministratorsPerms** for a group of AWS Cloud9 administrators\. \(Don't choose the permission set name itself\.\)

1. Choose **Finish**\.

1. Choose **Proceed to AWS accounts**\.

1. Repeat steps 11 through 17 in this procedure for any additional AWS Cloud9 access permissions that you want to assign to AWS accounts across the organization\.

## Step 7: Start Using AWS Cloud9<a name="setup-enterprise-sign-in-ide"></a>

After you complete the previous steps in this topic, you and your users are ready to sign in to AWS SSO and start using AWS Cloud9\.

1. If you are already signed in to an AWS account or to AWS SSO, sign out\. To do this, see [How do I sign out of my AWS account](https://aws.amazon.com/premiumsupport/knowledge-center/sign-out-account/) on the AWS Support website or [How to Sign Out of the User Portal](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtosignout.html) in the *AWS Single Sign\-On User Guide*\.

1. To sign in to AWS SSO, follow the instructions in [How to Accept the Invitation to Join AWS SSO](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtoactivateaccount.html) in the *AWS Single Sign\-On User Guide*\. This includes going to a unique sign\-in URL and signing in with a unique user name and password\. Your AWS account administrator will either email you this information or otherwise provide it to you\.
**Note**  
Be sure to bookmark the unique sign\-in URL that you were provided, so that you can easily return to it later\. Also be sure to store the unique user name and password for this URL in a secure location\.  
This combination of URL, user name, and password might change depending on different levels of AWS Cloud9 access permissions that your AWS account administrator gives you\. For example, you might use one URL, user name, and password to get AWS Cloud9 administrator access to one account, and you might use a different URL, user name, and password that allows only AWS Cloud9 user access to a different account\.

1. After you sign in to AWS SSO, choose the **AWS Account** tile\.

1. Choose your user's display name from the drop\-down list that is displayed\. If more than one name is displayed, choose the name that you want to start using AWS Cloud9\. If you're not sure which of these names to choose, see your AWS account administrator\.

1. Choose the **Management console** link next to your user's display name\. If more than one **Management console** link is displayed, choose the link next to the correct permission set\. If you're not sure which of these links to choose, see your AWS account administrator\.

1. From the AWS Management Console, do one of the following:
   + Choose **Cloud9**, if it's already displayed\.
   + Expand **All services**, and then choose **Cloud9**\.
   + In the **Find services** box, type **Cloud9**, and then press `Enter`\.
   + In the AWS navigation bar, choose **Services**, and then choose **Cloud9**\.

The AWS Cloud9 console is displayed, and you can begin using AWS Cloud9\.

## Next Steps<a name="setup-enterprise-next-steps"></a>


****  

|  **Task**  |  **See this topic**  | 
| --- | --- | 
|  Create an AWS Cloud9 development environment, and then use the AWS Cloud9 IDE to work with code in your new environment\.  |   [Creating an Environment](create-environment.md)   | 
|  Learn how to use the AWS Cloud9 IDE\.  |   [Getting Started: Basic Tutorials](tutorials-basic.md) and [Working with the IDE](ide.md)   | 
|  Invite others to use your new environment along with you, in real time and with text chat support\.  |   [Working with Shared Environments](share-environment.md)   | 