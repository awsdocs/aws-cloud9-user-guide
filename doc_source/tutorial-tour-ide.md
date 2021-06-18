# Step 2: Basic tour of the IDE<a name="tutorial-tour-ide"></a>

\(Previous step: [Step 1: Create an environment](tutorial-create-environment.md)\)

This part of the tutorial introduces some of the ways that you can use the AWS Cloud9 IDE to create and test applications\.
+ You can use an **editor** window to create and edit code\.
+ You can use a **terminal** window or a **Run Configuration** window to run your code without debugging it\.
+ You can use the **Debugger** window to debug your code\.

Perform these three tasks using JavaScript and the Node\.js engine\. See [Tutorials and samples](tutorials.md) for other programming languages\.

**Topics**
+ [Get your environment ready](#w43aac11c13c25b5b9)
+ [Write code](#w43aac11c13c25b5c11)
+ [Run your code](#w43aac11c13c25b5c13)
+ [Debug your code](#w43aac11c13c25b5c15)
+ [Next step](#tutorial-tour-ide-next)

## Get your environment ready<a name="w43aac11c13c25b5b9"></a>

Most of the tools you need to run and debug JavaScript code are already installed for you\. However, you need one additional Node\.js package for this tutorial\. Install it as follows\.

1. On the menu bar \(at the top of the AWS Cloud9 IDE\), choose **Window**, **New Terminal** \(or use an existing terminal window\)\.

1. In the terminal window \(one of the tabs in the bottom portion of the IDE\), enter the following\.

   ```
   npm install readline-sync
   ```

   Verify that the result is similar to the following \(If `npm WARN` messages are also displayed, you can ignore them\)\.

   ```
   + readline-sync@1.4.10
   added 1 package from 1 contributor and audited 5 packages in 0.565s
   found 0 vulnerabilities
   ```

## Write code<a name="w43aac11c13c25b5c11"></a>

Begin by writing some code\.

1. On the menu bar, choose **File**, **New File**\.

1. Add the following JavaScript to the new file\.

   ```
   var readline = require('readline-sync');
   var i = 10;
   var input;
   
   console.log("Hello Cloud9!");
   console.log("i is " + i);
   
   do {
       input = readline.question("Enter a number (or 'q' to quit): ");
       if (input === 'q') {
           console.log('OK, exiting.')
       }
       else{
           i += Number(input);
           console.log("i is now " + i);
       }
   } while (input != 'q');
   
   console.log("Goodbye!");
   ```

1. Choose **File**, **Save**, and then save the file as `hello-cloud9.js`\.

## Run your code<a name="w43aac11c13c25b5c13"></a>

Next, you can run your code\.

Depending on the programming language that you're using, there might be multiple ways in which you can run code\. This tutorial uses JavaScript, which you can run using a terminal window or a **Run Configuration** window\.

**To run the code using a Run Configuration window**

1. On the menu bar, choose **Run**, **Run Configurations**, **New Run Configuration**\.

1. In the new **Run Configuration** window \(one of the tabs in the bottom portion of the IDE\), enter `hello-cloud9.js` in the **Command** field, and then choose **Run**\.

1. Be sure that the **Run Configuration** prompt is active, and then interact with the application by entering a number at the prompt\.

1. View the output from your code in the **Run Configuration** window\. It should be similar to the following\.

![\[Run code in a Run Configuration.\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/basic-ide-run-run-config.png)

**To run the code using a terminal window**

1. Go to the terminal window that you used earlier \(or open a new one\)\.

1. In the terminal window, enter `ls` at the terminal prompt, and verify that your code file is in the list of files\.

1. Enter `node hello-cloud9.js` at the prompt to start the application\.

1. Interact with the application by entering a number at the prompt\.

1. View the output from your code in the terminal window\. It should be similar to the following\.

![\[Run code in a Run Configuration.\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/basic-ide-run-terminal.png)

## Debug your code<a name="w43aac11c13c25b5c15"></a>

Finally, you can debug your code by using the **Debugger** window\.

1. Add a breakpoint to your code at line 10 \(`if (input === 'q')`\) by choosing the margin next to line 10\. A red circle is displayed next to that line number, as follows\.  
![\[Adding a breakpoint to the code.\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/basic-ide-debug-breakpoint.png)

1. Open the **Debugger** window by choosing the **Debugger** button on the right side of the IDE\. Alternatively, choose **Window**, **Debugger** on the menu bar\.

   Then, put a watch on the `input` variable by choosing **Type an expression here** in the **Watch Expressions** section of the **Debugger** window\.  
![\[Debugger window, set watch\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/basic-ide-debug-watch.png)

1. Go to the **Run Configuration** window that you used earlier to run the code\. Choose **Run**\.

   Alternately, you can open a new **Run Configuration** window and start running the code by choosing **Run**, **Run With**, **Node\.js**, from the menu bar\.

1. Enter a number at the **Run Configuration** prompt and see that the code pauses at line 10\. The **Debugger** window shows the value you entered in **Watch Expressions**\.  
![\[Program stops at breakpoint\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/basic-ide-debug-break.png)

1. In the **Debugger** window, choose **Resume**, which is the blue arrow icon that is highlighted in the previous screenshot\.

1. Select **Stop** in the **Run Configuration** window to stop the debugger\.  
![\[Stop debugger.\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/basic-ide-debug-stop.png)

## Next step<a name="tutorial-tour-ide-next"></a>

[Step 3: Clean up](tutorial-clean-up.md)