# Advanced AWS Lambda Tutorial for AWS Cloud9<a name="tutorial-lambda-advanced"></a>

In this tutorial, you use the AWS Cloud9 IDE to create a function in AWS Lambda and an accompanying API in Amazon API Gateway\. After you create the function and its API, you run and debug them locally\. Then you run the function and API in Lambda and API Gateway in production\. The function and its API call Amazon Simple Notification Service \(Amazon SNS\) to send messages to an email address that you specify\.

**Note**  
Completing this tutorial might result in charges to your AWS account\. These include possible charges for Amazon EC2, Lambda, API Gateway, and Amazon SNS\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/), [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/), [Amazon API Gateway Pricing](https://aws.amazon.com/api-gateway/pricing/), and [Amazon SNS Pricing](https://aws.amazon.com/sns/pricing/)\.
+  [Prerequisites](#tutorial-lambda-advanced-prereqs) 
+  [Step 1: Create the Lambda Function and API](#tutorial-lambda-advanced-create-function) 
+  [Step 2: Set up Amazon SNS](#tutorial-lambda-advanced-sns-setup) 
+  [Step 3: Run the Function Locally](#tutorial-lambda-advanced-run-local-function) 
+  [Step 4: Debug the Function Locally](#tutorial-lambda-advanced-debug-local-function) 
+  [Step 5: Run the API Locally](#tutorial-lambda-advanced-run-local-api) 
+  [Step 6: Debug the API Locally](#tutorial-lambda-advanced-debug-local-api) 
+  [Step 7: Deploy and Run the Changed Function in Production](#tutorial-lambda-advanced-deploy-function) 
+  [Step 8: Clean Up](#tutorial-lambda-advanced-clean-up) 
+  [Next Steps](#tutorial-lambda-advanced-next-steps) 

## Prerequisites<a name="tutorial-lambda-advanced-prereqs"></a>

Before you start this tutorial, we recommend that you first complete the companion [AWS Lambda Tutorial for AWS Cloud9](tutorial-lambda.md)\. This tutorial builds on the prerequisites and concepts that are presented there\.

**Note**  
If you don't want to complete that entire tutorial first, you must at least complete the following steps in that tutorial or else create the equivalent AWS resources\.  
 [Prerequisites](tutorial-lambda.md#tutorial-lambda-prereqs): This includes deciding which user in an AWS account or organization you'll use to complete this tutorial\.
 [Step 1: Create and Open the Environment](tutorial-lambda-create-environment.md): This includes creating an AWS Cloud9 EC2 development environment and opening the AWS Cloud9 IDE for that environment\.

## Step 1: Create the Lambda Function and API<a name="tutorial-lambda-advanced-create-function"></a>

In this step, you use the AWS Cloud9 IDE to create the Lambda function and its accompanying API at the same time\. AWS Cloud9 stores the new function on the Amazon EC2 instance and deploys a copy of the function to Lambda\. AWS Cloud9 also stores the new accompanying API on the instance and deploys a copy of the API to API Gateway\.

The function uses Amazon Simple Notification Service \(Amazon SNS\) to send messages to your email address\. In a later step, you create the Amazon SNS resources that this function needs\.

Currently, you can use the IDE to create functions that use only Node\.js or Python\. This function uses Node\.js\.

1. With the IDE displayed for the environment, on the menu bar, choose **AWS Cloud9, Preferences**\.

1. In the navigation pane of the **Preferences** tab, choose **AWS Settings**\.

1. For **AWS Region**, select the AWS Region you want to create the function in\.  
![\[AWS Region selector in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-prefs-aws-region.png)

1. On the edge of the IDE, choose **AWS Resources**\.

1. Expand the **Lambda** pane, if it's not already expanded\. On the toolbar, choose **Create a new Lambda function**\.  
![\[Create a new Lambda function\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-create-lambda-function.png)

1. In the **Create serverless application** dialog box, for **Function name**, type a name for the function \(for example, `mySNSFunction`\)\.

1. For **Application name**, type a name for the function's containing serverless application \(for example, `MySNSApplication`\)\.

1. Choose **Next**\.

1. For **Select runtime**, choose **Node\.js 12\.x**\.

1. For **Select blueprint**, choose **sns\-send\-message**\. \(You might need to scroll through the list of blueprints to see it\.\)

1. Choose **Next**\.

1. For **Function trigger**, choose **API Gateway**\.

1. For **Resource Path**, type `/`\.

1. For **Security**, choose **NONE**, and then choose **Next**\.

1. For **Memory \(MB\)**, leave the default value of **128 MB**, which is sufficient for this tutorial\.

1. For **Role**, leave the default value of **Automatically generate role**, and then choose **Next**\. \(You change this role in the next step\.\)

1. Review your choices, and then choose **Finish**\.

AWS Cloud9 creates the function and its related API on the instance and then deploys a copy of the function and API to Lambda and API Gateway\. The serverless application and function are displayed in the **Local Functions** and **Remote Functions** lists in the **Lambda** pane of the **AWS Resources** window\. The serverless application's and function's component files \(for example, a AWS CloudFormation template that you use later to create Amazon SNS resources\) are displayed in the **Environment** window\. The editor opens the function's code file, `index.js`\.

If you run this function or API now, it won't work\. This is because the Amazon SNS resources that this function needs are not set up yet\. Also, the function doesn't have permission to call Amazon SNS\. In the next step, you set up these resources and provide this permission\.

## Step 2: Set up Amazon SNS<a name="tutorial-lambda-advanced-sns-setup"></a>

In this tutorial, the Lambda function uses Amazon SNS to send messages to your email address\. In this step, you run an AWS CloudFormation stack that quickly creates a topic in Amazon SNS and then subscribes your email address to the topic\. The stack also creates an execution role in IAM to allow the Lambda function permission to use Amazon SNS\. \(You could do all of this setup in Amazon SNS and IAM manually, but AWS CloudFormation makes this setup easier and faster\.\) After AWS CloudFormation creates the stack, you attach the execution role to the function, and then give Amazon SNS permission to start sending messages to your email address\.

1. In the terminal, change to the directory that contains the AWS CloudFormation template file named `sns-create-topic-subscription.yaml`\.

   ```
   cd ~/environment/MySNSApplication
   ```
**Note**  
In the IDE, `~/environment` is the same as specifying the root directory in the `Environment` window\.

1. Use the AWS CLI to run the following command, which creates and runs a AWS CloudFormation stack based on this template file\.

   ```
   aws cloudformation create-stack --template-body file://sns-create-topic-subscription.yaml --capabilities CAPABILITY_NAMED_IAM --parameters ParameterKey=SNSTopicName,ParameterValue=MySNSTopic ParameterKey=EmailAddress,ParameterValue=me@example.com --stack-name MySNSStack --region us-east-2
   ```

   In the preceding command, do the following\.
   + Replace `MySNSTopic` with whatever you want to name the Amazon SNS topic to send messages to\.
   + Replace `me@example.com` with your email address for Amazon SNS to send messages to\.
   + Replace `MySNSStack` with whatever you want to name the stack\.
   + Replace `us-east-2` with the ID of the AWS Region where you created the function \(see the corner of the **Lambda** pane in the **AWS Resources** window\)\.
**Note**  
If you use an IAM user to call AWS CloudFormation for this tutorial, instead of an AWS account root user or an IAM administrator user, the IAM user must have the following additional AWS access permissions\.  
 `cloudformation:CreateUploadBucket` 
 `cloudformation:GetTemplateSummary` 
 `cloudformation:ListStacks` 
 `iam:CreateRole` 
 `iam:PutRolePolicy` 
 `sns:CreateTopic` 
 `sns:GetTopicAttributes` 
 `sns:Publish` 
 `sns:SetTopicAttributes` 
 `sns:Subscribe` 
If you cannot add these permissions to the IAM user, see your organization's AWS account administrator\.

1. Confirm that AWS CloudFormation successfully created the stack\. To do this, use the AWS CLI to run the following command\.

   ```
   aws cloudformation describe-stacks --query 'Stacks[0].StackStatus' --output text --stack-name MySNSStack --region us-east-2
   ```

   Do not proceed until the AWS CLI outputs `CREATE_COMPLETE`\. \(You might need to run this command multiple times before you see `CREATE_COMPLETE`\.\)

1. In a few minutes, after AWS CloudFormation successfully creates the stack, check your inbox for an incoming email from **no\-reply@sns\.amazon\.com**\. In this email, choose the **Confirm subscription** link\. A webpage then opens, confirming the subscription\. Your email can't receive messages from this Amazon SNS topic until you confirm the subscription\.

1. Change the function's settings to use the newly created execution role\. To do this, in the **Environment** window, open the `template.yaml` file in the `~/environment/MySNSApplication` folder\. In the editor, between the lines of code `Properties` and `Handler: mySNSFunction/index.handler`, add the following two lines of code to specify the Amazon Resource Name \(ARN\) of the execution role for the function to use\.

   ```
   Properties:
     Role:
       'Fn::Sub': 'arn:aws:iam::${AWS::AccountId}:role/LambdaSNSExecutionRole'
     Handler: mySNSFunction/index.handler
   ```
**Note**  
Because the `template.yaml` file uses [YAML](http://yaml.org/) syntax, spacing is important\. Ensure that `Role` is indented exactly **two** spaces from `Properties`, and `'Fn::Sub'` is indented exactly **two** spaces from `Role`\. Be sure to use spaces, and not tabs, to represent whitespace in this file\.

1. In the same `template.yaml` file, extend the function's default timeout period by changing the `Timeout` value from `15` to `60`\. Then save the file\.

## Step 3: Run the Function Locally<a name="tutorial-lambda-advanced-run-local-function"></a>

In this step, you use the IDE to run the newly created function on the instance, which sends messages to your email address\. Currently, you can use the IDE to run functions that use only Node\.js or Python\.

1. With the IDE still displayed for the environment, in the **Lambda** pane of the **AWS Resources** window, expand **Local Functions**, expand the **MySNSApplication** Lambda folder, right\-click the **mySNSFunction** Lambda icon, and then choose **Run, Run Local**\.

1. In the **Payload** pane on the run tab, replace the pane's contents with the following, which sends the specified data to the function for processing\.

   ```
   {
     "region": "us-east-2",
     "message": "You just sent an email by using Amazon SNS.",
     "subject": "Hello from Amazon SNS",
     "topicARN": "arn:aws:sns:us-east-2:123456789012:MySNSTopic"
   }
   ```

   In the preceding payload, do the following\.
   + Replace `us-east-2` with the ID of the AWS Region where the Amazon SNS topic exists\.
   + Replace `123456789012` with your AWS account ID\.
   + Replace `MySNSTopic` with the name of the Amazon SNS topic\.

1. Choose **Run**\.

1. If the response shows a `statusCode` of `200`, then in a few minutes, check your email for the message that was sent\.

Compare your results to the following\.

![\[Running the Lambda function\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-run-lambda.png)

## Step 4: Debug the Function Locally<a name="tutorial-lambda-advanced-debug-local-function"></a>

In this step, you use the IDE to debug the function on the instance\. Currently, you can use the IDE to debug functions that use only Node\.js or Python\. Also, you can use the IDE to debug functions locally only\. You cannot use the IDE to debug functions in Lambda itself\.

1. With the IDE still displayed for the environment, open the `index.js` file\.

1. Create a breakpoint for the debugger\. To do this, in the editor, click inside the gutter next to the line of code that starts with `sns.publish` on line 45\. A red circle is displayed, representing the breakpoint\.

1. On the edge of the IDE, choose **Debugger**\.

1. Add four expressions for the debugger to watch\. To do this, in the **Watch Expressions** area, for **Type an expression here**, type `event['subject']`, and then press `Enter`\. Do this two more times, typing `context['memoryLimitInMB']` and `sns.endpoint.hostname`\.
**Note**  
If you completed the previous Lambda tutorial, you can delete any of those watch expressions that might still be there\. To do this, simply right\-click an expression, and then choose **Remove Watch Expression**\.

1. On the run tab from the previous step, choose the icon that looks like a bug\. \(It will switch from grey to green\.\)

1. Choose **Run**\.

   Code execution pauses at the breakpoint and displays the current values of the message's subject line, the function's memory limit in megabytes, and the Amazon SNS service's hostname\.

   You can also see these values by hovering your mouse over `event`, `context`, and `sns` in the code, followed by expanding the screen tip that is displayed\.

1. In the `Debugger` window, choose the blue **Resume** button to finish running the code\.

1. On the run tab, if the response shows a `statusCode` of `200`, then in a few minutes, check your email for the message that was sent\.

## Step 5: Run the API Locally<a name="tutorial-lambda-advanced-run-local-api"></a>

In this step, you use the IDE to have API Gateway run the Lambda function on the instance\.

1. In the **Lambda** pane of the **AWS Resources** window, right\-click the **mySNSFunction** Lambda icon, and then choose **Run, Run APIGateway Local**\.
**Note**  
You can also do this by choosing the **Lambda \(local\)** list on the run tab from the previous step, and then choosing **API Gateway \(local\)**\.

1. On the run tab, for **Path**, type `/`\.

1. For **Method**, choose **POST**\.

1. For **Body**, replace the pane's contents with the following, which sends this data as input to the API for processing\.

   ```
   {
     "region": "us-east-2",
     "message": "You just sent an email by using Amazon SNS.",
     "subject": "Hello from Amazon SNS",
     "topicARN": "arn:aws:sns:us-east-2:123456789012:MyDemoSNSTopic"
   }
   ```

1. If the bug icon is green, choose it to turn it off\. \(It switches back to grey\.\)

1. Choose **Run**\.

1. If the response shows `success`, then in a few minutes, check your email for the message that was sent\.

**Note**  
If the response is `Missing required key 'Message' in params` instead of `success`, then add the following code to your `index.js` file, save the file, and then try repeating this step again\.  

```
var sns = new AWS.SNS({apiVersion: '2010-03-31'});

// Begin adding code here.
if (event.body) {
  event = JSON.parse(event.body);
}
// End adding code here.

var params ={
  Message: event['message'],
  Subject: event['subject'],
  TopicArn: event['topicARN']
};
```
For more information, see [Response Differences When Invoking a Lambda Function from API Gateway](lambda-functions.md#lambda-functions-vs-api-gateway)\.

## Step 6: Debug the API Locally<a name="tutorial-lambda-advanced-debug-local-api"></a>

In this step, you use the IDE to have API Gateway debug the Lambda function on the instance\.

1. Ensure that the `index.js` file still has a breakpoint set on the line of code `sns.publish`\.

1. Ensure that the **Watch Expressions** area of the **Debugger** window is still watching `event['subject']`, `context['memoryLimitInMB']`, and `sns.endpoint.hostname`\.

1. On the run tab from the previous step, choose the icon that looks like a bug\. \(It switches from grey to green\.\)

1. Choose **Run**\.

   Code execution pauses at the breakpoint and displays the current values of the message's subject line, the function's memory limit in megabytes, the Amazon SNS service's hostname, and the caller's AWS access key ID\.

   You can also see these values by hovering your mouse over `event`, `context`, and `sns` followed by expanding the screen tip that is displayed\.

1. In the `Debugger` window, choose the blue **Resume** button to finish running the code\.

1. If the response shows `success`, then in a few minutes, check your email for the message that was sent\.

## Step 7: Deploy and Run the Changed Function in Production<a name="tutorial-lambda-advanced-deploy-function"></a>

In this step, you deploy the function that you changed in [Step 5: Run the API Locally](#tutorial-lambda-advanced-run-local-api) to Lambda and API Gateway\. You then test the changes in production to confirm the deployment\.

1. In the **Lambda** pane of the **AWS Resources** window, right\-click the **mySNSFunction** Lambda icon, and then choose **Deploy**\.

1. After the deployment succeeds, run the changed function in production\. To do this, in the **Lambda** pane of the **AWS Resources** window, right\-click the **mySNSFunction** Lambda icon, and then choose **Run, Run Remote**\.
**Note**  
You can also do this by choosing the **API Gateway \(local\)** list on the run tab from the previous step, and then choosing **Lambda \(remote\)**\.

1. Ensure that the **Payload** pane on the run tab still contains the following data\.

   ```
   {
     "region": "us-east-2",
     "message": "You just sent an email by using Amazon SNS.",
     "subject": "Hello from Amazon SNS",
     "topicARN": "arn:aws:sns:us-east-2:123456789012:MyDemoSNSTopic"
   }
   ```

1. Choose **Run**\.

1. If the response shows a `statusCode` of `200`, then in a few minutes, check your email for the message that was sent\.

1. Run the API in production\. To do this, in the **Lambda** pane of the **AWS Resources** window, right\-click the **mySNSFunction** Lambda icon, and then choose **Run, Run APIGateway Remote**\.
**Note**  
You can also do this by choosing the **Lambda \(remote\)** list on the run tab, and then choosing **API Gateway \(remote\)**\.

1. On the run tab, for **Path**, type `/`\.

1. For **Method**, choose **POST**\.

1. For **Body**, be sure the following data is still displayed\.

   ```
   {
     "region": "us-east-2",
     "message": "You just sent an email by using Amazon SNS.",
     "subject": "Hello from Amazon SNS",
     "topicARN": "arn:aws:sns:us-east-2:123456789012:MyDemoSNSTopic"
   }
   ```

1. Choose **Run**\.

1. If the response shows `success`, then in a few minutes, check your email for the message that was sent\.

## Step 8: Clean Up<a name="tutorial-lambda-advanced-clean-up"></a>

To prevent ongoing charges to your AWS account related to this tutorial, you can delete the function from Lambda, the API from API Gateway, the topic and subscription from Amazon SNS, the Lambda execution role from IAM, and the environment from AWS Cloud9\.

### Step 8\.1: Delete the Function and the API from Lambda and API Gateway<a name="step-8-1-delete-the-function-and-the-api-from-lam-and-abp"></a>

For AWS Cloud9 to create the function and its associated API, behind the scenes AWS Cloud9 uses the AWS Serverless Application Model \(AWS SAM\) to create a stack in AWS CloudFormation\. This stack then creates the function and its associated API\. In this procedure, you use the IDE to have AWS CloudFormation delete the stack, which also deletes the function and the API\. \(You could use the Lambda and API Gateway consoles instead of AWS CloudFormation to delete the function and its associated API\. However, that approach takes longer and still leaves the stack in AWS CloudFormation when it's no longer needed\.\)

**Warning**  
Deleting a stack cannot be undone\. When you delete this stack, the associated function and its API are deleted from Lambda and API Gateway and cannot be recovered\.

1. From the IDE, use the AWS CLI in the terminal to run the AWS CloudFormation`delete-stack` command, specifying the name of the stack\. This stack's name follows the format `cloud9-APPLICATION_NAME`, so you would specify `cloud9-MySNSApplication` for this tutorial\.

   ```
   aws cloudformation delete-stack --stack-name cloud9-MySNSApplication --region us-east-2
   ```

   If the command ran successfully, no output and no error message are displayed\.
**Note**  
If you use an IAM user to run this command for this tutorial, instead of an AWS account root user or an IAM administrator user, the IAM user must have the following additional AWS access permissions:  
 `cloudformation:ListStacks` 
 `cloudformation:DeleteStack` 
If you cannot add these permissions to the IAM user, see your organization's AWS account administrator\.

1. To verify that the stack is deleted, use the AWS CLI to run the AWS CloudFormation`describe-stacks` command\. If the function is deleted, a message is displayed that the stack doesn't exist\.

   ```
   aws cloudformation describe-stacks --query 'Stacks[0].StackStatus' --output text --stack-name cloud9-MySNSApplication --region us-east-2
   ```

1. If you no longer want to keep the local function in the IDE, delete the `~/environment/MySNSApplication` folder \(for example, by running the command `rm -rf ~/environment/MySNSApplication`\)\.

### Step 8\.2: Delete the Topic and Subscription from Amazon SNS and the Lambda Execution Role from IAM<a name="step-8-2-delete-the-topic-and-subscription-from-sns-and-the-lam-execution-role-from-iam"></a>

When you delete the AWS CloudFormation stack that you created in [Step 2: Set up Amazon SNS](#tutorial-lambda-advanced-sns-setup), the Amazon SNS topic and subscription are deleted, as well as the execution role for the Lambda function\.

**Warning**  
Deleting a stack cannot be undone\. When you delete this stack, the associated topic, subscription, and execution role are deleted from Amazon SNS and IAM and cannot be recovered\.

1. With the IDE still displayed for the environment, use the AWS CLI in the terminal to run the AWS CloudFormation`delete-stack` command, specifying the name of the stack\.

   ```
   aws cloudformation delete-stack --stack-name MySNSStack --region us-east-2
   ```
**Note**  
If you use an IAM user to run this command, instead of an AWS account root user or an IAM administrator user, the IAM user must have the following additional AWS access permissions\.  
 `cloudFormation:DeleteStack` 
 `iam:DeleteRole` 
 `iam:DeleteRolePolicy` 
 `sns:DeleteTopic` 
 `sns:Unsubscribe` 
If you cannot add these permissions to the IAM user, see your organization's AWS account administrator\.

   If the command ran successfully, no output and no error message are displayed\.

1. To verify that the stack is deleted, use the AWS CLI to run the following command\.

   ```
   aws cloudformation describe-stacks --query 'Stacks[0].StackStatus' --output text --stack-name MySNSStack --region us-east-2
   ```

   Keep running the preceding command until the output states that the stack doesn't exist\.

### Step 8\.3: Delete the Environment from AWS Cloud9<a name="step-8-3-delete-the-envtitle-from-ac9"></a>

**Warning**  
Deleting an environment cannot be undone\. Also, when you delete an EC2 environment, AWS Cloud9 also terminates the Amazon EC2 instance that it previously launched and connected to the environment\. Once terminated in Amazon EC2, the instance cannot be reactivated or recovered\.

1. With the IDE still displayed for the environment, open the dashboard in the AWS Cloud9 console\. To do this, on the menu bar in the IDE, choose **AWS Cloud9**, **Go To Your Dashboard**\.

1. Do one of the following\.
   + Choose the title that matches the name of the environment, and then choose **Delete**\.
   + Select the card that contains the name of the environment, and then choose **Delete**\.

1. In the **Delete** dialog box, type `Delete`, and then choose **Delete**\.

## Next Steps<a name="tutorial-lambda-advanced-next-steps"></a>

Explore any or all of the following topics to continue getting familiar with AWS Cloud9\.


****  

|  |  | 
| --- |--- |
|  Learn more about how to use AWS Cloud9 with Lambda  |   [Working with AWS Lambda Functions](lambda-functions.md)   | 
|  Learn more about the AWS Cloud9 IDE  |   [Getting Started: Basic Tutorials](tutorials-basic.md) and [Working with the IDE](ide.md)   | 
|  Invite others to use your environment with you, in real time and with text chat support  |   [Working with Shared Environments](share-environment.md)   | 
|  Create SSH environments \(environments that use cloud compute instances or servers that you create, instead of an Amazon EC2 instances that AWS Cloud9 creates for you\)\.  |   [Creating an Environment](create-environment.md) and [SSH Environment Host Requirements](ssh-settings.md)   | 
|  Use AWS Cloud9 with Amazon Lightsail  |   [Working with Amazon Lightsail Instances](lightsail-instances.md)   | 
|  Use AWS Cloud9 with AWS CodeStar  |   [Working with AWS CodeStar Projects](codestar-projects.md)   | 
|  Use AWS Cloud9 with AWS CodePipeline  |   [Working with AWS CodePipeline](codepipeline-repos.md)   | 
|  Use AWS Cloud9 with the AWS CLI, the aws\-shell, AWS CodeCommit, the AWS Cloud Development Kit \(AWS CDK\), GitHub, or Amazon DynamoDB, as well as Node\.js, Python, or other programming languages  |   [Tutorials and Samples](tutorials.md)   | 
|  Work with code for intelligent robotics applications in AWS RoboMaker\.  |   [Developing with AWS Cloud9](https://docs.aws.amazon.com/robomaker/latest/dg/cloud9.html) in the *AWS RoboMaker Developer Guide*   | 

To get help with AWS Cloud9 from the community, see the [AWS Cloud9 Discussion Forum](https://forums.aws.amazon.com/forum.jspa?forumID=268)\. \(When you enter this forum, AWS might require you to sign in\.\)

To get help with AWS Cloud9 directly from AWS, see the support options on the [AWS Support](https://aws.amazon.com/premiumsupport) page\.