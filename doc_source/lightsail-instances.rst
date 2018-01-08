.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _lightsail-instances:

###############################################################
Working with |lightsaillong| Instances in the |AC9IDElongtitle|
###############################################################

.. meta::
    :description:
        Describes how to work with AWS Lightsail instances in the AWS Cloud9 IDE.

You can use the |AC9IDE| to work with code on |lightsaillong| instances preconfigured with popular apps and frameworks
such as WordPress, LAMP (Linux, Apache, MySQL, and PHP), Node.js, Nginx, Drupal, and Joomla, as well as Linux distributions such
as Amazon Linux, Ubuntu, Debian, FreeBSD, and openSUSE.

|lightsail| is the easiest way to get started with AWS for developers, small businesses, students, and other users who need a
simple virtual private server (VPS) solution. |lightsail| provides developers compute, storage, and networking capacity and
capabilities to deploy and manage websites and web applications in the cloud. |lightsail| includes everything you need to
launch your project quickly |mdash| a virtual machine, SSD-based storage, data transfer, DNS management, and a static IP
|mdash| for a low, predictable monthly price. For more information, see `Amazon Lightsail Features <https://amazonlightsail.com/features/>`_.

In this topic, you create and set up a Linux-based |lightsail| instance that is compatible with |AC9|. You then create and connect an |envfirstssh| to the
|lightsail| instance.

.. note:: Completing these procedures might result in charges to your AWS account. These include possible charges for services such as |lightsail|. For more information, see
   `Amazon Lightsail Pricing <https://aws.amazon.com/lightsail/pricing/>`_.

   To create and set up a more advanced solution that includes a toolchain with the |AC9IDE|, source control, build, deployment, virtual servers or serverless resources, and more,
   skip the rest of this topic, and see :ref:`Working with AWS CodeStar Projects <codestar-projects>` instead.

   To use the |AC9IDE| to work with an |EC2| instance running Amazon Linux that contains no sample code, skip the rest of this topic, and see the :ref:`Tutorial <tutorial>` instead.

* :ref:`lightsail-instances-create`
* :ref:`lightsail-instances-setup`
* :ref:`lightsail-instances-environment`
* :ref:`lightsail-instances-change-code`

.. _lightsail-instances-create:

Step 1: Create a Linux-Based |lightsail| Instance
=================================================

In this step, you use the |lightsail| console to create an |EC2| instance running an app in a Linux-based distribution. This instance
automatically includes:

* A public and private IP address. (You can create a static public IP later.)
* Access to the instance using SSH over port 22, HTTP over port 80, and HTTPS over port 443. (You can change this.)
* A block storage disk. (You can attach additional disks later.)
* Built-in system reporting.

The |lightsail| console enables you to back up, reboot, stop, or delete the instance later.

#. Open and then sign in to the |lightsail| console, at https://lightsail.aws.amazon.com.

   We recommend you sign in using credentials for an IAM administrator user in your AWS account.
   If you cannot sign in as an IAM administrator user, check with your AWS account administrator.

#. If prompted, choose the language to use in the console, and then choose :guilabel:`Save`.
#. If prompted, choose :guilabel:`Let's get started`.
#. On the home page, with the :guilabel:`Instances` tab already selected, choose :guilabel:`Create instance`.

   .. image:: images/console-lightsail-create-instance.png
      :alt: Choosing the Create instance button in the Lightsail console

#. For :guilabel:`Instance location`, be sure the location matches an AWS Region where you want to create
   the instance and 
   where |AC9| is available. For more information, see :aws-gen-ref:`AWS Cloud9 <rande.html#cloud9_region>` in the |AWS-gr|.
   To change the AWS Region, Availability Zone, or both, choose :guilabel:`Change AWS Region and Availability Zone`, and then follow the
   onscreen instructions.
#. For :guilabel:`Pick your instance image`, with :guilabel:`Linux/Unix` already chosen for :guilabel:`Select a platform`, and
   :guilabel:`Apps + OS` already chosen for :guilabel:`Select a blueprint`, choose a blueprint.

   .. image:: images/console-lightsail-pick-instance-image.png
      :alt: Choosing an instance platform and blueprint in the Lightsail console

   .. note:: If you want to create an instance with no app, choose :guilabel:`OS Only` instead of :guilabel:`Apps + OS`, and then choose a distribution.

      To learn about the available choices, see :lightsail-docs:`Choosing an Amazon Lightsail instance image <getting-started/article/compare-options-choose-lightsail-instance-image>` on the |lightsail| website.

#. For :guilabel:`Choose your instance plan`, choose a plan, or leave the selected default plan.
#. For :guilabel:`Name your instance`, type a name for the instance, or leave the suggested default name.
#. For the number of instances, type the number of instances you want to create, or leave the default of a single instance (:guilabel:`x 1`).
#. Choose :guilabel:`Create`.

.. _lightsail-instances-setup:

Step 2: Set up the Instance to Use It with |AC9|
================================================

In this step, you connect to the running instance and then set it up so that |AC9| can use it later.

.. note:: The following instructions assume you chose :guilabel:`Apps + OS` in the previous step. If you chose :guilabel:`OS Only` and a distribution other than
   :guilabel:`Ubuntu` instead, you might need to adapt the following instructions accordingly.

#. With the |lightsail| console still open from the previous step, on the :guilabel:`Instances` tab, in the card for the instance, choose the instance's name.

   .. image:: images/console-lightsail-show-instance-details.png
      :alt: Choosing to show instance details in the Lightsail console

#. On the :guilabel:`Connect` tab, for :guilabel:`Connect using your own SSH client`, note the :guilabel:`Public IP` and :guilabel:`User name` values,
   as you will need them later.

   .. image:: images/console-lightsail-instance-ip-user.png
      :alt: Instance public address and user name showing in the Lightsail console

#. Choose :guilabel:`Connect using SSH`.
#. Be sure that the instance has the latest system updates. To do this, in the terminal session that 
   appears, run the command :command:`sudo apt-get update`.
#. Check to see if Python is installed, and if it is, check to be sure the version is 2.7. To 
   check the version, 
   run the command :command:`python --version`, and note the version number that appears. If no version number appears, 
   or if the version is not 2.7, install Python 2.7 on the instance 
   by running the command :command:`sudo apt-get install python`.
#. Check to see if Node.js is installed, and if it is, check that the version is 0.6.16 or
   later. To check the version, run the command :command:`node --version`, and note the
   version number that appears. If no version number appears, or the version is not 0.6.16 or later,
   install Node.js on the instance by running the command :command:`sudo apt-get install node`.

   If you install Node.js, run the command :command:`node --version` again. If no version appears, you
   might need to install Node.js in a different way. For possible solutions, see one of the following:

   * :ref:`sample-nodejs-install` in the :title:`Node.js Sample`
   * `Installing Node.js via package manager <https://nodejs.org/en/download/package-manager/>`_ on the Node.js website
   * `Node Version Manager <http://nvm.sh>`_ on GitHub

#. Run the command :command:`which node`, and note the value that appears. You will need it later.

.. _lightsail-instances-environment:

Step 3: Create and Connect to an |envfirstlongsshtitle|
=======================================================

In this step, you use the |AC9| console and the instance's terminal to create an |envssh| and then connect the |env| to the running instance.

#. With the terminal session still open from the previous step, open the |AC9| console, at https://console.aws.amazon.com/cloud9.

   .. note:: For this step, you will work with two different AWS services at the same time.
      If you signed in to the |lightsail| console as an |IAM| administrator user, but you want a different entity to own the new |envssh|,
      we suggest opening a different web browser and signing in to the |AC9| console as that entity.

#. In the |AC9| console, choose the AWS Region that matches the one you created the instance in.

   .. image:: images/console-region.png
      :alt: AWS Region selector in the AWS Cloud9 console

#. If a welcome page is displayed, for :guilabel:`New AWS Cloud9 environment`, choose :guilabel:`Create environment`.
   Otherwise, choose :guilabel:`Create environment`.

   .. image:: images/console-welcome-new-env.png
      :alt: Choosing the Next step button if welcome page is displayed

   Or:

   .. image:: images/console-new-env.png
      :alt: Choosing the Create environment button if welcome page is not displayed

#. On the :guilabel:`Name environment` page, for :guilabel:`Name`, type a name for your |env|.
#. To add a description to your |env|, type it in :guilabel:`Description`.
#. Choose :guilabel:`Next step`.
#. On the :guilabel:`Configure settings` page, for :guilabel:`Environment type`, choose :guilabel:`Connect and run in remote server (SSH)`.
#. For :guilabel:`User`, type the :guilabel:`User name` value you noted earlier.
#. For :guilabel:`Host`, type the :guilabel:`Public IP` value you noted earlier.
#. For :guilabel:`Port`, leave the default value of :guilabel:`22`.
#. Expand :guilabel:`Advanced settings`.
#. For :guilabel:`Environment path`, type the path that |AC9| will start from after login, which is :code:`~/` (the root of the user's home directory).
#. For :guilabel:`Node.js binary path`, type the value of the command :command:`which node` you noted earlier.
#. Leave :guilabel:`SSH jump host` blank.
#. Store the public SSH key that |AC9| creates for this |env| in your system clipboard. To do this, choose :guilabel:`Copy key to clipboard`.

   .. note:: To see the public SSH key value that was copied, expand :guilabel:`View public SSH key`.

#. Save the public SSH key value you just copied to the instance. To do this, use vi, a popular text editor, which is already installed on the instance:

   #. In the terminal session for the instance, run the command :command:`vi ~/.ssh/authorized_keys`.
   #. In the vi editor that appears, go to the end of the file, and switch to insert mode. To do this,
      press :kbd:`G`, then :kbd:`A`. 
      (:guilabel:`-- INSERT --` appears at the bottom of the vi editor.)
   #. Add two carriage returns to the end of the file by pressing :kbd:`Enter` twice.
   #. Paste the contents of your system clipboard, which contains the public SSH key value you just copied, to the terminal session clipboard. To do this, 
      in the bottom corner of the terminal session window, choose the clipboard button, then paste the contents of your system clipboard into the box. 

      .. image:: images/console-lightsail-terminal-clipboard.png
         :alt: Opening the Lightsail terminal session clipboard

   #. Paste the contents of the terminal session clipboard into the vi editor. To do this, at the insertion point in the vi editor, press :kbd:`Ctrl + Shift + V`. 
   #. Save the file. To do this, press :kbd:`Esc` to enter command mode. (:guilabel:`-- INSERT --` disappears from the bottom of the vi editor.) 
      Type :kbd:`:wq` (to :kbd:`write` the file and then :kbd:`quit` the vi editor), and then press :kbd:`Enter`.

#. Back in the |AC9| console, choose :guilabel:`Next step`.
#. On the :guilabel:`Review choices` page, choose :guilabel:`Create environment`. Wait while |AC9| creates your |env| and then displays the |AC9IDE| for the |env|.
   This can take several minutes. Please be patient.

.. _lightsail-instances-change-code:

Step 4: Use the |AC9IDE| to Change the Code on the Instance
===========================================================

Now that the |IDE| appears for the new |env|, you can use the terminal session in the |IDE| instead of the |lightsail| terminal session. The |IDE| provides 
a rich code editing experience with support for several programming languages and runtime debuggers, as well as color themes,
shortcut keybindings, programming language-specific syntax coloring and code formatting, and more.

To learn how to use the |IDE|, see :ref:`Tour the IDE <tutorial-tour-ide>` in the *Tutorial*.

To learn how to change the code on your instance, we recommend the following resources.

* **All** :lightsail-docs:`Getting the application password for your 'powered by Bitnami' Lightsail image <how-to/article/log-in-to-your-bitnami-application-running-on-amazon-lightsail>` on the |lightsail| website
* **Drupal**: `Bitnami Drupal For AWS Cloud <https://docs.bitnami.com/aws/apps/drupal/>`_ on the Bitnami website, and `Tutorials and site recipes <https://www.drupal.org/node/627198>`_ on the Drupal website
* **GitLab CE**: `Bitnami GitLab CE for AWS Cloud <https://docs.bitnami.com/aws/apps/gitlab/>`_ on the Bitnami website, and `GitLab Documentation <https://docs.gitlab.com/ce/>`_ on the GitLab website
* **Joomla**: `Bitnami Joomla! For AWS Cloud <https://docs.bitnami.com/aws/apps/joomla/>`_ on the Bitnami website, and `Getting Started with Joomla! <https://www.joomla.org/about-joomla/getting-started.html>`_ on the Joomla! website
* **LAMP Stack**: `Bitnami LAMP for AWS Cloud <https://docs.bitnami.com/aws/infrastructure/lamp/>`_ on the Bitnami website
* **Magento**: `Bitnami Magento For AWS Cloud <https://docs.bitnami.com/aws/apps/magento/>`_ on the Bitnami website, and the `Magento User Guide <http://docs.magento.com/m1/ce/user_guide/getting-started.html>`_ on the Magento website
* **MEAN**: `Bitnami MEAN For AWS Cloud <https://docs.bitnami.com/aws/infrastructure/mean/>`_ on the Bitnami website
* **Nginx**: `Bitnami Nginx For AWS Cloud <https://docs.bitnami.com/aws/infrastructure/nginx/>`_  on the Bitnami website, and the `NGINX Wiki <https://www.nginx.com/resources/wiki/>`_ on the NGINX website
* **Node.js**: `Bitnami Node.Js For AWS Cloud <https://docs.bitnami.com/aws/infrastructure/nodejs/>`_  on the Bitnami website, and the `Getting Started Guide <https://nodejs.org/en/docs/guides/getting-started-guide/>`_ on the Node.js website
* **Plesk Hosting Stack on Ubuntu**: :lightsail-docs:`Set up and configure Plesk on Lightsail <how-to/article/set-up-and-configure-plesk-stack-on-lightsail>` on the |lightsail| website
* **Redmine**: `Bitnami Redmine For AWS Cloud <https://docs.bitnami.com/aws/apps/redmine/>`_  on the Bitnami website, and `Getting Started <http://www.redmine.org/projects/redmine/wiki/Getting_Started>`_ on the Redmine website
* **WordPress**: :lightsail-docs:`Getting started using WordPress from your Amazon Lightsail instance <getting-started/article/getting-started-with-wordpress-and-lightsail>` on the |lightsail| website,
  and `Bitnami WordPress For AWS Cloud <https://docs.bitnami.com/aws/apps/wordpress/>`_ on the Bitnami website
