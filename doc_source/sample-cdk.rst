.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _sample-cdk:

############################
AWS CDK Sample for |AC9long|
############################

.. meta::
    :description:
        Provides a hands-on sample that you can use to experiment with the AWS Cloud Development Kit (AWS CDK) in AWS Cloud9.

This sample shows you how to work with the AWS Cloud Development Kit (AWS CDK) in an |envfirst|. The AWS CDK is a set of 
software tools and libraries that developers can use to model AWS infrastructure components as code.

The AWS CDK includes the 
AWS Construct Library that you can use to quickly resolve many tasks on AWS. For example, you can use the :code:`Fleet` construct to 
fully and securely deploy code to a fleet of hosts. You can create your own constructs to model various elements of your architectures, 
share them with others, or publish them to the community. For more information, see the `AWS Cloud Development Kit User Guide <https://awslabs.github.io/aws-cdk/>`_.

*The AWS CDK is currently in developer preview and we look forward to community feedback and collaboration!*

Creating this sample might result in charges to your AWS account. These include possible charges for services such as |EC2|, |SNS|, and |SQS|. For more information, see
`Amazon EC2 Pricing <https://aws.amazon.com/ec2/pricing/>`_, `Amazon SNS Pricing <https://aws.amazon.com/sns/pricing/>`_, and `Amazon SQS Pricing <https://aws.amazon.com/sqs/pricing/>`_.

* :ref:`sample-cdk-prereqs`
* :ref:`sample-cdk-install`
* :ref:`sample-cdk-code`
* :ref:`sample-cdk-run`
* :ref:`sample-cdk-clean-up`

.. _sample-cdk-prereqs:

Prerequisites
=============

.. include:: _sample-prereqs.txt

.. _sample-cdk-install:

Step 1: Install Required Tools
==============================

In this step, you install all of the tools in your |env| that the AWS CDK needs to run a sample that is written in the TypeScript programming language:

#. :ref:`Node Version Manager <sample-cdk-install-nvm>`, or :command:`nvm`, which you use to install Node.js later.
#. :ref:`Node.js <sample-cdk-install-nodejs>`, which is required by the sample and contains Node Package Manager, or :command:`npm`, which you use to install TypeScript and the AWS CDK later.
#. :ref:`TypeScript <sample-cdk-install-typescript>`, which is required by this sample. (The AWS CDK also provides support for several other programming languages.)
#. The :ref:`AWS CDK <sample-cdk-install-cdk>`.

.. _sample-cdk-install-nvm:

Step 1.1: Install Node Version Manager (nvm)
--------------------------------------------

#. In a terminal session in the |AC9IDE|, ensure the latest security updates and bug fixes are installed. To do this, run the :command:`yum update` command. (To start a new terminal session,
   on the menu bar, choose :menuselection:`Window, New Terminal`.) 

   .. code-block:: sh

      sudo yum -y update
      
#. Confirm whether :command:`nvm` is already installed. To do this, run the 
   :command:`nvm` command with the :command:`--version` option.
   
   .. code-block:: sh 

      nvm --version

   If successful, the output contains 
   the :command:`nvm` version number, and you can skip ahead to :ref:`sample-cdk-install-nodejs`.

#. Download and install :command:`nvm`. To do this, run the following command. 

   .. code-block:: sh

      curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash

#. Start using :command:`nvm`. You can either close the terminal session and then restart it, or source the :file:`~/.bashrc` file that contains the commands to load :command:`nvm`.

   .. code-block:: sh

      . ~/.bashrc

.. _sample-cdk-install-nodejs:

Step 1.2: Install Node.js
-------------------------

#. Confirm whether you already have Node.js installed, and if you do, confirm that the installed version is 8.12.0 or greater. 
   **This sample has been tested with Node.js 8.12.0.** To check, 
   with the terminal session still open in the |IDE|, run the :command:`node` command with the :command:`--version` option. 
   
   .. code-block:: sh
   
      node --version
      
   If you do have Node.js installed, the output contains the version number. If the version number is v8.12.0, skip ahead to :ref:`sample-cdk-install-typescript`.

#. Install Node.js 8.12.0 by running the :command:`nvm` command with the :command:`install` action and the version number, as follows.

   .. code-block:: sh 

      nvm install v8.12.0

#. Start using Node.js 8.12.0. To do this, run the :command:`nvm` command along with the :command:`alias` action, the version number to alias, and the version to 
   use for that alias, as follows.

   .. code-block:: sh 

      nvm alias default 8.12.0

   .. note:: The preceding command sets Node.js 8.12.0 as the default version of Node.js. Alternatively, you can run the :command:`nvm` command along with the :command:`use` 
      action instead of the :command:`alias` action (for example, 
      :command:`nvm use 8.12.0`). However, the :command:`use` action causes that version of Node.js to run only while the current terminal session is running.

#. To confirm that you're using Node.js 8.12.0, run the :command:`node --version` command again. If the correct version is installed, the output contains version v8.12.0.

.. _sample-cdk-install-typescript:

Step 1.3: Install TypeScript
----------------------------

#. Confirm whether you already have TypeScript installed. To do this, with the terminal session still open in the |IDE|, run the command-line TypeScript
   compiler with the :command:`--version` option.

   .. code-block:: sh

      tsc --version

   If you do have TypeScript installed, the output contains the TypeScript version number. 
   If TypeScript is installed, skip ahead to :ref:`sample-cdk-install-cdk`.

#. Install TypeScript. To do this, run the :command:`npm` command with the :command:`install` action, the :command:`-g` option, and the name of the TypeScript package. 
   This installs TypeScript as a global package in the |env|.

   .. code-block:: sh

      npm install -g typescript

#. Confirm that TypeScript is installed. To do this, run the command line TypeScript
   compiler with the :command:`--version` option.

   .. code-block:: sh

      tsc --version

   If TypeScript is installed, the output contains the TypeScript version number.

.. _sample-cdk-install-cdk:

Step 1.4: Install the AWS CDK
----------------------------- 

#. Confirm whether you already have the AWS CDK installed. To do this, with the terminal session still open in the |IDE|, run the :command:`cdk` command 
   with the :command:`--version` option.

   .. code-block:: sh

      cdk --version

   If the AWS CDK is installed, the output contains the AWS CDK version and build numbers. Skip ahead to :ref:`sample-cdk-code`.

#. Install the AWS CDK by running the :command:`npm` command along with the :code:`install` action, 
   the name of the AWS CDK package to install, and the :code:`-g` option to install the package globally in the |env|.

   .. code-block:: sh 

      npm install -g aws-cdk

#. Confirm that the AWS CDK is installed and correctly referenced. To do this, run the :command:`cdk` command with the :command:`--version` option.

   .. code-block:: sh 

      cdk --version

   If successful, the AWS CDK version and build numbers are displayed.

.. _sample-cdk-code:

Step 2: Add Code
================

In this step, you create a sample TypeScript project that contains all of the source code you need for the AWS CDK to programmatically deploy an |CFNlong| stack. This stack 
creates an |SNS| topic and an |SQS| queue in your AWS account and then subscribes the queue to the topic.

#. With the terminal session still open in the |IDE|, create a directory to store the project's source code, for example a :file:`~/environment/hello-cdk` directory 
   in your |env|. Then switch to that directory.

   .. code-block:: sh 

      rm -rf ~/environment/hello-cdk # Remove this directory if it already exists.
      mkdir ~/environment/hello-cdk  # Create the directory.
      cd ~/environment/hello-cdk     # Switch to the directory.

#. Set up the directory as a TypeScript language project for the AWS CDK. To do this, run the :command:`cdk` command with the :command:`init` action, the 
   :command:`sample-app` template, and the :command:`--language` option along with the name of the programming language.

   .. code-block:: sh 

      cdk init sample-app --language typescript

   This creates the following files and subdirectories in the directory.

   * A hidden :file:`.git` subdirectory and a hidden :file:`.gitignore` file, which makes the project compatible with source control tools such as Git.
   * A :file:`lib` subdirectory, which includes a :file:`hello-cdk-stack.ts` file. This file contains the code for your AWS CDK stack. This code is described in the next step in this procedure.
   * A :file:`bin` subdirectory, which includes a :file:`hello-cdk.ts` file. This file contains the entry point for your AWS CDK app.
   * A :file:`node_modules` subdirectory, which contains supporting code packages that the app and stack can use as needed.
   * A hidden :file:`.npmignore` file, which lists the types of subdirectories and files that :command:`npm` doesn't need when it builds the code.
   * A :file:`cdk.json` file, which contains information to make running the :command:`cdk` command easier.
   * A :file:`package-lock.json` file, which contains information that :command:`npm` can use to reduce possible build and run errors.
   * A :file:`package.json` file, which contains information to make running the :command:`npm` command easier and with possibly fewer build and run errors.
   * A :file:`README.md` file, which lists useful commands you can run with :command:`npm` and the AWS CDK.
   * A :file:`tsconfig.json` file, which contains information to make running the :command:`tsc` command easier and with possibly fewer build and run errors.

#. In the :guilabel:`Environment` window, open the :file:`lib/hello-cdk-stack.ts` file, and browse the following code in that file.

   .. code-block:: typescript

      import sns = require('@aws-cdk/aws-sns');
      import sqs = require('@aws-cdk/aws-sqs');
      import cdk = require('@aws-cdk/cdk');

      export class HelloCdkStack extends cdk.Stack {
        constructor(parent: cdk.App, name: string, props?: cdk.StackProps) {
          super(parent, name, props);

          const queue = new sqs.Queue(this, 'HelloCdkQueue', {
            visibilityTimeoutSec: 300
          });

          const topic = new sns.Topic(this, 'HelloCdkTopic');

          topic.subscribeQueue(queue);
        }
      }
      
   * The :code:`Stack`, :code:`App`, :code:`StackProps`, :code:`Queue`, and :code:`Topic` classes represent 
     an |CFN| stack and its properties, an executable program, an |SQS| queue, and an |SNS| topic, respectively.
   * The :code:`HelloCdkStack` class represents the |CFN| stack for this application. This stack contains the new |SQS| queue and |SNS| topic 
     for this application.

#. In the :guilabel:`Environment` window, open the :file:`bin/hello-cdk.ts` file, and browse the following code in that file.

   .. code-block:: typescript

      #!/usr/bin/env node
      import cdk = require('@aws-cdk/cdk');
      import { HelloCdkStack } from '../lib/hello-cdk-stack';

      const app = new cdk.App();
      new HelloCdkStack(app, 'HelloCdkStack');
      app.run();

   This code loads, instantiates, and then runs the :code:`HelloCdkStack` class from the :file:`lib/hello-cdk-stack.ts` file.

#. Use :command:`npm` to run the TypeScript compiler to check for coding errors, and then enable the AWS CDK to execute the project's :file:`bin/hello-cdk.js` file. 
   To do this, from the project's root directory, run the :command:`npm` command with the :command:`run` action, specifying 
   the :command:`build` command value in the :file:`package.json` file, as follows.

   .. code-block:: sh 

      npm run build

   The preceding command runs the TypeScript compiler, which adds supporting :file:`bin/hello-cdk.d.ts` and :file:`lib/hello-cdk-stack.d.ts` files. The compiler 
   also transpiles the :file:`hello-cdk.ts` and :file:`hello-cdk-stack.ts` files into :file:`hello-cdk.js` and 
   :file:`hello-cdk-stack.js` files. 

.. _sample-cdk-run:

Step 3: Run the Code
====================

In this step, you instruct the AWS CDK to create a |CFN| stack template based on the code in the :file:`bin/hello-cdk.js` file. You then instruct the AWS CDK to deploy the stack, which 
creates the |SNS| topic and |SQS| queue and then subscribes the queue to the topic. You then confirm that the topic and queue were successfully deployed by sending a message from the topic to the queue.

#. Have the AWS CDK create the |CFN| stack template. To do this, with the terminal session still open in the |IDE|, from the project's root directory, run the :command:`cdk` command with the 
   :command:`synth` action and the name of the stack. 

   .. code-block:: sh 

      cdk synth HelloCdkStack

   If successful, the output displays the |CFN| stack template's :code:`Resources` section.

#. The first time that you deploy an AWS CDK app into an environment for a specific AWS account and AWS Region combination, you must install a *bootstrap stack*. 
   This stack includes various resources that the AWS CDK needs to complete its various operations. For example, this stack includes an |S3| bucket that the AWS CDK uses to store templates 
   and assets during its deployment processes. To install the bootstrap stack, run the :command:`cdk` command with the 
   :command:`bootstrap` action.

   .. code-block:: sh 

      cdk bootstrap

#. Have the AWS CDK run the |CFN| stack template to deploy the stack. To do this, from the project's root directory, run the :command:`cdk` command with the 
   :command:`deploy` action and the name of the stack.

   .. code-block:: sh 

      cdk deploy HelloCdkStack

   If successful, the output displays that the :code:`HelloCdkStack` stack deployed without errors.

   .. note:: If the output displays a message that the stack does not define an environment and that AWS credentials could not be obtained from standard locations or no region was configured, 
      make sure that your AWS credentials are set correctly in the 
      |IDE|, and then run the :command:`cdk deploy` command again. For more information, see :ref:`Call AWS Services from an Environment <credentials>`.

#. To confirm that the |SNS| topic and |SQS| queue were successfully deployed, send a message to the topic, and then check the queue for the received message. To do this, you can use a tool such 
   as the |clilong| (|cli|) or the aws-shell. For more information about these tools, see the :ref:`AWS CLI and aws-shell Sample <sample-aws-cli>`.

   For example, to send a message to the topic, with the terminal session still open in the |IDE|, use the |cli| to run the |SNS| :command:`publish` command, supplying the message's subject and body, 
   the AWS Region for the topic, and the topic's Amazon Resource Name (ARN).

   .. code-block:: sh 

      aws sns publish --subject "Hello from the AWS CDK" --message "This is a message from the AWS CDK." --topic-arn arn:aws:sns:us-east-2:123456789012:HelloCdkStack-HelloCdkTopic1A234567-8BCD9EFGHIJ0K

   In the preceding command, replace :code:`arn:aws:sns:us-east-2:123456789012:HelloCdkStack-HelloCdkTopic1A234567-8BCD9EFGHIJ0K` with the ARN that |CFN| assigns to the topic. 
   To get the ID, you can run the |SNS| :command:`list-topics` command.

     .. code-block:: sh 

        aws sns list-topics --output table --query 'Topics[*].TopicArn'

   If successful, the output of the :command:`publish` command displays the :code:`MessageId` value for the message that was published.
   
   To check the queue for the received message, run the |SQS| :command:`receive-message` command, supplying the queue's URL.

   .. code-block:: sh 

      aws sqs receive-message --queue-url https://queue.amazonaws.com/123456789012/HelloCdkStack-HelloCdkQueue1A234567-8BCD9EFGHIJ0K

   In the preceding command, replace :code:`https://queue.amazonaws.com/123456789012/HelloCdkStack-HelloCdkQueue1A234567-8BCD9EFGHIJ0K` with the ARN that |CFN| assigns to the queue. 
   To get the URL, you can run the |SQS| :command:`list-queues` command. 

     .. code-block:: sh 

        aws sqs list-queues --output table --query 'QueueUrls[*]'

   If successful, the output of the :command:`receive-message` command displays information about the message that was received.

.. _sample-cdk-clean-up:

Step 4: Clean Up
================

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the |CFN| stack. This deletes the the |SNS| topic and |SQS| queue. You should also 
delete the |env|.

Step 4.1: Delete the Stack
--------------------------

With the terminal session still open in the |IDE|, from the project's root directory, run the :command:`cdk` command with the 
:command:`destroy` action and the stack's name.

.. code-block:: sh 

   cdk destroy HelloCdkStack

When prompted to delete the stack, type :kbd:`y`, and then press :kbd:`Enter`.

If successful, the output displays that the :code:`HelloCdkStack` stack was deleted without errors.

Step 4.2: Delete the |envtitle|
-------------------------------

To delete the |env|, see :doc:`Deleting an Environment <delete-environment>`.
