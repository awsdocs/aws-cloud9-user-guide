.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _lambda-functions:

#########################################################
Working with |LAMlong| Functions in the |AC9IDElongtitle|
#########################################################

.. meta::
    :description:
        Describes how to work with AWS Lambda functions in the AWS Cloud9 IDE.

You can use the |AC9IDE| to work with |LAMlong| functions and their related |ABPlong| APIs in an |envfirst|. For example, you can:

* Create a new function from within your |env|, uploading the local version of the function to |LAM|, and optionally creating additional AWS resources to support the new function at the same time.
* Run and debug a function and its related API in your |env|, running the function and API completely within the |env|.
* Run the remote version of a function and its related API within your |env|, running the remote version completely within |LAM| and |ABP|.
* Import an existing function in |LAM| into your |env|, so that you can run and debug the function and its related API, edit the code, or both.
* Upload changes you make to the local version of the function code to the remote version in |LAM|.

This topic assumes you already know about |LAM|. For more information, see the |LAM-dg|_.

.. note:: Completing these procedures might result in charges to your AWS account. These include possible charges for services such as |LAM|, |ABP|, and AWS services supported by the 
   AWS Serverless Application Model (SAM). For more information, see `AWS Lambda Pricing <https://aws.amazon.com/lambda/pricing/>`_, `Amazon API Gateway Pricing <https://aws.amazon.com/api-gateway/pricing/>`_, and 
   `Cloud Services Pricing <https://aws.amazon.com/pricing/services/>`_.

* :ref:`lambda-functions-prepare`
* :ref:`lambda-functions-create`
* :ref:`lambda-functions-import`
* :ref:`lambda-functions-invoke`
* :ref:`lambda-functions-api`
* :ref:`lambda-functions-vs-api-gateway`
* :ref:`lambda-functions-debug`
* :ref:`lambda-functions-change-code`
* :ref:`lambda-functions-upload-code`
* :ref:`lambda-functions-convert-to-sam`
* :ref:`lambda-functions-update-settings`

.. _lambda-functions-prepare:

Prepare to Work with |LAM| Functions
====================================

Before you can work with |LAM| functions in the |AC9IDE|, you must complete the following steps:

* :ref:`lambda-functions-prepare-user`
* :ref:`lambda-functions-prepare-access`
* :ref:`lambda-functions-prepare-role`
* :ref:`lambda-functions-prepare-region`
* :ref:`lambda-functions-prepare-open`

.. _lambda-functions-prepare-user:

Step 1: Set Up Your |IAM| Group with Required Access Permissions
-----------------------------------------------------------------

If your AWS access credentials are associated with an |IAM| administrator user in your AWS account, and you want to use that user to work with |LAM| functions, skip ahead to :ref:`lambda-functions-prepare-access`.

Otherwise, complete the following instructions to:

* Use the |IAM| console to attach the AWS managed policies named :code:`AWSLambdaFullAccess`, :code:`AmazonAPIGatewayAdministrator`, and :code:`AmazonAPIGatewayInvokeFullAccess` to an |IAM| group to which your user belongs.
* Use the |CFNlong| console to attach an additional inline policy to that group.

#. Sign in to the AWS Management Console, if you're not already signed in.

   For this step, we recommend you sign in using credentials for an |IAM| administrator in your AWS account. If you can't
   do this, check with your AWS account administrator.

#. Open the |IAM| console. To do this, in the console's navigation bar, choose :guilabel:`Services`. Then choose :guilabel:`IAM`.
#. Choose :guilabel:`Groups`.
#. Choose the group's name.
#. On the :guilabel:`Permissions` tab, for :guilabel:`Managed Policies`, choose :guilabel:`Attach Policy`.
#. In the list of policy names, choose the boxes next to :guilabel:`AWSLambdaFullAccess`, :guilabel:`AmazonAPIGatewayAdministrator`, 
   and :guilabel:`AmazonAPIGatewayInvokeFullAccess`.
   (If you don't see any of these policy names in the list, type the policy name in
   the :guilabel:`Search` box to display it.)
#. Choose :guilabel:`Attach Policy`.
#. Open the |CFN| console. To do this, in the console's navigation bar, choose :guilabel:`Services`. Then choose :guilabel:`CloudFormation`.
#. Choose :guilabel:`Create Stack`.
#. On the :guilabel:`Select Template` page, for :guilabel:`Choose a template`, choose :guilabel:`Specify an Amazon S3 template URL`. In the box,
   type or paste one of the following URL to the |CFN| template.

   .. code-block:: text

      https://s3.amazonaws.com/cloud9-cfn-templates/Cloud9LambdaAccessGroup.yaml

#. Choose :guilabel:`Next`.
#. On the :guilabel:`Specify Details` page, for :guilabel:`Stack name`, type a name for the stack, for example :code:`AWSCloud9LambdaAccessStack`.
   If you type a different name, replace it throughout this procedure.
#. For :guilabel:`Parameters`, for :guilabel:`GroupName`, type the name of the existing group in your AWS account you want to attach the access policy to.
#. Choose :guilabel:`Next`.
#. On the :guilabel:`Options` page, choose :guilabel:`Next`. (Do not change any of the default settings on the :guilabel:`Options` page.)
#. On the :guilabel:`Review` page, choose :guilabel:`I acknowledge that AWS CloudFormation might create IAM resources`.
#. Choose :guilabel:`Create`.

Wait until the :guilabel:`AWSCloud9LambdaAccessStack` stack shows :guilabel:`CREATE_COMPLETE`. This might take a few moments. Please be patient.

.. note:: The access policy that |CFN| attaches to the group is named :code:`AWSCloud9LambdaGroupAccess` and has the following definition, where :samp:`{ACCOUNT_ID}` is your 
   AWS account ID.

   .. code-block:: json

      {
        "Version": "2012-10-17",
        "Statement": [
          {
            "Action": [
              "cloudformation:CreateChangeSet",
              "cloudformation:CreateStack",
              "cloudformation:DescribeChangeSet",
              "cloudformation:DescribeStackEvents",
              "cloudformation:DescribeStacks",
              "cloudformation:ExecuteChangeSet",
              "cloudformation:ListStackResources",
              "cloudformation:UpdateStack",
              "iam:AttachRolePolicy",
              "iam:DetachRolePolicy",
              "iam:GetRole",
              "iam:GetUser",
              "iam:PassRole"
            ],
            "Resource": "*",
            "Effect": "Allow"
          },
          {
            "Action": [
              "iam:CreateRole",
              "iam:DeleteRole"
            ],
            "Resource": "arn:aws:iam::ACCOUNT_ID:role/cloud9-*",
            "Effect": "Allow"
          }
        ]
      }

.. _lambda-functions-prepare-access:

Step 2: Set Up Your |envtitle| with Your AWS Access Credentials
---------------------------------------------------------------

The |AC9IDE| uses the |clilong| (|cli|) in your |envfirst| to interact with |LAM| and other supporting AWS services. Therefore, the |cli| in your |env|
needs access to your AWS access credentials.

Do one of the following to set up the |cli| in your |env|:

* If you have an |envec2|, |AC9tempcreds| are already set up in your |env| for the |cli| to use, and you can skip ahead to :ref:`lambda-functions-prepare-role`. |AC9tempcreds| have permission to
  interact with most AWS services from your |env| (provided the AWS entity that is using the |env| also has those permissions). For more information, see
  :ref:`auth-and-access-control-temporary-managed-credentials`.
* If you have an |envec2| but |AC9tempcreds| don't meet your needs, you can attach an |IAM| instance profile
  to the |EC2| instance that connects to your |env|. Or you can
  store your permanent AWS access credentials within the |env|. For instructions, see :ref:`credentials-temporary` or :ref:`credentials-permanent-create`.
* If you have an |envssh|, you can store your permanent AWS access credentials within the |env|.
  For instructions, see :ref:`credentials-permanent-create`.

.. _lambda-functions-prepare-role:

Step 3: Create an Execution Role for Your |LAM| Functions
---------------------------------------------------------

If you want your |LAM| functions to do things usings AWS resources, you must specify
an |IAM| role (execution role) that contains the necessary access permissions for your functions to use.

When you create a |LAM| function, |AC9| can create an execution role for you. This execution role contains the permissions as described in
:lambda-dev-guide:`Basic Lambda Permissions <policy-templates.html#basic-execution>` in the |LAM-dg|.

If this execution role doesn't meet your needs, you must create an execution role on your own before you
create your |LAM| function. For more information, see the following:

* :LAM-dg:`AWS Lambda Permissions Model <intro-permission-model>` in the |LAM-dg|
* :IAM-ug:`Creating a Role to Delegate Permissions to an AWS Service <id_roles_create_for-service>` in the |IAM-ug|

.. _lambda-functions-prepare-region:

Step 4: Set Your |envtitle| to the Correct AWS Region
-----------------------------------------------------

You must set your |envfirst| to use the AWS Region where you want to create new |LAM| functions in your AWS account, or where you want to import existing |LAM| functions
from your AWS account into your |envfirst|.

To do this:

#. In the |AC9IDE|, on the menu bar, choose :guilabel:`AWS Cloud9, Preferences`.
#. In the navigation pane of the :guilabel:`Preferences` tab, choose :guilabel:`AWS Settings`.
#. For :guilabel:`AWS Region`, select the AWS Region you want to use.

.. _lambda-functions-prepare-open:

Step 5: Open the Lambda Section of the AWS Resources Window
-----------------------------------------------------------

Now you're ready to begin using the |AC9IDE| to work with |LAM| functions. To do this, expand the
:guilabel:`Lambda` section of the
:guilabel:`AWS Resources` window, if it isn't already expanded.

.. image:: images/console-lambda-menu.png
   :alt: AWS Resources window showing the Lambda section

If the :guilabel:`AWS Resources` window isn't visible, choose the :guilabel:`AWS Resources` button.

If you don't see the :guilabel:`AWS Resources` button, choose :guilabel:`Window, AWS Resources`
on the
menu bar to show it.

.. _lambda-functions-create:

Create a |LAM| Function
=======================

You can use the |AC9IDE| to create a new |LAM| function. If you already have a |LAM| function in your
AWS account for the AWS Region you set earlier, skip ahead to :ref:`lambda-functions-import`.

#. In the :guilabel:`Lambda` section of the :guilabel:`AWS Resources` window, choose where you want to create the function:

   * To create a single function by itself, choose the :guilabel:`Local Functions` heading.
   * To create a function and then add it to an existing group of one or more functions and related AWS
     resources (referred to as a :dfn:`serverless application`), in the
     :guilabel:`Local Functions` list, choose the serverless application for the group (represented by the |LAM| icon inside of a folder).

#. Do one of the following:

   * Choose :guilabel:`Create a new Lambda function` (the button with the |LAM| icon).
   * Right-click the :guilabel:`Local Functions` heading or the serverless application folder you chose earlier, and then choose :guilabel:`Create Here`.

   .. image:: images/console-lambda-create.png
      :alt: Creating a new Lambda function using the Lambda section of the AWS Resources window

#. In the :guilabel:`Create Serverless Application` dialog box, specify the following settings for the function:

   * :guilabel:`Function Name`: A name for the function.
   * :guilabel:`Application Name`: The name of the new serverless application to be associated with the new function.

#. Choose :guilabel:`Next`.
#. Choose the function blueprint you want to start with. (Currently, only
   Node.js and Python function blueprints are available.)

   To show blueprints for a specific runtime,
   for :guilabel:`Select Runtime`, choose the runtime. For example, to use the :code:`hello-world` function blueprint for Node.js 6.10, choose :guilabel:`Node.js 6.10`
   for :guilabel:`Select Runtime`, and then choose the :guilabel:`hello-world` blueprint for :guilabel:`Select Blueprint`.

#. Choose :guilabel:`Next`.
#. Do one of the following:

   * To skip having an AWS service automatically trigger this function, leave :guilabel:`Function Trigger` set to :guilabel:`none`, choose :guilabel:`Next`, and then skip ahead to step 9 in this procedure.
   * To have an AWS resource in your account automatically trigger your function, for :guilabel:`Function Trigger`, select the name of the AWS service that will contain the resource.
     (Currently, only :guilabel:`API Gateway` is available.)

#. If you chose :guilabel:`API Gateway` for :guilabel:`Function Trigger`, specify the following for :guilabel:`Trigger Settings`:

   * For :guilabel:`Resource Path`, type the URL portion of the API to use to invoke the function. For
     example, type :code:`/` to specify the resource root.
   * For :guilabel:`Security`, choose the security mechanism for the API endpoint:

     * :guilabel:`AWS_IAM`: Require that callers provide |IAM| access credentials to be authenticated.
       See
       :ABP-dg:`Control Access to API Gateway with IAM Permissions <permissions>` in the |ABP-dg|.
     * :guilabel:`NONE`: Enable open access.
     * :guilabel:`NONE_KEY`: Require that callers provide an API key to be authenticated. See
       :ABP-dg:`Set Up API Keys Using the API Gateway Console <api-gateway-setup-api-key-with-console>` in the |ABP-dg|.

#. Choose :guilabel:`Next`.
#. For :guilabel:`Memory (MB)`, choose the amount of memory, in megabytes, that this function will use.
#. Do one of the following:

   * To have |AC9| create a new, basic |IAM| role (execution role) for this function to use, for :guilabel:`Role`, choose :guilabel:`Automatically generate role`. Then choose :guilabel:`Next`.
   * To have |LAM| use an existing |IAM| role (execution role) in your AWS account, for :guilabel:`Role`, choose :guilabel:`Choose an existing role`. For :guilabel:`Existing Role`, choose the name of the role,
     and then choose :guilabel:`Next`.

#. Choose :guilabel:`Next`.
#. Choose :guilabel:`Finish`.

In the :guilabel:`Lambda` section of the :guilabel:`AWS Resources` window, |AC9| does the following:

* If you chose to create a single function by itself:

  #. |AC9| creates a serverless application with the name that you specified earlier. Then it adds a serverless
     application (represented by a |LAM| icon inside of a folder) to the
     :guilabel:`Local Functions` list. Then it adds the |LAM| function (represented by a |LAM| icon by
     itself), to this serverless application.
  #. |AC9| creates a remote version of the function in |LAM| and adds it to the :guilabel:`Remote Functions` list. |AC9| gives the remote version
     a different name. For example, if you named the serverless application :code:`myDemoServerlessApplication` and the function :code:`myDemoFunction`, the remote version
     name of your function would be
     :code:`cloud9-myDemoServerlessApplication-myDemoFunction-RANDOM_ID`,
     where :code:`RANDOM_ID` is a randomly determined ID.
  #. If you chose to have |ABP| automatically trigger the function, |AC9| creates an API in |ABP| with a name that corresponds to the function. For example, if you named the function :code:`myDemoFunction`,
     the API name would be :code:`cloud9-myDemoFunction`. |AC9| uses the value you specified
     in :guilabel:`Resource Path` to map the function to the API using the :code:`ANY` method.

* If you chose to create a single function and then add it to an existing serverless application:

  #. |AC9| adds the |LAM| function (represented by a |LAM| icon by itself), to the existing serverless application (represented by a |LAM| icon inside of a folder).
  #. |AC9| creates a remote version of the function in |LAM| and adds it to the :guilabel:`Remote Functions` list. |AC9| gives the remote version
     a different name. For example, if you named the function :code:`myDemoFunction` and added it to a
     serverless application named :code:`myDemoServerlessApplication`, the remote version name would
     be
     :code:`cloud9-myDemoServerlessApplication-myDemoFunction-RANDOM_ID`,
     where :code:`RANDOM_ID` is a randomly determined ID.
  #. If you chose to have |ABP| automatically trigger your function, |AC9| creates an API in |ABP| with
     a name that corresponds to the related serverless application, if it doesn't already exist.
     For example, if the serverless application is named :code:`myDemoServerlessApplication`, the API name would be
     :code:`cloud9-myDemoServerlessApplication`. |AC9| uses the value you specified in :guilabel:`Resource Path`
     to map the function to the API using the :code:`ANY` method.

In the :guilabel:`Environment` window, |AC9| does the following:

* If you chose to create a single function by itself, |AC9| creates a folder with the same name as the
  serverless application and puts this folder in the root of the |envfirst|. |AC9| then adds the following files to the folder:

  * :file:`.application.json`: A hidden file that contains JSON-formatted settings specific to
    the serverless application. |AC9| uses these settings
    for its internal use. Do not edit this file.
  * :file:`.gitignore`: A hidden file that contains a list of files Git ignores, if you want to
    use Git to manage your source code for this function.
  * :file:`template.yaml`: An AWS SAM template file that contains information about the |LAM|
    function and any other related supported AWS resources. Whenever you update
    the local version of your function and then upload it to |LAM|, |AC9| calls AWS SAM to use this template file to do the upload.
    For more information, see the :lambda-dev-guide:`Using the AWS Serverless Application Model (AWS SAM) <deploying-lambda-apps.html#serverless_app>` in the |LAM-dg|.

    .. note:: You can edit this file to create additional supporting AWS resources for your function. For more information, see the
       `AWS Serverless Application Model (AWS SAM) <https://github.com/awslabs/serverless-application-model>`_ repository on GitHub.

  * A subfolder with the same name as the function, containing a code file representing the function logic. 

* If you chose to create a single function and then add it to an existing serverless application, |AC9| does the following to the folder that represents the serverless application:

  * Updates the :file:`template.yaml` file previously described to include information about the |LAM| function and any other related supported AWS resources.
  * A subfolder with the same name as the function, containing a code file representing the function logic.

The :file:`.application.json` and :file:`.gitignore` files are hidden. To show hidden files or hide
them if they're shown, in the :guilabel:`Environment` window,
choose the gear icon, and then choose :guilabel:`Show Hidden Files`.

To invoke the function, see :ref:`lambda-functions-invoke`.

.. _lambda-functions-import:

Import a |LAM| Function
=======================

If you have an existing |LAM| function in your AWS account but not in your |envfirst|, you must
import it before you can work with it in your |env|.

#. In the :guilabel:`Environment` window, choose where you want to import the function.
#. In the :guilabel:`Lambda` section of the :guilabel:`AWS Resources` window, choose the function's name in the :guilabel:`Remote Functions` list.

   .. note:: If you don't see your function in the :guilabel:`Remote Functions` list, choose the :guilabel:`Refresh functions List` button (the button with the
      circular arrow icon).

#. Do one of the following:

   * Double-click the function you just chose.
   * On the menu bar in the :guilabel:`Lambda` section, choose the :guilabel:`Import the selected Lambda function` button (the button with the arrow that faces down).
   * Right-click the function you just chose, and then choose :guilabel:`Import`.

   .. image:: images/console-lambda-import.png
      :alt: Importing a Lambda function to use in an AWS Cloud9 development environment

   .. note:: You cannot import a |LAM| function into a folder that represents either a serverless application or a |LAM| function. If you try to do this, |AC9| will display a message that it will import
      the |LAM| function into the environment's root location instead. To let |AC9| do this, choose :guilabel:`Import`. Otherwise, choose :guilabel:`Cancel`, choose a different folder to import the function
      (or create a new empty folder to import the function into), and then restart this procedure from the beginning.

#. When prompted to finish importing the function, choose :guilabel:`OK`.

|AC9| imports your function into a new folder in the root of your |env|. (|AC9| also adds the function to the :guilabel:`Local Functions` list in the :guilabel:`Lambda` section of the :guilabel:`AWS Resources` window.)
This folder has the same name as the function. |AC9| adds the following files to this folder:

* :file:`.application.json`: A hidden file that contains JSON-formatted settings specific to the
  function. |AC9| uses these settings
  for its internal use.
* :file:`.gitignore`: A hidden file that contains a list of files Git ignores, if you want to use
  Git to manage your source code for this function.
* :file:`template.yaml`: A file for |AC9| internal use.

  .. note:: Although the :file:`template.yaml` file is expressed in AWS SAM format, it isn't used
     by AWS SAM. Therefore, you cannot edit this file to create additional supporting AWS resources for
     your function. Do not modify this file.

* One or more code files containing the function logic.

The :file:`.application.json` and :file:`.gitignore` files are hidden. To display or hide hidden files, in the :guilabel:`Environment` window,
choose the gear icon, and then choose :guilabel:`Show Hidden Files`.

To invoke the function, see :ref:`lambda-functions-invoke`.

.. _lambda-functions-invoke:

Invoke a |LAM| Function
=======================

To invoke an existing |LAM| function, you must first import the remote version of the function into your
|envfirst|, if the function isn't already there. To do this, see :ref:`lambda-functions-import`.

#. In the :guilabel:`Lambda` section of the :guilabel:`AWS Resources` window, expand the :guilabel:`Local
   Functions` list, if it isn't already expanded.
#. Expand the serverless application folder that contains the function that you want to invoke.
#. Choose the function that you want to invoke, right-click it, and then choose
   :guilabel:`Run`.

#. Do one of the following:

   * To run the local version of the function within your |env|, choose :guilabel:`Run Local`.
   * To run the remote version of the function within |LAM|, choose :guilabel:`Run Remote`.

   .. image:: images/console-lambda-run-lambda-menu.png
      :alt: Choose to run the local or remote version of your function

   .. note:: If nothing appears to happen, an invoke tab might already be open for the function. If so,
      choose :guilabel:`Lambda (local)` or :guilabel:`Lambda (remote)` in the open invoke tab.

#. In the :guilabel:`Test payload` pane of the invoke tab that is displayed, confirm any custom input
   data you want your function to use when you test it.
   For information about the input data format, see :LAM-dg:`Step 2.2: Invoke the Lambda Function Manually and Verify Results, Logs, and Metrics <get-started-invoke-manually>` in the |LAM-dg|.
#. In the invoke tab, choose the :guilabel:`Run` button.

   .. image:: images/console-lambda-run-lambda.png
      :alt: Choose to run the function locally within your environment or remotely within Lambda

   .. note:: After you run the function for the first time, a :file:`lambda-payloads.json`: file is added to the function's related serverless application folder in the :guilabel:`Environment` window. This file
      contains the contents of the custom input data.

      If you invoke an existing |LAM| function and then try to invoke the same function code for its related API in |ABP|, you might get an error or the code might not run as expected. For more information, see 
      :ref:`lambda-functions-vs-api-gateway`.

The invoke tab contains two panes:

* The :guilabel:`Test payload` pane displays any custom input data that was supplied for the function.
* The :guilabel:`Execution results` pane displays any output from the function and some information from
  the related |CWLlong| for the function.

For more information, see :LAM-dg:`Step 2.2: Invoke the Lambda Function Manually and Verify Results, Logs, and Metrics <get-started-invoke-manually>` in the |LAM-dg|.

To upload the local version of any changed function code to the related remote version in |LAM|, see :ref:`lambda-functions-upload-code`.

.. _lambda-functions-api:

Invoke an |ABP| API for a Related |LAM| Function
================================================

To invoke an API in |ABP| that is related to an existing |LAM| function, you must first import the remote
version of the function into your |envfirst|, if the function isn't already there. To do this, see :ref:`lambda-functions-import`.

.. note:: You cannot debug the remote version of the |ABP| API in your |env|. You can only invoke it. To debug the local version, see :ref:`lambda-functions-debug`.

#. In the :guilabel:`Lambda` section of the :guilabel:`AWS Resources` window, expand the :guilabel:`Local
   Functions` list, if it isn't already expanded.
#. Expand the serverless application folder that contains the function whose API you want to invoke.
#. Choose the function, right-click it, and then choose :guilabel:`Run`.

#. Do one of the following:

   * To run the local version of the API within your |env|, choose :guilabel:`Run API Gateway Local`.
   * To run the remote version of the function within |LAM|, choose :guilabel:`Run API Gateway Remote`.

   .. note:: If nothing appears to happen, an invoke tab might already be open for the function. If  so, choose :guilabel:`API Gateway (local)` or :guilabel:`API Gateway (remote)` in the open  invoke tab.

#. In the :guilabel:`Test payload` pane of the invoke tab that is displayed, confirm the :guilabel:`Function`,
   :guilabel:`Path`, :guilabel:`Method`, :guilabel:`Query String`, and :guilabel:`Body` you want the API
   to use when you test it.

   .. note:: Some APIs might not support settings such as :guilabel:`Body`. For more information, consult
      the owner of the API.

#. On the invoke tab, choose the :guilabel:`Run` button.

   .. image:: images/console-lambda-run-api.png
      :alt: Choose run on the invoke tab

   .. note:: If the API isn't connected to the function, a message appears that says an |ABP|
      trigger can't be found in the function's AWS SAM file. To use this
      AWS SAM file to connect an API in |ABP| to the function, see the
      `AWS Serverless Application Model (AWS SAM) <https://github.com/awslabs/serverless-application-model>`_
      repository on GitHub.

      If you invoke an API in |ABP| and then try to invoke the same code for its related function in |LAM|, you might get an error or the code might not run as expected. For more information, see 
      :ref:`lambda-functions-vs-api-gateway`.

The invoke tab contains two panes:

* The :guilabel:`Test payload` pane displays settings and any custom input data that was supplied for the API.
* The :guilabel:`Execution results` pane displays information such as the body, headers, and logs of the API response.

.. _lambda-functions-vs-api-gateway: 

Coding Differences When Invoking a |LAM| Function and Its Related |ABP| API
===========================================================================

When you invoke a |LAM| function and then try to invoke the same code for a related API in |ABP|, you might get an error or the code might not run as expected. Likewise, when you invoke an 
|ABP| API and then try to invoke the same code for a related |LAM| function, you might get an error or the code might not run as expected. This is because 
|LAM| and |ABP| use different event data formats. Therefore, you might not be able to 
successfully invoke the same code in both |LAM| and |ABP|.

For example, the following Node.js code invoked with |ABP| returns output in the expected JSON format:

.. code-block:: javascript

   'use strict';

   /* 
   Assume the following payload is input:

   {
     "fruit": "apple",
     "vegetable": "carrot"
   }

   The expected response is:

   {
     "statusCode": 200, 
     "headers": {
       "Content-type": "application/json"
     },
     "body": {
       "message": "Your favorite fruit is apple. Your favorite vegetable is carrot."
     }
   }
   */

   exports.handler = function(event, context, callback) {

     var body = JSON.parse(event.body);
    
     const message = "Your favorite fruit is " + body.fruit + ". " + 
       "Your favorite vegetable is " + body.vegetable + ".";

     const response = {
       statusCode: 200,
       headers: { "Content-type": "application/json" },
       body: JSON.stringify( { "message": message } )
     };
    
     callback(null, response);
   };

To invoke the preceding Node.js code with |LAM|, you must remove the line :code:`var body = JSON.parse(event.body)` as well as substitute :code:`body.fruit` and 
:code:`body.vegetable` with :code:`event.fruit` and :code:`event.vegetable`.

As another example, the following Python code invoked with |ABP| returns output in the expected JSON format:

.. code-block:: python 

   ''' 
   Assume the following payload is input:

   {
     "fruit": "apple",
     "vegetable": "carrot"
   }

   The expected response is:

   {
     "statusCode": 200, 
     "headers": {
       "Content-type": "application/json"
     },
     "body": {
       "message": "Your favorite fruit is apple. Your favorite vegetable is carrot."
     }
   }
   '''

   import json

   def lambda_handler(event, context):
    
     body = json.loads(event["body"])

     message = ("Your favorite fruit is " + body["fruit"] + ". " +
       "Your favorite vegetable is " + body["vegetable"] + ".") 
  
     response = {
       "statusCode": "200", 
       "headers": { "Content-type": "application/json" },
       "body": json.dumps({"message": message})
     }
  
     return response

To invoke the preceding Python code with |LAM|, you must remove the line :code:`body = json.loads(event["body"])` as well as substitute :code:`body["fruit"]` and 
:code:`body["vegetable"]` with :code:`event["fruit"]` and :code:`event["vegetable"]`.

.. _lambda-functions-debug:

Debug the Local Version of a |LAM| Function or Its Related |ABP| API
====================================================================

You can debug local |LAM| function code or its related |ABP| API in your |env| using common debugging aids such as breakpoints, stepping through code, and setting watch expressions.

.. note:: You cannot debug the remote version of a |LAM| function or its related |ABP| API in your |env|. You can only invoke it.

   You cannot debug local |LAM| function code that uses Python.

To debug the local version of an existing |LAM| function or its related |ABP| API, you must first import the remote version of
the function into your |envfirst|, if the function isn't already there. See :ref:`lambda-functions-import`.

#. In the :guilabel:`Environment` window, open the file that contains the |LAM| function's code you want to debug.
#. Set any breakpoints and watch expressions for your code. See :ref:`build-run-debug-debug`.
#. In the :guilabel:`Lambda` section of the :guilabel:`AWS Resources` window, expand the :guilabel:`Local
   Functions` list, if it isn't already expanded.
#. Expand the serverless application folder that contains the function you want to debug.
#. Choose the function to debug, right-click it, and then choose :guilabel:`Run, Run Local` or :guilabel:`Run, Run API Gateway Local`.

   .. note:: If nothing appears to happen, an invoke tab might already be open for the function. If so, go to the open invoke tab and choose :guilabel:`Lambda (local)` or :guilabel:`API Gateway (local)`.

#. For a |LAM| function, in the :guilabel:`Test payload` pane of the invoke tab that is displayed, confirm any custom input
   data you want your function to use when you test it.
   For information about the input data format, see :LAM-dg:`Step 2.2: Invoke the Lambda Function Manually and Verify Results, Logs, and Metrics <get-started-invoke-manually>` in the |LAM-dg|.
#. For an |ABP| API, in the :guilabel:`Test payload` pane of the invoke tab that is displayed, confirm the 
   :guilabel:`Path`, :guilabel:`Method`, :guilabel:`Query String`, and :guilabel:`Body` you want the API
   to use when you test it.

   .. note:: Some APIs might not support settings such as :guilabel:`Body`. For more information, consult
      the owner of the API.

#. Next to the :guilabel:`Run` button, choose :guilabel:`Run in Debug Mode` (the bug icon).
#. Choose the :guilabel:`Run` button.
#. Decide what to do whenever function execution pauses at a breakpoint. See :ref:`build-run-debug-debug`.

.. image:: images/console-lambda-debug.png
   :alt: Choose what happens when your function execution pauses at a breakpoint

.. _lambda-functions-change-code:

Change Code in a |LAM| Function
===============================

To use the |AC9IDE| to change the code in a function, you must first import the related remote version
of the function into your |envfirst|, if the function isn't already there. To do this, see :ref:`lambda-functions-import`.
Then do the following:

#. In the :guilabel:`Lambda` section of the :guilabel:`AWS Resources` window, expand the :guilabel:`Local
   Functions` list, if it isn't already expanded.
#. Expand the serverless application folder that contains the function whose code you want to change.
#. Right-click the function, and then choose :guilabel:`Edit Function`.

   .. image:: images/console-lambda-edit.png
      :alt: Lambda section of the AWS Resources window

#. Make the changes you want to the code, and then save the file.

To upload the local version of the changed function code to the related remote version in |LAM|, see :ref:`lambda-functions-upload-code`.

.. _lambda-functions-upload-code:

Upload Code for a |LAM| Function
================================

To upload the local version of a |LAM| function in your |env| to the related remote version of the function in |LAM|, do the following.

#. In the :guilabel:`Lambda` section of the :guilabel:`AWS Resources` window, expand the :guilabel:`Local
   Functions` list, if it isn't already expanded.
#. Expand the serverless application folder that contains the function you want to upload.
#. Do one of the following:

   * Right-click the serverless application folder that you just chose, and then choose :guilabel:`Deploy`.
   * Right-click the function you want to upload, and then choose :guilabel:`Deploy`.
   * Choose the function you want to upload, and then choose :guilabel:`Deploy the selected Lambda function` (the button with the arrow that faces up).

   .. image:: images/console-lambda-upload.png
      :alt: Upload command in the Lambda section of the AWS Resources window

.. _lambda-functions-convert-to-sam:

Convert a |LAM| Function to a Serverless Application
====================================================

If the local version of an existing |LAM| function in your |envfirst| isn't already part of a serverless
application, you can use the |AC9IDE| to convert that function into a serverless application.
You can then use the AWS SAM template file for that serverless application to create additional supporting AWS resources for your function. For more information, see the
`AWS Serverless Application Model (AWS SAM) <https://github.com/awslabs/serverless-application-model>`_ repository on GitHub.

To convert the local version of an existing |LAM| function into a serverless application, you must first import the remote version of
the function into your |envfirst|, if the function isn't already there. See :ref:`lambda-functions-import`.

#. In the :guilabel:`Lambda` section of the :guilabel:`AWS Resources` window, expand the :guilabel:`Local
   Functions` list, if it isn't already expanded.
#. Right-click the function you want to convert, and then choose :guilabel:`Convert to SAM`.

   .. image:: images/console-lambda-convert.png
      :alt: Convert to SAM command in the Lambda section of the AWS Resources window

|AC9| does the following:

* In the function's folder in the :guilabel:`Environment` window, the :code:`DeploymentMethod` setting in the :file:`.application.json` file changes from :code:`lambda` to :code:`cloudformation`. This means
  that now |AC9| will instruct AWS SAM to use |CFN| whenever you use the |IDE| to upload the function's code as part of the serverless application. (:code:`lambda` means that |AC9| will instruct |LAM| to deploy the
  function instead.) To upload the function code, see :ref:`lambda-functions-upload-code`.
* In the :guilabel:`Lambda` section of the :guilabel:`AWS Resources` window, in the :guilabel:`Local Functions` list, |AC9| adds the existing |LAM| function to a new serverless application (represented by a |LAM| icon inside of a folder).
  The serverless application has the same name as the function.

When you upload the function's code as described in :ref:`lambda-functions-upload-code`, because the function upload method is no longer |LAM| but now AWS SAM using |CFN|, |AC9| creates a new remote version of the function in |LAM| and adds it to the :guilabel:`Remote Functions` list.
|AC9| gives the remote version a name that is different from the original |LAM| function. For example,
if the serverless application and the function are both named :code:`myDemoFunction`, the remote version
name of your function would be :code:`cloud9-myDemoFunction-myDemoFunction-RANDOM_ID`,
where :code:`RANDOM_ID` is a randomly determined ID.

.. important:: After you do the conversion, if you then use the |IDE| to make any changes to the function code and then upload that code to |LAM|,
   only the remote version of the new function (for example, :code:`cloud9-myDemoFunction-myDemoFunction-RANDOM_ID`) will contain the change. The remote version of the original function (for example, :code:`myDemoFunction`) will not change.

   If you change your mind and want to enable the |IDE| to go back to uploading your code changes to the remote version of the original function (for example, :code:`myDemoFunction`), do the following:

   #. In the function's folder in the :guilabel:`Environment` window, change the :code:`DeploymentMethod` setting in the :file:`.application.json` file from :code:`cloudformation` back to :code:`lambda`, and then save the file. This
      removes the serverless application folder from the :guilabel:`Local Functions` list and causes |AC9| to go back to instructing |LAM| to deploy the function.
   #. Upload the function code as described in :ref:`lambda-functions-upload-code`. Now, only the remote version of the original function (for example, :code:`myDemoFunction`) will contain the change.
      The remote version of the new function (for example, :code:`cloud9-myDemoFunction-myDemoFunction-RANDOM_ID`) will not change.
   #. Because |AC9| will no longer upload code changes to the remote version of the new function (for
      example, :code:`cloud9-myDemoFunction-myDemoFunction-RANDOM_ID`), if you want you can use the |LAM|
      console to delete the new function
      (for example, :code:`cloud9-myDemoFunction-myDemoFunction-RANDOM_ID`).

.. _lambda-functions-update-settings:

Update Configuration Settings for a |LAM| Function
==================================================

You can use the |AC9IDE| to change function settings such as the description, handler identifier, amount of memory the function will use, and existing execution role the function will use.

To change configuration settings, you must first import the related remote version of the function into
your |envfirst|, if the function isn't already there. To do this, see :ref:`lambda-functions-import`.
Then do the following.

#. In the :guilabel:`Lambda` section of the :guilabel:`AWS Resources` window, expand the :guilabel:`Local
   Functions` list, if it isn't already expanded.
#. Expand the serverless application folder that contains the function whose setting you want to change.
#. Right-click the function, and then choose :guilabel:`Edit Config`.

   .. image:: images/console-lambda-config.png
      :alt: Update configuration settings for a Lambda function in the Lambda section of the AWS Resources
            window

#. Make changes to the configuration settings, and then save the file.

   .. note:: By default, configuration settings are displayed in plain text. To change this behavior to display configuration settings in a visual editor by default, 
      choose :guilabel:`AWS Cloud9, Preferences` on the menu bar. Choose :guilabel:`AWS Settings`, and then turn on :guilabel:`Use AWS SAM visual editor`. 
      To use the visual editor, close the function's :file:`template.yaml` file, and then right-click the function and choose :guilabel:`Edit Config` again. 
      To switch back to using plain text by default, turn off the :guilabel:`Use AWS SAM visual editor` setting. To temporarily edit plain text, choose :guilabel:`View with text editor (Ace)` 
      in the visual editor, and then choose :guilabel:`View, Editors, Ace` on the menu bar. 

#. Do one of the following:

   * On the configuration settings tab, in the simplified settings view, choose the :guilabel:`Upload Settings to Lambda` button.
   * Follow the instructions in :ref:`lambda-functions-upload-code`.

   .. image:: images/console-lambda-config-edit.png
      :alt: Upload settings to Lambda or upload code for a Lambda function using the configuration settings
            tab
