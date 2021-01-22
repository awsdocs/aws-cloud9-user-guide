# Working with AWS CloudFormation stacks using AWS Toolkit<a name="cloudformation-toolkit"></a>

The AWS Toolkit provides support for [AWS CloudFormation](https://aws.amazon.com/cloudformation/) stacks\. Using the AWS Toolkit, you can delete a AWS CloudFormation stack\.

## Deleting AWS CloudFormation stacks<a name="cloudformation-delete"></a>

You can use the AWS Toolkit to view and delete AWS CloudFormation stacks\.

### Prerequisites<a name="cloudformation-delete-prereq"></a>
+ Ensure that the credentials you're using in the AWS Cloud9 environment include appropriate read/write access to the AWS CloudFormation service\. If in the **AWS Explorer**, under **CloudFormation**, you see a message similar to "Error loading CloudFormation resources", check the permissions attached to those credentials\. Changes that you make to permissions will take a few minutes to affect the **AWS Explorer**\.

## To delete a AWS CloudFormation stack

1. In the **AWS Explorer**, open the context menu of the AWS CloudFormation stack you want to delete\.

1. Choose **Delete CloudFormation Stack**\.

1. In the message that appears, choose **Yes** to conﬁrm the delete\.

After the stack is deleted, it's no longer listed in the **AWS Explorer**\.