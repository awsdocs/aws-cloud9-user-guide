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

To set up to use |AC9|, follow one of these sets of procedures, depending on how you plan to use |AC9|.

.. list-table::
   :widths: 2 1
   :header-rows: 1

   * - **Usage pattern**
     - **Follow these procedures**
   * - I will always be the only one using my own AWS account, and I don't need to share my |envfirstplural| with anyone else.
     - **This topic**
   * - Multiple people will be using a single AWS account to create and share |envplural| within that account.
     - :ref:`Team Setup <setup>`
   * - Multiple people will be using a single AWS account, and I need to restrict creating |envplural| within that account to control costs.
     - :ref:`Advanced Team Setup <setup-teams>`

To set up for a single person to use |AC9| as the only individual in a single AWS account, simply create
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

After you finish creating the account, AWS will send you a confirmation email. Do not go past this
step until you get this confirmation.

.. _setup-express-sign-in-ide:

Step 2: Sign in to the |AC9| Console with an AWS Account Root User
==================================================================

After you complete the previous step, you're ready to sign in to the |AC9| console with an AWS account root user and start using it.

.. important:: Although it's possible to sign in to the |AC9| console with an AWS account root user, this isn't an AWS security
   best practice. We recommend you sign in as an |IAM| user instead. For more information,
   see :ref:`Team Setup <setup>`. See also :iam-user-guide:`Create Individual IAM Users <best-practices.html#create-iam-users>` in the |IAM-ug|.

#. Go to the AWS Cloud9 console: |AC9Console_link|.
#. If prompted, type the email address for the AWS account root user, and then choose :guilabel:`Next`.
#. If prompted, type the password for the AWS account root user, and then choose :guilabel:`Sign In`.

   You have now successfully signed in, and the |AC9| console is displayed.

Start experimenting with |AC9| by following the steps in the :doc:`IDE Tutorial <tutorial>`.
