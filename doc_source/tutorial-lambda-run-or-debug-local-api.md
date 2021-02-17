# Step 5: Run or Debug the API Locally<a name="tutorial-lambda-run-or-debug-local-api"></a>

\(Previous step: [Step 4: Run or Debug the Function Locally](tutorial-lambda-run-or-debug-local-function.md)\)

## Step 5\.1: Run the API Locally<a name="tutorial-lambda-run-local-api"></a>

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

1. If the bug icon is green, choose it to turn it off\. \(It switches back to gray\.\)  
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

## Step 5\.2: Debug the API Locally<a name="tutorial-lambda-debug-local-api"></a>

In this step, you use the IDE to have API Gateway debug the Lambda function on the instance\.

1. Ensure that the `index.js` file still has a breakpoint set on the line of code `callback(null, response)`\.

1. Ensure that the **Watch Expressions** area of the **Debugger** window is still watching `event.option`, `event.period`, `sc`, and `response.body`\.

1. On the run tab from the previous step, choose the icon that looks like a bug\. \(It switches from gray to green\.\)

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

## Next Step<a name="tutorial-lambda-run-or-debug-local-api-next"></a>

[Step 6: Run the Function in Production](tutorial-lambda-run-deployed-function.md)