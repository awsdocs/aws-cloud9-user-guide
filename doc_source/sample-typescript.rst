.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _sample-typescript:

###############################
TypeScript Sample for |AC9long|
###############################

.. meta::
    :description:
        Provides a hands-on sample that you can use to experiment with TypeScript in AWS Cloud9.

This sample shows you how to work with TypeScript in an |envfirst|.

Creating this sample might result in charges to your AWS account. These include possible charges for services such as |EC2| and |S3|. For more information, see
`Amazon EC2 Pricing <https://aws.amazon.com/ec2/pricing/>`_ and `Amazon S3 Pricing <https://aws.amazon.com/s3/pricing/>`_.

* :ref:`sample-typescript-prereqs`
* :ref:`sample-typescript-install`
* :ref:`sample-typescript-code`
* :ref:`sample-typescript-run`
* :ref:`sample-typescript-sdk`
* :ref:`sample-typescript-sdk-code`
* :ref:`sample-typescript-sdk-run`
* :ref:`sample-typescript-clean-up`

.. _sample-typescript-prereqs:

Prerequisites
=============

.. include:: _sample-prereqs.txt

.. _sample-typescript-install:

Step 1: Install Required Tools
==============================

In this step, you install TypeScript by using Node Package Manager (:command:`npm`).
To install :command:`npm`, you use Node Version Manager (:command:`nvm`). If you don't have :command:`nvm`, you install it in this step first.

#. In a terminal session in the |AC9IDE|, confirm whether TypeScript is already installed by running the command line TypeScript
   compiler with the :command:`--version` option. (To start a new terminal session,
   on the menu bar, choose :menuselection:`Window, New Terminal`.) If successful, the output contains the TypeScript version number.
   If TypeScript is installed, skip ahead to :ref:`sample-typescript-code`.

   .. code-block:: sh

      tsc --version

#. Confirm whether :command:`npm` is already installed by running :command:`npm` with the :command:`--version` option. If successful, the output contains
   the :command:`npm` version number. If :command:`npm` is installed, skip ahead to step 10 in this procedure to use :command:`npm` to install TypeScript.

   .. code-block:: sh

      npm --version

#. Run :code:`yum` to help ensure the latest security updates and bug fixes are installed.

   .. code-block:: sh

      sudo yum -y update

#. To install :command:`npm`, begin by running the following command to download Node Version Manager (:command:`nvm`). (:command:`nvm` is a simple
   Bash shell script that's useful for installing and managing Node.js versions. For more information, see
   `Node Version Manager <https://github.com/creationix/nvm/blob/master/README.md>`_ on the GitHub website.)

   .. code-block:: sh

      curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash

#. To start using :command:`nvm`, either close the terminal session and start it again, or source the :file:`~/.bashrc` file that contains the commands to load :command:`nvm`.

   .. code-block:: sh

      . ~/.bashrc

#. Confirm that :command:`nvm` is installed by running :command:`nvm` with the :command:`--version` option.

   .. code-block:: sh

      nvm --version

#. Install the latest version of Node.js by running :command:`nvm`. (:command:`npm` is included in Node.js.)

   .. code-block:: sh

      nvm install node

#. Confirm that Node.js is installed by running the command line version of Node.js with the :command:`--version` option.

   .. code-block:: sh

      node --version

#. Confirm that :command:`npm` is installed by running :command:`npm` with the :command:`--version` option.

   .. code-block:: sh

      npm --version

#. Install TypeScript by running :command:`npm` with the :command:`-g` option. This installs TypeScript as a
   global package in the |env|.

   .. code-block:: sh

      npm install -g typescript

#. Confirm that TypeScript is installed by running the command line TypeScript
   compiler with the :command:`--version` option.

   .. code-block:: sh

      tsc --version

.. _sample-typescript-code:

Step 2: Add Code
================

In the |AC9IDE|, create a file with the following content, and save the file with the name :file:`hello.ts`.
(To create a file, on the menu bar, choose :menuselection:`File, New File`. To save the file, choose :menuselection:`File, Save`.)

.. code-block:: typescript

   console.log('Hello, World!');

   console.log('The sum of 2 and 3 is 5.');

   const sum: number = parseInt(process.argv[2], 10) + parseInt(process.argv[3], 10);

   console.log('The sum of ' + process.argv[2] + ' and ' +
     process.argv[3] + ' is ' + sum + '.');

.. _sample-typescript-run:

Step 3: Run the Code
====================

#. In a terminal in the |IDE|, from the same directory as the :file:`hello.ts` file, run :command:`npm` to install the
   :code:`@types/node` library.

   .. code-block:: sh

      npm install @types/node

   This adds a
   :file:`node_modules/@types/node` folder in the same directory as the :file:`hello.ts` file. This new folder
   contains Node.js type definitions (for example, ones for the :code:`console.log` and :code:`process.argv`
   properties in the :file:`hello.ts` file) that TypeScript needs later in this procedure.

#. In the terminal, from the same directory as the :file:`hello.ts` file, run the TypeScript compiler. Specify the
   :file:`hello.ts` file and additional libraries to include.

   .. code-block:: sh

      tsc hello.ts --lib es6

   TypeScript uses the :file:`hello.ts` file and
   a set of ECMAScript 6 (ES6) library files to transpile the TypeScript code in the
   :file:`hello.ts` file into equivalent JavaScript code in a file named :file:`hello.js`.

#. In the :guilabel:`Environment` window, open the :file:`hello.js` file.
#. On the menu bar, choose :menuselection:`Run, Run Configurations, New Run Configuration`.
#. On the :guilabel:`[New] - Idle` tab, choose :guilabel:`Runner: Auto`, and then choose :guilabel:`Node.js`.
#. For :guilabel:`Command`, type :kbd:`hello.js 5 9`. In the code, :code:`5` represents :code:`process.argv[2]`,
   and :code:`9` represents :code:`process.argv[3]`. (:code:`process.argv[0]` represents the name of the runtime (:code:`node`), and :code:`process.argv[1]` represents the name
   of the file (:file:`hello.js`).)
#. Choose :guilabel:`Run`, and compare your output. When you're done, choose :guilabel:`Stop`.

   .. code-block:: text

      Hello, World!
      The sum of 2 and 3 is 5.
      The sum of 5 and 9 is 14.

.. image:: images/ide-nodejs-simple.png
   :width: 100%
   :alt: Node.js output after running the code in the AWS Cloud9 IDE

.. note:: Instead of creating a new run configuration in the |IDE|, you can also execute this code by running the command
   :command:`node hello.js 5 9` from the terminal.

.. _sample-typescript-sdk:

Step 4: Install and Configure the |sdk-nodejs|
==============================================

You can enhance this sample to use the |sdk-nodejs| to create an |s3| bucket, list your available buckets, and then delete the bucket you just created.

In this step, you install and configure the |sdk-nodejs|. The SDK provides a convenient way to interact with AWS services such as |s3|, from your JavaScript code.
After you install the |sdk-nodejs|, you must set up credentials management in your |env|. The SDK needs these credentials to interact with AWS services.

.. topic:: To install the |sdk-nodejs|

   In a terminal session in the |AC9IDE|, from the same directory as the :file:`hello.js` file from :ref:`sample-typescript-run`,
   run :command:`npm` to install the |sdk-nodejs|.

   .. code-block:: sh

      npm install aws-sdk

   This command adds several folders to the :file:`node_modules` folder from :ref:`sample-typescript-run`. These folders contain source code and
   dependencies for the |sdk-nodejs|.
   For more information, see :sdk-for-javascript-dev-guide-v2:`Installing the SDK for JavaScript <installing-jssdk.html>` in the
   |sdk-js-dg|.

.. topic:: To set up credentials management in your |env|

   Each time you use the |sdk-nodejs| to call an AWS service, you must provide a set of credentials with the call. These credentials determine whether the |sdk-nodejs| has the appropriate permissions to make that call. If the
   credentials don't cover the appropriate permissions, the call will fail.

   In this step, you store your credentials within the |env|. To do this, follow the instructions in :ref:`Call AWS Services from an Environment <credentials>`, and then return to this topic.

   For additional information, see :sdk-for-javascript-dev-guide-v2:`Setting Credentials in Node.js <setting-credentials-node.html>` in the
   |sdk-js-dg|.

.. _sample-typescript-sdk-code:

Step 5: Add AWS SDK Code
========================

In this step, you add some more code, this time to interact with |s3| to create a bucket, list your available buckets, and then delete the bucket you just created. You'll
run this code later.

In the |AC9IDE|, in the same directory as the :file:`hello.js` file in previous steps, create a file with the following content,
and save the file with the name :file:`s3.ts`.

.. code-block:: javascript

   import { } from 'async';

   if (process.argv.length < 4) {
     console.log('Usage: node s3.js <the bucket name> <the AWS Region to use>\n' +
       'Example: node s3.js my-test-bucket us-east-2');
     process.exit(1);
   }

   const AWS = require('aws-sdk'); // To set the AWS credentials and AWS Region.
   const async = require('async'); // To call AWS operations asynchronously.

   const s3 = new AWS.S3({apiVersion: '2006-03-01'});
   const bucket_name = process.argv[2];
   const region = process.argv[3];

   AWS.config.update({
     region: region
   });

   const create_bucket_params = {
     Bucket: bucket_name,
     CreateBucketConfiguration: {
       LocationConstraint: region
     }
   };

   const delete_bucket_params = {Bucket: bucket_name};

   // List all of your available buckets in this AWS Region.
   function listMyBuckets(callback) {
     s3.listBuckets(function(err, data) {
       if (err) {

       } else {
         console.log("My buckets now are:\n");

         for (let i = 0; i < data.Buckets.length; i++) {
           console.log(data.Buckets[i].Name);
         }
       }

       callback(err);
     });
   }

   // Create a bucket in this AWS Region.
   function createMyBucket(callback) {
     console.log('\nCreating a bucket named ' + bucket_name + '...\n');

     s3.createBucket(create_bucket_params, function(err, data) {
       if (err) {
         console.log(err.code + ": " + err.message);
       }

       callback(err);
     });
   }

   // Delete the bucket you just created.
   function deleteMyBucket(callback) {
     console.log('\nDeleting the bucket named ' + bucket_name + '...\n');

     s3.deleteBucket(delete_bucket_params, function(err, data) {
       if (err) {
         console.log(err.code + ": " + err.message);
       }

       callback(err);
     });
   }

   // Call the AWS operations in the following order.
   async.series([
     listMyBuckets,
     createMyBucket,
     listMyBuckets,
     deleteMyBucket,
     listMyBuckets
   ]);

.. _sample-typescript-sdk-run:

Step 6: Run the AWS SDK Code
============================

#. From a terminal in the |AC9IDE|, in the same directory as the :file:`s3.ts` file from :ref:`sample-typescript-sdk-code`,
   enable the code to call |S3| operations asynchronously by running :command:`npm` to install the async library.

   .. code-block:: sh

      npm install async

#. In the terminal, from the same directory as the :file:`s3.ts` file, run the TypeScript compiler. Specify the
   :file:`s3.ts` file and additional libraries to include.

   .. code-block:: sh

      tsc s3.ts --lib es6

   TypeScript uses the :file:`s3.ts` file, the |sdk-nodejs|, the async library, and
   a set of ECMAScript 6 (ES6) library files to transpile the TypeScript code in the
   :file:`s3.ts` file into equivalent JavaScript code in a file named :file:`s3.js`.

#. In the :guilabel:`Environment` window, open the :file:`s3.js` file.
#. On the menu bar, choose :menuselection:`Run, Run Configurations, New Run Configuration`.
#. On the :guilabel:`[New] - Idle` tab, choose :guilabel:`Runner: Auto`, and then choose :guilabel:`Node.js`.
#. For :guilabel:`Command`, type :samp:`s3.js {YOUR_BUCKET_NAME} {THE_AWS_REGION}`, where :samp:`{YOUR_BUCKET_NAME}` is the name of the bucket you want to create
   and then delete, and :samp:`{THE_AWS_REGION}` is the ID of the AWS Region to create the bucket in. For example, for the US East (Ohio) Region,
   use :code:`us-east-2`. For more IDs, see :aws-gen-ref:`Amazon Simple Storage Service (Amazon S3) <rande.html#s3_region>` in the |AWS-gr|.

   .. note:: |S3| bucket names must be unique across AWS |mdash| not just your AWS account.

#. Choose :guilabel:`Run`, and compare your output. When you're done, choose :guilabel:`Stop`.

   .. code-block:: text

      My buckets now are:

      Creating a new bucket named 'my-test-bucket'...

      My buckets now are:

      my-test-bucket

      Deleting the bucket named 'my-test-bucket'...

      My buckets now are:

.. _sample-typescript-clean-up:

Step 7: Clean Up
================

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the |env|.
For instructions, see :doc:`Deleting an Environment <delete-environment>`.
