# Working with AWS serverless applications using the AWS Toolkit<a name="serverless-apps-toolkit"></a>

The AWS Toolkit provides support for [serverless applications](https://aws.amazon.com/serverless/)\. Using the AWS Toolkit, you can create serverless applications that contain [AWS Lambda](https://aws.amazon.com/lambda/) functions, and then deploy the applications to an AWS CloudFormation stack\.

**Topics**
+ [Creating a serverless application](#sam-create)
+ [Running and debugging serverless applications](#sam-run-debug)
+ [Deploying a serverless application](#deploy-serverless-app)
+ [Enabling AWS Toolkit code lenses](#enable-code-lenses)
+ [Deleting a serverless application from the AWS Cloud](#delete-serverless-app)
+ [Configuration options for debugging serverless applications](sam-debug-config-ref.md)

## Creating a serverless application<a name="sam-create"></a>

This example shows how to use the AWS Toolkit to create a serverless application\. For information about how to run and debug serverless applications, see [Running and debugging serverless applications](#sam-run-debug)\.

The necessary prerequisites for creating a serverless application include the **AWS SAM CLI** and the **AWS CLI**\. These are included with AWS Cloud9\.

### Create a serverless application with the AWS Toolkit<a name="create-serverless-app"></a>

This example shows how to create a serverless application with the AWS Toolkit by using the [AWS Serverless Application Model \(AWS SAM\)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)\.

1. In the **AWS Explorer**, open the context \(right\-click\) menu for the **Lambda** node, and then choose **Create Lambda SAM Application**\. 
**Note**  
Alternatively, you can select the menu icon across from the **AWS: Explorer** heading, and choose **Create Lambda SAM Application**\.

1. Choose the runtime for your SAM application\. For this example, choose **nodejs12\.x**\.
**Note**  
If you select one of the runtimes with "\(Image\)," your application is package type `Image`\. If you select one of the runtimes without "\(Image\)," your application is the `Zip` type\. For more information about the difference between `Image` and `Zip` package types, see [Lambda deployment packages](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html) in the *AWS Lambda Developer Guide*\.

1. Choose one of the following templates for your serverless app:
   + **AWS SAM Hello World**: A basic template with a Lambda function that returns the classic "Hello World" message\.
   + **AWS Step Functions Sample App**: A sample application that runs a stock\-trading workflow\. Step functions orchestrate the interactions of the Lambda functions that are involved\. 

1. Choose a location for your new project\. If one is available, you can select an existing workspace folder\. Otherwise, browse for a different folder\. If you choose **Select a different folder**, a dialog box displays where you can select a folder location\.

1. Enter a name for your new application\. For this example, use `my-sam-app-nodejs`\. After you press **Enter**, the AWS Toolkit takes a few moments to create the project\.

When the project is created, you can view your application's files in the Environment window\. Find it listed in the **Explorer** window\.

![\[Screenshot showing the available runtimes for SAM applications.\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/)

## Running and debugging serverless applications<a name="sam-run-debug"></a>

You can use the AWS Toolkit to configure how to debug serverless applications and run them locally in your development environment\. You can debug a serverless application that's defined by an AWS Serverless Application Model \(AWS SAM\) template\. This template uses simple YAML syntax to describe resources such as functions, APIs, databases, and event\-source mappings that make up a serverless application\. 

For a closer look at the AWS SAM template, see the [AWS SAM template anatomy](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy.html) in the *AWS Serverless Application Model Developer Guide\.* 

Alternatively, you can rapidly debug serverless applications that haven't been committed to a SAM template\.

You start to configure debug behavior by using inline actions to identify an eligible AWS Lambda function\. To use the infrastructure defined by the SAM template, use the inline action in the relevant YAML\-formatted file\. To test the function directly without the template, use the context\-aware link for the Lambda handler in the application file\.

**Note**  
In this example, we're debugging an application that uses JavaScript\. But you can use debugging features available in the AWS Toolkit with the following languages and runtimes:  
JavaScript – Node\.js 10\.*x*, 12\.*x*, 14\.*x*
Python – 3\.7, 3\.8, 3\.9 \(Python 2\.7 and 3\.6 serverless applications can be run but not debugged by the AWS Toolkit\.\)
Your language choice also affects how context\-aware links indicate eligible Lambda handlers\. For more information, see [Running and debugging serverless functions directly from code](#run-debug-no-template)\.

### Using SAM templates to run and debug serverless applications<a name="sam-run-debug-template"></a>

For applications that are run and debugged using a SAM template, a YAML\-formatted file describes the application's behavior and the resources it uses\. If you create a serverless application using the AWS Toolkit, a file named `template.yaml` is automatically generated for your project\.

In this procedure, use the example application that was created in [Creating a serverless application](#sam-create)\.

### To use a SAM template to run and debug a serverless application

1. To view your application files that make up your serverless application, go to the **Environment** window\.

1. From the application folder \(for example, *my\-sample\-app*\), open the `template.yaml` file\.

1. For `template.yaml`, select **Edit Launch Configuration**\.

   A new editor displays the `launch.json` file that provides a debugging configuration with default attributes\.

1. <a name="properties"></a>Edit or confirm values for the following configuration properties:
   + `"name"` – Enter a reader\-friendly name to appear in the **Configuration** dropdown field in the **Run** view\.
   + `"target"` – Ensure that the value is `"template"`\. That way, the SAM template is the entry point for the debug session\. 
   + `"templatePath"` – Enter a relative or absolute path for the `template.yaml` file\.
   + `"logicalId"` – Ensure that the name matches the one that's specified in the **Resources** section of SAM template\. In this case, it's the `HelloWorldFunction` of type `AWS::Serverless::Function`\.

   For more information about these and other entries in the `launch.json` file, see [Configuration options for debugging serverless applications](sam-debug-config-ref.md)\.

1. If you're satisfied with your debug configuration, save `launch.json`\. Then, choose the green "play" button next to **RUN** to start debugging\.
**Note**  
If your SAM application fails to run, check the **Output** window to see if the error is caused by a Docker image not building\. You might need to free up disk space in your environment\.   
For more information, see [Error running SAM applications locally in AWS Toolkit because the AWS Cloud9 environment doesn't have enough disk space](troubleshooting.md#troubleshooting-dockerimage-toolkit)\. 

   When the debugging sessions starts, the **DEBUG CONSOLE** panel shows debugging output and displays any values that are returned by the Lambda function\. When debugging SAM applications, the **AWS Toolkit** is selected as the **Output** channel in the **Output** panel\.<a name="docker-problem"></a>
**Note**  
For Windows users, if you see a Docker mounting error during this process, you might need to refresh the credentials for your shared drives in **Docker Settings**\. A Docker mounting error looks similar to the following\.   

   ```
   Fetching lambci/lambda:nodejs10.x Docker container image......
   2019-07-12 13:36:58 Mounting C:\Users\<username>\AppData\Local\Temp\ ... as /var/task:ro,delegated inside runtime container
   Traceback (most recent call last):
   ...requests.exceptions.HTTPError: 500 Server Error: Internal Server Error ...
   ```

### Running and debugging serverless functions directly from code<a name="run-debug-no-template"></a>

When testing the AWS SAM application, you can choose to run and debug only the Lambda function\. Exclude other resources that are defined by the SAM template\. This approach involves using an inline action to identify Lambda function handlers in the source code that can be directly invoked\. 

The Lambda handlers that are detected by context\-aware links depend on the language and runtime you're using for your application\.


|  Language/runtime  | Conditions for Lambda functions to be identified by context\-aware links | 
| --- | --- | 
|  JavaScript \(Node\.js 10\.x, 12\.x, and 14\.x\)  |  The function has the following features: [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/serverless-apps-toolkit.html)  | 
|  Python \(3\.7, 3\.8 and 3\.9\)  |  The function has the following features: [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/serverless-apps-toolkit.html)  | 

### To run and debug a serverless application directly from the application code



1. To view your serverless application files, navigate to the application folder by choosing the folder icon next to the editor\.

1. From the application folder \(for example, *my\-sample\-app*\), expand the function folder \(in this example, *hello\-world*\) and open the `app.js` file\.

1. In the inline action that identifies an eligible Lambda handler function, choose `Add Debug Configuration`\. If the add debug configuration option doesn't appear, you must enable code lenses\. To enable code lenses, see [Enabling AWS Toolkit code lenses ](#enable-code-lenses)\.  
![\[Access the Add Debug Configuration option in the inline action for a Lambda function handler.\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/)

1. Select the runtime where your SAM application runs\.

1. In the editor for the `launch.json` file, edit or confirm values for the following configuration properties:
   + `"name"` – Enter a reader\-friendly name\.
   + `"target"` – Ensure that the value is `"code"` so that a Lambda function handler is directly invoked\.
   + `"lambdaHandler"` – Enter the name of the method within your code that Lambda calls to invoke your function\. For example, for applications in JavaScript, the default is `app.lambdaHandler`\.
   + `"projectRoot"` – Enter the path to the application file that contains the Lambda function\.
   + `"runtime"` – Enter or confirm a valid runtime for the Lambda execution environment \(for example, `"nodejs.12x"`\)\.
   + `"payload"` – Choose one of the following options to define the event payload that you want to provide to your Lambda function as input:
     + `"json"`: JSON\-formatted key\-value pairs that define the event payload\.
     + `"path"`: A path to the file that's used as the event payload\.

1. 

   If you're satisfied with the debug configuration, choose the green play arrow next to **RUN** to start debugging\.

   When the debugging sessions starts, the **DEBUG CONSOLE** panel shows debugging output and displays any values that are returned by the Lambda function\. When debugging SAM applications, **AWS Toolkit** is selected as the **Output** channel in the **Output** panel\.
**Note**  
If you see Docker mentioned in error messages, see this [note](#docker-problem)\.

### Running and debugging local Amazon API Gateway resources<a name="w94aac25c37b9c21"></a>

You can run or debug AWS SAM API Gateway local resources that are specified in `template.yaml`\. Do so by running an AWS Cloud9 launch configuration of `type=aws-sam` with the `invokeTarget.target=api`\.

**Note**  
API Gateway supports two types of APIs\. They are REST and HTTP APIs\. However, the API Gateway feature with the AWS Toolkit only supports REST APIs\. Sometimes HTTP APIs are called "API Gateway V2 APIs\."

**To run and debug local API Gateway resources**

1. Choose one of the following approaches to create a launch config for an AWS SAM API Gateway resource:
   + **Option 1**: Visit the handler source code \(specifically, a \.js, \.cs, or \.py file\) in your AWS SAM project, hover over the Lambda handler, and choose **Add Debug Configuration** If the add debug configuration option doesn't appear, enable code lenses\. To enable code lenses, see [Enabling AWS Toolkit code lenses ](#enable-code-lenses)\.\)\. Then, in the menu, choose the item marked API Event\.
   + **Option 2** Edit `launch.json` and create a new launch configuration using the following syntax\.

     ```
     {
         "type": "aws-sam",
         "request": "direct-invoke",
         "name": "myConfig",
         "invokeTarget": {
             "target": "api",
             "templatePath": "n12/template.yaml",
             "logicalId": "HelloWorldFunction"
         },
         "api": {
             "path": "/hello",
             "httpMethod": "post",
             "payload": {
                 "json": {}
             }
         }, 
         "sam": {},
         "aws": {}
     }
     ```

1. In the dropdown menu next to the **Run** button, choose the launch configuration \(named `myConfig` in the preceding example\)\.

1. \(Optional\) Add breakpoints to your Lambda project code\.

1. Choose the **Run** button beside the green **"play" button**\.

1. In the output pane, view the results\.

#### Configuration<a name="run-debug-api-gateway-configuration"></a>

When you use the `invokeTarget.target` property value `api`, the Toolkit changes the launch configuration validation and behavior to support an `api` field\.

```
{
    "type": "aws-sam",
    "request": "direct-invoke",
    "name": "myConfig",
    "invokeTarget": {
        "target": "api",
        "templatePath": "n12/template.yaml",
        "logicalId": "HelloWorldFunction"
    },
    "api": {
        "path": "/hello",
        "httpMethod": "post",
        "payload": {
            "json": {}
        },
        "querystring": "abc=def&qrs=tuv",
        "headers": {
            "cookie": "name=value; name2=value2; name3=value3"
        }
    },
    "sam": {},
    "aws": {}
}
```

Replace the values in the example as follows:

**invokeTarget\.logicalId**  
An API resource\.

**path**  
The API path that the launch config requests \(for example, `"path": "/hello"`\)\.  
Must be a valid API path resolved from the `template.yaml` that's specified by `invokeTarget.templatePath`\.

**httpMethod**  
Use one of the following verbs: "delete," "get," "head," "options," "patch," "post," and "put\."

**payload**  
The JSON payload \(HTTP body\) to send in the request with the same structure and rules as the [lambda\.payload](https://docs.aws.amazon.com/AWSDocsCloud9/latest/userguide/aws-explorer/sam-debug-config-ref.html) field\.  
`payload.path` points to a file that contains the JSON payload\.  
`payload.json` specifies a JSON payload inline\.

**headers**  
Optional map of name\-value pairs\. Use it to specify HTTP headers to include in the request\.  

```
"headers": {
     "accept-encoding": "deflate, gzip;q=1.0, *;q=0.5",
     "accept-language": "fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5",
     "cookie": "name=value; name2=value2; name3=value3",
     "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
}
```

**querystring**  
\(Optional\) Use this string to set the `querystring` of the request \(for example, `"querystring": "abc=def&ghi=jkl"`\)\.

**aws**  
How AWS connection information is provided\. For more information, see the **AWS connection \(`aws`\) properties** table in [Configuration options for debugging serverless applications](sam-debug-config-ref.md)\.

**sam**  
How the AWS SAM CLI builds the application\. For more information, see the **AWS SAM CLI \("`sam`"\) properties** in [Configuration options for debugging serverless applications](sam-debug-config-ref.md)\.

## Deploying a serverless application<a name="deploy-serverless-app"></a>

This example shows how to deploy the serverless application that was created in the previous topic \([Creating a serverless application](#sam-create)\) to AWS using the AWS Toolkit for Visual Studio Code\.

### Prerequisites<a name="deploy-sam-prereq"></a>
+ Make sure to choose a globally unique Amazon S3 bucket name\.
+ Ensure that the credentials you configured in include the appropriate read/write access to the following services: Amazon S3, AWS CloudFormation, AWS Lambda, and Amazon API Gateway\.
+ For applications with deployment type `Image`, make sure that you have both a globally unique Amazon S3 bucket name and an Amazon ECR repository URI to use for the deployment\.

### Deploying a serverless application<a name="deploy-sam-proc"></a>

1. In the **AWS Explorer** window, open the context \(right\-click\) menu for the **Lambda** node and select **Deploy SAM Application**\.

1. Choose the `template.yaml` file to use for the deployment\.

1. Now choose the AWS Region to deploy to\.

1. Enter the name of an Amazon S3 bucket that this deployment can use\. The bucket must be in the Region that you're deploying to\.
**Warning**  
The Amazon S3 bucket name must be globally unique across all existing bucket names in Amazon S3\. Add a unique identifier to the name given in the following example or choose another name\.

1. If your serverless application includes a function with package type `Image`, enter the name of an Amazon ECR repository that this deployment can use\. The repository must be in the Region that you're deploying to\.

1. Enter a name for the deployed stack, either a new stack name or an existing stack name\.

1. Verify the success of the deployment on the **AWS Toolkit** tab of the **Console**\.

   If an error occurs, a message pops up in the lower right\.

   If this happens, check the text in the **AWS Toolkit** tab for details\. The following is an example of error details\.

   ```
   Error with child process: Unable to upload artifact HelloWorldFunction referenced by CodeUri parameter of HelloWorldFunction resource.
   S3 Bucket does not exist. Execute the command to create a new bucket
   aws s3 mb s3://pbart-my-sam-app-bucket
   An error occurred while deploying a SAM Application. Check the logs for more information by running the "View AWS Toolkit Logs" command from the Command Palette.
   ```

   In this example, the error occurred because the Amazon S3 bucket didn't exist\.

When the deployment is complete, you'll see your application that's listed in the **AWS Explorer**\. To learn how to invoke the Lambda function that was created as part of the application, see [Invoking remote Lambda functions](lambda-toolkit.md#remote-lambda)\.

## Enabling AWS Toolkit code lenses<a name="enable-code-lenses"></a>

1. On the menu bar, choose **AWS Cloud9**, and then **Preferences**\.

1. On the **Preferences** tab, in the sidebar, choose **AWS Toolkit**\.

1. To enable code lenses, choose **Enable Code Lenses**\.

## Deleting a serverless application from the AWS Cloud<a name="delete-serverless-app"></a>

Deleting a serverless application involves deleting the AWS CloudFormation stack that you previously deployed to the AWS Cloud\. Note that this procedure does not delete your application directory from your local host\.

1. Open the **AWS Explorer**\.

1. In the **AWS Explorer** window, expand the Region containing the deployed application that you want to delete, and then expand **AWS CloudFormation**\.

1. Open the context \(right\-click\) menu for the name of the AWS CloudFormation stack that corresponds to the serverless application that you want to delete\. Then, choose **Delete CloudFormation Stack**\.

1. To confirm that you want to delete the selected stack, choose **Delete**\.

If the stack deletion succeeds, the AWS Toolkit removes the stack name from the AWS CloudFormation list in **AWS Explorer**\.