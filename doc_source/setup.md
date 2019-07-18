# Team Setup for AWS Cloud9<a name="setup"></a>

This topic explains how to use [AWS Identity and Access Management \(IAM\)](https://aws.amazon.com/iam/) to enable multiple users within a single AWS account to use AWS Cloud9\. To set up to use AWS Cloud9 for any other usage pattern, see [Getting Started with AWS Cloud9](get-started.md) for the correct instructions\.

These instructions assume that you have \(or will have\) administrative access to a single AWS account\. For more information, see [The AWS Account Root User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html) and [Creating Your First IAM Admin User and Group](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html) in the *IAM User Guide*\. If you already have an AWS account but you do not have administrative access to it, see your AWS account administrator\.

**Note**  
You can use [AWS Single Sign\-On \(SSO\)](https://aws.amazon.com/single-sign-on/) instead of IAM to enable multiple users within a single AWS account to use AWS Cloud9\. In this usage pattern, the single AWS account serves as the master account for an organization in AWS Organizations, and that organization has no member accounts\. To use AWS SSO, skip this topic and follow the instructions in [Enterprise Setup](setup-enterprise.md) instead\. For related information, see the following resources:  
 [What Is AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) in the *AWS Organization User Guide* \(AWS SSO requires the use of AWS Organizations\)
 [What Is AWS Single Sign\-On](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) in the *AWS Single Sign\-On User Guide* 
The 4\-minute video [AWS Knowledge Center Videos: How do I get started with AWS Organizations](https://www.youtube.com/watch?v=mScBPL8VV48) on the YouTube website
The 7\-minute video [Manage User Access to Multiple AWS Accounts Using AWS Single Sign\-on](https://www.youtube.com/watch?v=bXrsUEI1V38) on the YouTube website
The 9\-minute video [How to Setup AWS Single Sign On for Your On\-Premise Active Directory Users](https://www.youtube.com/watch?v=nuPjljOVZmU) on the YouTube website

To enable multiple users in a single AWS account to start using AWS Cloud9, start with one of the following steps, depending on which AWS resources you already have\.


****  

|  **Do you have an AWS account?**  |  **Do you have at least one IAM group and user in that account?**  |  **Start with this step**  | 
| --- | --- | --- | 
|  No  |  —  |   [Step 1: Create an AWS Account](#setup-create-account)   | 
|  Yes  |  No  |   [Step 2: Create an IAM Group and User, and Add the User to the Group](#setup-create-iam-resources)   | 
|  Yes  |  Yes  |   [Step 3: Add AWS Cloud9 Access Permissions to the Group](#setup-give-user-access)   | 

## Step 1: Create an AWS Account<a name="setup-create-account"></a>

**Note**  
Your organization might already have an AWS account set up for you\. If your organization has an AWS account administrator, check with that person before starting the following procedure\. If you already have an AWS account, skip ahead to [Step 2: Create an IAM Group and User, and Add the User to the Group](#setup-create-iam-resources)\.

To watch a 4\-minute video related to the following procedure, see [Creating an Amazon Web Services Account](https://www.youtube.com/watch?v=WviHsoz8yHk) on the YouTube website\.

**To create an AWS account**

1. Go to [https://aws\.amazon\.com](https://aws.amazon.com)\.

1. Choose **Sign In to the Console**\.

1. Choose **Create a new AWS account**\.

1. Complete the process by following the on\-screen directions\. This includes giving AWS your email address and credit card information\. You must also use your phone to enter a code that AWS gives you\.

After you finish creating the account, AWS will send you a confirmation email\. Do not go to the next step until you get this confirmation\.

## Step 2: Create an IAM Group and User, and Add the User to the Group<a name="setup-create-iam-resources"></a>

In this step, you create a group and a user in AWS Identity and Access Management \(IAM\), add the user to the group, and then use the user to access AWS Cloud9\. This is an AWS security best practice\. For more information, see [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*\.

If you already have all of the IAM groups and users that you need, skip ahead to [Step 3: Add AWS Cloud9 Access Permissions to the Group](#setup-give-user-access)\.

**Note**  
Your organization might already have an IAM group and user set up for you\. If your organization has an AWS account administrator, check with that person before starting the following procedures\.

You can complete these tasks using the [AWS Management Console](#setup-create-iam-resources-group-console) or the [AWS Command Line Interface \(AWS CLI\)](#setup-create-iam-resources-group-cli)\.

To watch a 9\-minute video related to the following console procedures, see [How do I set up an IAM user and sign in to the AWS Management Console using IAM credentials](https://www.youtube.com/watch?v=XMi5fXL2Hes) on the YouTube website\.

### Step 2\.1: Create an IAM Group with the Console<a name="setup-create-iam-resources-group-console"></a>

1. Sign in to the AWS Management Console, if you are not already signed in, at [https://console\.aws\.amazon\.com](https://console.aws.amazon.com)\.
**Note**  
Although you can sign in to the AWS Management Console with the email address and password that was provided when the AWS account was created \(we call this an AWS account *root user*\), this isn't an AWS security best practice\. In the future, we recommend you sign in using credentials for an IAM administrator user in the AWS account\. An IAM administrator user has similar AWS access permissions to an AWS account root user and avoids some of the associated security risks\. If you cannot sign in as an IAM administrator user, check with your AWS account administrator\. For more information, see [Creating Your First IAM Admin User and Group](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html) in the *IAM User Guide*\.

1. Open the IAM console\. To do this, in the AWS navigation bar, choose **Services**\. Then choose **IAM**\.

1. In the IAM console's navigation pane, choose **Groups**\.

1. Choose **Create New Group**\.

1. On the **Set Group Name** page, for **Group Name**, enter a name for the new group\.

1. Choose **Next Step**\.

1. On the **Attach Policy** page, choose **Next Step** without attaching any policies\. \(You will attach a policy in [Step 3: Add AWS Cloud9 Access Permissions to the Group](#setup-give-user-access)\.\)

1. Choose **Create Group**\.
**Note**  
We recommend that you repeat this procedure to create at least two groups: one group for AWS Cloud9 users, and another group for AWS Cloud9 administrators\. This AWS security best practice can help you better control, track, and troubleshoot issues with AWS resource access\.

Skip ahead to [Step 2\.2: Create an IAM User and Add the User to the Group with the Console](#setup-create-iam-resources-user-console)\.

### Step 2\.1: Create an IAM Group with the AWS CLI<a name="setup-create-iam-resources-group-cli"></a>

**Note**  
If you're using [AWS managed temporary credentials](auth-and-access-control.md#auth-and-access-control-temporary-managed-credentials), you can't use a terminal session in the AWS Cloud9 IDE to run some or all of the commands in this section\. To address AWS security best practices, AWS managed temporary credentials don’t allow some commands to be run\. Instead, you can run those commands from a separate installation of the AWS Command Line Interface \(AWS CLI\)\.

1. Install and configure the AWS CLI on your computer, if you haven't done so already\. To do this, see the following in the *AWS Command Line Interface User Guide*:
   +  [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/installing.html) 
   +  [Quick Configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-quick-configuration) 
**Note**  
Although you can configure the AWS CLI using the credentials associated with the email address and password that was provided when the AWS account was created \(we call this an AWS account *root user*\), this isn't an AWS security best practice\. Instead, we recommend you configure the AWS CLI using credentials for an IAM administrator user in the AWS account\. An IAM administrator user has similar AWS access permissions to an AWS account root user and avoids some of the associated security risks\. If you cannot configure the AWS CLI as an IAM administrator user, check with your AWS account administrator\. For more information, see [Creating Your First IAM Admin User and Group](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html) in the *IAM User Guide*\.

1. Run the IAM `create-group` command, specifying the new group's name \(for example, `MyCloud9Group`\)\.

   ```
   aws iam create-group --group-name MyCloud9Group
   ```
**Note**  
We recommend that you repeat this procedure to create at least two groups: one group for AWS Cloud9 users, and another group for AWS Cloud9 administrators\. This AWS security best practice can help you better control, track, and troubleshoot issues with AWS resource access\.

Skip ahead to [Step 2\.2: Create an IAM User and Add the User to the Group with the AWS CLI](#setup-create-iam-resources-user-cli)\.

### Step 2\.2: Create an IAM User and Add the User to the Group with the Console<a name="setup-create-iam-resources-user-console"></a>

1. With the IAM console open from the previous procedure, in the navigation pane, choose **Users**\.

1. Choose **Add user**\.

1. For **User name**, enter a name for the new user\.
**Note**  
You can create multiple users at the same time by choosing **Add another user**\. The other settings in this procedure apply to each of these new users\.

1. Select the **Programmatic access** and **AWS Management Console access** check boxes\. This allows the new user to use various AWS developer tools and service consoles\.

1. Leave the default choice of **Autogenerated password**\. This creates a random password for the new user to sign in to the console\. Or choose **Custom password** and enter a specific password for the new user\.

1. Leave the default choice of **Require password reset**\. This prompts the new user to change their password after they sign in to the console for the first time\.

1. Choose **Next: Permissions**\.

1. Leave the default choice of **Add user to group** \(or **Add users to group** for multiple users\)\.

1. In the list of groups, select the check box \(not the name\) next to the group you want to add the user to\.

1. Choose **Next: Review**\.

1. Choose **Create user** \(or **Create users** for multiple users\)\.

1. On the last page of the wizard, do one of the following:
   + Next to each new user, choose **Send email**, and follow the on\-screen directions to email the new user their console sign\-in URL and user name\. Then communicate to each new user their console sign\-in password, AWS access key ID, and AWS secret access key separately\.
   + Choose **Download \.csv**\. Then communicate to each new user their console sign\-in URL, console sign\-in password, AWS access key ID, and AWS secret access key that is in the downloaded file\.
   + Next to each new user, choose **Show** for both **Secret access key** and **Password**\. Then communicate to each new user their console sign\-in URL, console sign\-in password, AWS access key ID, and AWS secret access key\.
**Note**  
If you do not choose **Download \.csv**, this is the only time you can view the new user's AWS secret access key and console sign\-in password\. To generate a new AWS secret access key or console sign\-in password for the new user, see the following in the *IAM User Guide*\.  
 [Creating, Modifying, and Viewing Access Keys \(Console\)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey) 
 [Creating, Changing, or Deleting an IAM User Password \(Console\)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_admin-change-user.html#id_credentials_passwords_admin-change-user_console) 

1. Repeat this procedure for each additional IAM user that you want to create, and then skip ahead to [Step 3: Add AWS Cloud9 Access Permissions to the Group](#setup-give-user-access)\.

### Step 2\.2: Create an IAM User and Add the User to the Group with the AWS CLI<a name="setup-create-iam-resources-user-cli"></a>

**Note**  
If you're using [AWS managed temporary credentials](auth-and-access-control.md#auth-and-access-control-temporary-managed-credentials), you can't use a terminal session in the AWS Cloud9 IDE to run some or all of the commands in this section\. To address AWS security best practices, AWS managed temporary credentials don’t allow some commands to be run\. Instead, you can run those commands from a separate installation of the AWS Command Line Interface \(AWS CLI\)\.

1. Run the IAM `create-user` command to create the user, specifying the new user's name \(for example, `MyCloud9User`\)\.

   ```
   aws iam create-user --user-name MyCloud9User
   ```

1. Run the IAM `create-login-profile` command to create a new console sign\-in password for the user, specifying the user's name and initial sign\-in password \(for example, `MyC10ud9Us3r!`\)\. After the user signs in, AWS asks the user to change their sign\-in password\.

   ```
   aws iam create-login-profile --user-name MyCloud9User --password MyC10ud9Us3r! --password-reset-required
   ```

   If you need to generate a replacement console signin password for the user later, see [Creating, Changing, or Deleting an IAM User Password \(API, CLI, PowerShell\)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_admin-change-user.html#Using_ManagingPasswordsCLIAPI) in the *IAM User Guide*\.

1. Run the IAM `create-access-key` command to create a new AWS access key and corresponding AWS secret access key for the user\.

   ```
   aws iam create-access-key --user-name MyCloud9User
   ```

   Make a note of the `AccessKeyId` and `SecretAccessKey` values that are displayed\. After you run the IAM `create-access-key` command, this is the only time you can view the user's AWS secret access key\. If you need to generate a new AWS secret access key for the user later, see [Creating, Modifying, and Viewing Access Keys \(API, CLI, PowerShell\)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey_CLIAPI) in the *IAM User Guide*\.

1. Run the IAM `add-user-to-group` command to add the user to the group, specifying the group's and user's names\.

   ```
   aws iam add-user-to-group --group-name MyCloud9Group --user-name MyCloud9User
   ```

1. Communicate to the user their console sign\-in URL, initial console sign\-in password, AWS access key ID, and AWS secret access key\.

1. Repeat this procedure for each additional IAM user that you want to create\.

## Step 3: Add AWS Cloud9 Access Permissions to the Group<a name="setup-give-user-access"></a>

By default, most IAM groups and users don't have access to any AWS services, including AWS Cloud9\. \(An exception is IAM administrator groups and IAM administrator users, which have access to all AWS services in their AWS account by default\.\) In this step, you use IAM to add AWS Cloud9 access permissions directly to an IAM group to which one or more users belong, so that you can ensure those users can access AWS Cloud9\.

**Note**  
Your organization might already have a group set up for you with the appropriate access permissions\. If your organization has an AWS account administrator, check with that person before starting the following procedure\.

You can complete this task using the [AWS Management Console](#setup-give-user-access-console) or the [AWS CLI](#setup-give-user-access-cli)\.

### Add AWS Cloud9 Access Permissions to the Group with the Console<a name="setup-give-user-access-console"></a>

1. Sign in to the AWS Management Console, if you are not already signed in, at [https://console\.aws\.amazon\.com/](https://console.aws.amazon.com/)\.
**Note**  
Although you can sign in to the AWS Management Console with the email address and password that was provided when the AWS account was created \(we call this an AWS account *root user*\), this isn't an AWS security best practice\. In the future, we recommend you sign in using credentials for an IAM administrator user in the AWS account\. An IAM administrator user has similar AWS access permissions to an AWS account root user and avoids some of the associated security risks\. If you cannot sign in as an IAM administrator user, check with your AWS account administrator\. For more information, see [Creating Your First IAM Admin User and Group](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html) in the *IAM User Guide*\.

1. Open the IAM console\. To do this, in the AWS navigation bar, choose **Services**\. Then choose **IAM**\.

1. Choose **Groups**\.

1. Choose the group's name\.

1. Decide whether you want to add AWS Cloud9 user or AWS Cloud9 administrator access permissions to the group\. These permissions will apply to each user in the group\.

   AWS Cloud9 user access permissions allow each user in the group to do the following things within their AWS account:
   + Create their own AWS Cloud9 development environments\.
   + Get information about their own environments\.
   + Change the settings for their own environments\.

   AWS Cloud9 administrator access permissions allow each user in the group to do additional things within their AWS account, such as:
   + Create environments for themselves or others\.
   + Get information about environments for themselves or others\.
   + Delete environments for themselves or others\.
   + Change the settings of environments for themselves or others\.
**Note**  
We recommend that you add only a limited number of users to the AWS Cloud9 administrators group\. This AWS security best practice can help you better control, track, and troubleshoot issues with AWS resource access\.

1. On the **Permissions** tab, for **Managed Policies**, choose **Attach Policy**\.

1. In the list of policy names, choose the box next to **AWSCloud9User** for AWS Cloud9 user access permissions or **AWSCloud9Administrator** for AWS Cloud9 administrator access permissions\. \(If you don't see either of these policy names in the list, enter the policy name in the **Filter** box to display it\.\)

1. Choose **Attach Policy**\.
**Note**  
If you have more than one group you want to add AWS Cloud9 access permissions to, repeat this procedure for each of those groups\.

To see the list of access permissions that these AWS managed policies give to a group, see [AWS Managed \(Predefined\) Policies](auth-and-access-control.md#auth-and-access-control-managed-policies)\.

To learn about AWS access permissions that you can add to a group in addition to access permissions that are required by AWS Cloud9, see [Managed Policies and Inline Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html) and [Understanding Permissions Granted by a Policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_understand.html) in the *IAM User Guide*\.

Skip ahead to [Step 4: Sign in to the AWS Cloud9 Console](#setup-sign-in-ide)\.

### Add AWS Cloud9 Access Permissions to the Group with the AWS CLI<a name="setup-give-user-access-cli"></a>

**Note**  
If you're using [AWS managed temporary credentials](auth-and-access-control.md#auth-and-access-control-temporary-managed-credentials), you can't use a terminal session in the AWS Cloud9 IDE to run some or all of the commands in this section\. To address AWS security best practices, AWS managed temporary credentials don’t allow some commands to be run\. Instead, you can run those commands from a separate installation of the AWS Command Line Interface \(AWS CLI\)\.

1. Install and configure the AWS CLI on your computer, if you haven't done so already\. To do this, see the following in the *AWS Command Line Interface User Guide*:
   +  [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/installing.html) 
   +  [Quick Configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-quick-configuration) 
**Note**  
Although you can configure the AWS CLI using the credentials associated with the email address and password that was provided when the AWS account was created \(we call this an AWS account *root user*\), this isn't an AWS security best practice\. Instead, we recommend you configure the AWS CLI using credentials for an IAM administrator user in the AWS account\. An IAM administrator user has similar AWS access permissions to an AWS account root user and avoids some of the associated security risks\. If you cannot configure the AWS CLI as an IAM administrator user, check with your AWS account administrator\. For more information, see [Creating Your First IAM Admin User and Group](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html) in the *IAM User Guide*\.

1. Decide whether to add AWS Cloud9 user or AWS Cloud9 administrator access permissions to the group\. These permissions will apply to each user in the group\.

   AWS Cloud9 user access permissions allow each user in the group to do the following things within their AWS account:
   + Create their own AWS Cloud9 development environments\.
   + Get information about their own environments\.
   + Change the settings for their own environments\.

   AWS Cloud9 administrator access permissions allow each user in the group to do additional things within their AWS account, such as the following:
   + Create environments for themselves or others\.
   + Get information about environments for themselves or others\.
   + Delete environments for themselves or others\.
   + Change the settings of environments for themselves or others\.
**Note**  
We recommend that you add only a limited number of users to the AWS Cloud9 administrators group\. This AWS security best practice can help you better control, track, and troubleshoot issues with AWS resource access\.

1. Run the IAM `attach-group-policy` command, specifying the group's name and the Amazon Resource Name \(ARN\) for the AWS Cloud9 access permissions policy to add\.

   For AWS Cloud9 user access permissions, specify the following ARN\.

   ```
   aws iam attach-group-policy --group-name MyCloud9Group --policy-arn arn:aws:iam::aws:policy/AWSCloud9User
   ```

   For AWS Cloud9 administrator access permissions, specify the following ARN\.

   ```
   aws iam attach-group-policy --group-name MyCloud9Group --policy-arn arn:aws:iam::aws:policy/AWSCloud9Administrator
   ```
**Note**  
If you have more than one group you want to add AWS Cloud9 access permissions to, repeat this procedure for each of those groups\.

To see the list of access permissions that these AWS managed policies give to a group, see [AWS Managed \(Predefined\) Policies](auth-and-access-control.md#auth-and-access-control-managed-policies)\.

To learn about AWS access permissions that you can add to a group in addition to access permissions that are required by AWS Cloud9, see [Managed Policies and Inline Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html) and [Understanding Permissions Granted by a Policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_understand.html) in the *IAM User Guide*\.

## Step 4: Sign In to the AWS Cloud9 Console<a name="setup-sign-in-ide"></a>

After you complete the previous steps in this topic, you and your users are ready to sign in to the AWS Cloud9 console and start using it\.

1. If you are already signed in to the AWS Management Console as an AWS account root user, sign out of the console\.

1. Open the AWS Cloud9 console, at [https://console\.aws\.amazon\.com/cloud9/](https://console.aws.amazon.com/cloud9/)\.

1. Enter the AWS account number for the IAM user you created or identified earlier, and then choose **Next**\.
**Note**  
If you don't see an option for entering the AWS account number, choose **Sign in to a different account**\. Enter the AWS account number on the next page, and then choose **Next**\.

1. Enter the user name and password of the IAM user you created or identified earlier, and then choose **Sign In**\.

1. If prompted, follow the on\-screen directions to change your user's initial sign\-in password\. Save your new sign\-in password in a secure location\.

The AWS Cloud9 console is displayed, and you can begin using AWS Cloud9\.

## Next Steps<a name="setup-next-steps"></a>


****  

|  **Task**  |  **See this topic**  | 
| --- | --- | 
|  Restrict AWS Cloud9 usage for others in your AWS account, to control costs\.  |   [Additional Setup Options](setup-teams.md)   | 
|  Create an AWS Cloud9 development environment, and then use the AWS Cloud9 IDE to work with code in your new environment\.  |   [Creating an Environment](create-environment.md)   | 
|  Learn how to use the AWS Cloud9 IDE\.  |   [IDE Tutorial](tutorial.md)   | 
|  Invite others to use your new environment along with you, in real time and with text chat support\.  |   [Working with Shared Environments](share-environment.md)   | 