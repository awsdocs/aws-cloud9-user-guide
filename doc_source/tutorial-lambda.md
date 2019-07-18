# AWS Lambda Tutorial for AWS Cloud9<a name="tutorial-lambda"></a>

In this tutorial, you use the AWS Cloud9 IDE to create a function in AWS Lambda and an accompanying API in Amazon API Gateway\. After you create the function and its API, you run and debug them locally\. Then you run the function and API in Lambda and API Gateway in production\.

**Note**  
Completing this tutorial might result in charges to your AWS account\. These include possible charges for Amazon EC2, Lambda, and API Gateway\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/), [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/), and [Amazon API Gateway Pricing](https://aws.amazon.com/api-gateway/pricing/)\.

**Topics**
+ [Prerequisites](#tutorial-lambda-prereqs)
+ [Step 1: Create and Open the Environment](#tutorial-lambda-create-environment)
+ [Step 2: Create the Lambda Function and API](#tutorial-lambda-create-function)
+ [Step 3: Add Code to the Function](#tutorial-lambda-add-code)
+ [Step 4: Run the Function Locally](#tutorial-lambda-run-local-function)
+ [Step 5: Debug the Function Locally](#tutorial-lambda-debug-local-function)
+ [Step 6: Run the API Locally](#tutorial-lambda-run-local-api)
+ [Step 7: Debug the API Locally](#tutorial-lambda-debug-local-api)
+ [Step 8: Run the Function in Production](#tutorial-lambda-run-deployed-function)
+ [Step 9: Run the API in Production](#tutorial-lambda-run-deployed-api)
+ [Step 10: Change the Function Locally](#tutorial-lambda-change-function)
+ [Step 11: Deploy the Changed Function into Production](#tutorial-lambda-deploy-function)
+ [Step 12: Clean Up](#tutorial-lambda-clean-up)
+ [Next Steps](#tutorial-lambda-next-steps)

## Prerequisites<a name="tutorial-lambda-prereqs"></a>

To successfully complete this tutorial, you must first complete the steps in [Getting Started with AWS Cloud9](get-started.md)\.

## Step 1: Create and Open the Environment<a name="tutorial-lambda-create-environment"></a>

In this step, you use the AWS Cloud9 console to create and then open an AWS Cloud9 development environment\.

If you already have an environment, open it, and then skip ahead to [Step 2: Create the Lambda Function and API](#tutorial-lambda-create-function)\.

In AWS Cloud9, a *development environment* \(or just *environment*\) is a place where you store your development project's files and where you run the tools to develop your apps\. In this tutorial, you create a special kind of environment called an *EC2 environment*\. For this kind of environment, AWS Cloud9 launches and manages a new Amazon EC2 instance running Amazon Linux or Ubuntu Server, creates the environment, and then connects the environment to the newly\-launched instance\. When you open the environment, AWS Cloud9 displays the AWS Cloud9 IDE that enables you to work with the files and tools in that environment\.

1. Sign in to the AWS Cloud9 console as follows:
   + If you're the only individual using your AWS account or you are an IAM user in a single AWS account, go to [https://console\.aws\.amazon\.com/cloud9/](https://console.aws.amazon.com/cloud9/)\.
   + If your organization uses AWS Single Sign\-On \(AWS SSO\), see your AWS account administrator for sign\-in instructions\.
   + If you're using an AWS Educate Starter Account, see [Step 2: Sign In to the AWS Cloud9 Console](setup-student.md#setup-student-sign-in-ide) in *Individual Student Signup*\.
   + If you're a student in a classroom, see your instructor for sign\-in instructions\.

1. In the top navigation bar, choose the AWS Region to create the environment in\.  
![\[AWS Region selector in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-region.png)

1. If a welcome page is displayed, for **New AWS Cloud9 environment**, choose **Create environment**\. Otherwise, choose **Create environment**\.  
![\[Welcome page in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-welcome-new-env.png)

   Or:  
![\[Create environment button in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-new-env.png)

1. On the **Name environment** page, for **Name**, type a name for your environment \(for example, `my-lambda-environment`\)\.

1. For **Description**, type something about your environment \(for example, `This environment is for the AWS Cloud9 tutorial for Lambda.`\)\.

1. Choose **Next step**\.

1. On the **Configure settings** page, for **Environment type**, leave the default choice of **Create a new instance for environment \(EC2\)**\.

1. For **Instance type**, leave the default choice of **t2\.micro**\. This choice has relatively low RAM and vCPUs, which is sufficient for this tutorial\.
**Note**  
Choosing an instance type with greater compute resources might result in more charges to your AWS account\.

1. For **Platform**, choose the type of Amazon EC2 instance that AWS Cloud9 will create and then connect to this environment: **Amazon Linux** or **Ubuntu**\.

1. For **Cost\-saving setting**, leave the default choice of **After 30 minutes**\. This is the amount of time until AWS Cloud9 shuts down the Amazon EC2 instance for the environment, after all web browser instances that are connected to the IDE for the environment have been closed\.
**Note**  
Choosing a longer time period might result in more charges to your AWS account\.

1. Choose **Next step**\.

1. On the **Review** page, choose **Create environment**\. Wait while AWS Cloud9 creates your environment\. This can take a few minutes\.

After AWS Cloud9 creates your environment, it displays the AWS Cloud9 IDE for the environment\.

If AWS Cloud9 doesn't display the IDE after at least five minutes, there might be a problem with your web browser, your AWS access permissions, the instance, or the associated virtual private cloud \(VPC\)\. For possible fixes, see [Cannot Open an Environment](troubleshooting.md#troubleshooting-env-loading) in *Troubleshooting*\.

## Step 2: Create the Lambda Function and API<a name="tutorial-lambda-create-function"></a>

In this step, you use the AWS Cloud9 IDE to create the Lambda function and its accompanying API at the same time\. AWS Cloud9 stores the new function on the Amazon EC2 instance and deploys a copy of the function to Lambda\. AWS Cloud9 also stores the new accompanying API on the instance and deploys a copy of the API to API Gateway\.

The Lambda function returns information about the day or time you specify, for example, the day, month, and year, or the current hour, minute, and second\.

Currently, you can use the IDE to automatically create functions that use only Node\.js or Python\. This function uses Node\.js\.

1. Make sure you have completed the prerequisites for work with Lambda functions in the AWS Cloud9 IDE for the environment\. This includes checking to see whether you must: 
   + Set up your IAM group with required access permissions\.
   + Set up your environment with AWS access credentials\.
   + Create an execution rule for your Lambda functions\.

   For more information, see [Prepare to Work with Lambda Functions](lambda-functions.md#lambda-functions-prepare)\.

1. With the IDE open from the previous step, set the AWS Region that you want to create the function in\. To do this, on the menu bar, choose **AWS Cloud9, Preferences**\.

1. In the navigation pane of the **Preferences** tab, choose **AWS Settings**\.

1. For **AWS Region**, select the AWS Region you want to create the function in\.  
![\[AWS Region selector in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-prefs-aws-region.png)

1. On the edge of the IDE, choose **AWS Resources**\.  
![\[Create a new Lambda function\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-create-lambda-function.png)

1. Expand the **Lambda**, if it isn't already expanded\. On the toolbar, choose the **Create a new Lambda function** icon\.

1. In the **Create serverless application** dialog box, for **Function name**, type a name for the function \(for example, `myDateTimeFunction`\)\.

1. For **Application name**, type a name for the function's containing serverless application \(for example, `MyDateTimeApplication`\)\.

1. Choose **Next**\.

1. For **Select runtime**, choose **Node\.js 6\.10**\.

1. For **Select blueprint**, choose **empty\-nodejs**\. This creates some starter code that you work with in the next step\.

1. Choose **Next**\.

1. For **Function trigger**, choose **API Gateway**\. This creates an API in API Gateway that you use to run and debug the function in a later step\.

1. For **Resource Path**, type `/` \(a forward slash\)\. The **Resource Path** defines a portion of the URL that you use to run and debug the API in a later step\. For more information, see [Set up API Methods in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-method-settings.html) in the *API Gateway Developer Guide*\.

1. For **Security**, choose **NONE**, and then choose **Next**\. This specifies that you don't need any special credentials to run and debug this API\.

1. For **Memory \(MB\)**, leave the default value of **128 MB**, which is sufficient for this tutorial\.

1. For **Role**, leave the default value of **Automatically generate role**, and then choose **Next**\. This specifies the access permissions that the function needs to work properly\.

1. Review your choices, and then choose **Finish**\.

AWS Cloud9 creates the function and its related API on the instance\. Then it deploys a copy of the function and API to Lambda and API Gateway\. The serverless application and function are displayed in the **Local Functions** and **Remote Functions** lists in the **Lambda** pane of the **AWS Resources** window\. The serverless application's and function's component files are displayed in the **Environment** window\. The editor opens the function's code file, `index.js`\.

![\[The new Lambda function in the IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-new-lambda-function.png)

**Note**  
In addition to the function's code file, AWS Cloud9 creates the following helper files\.  
 `.application.json`: A hidden file that contains JSON\-formatted settings that are specific to the serverless application\. AWS Cloud9 uses these settings for its internal use\. Do not edit this file\.
 `.gitignore`: A hidden file that contains a list of files Git ignores, if you want to use Git to manage your source code for this function\.
 `template.yaml`: An AWS Serverless Application Model \(AWS SAM\) template file that contains information about the Lambda function, the related API in API Gateway, and any other related, supported AWS resources\. Whenever you update the local version of your function and then upload it to Lambda, AWS Cloud9 calls AWS SAM to use this template file to do the upload\. For more information, see [Using the AWS Serverless Application Model \(AWS SAM\)](https://docs.aws.amazon.com/lambda/latest/dg/deploying-lambda-apps.html#serverless_app) in the *AWS Lambda Developer Guide*\.
The `.application.json` and `.gitignore` files are hidden\. To show hidden files or hide them if they're shown, in the **Environment** window, choose the gear icon\. Then choose **Show Hidden Files**\.  

![\[Showing the hidden Lambda files\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-lambda-files.png)

## Step 3: Add Code to the Function<a name="tutorial-lambda-add-code"></a>

In this step, you replace the starter code for the generated function with specific code that returns information about the day or time you specify\.

With the `index.js` file already open in the editor, completely replace the file's contents with the following code, and then save the file\.

```
'use strict';

exports.handler = function(event, context, callback) {

  if (event.body) {
    event = JSON.parse(event.body);
  }

  var sc; // Status code
  var result = ""; // Response payload

  switch(event.option) {
    case "date":
      switch(event.period) {
        case "yesterday":
          result = setDateResult("yesterday");
          sc = 200;
          break;
        case "today":
          result = setDateResult();
          sc = 200;
          break;
        case "tomorrow":
          result = setDateResult("tomorrow");
          sc = 200;
          break;
        default:
          result = {
            "error": "Must specify 'yesterday', 'today', or 'tomorrow'."
          };
          sc = 400;
          break;
      }
      break;
      case "time":
        var d = new Date();
        var h = d.getHours();
        var mi = d.getMinutes();
        var s = d.getSeconds();

        result = {
          "hour": h,
          "minute": mi,
          "second": s
        };
        sc = 200;
        break;
      default:
        result = {
          "error": "Must specify 'date' or 'time'."
        };
        sc = 400;
      break;
  }

  const response = {
    statusCode: sc,
    headers: { "Content-type": "application/json" },
    body: JSON.stringify( result )
  };

  callback(null, response);

  function setDateResult(option) {

    var d = new Date(); // Today
    var mo; // Month
    var da; // Day
    var y; // Year

    switch(option) {
      case "yesterday":
        d.setDate(d.getDate() - 1);
        break;
      case "tomorrow":
        d.setDate(d.getDate() + 1);
      default:
       break;
    }

    mo = d.getMonth() + 1; // Months are zero offset (0-11)
    da = d.getDate();
    y = d.getFullYear();

    result = {
      "month": mo,
      "day": da,
      "year": y
    };

    return result;
  }
};
```

This function takes an incoming payload with an `option` value of `date` or `time`\. If `date` is specified, you must also specify a `period` value of `yesterday`, `today`, or `tomorrow`\. The function then returns the corresponding `month`, `day`, and `year`\. If, however, an `option` value of `time` is specified, the function returns the current `hour`, `minute`, and `second`\.

## Step 4: Run the Function Locally<a name="tutorial-lambda-run-local-function"></a>

In this step, you use the IDE to run the function on the instance\. Currently, you can use the IDE to run functions that use only Node\.js or Python\.

1. In the **Lambda** pane of the **AWS Resources** window, expand the **MyDateTimeApplication** Lambda folder, and then right\-click the **myDateTimeFunction** Lambda icon\.

1. Choose **Run, Run Local**\.  
![\[Running the Lambda function locally\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-lambda-run-local.png)

1. In the **Payload** pane of the run tab, replace `{}` with the following, which sends this data as input to the function for processing\.

   ```
   {
     "option": "date",
     "period": "today"
   }
   ```

1. Choose **Run**\.

1. The **Response** pane displays the following\.

   ```
   {
     "statusCode": 200,
     "headers": {
       "Content-type": "application/json"
     },
     "body": "{\"month\":4,\"day\":12,\"year\":2018}"
   }
   ```
**Note**  
If the **Response** pane displays `null`, be sure to save the `index.js`, and then choose **Run** again\.

   Compare your results to the following\.  
![\[Running the Lambda function\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-run-lambda-local.png)

1. Run the function several times with the following payloads to see what the **Response** pane displays\.

   ```
   {
     "option": "date",
     "period": "yesterday"
   }
   
   {
     "option": "date",
     "period": "tomorrow"
   }
   
   {
     "option": "time"
   }
   
   Displays an error. Must also specify a 'period' of 'yesterday', 'today', or 'tomorrow'.
   {
     "option": "date"
   }
   
   Displays an error. Must specify an 'option' of 'date' or 'time'.
   {
     "option": "dates"
   }
   ```

## Step 5: Debug the Function Locally<a name="tutorial-lambda-debug-local-function"></a>

In this step, you use the IDE to debug the function on the instance\. Currently, you can use the IDE to debug functions that use only Node\.js or Python\. Also, you can use the IDE to debug functions locally only\. You cannot use the IDE to debug functions in Lambda itself\.

1. In the `index.js` file, create a breakpoint for the debugger\. To do this, in the editor, next to the line of code `callback(null, response)`, click the gutter just to the left of line 62\. A red circle is displayed, representing the breakpoint\.

1. On the right edge of the IDE, choose **Debugger**\.

1. Add four expressions for the debugger to watch\. To do this, in the **Watch Expressions** area, for **Type an expression here**, type `event.option`, and then press `Enter`\. Do this three more times, typing `event.period`, `sc`, and `response.body`\.  
![\[Adding watch expressions\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-lambda-watch-expressions.png)

1. On the run tab that AWS Cloud9 opened in [Step 4: Run the Function Locally](#tutorial-lambda-run-local-function), choose the icon that looks like a bug\. \(It switches from grey to green\.\)  
![\[The debug icon.\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/debug-button.png)  
![\[Turning on debugging.\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/debug-icon-on.png)

1. In the **Payload** pane on the run tab, be sure the following payload is still visible\.

   ```
   {
     "option": "date",
     "period": "today"
   }
   ```

1. Choose **Run**\.

   Code execution pauses at the breakpoint\. The current values of `event.option`, `event.period`, `sc`, and `response.body` are displayed in the **Watch Expressions** area of the **Debugger** window\.

   You can also see these values in the code by hovering your mouse over `option` in line 12 in the code, `period` in line 14, `sc` in line 21, and `response` in line 56\. For `response` in line 56, expand **Object \{\}**, and then see the **body** value\.

   Compare your results to the following\.  
![\[Debugging the Lambda function\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-lambda-debug-local.png)

1. In the `Debugger` window, choose the blue **Resume** arrow to finish running the code\. \(It looks like a triangular play button\.\)

## Step 6: Run the API Locally<a name="tutorial-lambda-run-local-api"></a>

In this step, you use the IDE to have API Gateway run the Lambda function on the instance\.

1. In the **Lambda** pane of the **AWS Resources** window, right\-click the **myDateTimeFunction** Lambda icon, and then choose **Run, Run APIGateway Local**\.
**Note**  
You can also do this by choosing the **Lambda \(local\)** list on the run tab from the previous step, and then choosing **API Gateway \(local\)**\.

1. On the run tab, for **Path**, type `/` \(a forward slash\)\.

1. For **Method**, choose **POST**\.

1. For **Body**, replace `{}` with the following, which sends this data as input to the API for processing\.

   ```
   {
     "option": "date",
     "period": "today"
   }
   ```

1. If the bug icon is green, choose it to turn it off\. \(It switches back to grey\.\)  
![\[Turning off debugging\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/debug-icon-off.png)

1. Choose **Run**\.

1. The **Response** pane displays the following response\.

   ```
   {
     "month": 4,
     "day": 12,
     "year": 2018
   }
   ```

1. Run the function several times with the following payloads to see what the **Response** pane displays\.

   ```
   {
     "option": "date",
     "period": "yesterday"
   }
   
   {
     "option": "date",
     "period": "tomorrow"
   }
   
   {
     "option":"time"
   }
   
   Displays an error. Must also specify a 'period' of 'yesterday', 'today', or 'tomorrow'.
   {
     "option":"date"
   }
   
   Displays an error. Must specify an 'option' of 'date' or 'time'.
   {
     "option":"dates"
   }
   ```

Compare your results to the following\.

![\[Running the API\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-api-run-local.png)

## Step 7: Debug the API Locally<a name="tutorial-lambda-debug-local-api"></a>

In this step, you use the IDE to have API Gateway debug the Lambda function on the instance\.

1. Ensure that the `index.js` file still has a breakpoint set on the line of code `callback(null, response)`\.

1. Ensure that the **Watch Expressions** area of the **Debugger** window is still watching `event.option`, `event.period`, `sc`, and `response.body`\.

1. On the run tab from the previous step, choose the icon that looks like a bug\. \(It switches from grey to green\.\)

1. In the **Body** pane on the run tab, ensure the following is still visible\.

   ```
   {
     "option": "date",
     "period": "today"
   }
   ```

1. Choose **Run**\.

   Code execution pauses at the breakpoint, and the current values of `event.option`, `event.period`, `sc`, and `response.body` are displayed in the **Watch Expressions** area of the **Debugger** window\.

   You can also see these values in the code by hovering your mouse over `option`, `period`, `sc`, and `response` in the code\. For `response`, expand **Object \{\}**, and then see the **body** value\.

1. In the `Debugger` window, choose the blue **Resume** arrow to finish running the code\.

## Step 8: Run the Function in Production<a name="tutorial-lambda-run-deployed-function"></a>

In this step, you use the IDE to run the function in Lambda itself\.

AWS Cloud9 deployed the function to Lambda during [Step 2: Create the Lambda Function and API](#tutorial-lambda-create-function)\. However, AWS Cloud9 deployed the function before you made the changes in [Step 3: Add Code to the Function](#tutorial-lambda-add-code)\. That original function was very basic, taking no payload and returning no response\. So, you must first deploy your changes to Lambda, and then you can run the deployed function there\.

1. In the **Lambda** pane of the **AWS Resources** window, expand **Local Functions**, expand the **MyDateTimeApplication** Lambda folder, right\-click the **myDateTimeFunction** Lambda icon, and then choose **Deploy**\.

1. After the deployment finishes, right\-click the **myDateTimeFunction** Lambda icon, and then choose **Run, Run Remote**\.
**Note**  
You can also do this by choosing the **API Gateway \(local\)** list on the run tab from the previous step, and then choosing **Lambda \(remote\)**\.

1. In the **Payload** pane on the run tab, be sure one of the payloads from [Step 4: Run the Function Locally](#tutorial-lambda-run-local-function) is visible\. If it isn't there, add it\.

1. Choose **Run**, and see the results in the **Response** area\. These should be the same results as in [Step 4: Run the Function Locally](#tutorial-lambda-run-local-function)\.

## Step 9: Run the API in Production<a name="tutorial-lambda-run-deployed-api"></a>

In this step, you use the IDE to run the API in API Gateway itself\.

**Note**  
AWS Cloud9 deployed the API to API Gateway during [Step 2: Create the Lambda Function and API](#tutorial-lambda-create-function)\. Because you haven't made any changes to the API since AWS Cloud9 first deployed it, you don't need to deploy the API again before you can run it in API Gateway itself\.

1. In the **Lambda** pane of the **AWS Resources** window, right\-click the **myDateTimeFunction** Lambda icon, and then choose **Run, Run APIGateway Remote**\.
**Note**  
You can also do this by choosing the **Lambda \(remote\)** list on the run tab from the previous step, and then choosing **API Gateway \(remote\)**\.

1. Ensure **Path** is still set to **/**, **Method** is still set to **POST**, and **Body** is still set to one of the bodies in [Step 6: Run the API Locally](#tutorial-lambda-run-local-api)\. If any of these aren't set correctly, set them\.

1. Choose **Run**, and see the results in the **Response** area, which should be the same results as in [Step 6: Run the API Locally](#tutorial-lambda-run-local-api)\.

## Step 10: Change the Function Locally<a name="tutorial-lambda-change-function"></a>

In this step, you use the IDE to make a small change to the Lambda function\. You then test the changed function locally and the original function in production to see the differences\.

1. In the `index.js` file, on line 41, add a `time` value to the `result` variable, as follows\.

   ```
   result = {
     "time": d.toTimeString(),
     "hour": h,
     "minute": mi,
     "second": s
   };
   ```

1. On line 86, add a `date` value to the `result` variable, as follows\.

   ```
   result = {
     "date": d.toDateString(),
     "month": mo,
     "day": da,
     "year": y
   };
   ```

1. Save your changes to the `index.js` file\.

1. Run the changed function locally by following the instructions in [Step 4: Run the Function Locally](#tutorial-lambda-run-local-function)\. Notice that the `time` or `date` value is now displayed in the response\.

1. Run the original function in production by following the instructions in [Step 8: Run the Function in Production](#tutorial-lambda-run-deployed-function)\. Notice that the `time` or `date` value doesn't display in the response yet\. This is because you have not deployed the changed function into production\. You do this in the next step\.

## Step 11: Deploy the Changed Function into Production<a name="tutorial-lambda-deploy-function"></a>

In this step, you deploy the changed function again to Lambda itself\. You then test the changed function in production to confirm the deployment\.

1. In the **Lambda** pane of the **AWS Resources** window, right\-click the **myDateTimeFunction** Lambda icon, and then choose **Deploy**\.

1. After the deployment succeeds, run the changed function in production by following the instructions in [Step 8: Run the Function in Production](#tutorial-lambda-run-deployed-function)\. Notice that the `time` or `date` value now appears in the response\.

Remember, whenever you make a change to the local function and you want to deploy those changes to Lambda \(and API Gateway, if an accompanying API exists\), be sure to follow this step\.

## Step 12: Clean Up<a name="tutorial-lambda-clean-up"></a>

To prevent ongoing charges to your AWS account that are related to this tutorial after you're finished, you can delete the function from Lambda, the API from API Gateway, and the environment from AWS Cloud9\.

### Step 12\.1: Delete the Function and the API from Lambda and API Gateway<a name="step-12-1-delete-the-function-and-the-api-from-lam-and-abp"></a>

For AWS Cloud9 to create the function and its associated API, behind the scenes AWS Cloud9 uses the AWS Serverless Application Model \(AWS SAM\) to create a stack in AWS CloudFormation\. This stack then creates the function and its associated API\. In this procedure, you use the IDE to have AWS CloudFormation delete the stack, which also deletes the function and the API\. \(You could use the Lambda and API Gateway consoles instead of AWS CloudFormation to delete the function and its associated API\. However, that approach takes longer and still leaves the stack in AWS CloudFormation when it's no longer needed\.\)

**Warning**  
Deleting a stack cannot be undone\. When you delete this stack, the associated function and its API are deleted from Lambda and API Gateway and cannot be recovered\.

1. From the IDE, use the AWS Command Line Interface \(AWS CLI\) in the terminal to run the AWS CloudFormation`delete-stack` command, specifying the name and the AWS Region ID for the stack\. \(To display the terminal, on the menu bar, choose **Window, New Terminal**\)\. This stack's name follows the format `cloud9-APPLICATION_NAME`, so you would specify `cloud9-MyDateTimeApplication` for this tutorial\. To get the AWS Region ID \(represented in the following command as `us-east-2`\), see the corner of the **Lambda** pane in the **AWS Resources** window\.

   ```
   aws cloudformation delete-stack --stack-name cloud9-MyDateTimeApplication --region us-east-2
   ```

   If the command ran successfully, no output and no error message are displayed\.
**Note**  
If you use an IAM user to run this command for this tutorial, instead of an AWS account root user or an IAM administrator, the IAM user must have the following additional AWS access permissions\.  
 `cloudformation:ListStacks` 
 `cloudformation:DeleteStack` 
If you cannot add these permissions to the IAM user, see your organization's AWS account administrator\.

1. To verify that the stack is deleted, use the AWS CLI to run the AWS CloudFormation`describe-stacks` command\. If the function is deleted, a message is displayed that the stack doesn't exist\. \(You might need to run this command multiple times until that message is displayed\.\)

   ```
   aws cloudformation describe-stacks --query 'Stacks[0].StackStatus' --output text --stack-name cloud9-MyDateTimeApplication --region us-east-2
   ```

1. If you no longer want to keep the local function in the IDE, delete the `~/environment/MyDateTimeApplication` folder \(for example, by running the command `rm -rf ~/environment/MyDateTimeApplication`\)\.
**Note**  
In the IDE, `~/environment` is the same as specifying the root directory in the **Environment** window\.

### Step 12\.2: Delete the Environment from AWS Cloud9<a name="step-12-2-delete-the-envtitle-from-ac9"></a>

**Warning**  
Deleting an environment cannot be undone\. Also, when you delete an EC2 environment, AWS Cloud9 also terminates the Amazon EC2 instance that it previously launched and connected to the environment\. Once terminated in Amazon EC2, the instance cannot be reactivated or recovered\.

1. From the IDE, open the dashboard in the AWS Cloud9 console\. To do this, on the menu bar, choose **AWS Cloud9**, **Go To Your Dashboard**\.

1. Do one of the following:
   + Choose the title inside of the **my\-demo\-lambda\-environment** card, and then choose **Delete**\.
   + Select the **my\-demo\-lambda\-environment** card, and then choose **Delete**\.

1. In the **Delete** dialog box, type `Delete`, and then choose **Delete**\.

## Next Steps<a name="tutorial-lambda-next-steps"></a>

Explore any or all of the following topics to continue getting familiar with AWS Cloud9\.


****  

|  |  | 
| --- |--- |
|  Learn more about how to use AWS Cloud9 with Lambda  |   [Advanced AWS Lambda Tutorial for AWS Cloud9](tutorial-lambda-advanced.md) and [Working with AWS Lambda Functions in the AWS Cloud9 Integrated Development Environment \(IDE\)](lambda-functions.md)   | 
|  Learn more about the AWS Cloud9 IDE  |   [IDE Tutorial for AWS Cloud9](tutorial.md) and [Working with the AWS Cloud9 Integrated Development Environment \(IDE\)](ide.md)   | 
|  Invite others to use your environment with you, in real time and with text chat support  |   [Working with Shared Environments in AWS Cloud9](share-environment.md)   | 
|  Create SSH environments \(environments that use cloud compute instances or servers that you create, instead of an Amazon EC2 instances that AWS Cloud9 creates for you\)\.  |   [Creating an Environment in AWS Cloud9](create-environment.md) and [AWS Cloud9 SSH Development Environment Host Requirements](ssh-settings.md)   | 
|  Use AWS Cloud9 with Amazon Lightsail  |   [Working with Amazon Lightsail Instances in the AWS Cloud9 Integrated Development Environment \(IDE\)](lightsail-instances.md)   | 
|  Use AWS Cloud9 with AWS CodeStar  |   [Working with AWS CodeStar Projects in the AWS Cloud9 Integrated Development Environment \(IDE\)](codestar-projects.md)   | 
|  Use AWS Cloud9 with AWS CodePipeline  |   [Working with AWS CodePipeline in the AWS Cloud9 Integrated Development Environment \(IDE\)](codepipeline-repos.md)   | 
|  Use AWS Cloud9 with the AWS CLI, the aws\-shell, AWS CodeCommit, the AWS Cloud Development Kit \(AWS CDK\), GitHub, or Amazon DynamoDB, as well as Node\.js, Python, or other programming languages  |   [Samples for AWS Cloud9](samples.md)   | 
|  Work with code for intelligent robotics applications in AWS RoboMaker\.  |   [Developing with AWS Cloud9](https://docs.aws.amazon.com/robomaker/latest/dg/cloud9.html) in the *AWS RoboMaker Developer Guide*   | 

To get help with AWS Cloud9 from the community, see the [AWS Cloud9 Discussion Forum](https://forums.aws.amazon.com/forum.jspa?forumID=268)\. \(When you enter this forum, AWS might require you to sign in\.\)

To get help with AWS Cloud9 directly from AWS, see the support options on the [AWS Support](https://aws.amazon.com/premiumsupport) page\.