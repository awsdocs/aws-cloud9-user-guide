.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _sample-python:

###########################
Python Sample for |AC9long|
###########################

.. meta::
    :description:
        Provides a hands-on sample that you can use to experiment with Python in AWS Cloud9.

This sample enables you to run some Python scripts in an |envfirst|.

* :ref:`sample-python-install`
* :ref:`sample-python-code`
* :ref:`sample-python-run`
* :ref:`sample-python-sdk`
* :ref:`sample-python-sdk-code`
* :ref:`sample-python-sdk-run`
* :ref:`sample-python-clean-up`

.. note::

   .. include:: _sample-prereqs.txt

   Creating this sample might result in charges to your AWS account. These include possible charges for services such as |EC2| and |S3|. For more information, see
   `Amazon EC2 Pricing <https://aws.amazon.com/ec2/pricing/>`_ and `Amazon S3 Pricing <https://aws.amazon.com/s3/pricing/>`_.

.. _sample-python-install:

Step 1: Install Required Tools
==============================

In this step, you install Python, which is required to run this sample.

#. In a terminal session in the |AC9IDE|, confirm whether Python is already installed by running the :command:`python --version` command. (To start a new terminal session,
   on the menu bar, choose :menuselection:`Window, New Terminal`.) If successful, the output contains
   the Python version number. If Python is installed, skip ahead to :ref:`sample-python-code`.
#. Run the :command:`yum update` command to help ensure the latest security updates and bug fixes are installed.

   .. code-block:: sh

      sudo yum -y update

#. Install Python by running one or more of these :command:`install` commands.

   .. code-block:: sh

      sudo yum -y install python27 # Installs Python 2.7.
      sudo yum -y install python36 # Installs Python 3.6.

   .. note:: If you have Python 2 and 3 installed, and you want to use Python 3 but running the :command:`python --version` command outputs a version of Python 2, you can
      use Python 3 in one or more of the following ways: 

      * Instead of running  

   For more information, see `Download Python <https://www.python.org/downloads/>`_ on the Python website and `Installing Packages <https://packaging.python.org/installing/>`_
   in the :title:`Python Packaging User Guide`.

.. _sample-python-code:

Step 2: Add Code
================

In the |AC9IDE|, create a file with this content, and save the file with the name :file:`hello.py`.
(To create a file, on the menu bar, choose :menuselection:`File, New File`. To save the file, choose :menuselection:`File, Save`.)

.. code-block:: python

   import sys

   print('Hello, World!')

   print('The sum of 2 and 3 is 5.')

   sum = int(sys.argv[1]) + int(sys.argv[2])

   print('The sum of {0} and {1} is {2}.'.format(sys.argv[1], sys.argv[2], sum))

.. note:: The preceding code doesn't rely on any custom Python modules or packages. However, if you ever import custom 
   Python modules or packages, and you want |AC9| to use 
   those modules or pacakges to do code completion as you type, 
   turn on the :guilabel:`Project, Python Support, Enable Python code completion` setting in :guilabel:`Preferences`, 
   and then add the paths to those modules or packages to the :guilabel:`Project, Python Support, PYTHONPATH` setting. 
   (To view and change your preferences, choose :guilabel:`AWS Cloud9, Preferences` on the menu bar.)

.. _sample-python-run:

Step 3: Run the Code
====================

#. In the |AC9IDE|, on the menu bar, choose :menuselection:`Run, Run Configurations, New Run Configuration`.
#. On the :guilabel:`[New] - Idle` tab, choose :guilabel:`Runner: Auto`, and then choose :guilabel:`Python 2` or :guilabel:`Python 3`, depending 
   on which version of Python you want to use.

   .. note:: If :guilabel:`Python 2` or :guilabel:`Python 3` isn't available, you can create a custom runner for the version of Python that is installed in 
      your |env|.

      #. On the :guilabel:`[New] - Idle` tab, choose :guilabel:`Runner: Auto`, and then choose :guilabel:`New Runner`.
      #. On the :guilabel:`My Runner.run` tab, replace the tab's contents with this code.

         .. code-block:: json

            {
              "cmd" : ["python", "$file", "$args"],
              "info" : "Running $project_path$file_name...",
              "selector" : "source.py"
            }

      #. Choose :menuselection:`File, Save As` on the menu bar, and save the file as :file:`Python.run` in the :file:`/.c9/runners` folder.
      #. On the :guilabel:`[New] - Idle` tab, choose :guilabel:`Runner: Auto`, and then choose :guilabel:`Python`.
      #. Choose the :guilabel:`hello.py` tab to make it active.

      To use a specific version of Python that is installed in your |env|, change :code:`python` to the path to the Python executable in the preceding custom runner 
      definition (for example, :code:`/usr/bin/python27`, :code:`/usr/bin/python36`, or similar).

#. For :guilabel:`Command`, type :kbd:`hello.py 5 9`. In the code, :code:`5` represents :code:`sys.argv[1]`,
   and :code:`9` represents :code:`sys.argv[2]`.
#. Choose the :guilabel:`Run` button, and compare your output.

   .. code-block:: text

      Hello, World!
      The sum of 2 and 3 is 5.
      The sum of 5 and 9 is 14.

.. _sample-python-sdk:

Step 4: Install and Configure the |sdk-python|
==================================================

You can enhance this sample to use the |sdk-python| to create an |s3| bucket, list your available buckets, and then delete the bucket you just created.

In this step, you install and configure the |sdk-python|, which provides a convenient way to interact with AWS services, such as |s3|, from your Python code. Before you can install the
|sdk-python|, you must install pip. After you install the |sdk-python|, you must set up credentials management in your |env|. The
|sdk-python| needs these credentials to interact with AWS services.

.. topic:: To install pip

   #. In the |AC9IDE|, confirm whether pip is already installed by running the :command:`pip --version` command. If successful, the
      output contains the pip version number. Otherwise, an error message should be output. If pip is
      installed, skip ahead to the next procedure, **To install the |sdk-python|**.
   #. To install pip, run these commands, one at a time.

      .. code-block:: sh

         curl -O https://bootstrap.pypa.io/get-pip.py # Get the install script.
         sudo python get-pip.py                       # Install pip.
         rm get-pip.py                                # Delete the install script.

      For more information, see `pip Installation <https://pip.pypa.io/en/stable/installing/>`_ on the pip website.

.. topic:: To install the |sdk-python|

   After you install pip, use Python to run the :command:`pip install` command.

   .. code-block:: sh

      sudo python -m pip install boto3

   For more information, see the "Installation" section of :sdk-python-dg:`Quickstart <quickstart>` in the |sdk-python-dg|.

.. topic:: To set up credentials management in your |env|

   Each time you use the |sdk-python| to call an AWS service, you must provide a set of credentials with the call. These credentials determine whether the |sdk-python| has the appropriate permissions to make that call. If the
   credentials don't cover the appropriate permissions, the call will fail.

   In this step, you store your credentials within the |env|. To do this, follow the instructions in :ref:`Call AWS Services from an Environment <credentials>`, and then return to this topic.

   For additional information, see :sdk-python-dg:`Credentials <configuration>` in the |sdk-python-dg|.

.. _sample-python-sdk-code:

Step 5: Add AWS SDK Code
========================

In this step, you add some more code, this time to interact with |s3| to create a bucket, list your available buckets, and then delete the bucket you just created. You
will run this code later.

In the |AC9IDE|, create a file with this content, and save the file with the name :file:`s3.py`.

.. code-block:: python

   import boto3
   import sys
   import botocore

   region = 'YOUR_REGION'
   s3 = boto3.client(
     's3',
     region_name = region
   )

   bucket_name = sys.argv[1]

   # Lists all of your available buckets in this AWS Region.
   def list_my_buckets(s3):
     resp = s3.list_buckets()

     print('My buckets now are:\n')

     for bucket in resp['Buckets']:
       print(bucket['Name'])

     return

   list_my_buckets(s3)

   # Create a new bucket.
   try:
     print("\nCreating a new bucket named '" + bucket_name + "'...\n")
     s3.create_bucket(Bucket = bucket_name,
       CreateBucketConfiguration = {
         'LocationConstraint': region
       }
     )
   except botocore.exceptions.ClientError as e:
     if e.response['Error']['Code'] == 'BucketAlreadyExists':
       print("Cannot create the bucket. A bucket with the name '" +
         bucket_name + "' already exists. Exiting.")
     sys.exit()

   list_my_buckets(s3)

   # Delete the bucket you just created.
   print("\nDeleting the bucket named '" + bucket_name + "'...\n")
   s3.delete_bucket(Bucket = bucket_name)

   list_my_buckets(s3)

In the preceding code, replace :samp:`YOUR_REGION` with the ID of an AWS Region. For example, for the US East (Ohio) Region, use :code:`us-east-2`.
For more IDs, see :aws-gen-ref:`Amazon Simple Storage Service (Amazon S3) <rande.html#s3_region>` in the |AWS-gr|.

.. _sample-python-sdk-run:

Step 6: Run the AWS SDK Code
============================

#. On the menu bar, choose :menuselection:`Run, Run Configurations, New Run Configuration`.
#. On the :guilabel:`[New] - Idle` tab, choose :guilabel:`Runner: Auto`, and then choose :guilabel:`Python 2` or :guilabel:`Python 3`, depending 
   on which version of Python you want to use and is installed in your |env|.
#. For :guilabel:`Command`, type :samp:`s3.py {YOUR_BUCKET_NAME}`, where :samp:`{YOUR_BUCKET_NAME}` is the name of the bucket you want to create and then delete.

   .. note:: |S3| bucket names must be unique across AWS |mdash| not just your AWS account.

#. Choose the :guilabel:`Run` button, and compare your output.

   .. code-block:: text

      My buckets now are:

      Creating a new bucket named 'my-test-bucket'...

      My buckets now are:

      my-test-bucket

      Deleting the bucket named 'my-test-bucket'...

      My buckets now are:

.. _sample-python-clean-up:

Step 7: Clean Up
================

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the |env|.
For instructions, see :doc:`Deleting an Environment <delete-environment>`.
