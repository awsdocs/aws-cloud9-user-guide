.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _auth-and-access-control:

##########################################
Access Permissions Reference for |AC9long|
##########################################

.. meta::
    :description:
        Describes how to permit and deny access to AWS Cloud9 resources.

Access to |AC9| requires AWS access credentials. Those credentials must have permissions to do things such as create, share, or delete an |envfirst|.
The following sections describe how you can use |IAMlong| (|IAM|) to allow or deny access to your |AC9| resources and then map those permissions to credentials.

* :ref:`auth-and-access-control-overview`
* :ref:`auth-and-access-control-managed-policies`
* :ref:`auth-and-access-control-customer-policies`
* :ref:`auth-and-access-control-temporary-managed-credentials`

.. _auth-and-access-control-overview:

Overview
========

This section provides an overview of the |IAM| authentication and access control model
that applies to |AC9|.

.. note:: If you just want to set up predefined sets of access permissions for common usage
   scenarios and user types, skip ahead to :ref:`auth-and-access-control-managed-policies`.

* :ref:`auth-and-access-control-overview-auth`
* :ref:`access-permissions-overview-access-control`
* :ref:`access-permissions-overview-resources-and-operations`
* :ref:`auth-and-access-control-overview-resource-ownership`
* :ref:`access-permissions-overview-managing-access`

.. _auth-and-access-control-overview-auth:

Authentication
--------------

You can access AWS as any of the following types of identities:

**AWS account root user**

When you sign up for AWS, you provide an email address and password that is associated with your AWS
account. These are your root credentials, and they provide complete access to all of your AWS resources.

.. important:: As an AWS security best practice, we recommend that you use the root credentials only to create an IAM :dfn:`administrator group` with an 
   IAM :dfn:`administrator user`. This is a group that gives the user full permissions to your AWS account. Then you can use this administrator user to create other |IAM| users and roles with
   limited permissions. For more information, see :iam-user-guide:`Create Individual IAM Users <best-practices.html#create-iam-users>` and
   :IAM-ug:`Creating Your First IAM Admin User and Group <getting-started_create-admin-group>` in the |IAM-ug|.

**IAM user**

An :dfn:`IAM user` is simply an identity within your AWS account that has specific custom permissions
(for example, permissions to create an |envfirst|). You can use an |IAM| user name and password
to sign in to secure AWS webpages like the |AC9| console, |console|,
AWS Discussion Forums, and |SUPlong| Support Center.

In addition to a user name and password, you can also generate access keys for each user. You can use these keys when you access AWS services
programmatically, either through one of the several AWS SDKs or by using the |clilong| (|cli|) or the aws-shell. The AWS SDKs, the |cli|, and the aws-shell use these access keys to
cryptographically sign your request. If you don't use these tools, you must sign the request yourself. |AC9| supports Signature Version 4, a protocol
for authenticating inbound API requests. For more information about authenticating requests, see :AWS-gr:`Signature Version 4 Signing Process <signature-version-4>` in the |AWS-gr|.

**IAM role**

An :dfn:`IAM role` is another |IAM| identity you can create in your account that has specific permissions.
It's similar to an |IAM| user, but it isn't associated with a specific person. An |IAM| role enables
you to obtain temporary access keys that can be used to access
AWS services and resources. |IAM| roles with temporary credentials are useful in the following situations:

**AWS service access**

You can use an |IAM| role in your account to grant an AWS service permissions to access your account's
resources. For example, you can create a role that allows |LAMlong| to access an |S3| bucket on your behalf, and then load data stored in the bucket into an
|RSlong|. For more information, see :IAM-ug:`Creating a Role to Delegate Permissions to an AWS Service <id_roles_create_for-service>` in the |IAM-ug|.

**Applications running on Amazon EC2**

Instead of storing access keys within an |EC2| instance for use by applications running on the instance
and making AWS API requests, you can use an |IAM| role to manage temporary credentials for
these applications. To assign an AWS role to an |EC2|
instance and make it available to all of its applications, you can create an
:dfn:`instance profile` that is attached to the instance. An instance profile
contains the role and enables programs running on the |EC2| instance to get temporary
credentials. For more information, see
:ref:`credentials-temporary` and
:IAM-ug:`Using an IAM Role to Grant Permissions to Applications Running on Amazon EC2 Instances <id_roles_use_switch-role-ec2>` in the |IAM-ug|.

.. note:: Instead of attaching an instance profile to an |EC2| instance that connects to an |env|, |AC9| can automatically set up and manage temporary credentials
   on your behalf in an |envec2|. For more information, see :ref:`auth-and-access-control-temporary-managed-credentials`.
   
**Federated user access**

Instead of creating an |IAM| user, you can use pre-existing user identities from |ADSlong|, your enterprise user
directory, or a web identity provider. These are known as :dfn:`federated users`. AWS assigns a role to a federated user when access is requested
through an identity provider. For more information, see
:iam-user-guide:`Federated Users and Roles <introduction_access-management.html#intro-access-roles>` in the |IAM-ug|.

.. _access-permissions-overview-access-control:

Access Control
--------------

You can have valid credentials to authenticate your requests, but unless you have permissions, you cannot create or access |AC9| resources. For example,
you must have permissions to create, share, or delete an |envfirst|.

Every AWS resource is owned by an AWS account, and permissions to create or access a resource are governed by permissions policies. An account administrator
can attach permissions policies to |IAM| identities (that is, users, groups, and roles).

When you grant permissions, you decide who is getting the permissions, the resources they can access, and the actions that can be performed on those resources.

.. _access-permissions-overview-resources-and-operations:

|AC9| Resources and Operations
------------------------------

In |AC9|, the primary resource is an |envfirst|. In a policy, you use an Amazon Resource Name (ARN) to
identify the resource that the policy applies to. The following table lists |env| ARNs.
For more information, see :AWS-gr:`Amazon Resource Names (ARNs) and AWS Service Namespaces <aws-arns-and-namespaces>` in the |AWS-gr|.

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - Resource type
     - ARN format
   * - |envtitle|
     - :samp:`arn:aws:cloud9:{REGION_ID}:{ACCOUNT_ID}:environment:{ENVIRONMENT_ID}`
   * - Every |env| owned by the specified account in the specified region
     - :samp:`arn:aws:cloud9:{REGION_ID}:{ACCOUNT_ID}:environment:*`
   * - Every |env| owned by the specified account in the specified region
     - :samp:`arn:aws:cloud9:{REGION_ID}:{ACCOUNT_ID}:*`
   * - Every |AC9| resource, regardless of account and region
     - :samp:`arn:aws:cloud9:*`

For example, you can indicate a specific |env| in your statement using its ARN, as follows.

.. code-block:: text

   "Resource": "arn:aws:cloud9:us-east-2:123456789012:environment:70d899206236474f9590d93b7c41dfEX"

To specify all resources, use the wildcard character (:code:`*`) in the :code:`Resource` element, as follows.

.. code-block:: text

   "Resource": "*"

To specify multiple resources in a single statement, separate their ARNs with commas, as follows.

.. code-block:: text

   "Resource": [
     "arn:aws:cloud9:us-east-2:123456789012:environment:70d899206236474f9590d93b7c41dfEX",
     "arn:aws:cloud9:us-east-2:123456789012:environment:81e900317347585a0601e04c8d52eaEX"
   ]

|AC9| provides a set of operations to work with |AC9| resources. For a list, see the :ref:`auth-and-access-control-ref`.

.. _auth-and-access-control-overview-resource-ownership:

Understanding Resource Ownership
--------------------------------

The AWS account owns the resources that are created in the account, regardless of who created the resources. For example:

* If you use the root account credentials of your AWS account to create an |envfirst| (which, although possible, is not recommend as an AWS security best practice), your AWS account is the |memown| of the |env|.
* If you create an |IAM| user in your AWS account and grant permissions to create an |env| to that user, the user can create an |env|. However,
  your AWS account, to which the user belongs, owns the |env|.
* If you create an |IAM| role in your AWS account with permissions to create an |env|, anyone who can assume the role can create
  an |env|. Your AWS account, to which the role belongs, owns the |env|.

.. _access-permissions-overview-managing-access:

Managing Access to Resources
----------------------------

A permissions policy describes who has access to which resources.

.. note:: This section discusses the use of |IAM| in |AC9|. It doesn't provide detailed information about the |IAM| service. For complete |IAM| documentation,
   see :IAM-ug:`What Is IAM? <introduction>` in the |IAM-ug|. For information about |IAM| policy syntax and descriptions, see the
   :IAM-ug:`IAM JSON Policy Reference <reference_policies>` in the |IAM-ug|.

Policies attached to an |IAM| identity are referred to as :dfn:`identity-based policies` (or :dfn:`IAM policies`). Policies attached to a resource are referred to as
:dfn:`resource-based policies`. |AC9| supports both identity-based and resource-based policies.

Each of the following API actions requires only an |IAM| policy to be attached to the |IAM| identity who
wants to call these API actions.

* :code:`CreateEnvironmentEC2`
* :code:`DescribeEnvironments`

The following API actions require a resource-based policy. An |IAM| policy isn't required, but |AC9| will
use an |IAM| policy if it is attached to the |IAM| identity who
wants to call these API actions. The resource-based policy must be applied to the desired |AC9| resource.

* :code:`CreateEnvironmentMembership`
* :code:`DeleteEnvironment`
* :code:`DeleteEnvironmentMembership`
* :code:`DescribeEnvironmentMemberships`
* :code:`DescribeEnvironmentStatus`
* :code:`UpdateEnvironment`
* :code:`UpdateEnvironmentMembership`

For details on what each of these API actions do, see the |AC9-api|.

You cannot attach a resource-based policy to an |AC9| resource directly. Instead, |AC9| attaches the appropriate resource-based policies to |AC9| resources as you add, modify, update, or delete |memslong|.

To grant a user permissions to perform actions on |AC9| resources, you attach a permissions policy to an |IAM| group that the user belongs to. We recommend you attach
an AWS managed (predefined) policy for |AC9| whenever possible. AWS managed policies are easier and faster
to attach. They also contain predefined sets of access permissions for common usage
scenarios and user types, such as full administration of an |env|, |env| users, and users who have only |memro| access to an |env|. For a list of
AWS managed policies for |AC9|, see :ref:`auth-and-access-control-managed-policies`.

For more detailed usage scenarios and unique user types, you can create and attach your own customer-managed policies.
See :ref:`setup-teams` and :ref:`auth-and-access-control-customer-policies`.

To attach an |IAM| policy (AWS managed or customer-managed) to an |IAM| identity, 
see :iam-user-guide:`Attaching IAM Policies (Console) <access_policies_manage-attach-detach.html#attach-managed-policy-console>` in the |IAM-ug|.

.. _auth-and-access-control-managed-policies:

AWS Managed (Predefined) Policies for |AC9|
===========================================

AWS addresses many common use cases by providing standalone |IAM| policies that AWS creates and administers.
These AWS managed policies grant necessary
permissions for common use cases so you can avoid having to investigate what permissions are needed. For example, you can use AWS managed policies for |AC9| to quickly and easily
allow users to have full administration of an |envfirst|, act as an |env| user, or use an |env| they are added to. For more information, 
see :iam-user-guide:`AWS Managed Policies <access_policies_managed-vs-inline.html#aws-managed-policies>` in the |IAM-ug|.

To attach an AWS managed policy to an |IAM| identity, see :iam-user-guide:`Attaching IAM Policies (Console) <access_policies_manage-attach-detach.html#attach-managed-policy-console>` in the |IAM-ug|.

The following AWS managed policies, which you can attach to |IAM| identities in your account, are specific to |AC9|.

* :code:`AWSCloud9Administrator`: Provides the following permissions:

  * |EC2|: get information about Amazon VPCs and subnets in their AWS account. 
  * |AC9|: all |AC9| actions in their AWS account.
  * |IAM|: get information about |IAM| users in their AWS account, and create the |AC9| service-linked role in their AWS account as needed.

  The :code:`AWSCloud9Administrator` managed policy contains the following permissions:

  .. code-block:: json

     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Action": [
             "cloud9:*",
             "ec2:DescribeSubnets",
             "ec2:DescribeVpcs",
             "iam:GetUser",
             "iam:ListUsers"
           ],
           "Resource": "*"
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

* :code:`AWSCloud9User`: Provides the following permissions:

  * |EC2|: get information about Amazon VPCs and subnets in their AWS account.
  * |AC9|: create and get information about their |envplural|, and get and change user settings for their |envplural|.
  * |IAM|: get information about |IAM| users in their AWS account, and create the |AC9| service-linked role in their AWS account as needed.

  The :code:`AWSCloud9User` managed policy contains the following permissions:

  .. code-block:: json

     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Action": [
             "cloud9:CreateEnvironment*",
             "cloud9:GetUserPublicKey",
             "cloud9:GetUserSettings",
             "cloud9:UpdateUserSettings",
             "cloud9:ValidateEnvironmentName",
             "ec2:DescribeSubnets",
             "ec2:DescribeVpcs",
             "iam:GetUser",
             "iam:ListUsers"
           ],
           "Resource": "*"
         },
         {
           "Effect": "Allow",
           "Action": [
             "cloud9:DescribeEnvironmentMemberships"
           ],
           "Resource": "*",
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

* :code:`AWSCloud9EnvironmentMember`: Provides the following permissions:

  * |AC9|: get information about |envplural| they've been invited to, and get user settings for |envplural| they've been invited to.
  * |IAM|: get information about |IAM| users in their AWS account.

  The :code:`AWSCloud9EnvironmentMember` managed policy contains the following permissions:

  .. code-block:: json

     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Action": [
             "cloud9:GetUserSettings",
             "cloud9:UpdateUserSettings",
             "iam:GetUser",
             "iam:ListUsers"
           ],
           "Resource": "*"
         },
         {
           "Effect": "Allow",
           "Action": [
             "cloud9:DescribeEnvironmentMemberships"
           ],
           "Resource": "*",
           "Condition": {
             "Null": {
               "cloud9:UserArn": "true",
               "cloud9:EnvironmentId": "true"
             }
           }
         }
       ]
     }

.. _auth-and-access-control-customer-policies:

Creating Customer-Managed Policies for |AC9|
============================================

If none of the AWS managed policies meet your access control requirements, you can create and attach your own customer-managed policies.

To create a customer-managed policy, see :iam-user-guide:`Create an IAM Policy (Console) <access_policies_create.html#access_policies_create-start>` in the |IAM-ug|.

* :ref:`auth-and-access-control-customer-policies-specifying-policy-elements`
* :ref:`auth-and-access-control-customer-policies-examples`
* :ref:`auth-and-access-control-ref`

.. _auth-and-access-control-customer-policies-specifying-policy-elements:

Specifying Policy Elements: Effects, Principals, Actions, and Resources
-----------------------------------------------------------------------

For each |AC9| resource, the service defines a set of API operations. To grant permissions for these API operations, |AC9| defines a set of actions that you can
specify in a policy.

The following are the basic policy elements:

* :code:`Effect`: You specify the effect, either allow or deny, when the user requests the action. If you don't explicitly grant access to (allow) a resource,
  access is implicitly denied. You can also explicitly deny access to a resource. You might do this to
  ensure a user cannot access a resource,
  even if a different policy grants access.
* :code:`Principal`: In identity-based policies (IAM policies), the user the policy is attached to is the implicit principal.
  For resource-based policies, you specify the user, account, service, or other entity that you want to receive permissions.
* :code:`Resource`: You use an ARN to identify the resource that the policy applies to.
* :code:`Action`: You use action keywords to identify resource operations you want to allow or deny. For example, the :code:`cloud9:CreateEnvironmentEC2` permission gives the user
  permissions to perform the :code:`CreateEnvironmentEC2` operation.

To learn more about |IAM| policy syntax and descriptions, see the :IAM-ug:`IAM JSON Policy Reference <reference_policies>` in the |IAM-ug|.

For a table showing all of the |AC9| API actions and the resources they apply to, see the :ref:`auth-and-access-control-ref`.

.. _auth-and-access-control-customer-policies-examples:

Customer-Managed Policy Examples
--------------------------------

In this section, you can find example policies that grant permissions for |AC9| actions. You can adapt the following example |IAM| policies to allow or explicitly deny
|AC9| access for your |IAM| identities.

To create or attach a customer-managed policy to an |IAM| identity, see 
:iam-user-guide:`Create an IAM Policy (Console) <access_policies_create.html#access_policies_create-start>` and 
:iam-user-guide:`Attaching IAM Policies (Console) <access_policies_manage-attach-detach.html#attach-managed-policy-console>` in the |IAM-ug|.

.. note:: The following examples use the US East (Ohio) Region (:code:`us-east-2`), a fictitious AWS account ID (:code:`123456789012`), and a
   fictitious |envfirst| ID (:code:`81e900317347585a0601e04c8d52eaEX`).

* :ref:`auth-and-access-control-customer-policies-examples-describe-environments`
* :ref:`auth-and-access-control-customer-policies-examples-create-environment-ec2`
* :ref:`auth-and-access-control-customer-policies-examples-ec2-instance-types`
* :ref:`auth-and-access-control-customer-policies-examples-ec2-subnets`
* :ref:`auth-and-access-control-customer-policies-examples-ec2-name`
* :ref:`auth-and-access-control-customer-policies-examples-no-ec2`
* :ref:`auth-and-access-control-customer-policies-examples-update-environment`
* :ref:`auth-and-access-control-customer-policies-examples-describe-environment-memberships`
* :ref:`auth-and-access-control-customer-policies-examples-restrict-collaboration`
* :ref:`auth-and-access-control-customer-policies-examples-no-collaboration`
* :ref:`auth-and-access-control-customer-policies-examples-update-environment-membership`
* :ref:`auth-and-access-control-customer-policies-examples-delete-environment-membership`
* :ref:`auth-and-access-control-customer-policies-examples-delete-environment`

.. _auth-and-access-control-customer-policies-examples-describe-environments:

Get Information About |envtitleplural|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example |IAM| policy statement, attached to an |IAM| entity, allows that entity to get information about any |env| in their account.

.. code-block:: json

  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "cloud9:DescribeEnvironments",
        "Resource": "*"
      }
    ]
  }

Note that the preceding access permission is already included in the AWS managed policies :code:`AWSCloud9Administrator` and :code:`AWSCloud9User`.

.. _auth-and-access-control-customer-policies-examples-create-environment-ec2:

Create |envec2titleplural|
~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example |IAM| policy statement, attached to an |IAM| entity, allows that entity to create |envfirstec2plural| in their account.

.. code-block:: json

  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "cloud9:CreateEnvironmentEC2",
        "Resource": "*"
      }
    ]
  }

Note that the preceding access permission is already included in the AWS managed policies :code:`AWSCloud9Administrator` and :code:`AWSCloud9User`.

.. _auth-and-access-control-customer-policies-examples-ec2-instance-types:

Create |envec2titleplural| with Specific |EC2| Instance Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example |IAM| policy statement, attached to an |IAM| entity, allows that entity to create |envfirstec2plural| in their account. However, |envec2plural| can 
use only the specified class of |EC2| instance types.

.. code-block:: json

  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "cloud9:CreateEnvironmentEC2",
        "Resource": "*",
        "Condition": {
          "StringLike": {
            "cloud9:InstanceType": "t2.*"
          }
        }
      }
    ]
  }

Note that if the AWS managed policy :code:`AWSCloud9Administrator` or :code:`AWSCloud9User` is already attached to the |IAM| entity, those AWS managed policies will override the 
behavior of the preceding |IAM| policy statement, as those AWS managed policies are more permissive.

.. _auth-and-access-control-customer-policies-examples-ec2-subnets:

Create |envec2titleplural| in Specific |VPC| Subnets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example |IAM| policy statement, attached to an |IAM| entity, allows that entity to create |envfirstec2plural| in their account. However, |envec2plural| can 
use only the specified |VPC| subnets.

.. code-block:: json

  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "cloud9:CreateEnvironmentEC2",
        "Resource": "*",
        "Condition": {
          "StringLike": {
            "cloud9:SubnetId": [
              "subnet-12345678",
              "subnet-23456789"
            ]
          }
        }
      }
    ]
  }

Note that if the AWS managed policy :code:`AWSCloud9Administrator` or :code:`AWSCloud9User` is already attached to the |IAM| entity, those AWS managed policies will override the 
behavior of the preceding |IAM| policy statement, as those AWS managed policies are more permissive.

.. _auth-and-access-control-customer-policies-examples-ec2-name:

Create an |envec2title| with a Specific |envtitle| Name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example |IAM| policy statement, attached to an |IAM| entity, allows that entity to create an |envfirstec2| in their account. However, the |envec2| can 
use only the specified name.

.. code-block:: json

  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "cloud9:CreateEnvironmentEC2",
        "Resource": "*",
        "Condition": {
          "StringEquals": {
            "cloud9:EnvironmentName": "my-demo-environment"
          }
        }
      }
    ]
  }

Note that if the AWS managed policy :code:`AWSCloud9Administrator` or :code:`AWSCloud9User` is already attached to the |IAM| entity, those AWS managed policies will override the 
behavior of the preceding |IAM| policy statement, as those AWS managed policies are more permissive.

.. _auth-and-access-control-customer-policies-examples-no-ec2:

Create |envsshtitleplural| Only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example |IAM| policy statement, attached to an |IAM| entity, allows that entity to create |envfirstsshplural| in their account. However, the entity cannot 
create |envfirstec2plural|.

.. code-block:: json

  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "cloud9:CreateEnvironmentSSH",
        "Resource": "*"
      },
      {
        "Effect": "Deny",
        "Action": "cloud9:CreateEnvironmentEC2",
        "Resource": "*"
      }
    ]
  }

.. _auth-and-access-control-customer-policies-examples-update-environment:

Update |envtitleplural|, or Prevent Updating an |envtitle|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example |IAM| policy statement, attached to an |IAM| entity, allows that entity to change information about any |envfirst| in their account.

.. code-block:: json

  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "cloud9:UpdateEnvironment",
        "Resource": "*"
      }
    ]
  }

Note that the preceding access permission is already included in the AWS managed policy :code:`AWSCloud9Administrator`.

The following example |IAM| policy statement, attached to an |IAM| entity, explicitly prevents that entity from changing information about the |env| with the specified ARN.

.. code-block:: json

  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Deny",
        "Action": "cloud9:UpdateEnvironment",
        "Resource": "arn:aws:cloud9:us-east-2:123456789012:environment:81e900317347585a0601e04c8d52eaEX"
      }
    ]
  }

.. _auth-and-access-control-customer-policies-examples-describe-environment-memberships:

Get Lists of |memslongtitle|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example |IAM| policy statement, attached to an |IAM| entity, allows that entity to get a list of |mems| for any |env| in their account.

.. code-block:: json

  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "cloud9:DescribeEnvironmentMemberships",
        "Resource": "*"
      }
    ]
  }

Note that the preceding access permission is already included in the AWS managed policy :code:`AWSCloud9Administrator`. Also note that the preceding access permission is more permissive 
than the equivalent access permission in the AWS managed policy :code:`AWSCloud9User`.

.. _auth-and-access-control-customer-policies-examples-restrict-collaboration:

Share |envtitleplural| Only with a Specific User
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example |IAM| policy statement, attached to an |IAM| entity, allows that entity to share any |env| in their account with only the specified user.

.. code-block:: json

   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "cloud9:CreateEnvironmentMembership"
         ],
         "Resource": "*",
         "Condition": {
           "StringEquals": {
             "cloud9:UserArn": "arn:aws:iam::123456789012:user/MyDemoUser"
           }
         }
       }
     ]
   }

Note that if the AWS managed policy :code:`AWSCloud9Administrator` or :code:`AWSCloud9User` is already attached to the |IAM| entity, those AWS managed policies will override the 
behavior of the preceding |IAM| policy statement, as those AWS managed policies are more permissive.

.. _auth-and-access-control-customer-policies-examples-no-collaboration:

Prevent Sharing |envtitleplural|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example |IAM| policy statement, attached to an |IAM| entity, prevents that entity from sharing any |env| in their account.

.. code-block:: json

   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Deny",
         "Action": [
           "cloud9:CreateEnvironmentMembership",
           "cloud9:UpdateEnvironmentMembership"
         ],
         "Resource": "*"
       }
     ]
   }

.. _auth-and-access-control-customer-policies-examples-update-environment-membership:

Change, or Prevent Changing, the Settings of |memslongtitle|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example |IAM| policy statement, attached to an |IAM| entity, allows that entity to change the settings of |mems| in any |env| in their account.

.. code-block:: json

  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "cloud9:UpdateEnvironmentMembership",
        "Resource": "*"
      }
    ]
  }

Note that the preceding access permission is already included in the AWS managed policy :code:`AWSCloud9Administrator`.

The following example |IAM| policy statement, attached to an |IAM| entity, explicitly prevents that entity from changing the settings of |mems| in the |env| with the specified ARN.

.. code-block:: json

  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Deny",
        "Action": "cloud9:UpdateEnvironmentMembership",
        "Resource": "arn:aws:cloud9:us-east-2:123456789012:environment:81e900317347585a0601e04c8d52eaEX"
      }
    ]
  }

.. _auth-and-access-control-customer-policies-examples-delete-environment-membership:

Remove, or Prevent Removing, |memslongtitle|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example |IAM| policy statement, attached to an |IAM| entity, allows that entity to remove any |mem| from any |env| in their account.

.. code-block:: json

  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "cloud9:DeleteEnvironmentMembership",
        "Resource": "*"
      }
    ]
  }

Note that the preceding access permission is already included in the AWS managed policy :code:`AWSCloud9Administrator`.

The following example |IAM| policy statement, attached to an |IAM| entity, explicitly prevents that entity from removing any |mem| from the |env| with the specified ARN.

.. code-block:: json

  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Deny",
        "Action": "cloud9:DeleteEnvironmentMembership",
        "Resource": "arn:aws:cloud9:us-east-2:123456789012:environment:81e900317347585a0601e04c8d52eaEX"
      }
    ]
  }

.. _auth-and-access-control-customer-policies-examples-delete-environment:

Delete |envtitleplural|, or Prevent Deleting an |envtitle|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example |IAM| policy statement, attached to an |IAM| entity, allows that entity to delete any |env| in their account.

.. code-block:: json

  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": "cloud9:DeleteEnvironment",
        "Resource": "*"
      }
    ]
  }

Note that the preceding access permission is already included in the AWS managed policy :code:`AWSCloud9Administrator`.

The following example |IAM| policy statement, attached to an |IAM| entity, explicitly prevents that entity from deleting the |env| with the specified ARN.

.. code-block:: json

  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Deny",
        "Action": "cloud9:DeleteEnvironment",
        "Resource": "arn:aws:cloud9:us-east-2:123456789012:environment:81e900317347585a0601e04c8d52eaEX"
      }
    ]
  }

.. _auth-and-access-control-ref:

|AC9| Permissions Reference
---------------------------

You can use the following table as a reference when you are setting up access control and writing permissions policies that you can attach to an |IAM| identity (identity-based policies).

You can use AWS-wide condition keys in your |AC9| policies to express conditions. For a list, see
:iam-user-guide:`IAM JSON Policy Elements: Condition <reference_policies_elements_condition.html>` in the |IAM-ug|.

You specify the actions in the policy's :code:`Action` field. To specify an action, use the :code:`cloud9:` prefix followed by the API operation name
(for example, :code:`"Action": "cloud9:DescribeEnvironments"`). To specify multiple actions in a single statement, separate them with commas
(for example, :code:`"Action": [ "cloud9:UpdateEnvironment", "cloud9:DeleteEnvironment" ]`).

* :ref:`auth-and-access-control-ref-wildcards`
* :ref:`auth-and-access-control-ref-matrix`

.. _auth-and-access-control-ref-wildcards:

Using Wildcard Characters
~~~~~~~~~~~~~~~~~~~~~~~~~

You specify an ARN, with or without a wildcard character (:code:`*`), as the resource value in the policy's :code:`Resource` field. You can use a wildcard to specify
multiple actions or resources. For example, :code:`cloud9:*` specifies all |AC9| actions and :code:`cloud9:Describe*` specifies all |AC9| actions
that begin with :code:`Describe`.

The following example allows an |IAM| entity to get information about |envplural| and |env| memberships for any |env| in their account.

.. code-block:: json

   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "cloud9:Describe*"
         ],
         "Resource": "*"
       }
     ]
   }

Note that the preceding access permission is already included in the AWS managed policy :code:`AWSCloud9Administrator`. Also note that the preceding access permission is more permissive 
than the equivalent access permission in the AWS managed policy :code:`AWSCloud9User`.

.. _auth-and-access-control-ref-matrix:

|AC9| API Operations and Required Permissions for Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 1 2 2
   :header-rows: 1

   * - |AC9| operation
     - Required permission (API action)
     - Resource
   * - :code:`CreateEnvironmentEC2`
     - :code:`cloud9:CreateEnvironmentEC2`

       Required to create an |envfirstec2|.
     - :code:`*`
   * - :code:`CreateEnvironmentMembership`
     - :code:`cloud9:CreateEnvironmentMembership`

       Required to add a |mem| to an |env|.
     - :samp:`arn:aws:cloud9:{REGION_ID}:{ACCOUNT_ID}:environment:{ENVIRONMENT_ID}`
   * - :code:`DeleteEnvironment`
     - :code:`cloud9:DeleteEnvironment`

       Required to delete an |env|.
     - :samp:`arn:aws:cloud9:{REGION_ID}:{ACCOUNT_ID}:environment:{ENVIRONMENT_ID}`
   * - :code:`DeleteEnvironmentMembership`
     - :code:`cloud9:DeleteEnvironmentMembership`

       Required to remove a |mem| from an |env|.
     - :samp:`arn:aws:cloud9:{REGION_ID}:{ACCOUNT_ID}:environment:{ENVIRONMENT_ID}`
   * - :code:`DescribeEnvironmentMemberships`
     - :code:`cloud9:DescribeEnvironmentMemberships`

       Required to get a list of |mems| in an |env|.
     - :samp:`*`
   * - :code:`DescribeEnvironments`
     - :code:`cloud9:DescribeEnvironments`

       Required to get information about an |env|.
     - :samp:`arn:aws:cloud9:{REGION_ID}:{ACCOUNT_ID}:environment:{ENVIRONMENT_ID}`
   * - :code:`DescribeEnvironmentStatus`
     - :code:`cloud9:DescribeEnvironmentStatus`

       Required to get information about the status of an |env|.
     - :samp:`arn:aws:cloud9:{REGION_ID}:{ACCOUNT_ID}:environment:{ENVIRONMENT_ID}`
   * - :code:`UpdateEnvironment`
     - :code:`cloud9:UpdateEnvironment`

       Required to update settings for an |env|.
     - :samp:`arn:aws:cloud9:{REGION_ID}:{ACCOUNT_ID}:environment:{ENVIRONMENT_ID}`
   * - :code:`UpdateEnvironmentMembership`
     - :code:`cloud9:UpdateEnvironmentMembership`

       Required to update settings for a |mem| in an |env|.
     - :samp:`arn:aws:cloud9:{REGION_ID}:{ACCOUNT_ID}:environment:{ENVIRONMENT_ID}`

.. _auth-and-access-control-temporary-managed-credentials:

|AC9tempcredstitle|
===================

For an |envfirstec2|, |AC9| makes temporary AWS access credentials available to you in the |env|. We call these :dfn:`AWS managed temporary credentials`. This provides the following benefits:

* You don't need to store the permanent AWS access credentials of an AWS entity (for example, an |IAM|
  user) anywhere in the |env|. This prevents those credentials from being accessed by |memslong| without
  your knowledge and approval.
* You don't need to manually set up, manage, or attach an instance profile to the |EC2| instance that
  connects to the |env|. (An instance profile is another approach for managing temporary AWS access credentials.)
* |AC9| continually renews its temporary credentials, so a single set of credentials can only be used for a limited time. This is an AWS security best practice. For more information, see 
  :ref:`auth-and-access-control-temporary-managed-credentials-create-update`.
* |AC9| puts additional restrictions on how its temporary credentials can be used to access AWS actions and resources from the |env|. This is also an AWS security best practice.

Here's how |AC9tempcreds| work whenever an |envec2| tries to access an AWS service on behalf of an AWS entity (for example, an |IAM| user):

#. |AC9| checks to see if the calling AWS entity (for example, the |IAM| user) has permissions in |IAM| to take the requested action for the requested resource in AWS.
   If the permission doesn't exist or is explicitly denied, the request fails.
#. |AC9| checks |AC9tempcreds| to see if its permissions allow the requested action for the requested resource in AWS. If the permission doesn't exist or is explicitly
   denied, the request fails. For a list of permissions that |AC9tempcreds| support, see :ref:`auth-and-access-control-temporary-managed-credentials-supported`.
#. If both the AWS entity and |AC9tempcreds| allow the requested action for the requested resource, the request succeeds.
#. If either the AWS entity or |AC9tempcreds| explicitly deny (or fail to explicitly allow) the requested action for the requested resource, the request fails. This means that
   even if the calling AWS entity has the correct permissions, the request will fail if |AC9| doesn't also explicitly allow it. Likewise, if |AC9| allows a specific
   action to be taken for a specific resource, the request will fail if the AWS entity doesn't also explicitly allow it.

The owner of an |envec2| can turn on or off |AC9tempcreds| for that |env| at any time, as follows:

#. With the |env| open, in the |AC9IDE|, on the menu bar choose :guilabel:`AWS Cloud9, Preferences`.
#. In the :guilabel:`Preferences` tab, in the navigation pane, choose :guilabel:`AWS Settings, Credentials`.
#. Use :guilabel:`AWS managed temporary credentials` to turn |AC9tempcreds| on or off.

If you turn off |AC9tempcreds|, by default the |env| cannot access any AWS services, regardless of the AWS entity who makes the request. If you cannot or do not want to turn
on |AC9tempcreds| for an |env|, but you still need the |env| to access AWS services, consider the following alternatives:

* Attach an instance profile to the |EC2| instance that connects to the |env|. For instructions, see :ref:`credentials-temporary`.
* Store your permanent AWS access credentials in the |env|, for example, by setting special environment variables or by running the :code:`aws configure` command.
  For instructions, see :ref:`credentials-permanent-create`.

The preceding alternatives override all permissions that are allowed (or denied) by |AC9tempcreds| in an |envec2|.

.. _auth-and-access-control-temporary-managed-credentials-supported:

Actions Supported by |AC9tempcredstitle|
----------------------------------------

For an |envfirstec2|, |AC9tempcreds| allow all AWS actions for all AWS resources in the caller's AWS account, with the following restrictions:

* For |IAM|, only the following actions are allowed:

  * :code:`iam:AttachRolePolicy`
  * :code:`iam:ChangePassword`
  * :code:`iam:CreatePolicy`
  * :code:`iam:CreatePolicyVersion`
  * :code:`iam:CreateRole`
  * :code:`iam:CreateServiceLinkedRole`
  * :code:`iam:DeletePolicy`
  * :code:`iam:DeletePolicyVersion`
  * :code:`iam:DeleteRole`
  * :code:`iam:DeleteRolePolicy`
  * :code:`iam:DeleteSSHPublicKey`
  * :code:`iam:DetachRolePolicy`
  * :code:`iam:GetInstanceProfile`
  * :code:`iam:GetPolicy`
  * :code:`iam:GetPolicyVersion`
  * :code:`iam:GetRole`
  * :code:`iam:GetSSHPublicKey`
  * :code:`iam:GetUser`
  * :code:`iam:List*`
  * :code:`iam:PassRole`
  * :code:`iam:PutRolePolicy`
  * :code:`iam:SetDefaultPolicyVersion`
  * :code:`iam:UpdateAssumeRolePolicy`
  * :code:`iam:UpdateRoleDescription`
  * :code:`iam:UpdateSSHPublicKey`
  * :code:`iam:UploadSSHPublicKey`

* All |IAM| actions that interact with roles are allowed only for role names starting with :code:`cloud9-`. However, :code:`iam:PassRole` works with all role names.
* For |STSlong| (|STS|), only the following actions are allowed:

  * :code:`sts:GetCallerIdentity`
  * :code:`sts:DecodeAuthorizationMessage`

* All supported AWS actions are restricted to the IP address of the environment. This is an AWS security best practice.

If |AC9| doesn't support an action or resource that you need an |envec2| to access, or if |AC9tempcreds| is turned off for an |envec2| and you cannot turn it back on, consider the following alternatives:

* Attach an instance profile to the |EC2| instance that connects to the |envec2|. For instructions, see :ref:`credentials-temporary`.
* Store your permanent AWS access credentials in the |envec2|, for example, by setting special environment variables or by running the :code:`aws configure` command.
  For instructions, see :ref:`credentials-permanent-create`.

The preceding alternatives override all permissions that are allowed (or denied) by |AC9tempcreds| in an |envec2|.

.. _auth-and-access-control-temporary-managed-credentials-create-update:

Creating and Updating |AC9tempcredstitle|
-----------------------------------------

For an |envfirstec2|, |AC9tempcreds| are created the first time you open the |env|.

|AC9tempcreds| are updated under any of the following conditions:

* Whenever a certain period of time passes. Currently, this is every 5 minutes.
* Whenever you reload the web browser tab that displays the |IDE| for the |env|.
* When the timestamp that is listed in the :file:`~/.aws/credentials` file for the |env| is reached.
* If the :guilabel:`AWS managed temporary credentials` setting is set to off, whenever you turn it back on. 
  (To view or change this setting, choose :guilabel:`AWS Cloud, Preferences` in the menu bar of the |IDE|. 
  In the :guilabel:`Preferences` tab, in the navigation pane, choose :guilabel:`AWS Settings, Credentials`.)