.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _sample-aws-cli:

############################################
|clilong| and aws-shell Sample for |AC9long|
############################################

.. meta::
    :description:
        Provides a hands-on sample that you can use to experiment with the AWS Command Line Interface (AWS CLI) and the aws-shell in AWS Cloud9.

This sample enables you to set up the |clilong| (|cli|), the aws-shell, or both in an |envfirst|. The |cli| and the aws-shell are unified tools that
provide a consistent interface for interacting with all parts of AWS. You can use the |cli| or the aws-shell instead of
the |console| to quickly run commands to interact with AWS, and some of these commands can only be run with the |cli| or the aws-shell.

For more information about the |cli|, see the |cli-ug|_. For the aws-shell, see the following resources:

* `aws-shell <https://github.com/awslabs/aws-shell>`_ on the GitHub website
* `aws-shell <https://pypi.python.org/pypi/aws-shell>`_ on the pip website

For a list of commands you can run with the |cli| to interact with AWS, see the |cli-ref|_. You use the same commands with the aws-shell, except that 
you start commands without the :code:`aws` prefix.

Creating this sample might result in charges to your AWS account. These include possible charges for services such as |EC2| and |S3|. For more information, see
`Amazon EC2 Pricing <https://aws.amazon.com/ec2/pricing/>`_ and `Amazon S3 Pricing <https://aws.amazon.com/s3/pricing/>`_.

* :ref:`sample-aws-cli-prereqs`
* :ref:`sample-aws-cli-install`
* :ref:`sample-aws-cli-creds`
* :ref:`sample-aws-cli-run`
* :ref:`sample-aws-cli-clean-up`

.. _sample-aws-cli-prereqs:

Prerequisites
=============

.. include:: _sample-prereqs.txt

.. _sample-aws-cli-install:

Step 1: Install the |cli|, the aws-shell, or Both in Your |envtitle|
====================================================================

In this step, you use the |AC9IDE| to install the |cli|, the aws-shell, or both in your |env| so you can run commands to interact with AWS.

If you are using an |envfirstec2| and you only want to use the |cli|, you can skip ahead to :ref:`sample-aws-cli-run`. This is because the |cli| is already installed in an |envec2|, and a set of AWS access credentials is already set up in the |env|.
For more information, see :ref:`auth-and-access-control-temporary-managed-credentials`.

If you are not using an |envec2|, do the following to install the |cli|:

#. With your |env| open, in the |IDE|, check whether the |cli| is already installed. In the terminal, run the :command:`aws --version` command. (To start a new terminal session, on the
   menu bar, choose :menuselection:`Window, New Terminal`.) If the |cli| is installed, the version number
   is displayed, with information such as the version numbers of Python and the operating system version number of your |EC2| instance or your own server. For example,
   :samp:`aws-cli {N.NN.NN} Python/{N.N.NN} {OS/VERSION}`. If the |cli| is installed, skip ahead to :ref:`sample-aws-cli-creds`.
#. To install the |cli|, see :cli-ug:`Installing the AWS Command Line Interface <installing>` in the |cli-ug|. For example, for an |envec2| running Amazon Linux,
   run these three commands, one at a time, in the terminal to install the |cli|.

   .. code-block:: sh

      sudo yum -y update          # Install the latest system updates.
      sudo yum -y install aws-cli # Install the AWS CLI.
      aws --version               # Confirm the AWS CLI was installed.

Do the following to install the aws-shell:

#. With your |env| open, in the |IDE|, check whether the aws-shell is already installed. In the terminal, run the :command:`aws-shell --version` command. (To start a new terminal session, on the
   menu bar, choose :menuselection:`Window, New Terminal`.) If the aws-shell is installed, the :code:`aws>` prompt is displayed. If the aws-shell is installed, skip ahead to :ref:`sample-aws-cli-creds`.
#. To install the aws-shell, you use pip. To use pip, you must have Python installed. 

   To check whether Python is already installed (and to install it if needed), follow the instructions in :ref:`sample-python-install` in the *Python Sample*, and then return to this topic.
   
   To check whether pip is already installed, in the terminal, run the :command:`pip --version` command. If pip is installed, the version number is displayed. If pip is 
   not installed, install it. For example, for an |envec2| running Amazon Linux, run these three commands, one at a time, in the terminal to install pip.

   .. code-block:: sh

      wget https://bootstrap.pypa.io/get-pip.py # Get the pip install file.
      sudo python get-pip.py                    # Install pip. (May need to run 'sudo python2 get-pip.py' or 'sudo python3 get-pip.py' instead, depending on how Python is installed.)
      rm get-pip.py                             # Delete the pip install file, as it is no longer needed.

#. To use pip to install the aws-shell, run the following command.

   .. code-block:: sh

      sudo pip install aws-shell

#. If the aws-shell is already installed, to upgrade to the latest version, run the following command.

   .. code-block:: sh

      sudo pip install --upgrade aws-shell

.. _sample-aws-cli-creds:

Step 2: Set up Credentials Management in Your |envtitle|
========================================================

Each time you use the |cli| or the aws-shell to call an AWS service, you must provide a set of credentials with the call. These credentials determine whether the |cli| or the aws-shell has the appropriate permissions to make that call. If the
credentials don't cover the appropriate permissions, the call will fail.

If you are using an |envfirstec2|, you can skip ahead to :ref:`sample-aws-cli-run`. This is because credentials are already set up in an |envec2|. For more information, see :ref:`auth-and-access-control-temporary-managed-credentials`.

If you are not using an |envec2|, you must manually store your credentials within the |env|. To do this, follow the instructions in :doc:`credentials`, and then return to this topic.

.. _sample-aws-cli-run:

Step 3: Run Some Basic Commands with the |cli| or the aws-shell in Your |envtitle|
==================================================================================

In this step, you use the |cli| or the aws-shell in your |env| to create a bucket in |S3|, list your available buckets, and then delete the bucket.

#. If you want to use the aws-shell but haven't started it yet, start the aws-shell by running the :code:`aws-shell` command. The :code:`aws>` prompt is displayed.
#. Create a bucket. Run the :command:`aws s3 mb` command with the |cli| or :command:`s3 mb` command with the aws-shell, supplying the name of the bucket to create. In this example, we use a bucket named
   :samp:`s3://cloud9-{ACCOUNT-ID}-bucket`, where :samp:`{ACCOUNT-ID}` is your AWS account ID. If you use a different name, substitute it throughout this step.

   .. code-block:: sh

      aws s3 mb s3://cloud9-ACCOUNT-ID-bucket # For the AWS CLI.
      s3 mb s3://cloud9-ACCOUNT-ID-bucket     # For the aws-shell.

   .. note:: Bucket names must be unique across all of AWS, not just your AWS account. The preceding
      suggested bucket name can help you come up with a unique bucket name.
      If you get a message that contains the error :code:`BucketAlreadyExists`, you must run the command again with a different bucket name.

#. List your available buckets. Run the :command:`aws s3 ls` command with the |cli| or the :command:`s3 ls` command with the aws-shell. A list of your available buckets is displayed.
#. Delete the bucket. Run the :command:`aws s3 rb` command with the |cli| or the :command:`s3 rb` command with the aws-shell, supplying the name of the bucket to delete.

   .. code-block:: sh

      aws s3 rb s3://cloud9-ACCOUNT-ID-bucket # For the AWS CLI.
      s3 rb s3://cloud9-ACCOUNT-ID-bucket     # For the aws-shell.

   To confirm whether the bucket was deleted, run the :command:`aws s3 ls` command again with the |cli| or the :command:`s3 ls` command again with the aws-shell. The name of 
   the bucket that was deleted should no longer appear in the list.

   .. note:: You don't have to delete the bucket if you want to keep using it. For more information,
      see :S3-gsg:`Add an Object to a Bucket <PuttingAnObjectInABucket>` in the |S3-gsg|.
      See also :cli-ref:`s3 commands <s3/rm.html>` in the |cli-ref|. (Remember, if you don't delete the
      bucket, it might result in ongoing charges to your AWS account.)

To continue experimenting with the |cli|, see :cli-ug:`Working with Amazon Web Services <chap-working-with-services>` in the |cli-ug| as well as the 
|cli-ref|_. To continue experimenting with the aws-shell, see the |cli-ref|_, noting that you start commands without the :code:`aws` prefix.

.. _sample-aws-cli-clean-up:

Step 4: Clean Up
================

If you're using the aws-shell, you can stop using it by running the :command:`.exit` or :command:`.quit` command.

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the |env|.
For instructions, see :doc:`Deleting an Environment <delete-environment>`.







