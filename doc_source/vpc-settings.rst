.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _vpc-settings:

######################################
VPC Settings for |envfirsttitleplural|
######################################

.. meta::
    :description:
        Describes Amazon Virtual Private Cloud (Amazon VPC) requirements for use by certain AWS Cloud9 development environments in an AWS account.

Every |envfirstlong| associated with an |VPClong| (|VPC|) must meet specific 
VPC requirements. These |envplural| include |envec2plural|, as well as |envsshplural| associated with AWS cloud compute instances (for example |EC2| and 
|lightsaillong| instances) that run within a VPC.

* :ref:`vpc-settings-requirements`
* :ref:`vpc-settings-create-vpc`
* :ref:`vpc-settings-create-subnet`

.. _vpc-settings-requirements:

|VPC| Requirements for |AC9|
============================

The |VPC| that |AC9| uses requires the following settings. If you're already familiar with these requirements and just want to quickly create
a compatible VPC, skip ahead to :ref:`vpc-settings-create-vpc`.

Use the following checklist to confirm that the VPC meets **all** of the following requirements.

.. list-table::
   :widths: 1 3 2
   :header-rows: 1

   * - **Criteria**
     - **How to confirm**
     - **Additional resources**
   * - The VPC can be in the same AWS account and AWS Region as the |envfirstlong|.
   
       |mdash| OR |mdash|
   
       The VPC can be a shared VPC in a different AWS account than the |env|. (However, the VPC must be in the same AWS Region as the |env|).
     - :ref:`vpc-settings-requirements-list-vpcs`
     - 
       * :ref:`vpc-settings-create-vpc`
       * :VPC-ug:`Working with Shared VPCs <vpc-sharing>` in the |VPC-ug|
   * - The VPC must have a public subnet. (A subnet is public if its traffic is routed to an internet gateway.)
     - 
       * :ref:`vpc-settings-requirements-subnets-view`
       * :ref:`vpc-settings-requirements-subnet-public`
     - 
       * :ref:`vpc-settings-create-subnet`
       * :ref:`vpc-settings-requirements-internet-gateway-view`
       * :ref:`vpc-settings-requirements-internet-gateway-create`
       * :ref:`vpc-settings-requirements-internet-gateway-attach`
   * - The subnet must have a route table with a minimum set of routes.
     - 
       * :ref:`vpc-settings-requirements-subnet-route-table`
       * :ref:`vpc-settings-requirements-route-table-view`
       * :ref:`vpc-settings-requirements-route-table-settings`
     - 
       * :ref:`vpc-settings-requirements-route-table-create`
       * :ref:`vpc-settings-requirements-route-table-attach`
   * - The associated security groups for the VPC (or for the AWS cloud compute instance, depending on your architecture) must allow a minimum set of inbound and outbound traffic.
     - 
       * :ref:`vpc-settings-requirements-security-groups-vpc-view`
       * :ref:`vpc-settings-requirements-security-groups-instance-view`
       * :ref:`vpc-settings-requirements-security-group-vpc-view`
       * :ref:`vpc-settings-requirements-security-groups-instance-view`
       * :ref:`vpc-settings-requirements-traffic-settings`
     - 
       * :ref:`vpc-settings-requirements-security-group-vpc-create`
   * - For an additional layer of security, if the VPC has a network ACL, the network ACL must allow a minimum set of inbound and outbound traffic.
     - 
       * :ref:`vpc-settings-requirements-network-acl-confirm`
       * :ref:`vpc-settings-requirements-network-acls-view`
       * :ref:`vpc-settings-requirements-network-acl-view`
       * :ref:`vpc-settings-requirements-traffic-settings`
     - :ref:`vpc-settings-requirements-network-acl-create`

.. note:: For the following procedures, if you use the |VPC| or |EC2| consoles, we recommend you sign in to the |console| and open the |VPC| 
   console (https://console.aws.amazon.com/vpc) or |EC2| console (https://console.aws.amazon.com/ec2) using credentials for an
   |IAM| administrator user in your AWS account. If you use the |cli| or the aws-shell, we recommend you configure the |cli| or the aws-shell with the credentials for 
   an |IAM| administrator user in your AWS account. If you can't do this, check with your AWS account administrator.

.. _vpc-settings-requirements-list-vpcs:

View a List of VPCs For an AWS Region
-------------------------------------

To use the |VPC| console, in the AWS navigation bar, choose the AWS Region that |AC9| will create the |env| in. Then choose :guilabel:`Your VPCs` in the navigation pane.

To use the |CLI| or the aws-shell, run the |EC2| :command:`describe-vpcs` command, for example as follows.

.. code-block:: sh 

   aws ec2 describe-vpcs --output table --query 'Vpcs[*].VpcId' --region us-east-2

In the preceding command, replace :code:`us-east-2` with the AWS Region that |AC9| will create the |env| in. To run the preceding command in Windows, replace the single quotes with 
double quotes. To run the preceding command with the aws-shell, omit :code:`aws`.

The output contains the list of VPC IDs.

.. _vpc-settings-requirements-subnets-view:

View a List of Subnets for a VPC
--------------------------------

To use the |VPC| console, choose :guilabel:`Your VPCs` in the navigation pane. Note the VPC's ID in the :guilabel:`VPC ID` column. Then choose :guilabel:`Subnets` 
in the navigation pane, and look for subnets that contain that ID in the :guilabel:`VPC` column.

To use the |CLI| or the aws-shell, run the |EC2| :command:`describe-subnets` command, for example as follows.

.. code-block:: sh 

   aws ec2 describe-subnets --output table --query 'Subnets[*].[SubnetId,VpcId]' --region us-east-2

In the preceding command, replace :code:`us-east-2` with the AWS Region that contains the subnets. To run the preceding command in Windows, replace the single quotes with 
double quotes. To run the preceding command with the aws-shell, omit :code:`aws`.

In the output, look for subnets that match the VPC's ID.

.. _vpc-settings-requirements-subnet-public:

Confirm Whether a Subnet is Public
----------------------------------

To use the |VPC| console, choose :guilabel:`Subnets` in the navigation pane. Select the box next to the subnet you want |AC9| to use. On the :guilabel:`Route Table` tab, 
if there is an entry in the :guilabel:`Target` column that starts with :guilabel:`igw-`, the subnet is public.

To use the |CLI| or the aws-shell, run the |EC2| :command:`describe-route-tables` command, for example as follows.

.. code-block:: sh 

   aws ec2 describe-route-tables --output table --query 'RouteTables[*].Routes[*].{GatewayIds:GatewayId}' --region us-east-2 --filters Name=association.subnet-id,Values=subnet-12a3456b

In the preceding command, replace :code:`us-east-2` with the AWS Region that contains the subnet, and replace :code:`subnet-12a3456b` with the subnet ID. To run the preceding command in Windows, replace the single quotes with 
double quotes. To run the preceding command with the aws-shell, omit :code:`aws`.

In the output, if there is at least one result that starts with :code:`igw-`, the subnet is public.

In the output, if there are no results, then the route table might be associated with the VPC instead of the subnet. To confirm this, 
run the |EC2| :command:`describe-route-tables` command for the subnet's related VPC instead of the subnet itself, for example as follows.

.. code-block:: sh 

   aws ec2 describe-route-tables --output table --query 'RouteTables[*].Routes[*].{GatewayIds:GatewayId}' --region us-east-1 --filters Name=vpc-id,Values=vpc-1234ab56

In the preceding command, replace :code:`us-east-2` with the AWS Region that contains the VPC, and replace :code:`vpc-1234ab56` with the VPC ID. To run the preceding command in Windows, replace the single quotes with 
double quotes. To run the preceding command with the aws-shell, omit :code:`aws`.

In the output, if there is at least one result that starts with :code:`igw-`, the VPC contains an internet gateway.

.. _vpc-settings-requirements-internet-gateway-view:

View or Change Settings For an Internet Gateway
-----------------------------------------------

To use the |VPC| console, choose :guilabel:`Internet Gateways` in the navigation pane. Select the box next to the internet gateway. To see the settings, 
look at each of the tabs. To change a setting on a tab, choose :guilabel:`Edit` if applicable, and then follow the on-screen directions.

To use the |CLI| or the aws-shell to see the settings, run the |EC2| :command:`describe-internet-gateways` command, for example as follows.

.. code-block:: sh 

   aws ec2 describe-internet-gateways --output table --region us-east-2 --internet-gateway-id igw-1234ab5c

In the preceding command, replace :code:`us-east-2` with the AWS Region that contains the internet gateway, and replace :code:`igw-1234ab5c` with the internet gateway ID. 
To run the preceding command with the aws-shell, omit :code:`aws`.

.. _vpc-settings-requirements-internet-gateway-create:

Create an Internet Gateway
--------------------------

To use the |VPC| console, choose :guilabel:`Internet Gateways` in the navigation pane. Choose :guilabel:`Create internet gateway`, and then follow the on-screen directions.

To use the |CLI| or the aws-shell, run the |EC2| :command:`create-internet-gateway` command, for example as follows.

.. code-block:: sh 

   aws ec2 create-internet-gateway --output text --query 'InternetGateway.InternetGatewayId' --region us-east-2

In the preceding command, replace :code:`us-east-2` with the AWS Region that contains the new internet gateway. To run the preceding command in Windows, 
replace the single quotes with double quotes. To run the preceding command with the aws-shell, omit :code:`aws`.

The output contains the ID of the new internet gateway.

.. _vpc-settings-requirements-internet-gateway-attach:

Attach an Internet Gateway to a VPC
-----------------------------------

To use the |VPC| console, choose :guilabel:`Internet Gateways` in the navigation pane. Select the box next to the internet gateway. Choose 
:guilabel:`Actions, Attach to VPC` if available, and then follow the on-screen directions.

To use the |CLI| or the aws-shell, run the |EC2| :command:`attach-internet-gateway` command, for example as follows.

.. code-block:: sh 

   aws ec2 attach-internet-gateway --region us-east-2 --internet-gateway-id igw-a1b2cdef --vpc-id vpc-1234ab56

In the preceding command, replace :code:`us-east-2` with the AWS Region that contains the internet gateway, replace :code:`igw-a1b2cdef` with the internet gateway ID, and 
replace :code:`vpc-1234ab56` with the VPC ID. To run the preceding command with the aws-shell, omit :code:`aws`.

.. _vpc-settings-requirements-subnet-route-table:

Confirm Whether a Subnet Has a Route Table
------------------------------------------

To use the |VPC| console, choose :guilabel:`Subnets` in the navigation pane. Select the box next to the VPC's public subnet that you want |AC9| to use. 
On the :guilabel:`Route table` tab, if there is a value for :guilabel:`Route Table`, the public subnet has a route table.

To use the |CLI| or the aws-shell, run the |EC2| :command:`describe-route-tables` command, for example as follows.

.. code-block:: sh 

   aws ec2 describe-route-tables --output table --query 'RouteTables[*].Associations[*].{RouteTableIds:RouteTableId}' --region us-east-2 --filters Name=association.subnet-id,Values=subnet-12a3456b

In the preceding command, replace :code:`us-east-2` with the AWS Region that contains the public subnet, and replace :code:`subnet-12a3456b` with the public subnet ID. 
To run the preceding command in Windows, replace the single quotes with double quotes. To run the preceding command with the aws-shell, omit :code:`aws`.

If there are values in the output, the public subnet has at least one route table.

In the output, if there are no results, then the route table might be associated with the VPC instead of the subnet. To confirm this, 
run the |EC2| :command:`describe-route-tables` command for the subnet's related VPC instead of the subnet itself, for example as follows.

.. code-block:: sh 

   aws ec2 describe-route-tables --output table --query 'RouteTables[*].Associations[*].{RouteTableIds:RouteTableId}' --region us-east-2 --filters Name=vpc-id,Values=vpc-1234ab56

In the preceding command, replace :code:`us-east-2` with the AWS Region that contains the VPC, and replace :code:`vpc-1234ab56` with the VPC ID. To run the preceding command in Windows, replace the single quotes with 
double quotes. To run the preceding command with the aws-shell, omit :code:`aws`.

In the output, if there is at least one result, the VPC has at least one route table.

.. _vpc-settings-requirements-route-table-attach:

Attach a Route Table to a Subnet
--------------------------------

To use the |VPC| console, choose :guilabel:`Route Tables` in the navigation pane. Select the box next to the route table that you want to attach. 
On the :guilabel:`Subnet Associations` tab, choose :guilabel:`Edit`, select the box next to the subnet you want to attach it to, and then choose :guilabel:`Save`.

To use the |CLI| or the aws-shell, run the |EC2| :command:`associate-route-table` command, for example as follows.

.. code-block:: sh 

   aws ec2 associate-route-table --region us-east-2 --subnet-id subnet-12a3456b --route-table-id rtb-ab12cde3

In the preceding command, replace :code:`us-east-2` with the AWS Region that contains the route table, replace :code:`subnet-12a3456b` with the subnet ID, and 
replace :code:`rtb-ab12cde3` with the route table ID. To run the preceding command with the aws-shell, omit :code:`aws`.

.. _vpc-settings-requirements-route-table-create:

Create a Route Table
--------------------

To use the |VPC| console, choose :guilabel:`Route Tables` in the navigation pane. Choose :guilabel:`Create Route Table`, and then follow the on-screen directions.

To use the |CLI| or the aws-shell, run the |EC2| :command:`create-route-table` command, for example as follows.

.. code-block:: sh 

   aws ec2 create-route-table --output text --query 'RouteTable.RouteTableId' --region us-east-2 --vpc-id vpc-1234ab56

In the preceding command, replace :code:`us-east-2` with the AWS Region that contains the new route table, and 
replace :code:`vpc-1234ab56` with the VPC ID. To run the preceding command in Windows, replace the single quotes with double quotes. To run the preceding command with the aws-shell, omit :code:`aws`.

The output contains the ID of the new route table.

.. _vpc-settings-requirements-route-table-view:

View or Change Settings For a Route Table
-----------------------------------------

To use the |VPC| console, choose :guilabel:`Route Tables` in the navigation pane. Select the box next to the route table. 
To see the settings, look at each of the tabs. To change a setting on a tab, choose :guilabel:`Edit`, and then follow the on-screen directions.

To use the |CLI| or the aws-shell to see the settings, run the |EC2| :command:`describe-route-tables` command, for example as follows.

.. code-block:: sh 

   aws ec2 describe-route-tables --output table --region us-east-2 --route-table-ids rtb-ab12cde3

In the preceding command, replace :code:`us-east-2` with the AWS Region that contains the route table, and replace :code:`rtb-ab12cde3` with the route table ID. 
To run the preceding command with the aws-shell, omit :code:`aws`.

.. _vpc-settings-requirements-route-table-settings:

Minumum Suggested Route Table Settings for |AC9|
------------------------------------------------

.. list-table::
   :widths: 1 1 1 1
   :header-rows: 1

   * - **Destination**
     - **Target**
     - **Status**
     - **Propagated**
   * - CIDR-BLOCK
     - local
     - Active
     - No
   * - 0.0.0.0/0
     - igw-INTERNET-GATEWAY-ID
     - Active
     - No

In these settings, :samp:`{CIDR-BLOCK}` is the subnet's CIDR block, and :samp:`igw-{INTERNET-GATEWAY-ID}` 
is the ID of a compatible internet gateway.

.. _vpc-settings-requirements-security-groups-vpc-view:

View a List of Security Groups for a VPC
----------------------------------------

To use the |VPC| console, choose :guilabel:`Security Groups` in the navigation pane. In the :guilabel:`Search Security Groups` box, type the VPC's ID or name, and then press :kbd:`Enter`. 
Security groups for that VPC appear in the list of search results.

To use the |CLI| or the aws-shell, run the |EC2| :command:`describe-security-groups` command, for example as follows.

.. code-block:: sh 

   aws ec2 describe-security-groups --output table --query 'SecurityGroups[*].GroupId' --region us-east-2 --filters Name=vpc-id,Values=vpc-1234ab56

In the preceding command, replace :code:`us-east-2` with the AWS Region that contains the VPC, and replace :code:`vpc-1234ab56` with the VPC ID. 
To run the preceding command in Windows, replace the single quotes with 
double quotes. To run the preceding command with the aws-shell, omit :code:`aws`.

The output contains the list of security group IDs for that VPC.

.. _vpc-settings-requirements-security-groups-instance-view:

View a List of Security Groups For an AWS Cloud Compute Instance
----------------------------------------------------------------

To use the |EC2| console, expand :guilabel:`Instances` in the navigation pane, and then choose :guilabel:`Instances`. In the list of instances, select the box next to the instance. 
Security groups for that instance appear in the :guilabel:`Description` tab next to :guilabel:`Security groups`.

To use the |CLI| or the aws-shell, run the |EC2| :command:`describe-security-groups` command, for example as follows.

.. code-block:: sh 

   aws ec2 describe-instances --output table --query 'Reservations[*].Instances[*].NetworkInterfaces[*].Groups[*].GroupId' --region us-east-2 --instance-ids i-12a3c456d789e0123

In the preceding command, replace :code:`us-east-2` with the AWS Region that contains the instance, and replace :code:`i-12a3c456d789e0123` with the instance ID. 
To run the preceding command in Windows, replace the single quotes with 
double quotes. To run the preceding command with the aws-shell, omit :code:`aws`.

The output contains the list of security group IDs for that instance.

.. _vpc-settings-requirements-security-group-vpc-view:

View or Change Settings For a Security Group in a VPC
-----------------------------------------------------

To use the |VPC| console, choose :guilabel:`Security Groups` in the navigation pane. Select the box next to the security group. 
To see the settings, look at each of the tabs. To change a setting on a tab, choose :guilabel:`Edit` if applicable, and then follow the on-screen directions.

To use the |CLI| or the aws-shell to see the settings, run the |EC2| :command:`describe-security-groups` command, for example as follows.

.. code-block:: sh 

   aws ec2 describe-security-groups --output table --region us-east-2 --group-ids sg-12a3b456

In the preceding command, replace :code:`us-east-2` with the AWS Region that contains the instance, and replace :code:`sg-12a3b456` with the security group ID. 
To run the preceding command with the aws-shell, omit :code:`aws`.

.. _vpc-settings-requirements-security-group-instance-view:

View or Change Settings For a Security Group For an AWS Cloud Compute Instance
------------------------------------------------------------------------------

To use the |EC2| console, expand :guilabel:`Instances` in the navigation pane, and then choose :guilabel:`Instances`. In the list of instances, select the box next to the instance. 
In the :guilabel:`Description` tab, for :guilabel:`Security groups`, choose the security group. Look at each of the tabs. 
To change a setting on a tab, choose :guilabel:`Edit` if applicable, and then follow the on-screen directions. 

To use the |CLI| or the aws-shell to see the settings, run the |EC2| :command:`describe-security-groups` command, for example as follows.

.. code-block:: sh 

   aws ec2 describe-security-groups --output table --region us-east-2 --group-ids sg-12a3b456

In the preceding command, replace :code:`us-east-2` with the AWS Region that contains the instance, and replace :code:`sg-12a3b456` with the security group ID. 
To run the preceding command with the aws-shell, omit :code:`aws`.

.. _vpc-settings-requirements-traffic-settings:

Minimum Inbound and Outbound Traffic Settings for |AC9|
-------------------------------------------------------

* **Inbound**: All IP addresses using SSH over port 22. However, you can restrict these IP addresses to only those that |AC9| uses. For more information, see 
  :ref:`Inbound SSH IP Address Ranges <ip-ranges>`.

  .. note:: For |envec2plural| created on or after July 31 2018, |AC9| uses security groups to automatically restrict inbound IP addresses using SSH over port 22 to only those addresses that |AC9| uses. 
     For more information, see :ref:`Inbound SSH IP Address Ranges <ip-ranges>`.

* **Inbound (network ACLs only)**: For |envec2plural|, and for |envsshplural| associated with |EC2| instances running Amazon Linux, all IP addresses using TCP over ports 32768-61000. 
  For more information, and for port ranges for other |EC2| instance types, see :vpc-user-guide:`Ephemeral Ports <VPC_ACLs.html#VPC_ACLs_Ephemeral_Ports>` in the |VPC-ug|.
* **Outbound**: All traffic sources using any protocol and port.

You can set this behavior at the security group level. For an additional level of security, you can also use a network ACL. For more information, 
see :vpc-user-guide:`Comparison of Security Groups and Network ACLs <VPC_Security.html#VPC_Security_Comparison>` in the |VPC-ug|.

For example, to add inbound and outbound rules to a security group, you could set up those rules as follows.
   
Inbound rules:

.. list-table::
   :widths: 1 1 1 1
   :header-rows: 1

   * - **Type**
     - **Protocol**
     - **Port Range**
     - **Source**
   * - SSH (22)
     - TCP (6)
     - 22
     - 0.0.0.0 
       (But see the following note and :ref:`Inbound SSH IP Address Ranges <ip-ranges>`.)

.. note:: For |envec2plural| created on or after July 31 2018, |AC9| automatically adds an inbound rule to restrict inbound IP addresses using SSH over port 22 to only those addresses that |AC9| uses. 
   For more information, see :ref:`Inbound SSH IP Address Ranges <ip-ranges>`.

Outbound rules:

.. list-table::
   :widths: 1 1 1 1
   :header-rows: 1

   * - **Type**
     - **Protocol**
     - **Port Range**
     - **Source**
   * - ALL Traffic
     - ALL
     - ALL
     - 0.0.0.0/0
   
If you also choose to add inbound and outbound rules to a network ACL, you could set up those rules as follows.

Inbound rules:

.. list-table::
   :widths: 1 1 1 1 1 1
   :header-rows: 1

   * - **Rule #**
     - **Type**
     - **Protocol**
     - **Port Range**
     - **Source**
     - **Allow / Deny**
   * - 100
     - SSH (22)
     - TCP (6)
     - 22
     - 0.0.0.0 
       (But see :ref:`Inbound SSH IP Address Ranges <ip-ranges>`.)
     - ALLOW
   * - 200
     - Custom TCP Rule
     - TCP (6)
     - 32768-61000
       (For Amazon Linux instances. For other instance types, see :vpc-user-guide:`Ephemeral Ports <VPC_ACLs.html#VPC_ACLs_Ephemeral_Ports>`.)
     - 0.0.0.0/0
     - ALLOW  
   * - :code:`*`
     - ALL Traffic
     - ALL
     - ALL
     - 0.0.0.0/0
     - DENY

Outbound rules:

.. list-table::
   :widths: 1 1 1 1 1 1
   :header-rows: 1

   * - **Rule #**
     - **Type**
     - **Protocol**
     - **Port Range**
     - **Source**
     - **Allow / Deny**
   * - 100
     - ALL Traffic
     - ALL
     - ALL
     - 0.0.0.0/0
     - ALLOW
   * - :code:`*`
     - ALL Traffic
     - ALL
     - ALL
     - 0.0.0.0/0
     - DENY
   
For more information about security groups and network ACLs, see the following in the |VPC-ug|.

* :VPC-ug:`Security <VPC_Security>`
* :VPC-ug:`Security Groups for your VPC <VPC_SecurityGroups>`
* :VPC-ug:`Network ACLs <VPC_ACLs>`

.. _vpc-settings-requirements-security-group-vpc-create:

Create a Security Group in a VPC
--------------------------------

To use the |VPC| or |EC2| consoles, do one of the following. 

* In the |VPC| console, choose :guilabel:`Security Groups` in the navigation pane. Choose :guilabel:`Create Security Group`, and then follow the on-screen directions.
* In the |EC2| console, expand :guilabel:`Network & Security` in the navigation pane, and then choose :guilabel:`Security Groups`. 
  Choose :guilabel:`Create Security Group`, and then follow the on-screen directions.

To use the |CLI| or the aws-shell, run the |EC2| :command:`create-security-group` command, for example as follows.

.. code-block:: sh 

   aws ec2 create-security-group --region us-east-2 --vpc-id vpc-1234ab56

In the preceding command, replace :code:`us-east-2` with the AWS Region that contains the VPC, and replace :code:`vpc-1234ab56` with the VPC ID. 
To run the preceding command with the aws-shell, omit :code:`aws`.

.. _vpc-settings-requirements-network-acl-confirm:

Confirm Whether a VPC Has at Least One Network ACL
--------------------------------------------------

To use the |VPC| console, choose :guilabel:`Your VPCs` in the navigation pane. Select the box next to the VPC you want |AC9| to use. On the :guilabel:`Summary` tab, if there is a value for
:guilabel:`Network ACL`, the VPC has at least one network ACL.

To use the |CLI| or the aws-shell, run the |EC2| :command:`describe-network-acls` command, for example as follows.

.. code-block:: sh 

   aws ec2 describe-network-acls --output table --query 'NetworkAcls[*].Associations[*].NetworkAclId' --region us-east-2 --filters Name=vpc-id,Values=vpc-1234ab56

In the preceding command, replace :code:`us-east-2` with the AWS Region that contains the VPC, and replace :code:`vpc-1234ab56` with the VPC ID. 
To run the preceding command in Windows, replace the single quotes with 
double quotes. To run the preceding command with the aws-shell, omit :code:`aws`.

If the output contains at least one entry in the list, the VPC has at least one network ACL.

.. _vpc-settings-requirements-network-acls-view:

View a List of Network ACLs For a VPC
-------------------------------------

To use the |VPC| console, choose :guilabel:`Network ACLs` in the navigation pane. In the :guilabel:`Search Network ACLs` box, 
type the VPC's ID or name, and then press :kbd:`Enter`. Network ACLs for that VPC appear in the list of search results.

To use the |CLI| or the aws-shell, run the |EC2| :command:`describe-network-acls` command, for example as follows.

.. code-block:: sh 

   aws ec2 describe-network-acls --output table --query 'NetworkAcls[*].Associations[*].NetworkAclId' --region us-east-2 --filters Name=vpc-id,Values=vpc-1234ab56

In the preceding command, replace :code:`us-east-2` with the AWS Region that contains the VPC, and replace :code:`vpc-1234ab56` with the VPC ID. 
To run the preceding command in Windows, replace the single quotes with 
double quotes. To run the preceding command with the aws-shell, omit :code:`aws`.

The output contains a list of network ACLs for that VPC.

.. _vpc-settings-requirements-network-acl-view:

View or Change Settings For a Network ACL
-----------------------------------------

To use the |VPC| console, choose :guilabel:`Network ACLs` in the navigation pane. Select the box next to the network ACL. To see the settings, look at 
each of the tabs. To change a setting on a tab, choose :guilabel:`Edit` if applicable, and then follow the on-screen directions.

To use the |CLI| or the aws-shell to see the settings, run the |EC2| :command:`describe-network-acls` command, for example as follows.

.. code-block:: sh 

   aws ec2 describe-network-acls --output table --region us-east-2 --network-acl-ids acl-1234ab56 

In the preceding command, replace :code:`us-east-2` with the AWS Region that contains the network ACL, and replace :code:`acl-1234ab56` with the network ACL ID. 
To run the preceding command with the aws-shell, omit :code:`aws`.

.. _vpc-settings-requirements-network-acl-create:

Create a Network ACL
--------------------

To use the |VPC| console, choose :guilabel:`Network ACLs` in the navigation pane. Choose :guilabel:`Create Network ACL`, and then follow the on-screen directions.

To use the |CLI| or the aws-shell, run the |EC2| :command:`create-network-acl` command, for example as follows.

.. code-block:: sh 

   aws ec2 create-network-acl --region us-east-2 --vpc-id vpc-1234ab56

In the preceding command, replace :code:`us-east-2` with the AWS Region that contains the VPC that you want to attach the new network ACL to, and replace :code:`vpc-1234ab56` with the VPC ID. 
To run the preceding command with the aws-shell, omit :code:`aws`.

.. _vpc-settings-create-vpc:

Create an |VPC| for |AC9|
=========================

You can use the |VPC| console to create an |VPC| that is compatible with |AC9|.

.. note:: For this procedure, we recommend you sign in to the |console| and open the |VPC| console using credentials for an |IAM|
   administrator user in your AWS account. If you can't do this, check with your AWS account administrator.

   Some organizations may not allow you to create VPCs on your own. If you cannot create a VPC, check with your AWS account administrator or network administrator.

#. If the |VPC| console isn't already open, sign in to the |console| and open the |VPC| console at https://console.aws.amazon.com/vpc.
#. In the navigation bar, if the AWS Region isn't the same as the |env|, choose
   the correct AWS Region.
#. Choose :guilabel:`VPC Dashboard` in
   the navigation pane, if the :guilabel:`VPC Dashboard` page isn't already displayed.
#. Choose :guilabel:`Launch VPC Wizard`.
#. For :guilabel:`Step 1: Select a VPC Configuration`, with :guilabel:`VPC with a Single Public Subnet` already selected, choose :guilabel:`Select`.
#. For :guilabel:`Step 2: VPC with a Single Public Subnet`, we recommend that you leave the following default settings. (However, you can change the CIDR settings if
   you have custom CIDRs you want to use. For more information, see :vpc-user-guide:`VPC and Subnet Sizing <VPC_Subnets.html#VPC_Sizing>` in the |VPC-ug|.)

   * :guilabel:`IPv4 CIDR block`: :guilabel:`10.0.0.0/16`
   * :guilabel:`IPv6 CIDR block`: :guilabel:`No IPv6 CIDR Block`
   * :guilabel:`Public subnet's IPv4 CIDR`: :guilabel:`10.0.0.0/24`
   * :guilabel:`Availability Zone`: :guilabel:`No Preference`
   * :guilabel:`Enable DNS hostnames`: :guilabel:`Yes`
   * :guilabel:`Hardware tenancy`: :guilabel:`Default`

#. For :guilabel:`VPC name`, type a name for the VPC.
#. For :guilabel:`Subnet name`, type a name for the subnet in the VPC.
#. Choose :guilabel:`Create new VPC`.

   |VPC| creates the following resources that are compatible with |AC9|:

   * A VPC.
   * A public subnet for the VPC.
   * A route table for the public subnet with the minimum required settings.
   * An internet gateway for the public subnet.
   * A network ACL for the public subnet with the minimum required settings.

#. By default, the VPC allows incoming traffic from all types, protocols, ports, and IP addresses. 
   You can restrict this behavior to allow only IP addresses coming from |AC9| using SSH over port 22. One approach is to 
   set incoming rules on the VPC's default network ACL, as follows.

   #. In the navigation pane of the |VPC| console, choose :guilabel:`Your VPCs`.
   #. Select the box for the VPC you just created.
   #. On the :guilabel:`Summary` tab, choose the link next to :guilabel:`Network ACL`.
   #. Select the box next to the network ACL that is displayed.
   #. On the :guilabel:`Inbound Rules` tab, choose :guilabel:`Edit`.
   #. For :guilabel:`Rule # 100`, for :guilabel:`Type`, choose :guilabel:`SSH (22)`.
   #. For :guilabel:`Source`, type one of the CIDR blocks in the :ref:`Inbound SSH IP Address Ranges <ip-ranges>` list that matches the AWS Region for this VPC.
   #. Choose :guilabel:`Add another rule`.
   #. For :guilabel:`Rule #`, type :code:`200`.
   #. For :guilabel:`Type`, choose :guilabel:`SSH (22)`. 
   #. For :guilabel:`Source`, type the other CIDR block in the :ref:`Inbound SSH IP Address Ranges <ip-ranges>` list that matches the AWS Region for this VPC.
   #. At minimum, you must also allow incoming traffic from all IP addresses using TCP over ports 32768-61000 for Amazon Linux instance types. 
      (For background, and for port ranges for other |EC2| instance types, see :vpc-user-guide:`Ephemeral Ports <VPC_ACLs.html#VPC_ACLs_Ephemeral_Ports>` in the |VPC-ug|). To do this, choose :guilabel:`Add another rule`.
   #. For :guilabel:`Rule #`, type :code:`300`.
   #. For :guilabel:`Type`, choose :guilabel:`Custom TCP Rule`.
   #. For :guilabel:`Port Range`, type :code:`32768-61000` (for Amazon Linux instance types).
   #. For :guilabel:`Source`, type :code:`0.0.0.0/0`.
   #. Choose :guilabel:`Save`.
   #. You might need to add more inbound or outbound rules to the network ACL, depending on how you plan to use |AC9|. See the documentation for the 
      web services or APIs you want to allow to communicate into or out of the VPC for the :guilabel:`Type`, :guilabel:`Protocol`, :guilabel:`Port Range`, 
      and :guilabel:`Source` values to specify for these rules.

.. _vpc-settings-create-subnet:

Create a Subnet for |AC9|
=========================

You can use the |VPC| console to create a subnet for a VPC that is compatible with |AC9|.

If you followed the previous procedure to create a VPC for |AC9|, you do not also need to follow this procedure. This is because the :guilabel:`Create new VPC` wizard creates a subnet for you 
automatically.

.. important::

   * The AWS account must already have a compatible VPC in the same AWS Region for the |env|. For
     more information, see the VPC requirements in :ref:`vpc-settings-requirements`.
   * For this procedure, we recommend you sign in to the |console|, and then open the |VPC| console using
     credentials for an |IAM|
     administrator user in your AWS account. If you can't do this, check with your AWS account administrator.
   * Some organizations may not allow you to create subnets on your own. If you cannot create a subnet, check with your AWS account administrator or network administrator.

#. If the |VPC| console isn't already open, sign in to the |console| and open the |VPC| console at https://console.aws.amazon.com/vpc.
#. In the navigation bar, if the AWS Region isn't the same as the AWS Region for the |env|, choose
   the correct AWS Region.
#. Choose :guilabel:`Subnets` in the navigation
   pane, if the :guilabel:`Subnets` page isn't already displayed.
#. Choose :guilabel:`Create Subnet`.
#. In the :guilabel:`Create Subnet` dialog box, for :guilabel:`Name tag`, type a name for the subnet.
#. For :guilabel:`VPC`, choose the VPC to associate the subnet with.
#. For :guilabel:`Availability Zone`, choose the Availability Zone within the AWS Region for the subnet to use, or choose :guilabel:`No Preference` to let AWS choose an Availability Zone for you.
#. For :guilabel:`IPv4 CIDR block`, type the range of IP addresses for the subnet to use, in CIDR format. This range of IP addresses must be a subset of IP addresses in the VPC.

   For information about CIDR blocks, see :vpc-user-guide:`VPC and Subnet Sizing <VPC_Subnets.html#VPC_Sizing>` in the |VPC-ug|.
   See also `3.1. Basic Concept and Prefix Notation <http://tools.ietf.org/html/rfc4632#section-3.1>`_ in RFC 4632 or
   `IPv4 CIDR blocks <http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#IPv4_CIDR_blocks>`_ in Wikipedia.

#. After you create the subnet, be sure to associate it with a compatible route table and an internet gateway, as well as security groups, a network ACL, or both. For more information, see the requirements in :ref:`vpc-settings-requirements`.
