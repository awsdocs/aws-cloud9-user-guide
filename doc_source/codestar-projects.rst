.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _codestar-projects:

########################################################
Working with |ACSlong| Projects in the |AC9IDElongtitle|
########################################################

.. meta::
    :description:
        Describes how to work with AWS CodeStar projects in the AWS Cloud9 IDE.

You can use the |AC9IDE| to work with code in |ACSlong| projects.

|ACSlong| is a cloud-based service for creating, managing, and working with software development projects on AWS.
You can quickly develop, build, and deploy applications on AWS with an |ACSlong| project. An |ACSlong| project creates and integrates AWS services for your project development toolchain.
Depending on your choice of |ACSlong| project template, that toolchain might include source control, build, deployment, virtual servers or serverless resources, and more.
For more information, see the :codestar-user-guide:`AWS CodeStar User Guide <welcome.html>`.

.. note:: Completing these procedures might result in charges to your AWS account. These include possible charges for services such as |EC2|, |ACSlong|, and AWS services supported by |ACSlong|. For more information, see
   `Amazon EC2 Pricing <https://aws.amazon.com/ec2/pricing/>`_, `AWS CodeStar Pricing <https://aws.amazon.com/codestar/pricing/>`_, and `Cloud Services Pricing <https://aws.amazon.com/pricing/services/>`_.

   To use the |AC9IDE| to work with a newly-launched |EC2| instance preconfigured with a popular app or framework such as WordPress, MySQL, PHP, Node.js, Nginx, Drupal, or Joomla, or a Linux distribution such as 
   Ubuntu, Debian, FreeBSD, or openSUSE, you can use |lightsaillong| along with |AC9|. To do this, skip the rest of this topic, and see :ref:`Working with Amazon Lightsail Instances <lightsail-instances>` instead. 

   To use the |AC9IDE| to work with a newly-launched |EC2| instance running Amazon Linux that contains no sample code, skip the rest of this topic, and see the :ref:`IDE Tutorial <tutorial>` instead.

* :ref:`codestar-projects-setup`
* :ref:`codestar-projects-create-project`
* :ref:`codestar-projects-connect-to-project`

.. _codestar-projects-setup:

Step 1: Prepare to Work with |ACSlong| Projects
===============================================

In this step, you create an |ACSlong| service role and an |EC2| key pair, so that you can begin creating and working with |ACSlong| projects.

If you have used |ACSlong| before, skip ahead to :ref:`codestar-projects-create-project`.

For this step, follow the instructions in
:codestar-user-guide:`Setting Up AWS CodeStar <setting-up.html>` 
in the :title:`AWS CodeStar User Guide`. Do not create a new AWS account, |IAM| user, or |IAM| group as part of those instructions.
Use the ones you created or identified in :doc:`setup`. When you finish following those instructions, return to this topic.

.. _codestar-projects-create-project:

Step 2: Create a Project in |ACSlong|
=====================================

In this step, you create a project in |ACSlong|.

If you already have a project in |ACSlong| you want to use, skip ahead to :ref:`codestar-projects-connect-to-project`.

For this step, follow the instructions in
:codestar-user-guide:`Create a Project in AWS CodeStar <how-to-create-project.html>` 
in the :title:`AWS CodeStar User Guide`. In the |ACSlong| create project wizard, when you get to the :guilabel:`Set
up tools` page or :guilabel:`Connect to your source repository` page,
choose :guilabel:`Skip`, and then return to this topic.

.. _codestar-projects-connect-to-project:

Step 3: Create an |envfirsttitle| and Connect It to the Project
===============================================================

In this step, you create an |envfirst| in the |ACSlong| or |AC9| consoles. You then connect the new |env| to an |ACSlong| project.

For this step, follow one of the following sets of instructions, depending on the |envfirst| type you
want to use and the type of repository where the |ACSlong| project stores its code.

.. list-table::
   :widths: 1 1 3
   :header-rows: 1

   * - **Environment type**
     - **Repository type**
     - **Instructions**
   * - |envec2|
     - |ACC|
     - :codestar-user-guide:`Create an AWS Cloud9 Environment for a Project <setting-up-ide-cloud9.html#setting-up-ide-cloud9-create>` in the :title:`AWS CodeStar User Guide`
   * - |envssh|
     - |ACC|
     - :ref:`AWS CodeCommit Sample <sample-codecommit>`
   * - EC2 or |envssh|
     - GitHub
     - :codestar-user-guide:`Use GitHub with AWS Cloud9 <setting-up-ide-cloud9.html#setting-up-ide-cloud9-github>` in the :title:`AWS CodeStar User Guide`
