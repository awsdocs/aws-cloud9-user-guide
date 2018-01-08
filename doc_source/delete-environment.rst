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

To prevent ongoing charges to your AWS account related to an |envfirst| that you're no longer using,
you should delete the |env|.

#. Open the |AC9| console, if it isn't already open, at |AC9Console_link|.
#. In the top navigation bar, choose the AWS Region where the |env| is located.

   .. image:: images/console-region.png
      :alt: AWS Region selector in the AWS Cloud9 console
      
#. In the list of environments, for the |env| you want to delete, do one of the following:

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

#. If the |env| was an |envssh|, |AC9| leaves behind a hidden subdirectory on the |EC2| instance or your own server that 
   was connected to that |env|. You can now safely delete that subdirectory if you want to. The subdirectory is named 
   :file:`.c9`. It is located in the :guilabel:`Environment path` directory that you specified when you created the 
   |env|.
   
   .. include:: _find-environment.txt