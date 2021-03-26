# Tags<a name="tags"></a>

A tag is a label or attribute that you or AWS attaches to an AWS resource\. Each tag consists of a *key* and a paired *value*\. You can use tags to control access to your AWS Cloud9 resources, as described in [Control Access Using AWS Resource Tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) in the *[IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)*\. Tags can also help you manage billing information, as described in [User\-Defined Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/custom-tags.html)\.

When you [create an AWS Cloud9 EC2 development environment](create-environment-main.md), AWS Cloud9 includes certain system tags that it needs to manage the environment\. System tags start with "**aws:**"\. During that creation process, you can also add your own resource tags\.

After the environment is created, you can view the tags that are attached to the environment, add new resource tags to the environment, or modify or remove the tags that you added earlier\. You can attach up to 50 user\-defined tags to an AWS Cloud9 environment\.

View or update tags using one or more of the following methods\.
+ In the [AWS Cloud9 console](https://console.aws.amazon.com/cloud9/), select the environment you're interested in, and then choose **View Details**\.  
![\[View the details of an environment.\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/view-details.png)
+ Use the following AWS Cloud9 CLI commands: [https://docs.aws.amazon.com/cli/latest/reference/cloud9/list-tags-for-resource.html](https://docs.aws.amazon.com/cli/latest/reference/cloud9/list-tags-for-resource.html), [https://docs.aws.amazon.com/cli/latest/reference/cloud9/tag-resource.html](https://docs.aws.amazon.com/cli/latest/reference/cloud9/tag-resource.html), and [https://docs.aws.amazon.com/cli/latest/reference/cloud9/untag-resource.html](https://docs.aws.amazon.com/cli/latest/reference/cloud9/untag-resource.html)\.
+ Use the following AWS Cloud9 API actions: [ListTagsForResource](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_ListTagsForResource.html), [TagResource](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_TagResource.html), and [UntagResource](https://docs.aws.amazon.com/cloud9/latest/APIReference/API_UntagResource.html)\.

**Warning**  
Tags that you create or update for AWS Cloud9 by using the preceding methods are not automatically propagated to underlying resources\. For information about how to do this, see the next section, [Propagating tag updates to underlying resources](#tags-propagate)\.

## Propagating tag updates to underlying resources<a name="tags-propagate"></a>

When you use AWS Cloud9 CLI commands or API actions to add, modify, or remove the tags that are attached to an AWS Cloud9 environment, those changes aren't automatically propagated to underlying resources such as the AWS CloudFormation stack, the Amazon EC2 instance, and Amazon EC2 security groups\. You must manually propagate those changes\.

To make it easier to use the following procedures, you can obtain the environment ID for the environment you're interested in\. If you want to do this, follow these steps:

1. In the [AWS Cloud9 console](https://console.aws.amazon.com/cloud9/), select the environment that you're interested in, and then choose **View Details**\.

1. Look for the **Environment ARN** property and record the environment ID, which is the part of the environment ARN after "**environment:**"\.

You need to propagate tag updates to one or more of the following locations, depending on what you'll use the tags for\.

### Propagating tag updates to the AWS CloudFormation stack<a name="w37aac29c27c15c11"></a>

**Note**  
When you update tags to the AWS CloudFormation stack, those updates are automatically propagated to the Amazon EC2 instance and Amazon EC2 security groups that are associated with the stack\.

1. Navigate to the [AWS CloudFormation console\.](https://console.aws.amazon.com/cloudformation)

1. Find and choose the stack that corresponds to the AWS Cloud9 environment that you're interested in\. If you recorded the environment ID, you can use it to filter for the environment\.

1. On the **Stack info** tab, in the **Tags** section, review the list of tags\.

1. If you need to update the tags, choose **Update** near the top of the page, and follow the instructions\. For more information, see [Updating Stacks Directly](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-direct.html) in the *[AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/)*\.

You can also update tags using the [https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-stacks.html](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-stacks.html) and [https://docs.aws.amazon.com/cli/latest/reference/cloudformation/update-stack.html](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/update-stack.html) CLI commands\.

### Propagating tag updates to the Amazon EC2 instance<a name="w37aac29c27c15c13"></a>

1. Navigate to the [Amazon EC2 Instances](https://console.aws.amazon.com/ec2/home#Instances) console\.

1. Find and select the Amazon EC2 instance that corresponds to the AWS Cloud9 environment you're interested in\. If you recorded the environment ID earlier, you can use it to filter for the environment\.

1. On the **Tags** tab, view and update tags as necessary\.

You can also update tags using the [describe\-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-tags.html), [create\-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-tags.html), and [delete\-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-tags.html) CLI commands\.

### Propagating tag updates to Amazon EC2 security groups<a name="w37aac29c27c15c15"></a>

1. Navigate to the [Amazon EC2 Security Groups](https://console.aws.amazon.com/ec2/home#SecurityGroups) console\.

1. Find and select the security group that corresponds to the AWS Cloud9 environment that you're interested in\. If you recorded the environment ID earlier, you can use it to filter for the environment\.

1. Open the **Tags** tab to view and update tags as necessary\.

You can also update tags using the [describe\-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-tags.html), [create\-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-tags.html), and [delete\-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-tags.html) CLI commands\.