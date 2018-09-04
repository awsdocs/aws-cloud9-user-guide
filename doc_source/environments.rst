.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _environments:

######################################
Working with Environments in |AC9long|
######################################

.. meta::
    :description:
        Provides a list of topics that describe how to work with an environment in AWS Cloud9.

A :dfn:`development environment` is a place in |AC9long| where you store your project's files and where
you run the tools to develop your apps.

|AC9| provides two types of development |envplural|: :dfn:`EC2 environments` and :dfn:`SSH environments`. Here are the key similarities and differences between them.

.. list-table::
   :widths: 1 1
   :header-rows: 1

   * - **EC2 environments**
     - **SSH environments**
   * - |AC9| creates an associated |EC2| instance and manages that instance's lifecycle (for example, start, stop, and terminate).
     - You use an existing cloud compute instance or your own server. You manage that instance's or server's lifecycle.
   * - The instance runs on Amazon Linux.
     - You can use any cloud compute instance that runs Linux, or your own server running Linux.
   * - |AC9| automatically sets up the instance to start working with |AC9|.
     - You must manually configure the instance or your own server to work with |AC9|.
   * - |AC9| automatically sets up the |clilong| (|cli|) on the instance for you to start using.
     - If you want to use the |cli| on the instance or your own server, you must set it up yourself.
   * - The instance has access to hundreds of useful packages, with some common packages already installed and configured, such as Git, Docker, Node.js, and Python.
     - You might need to download, install, and configure additional packages to complete common tasks.
   * - You maintain the instance, for example by periodically applying system updates.
     - You maintain the instance or your own server.
   * - When you delete the |env|, |AC9| automatically terminates the associated instance.
     - When you delete the |env|, the instance or your own server remains.

Learn how to work with an |env| in |AC9| by reading one or more of these topics.

.. toctree::
   :maxdepth: 1
   :titlesonly:

    Creating an Environment <create-environment>
    Opening an Environment <open-environment>
    Call AWS Services from an Environment <credentials>
    Changing Environment Settings <change-environment>
    Working with Shared Environments <share-environment>
    Moving or Resizing an Environment <move-environment>
    Deleting an Environment <delete-environment>
