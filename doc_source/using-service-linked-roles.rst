.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. |SERVICENAMElong| replace:: |AC9long|
.. |SERVICENAME| replace:: |AC9|
.. |SLR-NAME| replace:: AWSServiceRoleForAWSCloud9
.. |INTRO-ACTION-IN-SERVICE| replace:: create an |AC9| development environment
.. |REMOVE-ACTION-IN-SERVICE| replace:: delete the last remaining |AC9| development environment in your AWS account

.. _using-service-linked-roles:

################################################
Using Service-Linked Roles for |SERVICENAMElong|
################################################

.. meta::
    :description:
        How to use service-linked roles to give AWS Cloud9 access to resources in your AWS account.

|SERVICENAMElong| uses |IAMlong| (|IAM|) :IAM-ug:`service-linked roles <id_roles_terms-and-concepts>`.
A service-linked role is a unique type of |IAM| role that is linked directly to |SERVICENAME|. Service-linked roles are predefined by
|SERVICENAME| and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up |SERVICENAME| easier because you don’t have to manually add the necessary permissions.
|SERVICENAME| defines the permissions of its service-linked roles, and only |SERVICENAME| can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other
|IAM| entity.

You can delete the roles only after first deleting their related resources. This protects
your |SERVICENAME| resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles,
see :IAM-ug:`AWS Services That Work with IAM <reference_aws-services-that-work-with-iam>` and look for the services that have **Yes** in the
**Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

* :ref:`service-linked-role-permissions`
* :ref:`create-service-linked-role`
* :ref:`edit-service-linked-role`
* :ref:`delete-service-linked-role`
* :ref:`slr-regions`

.. _service-linked-role-permissions:

Service-Linked Role Permissions for |SERVICENAME|
=================================================

|SERVICENAME| uses the service-linked role named |SLR-NAME|.
This service-linked role trusts the service :code:`cloud9.amazonaws.com` to assume the role.

The role permissions policy allows |SERVICENAME| to complete the following actions on the
specified resources.

.. code-block:: json

   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Action": [
           "cloudformation:CreateStack",
           "cloudformation:DescribeStacks",
           "ec2:CreateSecurityGroup",
           "ec2:DescribeInstances",
           "ec2:DescribeSecurityGroups",
           "ec2:DescribeVpcs",
           "ec2:RunInstances"
         ],
         "Resource": "*"
       },
       {
         "Effect": "Allow",
         "Action": [
           "ec2:AuthorizeSecurityGroupIngress",
           "ec2:DeleteSecurityGroup",
           "ec2:TerminateInstances"
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
         "Resource": "arn:aws:ec2:*:*:instance/*",
         "Condition": {
           "StringLike": {
             "aws:RequestTag/Name": "aws-cloud9-*"
           }
         }
       },
       {
         "Effect": "Allow",
         "Action": [
           "ec2:StartInstances"
         ],
         "Resource": "*",
         "Condition": {
           "StringLike": {
             "ec2:ResourceTag/aws:cloudformation:stack-name": "aws-cloud9-*"
           }
         }
       }
     ]
   }

You must configure permissions to allow |AC9| 
to create a service-linked role on behalf of an |IAM| entity (such as a user, group, or role).

To allow |AC9|
to create the |SLR-NAME| service-linked role, add the following statement to the
permissions policy for the |IAM| entity on whose behalf |AC9| needs to create the service-linked role.

.. code-block:: json

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

Alternatively, you can add the AWS managed policies :code:`AWSCloud9User` or :code:`AWSCloud9Administrator` to the |IAM| entity.

To allow an |IAM| entity to delete the |SLR-NAME| service-linked role, add the
following statement to the permissions policy for the |IAM| entity that needs to
delete a service-linked role.

.. code-block:: json

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

.. _create-service-linked-role:

Creating a Service-Linked Role for |SERVICENAME|
================================================

You don't need to manually create a service-linked role. When you |INTRO-ACTION-IN-SERVICE|, |SERVICENAME| creates the service-linked role for you.

.. _edit-service-linked-role:

Editing a Service-Linked Role for |SERVICENAME|
===============================================

|SERVICENAME| doesn't allow you to edit the |SLR-NAME| service-linked role. For example, after you
create a service-linked role, you can't change the name of the role because various entities
might reference the role. However, you can edit the description of the role using |IAM|. For 
more information, see :iam-user-guide:`Editing a Service-Linked Role <using-service-linked-roles.html#edit-service-linked-role>` in the |IAM-ug|.

.. _delete-service-linked-role:

Deleting a Service-Linked Role for |SERVICENAME|
================================================

If you no longer need to use a feature or service that requires a service-linked role, we 
recommend that you delete that role. That way you don’t have an unused entity that is not 
actively monitored or maintained.

.. _delete-service-linked-role-service-console:

Deleting a Service-Linked Role in |IAM|
---------------------------------------

Before you can use |IAM| to delete a service-linked role, you must remove any |SERVICENAME| resources used by the role.
To remove |SERVICENAME| resources, see :ref:`Deleting an Environment <delete-environment>`.

You can use the |IAM| console to delete the |SLR-NAME| service-linked 
role. For more information, see :iam-user-guide:`Deleting a Service-Linked Role <using-service-linked-roles.html#delete-service-linked-role>` in the |IAM-ug|.

.. _slr-regions:

Supported Regions for |SERVICENAME| Service-Linked Roles
========================================================

|SERVICENAME| supports using service-linked roles in the following regions.

.. list-table::
   :widths: 2 1 1
   :header-rows: 1

   * - **Region name**
     - **Region identity**
     - **Support in AWS Cloud9**
   * - |region-us-east-1|
     - |region-id-us-east-1|
     - Yes
   * - |region-us-east-2|
     - |region-id-us-east-2|
     - Yes
   * - |region-us-west-1|
     - |region-id-us-west-1|
     - No
   * - |region-us-west-2|
     - |region-id-us-west-2|
     - Yes
   * - |region-ap-south-1|
     - |region-id-ap-south-1|
     - No
   * - |region-ap-northeast-3|
     - |region-id-ap-northeast-3|
     - No
   * - |region-ap-northeast-2|
     - |region-id-ap-northeast-2|
     - No
   * - |region-ap-southeast-1|
     - |region-id-ap-southeast-1|
     - Yes
   * - |region-ap-southeast-2|
     - |region-id-ap-southeast-2|
     - No
   * - |region-ap-northeast-1|
     - |region-id-ap-northeast-1|
     - No
   * - |region-ca-central-1|
     - |region-id-ca-central-1|
     - No
   * - |region-eu-central-1|
     - |region-id-eu-central-1|
     - No
   * - |region-eu-west-1|
     - |region-id-eu-west-1|
     - Yes
   * - |region-eu-west-2|
     - |region-id-eu-west-2|
     - No
   * - |region-eu-west-3|
     - |region-id-eu-west-3|
     - No
   * - |region-sa-east-1|
     - |region-id-sa-east-1|
     - No




