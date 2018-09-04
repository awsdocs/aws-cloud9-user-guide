.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _app-preview:

########################################################
Previewing Running Applications in the |AC9IDElongtitle|
########################################################

.. meta::
    :description:
        Describes how to preview a running application from within the AWS Cloud9 IDE.

You can use the |AC9IDE| to preview a running application from within the |IDE|.

* :ref:`app-preview-run-app`
* :ref:`app-preview-preview-app`
* :ref:`app-preview-app-reload`
* :ref:`app-preview-app-preview-type`
* :ref:`app-preview-app-open-tab`
* :ref:`app-preview-url-switch`
* :ref:`app-preview-share`

.. _app-preview-run-app:

Run an Application
==================

Before you can preview your application from within the |IDE|, it must be running in the |envfirst| using 
HTTP over port :code:`8080`, :code:`8081`, or :code:`8082` with the IP of :code:`127.0.0.1`, :code:`localhost`, or :code:`0.0.0.0`.

.. note:: You don't have to run using HTTP over port :code:`8080`, :code:`8081`, or :code:`8082` with the IP of :code:`127.0.0.1`, :code:`localhost`, or :code:`0.0.0.0`. However, you won't be able to preview your running application from within the |IDE|.

   If you run with the IP of :code:`0.0.0.0`, anyone can potentially access your running application. For approaches to address this issue, see the following: 

   * :ref:`app-preview-share-security-group` in *Share a Running Application over the Internet*
   * :ref:`app-preview-share-subnet` in *Share a Running Application over the Internet*

To write the code to run your application on a specific port and IP, see your application's documentation.

To run your application, see :ref:`build-run-debug-run`.

To test this behavior, for example you could add the following JavaScript code to a file with a name such as :file:`server.js` in the root of your |env|. This code
runs a server using Node.js, as follows.

.. code-block:: javascript

   var http = require('http');
   var fs = require('fs');
   var url = require('url');

   http.createServer( function (request, response) {
     var pathname = url.parse(request.url).pathname;
     console.log("Trying to find '" + pathname.substr(1) + "'...");

     fs.readFile(pathname.substr(1), function (err, data) {
       if (err) {
         response.writeHead(404, {'Content-Type': 'text/html'});
         response.write("ERROR: Cannot find '" + pathname.substr(1) + "'.");
         console.log("ERROR: Cannot find '" + pathname.substr(1) + "'.");
       } else {
         console.log("Found '" + pathname.substr(1) + "'.");
         response.writeHead(200, {'Content-Type': 'text/html'});
         response.write(data.toString());
       }
       response.end();
     });
   }).listen(8080, 'localhost'); // Or 8081 or 8082 instead of 8080. Or '127.0.0.1' instead of 'localhost'.

Or you could add the following Python code to a file with a name such as :file:`server.py` in the root
of your |env|. This code runs a server using Python, as follows.

.. code-block:: python

   import os
   import SimpleHTTPServer
   import SocketServer

   ip = 'localhost' # Or '127.0.0.1' instead of 'localhost'.
   port = '8080' # Or '8081' or '8082' instead of '8080'.
   Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
   httpd = SocketServer.TCPServer((ip, int(port)), Handler)
   httpd.serve_forever()

Next, add the following HTML code to a file with a name such as :file:`index.html` in the root of your |env|.

.. code-block:: html

   <html>
     <head>
       <title>Hello Home Page</title>
     </head>
     <body>
       <p style="font-family:Arial;color:blue">Hello, World!</p>
     </body>
   </html>

To see this file's HTML output on the application preview tab, run :file:`server.js` with Node.js or :file:`server.py` file with Python.
Then follow the instructions in the next procedure to preview it. On the application preview tab, add :kbd:`/index.html` to the end of the URL, and then press :kbd:`Enter`.

.. _app-preview-preview-app:

Preview a Running Application
=============================

With your application already running using HTTP over port :code:`8080`, :code:`8081`, or :code:`8082` with the IP of :code:`127.0.0.1`, :code:`localhost`, or :code:`0.0.0.0` in the |env|, 
and with the corresponding application code file open and active in the |AC9IDE|, choose one of the following on the menu bar:

* :guilabel:`Preview, Preview Running Application`
* :guilabel:`Tools, Preview, Preview Running Application`

This opens an application preview tab within the |env|, and then displays the application's output on the tab.

If the application preview tab displays an error or is blank, try following the troubleshooting steps in :ref:`troubleshooting-app-preview`.

To enable others to preview the running application outside of the |IDE|, see :ref:`app-preview-share`. 

.. note:: If the application is not already running, you will see an error on the application preview tab. Run or restart the application, and then choose the menu bar command again.

   If your application cannot run on any of the preceding ports or IPs, or if your application must run on more than one of these ports at the same time (for example, your application must 
   run on ports :code:`8080` and :code:`3000` at the same time), the application preview tab might display an error or might be blank. This is because the application preview tab 
   within the |env| works only with the preceding ports and IPs, and it works with only a single port at a time.
   
   We don't recommend sharing the URL in the application preview tab with others. (The URL displays using the format 
   :code:`https://12a34567b8cd9012345ef67abcd890e1.vfs.cloud9.us-east-2.amazonaws.com/`, where :code:`12a34567b8cd9012345ef67abcd890e1` is the ID that |AC9| assigns to the |env|, 
   and :code:`us-east-2` is the ID of the AWS Region for the |env|.) This URL works only when the |IDE| for the |env| is open and the application is running in the same web browser.    

   If you try to go to the IP of :code:`127.0.0.1`, :code:`localhost`, or :code:`0.0.0.0` by using the application preview tab 
   in the |IDE| or in a separate web browser tab outside of the |IDE|, 
   the default built-in behavior of the |AC9IDE| is that this will attempt to go to your local computer, instead of attempting to go the 
   instance or your own server that is connected to the |env|.

.. _app-preview-app-reload:

Reload an Application Preview
=============================

On the application preview tab, choose the :guilabel:`Refresh` button (the circular arrow).

.. note:: This command does not restart the server. It just refreshes the contents of the application preview tab.

.. _app-preview-app-preview-type:

Change the Application Preview Type
===================================

On the application preview tab, choose one of the following in the preview type list:

  * :guilabel:`Browser`: Previews the output in a web browser format.
  * :guilabel:`Raw Content (UTF-8)`: Attempts to preview the output in Unicode Transformation Format
    8-bit (UTF-8) format, if applicable.
  * :guilabel:`Markdown`: Attempts to preview the output in Markdown format, if applicable.

.. _app-preview-app-open-tab:

Open an Application Preview in a Separate Web Browser Tab
=========================================================

On the application preview tab, choose :guilabel:`Pop Out Into New Window`.

.. note:: The application preview will not be displayed in a separate web browser tab unless the |AC9IDE|
   is also running in at least one other tab in the same web browser.

.. _app-preview-url-switch:

Switch to a Different Preview URL
=================================

On the application preview tab, type the path to a different URL in the address bar. The address bar is
located between the :guilabel:`Refresh` button and the preview type list.

.. _app-preview-share:

Share a Running Application over the Internet
=============================================

After you preview your running application, you can make it available to others over the internet.

To do this, if an |EC2| instance is connected to your |env|, follow these steps. Otherwise, see your server's documentation.

* :ref:`app-preview-share-get-metadata`
* :ref:`app-preview-share-security-group`
* :ref:`app-preview-share-subnet`
* :ref:`app-preview-share-change-port`
* :ref:`app-preview-share-url`

.. _app-preview-share-get-metadata:

Step 1: Get the ID and the IP Address of the Instance
-----------------------------------------------------

In this step, you note the instance ID and public IP address for the |EC2| instance that is connected to the |env|. You need the instance ID in a later step to 
allow incoming application requests. Then you give the public IP address to others so that they can access the running application.

#. Get the |EC2| instance's ID. To get this, do one of the following:

   * In a terminal session in the |AC9IDE| for the |env|, run the following command to get the |EC2| instance's ID.

     .. code-block:: sh

        curl http://169.254.169.254/latest/meta-data/instance-id

     The instance ID will look similar to this: :code:`i-12a3b456c789d0123`. Make a note of this instance ID.

   * In the |IDE| for the |env|, on the menu bar, choose your user icon, and then choose :guilabel:`Manage EC2 Instance`.
   
     .. image:: images/console-manage-instance.png
        :alt: Choosing to manage the instance from the AWS Cloud9 IDE

     In the |EC2| console that displays, make a note of the instance ID that displays in the :guilabel:`Instance ID` column. The instance ID will look similar to this: :code:`i-12a3b456c789d0123`. 

#. Get the |EC2| instance's public IP address. To get this, do one of the following:

   * In the |IDE| for the |env|, on the menu bar, choose :guilabel:`Share`. In the :guilabel:`Share this environment` dialog box, make a note of the public IP address in the :guilabel:`Application` box. 
     The public IP address will look similar to this: :code:`192.0.2.0`.

   * In a terminal session in the |IDE| for the |env|, run the following command to get the |EC2| instance's public IP address.

     .. code-block:: sh

        curl http://169.254.169.254/latest/meta-data/public-ipv4

     The public IP address will look similar to this: :code:`192.0.2.0`. Make a note of this public IP address.

   * In the |IDE| for the |env|, on the menu bar, choose your user icon, and then choose :guilabel:`Manage EC2 Instance`. In the |EC2| console that displays, on the :guilabel:`Description` tab, make a note of the 
     public IP address for the :guilabel:`IPv4 Public IP` field. The public IP address will look similar to this: :code:`192.0.2.0`.

   .. note:: The instance's public IP address might change anytime the instance restarts. To prevent this IP address from changing, one solution is to allocate an Elastic IP address and then assign that address to the running instance. For instructions, see 
      :ec2-user-guide:`Allocating an Elastic IP Address <elastic-ip-addresses-eip.html#using-instance-addressing-eips-allocating>` and 
      :ec2-user-guide:`Associating an Elastic IP Address with a Running Instance <elastic-ip-addresses-eip.html#using-instance-addressing-eips-associating>` in the |EC2-ug|.  Note also that 
      allocating an Elastic IP address might result in charges to your AWS account. For more information, see `Amazon EC2 Pricing <https://aws.amazon.com/ec2/pricing/>`_.

.. _app-preview-share-security-group:

Step 2: Set Up the Security Group for the Instance
--------------------------------------------------

In this step, you use the |EC2| console to set up the |EC2| security group for the instance that is connected to the |env|, to allow incoming HTTP requests over port 8080, 8081, or 8082.

.. note:: You don't have to run using HTTP over port :code:`8080`, :code:`8081`, or :code:`8082`. If you are running on a different protocol or port, substitute it throughout this step. 
   You won't be able to preview your running application from within the |IDE| until you switch back to running using HTTP over one of the ports and IPs as described in :ref:`app-preview-preview-app`.

   For an additional layer of security, you can also set up a network access control list (ACL) for a subnet in a virtual private cloud (VPC) that the instance can use. 
   For more information about security groups and network ACLs, see the following:
   
   * :ref:`app-preview-share-subnet`
   * :VPC-ug:`Security <VPC_Security>` in the |VPC-ug|
   * :VPC-ug:`Security Groups for Your VPC <VPC_SecurityGroups>` in the |VPC-ug|
   * :VPC-ug:`Network ACLs <VPC_ACLs>` in the |VPC-ug|

#. In the |IDE| for the |env|, on the menu bar, choose your user icon, and then choose :guilabel:`Manage EC2 Instance`. Then skip ahead to step 3 in this procedure.
#. If choosing :guilabel:`Manage EC2 Instance` or other steps in this procedure display errors, we recommend you sign in to the |EC2| console using credentials for an |IAM| administrator user in your AWS account, and then 
   complete the following instructions. If you cannot do this, check with your AWS account administrator.

   #. Sign in to the AWS Management Console, if you are not already signed in, at https://console.aws.amazon.com.
   #. Open the |EC2| console. To do this, in the AWS navigation bar, choose :guilabel:`Services`. Then choose :guilabel:`EC2`.
   #. In the AWS navigation bar, choose the AWS Region where the |env| is located.
   #. If the :guilabel:`EC2 Dashboard` is displayed, choose :guilabel:`Running Instances`. Otherwise, in the service navigation pane, expand :guilabel:`Instances` if it is not already expanded, 
      and then choose :guilabel:`Instances`.
   #. In the list of instances, select the instance where the :guilabel:`Instance ID` matches the instance ID you noted earlier.

#. In the :guilabel:`Description` tab for the instance, choose the security group link next to :guilabel:`Security groups`. 
#. With the security group displayed, look on the :guilabel:`Inbound` tab. If a rule already exists where :guilabel:`Type` is set to :guilabel:`Custom TCP Rule` and :guilabel:`Port Range` is set to 
   :guilabel:`8080`, :guilabel:`8081`, or :guilabel:`8082`, choose :guilabel:`Cancel`, and skip ahead to :ref:`app-preview-share-subnet`. Otherwise, choose :guilabel:`Edit`.
#. In the :guilabel:`Edit inbound rules` dialog box, choose :guilabel:`Add Rule`.
#. For :guilabel:`Type`, choose :guilabel:`Custom TCP Rule`.
#. For :guilabel:`Port Range`, type :code:`8080`, :code:`8081`, or :code:`8082`. 
#. For :guilabel:`Source`, choose :guilabel:`Anywhere`.

   .. note:: Choosing :guilabel:`Anywhere` for :guilabel:`Source` allows incoming requests from any IP address. To restrict this to specific IP addresses, 
      choose :guilabel:`Custom` and then type the IP address range, or choose :guilabel:`My IP` to restrict this to requests from your IP address only.

#. Choose :guilabel:`Save`.

.. _app-preview-share-subnet:

Step 3: Set Up the Subnet for the Instance
------------------------------------------

In this step, you use the consoles for |EC2| and |VPClong| (|VPC|) to set up the subnet for the |EC2| instance that is connected to the |env|, to also allow incoming HTTP requests over port 8080, 8081, or 8082.

.. note:: You don't have to run using HTTP over port :code:`8080`, :code:`8081`, or :code:`8082`. If you are running on a different protocol or port, substitute it throughout this step. 
   You won't be able to preview your running application from within the |IDE| until you switch back to running using HTTP over the ports and IPs as described in :ref:`app-preview-preview-app`.

   This step describes how to set up a network ACL for a subnet in an |VPC| that the instance can use. This step is not required. However, it adds an additional layer of security when compared to just using 
   security groups. For more information 
   about network ACLs, see the following:
   
   * :VPC-ug:`Security <VPC_Security>` in the |VPC-ug|
   * :VPC-ug:`Network ACLs <VPC_ACLs>` in the |VPC-ug|

#. With the |EC2| console already open from the previous step, in the service navigation pane, expand :guilabel:`Instances` if it is not already expanded, 
   and then choose :guilabel:`Instances`.
#. In the list of instances, select the instance where the :guilabel:`Instance ID` matches the instance ID you noted earlier.
#. In the :guilabel:`Description` tab for the instance, note the value of :guilabel:`Subnet ID`. It should look similar to this: :code:`subnet-1fab8aEX`.
#. Open the |VPC| console. To do this, in the AWS navigation bar, choose :guilabel:`Services`. Then choose :guilabel:`VPC`.

   For this step, we recommend you sign in to the |VPC| console using credentials for an |IAM| administrator user in your AWS account. If you cannot do this, check with your AWS account administrator.

#. If the :guilabel:`VPC Dashboard` is displayed, choose :guilabel:`Subnets`. Otherwise, in the service navigation pane, choose :guilabel:`Subnets`.
#. In the list of subnets, select the subnet where the :guilabel:`Subnet ID` value matches the one you noted earlier.
#. On the :guilabel:`Summary` tab, choose the network ACL link next to :guilabel:`Network ACL`. 
#. In the list of network ACLs, select the network ACL. (There is only one network ACL.)
#. Look on the :guilabel:`Inbound Rules` tab for the network ACL. If a rule already exists where :guilabel:`Type` is set to :guilabel:`HTTP* (8080)`, :guilabel:`HTTP* (8081)`, or :guilabel:`HTTP* (8082)`, 
   skip ahead to :ref:`app-preview-share-change-port`. Otherwise, choose :guilabel:`Edit`. 
#. Choose :guilabel:`Add another rule`.
#. For :guilabel:`Rule #`, type a number for the rule (for example, :code:`200`). 
#. For :guilabel:`Type`, choose :guilabel:`Custom TCP Rule`.
#. For :guilabel:`Port Range`, type :code:`8080`, :code:`8081`, or :code:`8082`. 
#. For :guilabel:`Source`, type the range of IP addresses to allow incoming requests from. For example, to allow incoming requests from any IP address, type :code:`0.0.0.0/0`.
#. With :guilabel:`Allow / Deny` set to :guilabel:`ALLOW`, choose :guilabel:`Save`.

.. _app-preview-share-change-port:

Step 4: Change the Running Application IP
-----------------------------------------

In your code, switch from using IP :code:`127.0.0.1`, :code:`localhost`, or :code:`0.0.0.0` to using the IP address or addresses you specified in the previous steps in this section. To use these new IPs, stop the application if is already running, and then run the application again.

.. note:: You won't be able to preview your running application from within the |IDE| until you switch back to running using HTTP over one of the ports and IPs as described in :ref:`app-preview-preview-app`.

.. _app-preview-share-url:

Step 5: Share the Running Application URL
-----------------------------------------

With the application running, give to others the public IP address you noted earlier. Be sure to start the URL with the correct protocol, and add the port number if it is 
not the default for that protocol (for example, :code:`http://192.0.2.0:8080/index.html` using HTTP over port 8080).

If the resulting web browser tab displays an error, or the tab is blank, try following the troubleshooting steps in :ref:`troubleshooting-app-sharing`.

.. note:: The instance's public IP address might change anytime the instance restarts. To prevent this IP address from changing, one solution is to allocate an Elastic IP address and then assign that address to the running instance. For instructions, see 
   :ec2-user-guide:`Allocating an Elastic IP Address <elastic-ip-addresses-eip.html#using-instance-addressing-eips-allocating>` and 
   :ec2-user-guide:`Associating an Elastic IP Address with a Running Instance <elastic-ip-addresses-eip.html#using-instance-addressing-eips-associating>` in the |EC2-ug|. Note also that 
   allocating an Elastic IP address might result in charges to your AWS account. For more information, see `Amazon EC2 Pricing <https://aws.amazon.com/ec2/pricing/>`_.

   You don't have to run using HTTP over port :code:`8080`, :code:`8081`, or :code:`8082`. However, you won't be able to preview your running application from within the |IDE| 
   until you switch back to running using HTTP over one of the ports and IPs as described in :ref:`app-preview-preview-app`.

   If users make requests to the preceding URL, and those requests originate from a virtual private network (VPN) that blocks traffic over the requested protocol or 
   port, those requests might fail. Those users must use a different network that allows traffic over the requested protocol and port. For more information, see your network administrator.

   We don't recommend sharing the URL in the application preview tab in the |IDE| with others. (The URL displays using the format 
   :code:`https://12a34567b8cd9012345ef67abcd890e1.vfs.cloud9.us-east-2.amazonaws.com/`, where :code:`12a34567b8cd9012345ef67abcd890e1` is the ID that |AC9| assigns to the |env|, 
   and :code:`us-east-2` is the ID of the AWS Region for the |env|.) This URL works only when the |IDE| for the |env| is open and the application is running in the same web browser.