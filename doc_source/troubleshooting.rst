.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _troubleshooting:

#########################
Troubleshooting |AC9long|
#########################

.. meta::
    :description:
        Provides troubleshooting guidance for AWS Cloud9.

Use the following information to help you identify and address issues with |AC9|.

* :ref:`troubleshooting-sts-assume-role`
* :ref:`troubleshooting-access-not-authorized`
* :ref:`troubleshooting-federated-service-role`
* :ref:`troubleshooting-env-loading`
* :ref:`troubleshooting-ssh-installer`
* :ref:`troubleshooting-python-ssh`
* :ref:`troubleshooting-app-preview`
* :ref:`troubleshooting-app-sharing`
* :ref:`troubleshooting-app-preview-refresh`
* :ref:`troubleshooting-app-preview-http`
* :ref:`troubleshooting-rhel`
* :ref:`troubleshooting-cli-invalid-token`
* :ref:`troubleshooting-update-ami`
* :ref:`troubleshooting-install-sam-local`
* :ref:`troubleshooting_ide_low_memory`

.. _troubleshooting-sts-assume-role:

|envtitle| Creation Error: "Not authorized to perform sts:AssumeRole"
=====================================================================

**Issue:** When you try to create a new |env|, you see this error: "Not authorized to perform
sts:AssumeRole," and the |env| is not created.

**Possible causes:** An |AC9| service-linked role doesn't exist in your AWS account.

**Recommended solutions:** Create an |AC9| service-linked role in your AWS account by running the following command with the |clilong| (|cli|) or the aws-shell.

.. code-block:: sh

   aws iam create-service-linked-role --aws-service-name cloud9.amazonaws.com # For the AWS CLI.
   iam create-service-linked-role --aws-service-name cloud9.amazonaws.com     # For the aws-shell.

If you cannot do this, check with your AWS account administrator.

After you run this command, try creating the |env| again.

.. _troubleshooting-access-not-authorized:

Console Error: "User is not authorized to perform action on resource"
=====================================================================

**Issue:** When you try to use the |AC9| console to create or manage an |envfirst|, you see an error that contains the phrase 
"User arn:aws:iam::123456789012:user/MyUser is not authorized to perform cloud9:action on resource arn:aws:cloud9:us-east-2:123456789012:environment:12a34567b8cd9012345ef67abcd890e1," where:

* :code:`arn:aws:iam::123456789012:user/MyUser` is the Amazon Resource Name (ARN) of the requesting user.
* :code:`action` is the name of the operation that the user requested.
* :code:`arn:aws:cloud9:us-east-2:123456789012:environment:12a34567b8cd9012345ef67abcd890e1` is the ARN of the |env| that the user requested to run the operation.

**Cause:** The |IAM| user you signed in to the |AC9| console with doesn't have the correct AWS access
permissions to perform the action.

**Solution:** Ensure the |IAM| user has the correct AWS access permissions, and then try to perform the
action again. For more information, see the following:

* :ref:`setup-give-user-access` in *Team Setup*
* :ref:`share-environment-member-roles` in *Working with Shared Environments*

.. _troubleshooting-federated-service-role:

Federated Identities Cannot Create |envtitleplural|
===================================================

**Issue:** When you try to use an AWS federated identity to create an |envfirst|, an access error message is displayed, and the environment isn't created.

**Cause:** : |AC9| uses service-linked roles. The service-linked role is created the first time an |env| is created in an account using the :code:`iam:CreateServiceLinkedRole` call.
However, federated users can't call |IAM| APIs. For more information, see :STS-api:`GetFederationToken <API_GetFederationToken>` in the |STS-api|.

**Solution:** Ask an AWS account administrator to create the service-linked role for |AC9| either in the |IAM| console or by running this command with the |clilong| (|cli|):

.. code-block:: sh 

   aws iam create-service-linked-role --aws-service-name cloud9.amazonaws.com

Or this command with the aws-shell: 

.. code-block:: sh 

   iam create-service-linked-role --aws-service-name cloud9.amazonaws.com
   
For more information, see :IAM-ug:`Using Service-Linked Roles <using-service-linked-roles>` in the |IAM-ug|.

.. _troubleshooting-env-loading:

Cannot Open an |envtitle|
=========================

**Issue:** When you try to open an |env|, the |IDE| does not display for a long time (after at least five minutes).

**Possible causes:**

* Your web browser does not have third-party cookies enabled.
* The |IAM| user that is signed in to the |AC9| console does not have the required AWS access permissions to open the |env|.
* If the |env| is associated with an AWS cloud compute instance (for example an |EC2| instance), the instance's associated VPC is not set to the correct settings for |AC9|.
* If the |env| is associated with an AWS cloud compute instance, the instance is transitioning between states or is failing automated status checks, during the time when |AC9| is trying to connect to the instance.
* If the |env| is an |envssh|, the associated cloud compute instance or your own server is not set up correctly to allow |AC9| to access it.

**Recommended solutions:**

* Enable third-party cookies in your web browser, and then try opening the |env| again. To enable third-party cookies:

  * For Apple Safari, see `Manage cookies and website data in Safari <https://support.apple.com/guide/safari/manage-cookies-and-website-data-sfri11471/mac>`_ on the Apple Support website.
  * For Google Chrome, see **Change your cookie settings** in `Clear, enable, and manage cookies in Chrome <https://support.google.com/chrome/answer/95647>`_ on the Google Chrome Help website.
  * For Internet Explorer, see **To block or allow all cookies** in `Description of Cookies <https://support.microsoft.com/help/260971/description-of-cookies>`_ on the Microsoft Support website.
  * For Mozilla Firefox, see the **Accept third party cookies** setting in `Enable and disable cookies that websites use to track your preferences <https://support.mozilla.org/kb/enable-and-disable-cookies-website-preferences>`_ on the Mozilla Support website.
  * For other web browsers, see their web browser's documentation.

  If you want to restrict enabling third-party cookies only for |AC9| and your web browser allows this, specify the following domains, depending on the supported AWS Regions where
  you want to use |AC9|.

  .. list-table::
     :widths: 1 2
     :header-rows: 1

     * - **AWS Region**
       - **Domains**
     * - Asia Pacific (Singapore)
       - :code:`*.vfs.cloud9.ap-southeast-1.amazonaws.com`

         :code:`vfs.cloud9.ap-southeast-1.amazonaws.com`
     * - EU (Ireland)
       - :code:`*.vfs.cloud9.eu-west-1.amazonaws.com`

         :code:`vfs.cloud9.eu-west-1.amazonaws.com`
     * - US East (N. Virginia)
       - :code:`*.vfs.cloud9.us-east-1.amazonaws.com`

         :code:`vfs.cloud9.us-east-1.amazonaws.com`
     * - US East (Ohio)
       - :code:`*.vfs.cloud9.us-east-2.amazonaws.com`

         :code:`vfs.cloud9.us-east-2.amazonaws.com`
     * - US West (Oregon)
       - :code:`*.vfs.cloud9.us-west-2.amazonaws.com`

         :code:`vfs.cloud9.us-west-2.amazonaws.com`

* Make sure the |IAM| user that is signed in to the |AC9| console has the required AWS access permissions to open the |env|, and then try opening the |env| again. For more information see the following,
  or check with your AWS account administrator:

  * :ref:`Step 3: Add AWS Cloud9 Access Permissions to the Group <setup-give-user-access>` in *Team Setup*
  * :ref:`AWS Managed (Predefined) Policies for AWS Cloud9 <auth-and-access-control-managed-policies>` in *Authentication and Access Control*
  * :ref:`Customer-Managed Policy Examples for Teams <setup-teams-policy-examples>` in *Advanced Team Setup*
  * :ref:`Customer-Managed Policy Examples <auth-and-access-control-customer-policies-examples>` in *Authentication and Access Control*
  * :IAM-ug:`Changing Permissions for an IAM User <id_users_change-permissions>` in the |IAM-ug|
  * :IAM-ug:`Troubleshoot IAM Policies <troubleshoot_policies>` in the |IAM-ug|

  If the signed-in |IAM| user still cannot open the |env|, you could try signing out and then signing back in as either the AWS account root user or an |IAM| administrator user in the account. Then try opening
  the |env| again. If you are able to open the |env| in this way, then there is most likely a problem with the |IAM| user's access permissions.

* If the |env| is associated with an AWS cloud compute instance (for example an |EC2| instance), make sure the instance's associated VPC is set to the correct settings for |AC9|, and then try opening the |env| again. For details, see
  :ref:`vpc-settings-requirements`.

  If the AWS cloud compute instance's associated VPC is set to the correct settings for |AC9| and you still cannot open the |env|, the instance's security group might be preventing access to |AC9|. Check the security group
  to make sure that at minimum, inbound SSH traffic is allowed over port 22 for all IP addresses (:code:`Anywhere` or :code:`0.0.0.0/0`). For instructions,
  see :ec2-user-guide:`Describing Your Security Groups <using-network-security.html#describing-security-group>` and
  :ec2-user-guide:`Updating Security Group Rules <using-network-security.html#updating-security-group-rules>` in the |EC2-ug|.

  For additional VPC troubleshooting steps, watch the related 5-minute video 
  `AWS Knowledge Center Videos: What can I check if I cannot connect to an instance in a VPC? <https://www.youtube.com/watch?v=--BoDeCF5Dw>`_ on the YouTube website. 

* If the |env| is associated with an AWS cloud compute instance, restart the instance, make sure the instance is running and has passed all system checks, and then try opening the |env| again.
  For details, see :EC2-ug:`Reboot Your Instance <ec2-instance-reboot>` and :ec2-user-guide:`Viewing Status Checks <monitoring-system-instance-status-check.html#viewing_status>` in the |EC2-ug|.
* If the |env| is an |envssh|, make sure the associated cloud compute instance or your own server is set up correctly to allow |AC9| to access it, and then try opening the |env| again.
  For details, see :ref:`SSH Environment Host Requirements <ssh-settings>`.

.. _troubleshooting-ssh-installer:

The |AC9| Installer Hangs or Fails
==================================

**Issue:** When you open an |envfirstssh|, you are prompted to run the :guilabel:`AWS Cloud9 Installer`. When you try to run it, it either hangs or displays errors, and you cannot use the |AC9IDE| for
the |env| as expected. (In some cases, a message might display before you are prompted to run the :guilabel:`AWS Cloud9 Installer`. The message states that opening the |env| is taking longer than expected.)

**Cause:** The :guilabel:`AWS Cloud9 Installer` cannot run a required setup script to properly set up the |env|.

**Solution:** Manually run the :file:`install.sh` script that the :guilabel:`AWS Cloud9 Installer` unsuccessfully tried to run, as follows:

#. Close the web browser tab for the |env|, which stops the :guilabel:`AWS Cloud9 Installer`.
#. Connect to the cloud compute instance or your own server using an SSH connection client outside of |AC9|, for example by using the :code:`ssh` command or PuTTY.
#. Run one of the following commands on the cloud compute instance or your own server:

   .. code-block:: sh

      curl -L https://raw.githubusercontent.com/c9/install/master/install.sh | bash
      wget -O - https://raw.githubusercontent.com/c9/install/master/install.sh | bash

#. Try opening the |env| again. You might be prompted to run the :guilabel:`AWS Cloud9 Installer` again. When you try to run it this time though, it should run without hangs or errors.
   However, depending on your Linux distribution and build, you might need to repeat this process to successfully set up the |env|.

.. _troubleshooting-python-ssh:

|envsshtitle| Error: "Python version 2.7 is required to install pty.js"
=======================================================================

**Issue:** After you open an |envfirstssh|, the terminal in the |AC9IDE| displays a message that begins with "Python version 2.7 is required to install pty.js."

**Cause:** To work as expected, an |envssh| requires that Python version 2.7 is installed.

**Solution:** Install Python version 2.7 in the |env|. To check your version,
from your server's terminal, run the command :command:`python --version`. To install Python 2.7 on your server,
see one of the following:

* :ref:`sample-python-install` in the :title:`Python Sample`.
* `Download Python <https://www.python.org/downloads/>`_ on the Python website and `Installing Packages <https://packaging.python.org/installing/>`_
  in the :title:`Python Packaging User Guide`.

.. _troubleshooting-app-preview:

Application Preview Tab Displays an Error or is Blank
=========================================================

**Issue:** On the menu bar in the |IDE|, when you choose :guilabel:`Preview, Preview Running Application` or :guilabel:`Tools, Preview, Preview Running Application`
to try to display your application in a preview tab in the |IDE|, the tab displays an error, or the tab is blank.

**Possible causes:**

* Your application is not running in the |IDE|.
* Your application is not running using HTTP.
* Your application is running over more than one port.
* Your application is running over a port other than :code:`8080`, :code:`8081`, or :code:`8082`.
* Your application is running with an IP other than :code:`127.0.0.1`, :code:`localhost`, or :code:`0.0.0.0`.
* The port (:code:`8080`, :code:`8081`, or :code:`8082`) is not specified in the URL on the preview tab.
* Your network blocks inbound traffic to ports :code:`8080`, :code:`8081`, or :code:`8082`.
* You are trying to go to an address that contains an IP 
  of :code:`127.0.0.1`, :code:`localhost`, or :code:`0.0.0.0`. The default built-in behavior of the |AC9IDE| 
  is that this will attempt to go to your local computer, instead of attempting to go the instance or your own server that is connected to the |env|.

**Recommended solutions:**

* Ensure that the application is running in the |IDE|.
* Ensure that the application is running using HTTP. For some examples in Node.js and Python, see :ref:`Run an Application <app-preview-run-app>`.
* Ensure that the application is running over only one port. For some examples in Node.js and Python, see :ref:`Run an Application <app-preview-run-app>`.
* Ensure that the application is running over port :code:`8080`, :code:`8081`, or :code:`8082`. For some examples in Node.js and Python, see :ref:`Run an Application <app-preview-run-app>`.
* Ensure that the application is running with an IP of :code:`127.0.0.1`, :code:`localhost`, or :code:`0.0.0.0`. For some examples in Node.js and Python, see :ref:`Run an Application <app-preview-run-app>`.
* Add :code:`:8080`, :code:`:8081`, or :code:`:8082` to the URL on the preview tab.
* Ensure that your network allows inbound traffic over ports :code:`8080`, :code:`8081`, or :code:`8082`. If you cannot make changes to your network, see your network administrator. 
* If you are trying to go to an address that contains an IP of :code:`127.0.0.1`, :code:`localhost`, or :code:`0.0.0.0`, try going to the following address instead: 
  :code:`https://12a34567b8cd9012345ef67abcd890e1.vfs.cloud9.us-east-2.amazonaws.com/`, where :code:`12a34567b8cd9012345ef67abcd890e1` is the ID that |AC9| assigns to the |env|, 
  and :code:`us-east-2` is the ID of the AWS Region for the |env|. Note that you can also try to go to this address outside of the |IDE|, but it works 
  only when the |IDE| for the |env| is open and the application is running in the same web browser. 
* After you are sure that all of the preceding conditions are met, try stopping the application and then starting it again.
* If you stopped the application and then started it again, try choosing :guilabel:`Preview, Preview Running Application` or :guilabel:`Tools, Preview, Preview Running Application`
  on the menu bar again. Or try choosing the :guilabel:`Refresh` button (the circular arrow) on the corresponding application preview tab, if the tab is already visible.

.. _troubleshooting-app-sharing:

Cannot Display Your Running Application Outside of the |IDE|
============================================================

**Issue:** When you or others try to display your running application in a web browser tab outside of the |IDE|, that web browser tab displays an error, or the tab is blank.

**Possible causes:**

* The application is not running in the |IDE|.
* The application is running with an IP of :code:`127.0.0.1` or :code:`localhost`.
* The application is running in an |envfirstlongec2|, and one or more security groups that are associated with the corresponding |EC2| instance do not allow inbound traffic over the protocols,
  ports, or IP addresses that the application requires.
* The application is running in an |envfirstlongssh| for an AWS cloud compute instance (for example an |EC2| instance), and the network ACL for the subnet in the virtual private cloud (VPC) that is 
  associated with the corresponding instance does not allow inbound traffic over the 
  protocols, ports, or IP addresses that the application requires.
* The URL is incorrect.
* The URL in the application preview tab is being requested instead of the instance's public IP address.
* You are trying to go to an address that contains an IP 
  of :code:`127.0.0.1` or :code:`localhost`. These IPs will attempt to access resources on your local computer instead of resources in the |env|.
* The instance's public IP address has changed.
* The web request originates from a virtual private network (VPN) that blocks traffic over the protocols, ports, or IP addresses that the application requires.
* The application is running in an |envssh|, and your server or the associated network does not allow traffic over the protocols, ports, or IP addresses that the application requires.

**Recommended solutions:**

* Ensure that the application is running in the |IDE|.
* Ensure that the application is not running with an IP of :code:`127.0.0.1` or :code:`localhost`. For some examples in Node.js and Python, see :ref:`Run an Application <app-preview-run-app>`.
* If the application is running on an AWS cloud compute instance (for example an |EC2| instance), ensure all security groups that are associated with the corresponding instance allow inbound traffic over the protocols, ports,
  and IP addresses that the application requires. For instructions, see :ref:`app-preview-share-security-group` in
  *Share a Running Application over the Internet*. See also :VPC-ug:`Security Groups for Your VPC <VPC_SecurityGroups>` in the |VPC-ug|.
* If the application is running on an AWS cloud compute instance, and a network ACL exists for the subnet in the VPC that is associated with the corresponding instance, ensure that
  network ACL allows inbound traffic over the protocols, ports, and IP addresses that the application requires. For instructions, see
  :ref:`app-preview-share-subnet` in *Share a Running Application over the Internet*. See also :VPC-ug:`Network ACLs <VPC_ACLs>` in the |VPC-ug|.
* Ensure that the requesting URL, including the protocol (and port, if it must be specified), is correct. For more information, see
  :ref:`app-preview-share-url` in *Share a Running Application over the Internet*.
* We do not recommend requesting a URL with the format :code:`https://12a34567b8cd9012345ef67abcd890e1.vfs.cloud9.us-east-2.amazonaws.com/` (where :code:`12a34567b8cd9012345ef67abcd890e1` is the ID 
  that |AC9| assigns to the |env|, and :code:`us-east-2` is the ID of the AWS Region for the |env|). This URL works only when the |IDE| for the |env| is open and the
  application is running in the same web browser.
* If you are trying to go to an address that contains an IP of :code:`127.0.0.1` or :code:`localhost`, try going to the correct non-local address for the running application instead. For more 
  information, see :ref:`app-preview-share`.
* If the application is running on an AWS cloud compute instance, determine whether the instance's public IP address has changed. The instance's public IP address might change anytime the instance restarts. To prevent this IP address from changing,
  you can allocate an Elastic IP address and assign it to the running instance. For more information, see :ref:`app-preview-share-url` in *Share a Running Application over the Internet*.
* If the web request originates from a VPN, ensure that VPN allows traffic over the protocols, ports, and IP addresses that the application requires.
  If you cannot make changes to your VPN, see your network administrator. Or make the web request from a different network if possible.
* If the application is running in an |envssh| for your own server, ensure your server and the associated network allow traffic over the protocols, ports, and IP addresses that the
  application requires. If you cannot make changes to your server or the associated network, see your server or network administrator.
* Try running the application from a terminal in the |env| by running the :code:`curl` command, followed by the URL. If this command displays an error message, there might be some other issue that is not related
  to |AC9|.

.. _troubleshooting-app-preview-refresh:

After Reloading an |envtitle|, You Must Refresh Application Preview
===================================================================

**Issue:** After you reload an |env| that displays an application preview tab, the tab doesn't display the application preview.

**Cause:** Sometimes users write code that can run an infinite loop or that otherwise uses so much memory
that the |AC9IDE| can pause or stop when the
application preview is running. To keep this from happening, |AC9| doesn't reload application preview
tabs whenever an |env| is reloaded.

**Solution:** After you reload an |env| that displays an application preview tab, to display the application
preview, choose the
:guilabel:`Click to load the page` button on the tab.

.. _troubleshooting-app-preview-http:

Unable to Preview Application in the |AC9IDE| with HTTP
=======================================================

**Issue:** In the address box of an application preview tab in the |AC9IDE|, the URL always starts with :code:`https`. If you try to change
:code:`https` in the box to :code:`http` and then press :kbd:`Enter`, the tab doesn't display the application
preview.

**Cause:** To help improve code safety, in the address box of the application preview tab in the |IDE|, |AC9| always uses :code:`https`. This behavior cannot be changed.

**Solution:** To view an application preview with an address starting with :code:`http` instead of :code:`https`, change
:code:`https` in the address box of the tab to :code:`http` and then press :kbd:`Enter`. Then choose the :code:`Open your page in a new tab` button. This
displays the application preview in a separate web browser tab using HTTP.

.. _troubleshooting-rhel:

Cannot Run Some Commands or Scripts in an |envec2title|
=======================================================

**Issue:** After you open an |envfirstlongec2|, you cannot install some types of packages, run commands such as :code:`apt`, or run scripts containing commands
that typically work with Linux operating systems such as Ubuntu.

**Cause:** The |EC2| instance that |AC9| uses for an |envec2| relies on Amazon Linux, which is based on Red Hat Enterprise Linux (RHEL).

**Solution:** If you install or manage packages or run commands or scripts in the |IDE| for an |envec2|,
ensure they are compatible with RHEL.

.. _troubleshooting-cli-invalid-token:

|cli| / aws-shell Error: "The security token included in the request is invalid" in an |envec2|
===============================================================================================

**Issue:** When you try to use the |clilong| (|cli|) or the aws-shell to run a command in the |AC9IDE| for an |envec2|, an error displays: "The security token included in the request is invalid."

**Possible causes:**

* If you have |AC9tempcreds| enabled, you are trying to run a command that is not allowed with those |tempcreds|. For a list of allowed commands, see :ref:`auth-and-access-control-temporary-managed-credentials-supported`.
* If you have |AC9tempcreds| enabled and the |env| is a shared |env|, the |env| owner has not opened the |env| within the past 12 hours so that |AC9| can refresh |AC9tempcreds| in the |env|.
  (|AC9| sets this 12-hour limit as an AWS security best practice.)

**Recommended solutions:**

* If you have |AC9tempcreds| enabled, run allowed commands only. If you must run a command that is not allowed by |AC9tempcreds|, one approach would be to configure the
  |cli| or aws-shell in the |env| with a set of permanent credentials, which removes this limitation. For instructions, see :ref:`credentials-permanent-create`.
* Have the |env| owner open the |env| so that |AC9| can refresh temporary credentials in the |env|.

For more information, see :ref:`auth-and-access-control-temporary-managed-credentials`.

.. _troubleshooting-update-ami:

|EC2| Instances Are Not Automatically Updated
=============================================

**Issue:** Recent system updates are not automatically applied to an |EC2| instance that connects to an |envfirst|.

**Cause:** Automatically applying recent system updates could cause your code or the |EC2| instance to behave in unexpected ways, without your prior knowledge or approval.

**Recommended solutions:**

Apply system updates to the |EC2| instance on a regular basis by following the instructions in :EC2-ug:`Updating Instance Software <install-updates>` in the |EC2-ug|.

To run commands on the instance, you can use a terminal session in the |AC9IDE| from the |env| that is connected to the instance.

Alternatively, you can use an SSH remote access utility such as **ssh** or PuTTY to connect to the instance. To do this, from your local computer, use an SSH key pair
creation utility such as **ssh-keygen** or PuTTYgen. Use the |AC9IDE| from the |env| that is connected to the instance to store the generated public key on the instance.
Then use the SSH remote access utility along with the generate private key to access the instance. For more information, see your utility's documentation.

.. _troubleshooting-install-sam-local:

Lambda Local Function Run Error: Cannot Install SAM Local
=========================================================

**Issue:** After you try to run the local version of an |LAMlong| function in the |AC9IDE|, a dialog box is displayed, stating that |AC9| is having trouble installing SAM Local.
|AC9| needs SAM Local to run local versions of |LAMlong| functions in the |IDE|. Until SAM Local is installed, you cannot run local versions of
|LAM| functions in the |IDE|.

**Cause:** AWS Cloud9 can't find SAM Local at the expected path in the |env|, which is :file:`~/.c9/bin/sam`. This is because SAM Local is not yet
installed, or if it is installed, |AC9| can't find it at that location.

**Recommended solutions:** You can wait for |AC9| to try to finish installing SAM Local, or you can install it yourself.

To see how |AC9| is doing with attempting to install SAM Local, choose :guilabel:`Window, Installer` on the menu bar.

To install SAM Local yourself, run the following commands, one at a time in the following order, from a terminal session in the |IDE|.

.. code-block:: sh

   npm install -g aws-sam-local        # Use Node Package Manager (npm) to install SAM Local as a global package in the environment.
   ln -sfn $(which sam) ~/.c9/bin/sam  # Create a symbolic link (a shortcut) from the path that AWS Cloud9 expects to where SAM Local is installed.

For more information, see the `awslabs/aws-sam-cli <https://github.com/awslabs/aws-sam-cli/blob/develop/README.rst>`_ repository on the GitHub website.

.. _troubleshooting_ide_low_memory:

|IDE| Warning: "This |envtitle| is Running Low on Memory" or "This |envtitle| Has High CPU Load"
================================================================================================

**Issue:** While the |IDE| is running, you see a message that contains the phrase "this |env| is running low on memory" or 
"this |env| has high CPU load."

**Cause:** The |IDE| might not have enough compute resources available to continue running without delays or hangs.

**Recommended solutions:**

* Stop one or more running processes to free up available memory. To do this, on the menu bar in the |IDE| for the |env|, 
  choose :guilabel:`Tools, Process List`. For each process you want to stop, choose the process, and then choose :guilabel:`Force Kill`. 
* Create a swap file in the |env|. A :dfn:`swap file` is a file in the |env| that the operating system can use as virtual memory.

  To confirm whether the |env| is currently using swap memory, run the :command:`top` command in a terminal session in the |env|. If swap memory is being used, 
  the output displays non-zero :code:`Swap` memory statistics (for example, :code:`Swap: 499996k total, 1280k used, 498716 free, 110672k cached`). To stop showing real-time 
  memory information, press :kbd:`Ctrl + C`.

  To create a swap file, you could run a command such as the following in the |env|.

  .. code-block:: sh 

     sudo fallocate --length 512MB /var/swapfile && sudo chmod 600 /var/swapfile && sudo mkswp /var/swapfile && echo '/var/swapfile swap swap defaults 0 0' | sudo tee -a /etc/fstab > /dev/null

  The preceding command does the following: 

  #. Creates a 512 MB file named :file:`swapfile` in the :file:`/var` directory.
  #. Changes access permissions for the :file:`swapfile` file to read-write for the owner only. 
  #. Sets up the :file:`swapfile` file as a swap file.
  #. Writes information to the :file:`/etc/fstab file`, which makes this swap file available whenever the system reboots.

  After you run the preceding command, to make this swap file available immediately instead of waiting for a reboot, run the following command.

  .. code-block:: sh 

     sudo swapon /var/swapfile

* Move or resize the |env| to an instance or server with more compute resources. To move or resize |EC2| instances, see 
  :ref:`Moving or Resizing and Environment <move-environment>`. For other instance or server types, refer to your 
  instance's or server's documentation.

.. Troubleshooting template

   .. _troubleshooting_title:

   Issue Title
   ===========

   **Issue:**

   **Possible causes:**

   **Recommended solutions:**
