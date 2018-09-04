.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _move-environment:

##############################################
Moving or Resizing an Environment in |AC9long|
##############################################

.. meta::
    :description:
        Describes how to move or resize an environment in AWS Cloud9.

You can move an |envfirst| from one |EC2| instance to another. (We also call this :dfn:`resizing` an |env|.) For example, you might want to do one of the following.

* Transfer an |env| from an |EC2| instance that is broken, or behaving in unexpected ways, to a healthy instance.
* Transfer an |env| from an older instance to an instance that has the latest system updates.
* Increase an instance's compute resources, because the |env| is over-utilized on the current instance.
* Decrease an instance's compute resources, because the |env| is under-utilized on the current instance.

.. note:: This topic only covers resizing an |env| from one |EC2| instance to another.
   To resize an |env| from one of your own servers to another, refer to your server's documentation.

   You cannot resize an |env| to an |EC2| instance of the same type. When you resize, you must choose a different |EC2| instance type for the new instance.

Before you start the resize process, note the following. 

* You must stop the |EC2| instance that is associated with an |env| before you can change the instance type. While the instance is stopped, neither you nor any 
  members will be able to use the |env| that are associated with the stopped instance.
* We move the instance to new hardware; however, the instance's ID does not change.
* If the instance is running in an |VPC| and has a public IPv4 address, we release the address and give it a new public IPv4 address. 
  The instance retains its private IPv4 addresses, any Elastic IP addresses, and any IPv6 addresses.
* Ensure that you plan for downtime while your instance is stopped. The process might take several minutes.

To resize an |env|, do the following. 

#. (Optional) If the new instance type requires drivers that are not installed on the existing instance, you must connect to your instance and install the drivers first. 
   For more information, see :ec2-user-guide:`Compatibility for Resizing Instances <ec2-instance-resize.html#resize-limitations>` in the |EC2-ug|.
#. Close all web browser tabs that are currently displaying the |env|.

   .. important:: If you do not close all of the web browser tabs that are currently displaying the |env|, |AC9| might interfere with allowing you to fully complete the procedure. 
      Specifically, |AC9| might try at the wrong time during this procedure to restart the |EC2| instance that is associated with the |env|. The instance must stay stopped until the 
      very last step in this procedure.

#. Sign in to the AWS Management Console, if you are not already signed in, at https://console.aws.amazon.com.

   We recommend you sign in using credentials for an |IAM| administrator user in your AWS account. If you cannot
   do this, check with your AWS account administrator.

#. Open the |EC2| console. To do this, in the :guilabel:`Services` list, choose :guilabel:`EC2`.
#. In the AWS navigation bar, choose the AWS Region that contains the |env| that you want to resize (for example, :guilabel:`US East (Ohio)`).
#. In the service navigation pane, expand :guilabel:`Instances` if it is not already expanded, and then choose :guilabel:`Instances`.
#. In the list of instances, choose the instance that is associated with the |env| that you want to resize. For an |envec2|, 
   the instance name starts with :code:`aws-cloud9-` followed by the |env| name. For example,
   if the |env| is named :code:`my-demo-environment`,
   the instance name will start with :code:`aws-cloud9-my-demo-environment`.
#. If the :guilabel:`Instance State` is not :guilabel:`stopped`, choose :guilabel:`Actions, Instance State, Stop`. When prompted, choose :guilabel:`Yes, Stop`. 
   It can take a few minutes for the instance to stop.
#. After the :guilabel:`Instance State` is :guilabel:`stopped`, with the instance still selected, 
   choose :guilabel:`Actions, Instance Settings, Change Instance Type`.
#. In the :guilabel:`Change Instance Type` dialog box, for :guilabel:`Instance Type`, choose the new instance type that you want the |env| to use. 

   .. note:: If the instance type that you want does not appear in the list, then it is not compatible with the instance's configuration (for example, because of its virtualization type).

#. (Optional) If the instance type that you chose supports EBS–optimization, select :guilabel:`EBS-optimized` to enable EBS–optimization, or clear :guilabel:`EBS-optimized` 
   to disable EBS–optimization.
   
   .. note:: If the instance type that you chose is EBS–optimized by default, :guilabel:`EBS-optimized` is selected and you can't clear it.

#. Choose :guilabel:`Apply` to accept the new settings. 

   .. note:: If you did not choose a different instance type for :guilabel:`Instance Type` earlier in this procedure, nothing happens after you choose :guilabel:`Apply`.

#. Reopen the |env|. For more information, see :ref:`Opening an Environment <open-environment>`.

For more information about the preceding procedure, see :ec2-user-guide:`Changing the Instance Type <ec2-instance-resize.html>` in the |EC2-ug|.
