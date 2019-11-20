# Step 3: Clean Up<a name="tutorial-clean-up-cli-step3"></a>

\(Previous step: [Step 2: Basic Tour of the IDE](tutorial-tour-ide-cli-step2.md)\)

To prevent ongoing charges to your AWS account related to this tutorial, you should delete the environment\.

**Warning**  
Deleting an environment cannot be undone\.

## Delete the Environment with the AWS CLI<a name="tutorial-clean-up-cli"></a>

1. Run the AWS Cloud9 `delete-environment` command, specifying the ID of the environment to delete\.

   ```
   aws cloud9 delete-environment --region MY-REGION --environment-id 12a34567b8cd9012345ef67abcd890e1
   ```

   In the preceding command, replace `MY-REGION` with the AWS Region in which the environment was created and `12a34567b8cd9012345ef67abcd890e1` with the ID of the environment to delete\.

   If you didn't save the ID when you created the environment, the ID can be found by using the AWS Cloud9 console\. Select the name of the environment in the console, then find the last part of the **Environment ARN**\.

1. If you created an Amazon VPC for this tutorial and you no longer need it, delete the VPC using the Amazon VPC console at [https://console\.aws\.amazon\.com/vpc](https://console.aws.amazon.com/vpc)\.

## Next Step<a name="tutorial-clean-up-cli-step3-next"></a>

[Related Information](tutorial-final-info-cli.md)