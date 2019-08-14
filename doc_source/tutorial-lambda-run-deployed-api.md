# Step 7: Run the API in Production<a name="tutorial-lambda-run-deployed-api"></a>

\(Previous step: [Step 6: Run the Function in Production](tutorial-lambda-run-deployed-function.md)\)

In this step, you use the IDE to run the API in API Gateway itself\.

**Note**  
AWS Cloud9 deployed the API to API Gateway during [Step 2: Create the Lambda Function and API](tutorial-lambda-create-function.md)\. Because you haven't made any changes to the API since AWS Cloud9 first deployed it, you don't need to deploy the API again before you can run it in API Gateway itself\.

1. In the **Lambda** pane of the **AWS Resources** window, right\-click the **myDateTimeFunction** Lambda icon, and then choose **Run, Run APIGateway Remote**\.
**Note**  
You can also do this by choosing the **Lambda \(remote\)** list on the run tab from the previous step, and then choosing **API Gateway \(remote\)**\.

1. Ensure **Path** is still set to **/**, **Method** is still set to **POST**, and **Body** is still set to one of the bodies in [Step 5\.1: Run the API Locally](tutorial-lambda-run-or-debug-local-api.md#tutorial-lambda-run-local-api)\. If any of these aren't set correctly, set them\.

1. Choose **Run**, and see the results in the **Response** area, which should be the same results as in [Step 5\.1: Run the API Locally](tutorial-lambda-run-or-debug-local-api.md#tutorial-lambda-run-local-api)\.

## Next Step<a name="tutorial-lambda-run-deployed-api-next"></a>

[Step 8: Change the Function and Deploy the Change](tutorial-lambda-change-and-deploy.md)