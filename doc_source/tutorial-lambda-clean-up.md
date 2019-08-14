# Step 9: Clean Up<a name="tutorial-lambda-clean-up"></a>

\(Previous step: [Step 8: Change the Function and Deploy the Change](tutorial-lambda-change-and-deploy.md)\)

To prevent ongoing charges to your AWS account that are related to this tutorial after you're finished, you can delete the function from Lambda, the API from API Gateway, and the environment from AWS Cloud9\.

## Step 9\.1: Delete the Function and the API from Lambda and API Gateway<a name="tutorial-lambda-clean-up-delete-function-and-api"></a>

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

## Step 9\.2: Delete the Environment from AWS Cloud9<a name="tutorial-lambda-clean-up-delete-env"></a>

**Warning**  
Deleting an environment cannot be undone\. Also, when you delete an EC2 environment, AWS Cloud9 also terminates the Amazon EC2 instance that it previously launched and connected to the environment\. Once terminated in Amazon EC2, the instance cannot be reactivated or recovered\.

1. From the IDE, open the dashboard in the AWS Cloud9 console\. To do this, on the menu bar, choose **AWS Cloud9**, **Go To Your Dashboard**\.

1. Do one of the following:
   + Choose the title inside of the **my\-demo\-lambda\-environment** card, and then choose **Delete**\.
   + Select the **my\-demo\-lambda\-environment** card, and then choose **Delete**\.

1. In the **Delete** dialog box, type `Delete`, and then choose **Delete**\.

## Next Step<a name="tutorial-lambda-clean-up-next"></a>

[Wrapping Up](tutorial-lambda-next-steps.md)