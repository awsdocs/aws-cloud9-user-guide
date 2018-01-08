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
        Describes how to resize an environment in AWS Cloud9.

You can move an |envfirst| from one |EC2| instance to another. Or you can change an |EC2| instance that connects to an |envfirst| from one instance type to another.
For example, you might want to do one of the following:

* Transfer an |env| from an instance that is broken, or behaving in unexpected ways, to a healthy instance.
* Transfer an |env| from an older instance to an instance that has the latest system updates.
* Increase an instance's compute resources, because the |env| is over-utilized on the instance.
* Decrease an instance's compute resources, because the |env| is under-utilized on the instance.

.. note:: This topic only covers moving an |envfirst| or resizing an |EC2| instance.
   To move an |envssh| from one of your own servers to another, or to resize one of your own servers, refer to your server's documentation.

   You cannot move or resize an |env| to an instance of the same type. When you move or resize, you must choose a different instance type for the new instance.

.. topic:: To move or resize an |env|

   See the :ec2-user-guide:`Resizing an Amazon EBS-backed Instance <ec2-instance-resize.html#resize-ebs-backed-instance>` 
   procedure in the |EC2-ug|, noting these details:

   * Following this procedure might result in charges to your AWS account for |EC2| and |EBS|. For more information, see
     `Amazon EC2 Pricing <https://aws.amazon.com/ec2/pricing/>`_ and `Amazon EBS Pricing <https://aws.amazon.com/ebs/pricing/>`_.
   * Skip the steps in this procedure
     that start with **[EC2-Classic]**. Both the original and new instances run in EC2-VPC. The original or
     new instances do not run in EC2-Classic.
   * Skip the details in this procedure
     about Auto Scaling. The original or new instances do not run in an Auto Scaling group.
   * The |EC2| instance name starts with :code:`aws-cloud9-` followed by the |envfirst| name. For example,
     if the |env| is named :code:`my-demo-environment`,
     the |EC2| instance name will start with :code:`aws-cloud9-my-demo-environment`.
   * You don't need to restart the instance after you resize it. When you open an |envfirst|, |AC9| starts
     the instance automatically.
   * We do not support using any of the other procedures in the topic, such as migrating the instance.
     This is because the Amazon Machine Image (AMI) that |AC9| uses
     is constantly changing. Therefore, we don't guarantee any individual AMI will be maintained for use
     with a migrated instance.