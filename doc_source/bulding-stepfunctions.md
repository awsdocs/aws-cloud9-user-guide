# Working with AWS Step Functions using the AWS Toolkit<a name="bulding-stepfunctions"></a>

The AWS Toolkit provides support for [AWS Step Functions](https://aws.amazon.com/step-functions/)\. Step Functions allow you to create state machines that define workflows for AWS Lambda functions and other AWS services that support business\-critical application\.

You can use the AWS Toolkit to do the following with Step Functions:
+ Create and publish a state machine, which is a workflow made up of individual steps\.
+ Download a file that defines a state machine workflow\.
+ Run a state machine workflow with input you've entered or selected\. 

**Topics**
+ [Prerequisites](#bulding-stepfunctions-pre)
+ [Create and publish a state machine](#state-machine-create)
+ [Run a state machine in AWS Toolkit](#starting-stepfunctions)
+ [Download a state machine definition file and visualize its workflow](#sfn-download)

## Prerequisites<a name="bulding-stepfunctions-pre"></a>

Step Functions can run code and access AWS resources \(such as invoking a Lambda function\)\. To maintain security, you must grant Step Functions access to those resources by using an IAM role\. 

With AWS Toolkit, you can take advantage of automatically generated IAM roles that are valid for the AWS Region in which you create the state machine\. To create your own IAM role for a state machine, see [How AWS Step Functions Works with IAM](https://docs.aws.amazon.com/step-functions/latest/dg/procedure-create-iam-role.html) in the *AWS Step Functions Developer Guide*\. 

## Create and publish a state machine<a name="state-machine-create"></a>

When you create a state machine with AWS Toolkit, you choose a starter template that defines a workflow for a business case\. You can then edit or replace that template to suit your specific needs\. For more information on defining a state machine in a file that represents its structure, see [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html) in the *AWS Step Functions Developer Guide*\.

1. In the **AWS Explorer** pane, open the context \(right\-click\) menu for **Step Functions**, and then choose **Create a new Step Function state machine**\.

1. In the command panel, choose a starter template for your state machine's workflow\. 

1. Next, choose a format for the Amazon States Language \(ASL\) file that defines your state machine\.

   An editor opens to display the ASL file that defines the state machine's workflow\.
**Note**  
For information on editing the ASL file to customize your workflow, see [State Machine Structure](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-state-machine-structure.html)\. 

1. In the ASL file, choose **Publish to Step Functions** to add your state machine to the AWS Cloud\. 
**Note**  
You can also choose **Render graph** in the ASL file to display a visual representation of the state machine's workflow\.  
![\[File option to publish your state machine to the AWS Cloud.\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/)![\[File option to publish your state machine to the AWS Cloud.\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/)![\[File option to publish your state machine to the AWS Cloud.\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/)

1. In the command panel, choose an AWS Region to host your step function\.

1. Next, you can choose to create a new step function or update an existing one\.

------
#### [ Quick Create  ]

   This option allows you to create a new step function from the ASL file using the [step\-functions/latest/dg/concepts\-standard\-vs\-express\.html](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html)\. You're asked to specify the following:
   + An IAM role that allows your step function to run code and access AWS resources\. \(You can choose an automatically generated IAM role that's valid for the AWS Region in which you create the state machine\.\)
   + A name for your new function\.

   You can check that your state machine was successfully created and obtain its ARN in the AWS Toolkit output tab\.

------
#### [ Quick Update ]

   If a state machine already exists in the AWS Region, you can choose one to update with the current ASL file\. 

   You can check that your state machine was successfully updated and obtain its ARN in the AWS Toolkit output tab\.

------

   After you create a state machine, it appears under **Step Functions** in the **AWS Explorer** pane\. If it doesn't immediately appear, choose the **Toolkit** menu, **Refresh Explorer**\.

## Run a state machine in AWS Toolkit<a name="starting-stepfunctions"></a>

You can use AWS Toolkit to run remote state machines\. The running state machine receives JSON text as input and passes that input to the first state in the workflow\. Individual states receive JSON as input and usually pass JSON as output to the next state\. For more information, see [ Input and Output Processing in Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-input-output-filtering.html)\.

1. In the **AWS Explorer** pane, choose **Step Functions**\. Then open the context \(right\-click\) menu for a specific state machine and choose **Start Execution**\.

1. In the **Start Execution** pane, add the JSON\-formatted input for state machine's workflow by either entering the text directly in the field below or uploading a file from your local device\.

1. Choose **Execute**

   The AWS Toolkit output tab displays a confirmation that the workflow has started and the ARN of the process ID\. You can use that process ID to check in the AWS Step Functions console whether the workflow ran successfully\. You can also see the timestamps for when your workflow started and ended\. 

## Download a state machine definition file and visualize its workflow<a name="sfn-download"></a>

To download a state machine means you download a file containing JSON text that represents the structure of that state machine\. You can then edit this file to create a new state machine or update an existing one\. For more information, see [Amazon States Language](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html) in the *AWS Step Functions Developer Guide*\.

1. In the **AWS Explorer** pane, choose **Step Functions**\. Then open the context \(right\-click\) menu for a specific state machine and choose **Download Definition**\.
**Note**  
The context menu also offers the options to **Copy Name** and **Copy ARN**\.

1. In the **Save** dialog box, select the folder in your environment where you store downloaded state machine file, and then choose **Save**\.

   The JSON\-formatted file that defines your state machine's workflow is displayed in an editor\.

1. To display a visual representation of the workflow, choose **Render graph**\.

   A window displays a flowchart, which shows the sequence of states in your state machine's workflow\.  
![\[Visual representation of the state machine's workflow\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/)![\[Visual representation of the state machine's workflow\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/)![\[Visual representation of the state machine's workflow\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/)