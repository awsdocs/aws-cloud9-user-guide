.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _change-environment:

##########################################
Changing Environment Settings in |AC9long|
##########################################

.. meta::
    :description:
        Describes how to change environment settings in AWS Cloud9.

You can change the preferences or settings for an |envfirst|.

* :ref:`change-environment-single`
* :ref:`change-environment-description`
* :ref:`change-environment-description-code`

.. _change-environment-single:

Change |envtitle| Preferences
=============================

#. Open the |env| you want to change settings for. To open an |env|, see :doc:`Opening an Environment <open-environment>`.
#. In the |AC9IDE|, on the menu bar, choose :menuselection:`AWS Cloud9, Preferences`.
#. In the :guilabel:`Preferences` window, choose :guilabel:`Project Settings`.
#. Change any of the available project settings as you want. These include settings such as :guilabel:`Code Editor (Ace)` and :guilabel:`Find in Files`.

.. note:: For more information, see :ref:`settings-project-change`.

.. _change-environment-description:

Change |envtitle| Settings with the Console
===========================================

#. Sign in to the |AC9| console, at |AC9Console_link|.
#. In the top navigation bar, choose the AWS Region where the |env| is located.

   .. image:: images/console-region.png
      :alt: AWS Region selector in the AWS Cloud9 console
      
#. In the list of environments, for the |env| whose settings you want to change, do one of the following.

   * Choose the title of the card for the |env|. Then choose :guilabel:`Edit` on the next page.

     .. image:: images/console-edit-env.png
        :alt: Editing environment settings in the environment details page

   * Select the card for the |env|, and then choose the :guilabel:`Edit` button.
 
     .. image:: images/console-edit-env-card.png
        :alt: Editing environment settings in the environments list

#. Make your changes, and then choose :guilabel:`Save changes`.

   You can use the |AC9| console to change the following settings. 

   * For |envec2plural|, :guilabel:`Name` and :guilabel:`Description`.
   * For |envsshplural|: :guilabel:`Name`, :guilabel:`Description`, :guilabel:`User`, :guilabel:`Host`, :guilabel:`Port`, 
     :guilabel:`Environment path`, :guilabel:`Node.js binary path`, and :guilabel:`SSH jump host`.

   To change other settings, do the following. 

   * For |envec2plural|, do the following. 
       
     * You cannot change :guilabel:`Type`, :guilabel:`Security groups`, :guilabel:`VPC`, :guilabel:`Subnet`, :guilabel:`Environment path`, or :guilabel:`Environment ARN`.
     * For :guilabel:`Permissions` or :guilabel:`Number of members`, see :ref:`share-environment-change-access`, 
       :ref:`Remove Your User <share-environment-change-access>`, :ref:`Invite an IAM User <share-environment-invite-user>`, and 
       :ref:`share-environment-delete-member`.
     * For :guilabel:`EC2 instance type`, :guilabel:`Memory`, or :guilabel:`vCPU`, see :ref:`Moving or Resizing an Environment <move-environment>`.

   * For |envsshplural|, do the following. 

     * You cannot change :guilabel:`Type` or :guilabel:`Environment ARN`.
     * For :guilabel:`Permissions` or :guilabel:`Number of members`, see :ref:`share-environment-change-access`, 
       :ref:`Remove Your User <share-environment-change-access>`, :ref:`Invite an IAM User <share-environment-invite-user>`, and 
       :ref:`share-environment-delete-member`.

.. include:: _find-environment.txt

.. _change-environment-description-code:

Change |envtitle| Settings with Code
====================================

To use code to change the settings of an |env| in |AC9|, call the |AC9| update |env| operation, as follows.

.. list-table::
   :widths: 1 1
   :header-rows: 0

   * - |cli|
     - :AC9-cli:`update-environment <update-environment>`
   * - |sdk-cpp|
     - :sdk-cpp-ref:`UpdateEnvironmentRequest <LATEST/class_aws_1_1_cloud9_1_1_model_1_1_update_environment_request>`, 
       :sdk-cpp-ref:`UpdateEnvironmentResult <LATEST/class_aws_1_1_cloud9_1_1_model_1_1_update_environment_result>`
   * - |sdk-go|
     - :sdk-for-go-api-ref:`UpdateEnvironment <service/cloud9/#Cloud9.UpdateEnvironment>`, 
       :sdk-for-go-api-ref:`UpdateEnvironmentRequest <service/cloud9/#Cloud9.UpdateEnvironmentRequest>`, 
       :sdk-for-go-api-ref:`UpdateEnvironmentWithContext <service/cloud9/#Cloud9.UpdateEnvironmentWithContext>`
   * - |sdk-java|
     - :sdk-java-api:`UpdateEnvironmentRequest <com/amazonaws/services/cloud9/model/UpdateEnvironmentRequest>`, 
       :sdk-java-api:`UpdateEnvironmentResult <com/amazonaws/services/cloud9/model/UpdateEnvironmentResult>`
   * - |sdk-js|
     - :sdk-for-javascript-api-ref:`updateEnvironment <AWS/Cloud9.html#updateEnvironment-property>`
   * - |sdk-net|
     - :sdk-net-api-v3:`UpdateEnvironmentRequest <items/Cloud9/TUpdateEnvironmentRequest>`, 
       :sdk-net-api-v3:`UpdateEnvironmentResponse <items/Cloud9/TUpdateEnvironmentResponse>`
   * - |sdk-php|
     - :sdk-for-php-api-ref:`updateEnvironment <api-cloud9-2017-09-23.html#updateenvironment>`
   * - |sdk-python|
     - :sdk-for-python-api-ref:`update_environment <services/cloud9.html#Cloud9.Client.update_environment>`
   * - |sdk-ruby|
     - :sdk-for-ruby-api-ref:`update_environment <Aws/Cloud9/Client.html#update_environment-instance_method>`
   * - |TWPlong|
     - :TWP-ref:`Update-C9Environment <items/Update-C9Environment>`
   * - |AC9| API
     - :AC9-api:`UpdateEnvironment <API_UpdateEnvironment>`