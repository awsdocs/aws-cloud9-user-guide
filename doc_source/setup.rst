.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _setup:

########################
Team Setup for |AC9long|
########################

.. meta::
    :description:
        Describes how to set up a team to start using AWS Cloud9.

To start using |AC9|, follow one of these sets of procedures, depending on how you plan to use |AC9|.

.. list-table::
   :widths: 2 1
   :header-rows: 1

   * - **Usage pattern**
     - **Follow these procedures**
   * - I want to start using |AC9| quickly. 

       |mdash| Or |mdash| 
   
       I will be the only one using |AC9| in my AWS account.
     - :ref:`Express Setup <setup-express>`
   * - I want multiple users in my AWS account to use |AC9|.
     - **This topic**
   * - I want multiple users in my AWS account to use |AC9|, and I want to restrict their usage to control costs.
     - :ref:`Advanced Setup for Teams <setup-teams>`

To enable multiple users in your AWS account to start using |AC9|, start with one of the following steps, depending on which AWS resources you already have.

.. list-table::
   :widths: 3 1 3
   :header-rows: 1

   * - **Do you have an AWS account?**
     - **Do you have an IAM group and user in that account?**
     - **Start with this step**
   * - No
     - |mdash|
     - :ref:`setup-create-account`
   * - Yes
     - No
     - :ref:`setup-create-iam-resources`
   * - Yes
     - Yes
     - :ref:`setup-give-user-access`

.. _setup-create-account:

Step 1: Create an AWS Account
=============================

.. note:: Your organization might already have an AWS account set up for you. If your organization has an AWS account
   administrator, check with that person before starting the following procedure. If you already have
   an AWS account, skip ahead to :ref:`setup-create-iam-resources`.

To watch a 4-minute video related to the following procedure, see `Creating an Amazon Web Services Account <https://www.youtube.com/watch?v=WviHsoz8yHk>`_ on the YouTube website.

.. topic:: To create an AWS account

   #. Go to https://aws.amazon.com.
   #. Choose :guilabel:`Sign In to the Console`.
   #. Choose :guilabel:`Create a new AWS account`.
   #. Complete the process by following the on-screen directions. This includes giving AWS your email address and
      credit card information. You must also use your phone to enter a code that AWS gives you.

After you finish creating the account, AWS will send you a confirmation email. Do not go to the next 
step until you get this confirmation.

.. _setup-create-iam-resources:

Step 2: Create an |IAM| Group and User, and Add the User to the Group
=====================================================================

In this step, you will create a group and a user in |IAMlong| (|IAM|), add the user to the group, and then use the user to access
|AC9|. This is an AWS security best practice. For more information, see :IAM-ug:`IAM Best Practices <best-practices>` in the |IAM-ug|.

If you already have an |IAM| group and user, skip ahead to :ref:`setup-give-user-access`.

.. note:: Your organization might already have an |IAM| group and user set up for you. If your organization has an AWS account
   administrator, check with that person before starting the following procedures.

You can complete these tasks using the :ref:`AWS Management Console <setup-create-iam-resources-group-console>` or the :ref:`AWS Command Line Interface (AWS CLI) <setup-create-iam-resources-group-cli>`.

To watch a 9-minute video related to the following console procedures, see `How do I set up an IAM user and sign in to the AWS Management Console using IAM credentials <https://www.youtube.com/watch?v=XMi5fXL2Hes>`_ on the YouTube website.

.. _setup-create-iam-resources-group-console:

Step 2.1: Create an |IAM| Group with the Console
------------------------------------------------

#. Sign in to the AWS Management Console, if you are not already signed in, at https://console.aws.amazon.com.

   .. note:: Although it's possible to sign in to the AWS Management Console using the credentials for an AWS account root user, this isn't an AWS security
      best practice. Instead, we recommend you sign in using credentials for an |IAM| administrator user in your AWS account. An |IAM| administrator user has similar AWS access permissions to
      an AWS account root user and avoids some of the associated security risks. If you cannot
      sign in as an |IAM| administrator user, check with your AWS account administrator. For more information, see the following in the |IAM-ug|.

      * :IAM-ug:`Creating Your First IAM Admin User and Group <getting-started_create-admin-group>`
      * :iam-user-guide:`The IAM User Sign-in Page <console.html#user-sign-in-page>`

#. Open the |IAM| console. To do this, in the AWS navigation bar, choose :guilabel:`Services`. Then choose :guilabel:`IAM`.
#. In the |IAM| console's navigation pane, choose :guilabel:`Groups`.
#. Choose :guilabel:`Create New Group`.
#. On the :guilabel:`Set Group Name` page, for :guilabel:`Group Name`, type a name for the new group.
#. Choose :guilabel:`Next Step`.
#. On the :guilabel:`Attach Policy` page, choose :guilabel:`Next Step` without attaching any policies. (You will attach a policy in :ref:`setup-give-user-access`.)
#. Choose :guilabel:`Create Group`.

   .. note:: We recommend that you repeat this procedure to create 2 groups: one group for |AC9| users, and another group for |AC9| administrators.
      This AWS security best practice can help you better control, track, 
      and troubleshoot issues with AWS resource access.

Skip ahead to :ref:`setup-create-iam-resources-user-console`.

.. _setup-create-iam-resources-group-cli:

Step 2.1: Create an |IAM| Group with the |CLI|
----------------------------------------------

#. Install and configure the |CLI| on your computer, if you have not done so already. To do this, see the following in the |cli-ug|.

   * :cli-ug:`Installing the AWS Command Line Interface <installing>`
   * :cli-user-guide:`Quick Configuration <cli-chap-getting-started.html#cli-quick-configuration>`
   
   .. note:: Although it's possible to configure the |cli| using the credentials for an AWS account root user, this isn't an AWS security
      best practice. Instead, we recommend you configure the |cli| using credentials for an |IAM| administrator user in your AWS account. An |IAM| administrator user has similar AWS access permissions to
      an AWS account root user and avoids some of the associated security risks. If you cannot
      configure the |cli| as an |IAM| administrator user, check with your AWS account administrator. For more information, see 
      :IAM-ug:`Creating Your First IAM Admin User and Group <getting-started_create-admin-group>` in the |IAM-ug|.

#. Run the IAM :code:`create-group` command, specifying the new group's name (for example, :code:`MyCloud9Group`).

   .. code-block:: sh

      aws iam create-group --group-name MyCloud9Group

   .. note::  We recommend that you repeat this procedure to create 2 groups: one group for |AC9| users, and another group for |AC9| administrators.
      This AWS security best practice can help you better control, track, 
      and troubleshoot issues with AWS resource access.

Skip ahead to :ref:`setup-create-iam-resources-user-cli`.

.. _setup-create-iam-resources-user-console:

Step 2.2: Create an |IAM| User and Add the User to the Group with the Console
-----------------------------------------------------------------------------

#. With the |IAM| console open from the previous procedure, in the navigation pane, choose :guilabel:`Users`.
#. Choose :guilabel:`Add user`.
#. For :guilabel:`User name`, type a name for the new user.

   .. note:: You can create multiple users at the same time by choosing :guilabel:`Add another user`. The other settings in this procedure apply to each of these new users.

#. Select the :guilabel:`Programmatic access` and :guilabel:`AWS Management Console access` check boxes. This allows the new user to use various AWS developer tools and service consoles.
#. Leave the default choice of :guilabel:`Autogenerated password`, which creates a random password for the new user to sign in to the console. Or choose :guilabel:`Custom password`
   and type a specific password for the new user.
#. Leave the default choice of :guilabel:`Require password reset`, which prompts the new user to change their password after they sign in to the console for the first time.
#. Choose :guilabel:`Next: Permissions`.
#. Leave the default choice of :guilabel:`Add user to group` (or :guilabel:`Add users to group` for multiple users).
#. In the list of groups, select the check box (not the name) next to the group you want to add the user to.
#. Choose :guilabel:`Next: Review`.
#. Choose :guilabel:`Create user` (or :guilabel:`Create users` for multiple users).
#. On the last page of the wizard, do one of the following.

   * Next to each new user, choose :guilabel:`Send email`, and follow the on-screen directions to email the new user their console sign in URL and user name. Then communicate to
     each new user their console sign in password, AWS access key ID, and AWS secret access key separately.
   * Choose :guilabel:`Download .csv`. Then communicate to each new user their console sign in URL, console sign in password, AWS access key ID, and AWS secret access key that is in the downloaded file.
   * Next to each new user, choose :guilabel:`Show` for both :guilabel:`Secret access key` and :guilabel:`Password`. Then communicate to each new user their console sign in URL, console sign in
     password, AWS access key ID, and AWS secret access key.

   .. note:: If you do not choose :guilabel:`Download .csv`, this is the only time you can view the new user's AWS secret access key and console sign in
      password. To generate a new AWS secret access key or console sign in password for the new user, see the following in the |IAM-ug|.

      * :iam-user-guide:`Creating, Modifying, and Viewing Access Keys (Console) <id_credentials_access-keys.html#Using_CreateAccessKey>`
      * :iam-user-guide:`Creating, Changing, or Deleting an IAM User Password (Console) <id_credentials_passwords_admin-change-user.html#id_credentials_passwords_admin-change-user_console>`

Skip ahead to :ref:`setup-give-user-access`.

.. _setup-create-iam-resources-user-cli:

Step 2.2: Create an |IAM| User and Add the User to the Group with the |CLI|
---------------------------------------------------------------------------

#. Run the IAM :code:`create-user` command to create the user, specifying the new user's name (for example, :code:`MyCloud9User`).

   .. code-block:: sh

      aws iam create-user --user-name MyCloud9User

#. Run the IAM :code:`create-login-profile` command to create a new console sign in password for the user, specifying the user's name and 
   initial sign in password (for example, :code:`MyC10ud9Us3r!`). After the user signs in, AWS asks the user to change their sign in password.

   .. code-block:: sh
   
      aws iam create-login-profile --user-name MyCloud9User --password MyC10ud9Us3r! --password-reset-required

   To generate a replacement console sign in password for the user later if needed, see 
   :iam-user-guide:`Creating, Changing, or Deleting an IAM User Password (API, CLI, PowerShell) <id_credentials_passwords_admin-change-user.html#Using_ManagingPasswordsCLIAPI>` 
   in the |IAM-ug|.

#. Run the IAM :code:`create-access-key` command to create a new AWS access key and corresponding AWS secret access key for the user.

   .. code-block:: sh
   
      aws iam create-access-key --user-name MyCloud9User

   Make a note of the :code:`AccessKeyId` and :code:`SecretAccessKey` values that are displayed. 
   After you run the IAM :code:`create-access-key` command, this is the only time you can view the user's AWS secret access key. 
   To generate a new AWS secret access key for the user later if needed, see 
   :iam-user-guide:`Creating, Modifying, and Viewing Access Keys (API, CLI, PowerShell) <id_credentials_access-keys.html#Using_CreateAccessKey_CLIAPI>` 
   in the |IAM-ug|.

#. Run the IAM :code:`add-user-to-group` command to add the user to the group, specifying the group's and user's names.

   .. code-block:: sh

      aws iam add-user-to-group --group-name MyCloud9Group --user-name MyCloud9User

#. Communicate to the user their console sign in URL, initial console sign in password, AWS access key ID, and AWS secret access key.

.. _setup-give-user-access:

Step 3: Add |AC9| Access Permissions to the Group
=================================================

By default, most |IAM| groups and users do not have access to |AC9|. (An exception is |IAM| administrator groups and |IAM| administrator users, which have access to all AWS services in their AWS account by default.)
In this step, you use |IAM| to add |AC9| access permissions directly to an |IAM| group to which one or more users belong, so that you can ensure
those users can access |AC9|.

If you already have an |IAM| user you want to use, and that user belongs to an |IAM| administrator group,
skip ahead to :ref:`setup-sign-in-ide`.

.. note:: Your organization might already have a group set up for you with the appropriate access permissions.
   If your organization has an AWS account administrator, check with that person before starting the following procedure.

You can complete this task using the :ref:`AWS Management Console <setup-give-user-access-console>` or the :ref:`AWS CLI <setup-give-user-access-cli>`.

.. _setup-give-user-access-console:

Add |AC9| Access Permissions to the Group with the Console
----------------------------------------------------------

#. Sign in to the AWS Management Console, if you are not already signed in, at https://console.aws.amazon.com/.

   .. note:: Although it's possible to sign in to the AWS Management Console using the credentials for an AWS account root user, this isn't an AWS security
      best practice. Instead, we recommend you sign in using credentials for an |IAM| administrator user in your AWS account. If you cannot
      do this, check with your AWS account administrator.

#. Open the |IAM| console. To do this, in the AWS navigation bar, choose :guilabel:`Services`. Then choose :guilabel:`IAM`.
#. Choose :guilabel:`Groups`.
#. Choose the group's name.
#. Decide whether you want to add |AC9| user or |AC9| administrator access permissions to the group. These permissions will apply to each user in the group.

   |AC9| user access permissions allow each user in the group to do the following things within their AWS account:

   * Create their own |envfirstplural|.
   * Get information about their own |envplural|.
   * Change the settings for their own |envplural|.

   |AC9| administrator access permissions allow each user in the group to do additional things within their AWS account, such as:

      * Create |envplural| for themselves or others.
      * Get information about |envplural| for themselves or others.
      * Delete |envplural| for themselves or others.
      * Change the settings of |envplural| for themselves or others.

   .. note:: We recommend that you add only a limited number of users to the |AC9| administrators group.
      This AWS security best practice can help you better control, track,
      and troubleshoot issues with AWS resource access.

#. On the :guilabel:`Permissions` tab, for :guilabel:`Managed Policies`, choose :guilabel:`Attach Policy`.
#. In the list of policy names, choose the box next to :guilabel:`AWSCloud9User` for |AC9| user access permissions
   or :guilabel:`AWSCloud9Administrator` for |AC9| administrator access permissions.
   (If you don't see either of these policy names in the list, type the policy name
   in the :guilabel:`Filter` box to display it.)
#. Choose :guilabel:`Attach Policy`.

   .. note:: If you have more than one group you want to add |AC9| access permissions to, repeat this procedure for each of those groups.

To see the list of access permissions that these AWS managed policies give to a group, see :ref:`AWS Managed (Predefined) Policies <auth-and-access-control-managed-policies>`.

Skip ahead to :ref:`setup-sign-in-ide`.

.. _setup-give-user-access-cli:

Add |AC9| Access Permissions to the Group with the |CLI|
--------------------------------------------------------

#. Install and configure the |CLI| on your computer, if you have not done so already. To do this, see the following in the |cli-ug|.

   * :cli-ug:`Installing the AWS Command Line Interface <installing>`
   * :cli-user-guide:`Quick Configuration <cli-chap-getting-started.html#cli-quick-configuration>`
   
   .. note:: Although it's possible to configure the |cli| using the credentials for an AWS account root user, this isn't an AWS security
      best practice. Instead, we recommend you configure the |cli| using credentials for an |IAM| administrator user in your AWS account. An |IAM| administrator user has similar AWS access permissions to
      an AWS account root user and avoids some of the associated security risks. If you cannot
      configure the |cli| as an |IAM| administrator user, check with your AWS account administrator. For more information, see 
      :IAM-ug:`Creating Your First IAM Admin User and Group <getting-started_create-admin-group>` in the |IAM-ug|.

#. Decide whether you want to add |AC9| user or |AC9| administrator access permissions to the group. These permissions will apply to each user in the group.

   |AC9| user access permissions allow each user in the group to do the following things within their AWS account.

   * Create their own |envfirstplural|.
   * Get information about their own |envplural|.
   * Change the settings for their own |envplural|.

   |AC9| administrator access permissions allow each user in the group to do additional things within their AWS account, such as the following.

      * Create |envplural| for themselves or others.
      * Get information about |envplural| for themselves or others.
      * Delete |envplural| for themselves or others.
      * Change the settings of |envplural| for themselves or others.

   .. note:: We recommend that you add only a limited number of users to the |AC9| administrators group.
      This AWS security best practice can help you better control, track,
      and troubleshoot issues with AWS resource access.

#. Run the IAM :code:`attach-group-policy` command, specifying the group's name and the Amazon Resource Name (ARN) for the |AC9| access permissions policy 
   to add.

   For |AC9| user access permissions, specify the following ARN.

   .. code-block:: sh

      aws iam attach-group-policy --group-name MyCloud9Group --policy-arn arn:aws:iam::aws:policy/AWSCloud9User

   For |AC9| administrator access permissions, specify the following ARN.
   
   .. code-block:: sh

      aws iam attach-group-policy --group-name MyCloud9Group --policy-arn arn:aws:iam::aws:policy/AWSCloud9Administrator

   .. note:: If you have more than one group you want to add |AC9| access permissions to, repeat this procedure for each of those groups.

To see the list of access permissions that these AWS managed policies give to a group, see :ref:`AWS Managed (Predefined) Policies <auth-and-access-control-managed-policies>`.

.. _setup-sign-in-ide:

Step 4: Sign in to the |AC9| Console
====================================

After you complete the previous steps in this topic, you and your users are ready to sign in to the |AC9| console and start using it.

#. If you are already signed in to the |console| as an AWS account root user, sign out of the console.
#. Open the |AC9| console, at |AC9Console_link|.
#. If prompted, type the AWS account number for the |IAM| user you created or identified earlier, and then choose :guilabel:`Next`.

   .. note:: If you do not see an option for typing the AWS account number, choose :guilabel:`Sign in to a different account`. Type the AWS account number on the next page, and then choose :guilabel:`Next`.

#. If prompted, type the user name and password of the |IAM| user you created or identified earlier, and then choose :guilabel:`Sign In`.
#. If prompted, follow the on-screen directions to change your user's initial sign-in password. Save your new sign-in password in a secure location.

You have now successfully signed in, and the |AC9| console is displayed.

.. _setup-next-steps:

Next Steps
==========

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - **Task**
     - **See this topic**
   * - Restrict |AC9| usage for others in your AWS account, to control costs.
     - :ref:`Advanced Team Setup <setup-teams>`
   * - Create an |envfirst|, and then use the |AC9IDE| to work with code in your new |env|.
     - :ref:`Creating an Environment <create-environment>`
   * - Learn how to use the |AC9IDE|.
     - :ref:`IDE Tutorial <tutorial>`
   * - Invite others to use your new |env| along with you, in real time and with text chat support.
     - :ref:`Working with Shared Environments <share-environment>`
