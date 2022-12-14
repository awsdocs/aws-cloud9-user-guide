# Troubleshooting Systems Manager automation documents in AWS Toolkit<a name="systems-manager-troubleshoot"></a>

**I saved my automation document in AWS Toolkit, but I don’t see it in the AWS Management Console\.**  
Saving an automation document in AWS Toolkit doesn't publish the automation document to AWS\. For more information on publishing your Automation document, see [Publishing a Systems Manager automation document](systems-manager-automation-docs.md#systems-manager-publish)\.

**Publishing my automation document failed with a permissions error\.**  
Make sure your AWS credentials profile has the necessary permissions to publish Automation documents\. For an example permissions policy, see [IAM permissions for Systems Manager Automation documents](systems-manager-automation-docs.md#systems-manager-permissions)\.

**I published my automation document to AWS, but I don’t see it in the AWS Explorer pane\.**  
Make sure that you’ve published the document to the same AWS Region you’re browsing in the AWS Explorer pane\.

**I’ve deleted my automation document, but I’m still being billed for the resources it created\.**  
Deleting an automation document doesn’t delete the resources it created or modified\. You can identify the AWS resources that you’ve created from the [AWS Billing Management Console](https://console.aws.amazon.com/billing/home), explore your charges, and choose what resources to delete from there\.