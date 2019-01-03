.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _share-environment:

#############################################
Working with Shared Environments in |AC9long|
#############################################

.. meta::
    :description:
        Describes how to share an environment and work with shared environments in AWS Cloud9.

A :dfn:`shared environment` is an |envfirst| that multiple users have been invited to participate in. This topic provides instructions for sharing an |env| in |AC9| and how to participate in a shared |env|.

To invite a user to participate in an |env| you own, follow one of these sets of procedures, depending on the type of user you want to invite.

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - **User type**
     - **Follow these procedures**     
   * - A user in the same AWS account as the |env|.
     - :ref:`share-environment-invite-user`
   * - An |AC9| administrator in the same AWS account as the |env|, specifically:
   
       * The AWS account root user.
       * An |IAM| administrator user.
       * A user with the AWS managed policy :code:`AWSCloud9Administrator` attached.

     - To invite the |AC9| administrator yourself, see :ref:`share-environment-invite-user`.

       To have the |AC9| administrator invite themself (or others in the same AWS account), see :ref:`share-environment-admin-user`.

   * - A user in a different AWS account than the |env|.
     - :ref:`share-environment-invite-user-cross-account`

.. _share-environment-contents:

Contents
========

* :ref:`share-environment-about`
* :ref:`share-environment-member-roles`
* :ref:`share-environment-invite-user`
* :ref:`share-environment-admin-user`
* :ref:`share-environment-invite-user-cross-account`
* :ref:`share-environment-open`
* :ref:`share-environment-members-list`
* :ref:`share-environment-active-file`
* :ref:`share-environment-open-file`
* :ref:`share-environment-active-cursor`
* :ref:`share-environment-chat`
* :ref:`share-environment-chat-view`
* :ref:`share-environment-chat-delete`
* :ref:`share-environment-chat-delete-all`
* :ref:`share-environment-change-access`
* :ref:`share-environment-delete-you`
* :ref:`share-environment-delete-member`
* :ref:`share-environment-best-practices`

.. _share-environment-about:

Shared |envtitle| Usage Scenarios
=================================

A shared |env| is good for the following.

* Pair programming (also know as :dfn:`peer programming`). This is where two users work together on the same code in a single |env|. In pair programming, typically one user writes code while
  the other user observes the code being written. The observer gives immediate input and feedback to the code writer. These positions frequently switch during a project. Without a shared
  |env|, teams of pair programmers typically sit in front of a single machine, and only one user at a
  time can write code. With a shared |env|, both users can sit in front of
  their own machine and can write code at the same time, even if they are in different physical offices.
* Computer science classes. This is useful when teachers or teaching assistants want to access a student's |env| to review their homework or fix issues with their |env| in real time.
  Students can also work together with their classmates on shared homework projects, writing code together in a single |env| in real time. They can do this even though they might be in different locations using
  different computer operating systems and web browser types.
* Any other situation where multiple users need to collaborate on the same code in real time.

.. _share-environment-member-roles:

About |memlongtitle| Access Roles
=================================

Before you share an |env| or participate in a shared |env| in |AC9|, you should understand the access permission levels for a shared |env|. We call these
permission levels :dfn:`environment member access roles`.

A shared |env| in |AC9| offers three |memlong| access roles: :dfn:`owner`, :dfn:`read/write`, and :dfn:`read-only`.

* An |memown| has full control over an |env|. Each |env| has one and only one |memown|, who is the |env| creator.
  An |memown| can do the following.

  * Add, change, and remove |mems| for the |env|
  * Open, view, and edit files
  * Run code
  * Change |env| settings
  * Chat with other |mems|
  * Delete existing chat messages

  In the |AC9IDE|, an |env| owner is displayed with :guilabel:`Read+Write` access.
* A |memrw| member can do the following.

  * Open, view, and edit files
  * Run code
  * Change various |env| settings from within the |AC9IDE|
  * Chat with other |mems|
  * Delete existing chat messages

  In the |AC9IDE|, |memrw| members are displayed with :guilabel:`Read+Write` access.
* A |memro| member can do the following.

  * Open and view files
  * Chat with other |mems|
  * Delete existing chat messages

  In the |AC9IDE|, |memro| members are displayed with :guilabel:`Read Only` access.

Before a user can become an |env| owner or |mem|, that user must meet one of the following criteria.

* The user is an **AWS account root user**.
* The user is an **IAM administrator user**. 
  For more information, see :IAM-ug:`Creating Your First IAM Admin User and Group <getting-started_create-admin-group>` in the |IAM-ug|.
* The user is a **user who belongs to an IAM group**, a **user who assumes a role**, or a **federated user who assumes a role**, 
  *and* that group or role has the AWS managed policy :code:`AWSCloud9Administrator` or :code:`AWSCloud9User` (or :code:`AWSCloud9EnvironmentMember`, to be a |mem| only) attached. 
  For more information, see :ref:`AWS Managed (Predefined) Policies <auth-and-access-control-managed-policies>`. 
  
  * To attach one of the preceding managed policies to an |IAM| group, 
    you can use the :ref:`AWS Management Console <share-environment-member-roles-console>` or the :ref:`AWS Command Line Interface (AWS CLI) <share-environment-member-roles-cli>` 
    as described in the following procedures.
  * To create a role in |IAM| with one of the preceding managed policies for a user or a federated user to assume, see :IAM-ug:`Creating Roles <id_roles_create>` in the |IAM-ug|. 
    To have a user or a federated user assume the role, see coverage of assuming roles in :IAM-ug:`Using IAM Roles <id_roles_use>` in the |IAM-ug|. 

.. _share-environment-member-roles-console:

Attach an AWS Managed Policy for |AC9| to a Group Using the Console
-------------------------------------------------------------------

#. Sign in to the AWS Management Console, if you are not already signed in.

   For this step, we recommend you sign in using credentials for an |IAM| administrator user in your AWS account. If you cannot
   do this, check with your AWS account administrator.

#. Open the |IAM| console. To do this, in the console's navigation bar, choose :guilabel:`Services`. Then choose :guilabel:`IAM`.
#. Choose :guilabel:`Groups`.
#. Choose the group's name.
#. On the :guilabel:`Permissions` tab, for :guilabel:`Managed Policies`, choose :guilabel:`Attach Policy`.
#. In the list of policy names, choose one of the following boxes.

   * :guilabel:`AWSCloud9User` (preferred) or :guilabel:`AWSCloud9Administrator` to enable each user in the group to be an |env| owner 
   * :guilabel:`AWSCloud9EnvironmentMember` to enable each user in the group to be a member only

   (If you don't see one of these policy names in the list, type the policy name in
   the :guilabel:`Search` box to display it.)

#. Choose :guilabel:`Attach policy`.

.. _share-environment-member-roles-cli:

Attach an AWS Managed Policy for |AC9| to a Group Using the |cli|
-----------------------------------------------------------------

Run the IAM :code:`attach-group-policy` command to attach the AWS managed policy for |AC9| to the group, specifying the group's name and the Amazon Resource Name (ARN) of the policy, for example:

.. code-block:: sh

   aws iam attach-group-policy --group-name MyGroup --policy-arn arn:aws:iam::aws:policy/POLICY_NAME

In the preceding command, replace :code:`MyGroup` with the name of the group. Replace :code:`POLICY_NAME` with the name of one of the following AWS managed policies.

* :code:`AWSCloud9User` (preferred) or :code:`AWSCloud9Administrator` to enable each user in the group to be an |env| owner
* :code:`AWSCloud9EnvironmentMember` to enable each user in the group to be a member only

.. _share-environment-invite-user:

Invite a User in the Same Account as the |envtitle|
===================================================

Use the instructions in this section to share an |envfirstlong| that you own in your AWS account with a user in that same account. 

#. If the user you want to invite is **not** one of the following types of users, be sure the user you want to invite 
   already has the corresponding environment member access role. For 
   instructions, see :ref:`share-environment-member-roles`.

   * The **AWS account root user**.
   * An **IAM administrator user**.
   * A **user who belongs to an IAM group**, a **user who assumes a role**, or a **federated user who assumes a role**, *and* that 
     group or role has the AWS managed policy :code:`AWSCloud9Administrator` attached. 

#. Open the |env| that you own and want to invite the user to, if the |env| is not already open.
#. In the menu bar in the |AC9IDE|, do one of the following.

   * Choose :guilabel:`Window, Share`.
   * Choose :guilabel:`Share` (located next to the :guilabel:`Preferences` gear icon).

     .. image:: images/ide-share.png
        :alt: The Share command in the AWS Cloud9 IDE menu bar

#. In the :guilabel:`Share this environment` dialog box, for :guilabel:`Invite Members`, type one of the following.

   * To invite an **IAM user**, type the user's name.
   * To invite the **AWS account root user**, type :code:`arn:aws:iam::123456789012:root`, replacing :code:`123456789012` with your AWS account ID.
   * To invite a **user with an assumed role** or a **federated user with an assumed role**, 
     type :code:`arn:aws:sts::123456789012:assumed-role/MyAssumedRole/MyAssumedRoleSession`, replacing :code:`123456789012` with your AWS account ID, 
     :code:`MyAssumedRole` with the name of the assumed role, and :code:`MyAssumedRoleSession` with the session name for the assumed role.

#. To make this user a |memro| member, choose :guilabel:`R`. To make this user |memrw|, choose :guilabel:`RW`.
#. Choose :guilabel:`Invite`.

   .. note:: If you make this user a |memrw| member, a dialog box is displayed, containing information
      about possibly putting your
      AWS security credentials at risk. The following information provides more background about this issue.

      You should share an |env| only with those you trust.

      A |memrw| member may be able to use the |cli|, the aws-shell, or AWS SDK code in your
      |env| to take actions in AWS on your behalf. Furthermore, if you store your permanent AWS access credentials within the |env|,
      that |mem| could potentially copy those credentials and use them
      outside of the |env|.

      Removing your permanent AWS access credentials from your |env| and using temporary AWS access credentials
      instead does not fully address this issue. It lessens
      the opportunity of the |mem| to copy those temporary credentials and use them outside of the |env| (as those temporary credentials will work only for a limited time).
      However, temporary credentials still enable a |memrw| member to take actions in AWS from the |env| on your behalf.

#. Contact the user to let them know they can open this |env| and begin using it.

.. _share-environment-admin-user:

Have an |AC9| Administrator in the Same Account as the |envtitle| Invite Themself or Others
===========================================================================================

The following types of users can invite themselves (or other users in the same AWS account) to any |env| in the same account.

* The **AWS account root user**.
* An **IAM administrator user**.
* A **user who belongs to an IAM group**, a **user who assumes a role**, or a **federated user who assumes a role**, *and* that 
  group or role has the AWS managed policy :code:`AWSCloud9Administrator` attached. 

If the invited user is **not** one of the preceding types of users, be sure that user already has the corresponding environment member access role. For 
instructions, see :ref:`share-environment-member-roles`.

To invite the user, use the |cli| or the aws-shell to run the 
AWS Cloud9 :code:`create-environment-membership` command, as follows.
   
.. code-block:: sh
     
   aws cloud9 create-environment-membership --environment-id 12a34567b8cd9012345ef67abcd890e1 --user-arn USER_ARN --permissions PERMISSION_LEVEL

In the preceding command, replace :code:`12a34567b8cd9012345ef67abcd890e1` with the ID of the |env|, and :code:`PERMISSION_LEVEL` with :code:`read-write` or :code:`read-only`. 
Replace :code:`USER_ARN` with one of the following:

* To invite an **IAM user**, type :code:`arn:aws:iam::123456789012:user/MyUser`, replacing :code:`123456789012` with your AWS account ID and 
  :code:`MyUser` with the user's name.
* To invite the **AWS account root user**, type :code:`arn:aws:iam::123456789012:root`, replacing :code:`123456789012` with your AWS account ID.
* To invite a **user with an assumed role** or a **federated user with an assumed role**, 
  type :code:`arn:aws:sts::123456789012:assumed-role/MyAssumedRole/MyAssumedRoleSession`, replacing :code:`123456789012` with your AWS account ID, 
  :code:`MyAssumedRole` with the name of the assumed role, and :code:`MyAssumedRoleSession` with the session name for the assumed role.

For example, to invite the AWS account root user for account ID :code:`123456789012` to an |env| with ID :code:`12a34567b8cd9012345ef67abcd890e1` as a |memrw| member, run the following command.

.. code-block:: sh
     
   aws cloud9 create-environment-membership --environment-id 12a34567b8cd9012345ef67abcd890e1 --user-arn arn:aws:iam::123456789012:root --permissions read-write

.. note:: If you're using the aws-shell, omit the :code:`aws` prefix from the preceding commands.

.. _share-environment-invite-user-cross-account:

Invite a User in a Different Account Than the |envtitle|
========================================================

Use the instructions in this section to share an |envfirstlong| that you own in your AWS account with a user in a different account. 

Prerequisites
-------------

Before you complete the steps in the section, be sure you have the following.

* Two AWS accounts. One account contains the |env| you want to share. To reduce confusion, we refer to this account as "your account" and as "account :code:`111111111111`" in this section's examples. 
  A separate account contains the user you want to share the |env| with. To reduce confusion, we refer to this account as "the other account" and as "account :code:`999999999999`" in this section's examples.
* An |IAM| group in the other account :code:`999999999999`, which we refer to as :code:`AWSCloud9CrossAccountGroup` in this section's examples. 
  (To use a different group in that account, substitute its name throughout this section's examples).
* A user in the other account :code:`999999999999`, which we refer to as :code:`AWSCloud9CrossAccountUser` in this section's examples. This user is a member of the 
  :code:`AWSCloud9CrossAccountGroup` group in the other account. (To use a different user in that account, substitute its name throughout this section's examples).
* An |env| in your account :code:`111111111111` that you want to allow the user in the other account :code:`999999999999` to access. 

Step 1: Create an |IAM| Role in Your Account to Allow Access from the Other Account
-----------------------------------------------------------------------------------

In this step, you create an |IAM| role in your account :code:`111111111111`. This role allows users in the other account :code:`999999999999` to access your account using the permissions you specify.

#. Sign in to the AWS Management Console using your AWS account :code:`111111111111`.

   We recommend you sign in using credentials for an |IAM| administrator user in your AWS account. If you can't
   do this, check with your AWS account administrator.

#. Open the |IAM| console. To do this, on the global navigation bar, choose :guilabel:`Services`, and then choose :guilabel:`IAM`.
#. In the service navigation pane, choose :guilabel:`Roles`.
#. On the :guilabel:`Roles` page, choose :guilabel:`Create role`.
#. On the :guilabel:`Select type of trusted entity` page, choose the :guilabel:`Another AWS account` tile.
#. In :guilabel:`Specify accounts that can use this role`, for :guilabel:`Account ID`, type the ID of the other AWS account: :code:`999999999999`. (Leave the :guilabel:`Options` boxes cleared.)
#. Choose :guilabel:`Next: Permissions`.
#. On the :guilabel:`Attach permissions policies` page, select the box next to the policy (or policies) that contain the permissions you want the other AWS account to have in your account. 
   For this example, choose :guilabel:`AWSCloud9EnvironmentMember`. (If you can't find it, type :code:`AWSCloud9EnvironmentMember` in the :guilabel:`Search` box to display it.) This particular 
   policy allows users in the other account to become |memro| or |memrw| members in shared |envplural| in your account after you invite them. 
#. Choose :guilabel:`Review`.
#. On the :guilabel:`Review` page, for :guilabel:`Role name`, type a name for the role. For this example, type :guilabel:`AWSCloud9EnvironmentMemberCrossAccountRole`. 
   (To use a different name for the role, substitute it throughout this section's examples).
#. Choose :guilabel:`Create role`.
#. In the list of roles that is displayed, choose :guilabel:`AWSCloud9EnvironmentMemberCrossAccountRole`. 
#. On the :guilabel:`Summary` page, copy the value of :guilabel:`Role ARN`, for example, :guilabel:`arn:aws:iam::111111111111:role/AWSCloud9EnvironmentMemberCrossAccountRole`. 
   You need this value for Step 3 in this section.

Step 2: Add the User in the Other Account as a |memtitle| of Your |envtitle|
----------------------------------------------------------------------------

Now that you have an |IAM| role in your account :code:`111111111111`, and know the name of the user in other account :code:`999999999999`, you can add the user as a |mem| of the |env|.

#. If you're not already signed in to the AWS Management Console as the owner of the |env| in your account :code:`111111111111`, sign in now.
#. Open the |IDE| for the |env|. (If you're not sure how to do this, see :ref:`Opening an Environment <open-environment>`.)
#. On the menu bar, choose :guilabel:`Share`.
#. In the :guilabel:`Share this environment` dialog box, for :guilabel:`Invite Members`, type 
   :code:`arn:aws:sts::111111111111:assumed-role/AWSCloud9EnvironmentMemberCrossAccountRole/AWSCloud9CrossAccountUser`, where:

   * :code:`111111111111` is the actual ID of your AWS account. 
   * :code:`AWSCloud9EnvironmentMemberCrossAccountRole` is the name of the |IAM| role in your account :code:`111111111111`, as specified earlier in Step 1 of this section. 
   * :code:`AWSCloud9CrossAccountUser` is the name of the user in the other account :code:`999999999999`.

#. Choose :guilabel:`Invite`, and follow the onscreen instructions to complete the invitation process.

Step 3: Grant Access in the Other Account to Use the |IAM| Role in Your Account
-------------------------------------------------------------------------------

In this step, you allow the user in the other account :code:`999999999999` to use the |IAM| role you created in your account :code:`111111111111`.

#. If you're still signed in to the AWS Management Console using your AWS account :code:`111111111111`, sign out now.
#. Sign in to the AWS Management Console using the other AWS account :code:`999999999999`.

   We recommend you sign in using credentials for an |IAM| administrator user in the other account. If you can't
   do this, check with your AWS account administrator.

#. Open the |IAM| console. To do this, on the global navigation bar, choose :guilabel:`Services`, and then choose :guilabel:`IAM`.
#. In the service navigation pane, choose :guilabel:`Groups`.
#. In the list of groups that is displayed, choose :guilabel:`AWSCloud9CrossAccountGroup`.
#. On the :guilabel:`Permissions` tab, expand :guilabel:`Inline Policies`, and then choose the link at the end of "To create one, click here."
#. On the :guilabel:`Set Permissions` page, choose :guilabel:`Custom Policy`, and then choose :guilabel:`Select`.
#. On the :guilabel:`Review Policy` page, for :guilabel:`Policy Name`, type a name for the policy. For this example, we suggest typing :guilabel:`AWSCloud9CrossAccountGroupPolicy`.
   (You can use a different name for the policy).
#. For :guilabel:`Policy Document`, type the following, substituting :code:`111111111111` for the actual ID of your AWS account.

   .. code-block:: json

      {
        "Version": "2012-10-17",
        "Statement": {
          "Effect": "Allow",
          "Action": "sts:AssumeRole",
          "Resource": "arn:aws:iam::111111111111:role/AWSCloud9EnvironmentMemberCrossAccountRole"
        }
      }

#. Choose :guilabel:`Apply Policy`.

Step 4: Use the Other Account to Open the Shared |envtitle| in Your Account
---------------------------------------------------------------------------

In this step, the user in the other account :code:`999999999999` uses the |IAM| role in your account :code:`111111111111` to open the shared |env| that's also in your account.

#. If you're not already signed in to the AWS Management Console as the user named :guilabel:`AWSCloud9CrossAccountUser` in the other AWS account :code:`999999999999`, sign in now. 
#. On the global navigation bar, choose :guilabel:`AWSCloud9CrossAccountUser`, and then choose :guilabel:`Switch Role`.
#. On the :guilabel:`Switch role` page, choose :guilabel:`Switch Role`.
#. For :guilabel:`Account`, type your AWS account ID: :code:`111111111111`.
#. For :guilabel:`Role`, type :code:`AWSCloud9EnvironmentMemberCrossAccountRole`.
#. For :guilabel:`Display Name`, type a name that helps you more easily identify this role for later use, or leave the suggested display name.
#. Choose :guilabel:`Switch Role`. In the global navigation bar, :guilabel:`AWSCloud9CrossAccountUser` is replaced with the :guilabel:`Display Name` value and also changes its background color.
#. On the global navigation bar, choose :guilabel:`Services`, and then choose :guilabel:`Cloud9`.
#. On the global navigation bar, choose the AWS Region that contains the |env|.
#. In the service navigation pane, choose :guilabel:`Shared with you`.
#. In the card for the |env| that you want to open, choose :guilabel:`Open IDE`.

You can switch back to using the original user identity :code:`AWSCloud9CrossAccountUser`. With the AWS Management Console still open for this step, 
on the global navigation bar choose the :guilabel:`Display Name` value from earlier in this step. Then choose :guilabel:`Back to AWSCloud9CrossAccountUser`.

To use the :guilabel:`AWSCloud9EnvironmentMemberCrossAccountRole` role again, with the AWS Management Console still open for this step, on the global navigation bar 
choose :guilabel:`AWSCloud9CrossAccountUser`. For :guilabel:`Role History`, choose the :guilabel:`Display Name` value from earlier in this step.

.. _share-environment-open:

Open a Shared |envtitle|
========================

To open a shared |env|, you use your |AC9| dashboard. You then use the |AC9IDE| to do things in a shared |env| such as work with files and chat with
other |mems|.

#. Be sure the corresponding access policy is attached to the group or role for your user.
   For more information, see :ref:`share-environment-member-roles`.
#. Sign in to |AC9|, if you are not already signed in. For more information, see :ref:`setup-sign-in-ide` in *Team Setup*.
#. Open the shared |env| from your |AC9| dashboard. For more information, see :doc:`open-environment`.

You use the :guilabel:`Collaborate` window to interact with other |mems|, as described in the rest of this topic.

.. note:: If the :guilabel:`Collaborate` window is not visible, choose the :guilabel:`Collaborate` button. If the
   :guilabel:`Collaborate` button is not visible, on the menu bar, choose :guilabel:`Window, Collaborate`.

.. image:: images/ide-collaborate.png
   :alt: The Collaborate window in the AWS Cloud9 IDE

.. _share-environment-members-list:

See a List of |memslongtitle|
=============================

With the shared |env| open, in the :guilabel:`Collaborate` window, expand :guilabel:`Environment Members`, if the list of |mems| is not visible.

A circle next to each |mem| indicates their online status, as follows.

* Active |mems| have a green circle.
* Offline |mems| have a gray circle.
* Idle |mems| have an orange circle.

.. image:: images/ide-collaborate-status.png
   :alt: Member online status in the AWS Cloud9 IDE

To use code to get a list of |memslong|, call the |AC9| describe |env| memberships operation, as follows.

.. list-table::
   :widths: 1 1
   :header-rows: 0

   * - |cli|
     - :AC9-cli:`describe-environment-memberships <describe-environment-memberships>`
   * - |sdk-cpp|
     - :sdk-cpp-ref:`DescribeEnvironmentMembershipsRequest <LATEST/class_aws_1_1_cloud9_1_1_model_1_1_describe_environment_memberships_request>`, 
       :sdk-cpp-ref:`DescribeEnvironmentMembershipsResult <LATEST/class_aws_1_1_cloud9_1_1_model_1_1_describe_environment_memberships_result>`
   * - |sdk-go|
     - :sdk-for-go-api-ref:`DescribeEnvironmentMemberships <service/cloud9/#Cloud9.DescribeEnvironmentMemberships>`, 
       :sdk-for-go-api-ref:`DescribeEnvironmentMembershipsRequest <service/cloud9/#Cloud9.DescribeEnvironmentMembershipsRequest>`, 
       :sdk-for-go-api-ref:`DescribeEnvironmentMembershipsWithContext <service/cloud9/#Cloud9.DescribeEnvironmentMembershipsWithContext>`
   * - |sdk-java|
     - :sdk-java-api:`DescribeEnvironmentMembershipsRequest <com/amazonaws/services/cloud9/model/DescribeEnvironmentMembershipsRequest>`, 
       :sdk-java-api:`DescribeEnvironmentMembershipsResult <com/amazonaws/services/cloud9/model/DescribeEnvironmentMembershipsResult>`
   * - |sdk-js|
     - :sdk-for-javascript-api-ref:`describeEnvironmentMemberships <AWS/Cloud9.html#describeEnvironmentMemberships-property>`
   * - |sdk-net|
     - :sdk-net-api-v3:`DescribeEnvironmentMembershipsRequest <items/Cloud9/TDescribeEnvironmentMembershipsRequest>`, 
       :sdk-net-api-v3:`DescribeEnvironmentMembershipsResponse <items/Cloud9/TDescribeEnvironmentMembershipsResponse>`
   * - |sdk-php|
     - :sdk-for-php-api-ref:`describeEnvironmentMemberships <api-cloud9-2017-09-23.html#describeenvironmentmemberships>`
   * - |sdk-python|
     - :sdk-for-python-api-ref:`describe_environment_memberships <services/cloud9.html#Cloud9.Client.describe_environment_memberships>`
   * - |sdk-ruby|
     - :sdk-for-ruby-api-ref:`describe_environment_memberships <Aws/Cloud9/Client.html#describe_environment_memberships-instance_method>`
   * - |TWPlong|
     - :TWP-ref:`Get-C9EnvironmentMembershipList <items/Get-C9EnvironmentMembershipList>`
   * - |AC9| API
     - :AC9-api:`DescribeEnvironmentMemberships <API_DescribeEnvironmentMemberships>`

.. _share-environment-active-file:

Open the Active File of an |memlongtitle|
=========================================

With the shared |env| open, in the menu bar, choose the |mem| name. Then choose :guilabel:`Open Active File`.

.. image:: images/ide-collaborate-active-file.png
   :alt: The Open Active File command in the AWS Cloud9 IDE

.. _share-environment-open-file:

Open the Open File of an |memlongtitle|
=======================================

#. With the shared |env| open, in the :guilabel:`Collaborate` window, expand :guilabel:`Environment Members`, if the list of |mems| is not visible.
#. Expand the name of the user whose open file you want to open in your |env|.
#. Double-click the name of the file you want to open.

.. image:: images/ide-collaborate-open-file.png
   :alt: Opening a team member's file in the AWS Cloud9 IDE

.. _share-environment-active-cursor:

Go to the Active Cursor of an |memlongtitle|
============================================

#. With the shared |env| open, in the :guilabel:`Collaborate` window, expand :guilabel:`Environment Members`, if the list of |mems| is not visible.
#. Right-click the |mem| name, and then choose :guilabel:`Show Location`.

.. _share-environment-chat:

Chat with Other |memslongtitle|
===============================

With the shared |env| open, at the bottom of the :guilabel:`Collaborate` window, for :guilabel:`Enter your message here`, type your chat message, and then press :kbd:`Enter`.

.. image:: images/ide-collaborate-chat.png
   :alt: The chat area in the AWS Cloud9 IDE

.. _share-environment-chat-view:

View Chat Messages in a Shared |envtitle|
=========================================

With the shared |env| open, in the :guilabel:`Collaborate` window, expand :guilabel:`Group Chat`, if the list of chat messages is not visible.

.. _share-environment-chat-delete:

Delete a Chat Message from a Shared |envtitle|
==============================================

With the shared |env| open, in the :guilabel:`Collaborate` window, right-click the chat message in :guilabel:`Group Chat`, and then choose :guilabel:`Delete Message`.

.. note:: When you delete a chat message, it is deleted from the |env| for all |mems|.

.. _share-environment-chat-delete-all:

Delete All Chat Messages from a Shared |envtitle|
=================================================

With the shared |env| open, in the :guilabel:`Collaborate` window, right-click anywhere in :guilabel:`Group Chat`, and then choose :guilabel:`Clear history`.

.. note:: When you delete all chat messages, they are deleted from the |env| for all |mems|.

.. _share-environment-change-access:

Change the Access Role of an |memlongtitle|
===========================================

#. Open the |env| that you own and that contains the |mem| whose access role you want to change, if the
   |env| is not already open. For more information, see :doc:`open-environment`.
#. In the :guilabel:`Collaborate` window, expand :guilabel:`Environment Members`, if the list of |mems| is not visible.
#. Do one of the following:

   * Next to the |mem| name whose access role you want to change, choose :guilabel:`R` or :guilabel:`RW`
     to make this |mem| owner or |memrw|, respectively.
   * To change a |memrw| member to |memro|, right-click the |mem| name, and then choose :guilabel:`Revoke Write Access`.
   * To change a |memro| member to |memrw|, right-click the |mem| name, and then choose :guilabel:`Grant Read+Write Access`.

     .. note:: If you make this user a |memrw| member, a dialog box is displayed, containing information
        about possibly putting your
        AWS security credentials at risk. Do not make a user a |memrw| member unless you trust that user to take actions in AWS
        on your behalf. For more information, see the related note in :ref:`share-environment-invite-user`.

To use code to change the access role of a |memlong|, call the |AC9| update |env| membership operation, as follows.

.. list-table::
   :widths: 1 1
   :header-rows: 0

   * - |cli|
     - :AC9-cli:`update-environment-membership <update-environment-membership>`
   * - |sdk-cpp|
     - :sdk-cpp-ref:`UpdateEnvironmentMembershipRequest <LATEST/class_aws_1_1_cloud9_1_1_model_1_1_update_environment_membership_request>`, 
       :sdk-cpp-ref:`UpdateEnvironmentMembershipResult <LATEST/class_aws_1_1_cloud9_1_1_model_1_1_update_environment_membership_result>`
   * - |sdk-go|
     - :sdk-for-go-api-ref:`UpdateEnvironmentMembership <service/cloud9/#Cloud9.UpdateEnvironmentMembership>`, 
       :sdk-for-go-api-ref:`UpdateEnvironmentMembershipRequest <service/cloud9/#Cloud9.UpdateEnvironmentMembershipRequest>`, 
       :sdk-for-go-api-ref:`UpdateEnvironmentMembershipWithContext <service/cloud9/#Cloud9.UpdateEnvironmentMembershipWithContext>`
   * - |sdk-java|
     - :sdk-java-api:`UpdateEnvironmentMembershipRequest <com/amazonaws/services/cloud9/model/UpdateEnvironmentMembershipRequest>`, 
       :sdk-java-api:`UpdateEnvironmentMembershipResult <com/amazonaws/services/cloud9/model/UpdateEnvironmentMembershipResult>`
   * - |sdk-js|
     - :sdk-for-javascript-api-ref:`updateEnvironmentMembership <AWS/Cloud9.html#updateEnvironmentMembership-property>`
   * - |sdk-net|
     - :sdk-net-api-v3:`UpdateEnvironmentMembershipRequest <items/Cloud9/TUpdateEnvironmentMembershipRequest>`, 
       :sdk-net-api-v3:`UpdateEnvironmentMembershipResponse <items/Cloud9/TUpdateEnvironmentMembershipResponse>`
   * - |sdk-php|
     - :sdk-for-php-api-ref:`updateEnvironmentMembership <api-cloud9-2017-09-23.html#updateenvironmentmembership>`
   * - |sdk-python|
     - :sdk-for-python-api-ref:`update_environment_membership <services/cloud9.html#Cloud9.Client.update_environment_membership>`
   * - |sdk-ruby|
     - :sdk-for-ruby-api-ref:`update_environment_membership <Aws/Cloud9/Client.html#update_environment_membership-instance_method>`
   * - |TWPlong|
     - :TWP-ref:`Update-C9EnvironmentMembership <items/Update-C9EnvironmentMembership>`
   * - |AC9| API
     - :AC9-api:`UpdateEnvironmentMembership <API_UpdateEnvironmentMembership>`

.. _share-environment-delete-you:

Remove Your User From a Shared |envtitle|
=========================================

.. note:: You cannot remove your user from an |env| if you are the |env| owner.

   Removing your user from an |env| does not remove your user from |IAM|.
   
#. With the shared |env| open, in the :guilabel:`Collaborate` window, expand :guilabel:`Enviroment Members`, if the list of |mems| is not visible.
#. Do one of the following.

   * Next to :guilabel:`You`, choose the trash can icon.
   * Right-click :guilabel:`You`, and then choose :guilabel:`Leave environment`.

#. When prompted, choose :guilabel:`Leave`.

To use code to remove your user from a shared |env|, call the |AC9| delete |env| membership operation, as follows.

.. list-table::
   :widths: 1 1
   :header-rows: 0

   * - |cli|
     - :AC9-cli:`delete-environment-membership <delete-environment-membership>`
   * - |sdk-cpp|
     - :sdk-cpp-ref:`DeleteEnvironmentMembershipRequest <LATEST/class_aws_1_1_cloud9_1_1_model_1_1_delete_environment_membership_request>`, 
       :sdk-cpp-ref:`DeleteEnvironmentMembershipResult <LATEST/class_aws_1_1_cloud9_1_1_model_1_1_delete_environment_membership_result>`
   * - |sdk-go|
     - :sdk-for-go-api-ref:`DeleteEnvironmentMembership <service/cloud9/#Cloud9.DeleteEnvironmentMembership>`, 
       :sdk-for-go-api-ref:`DeleteEnvironmentMembershipRequest <service/cloud9/#Cloud9.DeleteEnvironmentMembershipRequest>`, 
       :sdk-for-go-api-ref:`DeleteEnvironmentMembershipWithContext <service/cloud9/#Cloud9.DeleteEnvironmentMembershipWithContext>`
   * - |sdk-java|
     - :sdk-java-api:`DeleteEnvironmentMembershipRequest <com/amazonaws/services/cloud9/model/DeleteEnvironmentMembershipRequest>`, 
       :sdk-java-api:`DeleteEnvironmentMembershipResult <com/amazonaws/services/cloud9/model/DeleteEnvironmentMembershipResult>`
   * - |sdk-js|
     - :sdk-for-javascript-api-ref:`deleteEnvironmentMembership <AWS/Cloud9.html#deleteEnvironmentMembership-property>`
   * - |sdk-net|
     - :sdk-net-api-v3:`DeleteEnvironmentMembershipRequest <items/Cloud9/TDeleteEnvironmentMembershipRequest>`, 
       :sdk-net-api-v3:`DeleteEnvironmentMembershipResponse <items/Cloud9/TDeleteEnvironmentMembershipResponse>`
   * - |sdk-php|
     - :sdk-for-php-api-ref:`deleteEnvironmentMembership <api-cloud9-2017-09-23.html#deleteenvironmentmembership>`
   * - |sdk-python|
     - :sdk-for-python-api-ref:`delete_environment_membership <services/cloud9.html#Cloud9.Client.delete_environment_membership>`
   * - |sdk-ruby|
     - :sdk-for-ruby-api-ref:`delete_environment_membership <Aws/Cloud9/Client.html#delete_environment_membership-instance_method>`
   * - |TWPlong|
     - :TWP-ref:`Remove-C9EnvironmentMembership <items/Remove-C9EnvironmentMembership>`
   * - |AC9| API
     - :AC9-api:`DeleteEnvironmentMembership <API_DeleteEnvironmentMembership>`

.. _share-environment-delete-member:

Remove Another |memlongtitle|
=============================

.. note:: To remove any |mem| other than your user from an |env|, you must be signed in to |AC9| using the credentials of the |env| owner.

   Removing a |mem| does not remove the user from |IAM|.
   
#. Open the |env| that contains the |mem| you want to remove, if the |env| is not already open. For more information, see :doc:`open-environment`.
#. In the :guilabel:`Collaborate` window, expand :guilabel:`Environment Members`, if the list of |mems| is not visible.
#. Do one of the following.

   * Next to the name of the |mem| you want to delete, choose the trash can icon.
   * Right-click the name of the |mem| you want to delete, and then choose :guilabel:`Revoke Access`.

#. When prompted, choose :guilabel:`Remove Member`.

To use code to remove a |mem| from an |env|, call the |AC9| delete |env| membership operation, as follows.

.. list-table::
   :widths: 1 1
   :header-rows: 0

   * - |cli|
     - :AC9-cli:`delete-environment-membership <delete-environment-membership>`
   * - |sdk-cpp|
     - :sdk-cpp-ref:`DeleteEnvironmentMembershipRequest <LATEST/class_aws_1_1_cloud9_1_1_model_1_1_delete_environment_membership_request>`, 
       :sdk-cpp-ref:`DeleteEnvironmentMembershipResult <LATEST/class_aws_1_1_cloud9_1_1_model_1_1_delete_environment_membership_result>`
   * - |sdk-go|
     - :sdk-for-go-api-ref:`DeleteEnvironmentMembership <service/cloud9/#Cloud9.DeleteEnvironmentMembership>`, 
       :sdk-for-go-api-ref:`DeleteEnvironmentMembershipRequest <service/cloud9/#Cloud9.DeleteEnvironmentMembershipRequest>`, 
       :sdk-for-go-api-ref:`DeleteEnvironmentMembershipWithContext <service/cloud9/#Cloud9.DeleteEnvironmentMembershipWithContext>`
   * - |sdk-java|
     - :sdk-java-api:`DeleteEnvironmentMembershipRequest <com/amazonaws/services/cloud9/model/DeleteEnvironmentMembershipRequest>`, 
       :sdk-java-api:`DeleteEnvironmentMembershipResult <com/amazonaws/services/cloud9/model/DeleteEnvironmentMembershipResult>`
   * - |sdk-js|
     - :sdk-for-javascript-api-ref:`deleteEnvironmentMembership <AWS/Cloud9.html#deleteEnvironmentMembership-property>`
   * - |sdk-net|
     - :sdk-net-api-v3:`DeleteEnvironmentMembershipRequest <items/Cloud9/TDeleteEnvironmentMembershipRequest>`, 
       :sdk-net-api-v3:`DeleteEnvironmentMembershipResponse <items/Cloud9/TDeleteEnvironmentMembershipResponse>`
   * - |sdk-php|
     - :sdk-for-php-api-ref:`deleteEnvironmentMembership <api-cloud9-2017-09-23.html#deleteenvironmentmembership>`
   * - |sdk-python|
     - :sdk-for-python-api-ref:`delete_environment_membership <services/cloud9.html#Cloud9.Client.delete_environment_membership>`
   * - |sdk-ruby|
     - :sdk-for-ruby-api-ref:`delete_environment_membership <Aws/Cloud9/Client.html#delete_environment_membership-instance_method>`
   * - |TWPlong|
     - :TWP-ref:`Remove-C9EnvironmentMembership <items/Remove-C9EnvironmentMembership>`
   * - |AC9| API
     - :AC9-api:`DeleteEnvironmentMembership <API_DeleteEnvironmentMembership>`

.. _share-environment-best-practices:

|envtitle| Sharing Best Practices
=================================

We recommend the following practices when sharing |envplural|.

* Only invite read/write members you trust to your |envplural|.
* For |envec2plural|, read/write members can use the |env| owner's AWS access credentials, instead of
  their own credentials, to make calls from the |env| to AWS services.
  To prevent this,
  the |env| owner can disable |AC9tempcreds| for the |env|. However, this also prevents the |env| owner
  from making calls. For more information, see :ref:`auth-and-access-control-temporary-managed-credentials`.
* Turn on |CTlong| to track activity in your |envplural|. For more information, see the |CT-ug|_.
* Do not use your AWS account root user to create and share |envplural|. Use |IAM| users in the account instead. For more information, see
  :iam-user-guide:`First-Time Access Only: Your Root User Credentials <introduction_identity-management.html#intro-identity-first-time-access>` and
  :iam-user-guide:`IAM Users <introduction_identity-management.html#intro-identity-users>` in the |IAM-ug|.