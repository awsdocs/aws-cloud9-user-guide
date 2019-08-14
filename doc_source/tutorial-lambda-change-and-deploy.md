# Step 8: Change the Function and Deploy the Change<a name="tutorial-lambda-change-and-deploy"></a>

\(Previous step: [Step 7: Run the API in Production](tutorial-lambda-run-deployed-api.md)\)

## Step 8\.1: Change the Function Locally<a name="tutorial-lambda-change-function"></a>

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

1. Run the changed function locally by following the instructions in [Step 4\.1: Run the Function Locally](tutorial-lambda-run-or-debug-local-function.md#tutorial-lambda-run-local-function)\. Notice that the `time` or `date` value is now displayed in the response\.

1. Run the original function in production by following the instructions in [Step 6: Run the Function in Production](tutorial-lambda-run-deployed-function.md)\. Notice that the `time` or `date` value doesn't display in the response yet\. This is because you have not deployed the changed function into production\. You do this in the next step\.

## Step 8\.2: Deploy the Changed Function into Production<a name="tutorial-lambda-deploy-function"></a>

In this step, you deploy the changed function again to Lambda itself\. You then test the changed function in production to confirm the deployment\.

1. In the **Lambda** pane of the **AWS Resources** window, right\-click the **myDateTimeFunction** Lambda icon, and then choose **Deploy**\.

1. After the deployment succeeds, run the changed function in production by following the instructions in [Step 6: Run the Function in Production](tutorial-lambda-run-deployed-function.md)\. Notice that the `time` or `date` value now appears in the response\.

Remember, whenever you make a change to the local function and you want to deploy those changes to Lambda \(and API Gateway, if an accompanying API exists\), be sure to follow this step\.

## Next Step<a name="tutorial-lambda-change-and-deploy-next"></a>

[Step 9: Clean Up](tutorial-lambda-clean-up.md)