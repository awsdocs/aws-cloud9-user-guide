# Step 4: Run or Debug the Function Locally<a name="tutorial-lambda-run-or-debug-local-function"></a>

\(Previous step: [Step 3: Add Code to the Function](tutorial-lambda-add-code.md)\)

## Step 4\.1: Run the Function Locally<a name="tutorial-lambda-run-local-function"></a>

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

## Step 4\.2: Debug the Function Locally<a name="tutorial-lambda-debug-local-function"></a>

In this step, you use the IDE to debug the function on the instance\. Currently, you can use the IDE to debug functions that use only Node\.js or Python\. Also, you can use the IDE to debug functions locally only\. You cannot use the IDE to debug functions in Lambda itself\.

1. In the `index.js` file, create a breakpoint for the debugger\. To do this, in the editor, next to the line of code `callback(null, response)`, click the gutter just to the left of line 62\. A red circle is displayed, representing the breakpoint\.

1. On the right edge of the IDE, choose **Debugger**\.

1. Add four expressions for the debugger to watch\. To do this, in the **Watch Expressions** area, for **Type an expression here**, type `event.option`, and then press `Enter`\. Do this three more times, typing `event.period`, `sc`, and `response.body`\.  
![\[Adding watch expressions\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-lambda-watch-expressions.png)

1. On the run tab that AWS Cloud9 opened in [Step 4\.1: Run the Function Locally](#tutorial-lambda-run-local-function), choose the icon that looks like a bug\. \(It switches from gray to green\.\)  
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

## Next Step<a name="tutorial-lambda-run-or-debug-local-function-next"></a>

[Step 5: Run or Debug the API Locally](tutorial-lambda-run-or-debug-local-api.md)