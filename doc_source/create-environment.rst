.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _create-environment:

####################################
Creating an Environment in |AC9long|
####################################

.. meta::
    :description:
        Describes how to create an environment in AWS Cloud9.

To create an |envfirstlong|, follow one of these sets of procedures, depending on how you plan to use |AC9|.

.. list-table::
   :widths: 2 1
   :header-rows: 1

   * - **Usage pattern**
     - **Follow these procedures**
   * - I want |AC9| to create a development |env|, launch a new |EC2| instance running Amazon Linux with no sample code, connect the |env| to the new instance, and then open the |AC9IDE|.
     - **This topic**
   * - I want |AC9| to create an |env|, connect it to an existing |EC2| instance or my own server, and then open the |IDE|. 
     - **This topic**
   * - I want to launch a new |EC2| instance preconfigured with a popular app or framework such as WordPress, MySQL, PHP, Node.js, Nginx, Drupal, or Joomla, 
       or a Linux distribution such as Ubuntu, Debian, FreeBSD, or openSUSE. Then I want |AC9| to create an |env|, connect it to the new instance, and then open the |IDE|.
     - :ref:`Working with Amazon Lightsail Instances <lightsail-instances>`
   * - I want to create a software development project that includes a toolchain with source control, build, deployment, and virtual servers or serverless resources. Then I want 
       |AC9| to create an |env|, connect it to the project, and then open the |IDE|.
     - :ref:`Working with AWS CodeStar Projects <codestar-projects>`

Before you start this procedure, you must already be signed in to |AC9|. To sign in to |AC9|,
see one of the following:
   
* :ref:`setup-express-sign-in-ide` in :title:`Express Setup`.
* :ref:`setup-sign-in-ide` in :title:`Team Setup`.

.. note:: Completing this procedure might result in charges to your AWS account. These include possible charges for |EC2|. For more information, see
   `Amazon EC2 Pricing <https://aws.amazon.com/ec2/pricing/>`_.

To create an |env|, do the following:

#. After you sign in to the |AC9| console, in the top navigation bar, choose an AWS Region to create the |env| in. For a list of available AWS Regions, see 
   :aws-gen-ref:`AWS Cloud9 <rande.html#cloud9_region>` in the |AWS-gr|.

   .. image:: images/console-region.png
      :alt: AWS Region selector in the AWS Cloud9 console

#. If a welcome page is displayed, for :guilabel:`New AWS Cloud9 environment`, choose :guilabel:`Create environment`.
   Otherwise, choose :guilabel:`Create environment`.

   .. image:: images/console-welcome-new-env.png
      :alt: Choosing the Next step button if welcome page is displayed

   Or: 
   
   .. image:: images/console-new-env.png
      :alt: Choosing the Create environment button if welcome page is not displayed

#. On the :guilabel:`Name environment` page, for :guilabel:`Name`, type a name for your |envfirstlong|.
#. To add a description to your |env|, type it in :guilabel:`Description`.
#. Choose :guilabel:`Next step`.
#. On the :guilabel:`Configure settings` page, for :guilabel:`Environment type`, do one of the following:

   * To launch an |EC2| instance and then connect to the new |env| from the newly-launched instance, choose :guilabel:`Create a new instance for environment (EC2)`.
     (We call this an :dfn:`EC2 environment`.)

     .. note:: Choosing :guilabel:`Create a new instance for environment (EC2)` might result in possible charges to your AWS account for |EC2|. For more information, see
        `Amazon EC2 Pricing <https://aws.amazon.com/ec2/pricing/>`_.

   * To connect to the new |env| from an existing |EC2| instance or your own server, choose :guilabel:`Connect and run in remote server (SSH)`. (We call this an :dfn:`SSH environment`.) 
     For more information, see :ref:`SSH Environment Host Requirements <ssh-settings>`.

     .. note:: To choose :guilabel:`Connect and run in remote server (SSH)`, you must be able to reach the existing instace or your own server over the public internet using SSH. For example,
        you cannot choose :guilabel:`Connect and run in remote server (SSH)` if you
        can only reach the instance or your own server through a virtual private cloud (VPC) or virtual private network
        (VPN) and that VPC or VPN doesn't have access to the public internet.

#. Depending on the environment type you chose in step 6 of this procedure, do one of the following:

   * If you chose :guilabel:`Create a new instance for environment (EC2)`, then for :guilabel:`Instance type`, choose an instance type with the amount of RAM and vCPUs you think you need for the kinds of tasks you want to do. Or leave the default choice.

     .. note:: Choosing instance types with more RAM and vCPUs might result in additional charges to your AWS account for |EC2|.

   * If you chose :guilabel:`Connect and run in remote server (SSH)`, skip ahead to step 10 in this procedure. It shows you how to set up an existing |EC2| instance or your own server and specify |envssh| settings.

#. |AC9| uses |VPClong| (|VPC|) in your AWS account to communicate with the newly-launched |EC2| instance. Depending on how |VPC| is set up in your AWS account, do one of the following.

   .. list-table::
      :widths: 2 3 1 3
      :header-rows: 1

      * - **Does the account have a VPC with at least one subnet in that VPC?**
        - **Is the VPC you want AWS Cloud9 to use the default VPC in the account?**
        - **Does the VPC have a single subnet?**
        - **Do this**
      * - No
        - |mdash|
        - |mdash|
        - If no VPC exists, create one. To do this, expand :guilabel:`Network settings`. For :guilabel:`Network (VPC)`, choose :guilabel:`Create new VPC`, and then follow the 
          on-screen directions. For more information, see :ref:`vpc-settings-create-vpc`.
          
          If a VPC exists but has no subnet, create one. To do this, expand :guilabel:`Network settings`. For :guilabel:`Network (VPC)`, choose :guilabel:`Create new subnet`, 
          and then follow the on-screen directions. For more information, see :ref:`vpc-settings-create-subnet`.
      * - Yes
        - Yes
        - Yes
        - Skip ahead to the next step in this procedure. (|AC9| will automatically use the default VPC with its single subnet.)
      * - Yes
        - Yes
        - No
        - Expand :guilabel:`Network settings (advanced)`. For :guilabel:`Subnet`, choose the subnet you want |AC9| to use in the preselected default VPC. 
      * - Yes
        - No
        - Yes or No
        - Expand :guilabel:`Network settings`. For :guilabel:`Network (VPC)`, choose the VPC that you want |AC9| to use. 
          For :guilabel:`Subnet`, choose the subnet you want |AC9| to use in that VPC.

   For more information, see :doc:`Amazon VPC Settings <vpc-settings>`.

#. For :guilabel:`Cost-saving setting`, choose the amount of time that |AC9| will stop the |env| after the |IDE| has not been used. Or leave the default choice.

   .. note:: Choosing a shorter time period might result in fewer charges to your AWS account. Likewise, choosing a longer time might result in more charges.

   Skip ahead to step 11 in this procedure.

#. If you chose :guilabel:`Connect and run in remote server (SSH)`, do the following:

   #. Make sure the existing |EC2| instance or your own server runs Linux.
   #. Make sure the existing instance or server is reachable over the public Internet. 

      .. note:: If you are using an existing |EC2| instance, and that instance is part of an |VPClong| (|VPC|), there are additional requirements. See :ref:`Amazon VPC Settings <vpc-settings>`.

   #. On the existing instance or server, you must have Python installed, and the **version must be 2.7**. To check your version, from your instance's or server's terminal, run the command :command:`python --version`. To install Python 2.7 on your server, see one of the following:

      * :ref:`sample-python-install` in the :title:`Python Sample`.
      * `Download Python <https://www.python.org/downloads/>`_ from the Python website and see `Installing
        Packages <https://packaging.python.org/installing/>`_ in the :title:`Python Packaging User Guide`.

   #. On the existing instance or server, you must have Node.js installed, and the **version must be 0.6.16 or later**. To check your version, from your instance's or server's terminal, run the command :command:`node --version`. To install Node.js on your server, see one of the following:

      * :ref:`sample-nodejs-install` in the :title:`Node.js Sample`.
      * `Installing Node.js via package manager <https://nodejs.org/en/download/package-manager/>`_ on the Node.js website.
      * `Node Version Manager <http://nvm.sh>`_ on GitHub.

   #. After you confirm that Node.js is installed on the existing instance or server, do the following:

      #. Back in the |AC9| console, choose :guilabel:`Copy key to clipboard`. Paste the public SSH key value that was copied into the :file:`~/.ssh/authorized_keys` file on the existing instance or server.

         .. note:: To see the public SSH key value that was copied, expand :guilabel:`View public SSH key`.

      #. For :guilabel:`Login name` in the |AC9| console, type the login name you use for the instance or server. For example, for an |EC2| instance running Amazon Linux, it might be :code:`ec2-user`. For another type of server, it might be :code:`root`.
      #. For :guilabel:`Host`, type the public IP address (preferred) or the hostname of the instance or server.
      #. For :guilabel:`Port`, type the port that you want |AC9| to use to try to connect to the instance or server, or leave the default port.
      #. To specify the path to the directory on the instance or server that you want |AC9| to start from after login, expand :guilabel:`Advanced settings`, and then type the path in :guilabel:`Environment path`. If you leave this blank, |AC9| uses the directory that your server typically starts with after login. This is usually a home or default directory.

         .. important:: This directory must have its access permissions set to :code:`rwxr-xr-x`. This means read-write-execute permissions for the owner, 
            read-execute permissions for the group, and read-execute permissions for others. For example, if the directory's path is :code:`~`, you can set 
            these permissions on the directory by running the :command:`chmod` command, as follows.

            .. code-block:: sh

               sudo chmod u=rwx,g=rx,o=rx ~

      #. To specify the path to the Node.js binary on the instance or server, expand 
         :guilabel:`Advanced settings`, and then type the path in :guilabel:`Node.js binary path`. 
         To get the path, you can run the command :command:`which node` (or 
         :command:`nvm which node` if you're using nvm) on your server. 
         For example, the path might be :code:`/usr/bin/node`. 
         If you leave this blank, |AC9| will try to guess where the Node.js binary is when it tries to connect.
      #. To specify a jump host that the instance or server uses, type information about the jump host in :guilabel:`SSH jump host`, using the format :code:`USER_NAME@HOSTNAME:PORT_NUMBER` (for example, 
         :code:`ec2-user@:ip-192-0-2-0:22`)

         The jump host must meet the following requirements:

         * It must be reachable over the public Internet using SSH.
         * It must allow inbound access by any IP address over the specified port.
         * The public SSH key value that was copied into the :file:`~/.ssh/authorized_keys` file on the existing instance or server must also be copied into the :file:`~/.ssh/authorized_keys` file on the jump host.

#. Choose :guilabel:`Next step`.
#. On the :guilabel:`Review choices` page, choose :guilabel:`Create environment`. Wait while |AC9| creates your |env|. 
   This can take several minutes. Please be patient.

   .. note:: If you chose :guilabel:`Connect and run in remote server (SSH)` previously, you'll will be prompted to confirm whether |AC9| can set up the new |env| on the existing instance or server. You'll also be given a choice to install some optional components. Simply choose :guilabel:`Next` on each of these confirmation pages.
