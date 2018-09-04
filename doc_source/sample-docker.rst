.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _sample-docker:

###########################
Docker Sample for |AC9long|
###########################

.. meta::
    :description:
        Provides a hands-on sample that you can use to experiment with Docker in AWS Cloud9.

This sample shows you how to connect an |envfirstlongssh| to a running Docker container inside of an Amazon Linux instance in |EC2|.
This enables you to use the |AC9IDE| to work with code and files inside of a Docker container and to run commands on that container.
For information about Docker, see `What is Docker <https://www.docker.com/what-docker>`_ on the Docker website.

Creating this sample might result in charges to your AWS account. These include possible charges for services such as |EC2|. For more information, see
`Amazon EC2 Pricing <https://aws.amazon.com/ec2/pricing/>`_.

* :ref:`sample-docker-prereqs`
* :ref:`sample-docker-install`
* :ref:`sample-docker-build`
* :ref:`sample-docker-run`
* :ref:`sample-docker-env`
* :ref:`sample-docker-code`
* :ref:`sample-docker-clean-up`

.. _sample-docker-prereqs:

Prerequisites
=============

* **You should have an Amazon EC2 instance running Amazon Linux.** This sample assumes you already have an |EC2| instance running Amazon Linux in your AWS account.
  To launch an |EC2| instance, see `Launch a Linux Virtual Machine <https://aws.amazon.com/getting-started/tutorials/launch-a-virtual-machine/>`_.
  In the :guilabel:`Choose an Amazon Machine Image (AMI)` page of the wizard, choose an AMI whose display name starts with :guilabel:`Amazon Linux AMI`.
* **If the Amazon EC2 instance runs within an Amazon VPC, there are additional requirements.** See :ref:`vpc-settings`.
* **The Amazon EC2 instance should have at least 8 to 16 GB of free disk space available.** This sample uses Docker images that are over 3 GB in size and can use additional
  increments of 3 GB or more of disk space to build images. If you try to run this sample on
  a disk that has 8 GB of free space or less, we've found that the Docker image might not build or the Docker container might not run. To check the instance's
  free disk space, you can run a command such as :command:`df -h` (for "disk filesystem information in human-readable format") on the instance.
  To increase an existing instance's disk size, see :EC2-ug:`Modifying a Volume <ebs-modify-volume>` in the |EC2-ug|.

.. _sample-docker-install:

Step 1: Install and Run Docker
==============================

In this step, you check if Docker is installed on the |EC2| instance, and install Docker if it isn't already installed. After you install Docker, you run it on
the instance.

#. Connect to the running |EC2| instance by using an SSH client such as the :command:`ssh` utility or PuTTY. To do this, see
   "Step 3: Connect to Your Instance" in `Launch a Linux Virtual Machine <https://aws.amazon.com/getting-started/tutorials/launch-a-virtual-machine/>`_.
#. Check if Docker is installed on the instance. To do this, run the :command:`docker` command on the instance with the :command:`--version` option.

   .. code-block:: sh

      docker --version

   If Docker is installed, the Docker version and build number are displayed. In this case, skip ahead to step 5 later in this procedure.

#. Install Docker. To do this, run the :command:`yum` command with the :command:`install` action, specifying the :command:`docker` package to install.

   .. code-block:: sh

      sudo yum install -y docker

#. Confirm that Docker is installed. To do this, run the :command:`docker --version` command again. The Docker version and build number are displayed.
#. Run Docker. To do this, run the :command:`service` command with the :command:`docker` service and the :command:`start` action.

   .. code-block:: sh

      sudo service docker start

#. Confirm Docker is running. To do this, run the :command:`docker` command with the :command:`info` action.

   .. code-block:: sh

      sudo docker info

   If Docker is running, information about Docker is displayed.

.. _sample-docker-build:

Step 2: Build the Image
=======================

In this step, you use a Dockerfile to build one of the available Docker images for |AC9| onto the instance. This sample uses an image that includes Node.js and a sample chat server application.

#. On the instance, create the Dockerfile. To do this, with the SSH client still connected to the instance,
   in the :file:`/tmp` directory on the instance, create a file named :file:`Dockerfile`. For example, run the :command:`touch` command as follows.

   .. code-block:: sh

      sudo touch /tmp/Dockerfile

#. Add the following contents to the :file:`Dockerfile` file.

   .. code-block:: text

      # Build a Docker image based on the cloud9/ws-nodejs Docker image
      # definition for AWS Cloud9.
      FROM cloud9/ws-nodejs

      # Enable the Docker container to communicate with AWS Cloud9 by
      # installing SSH.
      RUN apt-get update && apt-get install -y openssh-server

      # Ensure that Node.js is installed.
      RUN apt-get install -y nodejs && ln -s /usr/bin/nodejs /usr/bin/node

      # Disable password authentication by turning off the
      # Pluggable Authentication Module (PAM).
      RUN sed -i 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config

      # Add the AWS Cloud9 SSH public key to the Docker container.
      # This assumes a file named authorized_keys containing the
      # AWS Cloud9 SSH public key already exists in the same
      # directory as the Dockerfile.
      RUN mkdir -p /home/ubuntu/.ssh
      ADD ./authorized_keys /home/ubuntu/.ssh/authorized_keys
      RUN chown -R ubuntu /home/ubuntu/.ssh /home/ubuntu/.ssh/authorized_keys && \
      chmod 700 /home/ubuntu/.ssh && \
      chmod 600 /home/ubuntu/.ssh/authorized_keys

      # Start SSH in the Docker container.
      CMD /usr/sbin/sshd -D

      # Update the password to a random one for the user ubuntu.
      RUN echo "ubuntu:$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)" | chpasswd

   To add the preceding contents to the :file:`Dockerfile` file, you could use the :command:`vi` utility on the instance as follows.

   #. Use :command:`vi` to open the :code:`/tmp/Dockerfile` file.

      .. code-block:: sh

         sudo vi /tmp/Dockerfile

   #. Paste the preceding contents into the :file:`Dockerfile` file. If you're not sure how to do this, see your SSH client's documentation.
   #. Switch to command mode. To do this, press the :kbd:`Esc` key. (:code:`-- INSERT --` disappears from the bottom of the window.)
   #. Type :code:`:wq` (to write to the :file:`/tmp/Dockerfile` file, save the file, and then exit :command:`vi`), and then press :kbd:`Enter`.

   .. note:: Additional Docker images for |AC9| are available in the `c9/templates <https://github.com/c9/templates>`_ repository on the GitHub website.
      The following table lists the available images and their content and definitions. To use a different Docker image for |AC9|, replace
      :code:`cloud9/ws-nodejs` in the Dockerfile with one of the following image IDs.

      .. list-table::
         :widths: 1 2 1
         :header-rows: 1

         * - **Image ID**
           - **Contents**
           - **Definition**
         * - `cloud9/workspace <https://hub.docker.com/r/cloud9/workspace/>`_
           - Ubuntu 14.04.5 with common tools such as Git, Node.js, OpenJDK, Apache Ant, Apache Maven, Nginx, MySQL, PostgreSQL, Ruby, Apache HTTP Server, and PHP.
           - `Definition <https://github.com/c9/templates/blob/master/workspace/Dockerfile>`_
         * - `cloud9/ws-android <https://hub.docker.com/r/cloud9/ws-android/>`_
           - The contents of the :code:`cloud9/workspace` image with the Android SDK, Gradle, and common Android tools.
           - `Definition <https://github.com/c9/templates/blob/master/ws-android/Dockerfile>`_
         * - `cloud9/ws-cpp <https://hub.docker.com/r/cloud9/ws-cpp/>`_
           - The contents of the :code:`cloud9/workspace` image with the GNU Compiler Collection (GCC) and sample C and C++ command line applications.
           - `Definition <https://github.com/c9/templates/blob/master/ws-cpp/Dockerfile>`_
         * - `cloud9/ws-default <https://hub.docker.com/r/cloud9/ws-default/>`_
           - The contents of the :code:`cloud9/workspace` image with a basic readme file.
           - `Definition <https://github.com/c9/templates/blob/master/ws-default/Dockerfile>`_
         * - `cloud9/ws-html5 <https://hub.docker.com/r/cloud9/ws-html5/>`_
           - The contents of the :code:`cloud9/workspace` image with a sample HTML file.
           - `Definition <https://github.com/c9/templates/blob/master/ws-html5/Dockerfile>`_
         * - `cloud9/ws-meteor <https://hub.docker.com/r/cloud9/ws-meteor/>`_
           - The contents of the :code:`cloud9/workspace` image with Meteor and a sample Meteor application.
           - `Definition <https://github.com/c9/templates/blob/master/ws-meteor/Dockerfile>`_
         * - `cloud9/ws-nodejs <https://hub.docker.com/r/cloud9/ws-nodejs/>`_ (this sample)
           - The contents of the :code:`cloud9/workspace` image with additional versions of Node.js and a sample chat server application.
           - `Definition <https://github.com/c9/templates/blob/master/ws-nodejs/Dockerfile>`_
         * - `cloud9/ws-php <https://hub.docker.com/r/cloud9/ws-php/>`_
           - The contents of the :code:`cloud9/workspace` image with a sample PHP application.
           - `Definition <https://github.com/c9/templates/blob/master/ws-php/Dockerfile>`_
         * - `cloud9/ws-python-plain <https://hub.docker.com/r/cloud9/ws-python-plain/>`_
           - The contents of the :code:`cloud9/workspace` image with several versions of Python and a sample web application.
           - `Definition <https://github.com/c9/templates/blob/master/ws-python-plain/Dockerfile>`_
         * - `cloud9/ws-python <https://hub.docker.com/r/cloud9/ws-python/>`_
           - The contents of the :code:`cloud9/workspace` image with Django.
           - `Definition <https://github.com/c9/templates/blob/master/ws-python/Dockerfile>`_
         * - `cloud9/ws-ruby <https://hub.docker.com/r/cloud9/ws-ruby/>`_
           - The contents of the :code:`cloud9/workspace` image with several versions of Ruby and Ruby on Rails.
           - `Definition <https://github.com/c9/templates/blob/master/ws-ruby/Dockerfile>`_
         * - `cloud9/ws-wordpress <https://hub.docker.com/r/cloud9/ws-wordpress/>`_
           - The contents of the :code:`cloud9/workspace` image with WordPress.
           - `Definition <https://github.com/c9/templates/blob/master/ws-wordpress/Dockerfile>`_

#. On the instance, create a file that contains the |AC9| SSH public key for the Docker container to use. To do this, in the same directory as the :file:`Dockerfile` file,
   create a file named :file:`authorized_keys`, for example, by running the :command:`touch` command.

   .. code-block:: sh

      sudo touch /tmp/authorized_keys

#. Add the |AC9| SSH public key to the :file:`authorized_keys` file. To get the |AC9| SSH public key, do the following:

   #. Open the |AC9| console at |AC9Console_link|.
   #. In the AWS navigation bar, in the AWS Region selector, choose the AWS Region where you'll want to create the |envfirstlong| later in this topic.
   #. If a welcome page is displayed, for :guilabel:`New AWS Cloud9 environment`, choose :guilabel:`Create environment`. Otherwise, choose :guilabel:`Create environment`.
   #. On the :guilabel:`Name environment` page, for :guilabel:`Name`, type a name for the |env|. (The name doesn't matter here. You'll choose a different name later.)
   #. Choose :guilabel:`Next step`.
   #. For :guilabel:`Environment type`, choose :guilabel:`Connect and run in remote server (SSH)`.
   #. Expand :guilabel:`View public SSH key`.
   #. Choose :guilabel:`Copy key to clipboard`. (This is between :guilabel:`View public SSH key` and :guilabel:`Advanced settings`.)
   #. Choose :guilabel:`Cancel`.
   #. Paste the contents of the clipboard into the :file:`authorized_keys` file, and then save the file. For example, you can use the :command:`vi` utility, as described earlier in this step.

#. Build the image by running the :command:`docker` command with the :command:`build` action, adding the tag :code:`cloud9-image:latest` to the image and
   specifying the path to the :file:`Dockerfile` file to use.

   .. code-block:: sh

      sudo docker build -t cloud9-image:latest /tmp

   If successful, the last two lines of the build output display :code:`Successfully built` and :code:`Successfully tagged`.

   To confirm that Docker successfully built the image, run the :command:`docker` command with the :code:`image ls` action.

   .. code-block:: sh

      sudo docker image ls

   If successful, the output displays an entry where the :code:`REPOSITORY` field is set to :code:`cloud9-image` and the :code:`TAG` field is set to :code:`latest`.

#. Make a note of the |EC2| instance's public IP address. You'll need it for :ref:`sample-docker-env`. If you're not sure what the public IP address of the instance is,
   you can run the following command on the instance to get it.

      .. code-block:: sh

         curl http://169.254.169.254/latest/meta-data/public-ipv4

.. _sample-docker-run:

Step 3: Run the Container
=========================

In this step, you run a Docker container on the instance. This container is based on the image you built in the previous step.

#. To run the Docker container, run the :command:`docker` command on the instance with the :command:`run` action and the following options.

   .. code-block:: sh

      sudo docker run -d -it --expose 9090 -p 0.0.0.0:9090:22 --name cloud9 cloud9-image:latest

   * :code:`-d` runs the container in detached mode, exiting whenever the root process that is used to run the container (in this sample, the SSH client) exits.
   * :code:`-it` runs the container with an allocated pseudo-TTY and keeps STDIN open, even if the container is not attached.
   * :code:`--expose` makes the specified port (in this sample, port :code:`9090`) available from the container.
   * :code:`-p` makes the specified port available internally to the |EC2| instance over the specified IP address and port. In this sample, port :code:`9090` on the container can be accessed
     internally through port :code:`22` on the |EC2| instance.
   * :code:`--name` is a human-readable name for the container (in this sample, :code:`cloud9`).
   * :code:`cloud9-image:latest` is the human-readable name of the built image to use to run the container.

   To confirm that Docker is successfully running the container, run the :command:`docker` command with the :code:`container ls` action.

   .. code-block:: sh

      sudo docker container ls

   If successful, the output displays an entry where the :code:`IMAGE` field is set to :code:`cloud9-image:latest` and the :code:`NAMES` field is set to :code:`cloud9`.

#. Log in to the running container. To do this, run the :command:`docker` command with the :command:`exec` action and the following options.

   .. code-block:: sh

      sudo docker exec -it cloud9 bash

   * :code:`-it` runs the container with an allocated pseudo-TTY and keeps STDIN open, even if the container isn't attached.
   * :code:`cloud9` is the human-readable name of the running container.
   * :code:`bash` starts the standard shell in the running container.

   If successful, the terminal prompt changes to display the logged-in user's name for the container and the ID of the container.

   .. note:: If you ever want to log out of the running container, run the :command:`exit` command. The terminal prompt changes back to display the logged-in user's name for the instance and
      the private DNS of the instance. The container should still be running.

#. For the directory on the running container that you want |AC9| to start from after it logs in, set its access permissions to
   :command:`rwxr-xr-x`. This means read-write-execute permissions for the owner, read-execute permissions for the group, and read-execute permissions for others. For example,
   if the directory's path is :file:`~`, you can set these permissions on the directory by running the :command:`chmod` command in the running container as follows.

   .. code-block:: sh

      sudo chmod u=rwx,g=rx,o=rx ~

#. Make a note of the path to the directory on the running container that contains the Node.js binary, as you'll need it for :ref:`sample-docker-env`.
   If you're not sure what this path is, run the following command on the running container to get it.

   .. code-block:: sh

      which node

.. _sample-docker-env:

Step 4: Create the |envtitle|
=============================

In this step, you use |AC9| to create an |envfirstlongssh| and connect it to the running Docker container. After |AC9| creates the
environment, it displays the |AC9IDE| so that you can start working with the files and code in the container.

#. Open the |AC9| console, if it isn't already open, at |AC9Console_link|.
#. In the AWS navigation bar, in the AWS Region selector, choose the AWS Region where you want to create the |envssh|.
#. If a welcome page is displayed, for :guilabel:`New AWS Cloud9 environment`, choose :guilabel:`Create environment`. Otherwise, choose :guilabel:`Create environment`.
#. On the :guilabel:`Name environment` page, for :guilabel:`Name`, type a name for the |env|.
#. To add a description to the |env|, type it in :guilabel:`Description`.
#. Choose :guilabel:`Next step`.
#. For :guilabel:`Environment type:`, choose :guilabel:`Connect and run in remote server (SSH)`.
#. For :guilabel:`User`, type :code:`ubuntu`.
#. For :guilabel:`Host`, type the pubic IP address of the |EC2| instance, which you noted earlier.
#. For :guilabel:`Port`, type :code:`9090`.
#. Expand :guilabel:`Advanced settings`.
#. For :guilabel:`Environment path`, type the path to the directory on the running container that you want |AC9| to start from after it logs in.
#. For :guilabel:`Node.js binary path`, type the path to the directory on the running container that contains the Node.js binary, which you noted earlier.
#. Choose :guilabel:`Next step`.
#. Choose :guilabel:`Create environment`.
#. When the :guilabel:`AWS Cloud9 Installer` dialog box appears, choose :guilabel:`Next`.
#. In the list of components to be installed, clear the :guilabel:`c9.ide.lambda.docker` check box, and then choose :guilabel:`Next`. This is because |AC9| cannot run Docker inside of Docker.
#. When the :guilabel:`AWS Cloud9 Installer` dialog box displays :guilabel:`Installation Completed`, choose :guilabel:`Next`, and then choose :guilabel:`Finish`.
   The |AC9IDE| appears for the running container, and you can start working with the container's files and code.

.. note:: If the container stops running, you can no longer use the |IDE| to access the container until you start running the container again.
   To do this, go back to :ref:`sample-docker-run`.

.. _sample-docker-code:

Step 5: Run the Code
====================

In this step, you use the |AC9IDE| to run a sample application inside the running Docker container.

#. With the |AC9IDE| displayed for the running container, start the sample chat server. To do this,
   in the :guilabel:`Environment` window, right-click the sample :file:`workspace/server.js` file, and then choose :guilabel:`Run`.
#. Preview the sample application. To do this, in the :guilabel:`Environment` window, open the
   the :file:`workspace/client/index.html` file. Then, on the menu bar, choose :guilabel:`Tools, Preview, Preview Running Application`.
#. On the application preview tab, for :guilabel:`Your Name`, type your name. For :guilabel:`Message`, type a message.
   Then choose :guilabel:`Send`. The chat server adds your name and message to the list.

.. _sample-docker-clean-up:

Step 6: Clean Up
================

In this step, you delete the |env| and remove |AC9| and Docker support files from the |EC2| instance.
Also, to prevent ongoing charges to your AWS account after you're done using this sample, you should terminate the |EC2| instance that is running Docker.

Step 6.1: Delete the |envtitle|
-------------------------------

To delete the |env|, see :doc:`Deleting an Environment <delete-environment>`.

Step 6.2: Remove |AC9| Support Files from the Container
-------------------------------------------------------

After you delete the |env|, some |AC9| support files still remain in the container. If you want to keep using the container but no longer
need these support files, delete the :file:`.c9` folder from the directory on the container that you specified |AC9| to start from after it logs in.
For example, if the directory is :file:`~`, run the :command:`rm` command with the :command:`-r` option as follows.

.. code-block:: sh

   sudo rm -r ~/.c9

Step 6.3: Remove Docker Support Files from the Instance
-------------------------------------------------------

If you no longer want to keep the Docker container, the Docker image, and Docker on the |EC2| instance, but you want to keep the instance, you
can remove these Docker support files as follows.

#. Remove the Docker container from the instance. To do this, run the :command:`docker` command on the instance
   with the :command:`stop` and :command:`rm` stop actions and the human-readable name of the container.

   .. code-block:: sh

      sudo docker stop cloud9
      sudo docker rm cloud9

#. Remove the Docker image from the instance. To do this, run the :command:`docker` command on the instance
   with the :command:`image rm` action and the image's tag.

   .. code-block:: sh

      sudo docker image rm cloud9-image:latest

#. Remove any additional Docker support files that might still exit. To do this, run the :command:`docker` command on the instance
   with the :command:`system prune` action.

   .. code-block:: sh

      sudo docker system prune -a

#. Uninstall Docker. To do this, run the :command:`yum` command on the instance with the :command:`remove` action, specifying the
   :command:`docker` package to uninstall.

   .. code-block:: sh

      sudo yum -y remove docker

   You can also remove the :file:`Dockerfile` and :file:`authorized_keys` files you created earlier. For example, run the
   :command:`rm` command on the instance.

   .. code-block:: sh

      sudo rm /tmp/Dockerfile
      sudo rm /tmp/authorized_keys

Step 6.4: Terminate the Instance
--------------------------------

To terminate the |EC2| instance, see :EC2-ug:`Terminate Your Instance <terminating-instances>` in the |EC2-ug|.
