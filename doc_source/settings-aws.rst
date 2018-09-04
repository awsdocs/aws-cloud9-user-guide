.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _settings-aws:

###################################################################
Working with AWS Project and User Settings in the |AC9IDElongtitle|
###################################################################

.. meta::
    :description:
        Describes how to work with AWS project and user settings in the AWS Cloud9 IDE.

AWS service settings, located in the :guilabel:`AWS Settings` pane of the :guilabel:`Preferences` tab, include the following kinds of settings:

* Which AWS Region to use for the :guilabel:`AWS Resources` window
* Whether to use |AC9tempcreds|
* Whether to display the AWS Serverless Application Model (AWS SAM) template editor in plain text or visual mode

To view or change these settings, choose :guilabel:`AWS Cloud9, Preferences` in the menu bar of an |IDE| for an |env|. 

In the following lists, project-level settings apply only to the current |envfirst|, while 
user-level settings apply across each |env| associated with your |IAM| user. For more information, see 
:ref:`settings-project-apply` and :ref:`settings-user-share`.

* :ref:`settings-aws-project`
* :ref:`settings-aws-user`

.. _settings-aws-project:

Project-Level Settings
======================

:guilabel:`AWS Region`
   Which AWS Region to use for the :guilabel:`Lambda` section of the :guilabel:`AWS Resources` window.

:guilabel:`AWS managed temporary credentials`
   If turned on, uses |AC9tempcreds| when calling AWS services from the |cli|, the aws-shell, or AWS SDK code from an |env|. For more information, 
   see :ref:`auth-and-access-control-temporary-managed-credentials`.

.. _settings-aws-user:

User-Level Settings
===================

:guilabel:`Use AWS SAM visual editor`
   If turned on, displays the AWS Serverless Application Model (AWS SAM) template editor in visual mode 
   when using the :guilabel:`Lambda` section of the :guilabel:`AWS Resources` window. If turned off, displays the editor in text mode.