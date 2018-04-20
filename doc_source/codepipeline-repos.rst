.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _codepipeline-repos:

###############################################
Working with |ACPlong| in the |AC9IDElongtitle|
###############################################

.. meta::
    :description:
        Describes how to use the AWS Cloud9 IDE to work with source code repositories that are used by AWS CodePipeline.

You can use the |AC9IDE| to work with source code in repositories that are compatible with |ACPlong|.

|ACP| is a continuous delivery service you can use to model, visualize, and automate the steps required to release your software and ongoing changes you make to it. 
You can use |ACP| to quickly model and configure the different stages of a software release process. 
For more information, see the :codepipeline-user-guide:`AWS CodePipeline User Guide <welcome.html>`.

.. note:: Completing these procedures might result in charges to your AWS account. These include possible charges for services such as |EC2|, |ACP|, |S3|, and AWS services supported by |ACP|. 
   For more information, see `Amazon EC2 Pricing <https://aws.amazon.com/ec2/pricing/>`_, `AWS CodePipeline Pricing <https://aws.amazon.com/codepipeline/pricing/>`_, 
   `Amazon S3 Pricing <https://aws.amazon.com/s3/pricing/>`_, and `Cloud Services Pricing <https://aws.amazon.com/pricing/services/>`_.

   |ACSlong| provides additional features along with pipelines, such as project templates, dashboards, and teams. 
   To use |ACSlong| instead of |ACP|, skip the rest of this topic, and see :ref:`Working with AWS CodeStar Projects <codestar-projects>` instead.

* :ref:`codepipeline-repos-create-source-code`
* :ref:`codepipeline-repos-connect-to-repo`
* :ref:`codepipeline-repos-setup`
* :ref:`codepipeline-repos-create-pipeline`

.. _codepipeline-repos-create-source-code:

Step 1: Create or Identify Your Source Code Repository
======================================================

In this step, you create or identify a source code repository that is compatible with |ACP|. 

Later in this topic, you upload your software's source code to that 
repository. |ACP| will build, test, and deploy the uploaded source code in that repository by using related pipelines that you also create.

Your source code repository must be one of the following repository types that |ACP| supports:

* **AWS CodeCommit**. If you already have a repository in |ACC| that you want to use, skip ahead to :ref:`codepipeline-repos-connect-to-repo`. Otherwise, to use |ACC|, 
  follow these instructions in the :title:`AWS CodeCommit Sample` in this order, 
  and then return to this topic:

  * :ref:`sample-codecommit-permissions`
  * :ref:`sample-codecommit-create-repo`

* **Amazon S3**. If you already have a bucket in |S3| that you want to use, skip ahead to :ref:`codepipeline-repos-connect-to-repo`. Otherwise, to use |S3|, 
  follow these instructions in the |S3-gsg| in this order, and then return to this topic:

  * :s3-getting-started-guide:`Sign Up for Amazon S3 <SigningUpforS3.html>`
  * :s3-getting-started-guide:`Create a Bucket <CreatingABucket.html>`
  
* **GitHub**. If you already have a repository in GitHub that you want to use, skip ahead to :ref:`codepipeline-repos-connect-to-repo`. Otherwise, to use GitHub, 
  follow these instructions in the :title:`GitHub Sample` in this order, and then return to this topic:

  * :ref:`sample-github-create-account`
  * :ref:`sample-github-create-repo`

.. _codepipeline-repos-connect-to-repo:

Step 2: Create an |envfirsttitle|, Connect It to the Code Repository, and Upload Your Code
==========================================================================================

In this step, you create an |envfirst| in the |AC9| console. You then connect the |env| to the repository that |ACP| will use. Finally, you 
use the |AC9IDE| for the |env| to upload your source code to the repository.

To create the |env|, follow the instructions in :ref:`Creating an Environment <create-environment>`, and then return to this topic. 
(If you already have an |env|, you can use it. You don't need to create a new one.)

To connect the |env| to the repository, and then upload your source code to the repository if it isn't already there, use one of the following sets of instructions. The set you choose 
depends on the type of repository that stores the source code.

.. list-table::
   :widths: 1 5
   :header-rows: 1

   * - **Repository type**
     - **Instructions**
   * - |ACC|
     - Follow these instructions in the :title:`AWS CodeCommit Sample`:

       * :ref:`sample-codecommit-connect-repo` 
       * :ref:`sample-codecommit-clone-repo`
       * :ref:`sample-codecommit-add-files`, substituting your own source code for this step

   * - |S3|
     - 
       * Install and configure the |cli| or aws-shell in the |env|, as described in the :ref:`AWS CLI and aws-shell Sample <sample-aws-cli>`.
       * To upload your source code to the bucket, use the |cli| or the aws-shell in the |env| to run the 
         `aws s3 cp <https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html>`_ command. (For the aws-shell, you can remove :code:`aws` from the command.)

   * - GitHub
     - Follow these instructions in the :title:`GitHub Sample`:

       * :ref:`sample-github-install-git`
       * :ref:`sample-github-clone-repo`
       * :ref:`sample-github-add-files`, substituting your own source code for this step

After you connect the |env| to the repository, whenever you push source code changes from the |AC9IDE| to the repository, |ACP| automatically sends those changes through 
related pipelines to be built, tested, and deployed. You create a related pipeline later in this topic.

.. _codepipeline-repos-setup:

Step 3: Prepare to Work with |ACPlong|
======================================

In this step, you attach a specific AWS managed policy to the |IAM| group you created or identified in :ref:`Team Setup <setup>`. This enables the group's users to begin 
creating and working with pipelines in |ACP|.

If you have used |ACP| before, skip ahead to :ref:`codepipeline-repos-create-pipeline`.

For this step, follow these instructions in 
:codepipeline-user-guide:`Step 3: Use an IAM Managed Policy to Assign AWS CodePipeline Permissions to the IAM User <getting-started-codepipeline.html#assign-permissions>` 
in the |ACP-ug|, and then return to this topic.

.. _codepipeline-repos-create-pipeline:

Step 4: Create a Pipeline in |ACPlong|
======================================

In this step, you create a pipeline in |ACP| that uses the repository you created or identified earlier in this topic.

For this step, follow the instructions in :codepipeline-user-guide:`Create a Pipeline in AWS CodePipeline <pipelines-create.html>` 
in the |ACP-ug|.

After you create the pipeline, |ACP| sends the current version of the source code in the repository through the pipeline to be built, tested, and deployed. Then, whenever you push 
source code changes from the |AC9IDE| to the repository, |ACP| automatically sends those changes through 
the pipeline to be built, tested, and deployed.

To view the pipeline, follow the instructions in :codepipeline-user-guide:`View Pipeline Details and History in AWS CodePipeline <pipelines-view.html>` in the |ACP-ug|.
