.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _installer:

#############################
Using the |AC9long| Installer
#############################

.. meta::
    :description:
        Describes how to use the AWS Cloud9 Installer, a script that installs prerequisites on an existing cloud compute instance or your own server so that AWS Cloud9 can use it.

Before you create an |envfirstlongssh|, the cloud compute instance (for example an |EC2| instance) or your own server that will connect to the |env| must meet the 
:ref:`SSH Host Requirements <ssh-settings-requirements>`. One of these requirements is to download and run the |AC9| Installer on the instance or server. The |AC9| Installer is a Linux shell script 
that checks whether the instance or server is running on an operating system platform and architecture that |AC9| supports. If this check succeeds, the script then attempts to install 
components and their dependencies that |AC9| requires to be on the instance or server.

This topic describes how to download and run this installer script on the target instance or server.

* :ref:`installer-download-run`
* :ref:`installer-troubleshooting`

.. _installer-download-run:

Download and Run the |AC9| Installer
====================================

#. Make sure the cloud compute instance or your own server that will connect to the |env| meets the 
   :ref:`SSH Host Requirements <ssh-settings-requirements>`. This includes having specific versions of Python and 
   Node.js already installed; setting specific permissions on the directory that you want |AC9| to start from after login; and setting up any associated |VPClong|.
#. While you are connected to the instance or server, run one of the following commands on that instance or server.

   .. code-block:: sh

      curl -L https://raw.githubusercontent.com/c9/install/master/install.sh | bash
      wget -O - https://raw.githubusercontent.com/c9/install/master/install.sh | bash

#. If a :guilabel:`Done` message displays with no errors, you can :ref:`create the SSH environment <create-environment-ssh>`.

   If an error message displays, see the next section for troubleshooting information. 

.. _installer-troubleshooting:

Troubleshooting the |AC9| Installer
===================================

This section describes common issues, possible causes, and recommended solutions for troubleshooting |AC9| Installer errors.

If your issue is not listed, or if you need additional help, see the `AWS Cloud9 Discussion Forum <https://forums.aws.amazon.com/forum.jspa?forumID=268>`_. (When you enter this forum, AWS might require you to sign in.) 
You can also `contact us <https://aws.amazon.com/contact-us/>`_ directly.

* :ref:`installer-wget-not-found`
* :ref:`installer-install-make`
* :ref:`installer-install-gcc`
* :ref:`installer-install-curses`

.. _installer-wget-not-found:

-bash: wget: command not found
------------------------------

**Issue:** When you run the installer script, the following message displays: :code:`-bash: wget: command not found`.

**Possible cause:** The :command:`wget` utility is not installed on the instance or server.

**Recommended solution:** Run the installer script on the instance or server with the :command:`curl` utility instead.

.. _installer-install-make:

Error: please install make to proceed
-------------------------------------

**Issue:** When you run the installer script, the following message displays: :code:`Error: please install make to proceed`.

**Possible cause:** The :command:`make` utility is not installed on the instance or server.

**Recommended solution:** Install the :command:`make` utility, and then try running the installer script on the instance or server again.

To install the :command:`make` utility, you could run a command on the instance or server such as the following.

* For Amazon Linux, Amazon Linux 2, and Red Hat Enterprise Linux (RHEL) running in |EC2|: :command:`sudo yum -y groupinstall "Development Tools"`
* For SUSE: :command:`sudo zypper install -y make`

.. _installer-install-gcc:

Error: please install gcc to proceed 
------------------------------------

**Issue:** When you run the installer script, the following message displays: :code:`Error: please install gcc to proceed`.

**Possible cause:** The :command:`gcc` utility is not installed on the instance or server.

**Recommended solution:** Install the :command:`gcc` utility, and then try running the installer script on the instance or server again.

To install the :command:`gcc` utility, you could run a command on the instance or server such as the following.

* For Amazon Linux, Amazon Linux 2, and Red Hat Enterprise Linux (RHEL) running in |EC2|: :command:`sudo yum -y groupinstall "Development Tools"`
* For SUSE: :command:`sudo zypper install -y gcc` 
* For other operating systems, see `Installing GCC <https://gcc.gnu.org/install/>`_.

.. _installer-install-curses:

configure: error: curses not found
----------------------------------

**Issue:** When you run the installer script, the following message displays: :code:`configure: error: curses not found`.

**Possible cause:** The :command:`ncurses` terminal control library is not installed on the instance or server.

**Recommended solution:** Install the :command:`ncurses` terminal control library (and, on some operating systems, the :command:`glibc-static` library), 
and then try running the installer script on the instance or server again.

To install the :command:`ncurses` terminal control library (and, on some operating systems, the :command:`glibc-static` library), you could run commands on the instance or server such as the following.

* For Amazon Linux, Amazon Linux 2, and Red Hat Enterprise Linux (RHEL) running in |EC2|: :command:`sudo yum -y install ncurses-devel`
* For SUSE: :command:`sudo zypper install -y ncurses-devel` and :command:`sudo zypper install -y glibc-static`


