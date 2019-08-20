# Step 3: Run the Code<a name="tutorial-ruby-run"></a>

\(Previous step: [Step 2: Add Code](tutorial-ruby-code.md)\)

1. In the AWS Cloud9 IDE, on the menu bar, choose **Run**, **Run Configurations**, **New Run Configuration**\.

1. On the **\[New\] \- Idle** tab, choose **Runner: Auto**, and then choose **Ruby** \(item 1 in the screenshot shown below\)\.

1. For **Command** \(item 2 in the screenshot\), type `hello.rb 5 9`\. Given this command, `ARGV[0]` in the code receives a value of `5` and `ARGV[1]` receives a value of `9`\.

1. Choose the **Run** button \(item 3 below\), and compare your output to the following\.

   ```
   Hello, World!
   The sum of 2 and 3 is 5.
   The sum of 5 and 9 is 14.
   ```

![\[Output of running the Ruby code in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-ruby-simple.png)

## Next Step<a name="tutorial-ruby-run-next"></a>

[Step 4: Install and Configure the AWS SDK for Ruby](tutorial-ruby-sdk.md)