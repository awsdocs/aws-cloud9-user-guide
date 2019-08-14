# Step 6: Run the Function in Production<a name="tutorial-lambda-run-deployed-function"></a>

\(Previous step: [Step 5: Run or Debug the API Locally](tutorial-lambda-run-or-debug-local-api.md)\)

In this step, you use the IDE to run the function in Lambda itself\.

AWS Cloud9 deployed the function to Lambda during [Step 2: Create the Lambda Function and API](tutorial-lambda-create-function.md)\. However, AWS Cloud9 deployed the function before you made the changes in [Step 3: Add Code to the Function](tutorial-lambda-add-code.md)\. That original function was very basic, taking no payload and returning no response\. So, you must first deploy your changes to Lambda, and then you can run the deployed function there\.

1. In the **Lambda** pane of the **AWS Resources** window, expand **Local Functions**, expand the **MyDateTimeApplication** Lambda folder, right\-click the **myDateTimeFunction** Lambda icon, and then choose **Deploy**\.

1. After the deployment finishes, right\-click the **myDateTimeFunction** Lambda icon, and then choose **Run, Run Remote**\.
**Note**  
You can also do this by choosing the **API Gateway \(local\)** list on the run tab from the previous step, and then choosing **Lambda \(remote\)**\.

1. In the **Payload** pane on the run tab, be sure one of the payloads from [Step 4\.1: Run the Function Locally](tutorial-lambda-run-or-debug-local-function.md#tutorial-lambda-run-local-function) is visible\. If it isn't there, add it\.

1. Choose **Run**, and see the results in the **Response** area\. These should be the same results as in [Step 4\.1: Run the Function Locally](tutorial-lambda-run-or-debug-local-function.md#tutorial-lambda-run-local-function)\.

## Next Step<a name="tutorial-lambda-run-deployed-function-next"></a>

[Step 7: Run the API in Production](tutorial-lambda-run-deployed-api.md)