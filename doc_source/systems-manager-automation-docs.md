# Working with Systems Manager automation documents<a name="systems-manager-automation-docs"></a>

AWS Systems Manager gives you visibility and control of your infrastructure on AWS\. Systems Manager provides a unified user interface so you can view operational data from multiple AWS services and automate operational tasks across your AWS resources\.

A [Systems Manager document](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-systems-manager-docs.html) defines the actions that Systems Manager performs on your managed instances\. An automation document is a type of Systems Manager document that you use to perform common maintenance and deployment tasks such as creating or updating an Amazon Machine Image \(AMI\)\. This topic outlines how to create, edit, publish, and delete automation documents with AWS Toolkit\.

**Topics**
+ [Assumptions and prerequisites](#systems-manager-assumptions)
+ [IAM permissions for Systems Manager Automation documents](#systems-manager-permissions)
+ [Creating a new Systems Manager automation document](#systems-manager-create)
+ [Publishing a Systems Manager automation document](#systems-manager-publish)
+ [Editing an existing Systems Manager automation document](#systems-manager-open)
+ [Working with versions](#systems-manager-edit-default-version)
+ [Deleting a Systems Manager automation document](#systems-manager-delete)
+ [Running a Systems Manager automation document](#systems-manager-run)
+ [Troubleshooting Systems Manager automation documents in AWS Toolkit](systems-manager-troubleshoot.md)

## Assumptions and prerequisites<a name="systems-manager-assumptions"></a>

Before you begin, make sure:
+ You’re familiar with Systems Manager\. For more information, see the [https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)\.
+ You’re familiar with Systems Manager automation use cases\. For more information, see [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) in the *AWS Systems Manager User Guide*\.

## IAM permissions for Systems Manager Automation documents<a name="systems-manager-permissions"></a>

You must have a credentials profile that contains the AWS Identity and Access Management \(IAM\) permissions necessary to create, edit, publish, and delete Systems Manager automation documents\. The following policy document defines the necessary IAM permissions that can be used in a principal policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ssm:ListDocuments",
                "ssm:ListDocumentVersions",
                "ssm:DescribeDocument",
                "ssm:GetDocument",
                "ssm:CreateDocument",
                "ssm:UpdateDocument",
                "ssm:UpdateDocumentDefaultVersion",
                "ssm:DeleteDocument"
            ],
            "Resource": "*"
        }
    ]
}
```

For information on how to update an IAM policy, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*\.

## Creating a new Systems Manager automation document<a name="systems-manager-create"></a>

You can create an automation document in `JSON` or `YAML` using AWS Toolkit\. When you create an automation document, it's presented in an untitled file\. You can name your file and save it, but the file isn't uploaded to AWS until you publish it\.

**To create a new automation document**

1. Choose the search icon on the left navigation pane or press **Ctrl\+P** to open the Search pane\.

1. In the Search pane, start to enter the term "systems manager" and choose the **AWS: Create a new Systems Manager Document Locally** command when it displays\.

1. Choose one of the starter templates for a Hello World example\.

1. Choose either `JSON` or `YAML` as the format for your document\.

   The editor displays your new automation document\.

**Note**  
When you first create a local automation document, it doesn't automatically appear in AWS\. You must publish it to AWS before you can run it\. 

## Publishing a Systems Manager automation document<a name="systems-manager-publish"></a>

After you create or edit your automation document in AWS Toolkit, you can publish it to AWS\.

**To publish your automation document**

1. Open the automation document that you want to publish using the procedure outlined in [Editing an existing Systems Manager automation document](#systems-manager-open)\.

1. Choose the search icon on the left navigation pane or press **Ctrl\+P** to open the Search pane\.

1. In the Search pane, start to enter the term "systems manager" and choose the **AWS: Publish a new Systems Manager Document ** command when it displays\.

1. For **Step 1 of 3**, choose the AWS Region where you want to publish the document\.

1. For **Step 2 of 3**, choose **Quick Create** to create an automation document\. Or choose **Quick Update** to update an existing automation document in that AWS Region\.
**Note**  
You can update only automation documents that you own\. If you choose **Quick Update** and you don't own any documents in that Region, a message informs you to publish a document before updating it\.

1. For **Step 3 of 3**, depending on your choice in the previous step, enter the name of a new automation document or select an existing document to update\.
**Note**  
When you publish an update to an existing automation document in AWS, a new version is added to the document\. If a document has multiple versions, you can set the [default one](#systems-manager-edit-default-version)\.

## Editing an existing Systems Manager automation document<a name="systems-manager-open"></a>

You use the AWS Explorer to find existing Systems Manager automation documents\. When you open an existing document, it appears as an untitled file in an AWS Cloud9 editor\. There are three types of automation document that you download:
+ **Owned by Amazon**: Pre\-configured SSM documents that can be used by specifying parameters at runtime\.
+ **Owned by me**: Documents that I've created and published to AWS\. 
+ **Shared with me**: Documents that owners have shared with you, based on your AWS account ID\. 

The only type of documents that you can update on AWS are those that are *owned by me*\. You can also download automation documents that are shared or owned by Amazon, and edit them in AWS Cloud9\. But when you publish to AWS, you must use either create a new document or update an existing document you own\. You can't create new versions of documents that have another owner or are owned by Amazon\.

For more information, see [AWS Systems Manager documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html) in the *AWS Systems Manager User Guide*\.

1. In the AWS Explorer, for **Systems Manager**, choose the category of SSM document you want to download: **Owned by Amazon**, **Owned by me**, or **Shared with me**\.

1. For a specific document, open the context \(right\-click\) menu and choose **Download as YAML** or **Download as JSON**\.

   The formatted SSM document displays in a new editor tab\.

After you've finished editing, you can use the **AWS: Publish a new Systems Manager Document ** command to create a new document in the AWS Cloud or update an existing document that you own\. 

## Working with versions<a name="systems-manager-edit-default-version"></a>

Systems Manager automation documents use versions for change management\. With AWS Toolkit, you can set the default version of the document, which is the version that's used when you run the document \. 

**To set a default version**
+ In the AWS Explorer, navigate to the document that you want to set the default version on, open the context \(right\-click\) menu for the document, and choose **Set default version**\.
**Note**  
If the chosen document only has one version, you won't be able to change the default\.

## Deleting a Systems Manager automation document<a name="systems-manager-delete"></a>

You can delete the automation documents that you own in AWS Toolkit\. Deleting an Automation document deletes the document and all versions of the document\. 

**Important**  
Deleting is a destructive action that can't be undone\.
Deleting an automation document that has already been started doesn't delete the AWS resources that were created or modified when it was run\.
Deleting is permitted only if you own the document\.

**To delete your automation document**

1. In the AWS Explorer pane, for **Systems Manager**, expand **Owned by Me** to list your documents\.

1. Open the context \(right\-click\) menu for the document you want to delete, and choose **Delete document**\.

1. In the warning dialog box that displays, choose **Delete** to confirm\.

## Running a Systems Manager automation document<a name="systems-manager-run"></a>

After your automation document is published to AWS, you can run it to perform tasks on your behalf in your AWS account\. To run your Automation document, you use the AWS Management Console, the Systems Manager APIs, the AWS CLI, or the AWS Tools for PowerShell\. For instructions on how to run an automation document, see [Running a simple automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing.html) in the *AWS Systems Manager User Guide*\.

Alternatively, if you want to use one of the AWS SDKs with the Systems Manager APIs to run your Automation document, see the [AWS SDK references](https://aws.amazon.com/getting-started/tools-sdks/)\.

**Important**  
Running an automation document can create new resources in AWS and can incur billing costs\. We strongly recommend that you understand what your automation document will create in your account before you run it\.