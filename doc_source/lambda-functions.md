# Working with AWS Lambda Functions in the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="lambda-functions"></a>

You can use the AWS Cloud9 IDE to work with AWS Lambda functions and their related Amazon API Gateway APIs in an AWS Cloud9 development environment\. For example, you can:
+ Create a new function from within your environment, uploading the local version of the function to Lambda, and optionally creating additional AWS resources to support the new function at the same time\.
+ Run and debug a function and its related API in your environment, running the function and API completely within the environment\.
+ Run the remote version of a function and its related API within your environment, running the remote version completely within Lambda and API Gateway\.
+ Import an existing function in Lambda into your environment, so that you can run and debug the function and its related API, edit the code, or both\.
+ Upload changes you make to the local version of the function code to the remote version in Lambda\.

This topic assumes you already know about Lambda\. For more information, see the [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/)\.

**Note**  
Completing these procedures might result in charges to your AWS account\. These include possible charges for services such as Lambda, API Gateway, and AWS services supported by the AWS Serverless Application Model \(AWS SAM\)\. For more information, see [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/), [Amazon API Gateway Pricing](https://aws.amazon.com/api-gateway/pricing/), and [Cloud Services Pricing](https://aws.amazon.com/pricing/services/)\.

**Topics**
+ [Prepare to Work with Lambda Functions](#lambda-functions-prepare)
+ [Create a Lambda Function With the Create Serverless Application Wizard](#lambda-functions-create)
+ [Create and Deploy Lambda Functions with the AWS Serverless Application Repository](#lambda-functions-create-repo)
+ [Import a Lambda Function](#lambda-functions-import)
+ [Invoke a Lambda Function](#lambda-functions-invoke)
+ [Invoke a Lambda Function that Uses Environment Variables](#lambda-functions-invoke-env-vars)
+ [Working with Lambda Functions that Use Versions, Aliases, or Layers](#lambda-functions-versions-aliases-layers)
+ [Invoke an API Gateway API for a Related Lambda Function](#lambda-functions-api)
+ [Response Differences When Invoking a Lambda Function from API Gateway](#lambda-functions-vs-api-gateway)
+ [Add Dependent Code to a Lambda Function](#lambda-functions-adding-packages)
+ [Debug the Local Version of a Lambda Function or Its Related API Gateway API](#lambda-functions-debug)
+ [Change Code in a Lambda Function](#lambda-functions-change-code)
+ [Upload Code for a Lambda Function](#lambda-functions-upload-code)
+ [Convert a Lambda Function to a Serverless Application](#lambda-functions-convert-to-sam)
+ [Update Configuration Settings for a Lambda Function](#lambda-functions-update-settings)
+ [Delete a Lambda Function](#lambda-functions-delete)

## Prepare to Work with Lambda Functions<a name="lambda-functions-prepare"></a>

Before you can work with Lambda functions in the AWS Cloud9 IDE, you must complete the following steps:

**Topics**
+ [Step 1: Set Up Your IAM Group with Required Access Permissions](#lambda-functions-prepare-user)
+ [Step 2: Set Up Your Environment with Your AWS Access Credentials](#lambda-functions-prepare-access)
+ [Step 3: Create an Execution Role for Your Lambda Functions](#lambda-functions-prepare-role)
+ [Step 4: Set Your Environment to the Correct AWS Region](#lambda-functions-prepare-region)
+ [Step 5: Open the Lambda Section of the AWS Resources Window](#lambda-functions-prepare-open)

### Step 1: Set Up Your IAM Group with Required Access Permissions<a name="lambda-functions-prepare-user"></a>

If your AWS access credentials are associated with an IAM administrator user in your AWS account, and you want to use that user to work with Lambda functions, skip ahead to [Step 2: Set Up Your Environment with Your AWS Access Credentials](#lambda-functions-prepare-access)\.

Otherwise, complete the following instructions to use the IAM console to attach the AWS managed policies named `AWSLambdaFullAccess`, `AmazonAPIGatewayAdministrator`, `AmazonAPIGatewayInvokeFullAccess`, and an additional inline policy, to an IAM group to which your user belongs\.

1. Sign in to the AWS Management Console, if you're not already signed in\.

   For this step, we recommend you sign in using credentials for an IAM administrator in your AWS account\. If you can't do this, check with your AWS account administrator\.

1. Open the IAM console\. To do this, in the console's navigation bar, choose **Services**\. Then choose **IAM**\.

1. Choose **Groups**\.

1. Choose the group's name\.

1. On the **Permissions** tab, for **Managed Policies**, choose **Attach Policy**\.

1. In the list of policy names, choose the boxes next to **AWSLambdaFullAccess**, **AmazonAPIGatewayAdministrator**, and **AmazonAPIGatewayInvokeFullAccess**\. \(If you don't see any of these policy names in the list, type the policy name in the **Search** box to display it\.\)

1. Choose **Attach Policy**\.

1. Download the following ZIP file to your local computer: [Cloud9LambdaAccessGroup\.zip](samples/Cloud9LambdaAccessGroup.zip)\. Then extract the AWS CloudFormation template file named `Cloud9LambdaAccessGroup.yaml` from the downloaded ZIP file\. 

1. Open the AWS CloudFormation console\. To do this, in the console's navigation bar, choose **Services**\. Then choose **CloudFormation**\.

1. Choose **Create Stack**\.

1. On the **Select Template** page, for **Choose a template**, choose **Upload a template to Amazon S3**\. Choose **Browse**, and then choose the AWS CloudFormation template file that you just extracted\.

1. Choose **Next**\.

1. On the **Specify Details** page, for **Stack name**, type a name for the stack \(for example `AWSCloud9LambdaAccessStack`\. If you type a different name, replace it throughout this procedure\)\.

1. For **Parameters**, for **GroupName**, type the name of the existing group in your AWS account you want to attach the access policy to\.

1. Choose **Next**\.

1. On the **Options** page, choose **Next**\. \(Do not change any of the default settings on the **Options** page\.\)

1. On the **Review** page, choose **I acknowledge that AWS CloudFormation might create IAM resources**\.

1. Choose **Create**\.

Wait until the **AWSCloud9LambdaAccessStack** stack shows **CREATE\_COMPLETE**\. This might take a few moments\. Please be patient\.

**Note**  
The access policy that AWS CloudFormation attaches to the group is named `AWSCloud9LambdaGroupAccess` and has the following definition, where ` ACCOUNT_ID ` is your AWS account ID\.  

```
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
```

### Step 2: Set Up Your Environment with Your AWS Access Credentials<a name="lambda-functions-prepare-access"></a>

The AWS Cloud9 IDE uses the AWS Command Line Interface \(AWS CLI\) in your AWS Cloud9 development environment to interact with Lambda and other supporting AWS services\. Therefore, the AWS CLI in your environment needs access to your AWS access credentials\.

Do one of the following to set up the AWS CLI in your environment:
+ If you have an EC2 environment, AWS managed temporary credentials are already set up in your environment for the AWS CLI to use, and you can skip ahead to [Step 3: Create an Execution Role for Your Lambda Functions](#lambda-functions-prepare-role)\. AWS managed temporary credentials have permission to interact with most AWS services from your environment \(provided the AWS entity that is using the environment also has those permissions\)\. For more information, see [AWS managed temporary credentials](how-cloud9-with-iam.md#sec-auth-and-access-control-temporary-managed-credentials)\.
+ If you have an EC2 environment but AWS managed temporary credentials don't meet your needs, you can attach an IAM instance profile to the Amazon EC2 instance that connects to your environment\. Or you can store your permanent AWS access credentials within the environment\. For instructions, see [Create and Use an Instance Profile to Manage Temporary Credentials](credentials.md#credentials-temporary) or [Create and Store Permanent Access Credentials in an Environment](credentials.md#credentials-permanent-create)\.
+ If you have an SSH environment, you can store your permanent AWS access credentials within the environment\. For instructions, see [Create and Store Permanent Access Credentials in an Environment](credentials.md#credentials-permanent-create)\.

### Step 3: Create an Execution Role for Your Lambda Functions<a name="lambda-functions-prepare-role"></a>

If you want your Lambda functions to do things using AWS resources, you must specify an IAM role \(execution role\) that contains the necessary access permissions for your functions to use\.

When you create a Lambda function, AWS Cloud9 can create an execution role for you\. This execution role contains the permissions as described in [Basic Lambda Permissions](https://docs.aws.amazon.com/lambda/latest/dg/policy-templates.html#basic-execution) in the *AWS Lambda Developer Guide*\.

If this execution role doesn't meet your needs, you must create an execution role on your own before you create your Lambda function\. For more information, see the following:
+  [AWS Lambda Permissions Model](https://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html) in the *AWS Lambda Developer Guide*
+  [Creating a Role to Delegate Permissions to an AWS Service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *IAM User Guide*

### Step 4: Set Your Environment to the Correct AWS Region<a name="lambda-functions-prepare-region"></a>

You must set your AWS Cloud9 development environment to use the AWS Region where you want to create new Lambda functions in your AWS account, or where you want to import existing Lambda functions from your AWS account into your AWS Cloud9 development environment\.

To do this:

1. In the AWS Cloud9 IDE, on the menu bar, choose **AWS Cloud9, Preferences**\.

1. In the navigation pane of the **Preferences** tab, choose **AWS Settings**\.

1. For **AWS Region**, select the AWS Region you want to use\.

### Step 5: Open the Lambda Section of the AWS Resources Window<a name="lambda-functions-prepare-open"></a>

Now you're ready to begin using the AWS Cloud9 IDE to work with Lambda functions\. To do this, expand the **Lambda** section of the **AWS Resources** window, if it isn't already expanded\.

![\[AWS Resources window showing the Lambda section\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-lambda-menu.png)

If the **AWS Resources** window isn't visible, choose the **AWS Resources** button\.

If you don't see the **AWS Resources** button, choose **Window, AWS Resources** on the menu bar to show it\.

## Create a Lambda Function With the Create Serverless Application Wizard<a name="lambda-functions-create"></a>

You can use the AWS Cloud9 IDE to create a new Lambda function\. If you already have a Lambda function in your AWS account for the AWS Region you set earlier, skip ahead to [Import a Lambda Function](#lambda-functions-import)\.

**Note**  
This procedure describes how to use the **Create serverless application** wizard to create a single Lambda function based on function blueprints that are owned by AWS\. To create multiple Lambda functions at the same time, Lambda functions along with supporting components at the same time, or Lambda functions that are owned by entities other than AWS, skip ahead to [Create and Deploy Lambda Functions with the AWS Serverless Application Repository](#lambda-functions-create-repo)\.

1. In the **Lambda** section of the **AWS Resources** window, choose where you want to create the function:
   + To create a single function by itself, choose the **Local Functions** heading\.
   + To create a function and then add it to an existing group of one or more functions and related AWS resources \(referred to as a *serverless application*\), in the **Local Functions** list, choose the serverless application for the group \(represented by the Lambda icon inside of a folder\)\.

1. Do one of the following:
   + Choose **Create a new Lambda function** \(the button with the Lambda icon\)\.
   + Right\-click the **Local Functions** heading or the serverless application folder you chose earlier, and then choose **Create Here**\.  
![\[Creating a new Lambda function using the Lambda section of the AWS Resources window\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-lambda-create.png)

1. In the **Create serverless application** dialog box, specify the following settings for the function:
   +  **Function Name**: A name for the function\.
   +  **Application Name**: The name of the new serverless application to be associated with the new function\.
**Important**  
Both of these names must contain only alphanumeric characters and hyphens\. Each name must start with an alphabetic character, and each name must not exceed 128 characters\.

1. Choose **Next**\.

1. Choose the function blueprint you want to start with\. \(Currently, only Node\.js and Python function blueprints are available\.\)

   To show blueprints for a specific runtime, for **Select Runtime**, choose the runtime\. For example, to use the `hello-world` function blueprint for Node\.js 6\.10, choose **Node\.js 6\.10** for **Select Runtime**, and then choose the **hello\-world** blueprint for **Select Blueprint**\.

1. Choose **Next**\.

1. Do one of the following:
   + To skip having an AWS service automatically trigger this function, leave **Function Trigger** set to **none**, choose **Next**, and then skip ahead to step 9 in this procedure\.
   + To have an AWS resource in your account automatically trigger your function, for **Function Trigger**, select the name of the AWS service that will contain the resource\. \(Currently, only **API Gateway** is available\.\)

1. If you chose **API Gateway** for **Function Trigger**, specify the following for **Trigger Settings**:
   + For **Resource Path**, type the URL portion of the API to use to invoke the function\. For example, type `/` to specify the resource root\.
   + For **Security**, choose the security mechanism for the API endpoint:
     +  **AWS\_IAM**: Require that callers provide IAM access credentials to be authenticated\. See [Control Access to API Gateway with IAM Permissions](https://docs.aws.amazon.com/apigateway/latest/developerguide/permissions.html) in the *API Gateway Developer Guide*\.
     +  **NONE**: Enable open access\.
     +  **NONE\_KEY**: Require that callers provide an API key to be authenticated\. See [Set Up API Keys Using the API Gateway Console](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-setup-api-key-with-console.html) in the *API Gateway Developer Guide*\.

1. Choose **Next**\.

1. For **Memory \(MB\)**, choose the amount of memory, in megabytes, that this function will use\.

1. Do one of the following:
   + To have AWS Cloud9 create a new, basic IAM role \(execution role\) for this function to use, for **Role**, choose **Automatically generate role**\. Then choose **Next**\.
   + To have Lambda use an existing IAM role \(execution role\) in your AWS account, for **Role**, choose **Choose an existing role**\. For **Existing Role**, choose the name of the role, and then choose **Next**\.

1. Choose **Next**\.

1. Choose **Finish**\.

Compare your results to the following:

![\[Creating a Lambda function\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-lambda-create.gif)

In the **Lambda** section of the **AWS Resources** window, AWS Cloud9 does the following:
+ If you chose to create a single function by itself:

  1. AWS Cloud9 creates a serverless application with the name that you specified earlier\. Then it adds a serverless application \(represented by a Lambda icon inside of a folder\) to the **Local Functions** list\. Then it adds the Lambda function \(represented by a Lambda icon by itself\), to this serverless application\.

  1. AWS Cloud9 creates a remote version of the function in Lambda and adds it to the **Remote Functions** list\. AWS Cloud9 gives the remote version a different name\. For example, if you named the serverless application `myDemoServerlessApplication` and the function `myDemoFunction`, the remote version name of your function would be `cloud9-myDemoServerlessApplication-myDemoFunction-RANDOM_ID`, where `RANDOM_ID` is a randomly determined ID\.  
![\[Both the local and remote functions refer to the same function\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-lambda-ide.png)

  1. If you chose to have API Gateway automatically trigger the function, AWS Cloud9 creates an API in API Gateway with a name that corresponds to the function\. For example, if you named the function `myDemoFunction`, the API name would be `cloud9-myDemoFunction`\. AWS Cloud9 uses the value you specified in **Resource Path** to map the function to the API using the `ANY` method\.
+ If you chose to create a single function and then add it to an existing serverless application:

  1. AWS Cloud9 adds the Lambda function \(represented by a Lambda icon by itself\), to the existing serverless application \(represented by a Lambda icon inside of a folder\)\.

  1. AWS Cloud9 creates a remote version of the function in Lambda and adds it to the **Remote Functions** list\. AWS Cloud9 gives the remote version a different name\. For example, if you named the function `myDemoFunction` and added it to a serverless application named `myDemoServerlessApplication`, the remote version name would be `cloud9-myDemoServerlessApplication-myDemoFunction-RANDOM_ID`, where `RANDOM_ID` is a randomly determined ID\.

  1. If you chose to have API Gateway automatically trigger your function, AWS Cloud9 creates an API in API Gateway with a name that corresponds to the related serverless application, if it doesn't already exist\. For example, if the serverless application is named `myDemoServerlessApplication`, the API name would be `cloud9-myDemoServerlessApplication`\. AWS Cloud9 uses the value you specified in **Resource Path** to map the function to the API using the `ANY` method\.

In the **Environment** window, AWS Cloud9 does the following:
+ If you chose to create a single function by itself, AWS Cloud9 creates a folder with the same name as the serverless application and puts this folder in the root of the AWS Cloud9 development environment\. AWS Cloud9 then adds the following files to the folder:
  +  `.application.json`: A hidden file used by AWS Cloud9 that contains JSON\-formatted settings specific to the serverless application\.
  +  `.gitignore`: A hidden file that contains a list of files Git ignores, if you want to use Git to manage your source code for this function\.
  +  `template.yaml`: An AWS SAM template file that contains information about the Lambda function and any other related supported AWS resources\. Whenever you update the local version of your function and then upload it to Lambda, AWS Cloud9 calls AWS SAM to use this template file to do the upload\. For more information, see [Using the AWS Serverless Application Model \(AWS SAM\)](https://docs.aws.amazon.com/lambda/latest/dg/deploying-lambda-apps.html#serverless_app) in the *AWS Lambda Developer Guide*\.
**Note**  
You can edit this file to create additional supporting AWS resources for your function\. For more information, see the [AWS Serverless Application Model \(AWS SAM\)](https://github.com/awslabs/serverless-application-model) repository on GitHub\.
  + A subfolder with the same name as the function, containing a code file representing the function logic\.
  + If the function uses Python, additional subfolders and files are added to the preceding subfolder to enable Python debugging:
    +  `.debug`: A subfolder that contains Python modules and files for debugging purposes\.
    +  `venv`: A standard Python virtualenv folder\. This includes a module named ikpdb, which AWS Cloud9 uses to debug Python applications\.
    +  `__init__.py`: A standard Python package initialization file\.
    +  `requirements.txt`: A standard file for installing Python modules\.
    + AWS Cloud9 also adds a `CodeUri` property to the `template.yaml` file and sets this property to reference the `.debug/` folder\.
+ If you chose to create a single function and then add it to an existing serverless application, AWS Cloud9 does the following to the folder that represents the serverless application:
  + Updates the `template.yaml` file previously described to include information about the Lambda function and any other related supported AWS resources\.
  + A subfolder with the same name as the function, containing a code file representing the function logic\.
  + If the function uses Python, additional subfolders and files are added to the preceding subfolder to enable Python debugging:
    +  `.debug`: A subfolder that contains Python modules and files for debugging purposes\.
    +  `venv`: A standard Python virtualenv folder\. This includes a module named ikpdb, which AWS Cloud9 uses to debug Python applications\.
    +  `__init__.py`: A standard Python package initialization file\.
    +  `requirements.txt`: A standard file for installing Python modules\.
    + AWS Cloud9 also adds a `CodeUri` property to the `template.yaml` file and sets this property to reference the `.debug/` folder\.

The `.application.json` and `.gitignore` files \(and the `.debug` folder for Python\) are hidden\. To show hidden files or hide them if they're shown, in the **Environment** window, choose the gear icon, and then choose **Show Hidden Files**\.

![\[Showing the hidden Lambda files\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-lambda-files.png)

To invoke the function, see [Invoke a Lambda Function](#lambda-functions-invoke)\. If the function has a related API in API Gateway, to invoke the API, see [Invoke an API Gateway API for a Related Lambda Function](#lambda-functions-api)\.

## Create and Deploy Lambda Functions with the AWS Serverless Application Repository<a name="lambda-functions-create-repo"></a>

You can use the AWS Cloud9 IDE and the [AWS Serverless Application Repository](https://aws.amazon.com/serverless/serverlessrepo/) to create multiple Lambda functions at the same time, Lambda functions along with supporting components at the same time, or Lambda functions that are owned by entities other than AWS\. If you already have Lambda functions in your AWS account for the AWS Region you set earlier, skip ahead to [Import a Lambda Function](#lambda-functions-import)\.

1. In a separate web browser tab, open the [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com)\.

1. Find the serverless application you want to create, and then choose the title of the serverless application that you want inside of its card\. \(If the card isn't visible, begin typing information about the serverless application that you want in the **Search applications by name, description, or labels** box to show it\.\)

1. On the **Application details** page that appears, if a URL for a Git\-based repository is displayed, copy that URL \(for example, `https://github.com/USER_NAME/REPOSITORY_NAME`\)\.
**Note**  
If a URL isn't displayed, try choosing the **Deploy** button on the **Application details** page, and then look for a **Source code URL** value\.

1. Back in the AWS Cloud9 IDE, open a terminal, if one isn't already open\. \(To open a terminal, on the menu bar, choose **Window, New Terminal**\.\)

1. In the terminal, change to the directory in your environment where you want to copy the serverless application's starter files \(for example, by running the command `cd ~/environment`\)\.

1. Run the command `git clone`, followed by the Git URL you copied earlier \(for example, `git clone https://github.com/USER_NAME/REPOSITORY_NAME`\)\. The IDE then adds the serverless application's functions to the **Lambda** section of the **AWS Resources** window\.
**Note**  
Running the `git clone` command with some of the URLs in the **Application details** pages or **Source code URL** values might not work as expected or might produce unexpected results\. Alternatively, you can manually download the files you want from the desired repository to your local workstation\. Then manually upload those files to the IDE by running **File, Upload Local Files** on the menu bar\.  
When you clone the GitHub repository, the IDE uses the AWS Serverless Application Model \(AWS SAM\) template file in the repository to determine which of the serverless application's functions to display in the **Lambda** section of the **AWS Resources** window\. The AWS SAM template file must follow the [AWS Serverless Application Model \(AWS SAM\)](https://github.com/awslabs/serverless-application-model) file format\. If the repository doesn't contain an AWS SAM template file, or if the file doesn't follow the AWS SAM file format, the IDE won't display those functions\. You also won't be able to run, debug, or deploy those functions or any of their associated API Gateway resources from the **Lambda** section of the **AWS Resources** window\.

1. You might need to complete some setup before you can run, debug, or deploy the serverless application from the IDE as expected\. For setup instructions, see the **Application details** page that you opened earlier\. Or look for any setup instructions within the serverless application's files that you cloned to your IDE\.

To invoke the functions, see [Invoke a Lambda Function](#lambda-functions-invoke)\. If the functions have related APIs in API Gateway, to invoke the APIs, see [Invoke an API Gateway API for a Related Lambda Function](#lambda-functions-api)\. When you invoke a function or API this way for the first time, AWS Cloud9 adds a hidden `.application.json` file to the serverless application's component files\. This file is used by AWS Cloud9 and contains JSON\-formatted settings that are specific to the serverless application\.

If the serverless application requires parameters to be specified during deployment, you can deploy it from the IDE only by using the terminal\. To see if parameters are required, on the **Application details** page you opened earlier, choose the **Deploy** button, and then see the **Configure application parameters** card for any parameters\. If there are any parameters, deploy the serverless application from the terminal in the IDE by running the AWS CloudFormation `deploy` command, for example:

```
aws cloudformation deploy --template-file TEMPLATE_FILE_PATH --parameter-overrides "PARAMETER_KEY_1=PARAMETER_VALUE_1" "PARAMETER_KEY_N=PARAMETER_VALUE_N" --region REGION_ID
```

In the preceding command:
+  `TEMPLATE_FILE_PATH` represents the path to the AWS SAM template file\.
+  `PARAMETER_KEY_1` represents the name of the first parameter\.
+  `PARAMETER_VALUE_1` represents the value of the first parameter\.
+  `PARAMETER_KEY_N` represents the name of an additional parameter, and so on\.
+  `PARAMETER_VALUE_N` represents the value of an additional parameter, and so on\.
+  `REGION_ID` represents the ID of the AWS Region where you want to deploy the serverless application \(for example, `us-east-2`\)\.
+ Additional options might need to be specified, depending on the serverless application's requirements\. For more information, see the **Application details** page that you opened earlier, or look for any setup instructions within the serverless application's files that you cloned to your IDE\.

If you try to use the **Lambda** section of the **AWS Resources** window to deploy a serverless application that requires parameters, a message is displayed that required parameters are missing, and the serverless application is not deployed\.

## Import a Lambda Function<a name="lambda-functions-import"></a>

If you have an existing Lambda function in your AWS account but not in your AWS Cloud9 development environment, you must import it before you can work with it in your environment\.

**Note**  
If the Lambda function is part of an existing AWS CodeStar project, and the environment was created from within the project in the AWS CodeStar console, the function is already imported, so you do not need to import it again\.  
To confirm this behavior, look in the **Local Functions** list in the **Lambda** section of the **AWS Resources** window for a serverless application \(represented by a Lambda icon inside of a folder\) with the same name as the AWS CodeStar project, containing a Lambda function \(represented by a Lambda icon by itself\) with the function's base name\. Look also in the **Remote Functions** list for a Lambda function with a name in the format `awscodestar-PROJECT_NAME-lambda-BASE_FUNCTION_NAME-RANDOM_ID`, where `PROJECT_NAME` is the AWS CodeStar project name, `BASE_FUNCTION_NAME` is the function's base name, and `RANDOM_ID` is a randomly determined ID\.  

![\[Both the local and remote functions refer to the same function\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-lambda-codestar.png)
Since the function is already imported, we do not recommend that you import the remote version of the function in the AWS CodeStar project\. Otherwise, you will have two versions of the same function code in your **Environment** window but with different folder names, which could be confusing\.

To import a Lambda function, do the following:

1. In the **Environment** window, choose where you want to import the function\.

1. In the **Lambda** section of the **AWS Resources** window, choose the function's name in the **Remote Functions** list\.
**Note**  
If you don't see your function in the **Remote Functions** list, choose the **Refresh functions List** button \(the button with the circular arrow icon\)\.

1. Do one of the following:
   + Double\-click the function you just chose\.
   + On the menu bar in the **Lambda** section, choose the **Import the selected Lambda function** button \(the button with the arrow that faces down\)\.
   + Right\-click the function you just chose, and then choose **Import**\.  
![\[Importing a Lambda function to use in an AWS Cloud9 development environment\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-lambda-import.png)
**Note**  
You cannot import a Lambda function into a folder that represents either a serverless application or a Lambda function\. If you try to do this, AWS Cloud9 will display a message that it will import the Lambda function into the environment's root location instead\. To let AWS Cloud9 do this, choose **Import**\. Otherwise, choose **Cancel**, choose a different folder to import the function \(or create a new empty folder to import the function into\), and then restart this procedure from the beginning\.

1. When prompted to finish importing the function, choose **OK**\.

AWS Cloud9 imports your function into a new folder in the root of your environment\. \(AWS Cloud9 also adds the function to the **Local Functions** list in the **Lambda** section of the **AWS Resources** window\.\) This folder has the same name as the function\. AWS Cloud9 adds the following files to this folder:
+  `.application.json`: A hidden file used by AWS Cloud9 that contains JSON\-formatted settings specific to the function\.
+  `.gitignore`: A hidden file that contains a list of files Git ignores, if you want to use Git to manage your source code for this function\.
+  `template.yaml`: A file for AWS Cloud9 internal use\.
**Note**  
Although the `template.yaml` file is expressed in AWS SAM format, it isn't used by AWS SAM\. Therefore, you cannot edit this file to create additional supporting AWS resources for your function\. Do not modify this file\.
+ One or more code files containing the function logic\.

The `.application.json` and `.gitignore` files are hidden\. To display or hide hidden files, in the **Environment** window, choose the gear icon, and then choose **Show Hidden Files**\.

To invoke the function, see [Invoke a Lambda Function](#lambda-functions-invoke)\.

## Invoke a Lambda Function<a name="lambda-functions-invoke"></a>

To invoke an existing Lambda function, you must first import the remote version of the function into your AWS Cloud9 development environment, if the function isn't already there\. To do this, see [Import a Lambda Function](#lambda-functions-import)\.

1. In the **Lambda** section of the **AWS Resources** window, expand the **Local Functions** list, if it isn't already expanded\.

1. Expand the serverless application folder that contains the function that you want to invoke\.

1. Choose the function that you want to invoke, right\-click it, and then choose **Run**\.

1. Do one of the following:
   + To run the local version of the function within your environment, choose **Run Local**\.
   + To run the remote version of the function within Lambda, choose **Run Remote**\.  
![\[Choose to run the local or remote version of your function\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-lambda-run-lambda-menu.png)
**Note**  
If nothing appears to happen, an invoke tab might already be open for the function\. If so, choose **Lambda \(local\)** or **Lambda \(remote\)** in the open invoke tab\.

1. In the **Test payload** pane of the invoke tab that is displayed, confirm any custom input data you want your function to use when you test it\. For information about the input data format, see [Step 2\.2: Invoke the Lambda Function Manually and Verify Results, Logs, and Metrics](https://docs.aws.amazon.com/lambda/latest/dg/get-started-invoke-manually.html) in the *AWS Lambda Developer Guide*\.

1. In the invoke tab, choose the **Run** button\.  
![\[Choose to run the function locally within your environment or remotely within Lambda\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-lambda-run-lambda.png)
**Note**  
After you run the function for the first time, a `lambda-payloads.json`: file is added to the function's related serverless application folder in the **Environment** window\. This file contains the contents of the custom input data\.  
If you invoke an existing Lambda function and then try to invoke the same function code for its related API in API Gateway with the same custom input data, you might get an error or the code might not run as expected\. For more information, see [Response Differences When Invoking a Lambda Function from API Gateway](#lambda-functions-vs-api-gateway)\.

The invoke tab contains two panes:
+ The **Test payload** pane displays any custom input data that was supplied for the function\.
+ The **Execution results** pane displays any output from the function and some information from the related Amazon CloudWatch Logs for the function\.

Compare your results to the following:

![\[Invoking a Lambda function\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-lambda-run.gif)

For more information, see [Step 2\.2: Invoke the Lambda Function Manually and Verify Results, Logs, and Metrics](https://docs.aws.amazon.com/lambda/latest/dg/get-started-invoke-manually.html) in the *AWS Lambda Developer Guide*\.

To upload the local version of any changed function code to the related remote version in Lambda, see [Upload Code for a Lambda Function](#lambda-functions-upload-code)\.

## Invoke a Lambda Function that Uses Environment Variables<a name="lambda-functions-invoke-env-vars"></a>

To invoke a Lambda function locally or remotely that uses environment variables, do one of the following\.

**Invoke a Lambda function locally with predefined environment variables and their values**  
Add the predefined environment variable definitions to the function's `template.yaml` file if they are not already there, and then run the **Run Local** command for that function from the **Lambda** section of the **AWS Resources** window\.   
For example, given the following Node\.js function definition in a file named `index.js`:  

```
exports.handler = (event, context, callback) => {
    
    var result = {  
      MY_ENV_VAR_1: process.env.MY_ENV_VAR_1,
      MY_ENV_VAR_2: process.env.MY_ENV_VAR_2 
    };
    
    const response = {
      statusCode: 200,
      headers: { "Content-type": "application/json" },
      body: result
    };
      
    callback(null, response);
    
};
```
And given the following addition to the function's `template.yaml` file one directory above `index.js`:  

```
...
Resources:
  MyEnvVarsFunction:
    Type: 'AWS::Serverless::Function'
    Properties:
      ...
      Environment:
        Variables:
          MY_ENV_VAR_1: "This is my environment variable 1 value from the template.yaml file."
          MY_ENV_VAR_2: "This is my environment variable 2 value from the template.yaml file."
```
And running the **Run Local** command for that function from the **Lambda** section of the **AWS Resources** window, the following is output:  

```
{
  "statusCode": 200,
  "headers": {
    "Content-type": "application/json"
  },
  "body": {
    "MY_ENV_VAR_1": "This is my environment variable 1 value from the template.yaml file.",
    "MY_ENV_VAR_2": "This is my environment variable 2 value from the template.yaml file."
  }
}
```

**Invoke a Lambda function locally with environment variables and their values that the caller provides dynamically at run time**  
You cannot use the **Run Local** command for such a function from the **Lambda** section of the **AWS Resources** window\.   
Instead, add the predefined environment variable definitions to the function's `template.yaml` file if they are not already there\. Then use the terminal in the IDE to run the AWS SAM CLI with the invoke command along with the \-\-env\-vars argument and a separate JSON file that contains the environment variable definitions and their values\.   
For example, given the following Node\.js function named `MyEnvVarsFunction` with its definition in a file named `index.js`:  

```
exports.handler = (event, context, callback) => {
    
  var result = {  
    MY_ENV_VAR_1: process.env.MY_ENV_VAR_1,
    MY_ENV_VAR_2: process.env.MY_ENV_VAR_2 
  };
    
  const response = {
    statusCode: 200,
    headers: { "Content-type": "application/json" },
    body: result
  };
      
  callback(null, response);
    
};
```
And given the following addition to the function's `template.yaml` file one directory above `index.js`:  

```
...
Resources:
  MyEnvVarsFunction:
    Type: 'AWS::Serverless::Function'
    Properties:
      ...
      Environment:
        Variables:
          MY_ENV_VAR_1: "This is my environment variable 1 value from the template.yaml file."
          MY_ENV_VAR_2: "This is my environment variable 2 value from the template.yaml file."
```
And given the following file named `MyEnvVars.json` in the same directory as `index.js`:  

```
{
  "MyEnvVarsFunction": {
    "MY_ENV_VAR_1": "This is my environment variable 1 value from the JSON file.",
    "MY_ENV_VAR_2": "This is my environment variable 2 value from the JSON file."
  }
}
```
And running the following AWS SAM CLI command from the same directory as `index.js`:  

```
sam local invoke --event lambda-payloads.json --template ../template.yaml --env-vars MyEnvVars.json
```
The following is output:  

```
{  
  "statusCode": 200,
  "headers": {
    "Content-type": "application/json"
  },
  "body": {
    "MY_ENV_VAR_1": "This is my environment variable 1 value from the JSON file.",
    "MY_ENV_VAR_2": "This is my environment variable 2 value from the JSON file."
  }
}
```

**Invoke a Lambda function remotely that already has predefined environment variable and their values**  
Run the **Run Remote** command for that function from the **Lambda** section of the **AWS Resources** window\.   
To view or change predefined environment variable values for an existing remote function before you invoke it remotely, see [AWS Lambda Environment Variables](https://docs.aws.amazon.com/lambda/latest/dg/env_variables.html) in the *AWS Lambda Developer Guide*\.

**Invoke a Lambda function remotely with environment variables and their values that the caller provides dynamically at run time**  
You cannot use the **Run Remote** command for such a function from the **Lambda** section of the **AWS Resources** window\.   
Instead, you can use the terminal in the IDE to run the AWS CLI with the lambda command's update\-function\-configuration action and the \-\-environment argument with the environment variable definitions and their values\. Then run the lambda command's invoke action\.   
For example, given the following Node\.js function named `MyEnvVarsFunction` with the following definition and with predefined environment variables named `MY_ENV_VAR_1` and `MY_ENV_VAR_2`:   

```
exports.handler = (event, context, callback) => {
    
  var result = {  
    MY_ENV_VAR_1: process.env.MY_ENV_VAR_1,
    MY_ENV_VAR_2: process.env.MY_ENV_VAR_2 
  };
    
  const response = {
    statusCode: 200,
    headers: { "Content-type": "application/json" },
    body: result
  };
      
  callback(null, response);
    
};
```
And running the following AWS CLI commands, one at a time in the following order:  

```
aws lambda update-function-configuration --function-name MyEnvVarsFunction --environment '{"Variables":{"MY_ENV_VAR_1":"This is my environment variable 1 value from the AWS CLI.","MY_ENV_VAR_2":"This is my environment variable 2 value from the AWS CLI."}}'

aws lambda invoke --function-name MyEnvVarsFunction results.json
```
The following is output to a file named `results.json`:  

```
{
  "statusCode": 200,
  "headers": {
    "Content-type": "application/json"
  },
  "body": {
    "MY_ENV_VAR_1": "This is my environment variable 1 value from the AWS CLI.",
    "MY_ENV_VAR_2": "This is my environment variable 2 value from the AWS CLI."  
  }
}
```
For more details, see the discussion of update\-function\-configuration and invoke in [Create the Lambda function and Test It](https://docs.aws.amazon.com/lambda/latest/dg/tutorial-env_cli.html#with-env-create-function) in the *AWS Lambda Developer Guide*\.

## Working with Lambda Functions that Use Versions, Aliases, or Layers<a name="lambda-functions-versions-aliases-layers"></a>

The **Lambda** section of the **AWS Resources** window currently does not provide any features for working with versions, aliases, or layers for Lambda functions\. Instead, you can use the terminal in the IDE to run the AWS CLI and AWS SAM CLI with the corresponding commands, actions, and arguments\. For details, see the following\.
+ [Introduction to AWS Lambda Versioning](https://docs.aws.amazon.com/lambda/latest/dg/versioning-intro.html) in the *AWS Lambda Developer Guide*
+ [Introduction to AWS Lambda Aliases](https://docs.aws.amazon.com/lambda/latest/dg/aliases-intro.html) in the *AWS Lambda Developer Guide*
+ [Managing Versioning Using the AWS Management Console, the AWS CLI, or Lambda API Operations](https://docs.aws.amazon.com/lambda/latest/dg/how-to-manage-versioning.html) in the *AWS Lambda Developer Guide*
+ [AWS Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) in the *AWS Lambda Developer Guide*
+ [Working with Layers](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-layers.html) in the *AWS Serverless Application Model Developer Guide*
+ [AWS::Serverless::LayerVersion](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-template.html#serverless-sam-template-layerversion) in the *AWS Serverless Application Model Developer Guide*

## Invoke an API Gateway API for a Related Lambda Function<a name="lambda-functions-api"></a>

To invoke an API in API Gateway that is related to an existing Lambda function, you must first import the remote version of the function into your AWS Cloud9 development environment, if the function isn't already there\. To do this, see [Import a Lambda Function](#lambda-functions-import)\.

**Note**  
You cannot debug the remote version of the API Gateway API in your environment\. You can only invoke it\. To debug the local version, see [Debug the Local Version of a Lambda Function or Its Related API Gateway API](#lambda-functions-debug)\.

1. In the **Lambda** section of the **AWS Resources** window, expand the **Local Functions** list, if it isn't already expanded\.

1. Expand the serverless application folder that contains the function whose API you want to invoke\.

1. Choose the function, right\-click it, and then choose **Run**\.

1. Do one of the following:
   + To run the local version of the API within your environment, choose **Run API Gateway Local**\.
   + To run the remote version of the function within Lambda, choose **Run API Gateway Remote**\.
**Note**  
If nothing appears to happen, an invoke tab might already be open for the function\. If so, choose **API Gateway \(local\)** or **API Gateway \(remote\)** in the open invoke tab\.

1. In the **Test payload** pane of the invoke tab that is displayed, confirm the **Function**, **Path**, **Method**, **Query String**, and **Body** you want the API to use when you test it\.
**Note**  
Some APIs might not support settings such as **Body**\. For more information, consult the owner of the API\.

1. On the invoke tab, choose the **Run** button\.  
![\[Choose run on the invoke tab\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-lambda-run-api.png)
**Note**  
If the API isn't connected to the function, a message appears that says an API Gateway trigger can't be found in the function's AWS SAM file\. To use this AWS SAM file to connect an API in API Gateway to the function, see the [AWS Serverless Application Model \(AWS SAM\)](https://github.com/awslabs/serverless-application-model) repository on GitHub\.  
If you invoke an API in API Gateway and then try to invoke the same code for its related function in Lambda with the same custom input data, you might get an error or the code might not run as expected\. For more information, see [Response Differences When Invoking a Lambda Function from API Gateway](#lambda-functions-vs-api-gateway)\.

The invoke tab contains two panes:
+ The **Test payload** pane displays settings and any custom input data that was supplied for the API\.
+ The **Execution results** pane displays information such as the body, headers, and logs of the API response\.

Compare your results to the following:

![\[Invoking an API in API Gateway\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-lambda-api.gif)

## Response Differences When Invoking a Lambda Function from API Gateway<a name="lambda-functions-vs-api-gateway"></a>

When you invoke a Lambda function from an API in API Gateway and then try to parse the response, you might get an error or the code might not run as expected\. This is because Lambda and API Gateway use slightly different response formats\. Specifically, API Gateway wraps its response in a parent `body` object\. To address this issue, you can add code to a function that checks to see if a parent `body` exists in the response\. If it does, you can then extract the data from that `body` object\.

For example, given the following Node\.js function code:

```
'use strict';

exports.handler = function(event, context, callback) {

  if (event.body) {
    event = JSON.parse(event.body);
  }

  const message = "Your favorite fruit is " + event.fruit + ". " +
    "Your favorite vegetable is " + event.vegetable + ".";

  const response = {
    statusCode: 200,
    headers: { "Content-type": "application/json" },
    body: JSON.stringify( { "message": message } )
  };

  callback(null, response);
};
```

And given the following equivalent Python function code:

```
import json

def lambda_handler(event, context):

  if 'body' in event:
    event = json.loads(event["body"])

  message = ("Your favorite fruit is " + event["fruit"] + ". " +
    "Your favorite vegetable is " + event["vegetable"] + ".")

  response = {
    "statusCode": "200",
    "headers": { "Content-type": "application/json" },
    "body": json.dumps({"message": message})
  }

  return response
```

To invoke the preceding code, you use the following input payload \(for Lambda\) or input body \(for API Gateway\):

```
{
  "fruit": "apple",
  "vegetable": "carrot"
}
```

Which returns the following response for Lambda:

```
{
  "statusCode": 200,
  "headers": {
    "Content-type": "application/json"
  },
  "body": "{\"message\":\"Your favorite fruit is apple. Your favorite vegetable is carrot.\"}"
}
```

And returns the following response for API Gateway \(assuming a **Path** of **/** and a **Method** of **POST**\):

```
{
  "message": "Your favorite fruit is apple. Your favorite vegetable is carrot."
}
```

If you do not include the `if (event.body)` check for Node\.js or the `if 'body' in event` check for Python, then calling this function from API Gateway might return an error or the API might not run as expected\.

## Add Dependent Code to a Lambda Function<a name="lambda-functions-adding-packages"></a>

For Node\.js, we support using Node Package Manager \(npm\) to add dependent packages to Lambda functions in your environment\. For Python, we support pip\. For general information about npm and pip, see the [npm](https://www.npmjs.com/) and [pip](https://pip.pypa.io) websites\.

To depend on an npm package from a Node\.js Lambda function, use for example the Node\.js `require` statement\. Then use npm to install the related npm package in the environment within the same directory as the function code\. When you deploy the Lambda function as described in [Upload Code for a Lambda Function](#lambda-functions-upload-code), AWS Cloud9 deploys both the function and its related packages to Lambda\.

To demonstrate, the following example Node\.js Lambda function code depends on the `lodash` package to sort the specified JSON input payload\.

```
'use strict';

/*
Assume the following payload is input:

[
  {
    "firstName": "Shirley",
    "lastName": "Rodriguez"
  },
  {
    "firstName": "Jane",
    "lastName": "Doe"
  },
  {
    "firstName": "Arnav",
    "lastName": "Desai"
  }
]

The expected response is:

{
  "statusCode": 200,
  "headers": {
    "Content-type": "application/json"
  },
  "body": {
    "result": [
      {
        "firstName": "Arnav",
        "lastName": "Desai"
      },
      {
        "firstName": "Jane",
        "lastName": "Doe"
      },
      {
        "firstName": "Shirley",
        "lastName": "Rodriguez"
      }
    ]
  }
}
*/

exports.handler = (event, context, callback) => {

  var lodash = require('lodash');
  var result = lodash.orderBy(event, ['firstName'], ['asc']);

  const response = {
    statusCode: 200,
    headers: { "Content-type": "application/json" },
    body: JSON.stringify( { "result": result } )
  };

  callback(null, response);
};
```

To install the `lodash` package in the environment, use a terminal session in the IDE to change to the directory containing the function code\. Then run the following two commands, in the following order\. The first command creates and configure a `package.json` file in that directory to make sure when you deploy the function to Lambda, the `lodash` package is also deployed\. The second command installs the `lodash` package in the same directory in the environment as the function code and then updates the `package.json` file in that directory accordingly\.

```
npm init
npm install lodash --save
```

For help with the `npm init` command and the `package.json` file, see [Working with package\.json](https://docs.npmjs.com/getting-started/using-a-package.json) on the npm website\.

From the IDE, invoke the local version of the Lambda function, as described in [Invoke a Lambda Function](#lambda-functions-invoke)\. Deploy the function as described in [Upload Code for a Lambda Function](#lambda-functions-upload-code), and then invoke the remote version of the function\. The local and remote versions of the function should work as expected\.

To depend on a pip package from a Python Lambda function, use for example the Python `import` statement\. Then use pip to install the related pip package in the environment **one directory above** the directory that contains the function code\. When you deploy the Lambda function as described in [Upload Code for a Lambda Function](#lambda-functions-upload-code), AWS Cloud9 deploys both the function and its related packages to Lambda\.

To demonstrate, the following example Python Lambda function code depends on the `requests` package to make an HTTP request and then return information about the related HTTP response\.

```
'''
Assume the following payload is input:

{
  "url": "https://aws.amazon.com"
}

The expected response is similar to the following:

{
  "statusCode": "200",
  "headers": {
    "Content-type": "application/json"
  },
  "body": {
    "statusCode": 200,
    "date": "Fri, 19 Jan 2018 17:57:48 GMT",
    "lastModified": "Thu, 18 Jan 2018 18:08:23 GMT"
  }
}
'''

import requests
import json

def lambda_handler(event, context):

  result = requests.get(event["url"])

  response = {
    "statusCode": "200",
    "headers": { "Content-type": "application/json" },
    "body": json.dumps( { "statusCode": result.status_code,
      "date": result.headers["Date"],
      "lastModified": result.headers["Last-Modified"] } )
  }

 return response
```

To install the `requests` package in the environment, use a terminal session in the IDE to change to the directory containing the function code\. Then run the following command\. This command installs the `requests` package in the directory in the environment that is **one directory above** the function code\.

```
pip install requests --target ../
```

From the IDE, invoke the local version of the Lambda function, as described in [Invoke a Lambda Function](#lambda-functions-invoke)\. Deploy the function as described in [Upload Code for a Lambda Function](#lambda-functions-upload-code), and then invoke the remote version of the function\. The local and remote versions of the function should work as expected\.

For a Python Lambda function, to depend on code in a separate Python code file that is in the same directory as the function, use the `from` and `import` statements\. When you deploy the Lambda function as described in [Upload Code for a Lambda Function](#lambda-functions-upload-code), AWS Cloud9 deploys to Lambda both the function and the separate Python code files in the same directory as the function\.

To demonstrate, take for example the following directory structure in the AWS Cloud9 IDE for a Python Lambda function:

```
myDemoServerlessApplication
  `- myDemoFunction
       |- lambda-payloads.json
       |- lambda_function.py
       `- myClasses.py
```

If the `myClasses.py` file contains the definition of a class named `MyClass1`, for example:

```
class MyClass1:
  # Class definition...
```

To reference the `MyClass1` class from the `lambda_function.py` file, add the following statement to the file:

```
from myDemoFunction.myClasses import MyClass1
```

## Debug the Local Version of a Lambda Function or Its Related API Gateway API<a name="lambda-functions-debug"></a>

You can debug local Lambda function code or its related API Gateway API in your environment using common debugging aids such as breakpoints, stepping through code, and setting watch expressions\.

**Note**  
You cannot debug the remote version of a Lambda function or its related API Gateway API in your environment\. You can only invoke it\.

To debug the local version of an existing Lambda function or its related API Gateway API, you must first import the remote version of the function into your AWS Cloud9 development environment, if the function isn't already there\. See [Import a Lambda Function](#lambda-functions-import)\.

**Important**  
If you import the remote version of a Python function into your environment, you must choose one of the following options before you can debug it:  
 **Option 1: If the Python function doesn't use venv, use pip to install IKPdb into the same directory as the function's template\.yaml file\.**   
Use a terminal session in the IDE to change to the directory containing the function's `template.yaml` file\. Then run one of the following commands\. This command installs the Python debugger IKPdb in the same directory as the function's `template.yaml` file:  

```
pip install ikpdb --target .      # For a function that uses Python 2.7.
pip-3.6 install ikp3db --target . # For a function that uses Python 3.6.
```
 **Option 2: If the Python function uses venv, use pip in venv to install IKPdb into the function's venv directory, and then add the CodeUri property to the function's template\.yaml file\.**   
Use a terminal session in the IDE to change to the directory containing the function's `template.yaml` file\. From that folder, run one of the following commands\. This command uses pip in the function's `venv/bin` directory to install the Python debugger IKPdb into the function's `venv/lib/pythonMAJOR.MINOR/dist-packages` directory:  

   ```
   venv/bin/pip install ikpdb       # For a function that uses Python 2.7.
   venv/bin/pip3.6 install ikp3db   # For a function that uses Python 3.6.
   ```
In the **Environment** window, open the function's `template.yaml` file for editing\. In the `Properties` section for the function, add the `CodeUri` property, set its value to `.debug/`, and then save the file\. For example:  

   ```
   AWSTemplateFormatVersion: '2010-09-09'
   Transform: 'AWS::Serverless-2016-10-31'
   Description: An AWS Serverless Specification template describing your function.
   Resources:
     myDemoFunction:
       Type: 'AWS::Serverless::Function'
       Properties:
         CodeUri: .debug/
         # ...
   ```

1. In the **Environment** window, open the file that contains the Lambda function's code you want to debug\.

1. Set any breakpoints and watch expressions for your code\. See [Debug Your Code](build-run-debug.md#build-run-debug-debug)\.

1. In the **Lambda** section of the **AWS Resources** window, expand the **Local Functions** list, if it isn't already expanded\.

1. Expand the serverless application folder that contains the function you want to debug\.

1. Choose the function to debug, right\-click it, and then choose **Run, Run Local** or **Run, Run API Gateway Local**\.
**Note**  
If nothing appears to happen, an invoke tab might already be open for the function\. If so, go to the open invoke tab and choose **Lambda \(local\)** or **API Gateway \(local\)**\.

1. For a Lambda function, in the **Test payload** pane of the invoke tab that is displayed, confirm any custom input data you want your function to use when you test it\. For information about the input data format, see [Step 2\.2: Invoke the Lambda Function Manually and Verify Results, Logs, and Metrics](https://docs.aws.amazon.com/lambda/latest/dg/get-started-invoke-manually.html) in the *AWS Lambda Developer Guide*\.

1. For an API Gateway API, in the **Test payload** pane of the invoke tab that is displayed, confirm the **Path**, **Method**, **Query String**, and **Body** you want the API to use when you test it\.
**Note**  
Some APIs might not support settings such as **Body**\. For more information, consult the owner of the API\.

1. Next to the **Run** button, choose **Run in Debug Mode** \(the bug icon\)\.

1. Choose the **Run** button\.

1. Decide what to do whenever function execution pauses at a breakpoint\. See [Debug Your Code](build-run-debug.md#build-run-debug-debug)\.

![\[Choose what happens when your function execution pauses at a breakpoint\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-lambda-debug.png)

Compare your results to the following:

![\[Debugging a Lambda function\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-lambda-debug.gif)

## Change Code in a Lambda Function<a name="lambda-functions-change-code"></a>

To use the AWS Cloud9 IDE to change the code in a function, you must first import the related remote version of the function into your AWS Cloud9 development environment, if the function isn't already there\. To do this, see [Import a Lambda Function](#lambda-functions-import)\. Then do the following:

1. In the **Lambda** section of the **AWS Resources** window, expand the **Local Functions** list, if it isn't already expanded\.

1. Expand the serverless application folder that contains the function whose code you want to change\.

1. Right\-click the function, and then choose **Edit Function**\.  
![\[Lambda section of the AWS Resources window\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-lambda-edit.png)

1. Make the changes you want to the code, and then save the file\.

To upload the local version of the changed function code to the related remote version in Lambda, see [Upload Code for a Lambda Function](#lambda-functions-upload-code)\.

## Upload Code for a Lambda Function<a name="lambda-functions-upload-code"></a>

To upload the local version of a Lambda function in your environment to the related remote version of the function in Lambda, follow one of these procedures, depending on how the function was created\.


****  

|  **How was the function created?**  |  **Follow this procedure**  | 
| --- | --- | 
|  By using the **Create serverless application** wizard in the IDE\.  |   [Upload Code for a Lambda Function Created By the Create Serverless Application Wizard](#lambda-function-upload-code-wizard)   | 
|  As part of an AWS CodeStar project\.  |   [Upload Code for a Lambda Function That is Part of an AWS CodeStar Project](#lambda-function-upload-codestar)   | 
|  By using the AWS Serverless Application Repository, and the serverless application requires parameters to be specified during deployment\.  |   [Upload Code for a Lambda Function That is Part of an AWS Serverless Application Repository Project with Parameters](#lambda-function-upload-code-sam-params)   | 
|  Any other way\.  |   [Upload Code for a Lambda Function By Using a Specific AWS CloudFormation Stack, Function Name, or Both](#lambda-function-upload-code-specify)   | 

### Upload Code for a Lambda Function Created By the Create Serverless Application Wizard<a name="lambda-function-upload-code-wizard"></a>

After you [Create a Lambda Function With the Create Serverless Application Wizard](#lambda-functions-create) in your environment, you can upload the local version of that function to the related remote version of the function in Lambda as follows\.

1. In the **Lambda** section of the **AWS Resources** window, expand the **Local Functions** list, if it isn't already expanded\.

1. Expand the serverless application folder that contains the function you want to upload\.

1. Do one of the following:
   + Right\-click the serverless application folder that you just chose, and then choose **Deploy**\.
   + Right\-click the function you want to upload, and then choose **Deploy**\.
   + Choose the function you want to upload, and then choose **Deploy the selected Lambda function** \(the button with the arrow that faces up\)\.  
![\[Upload command in the Lambda section of the AWS Resources window\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-lambda-upload.png)

### Upload Code for a Lambda Function That is Part of an AWS CodeStar Project<a name="lambda-function-upload-codestar"></a>

As you are [Working with AWS CodeStar Projects in the AWS Cloud9 Integrated Development Environment \(IDE\)](codestar-projects.md), you can upload the local version of that function in your environment to the related remote version of the function in Lambda as follows\.

Use a terminal session in the IDE to run the `git push` command to push committed code changes to the repository for the AWS CodeStar project\. This instructs AWS CodeStar to upload the local version of the Lambda function in your environment to the related remote version of the function in Lambda\.

If you do not follow this procedure, the error "Parameters: \[ProjectId\] must have values" will display, and the function will not deploy\.

### Upload Code for a Lambda Function That is Part of an AWS Serverless Application Repository Project with Parameters<a name="lambda-function-upload-code-sam-params"></a>

If you [Create and Deploy Lambda Functions with the AWS Serverless Application Repository](#lambda-functions-create-repo), and that project requires you to specify parameters during the upload, see coverage of the AWS CloudFormation `deploy` command in [Create and Deploy Lambda Functions with the AWS Serverless Application Repository](#lambda-functions-create-repo) for upload instructions\.

If you do not follow that procedure, an error will display that required parameters are missing, and the code will not upload\.

### Upload Code for a Lambda Function By Using a Specific AWS CloudFormation Stack, Function Name, or Both<a name="lambda-function-upload-code-specify"></a>

To begin the upload process, AWS Cloud9 instructs AWS CloudFormation to create a stack with a specific name\. AWS CloudFormation uses the information in this stack to complete the upload of the local version of the Lambda function in your environment to a specific function in Lambda\. By default, the name of this stack and the name of the Lambda function is one of the following, which you can change if needed\.
+ If a hidden `.application.json` file exists in the same folder as the local version of the Lambda function, and the file contains a `StackName` value, the stack's name is the same as the `StackName` value, and the Lambda function name is `cloud9-APPLICATION_NAME-FUNCTION_NAME`\.
+ If there is no hidden `.application.json` file in the same folder as the local version of the Lambda function, or if the `application.json` file exists but has no `StackName` value, the stack's name is `cloud9-FOLDER_NAME`, and the Lambda function name is `cloud9-APPLICATION_NAME-FUNCTION_NAME`\.

In the preceding stack and function names, `FOLDER_NAME` is the name of the related folder in the **Environment** window, while `APPLICATION_NAME` and `FUNCTION_NAME` are the related values as displayed in the **Lambda** section of the **AWS Resources** window\.

If you do not want to change the name of the default AWS CloudFormation stack or the default function name in Lambda, then skip ahead to the upload procedure at the end of this section\.

To use or create a non\-default AWS CloudFormation stack in your AWS account in the same AWS Region as displayed in the **Lambda** section of the **AWS Resources** window, do one of the following\.
+ If you want to use an existing AWS CloudFormation stack to upload the code, then in the **Lambda** section of the **AWS Resources** window, right\-click the serverless application folder that contains the Lambda function you want to upload the code to, choose **Link to CloudFormation Stack**, and follow the on\-screen instructions to choose the existing stack to use\.
**Note**  
You can only choose from existing stacks that are in the following AWS CloudFormation states\.  
 `CREATE_COMPLETE` 
 `CREATE_IN_PROGRESS` 
 `REVIEW_IN_PROGRESS` 
 `ROLLBACK_COMPLETE` 
 `ROLLBACK_IN_PROGRESS` 
 `UPDATE_COMPLETE` 
 `UPDATE_COMPLETE_CLEANUP_IN_PROGRESS` 
 `UPDATE_IN_PROGRESS` 
 `UPDATE_ROLLBACK_COMPLETE` 
 `UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS` 
 `UPDATE_ROLLBACK_IN_PROGRESS` 
+ If you want to create a new AWS CloudFormation stack with a name that you specify, then do one of the following:
  + If a hidden `.application.json` file exists in the same folder as the local version of the Lambda function, and the file contains a `StackName` value, change the `StackName` value in the `.application.json` file to the name of the AWS CloudFormation stack you want to use, and then save the `.application.json` file\.
  + If a hidden `.application.json` file exists in the same folder as the local version of the Lambda function, but the file does not contain a `StackName` value, add a `StackName` value to the beginning of the `.application.json` file with the name of the new AWS CloudFormation stack you want to use, and then save the `.application.json` file\. For example, for a stack name of `MyDemoStack`, add the following value to the beginning of the file\. \(Do not type the ellipses\. They are shown only to help you add the value to the correct location in the file\.\)

    ```
    {
      "StackName": "MyDemoStack",
      ...
    }
    ```
  + If a hidden `.application.json` file does not exist in the same folder as the local version of the Lambda function, then create a new `.application.json` file in that folder, add a `StackName` value to the `.application.json` file with the name of the new AWS CloudFormation stack you want to use, and then save the `.application.json` file\. For example, for a stack name of `MyDemoStack`, add the following value to the file\.

    ```
    {
      "StackName": "MyDemoStack"
    }
    ```

To upload the code to a non\-default Lambda function in your AWS account in the same AWS Region as displayed in the **Lambda** section of the **AWS Resources** window, add the function name as a `FunctionName` value to the `Properties` section of the Lambda function resource in the related AWS SAM template file \(for example, `template.yaml`\)\. For example, for a Lambda function resource named `MyDemoFunction`, add a `FunctionName` value of `MyDemoFunction` to upload the code to a Lambda function named `MyDemoFunction` instead of `cloud9-APPLICATION_NAME-FUNCTION_NAME`\. \(Do not type the ellipses\. They are shown only to help you add the value to the correct location in the file\.\)

```
...
Resources:
  MyDemoFunction:
    Type: AWS::Serverless::Function
    Properties:
      FunctionName: MyDemoFunction
      ...
```

When you are ready to upload the code, do the following\.

1. In the **Lambda** section of the **AWS Resources** window, expand the **Local Functions** list, if it isn't already expanded\.

1. Expand the serverless application folder that contains the function you want to upload\.

1. Do one of the following:
   + Right\-click the serverless application folder that you just chose, and then choose **Deploy**\.
   + Right\-click the function you want to upload, and then choose **Deploy**\.
   + Choose the function you want to upload, and then choose **Deploy the selected Lambda function** \(the button with the arrow that faces up\)\.  
![\[Upload command in the Lambda section of the AWS Resources window\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-lambda-upload.png)

## Convert a Lambda Function to a Serverless Application<a name="lambda-functions-convert-to-sam"></a>

If the local version of an existing Lambda function in your AWS Cloud9 development environment isn't already part of a serverless application, you can use the AWS Cloud9 IDE to convert that function into a serverless application\. You can then use the AWS SAM template file for that serverless application to create additional supporting AWS resources for your function\. For more information, see the [AWS Serverless Application Model \(AWS SAM\)](https://github.com/awslabs/serverless-application-model) repository on GitHub\.

To convert the local version of an existing Lambda function into a serverless application, you must first import the remote version of the function into your AWS Cloud9 development environment, if the function isn't already there\. See [Import a Lambda Function](#lambda-functions-import)\.

1. In the **Lambda** section of the **AWS Resources** window, expand the **Local Functions** list, if it isn't already expanded\.

1. Right\-click the function you want to convert, and then choose **Convert to SAM**\.  
![\[Convert to SAM command in the Lambda section of the AWS Resources window\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-lambda-convert.png)

AWS Cloud9 does the following:
+ In the function's folder in the **Environment** window, the `DeploymentMethod` setting in the `.application.json` file changes from `lambda` to `cloudformation`\. This means that now AWS Cloud9 will instruct AWS SAM to use AWS CloudFormation whenever you use the IDE to upload the function's code as part of the serverless application\. \(`lambda` means that AWS Cloud9 will instruct Lambda to deploy the function instead\.\) To upload the function code, see [Upload Code for a Lambda Function](#lambda-functions-upload-code)\.
+ In the **Lambda** section of the **AWS Resources** window, in the **Local Functions** list, AWS Cloud9 adds the existing Lambda function to a new serverless application \(represented by a Lambda icon inside of a folder\)\. The serverless application has the same name as the function\.

When you upload the function's code as described in [Upload Code for a Lambda Function](#lambda-functions-upload-code), because the function upload method is no longer Lambda but now AWS SAM using AWS CloudFormation, AWS Cloud9 creates a new remote version of the function in Lambda and adds it to the **Remote Functions** list\. AWS Cloud9 gives the remote version a name that is different from the original Lambda function\. For example, if the serverless application and the function are both named `myDemoFunction`, the remote version name of your function would be `cloud9-myDemoFunction-myDemoFunction-RANDOM_ID`, where `RANDOM_ID` is a randomly determined ID\.

**Important**  
After you do the conversion, if you then use the IDE to make any changes to the function code and then upload that code to Lambda, only the remote version of the new function \(for example, `cloud9-myDemoFunction-myDemoFunction-RANDOM_ID`\) will contain the change\. The remote version of the original function \(for example, `myDemoFunction`\) will not change\.  
If you change your mind and want to enable the IDE to go back to uploading your code changes to the remote version of the original function \(for example, `myDemoFunction`\), do the following:  
In the function's folder in the **Environment** window, change the `DeploymentMethod` setting in the `.application.json` file from `cloudformation` back to `lambda`, and then save the file\. This removes the serverless application folder from the **Local Functions** list and causes AWS Cloud9 to go back to instructing Lambda to deploy the function\.
Upload the function code as described in [Upload Code for a Lambda Function](#lambda-functions-upload-code)\. Now, only the remote version of the original function \(for example, `myDemoFunction`\) will contain the change\. The remote version of the new function \(for example, `cloud9-myDemoFunction-myDemoFunction-RANDOM_ID`\) will not change\.
Because AWS Cloud9 will no longer upload code changes to the remote version of the new function \(for example, `cloud9-myDemoFunction-myDemoFunction-RANDOM_ID`\), if you want you can use the Lambda console to delete the new function \(for example, `cloud9-myDemoFunction-myDemoFunction-RANDOM_ID`\)\.

## Update Configuration Settings for a Lambda Function<a name="lambda-functions-update-settings"></a>

You can use the AWS Cloud9 IDE to change function settings such as the description, handler identifier, amount of memory the function will use, and existing execution role the function will use\.

To change configuration settings, you must first import the related remote version of the function into your AWS Cloud9 development environment, if the function isn't already there\. To do this, see [Import a Lambda Function](#lambda-functions-import)\. Then do the following\.

1. In the **Lambda** section of the **AWS Resources** window, expand the **Local Functions** list, if it isn't already expanded\.

1. Expand the serverless application folder that contains the function whose setting you want to change\.

1. Right\-click the function, and then choose **Edit Config**\.  
![\[Update configuration settings for a Lambda function in the Lambda section of the AWS Resources window\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-lambda-config.png)

1. Make changes to the configuration settings, and then save the file\.
**Note**  
By default, configuration settings are displayed in plain text\. To change this behavior to display configuration settings in a visual editor by default, choose **AWS Cloud9, Preferences** on the menu bar\. Choose **AWS Settings**, and then turn on **Use AWS SAM visual editor**\. To use the visual editor, close the function's `template.yaml` file, and then right\-click the function and choose **Edit Config** again\. To switch back to using plain text by default, turn off the **Use AWS SAM visual editor** setting\. To temporarily edit plain text, choose **View with text editor \(Ace\)** in the visual editor, and then choose **View, Editors, Ace** on the menu bar\.

1. Do one of the following:
   + On the configuration settings tab, in the simplified settings view, choose the **Upload Settings to Lambda** button\.
   + Follow the instructions in [Upload Code for a Lambda Function](#lambda-functions-upload-code)\.  
![\[Upload settings to Lambda or upload code for a Lambda function using the configuration settings tab\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-lambda-config-edit.png)

## Delete a Lambda Function<a name="lambda-functions-delete"></a>

You can delete the local version of a Lambda function from your environment, delete the remote version of the function from Lambda, or both, as follows\.

**Topics**
+ [Delete the Local Version of a Lambda Function](#lambda-functions-delete-local)
+ [Delete the Remote Version of the Lambda Function](#lambda-functions-delete-remote)

### Delete the Local Version of a Lambda Function<a name="lambda-functions-delete-local"></a>

Use the **Environment** window in the AWS Cloud9 IDE to delete the directory that contains the function\. \(You cannot use the **Lambda** section of the **AWS Resources** window in the AWS Cloud9 IDE to delete the local version of a Lambda function\.\)

**Warning**  
If you accidentally delete the local version of a Lambda function, the only way to add it back to your environment is to import the remote version of the function into your environment, if the remote version still exists\. For instructions, see [Import a Lambda Function](#lambda-functions-import)\.

### Delete the Remote Version of the Lambda Function<a name="lambda-functions-delete-remote"></a>

To delete the remote version of the Lambda function, use the Lambda console, the AWS CloudFormation console, or code\. \(You cannot use the **Lambda** section of the **AWS Resources** window in the AWS Cloud9 IDE to delete the remote version of a Lambda function\.\)

To determine which approach to use to delete the remote version of a Lambda function, in the AWS Cloud9 IDE, open the `.application.json` file that is in the same directory as the local version of the Lambda function\. If the `DeploymentMethod` value is set to `lambda`, you use Lambda to delete the function\. If the `DeploymentMethod` value is set to `cloudformation`, you should use AWS CloudFormation to delete the function\.

**Note**  
If the `DeploymentMethod` value is set to `cloudformation` in the `.application.json` file, we do not recommend using Lambda to delete the function\. If you use Lambda instead of AWS CloudFormation to delete the function in this case, then you might leave some associated AWS resources still remaining\. Those remaining resources could result in ongoing charges to your AWS account\.

**Topics**
+ [Use Lambda to Delete the Remote Version of the Function](#lambda-functions-delete-remote-lambda)
+ [Use AWS CloudFormation to Delete the Remote Version of the Function](#lambda-functions-delete-remote-cloudformation)

#### Use Lambda to Delete the Remote Version of the Function<a name="lambda-functions-delete-remote-lambda"></a>

Use the Lambda console or code to delete the function that has the same name as the function in the **Lambda** section of the **AWS Resources** window or the `PhysicalId` value in the `.application.json` file, as follows\.

**Warning**  
When you delete the remote version of a function, it is permanently deleted from Lambda\. If you accidentally delete the remote version of a function and need to recover it, you can upload the local version of the function to Lambda, if the local version still exists\. For instructions, see [Upload Code for a Lambda Function](#lambda-functions-upload-code)\.
+ To delete the function by using the Lambda console, do the following\.

  1. Open the Lambda console, at [https://console\.aws\.amazon\.com/lambda](https://console.aws.amazon.com/lambda)\.

  1. On the AWS navigation bar, if the AWS Region that contains the Lambda function is not displayed, then choose it\.

  1. If the list of functions is not displayed, then choose **Functions** in the service navigation pane\.

  1. Do one of the following\.
     + Choose the radio button next to the name of the function that you want to delete\. Then choose **Actions, Delete**\. Confirm the deletion by choosing **Delete**\.
     + Choose the name of the function that you want to delete\. Then choose **Actions, Delete Function**\. Confirm the deletion by choosing **Delete**\.
+ To delete the function by using code, call the Lambda delete function operation, as follows\.  
****    
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/lambda-functions.html)

#### Use AWS CloudFormation to Delete the Remote Version of the Function<a name="lambda-functions-delete-remote-cloudformation"></a>

Use the AWS CloudFormation console or code to delete the stack that has the same name as the `StackName` value in the `.application.json` file, as follows\.

**Warning**  
When you delete a stack, AWS CloudFormation deletes all AWS resources that are associated with that stack\. This includes not only Lambda functions but could also include other related resources such as APIs in Amazon API Gateway\. If you accidentally delete the remote version of a function and need to recover it, you can upload the local version of the function from the AWS Cloud9 IDE to Lambda, if the local version still exists\. For instructions, see [Upload Code for a Lambda Function](#lambda-functions-upload-code)\. All of the stack's other resources are permanently deleted and cannot be recovered\.
+ To delete the stack by using the AWS CloudFormation console, do the following\.

  1. Open the AWS CloudFormation console, at [https://console\.aws\.amazon\.com/cloudformation](https://console.aws.amazon.com/cloudformation)\.

  1. On the AWS navigation bar, if the AWS Region that contains the stack is not displayed, then choose it\.

  1. In the list of stacks, do one of the following\.
     + Select the check box next to the name of the stack that you want to delete\. Then choose **Actions, Delete Stack**\. Confirm the deletion by choosing **Yes, Delete**\.
     + Choose the name of the stack that you want to delete\. Then choose **Other Actions, Delete Stack**\. Confirm the deletion by choosing **Yes, Delete**\.
+ To delete the stack by using code, call the AWS CloudFormation delete stack operation, as follows\.  
****    
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/lambda-functions.html)