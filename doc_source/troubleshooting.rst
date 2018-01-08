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
* :ref:`troubleshooting-python-ssh`
* :ref:`troubleshooting-rhel`
* :ref:`troubleshooting-update-ami`
* :ref:`troubleshooting-app-preview-refresh`
* :ref:`troubleshooting-app-preview-http`

.. _troubleshooting-sts-assume-role:

Error: "Not authorized to perform sts:AssumeRole" When Creating an |envfirsttitle|
===================================================================================

**Issue:** When you try to create a new |env|, you see this error: "Not authorized to perform
sts:AssumeRole," and the |env| is not created.

**Possible causes:** An |AC9| service-linked role doesn't exist in your AWS account.

**Recommended solutions:** Create an |AC9| service-linked role in your AWS account by running the following command with the |CLIlong| (|CLI|).

.. code-block:: sh

   aws iam create-service-linked-role --aws-service-name cloud9.amazonaws.com

If you cannot do this, check with your AWS account administrator.

After you run this command, try creating the |env| again. 

.. _troubleshooting-access-not-authorized:

Error: "User is not authorized to perform action on resource" When Using the |AC9| Console
==========================================================================================

**Issue:** When you try to use the |AC9| console to create or manage an |envfirst|, you see this error: "User USER-ARN is not authorized to perform ACTION on resource RESOURCE-ARN," where:

* :samp:`{USER-ARN}` is the Amazon Resource Name (ARN) of the |IAM| user that tried to access the resource.
* :samp:`{ACTION}` is the AWS action the |IAM| user tried to perform.
* :samp:`{RESOURCE-ARN}` is the ARN of the AWS resource that the |IAM| user tried to access.

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

**Solution:** Ask an AWS account administrator to create the service-linked role for |AC9| either in the |IAM| console or by running the command 
:code:`aws iam create-service-linked-role --aws-service-name cloud9.amazonaws.com` from the |CLIlong| (|CLI|). For more information, see 
:IAM-ug:`Using Service-Linked Roles <using-service-linked-roles>` in the |IAM-ug|.

.. _troubleshooting-env-loading:

|envtitle| Loading Screen Displays for a Long Time
==================================================

**Issue:** When you try to open an |env|, the |IDE| does not display after five minutes or longer. 

**Possible cause:** Your web browser does not have third-party cookies enabled. 

**Recommended solution:** Enable third-party cookies in your web browser, and then try opening the environment again. To enable third-party cookies: 
 
*	For Apple Safari, see `Manage cookies and website data using Safari <https://support.apple.com/kb/PH21411>`_ on the Apple Support website.
*	For Google Chrome, see **Change your cookie settings** in `Clear, enable, and manage cookies in Chrome <https://support.google.com/chrome/answer/95647>`_ on the Google Chrome Help website. 
*	For Internet Explorer, see **To block or allow all cookies** in `Description of Cookies <https://support.microsoft.com/help/260971/description-of-cookies>`_ on the Microsoft Support website.
*	For Mozilla Firefox, see the **Accept third party cookies** setting in `Enable and disable cookies that websites use to track your preferences <https://support.mozilla.org/kb/enable-and-disable-cookies-website-preferences>`_ on the Mozilla Support website.
*	For other web browsers, see their web browser's documentation.

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

.. _troubleshooting-rhel:

Cannot Run Some Commands or Scripts in an |envec2title|
=======================================================

**Issue:** After you open an |envfirstlongec2|, you cannot install some types of packages, run commands such as :code:`apt`, or run scripts containing commands
that typically work with Linux operating systems such as Ubuntu.

**Cause:** The |EC2| instance that |AC9| uses for an |envec2| relies on Amazon Linux, which is based on Red Hat Enterprise Linux (RHEL).

**Solution:** If you install or manage packages or run commands or scripts in the |IDE| for an |envec2|,
ensure they are compatible with RHEL.

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

.. Troubleshooting template

   .. _troubleshooting_title:

   Issue Title
   ===========

   **Issue:**

   **Possible causes:**

   **Recommended solutions:**
