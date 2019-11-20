# Step 3: Clean Up<a name="tutorial-clean-up"></a>

\(Previous step: [Step 2: Basic Tour of the IDE](tutorial-tour-ide.md)\)

To prevent ongoing charges to your AWS account related to this tutorial, you should delete the environment\.

**Warning**  
Deleting an environment cannot be undone\.

## Delete the Environment by Using the AWS Cloud9 Console<a name="tutorial-clean-up-console"></a>

1. To open the dashboard, on the menu bar in the IDE, choose **AWS Cloud9**, **Go To Your Dashboard**\.

1. Do one of the following:
   + Choose the title inside of the **my\-demo\-environment** card, and then choose **Delete**\.  
![\[Deleting an environment in the environment details page\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-delete-env.png)
   + Select the **my\-demo\-environment** card, and then choose **Delete**\.  
![\[Deleting an environment in the environments list\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-delete-env-card.png)

1. In the **Delete** dialog box, enter `Delete`, and then choose **Delete**\. The delete operation will take a few minutes\.

**Note**  
If you followed this tutorial exactly, then the environment was an EC2 environment and AWS Cloud9 also terminates the Amazon EC2 instance that was connected to that environment\.  
However, if you used an SSH environment instead of following the tutorial, and that environment was connected to an Amazon EC2 instance, AWS Cloud9 doesn't terminate that instance\. If you don't terminate that instance later, your AWS account might continue to have ongoing charges for Amazon EC2 related to that instance\.

## Next Step<a name="tutorial-clean-up-next"></a>

[Related Information](tutorial-final-info.md)