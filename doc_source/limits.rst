.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _limits:

################
Limits for |AC9|
################

.. meta::
    :description:
        Lists the limits for AWS Cloud9 and related AWS services.
        
The following tables list limits in |AC9| and related AWS services.

* :ref:`limits-core`
* :ref:`limits-related`

.. _limits-core:

|AC9| Limits
============

.. list-table::
   :widths: 1 2

   * - Maximum number of |envfirstec2plural|
     - * 20 per user per AWS Region
       * 200 per AWS account per Region
   * - Maximum number of |envsshplural|
     - * 10 per user per Region
       * 100 per AWS account per Region
   * - Maximum number of |mems| in an |env|
     - 8 per user per Region
   * - Maximum editable file size
     - 8 MB

.. _limits-related:

Related AWS Service Limits
==========================

.. list-table::
   :widths: 1 2

   * - Maximum number of |EBSlong| (|EBS|) volumes
     - 5,000

       For more information, see :aws-gen-ref:`Amazon Elastic Block Store (Amazon EBS) Limits <aws_service_limits.html#limits_ebs>` in the |AWS-gr|.
   * - Maximum number of |CFN| stacks
     - 200

       For more information, see :CFN-ug:`AWS CloudFormation Limits <cloudformation-limits>` in the |CFN-ug|.
   * - |EC2| limits
     - See :aws-gen-ref:`Amazon Elastic Compute Cloud (Amazon EC2) Limits <aws_service_limits.html#limits_ec2>` in the |AWS-gr|.