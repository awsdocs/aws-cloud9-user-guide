.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _delete-environment:

####################################
Deleting an Environment in |AC9long|
####################################

.. meta::
    :description:
        Describes how to delete an environment in AWS Cloud9.

To prevent any ongoing charges to your AWS account related to an |envfirst| that you're no longer using,
you should delete the |env|.

* :ref:`delete-environment-console`
* :ref:`delete-environment-code`

.. _delete-environment-console:

Deleting an |envtitle| with the Console
=======================================

.. warning:: When you delete an |env|, |AC9| deletes the |env| permanently. This includes permanently deleting all related 
   settings, user data, and uncommitted code. Deleted |envplural| cannot be recovered.

#. Sign in to the |AC9| console, at |AC9Console_link|.
#. In the top navigation bar, choose the AWS Region where the |env| is located.

   .. image:: images/console-region.png
      :alt: AWS Region selector in the AWS Cloud9 console
      
#. In the list of environments, for the |env| you want to delete, do one of the following.

   * Choose the title of the card for the |env|. Then choose :guilabel:`Delete` on the next page.

     .. image:: images/console-delete-env.png
        :alt: Deleting an environment from the environment details page

   * Select the card for the |env|, and then choose the :guilabel:`Delete` button.

     .. image:: images/console-delete-env-card.png
        :alt: Deleting an environment from the environments list

#. In the :guilabel:`Delete` dialog box, type :code:`Delete`, and then choose :guilabel:`Delete`.

   If the |env| was an |envec2|, |AC9| also terminates the |EC2| instance that was connected to that |env|.

   However, if the |env| was an |envssh|, and that |env| was connected to an |EC2| instance, |AC9| doesn't terminate 
   that instance. If you don't terminate that instance later, your AWS account might continue to have ongoing charges 
   for |EC2| related to that instance.

#. If the |env| was an |envssh|, |AC9| leaves behind a hidden subdirectory on the cloud compute instance or your own server that 
   was connected to that |env|. You can now safely delete that subdirectory if you want to. The subdirectory is named 
   :file:`.c9`. It is located in the :guilabel:`Environment path` directory that you specified when you created the 
   |env|.
   
   .. include:: _find-environment.txt

.. _delete-environment-code:

Deleting an |envtitle| with Code
================================

.. warning:: When you delete an |env|, |AC9| deletes the |env| permanently. This includes permanently deleting all related 
   settings, user data, and uncommitted code. Deleted |envplural| cannot be recovered.

To use code to delete an |env| in |AC9|, call the |AC9| delete |env| operation, as follows.

.. list-table::
   :widths: 1 1
   :header-rows: 0

   * - |cli|
     - :AC9-cli:`delete-environment <delete-environment>`
   * - |sdk-cpp|
     - :sdk-cpp-ref:`DeleteEnvironmentRequest <LATEST/class_aws_1_1_cloud9_1_1_model_1_1_delete_environment_request>`, 
       :sdk-cpp-ref:`DeleteEnvironmentResult <LATEST/class_aws_1_1_cloud9_1_1_model_1_1_delete_environment_result>`
   * - |sdk-go|
     - :sdk-for-go-api-ref:`DeleteEnvironment <service/cloud9/#Cloud9.DeleteEnvironment>`, 
       :sdk-for-go-api-ref:`DeleteEnvironmentRequest <service/cloud9/#Cloud9.DeleteEnvironmentRequest>`, 
       :sdk-for-go-api-ref:`DeleteEnvironmentWithContext <service/cloud9/#Cloud9.DeleteEnvironmentWithContext>`
   * - |sdk-java|
     - :sdk-java-api:`DeleteEnvironmentRequest <com/amazonaws/services/cloud9/model/DeleteEnvironmentRequest>`, 
       :sdk-java-api:`DeleteEnvironmentResult <com/amazonaws/services/cloud9/model/DeleteEnvironmentResult>`
   * - |sdk-js|
     - :sdk-for-javascript-api-ref:`deleteEnvironment <AWS/Cloud9.html#deleteEnvironment-property>`
   * - |sdk-net|
     - :sdk-net-api-v3:`DeleteEnvironmentRequest <items/Cloud9/TDeleteEnvironmentRequest>`, 
       :sdk-net-api-v3:`DeleteEnvironmentResponse <items/Cloud9/TDeleteEnvironmentResponse>`
   * - |sdk-php|
     - :sdk-for-php-api-ref:`deleteEnvironment <api-cloud9-2017-09-23.html#deleteenvironment>`
   * - |sdk-python|
     - :sdk-for-python-api-ref:`delete_environment <services/cloud9.html#Cloud9.Client.delete_environment>`
   * - |sdk-ruby|
     - :sdk-for-ruby-api-ref:`delete_environment <Aws/Cloud9/Client.html#delete_environment-instance_method>`
   * - |TWPlong|
     - :TWP-ref:`Remove-C9Environment <items/Remove-C9Environment>`
   * - |AC9| API
     - :AC9-api:`DeleteEnvironment <API_DeleteEnvironment>`
