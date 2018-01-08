.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

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

.. _change-environment-single:

Change |envtitle| Preferences
=============================

#. Open the |env| you want to change settings for. To open an |env|, see :doc:`Opening an Environment <open-environment>`.
#. In the |AC9IDE|, on the menu bar, choose :menuselection:`AWS Cloud9, Preferences`.
#. In the :guilabel:`Preferences` window, choose :guilabel:`Project Settings`.
#. Change any of the available project settings as you want. These include settings such as :guilabel:`Code Editor (Ace)` and :guilabel:`Find in Files`.

.. note:: For more information, see :ref:`settings-project-change`.

.. _change-environment-description:

Change |envtitle| Settings
==========================

#. Open the |AC9| console, if it isn't already open, at |AC9Console_link|.
#. In the top navigation bar, choose the AWS Region where the |env| is located.

   .. image:: images/console-region.png
      :alt: AWS Region selector in the AWS Cloud9 console
      
#. In the list of environments, for the |env| whose settings you want to change, do one of the following:

   * Choose the title of the card for the |env|. Then choose :guilabel:`Edit` on the next page.

     .. image:: images/console-edit-env.png
        :alt: Editing environment settings in the environment details page

   * Select the card for the |env|, and then choose the :guilabel:`Edit` button.
 
     .. image:: images/console-edit-env-card.png
        :alt: Editing environment settings in the environments list

#. Make your changes, and then choose :guilabel:`Save changes`.

   You can use the |AC9| console to change the following settings: 

   * For |envec2plural|, :guilabel:`Name` and :guilabel:`Description`.
   * For |envsshplural|: :guilabel:`Name`, :guilabel:`Description`, :guilabel:`User`, :guilabel:`Host`, :guilabel:`Port`, 
     :guilabel:`Environment path`, :guilabel:`Node.js binary path`, and :guilabel:`SSH jump host`.

   To change other settings, do the following: 

   * For |envec2plural|: 
       
     * You cannot change :guilabel:`Type`, :guilabel:`Security groups`, :guilabel:`VPC`, :guilabel:`Subnet`, :guilabel:`Environment path`, or :guilabel:`Environment ARN`.
     * For :guilabel:`Permissions` or :guilabel:`Number of members`, see :ref:`share-environment-change-access`, 
       :ref:`Remove Your User <share-environment-change-access>`, :ref:`Invite an IAM User <share-environment-invite-user>`, and 
       :ref:`share-environment-delete-member`.
     * For :guilabel:`EC2 instance type`, :guilabel:`Memory`, or :guilabel:`vCPU`, see :ref:`Moving or Resizing an Environment <move-environment>`.

   * For |envsshplural|: 

     * You cannot change :guilabel:`Type` or :guilabel:`Environment ARN`.
     * For :guilabel:`Permissions` or :guilabel:`Number of members`, see :ref:`share-environment-change-access`, 
       :ref:`Remove Your User <share-environment-change-access>`, :ref:`Invite an IAM User <share-environment-invite-user>`, and 
       :ref:`share-environment-delete-member`.

.. include:: _find-environment.txt
