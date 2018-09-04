.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _ssh-settings:

########################################
|envfirstlongsshtitle| Host Requirements
########################################

.. meta::
    :description:
        Describes requirements for an existing Amazon EC2 instance or your own server to be used by an AWS Cloud9 SSH development environment in an AWS account.

When you create an |envec2|, |AC9| creates a new |env|, requests |EC2| to launch a new instance, and then connects the newly launched instance to the new |env|. Creating an
|envec2| has the following benefits:

* **Automatic instance launching.** When you create an |envec2|, |AC9| requests |EC2| to create a new instance at the same time. In an |envssh|, you must provide an existing cloud compute instance (for 
  example an |EC2| instance) or your own server yourself.
* **Automatic instance shutdown.** By default, |AC9| automatically shuts down the |envec2| 30 minutes after all web browser instances that are connected to the IDE for the |envec2| are closed. 
  (You can change this behavior at any time.) This helps reduce additional charges to your AWS account for using |EC2|.
* **Automatic instance cleanup.** When you delete an |envec2|, the connected |EC2| instance is automatically deleted. This also helps reduce additional charges to your AWS account for using |EC2|. In an |envssh| that 
  is connected to cloud compute instance, you must remember to delete the instance yourself.

When and How to Create an |envsshtitle|
=======================================

You must create an |envssh| instead of an |envec2| whenever any of the following is true:

.. list-table::
   :widths: 1 1
   :header-rows: 1

   * - **Requirement**
     - **Directions**
   * - You don't want to incur additional charges to your AWS account for using AWS cloud compute instances, so you decide to connect |AC9| to an existing cloud compute instance outside of AWS or your own server instead.
     -
       #. Be sure your instance or server meets the :ref:`requirements <ssh-settings-requirements>` later in this
          topic.
       #. :ref:`Create an SSH environment <create-environment>` for |AC9| to connect your instance or server to.

   * - You want to use an existing AWS cloud compute instance (for example an |EC2| instance) in your AWS account instead of having |AC9| to launch a new instance at the same time the |env| is created.
     -
       #. Be sure the instance meets the :ref:`requirements <ssh-settings-requirements>` later in this
          topic.
       #. :ref:`Create an SSH environment <create-environment>` for |AC9| to connect the instance to.

   * - You want to use an |EC2| instance type that |AC9| currently doesn't support for an |envec2| (for example, R4).
     -
       #. :EC2-ug:`Launch an Amazon EC2 instance <EC2_GetStarted>` based on the desired instance type. Or identify an existing instance in your AWS account that runs the desired instance type.
       #. Be sure the instance meets the :ref:`requirements <ssh-settings-requirements>` later in this
          topic.
       #. :ref:`Create an SSH environment <create-environment>` for |AC9| to connect the instance to.

   * - You want to use an |EC2| instance that is based on an Amazon Machine Image (AMI) other than Amazon Linux (for example, Ubuntu Server).
     -
       #. :EC2-ug:`Launch an Amazon EC2 instance <EC2_GetStarted>` based on the desired AMI. Or identify an existing instance in your AWS account that is based on the desired AMI.
       #. Be sure the instance meets the :ref:`requirements <ssh-settings-requirements>` later in this
          topic.
       #. :ref:`Create an SSH environment <create-environment>` for |AC9| to connect the instance to.

   * - You want to connect multiple |envplural| to a single existing cloud compute instance or your own server.
     -
       #. Be sure the instance or server meets the :ref:`requirements <ssh-settings-requirements>` later
          in this topic.
       #. :ref:`Create an SSH environment <create-environment>` for each |env| you want |AC9| to connect the instance or server to.

.. note:: Launching an |EC2| instance might result in possible charges to your AWS account for |EC2|. For more information, see `Amazon EC2 Pricing <https://aws.amazon.com/ec2/pricing/>`_.

.. _ssh-settings-requirements:

SSH Host Requirements
=====================

The existing cloud compute instance or your own server must meet the following requirements for |AC9| to connect it to an |envssh|.

* It must run Linux.

  .. note:: To log in to an existing AWS cloud compute instance to verify and meet requirements, see one or more of the following resources:

     * For |EC2|, see :EC2-ug:`Connect to Your Linux Instance <AccessingInstances>` in the |EC2-ug|.
     * For Amazon Lightsail, see `Connect to your Linux/Unix-based Lightsail instance <https://lightsail.aws.amazon.com/ls/docs/how-to/article/lightsail-how-to-connect-to-your-instance-virtual-private-server>`_ in the *Amazon Lightsail Documentation*.
     * For |AEBlong|, see :AEB-dg:`Listing and Connecting to Server Instances <using-features.ec2connect>` in the |AEB-dg|.
     * For |OPSlong|, see :OPS-ug:`Using SSH to Log In to a Linux Instance <workinginstances-ssh>` in the |OPS-ug|.
     * For other AWS services, see the service's `documentation <https://aws.amazon.com/documentation/>`_.

* It must be reachable over the public internet.

  .. note:: If you are using an existing AWS cloud compute instance, and that instance is part of an |VPClong| (|VPC|), there are additional requirements. See :ref:`Amazon VPC Settings <vpc-settings>`.

* It must have Python installed, and the **version must be 2.7**. To check the version, from the existing instance's or server's terminal, run the command :command:`python --version`.
  To install Python 2.7 on the instance or server, see one of the following:

  * :ref:`sample-python-install` in the :title:`Python Sample`.
  * `Download Python <https://www.python.org/downloads/>`_ from the Python website and see `Installing
    Packages <https://packaging.python.org/installing/>`_ in the :title:`Python Packaging User Guide`.

* It must have Node.js installed, and the **version must be 0.6.16 or later**. To check the version, from the existing instance's or server's terminal, run the command :command:`node --version`.
  To install Node.js on the instance or server, see one of the following:

  * :ref:`sample-nodejs-install` in the :title:`Node.js Sample`.
  * `Installing Node.js via package manager <https://nodejs.org/en/download/package-manager/>`_ on the Node.js website.
  * `Node Version Manager <http://nvm.sh>`_ on GitHub.

* The public SSH key value that |AC9| generates for the |envssh| must be stored in the correct location on the existing instance or server. To do this, as you :ref:`create a new environment <create-environment>`,
  with the create environment wizard open to the :guilabel:`Configure settings` page and :guilabel:`Connect and run remote server (SSH)` chosen, choose :guilabel:`Copy key to clipboard`.
  Paste the public SSH key value that was copied into the :file:`~/.ssh/authorized_keys` file on the existing instance or server.

  .. note:: To see the public SSH key value that was copied, expand :guilabel:`View public SSH key` on the :guilabel:`Configure settings` page.

* The path to the directory on the existing instance or server that you want |AC9| to start from after login must have its access permissions set to :code:`rwxr-xr-x`.
  This means read-write-execute permissions for the owner, read-execute permissions for the group, and read-execute permissions for others. For example, if the directory's path is :code:`~`, you can set
  these permissions on the directory by running the :command:`chmod` command from the instance's or server's terminal, as follows.

  .. code-block:: sh

     sudo chmod u=rwx,g=rx,o=rx ~

* Optionally, you can restrict inbound traffic over SSH to only the IP addresses that |AC9| uses. To do this, set inbound SSH traffic to the IP ranges as described 
  in :ref:`Inbound SSH IP Address Ranges <ip-ranges>`.

* If the |envssh| will be associated with an AWS cloud compute instance that runs within an |VPClong| (|VPC|), there are additional requirements. See :ref:`vpc-settings`.

After you are sure your instance or server meets the preceding requirements, :ref:`create an SSH environment
<create-environment-ssh>` for |AC9| to connect it to.
