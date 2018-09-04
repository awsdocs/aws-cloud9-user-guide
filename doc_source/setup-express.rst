.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _setup-express:

###########################
Express Setup for |AC9long|
###########################

.. meta::
    :description:
        Describes how to quickly set up for a single individual to start using AWS Cloud9.

To start using |AC9|, follow one of these sets of procedures, depending on how you plan to use |AC9|.

.. list-table::
   :widths: 2 1
   :header-rows: 1

   * - **Usage pattern**
     - **Follow these procedures**
   * - I want to start using |AC9| quickly. 

       |mdash| Or |mdash| 
   
       I will be the only one using |AC9| in my AWS account.
     - **This topic**
   * - I want multiple users in my AWS account to use |AC9|.
     - :ref:`Team Setup <setup>`
   * - I want multiple users in my AWS account to use |AC9|, and I want to restrict their usage to control costs.
     - :ref:`Advanced Team Setup <setup-teams>`

To begin using |AC9| quickly, or to use |AC9| as the only one in your AWS account, simply create
an AWS account if you don't already have one, and then sign in to the |AC9| console with the credentials
of the AWS account root user.

.. important:: Although it's possible to use |AC9| as an AWS account root user, this isn't an AWS security
   best practice. We recommend you use |AC9| as an |IAM| user instead. For more information,
   see :ref:`Team Setup <setup>`. See also :iam-user-guide:`Create Individual IAM Users <best-practices.html#create-iam-users>` in the |IAM-ug|.

.. _setup-express-create-account:

Step 1: Create an AWS Account
=============================

If you already have an AWS account, skip ahead to :ref:`setup-express-sign-in-ide`.

To watch a 4-minute video related to the following procedure, see `Creating an Amazon Web Services Account <https://www.youtube.com/watch?v=WviHsoz8yHk>`_ on the YouTube website.

.. topic:: To create an AWS account

   #. Go to https://aws.amazon.com.
   #. Choose :guilabel:`Sign In to the Console`.
   #. Choose :guilabel:`Create a new AWS account`.
   #. Complete the process by following the on-screen directions. This includes giving AWS your email address and
      credit card information. You must also use your phone to enter a code that AWS gives you.

After you finish creating the account, AWS will send you a confirmation email. Do not go to the next step until you get this confirmation.

.. _setup-express-sign-in-ide:

Step 2: Sign in to the |AC9| Console with an AWS Account Root User
==================================================================

After you complete the previous step, you're ready to sign in to the |AC9| console with an AWS account root user and start using it.

.. important:: Although it's possible to sign in to the |AC9| console with an AWS account root user, this isn't an AWS security
   best practice. We recommend you sign in as an |IAM| user instead. For more information,
   see :ref:`Team Setup <setup>`. See also :iam-user-guide:`Create Individual IAM Users <best-practices.html#create-iam-users>` in the |IAM-ug|.

#. Open the AWS Cloud9 console, at |AC9Console_link|.
#. If prompted, type the email address for the AWS account root user, and then choose :guilabel:`Next`.
#. If prompted, type the password for the AWS account root user, and then choose :guilabel:`Sign In`.

   You have now successfully signed in, and the |AC9| console is displayed.

.. _setup-express-next-steps:

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
   * - Enable others in your AWS account to start using |AC9|.
     - :ref:`Team Setup <setup>`
   * - Invite others to use your new |env| along with you, in real time and with text chat support.
     - :ref:`Working with Shared Environments <share-environment>`
   * - Restrict |AC9| usage for others in your AWS account, to control costs.
     - :ref:`Advanced Team Setup <setup-teams>`
