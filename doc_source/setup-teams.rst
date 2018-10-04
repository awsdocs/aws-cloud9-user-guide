.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _setup-teams:

#################################
Advanced Team Setup for |AC9long|
#################################

.. meta::
    :description:
        Describes how to do advanced setup for teams to start using AWS Cloud9.

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
     - :ref:`Team Setup <setup>`
   * - I want multiple users in my AWS account to use |AC9|, and I want to restrict their usage to control costs.
     - **This topic**

This topic assumes you have already completed the setup steps in :ref:`Team Setup <setup>`.

In :ref:`Team Setup <setup>`, you created |IAM| groups and added |AC9| access permissions directly to those groups, to ensure that users in those groups can access |AC9|. In this topic,
you will add more access permissions to restrict the kinds of |envplural| that users in those groups can create. This can help control costs related to |AC9| in an AWS account.

To add these access permissions, you create your own set of policies in |IAM| that define the AWS access permissions you want to enforce. (We call each of these a
:dfn:`customer-managed policy`.) Then you attach those customer-managed policies to the |IAM| groups that the users belong to. (In some scenarios, you must also detach
existing AWS managed policies that are already attached to those |IAM| groups.) To set this up, follow
the procedures in this topic.

.. note:: The following procedures cover attaching and detaching policies for |AC9| users groups only. These procedures assume you already have a separate |AC9| users group and |AC9| administrators group and
   that you have only a limited number of users in the |AC9| administrators group. This AWS security best practice can help you better control, track,
   and troubleshoot issues with AWS resource access.

* :ref:`setup-teams-create-policy`
* :ref:`setup-teams-add-policy`
* :ref:`setup-teams-policy-examples`

.. _setup-teams-create-policy:

Step 1: Create a Customer-Managed Policy
========================================

You can create a customer-managed policy using the :ref:`AWS Management Console <setup-teams-create-policy-console>` or 
the :ref:`AWS Command Line Interface (AWS CLI) <setup-teams-create-policy-cli>`.

.. _setup-teams-create-policy-console:

Create a Customer-Managed Policy Using the Console
--------------------------------------------------

#. Sign in to the AWS Management Console, if you are not already signed in.

   We recommend you sign in using credentials for an |IAM| administrator user in your AWS account. If you cannot
   do this, check with your AWS account administrator.

#. Open the |IAM| console. To do this, in the console's navigation bar, choose :guilabel:`Services`. Then choose :guilabel:`IAM`.
#. In the service's navigation pane, choose :guilabel:`Policies`.
#. Choose :guilabel:`Create policy`.
#. In the :guilabel:`JSON` tab, paste one of our suggested :ref:`Customer-Managed Policy Examples <setup-teams-policy-examples>`.

   .. note:: You can also create your own customer-managed policies. For more information, see
      the :IAM-ug:`IAM JSON Policy Reference <reference_policies>` in the |IAM-ug| and the AWS services'
      `documentation <https://aws.amazon.com/documentation/>`_.

#. Choose :guilabel:`Review policy`.
#. On the :guilabel:`Review policy` page, type a :guilabel:`Name` and an optional :guilabel:`Description` for the policy, and then choose :guilabel:`Create policy`.

Repeat this step for each additional customer-managed policy that you want to create, then skip ahead to :ref:`setup-teams-add-policy-console`.

.. _setup-teams-create-policy-cli:

Create a Customer-Managed Policy Using the |cli|
------------------------------------------------

#. On the computer where you run the |cli|, create a file to describe the policy (for example, :file:`policy.json`).

   If you create the file with a different file name, substitute it throughout this procedure.

#. Paste one of our suggested :ref:`Customer-Managed Policy Examples <setup-teams-policy-examples>` into the :file:`policy.json` file.

   .. note:: You can also create your own customer-managed policies. For more information, see
      the :IAM-ug:`IAM JSON Policy Reference <reference_policies>` in the |IAM-ug| and the AWS services'
      `documentation <https://aws.amazon.com/documentation/>`_.

#. From the terminal or command prompt, switch to the directory that contains the :file:`policy.json` file.
#. Run the IAM :code:`create-policy` command, specifying a name for the policy and the :file:`policy.json` file.

   .. code-block:: sh

      aws iam create-policy --policy-document file://policy.json --policy-name MyPolicy

   In the preceding command, replace :code:`MyPolicy` with a name for the policy.

Skip ahead to :ref:`setup-teams-add-policy-cli`.

.. _setup-teams-add-policy:

Step 2: Add Customer-Managed Policies to a Group
================================================

You can add customer-managed policies to a group using the :ref:`AWS Management Console <setup-teams-add-policy-console>` or 
the :ref:`AWS Command Line Interface (AWS CLI) <setup-teams-add-policy-cli>`.

.. _setup-teams-add-policy-console:

Add Customer-Managed Policies to a Group Using the Console
----------------------------------------------------------

#. With the |IAM| console open from the previous procedure, in the service's navigation pane, choose :guilabel:`Groups`.
#. Choose the group's name.
#. On the :guilabel:`Permissions` tab, for :guilabel:`Managed Policies`, choose :guilabel:`Attach Policy`.
#. In the list of policy names, choose the box next to each customer-managed policy you want to attach to the group.
   (If you don't see a specific policy name in the list, type the policy name
   in the :guilabel:`Filter` box to display it.)
#. Choose :guilabel:`Attach Policy`.

.. _setup-teams-add-policy-cli:

Add Customer-Managed Policies to a Group Using the |cli|
--------------------------------------------------------

Run the IAM :code:`attach-group-policy` command, specifying the group's name and the Amazon Resource Name (ARN) of the policy.

.. code-block:: sh

   aws iam attach-group-policy --group-name MyGroup --policy-arn arn:aws:iam::123456789012:policy/MyPolicy

In the preceding command, replace :code:`MyGroup` with the name of the group. Replace :code:`123456789012` with the AWS account ID, and replace 
:code:`MyPolicy` with the name of the customer-managed policy.

.. _setup-teams-policy-examples:

Customer-Managed Policy Examples for Teams Using |AC9|
======================================================

Following are some examples of policies you can use to restrict the kinds of |envplural| that users in a group can create in an AWS account.

* :ref:`setup-teams-policy-examples-prevent-environments`
* :ref:`setup-teams-policy-examples-prevent-ec2-environments`
* :ref:`setup-teams-policy-examples-specific-instance-types`
* :ref:`setup-teams-policy-examples-single-ec2-environment`

.. _setup-teams-policy-examples-prevent-environments:

Prevent Users in a Group from Creating |envtitleplural|
-------------------------------------------------------

The following customer-managed policy, when attached to an |AC9| users group, prevents those users from creating |envplural| in an AWS account. This is useful if you want an 
|IAM| administrator user in your AWS account to manage creating |envplural| instead of users in an |AC9| users group.

.. code-block:: json

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

Note that the preceding customer-managed policy explicitly overrides :code:`"Effect": "Allow"` for :code:`"Action": "cloud9:CreateEnvironmentEC2"` and :code:`"cloud9:CreateEnvironmentSSH"` on :code:`"Resource": "*"` in the
:code:`AWSCloud9User` managed policy that is already attached to the |AC9| users group.

.. _setup-teams-policy-examples-prevent-ec2-environments:

Prevent Users in a Group from Creating |envec2titleplural|
----------------------------------------------------------

The following customer-managed policy, when attached to an |AC9| users group, prevents those users from creating |envec2plural| in an AWS account. This is useful if you want an 
|IAM| administrator user in your AWS account to manage creating |envec2plural| instead of users in an |AC9| users group. This assumes you haven't also attached a policy that
prevents users in that group from creating |envsshplural|. Otherwise, those users won't be able to create |envplural| at all.

.. code-block:: json

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

Note that the preceding customer-managed policy explicitly overrides :code:`"Effect": "Allow"` for :code:`"Action": "cloud9:CreateEnvironmentEC2"` on :code:`"Resource": "*"` in the
:code:`AWSCloud9User` managed policy that is already attached to the |AC9| users group.

.. _setup-teams-policy-examples-specific-instance-types:

Allow Users in a Group to Create |envec2titleplural| Only with Specific |EC2| Instance Types
--------------------------------------------------------------------------------------------

The following customer-managed policy, when attached to an |AC9| users group, allows those users to create |envec2plural| that only use instance types starting with :code:`t2` in an AWS account. This policy assumes you haven't also attached a policy that
prevents users in that group from creating |envec2plural|. Otherwise, those users won't be able to create |envec2plural| at all.

You can replace :code:`"t2.*"` in the following policy with a different instance class (for example, :code:`"m4.*"`). Or you can restrict it to multiple instance classes or instance types (for example,
:code:`[ "t2.*", "m4.*" ]` or :code:`[ "t2.micro", "m4.large" ]`).

For an |AC9| users group, detach the :code:`AWSCloud9User` managed policy from the group, and then add the following customer-managed policy in its place. (If you do not detach the :code:`AWSCloud9User`
managed policy, the following customer-managed policy will have no effect.)

.. code-block:: json

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

Note that the preceding customer-managed policy also allows those users to create |envsshplural|. To prevent those users from creating |envsshplural| altogether, remove
:code:`"cloud9:CreateEnvironmentSSH",` from the preceding customer-managed policy.

.. _setup-teams-policy-examples-single-ec2-environment:

Allow Users in a Group to Create Only a Single |envec2title| Per AWS Region
---------------------------------------------------------------------------

The following customer-managed policy, when attached to an |AC9| users group, allows each of those users to create a maximum of one |envec2| per AWS Region that |AC9| is available in. This is done by restricting 
the name of the |env| to one specific name in that AWS Region (in this example, :code:`my-demo-environment`).

.. note:: |AC9| doesn't enable restricting the creation of |envplural| to specific AWS Regions. Nor does it enable restricting the overall number of |envplural| that can be created 
   (other than the published :ref:`service limits <limits>`). 

For an |AC9| users group, detach the :code:`AWSCloud9User` managed policy from the group, and then add the following customer-managed policy in its place. (If you do not detach the :code:`AWSCloud9User`
managed policy, the following customer-managed policy will have no effect.)

.. code-block:: json

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

Note that the preceding customer-managed policy allows those users to create |envsshplural|. To prevent those users from creating |envsshplural| altogether, remove
:code:`"cloud9:CreateEnvironmentSSH",` from the preceding customer-managed policy.

For additional examples, see the :ref:`auth-and-access-control-customer-policies-examples` in :ref:`Authentication and Access Control <auth-and-access-control>`.

.. _setup-teams-next-steps:

Next Steps
==========

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - **Task**
     - **See this topic**
   * - Create an |envfirst|, and then use the |AC9IDE| to work with code in your new |env|.
     - :ref:`Creating an Environment <create-environment>`
   * - Learn how to use the |AC9IDE|.
     - :ref:`IDE Tutorial <tutorial>`
   * - Invite others to use your new |env| along with you, in real time and with text chat support.
     - :ref:`Working with Shared Environments <share-environment>`