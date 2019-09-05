# Limits for AWS Cloud9<a name="limits"></a>

The following tables list limits in AWS Cloud9 and related AWS services\.
+  [AWS Cloud9 Limits](#limits-core) 
+  [Related AWS Service Limits](#limits-related) 

## AWS Cloud9 Limits<a name="limits-core"></a>

The following table provides the default limits for AWS Cloud9 for an AWS account\. Unless otherwise noted, each limit is Region\-specific\.

To request an increase for a limit that is adjustable, do the following:

1. Sign in to AWS and open the [Create case](https://console.aws.amazon.com/support/cases#/create) page on the [AWS Support Center website](https://console.aws.amazon.com/support/home)\.

1. Select **Service limit increase**\.

1. Under **Case classification**, choose *cloud9* from the **Limit type** list\.

1. Fill out the rest of the fields as appropriate\. If the request is urgent, choose **Phone** as the method of contact instead of **Web**\.

1. Choose **Submit**\.

These increases are not granted immediately, so it might take a couple of days for your increase to become effective\.


****  

| Resource | Default Limit | Adjustable | 
| --- | --- | --- | 
|  Maximum number of AWS Cloud9 EC2 development environments  |  [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/limits.html)  |  Yes  | 
|  Maximum number of SSH environments  |  [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/limits.html)  |  Yes  | 
|  Maximum number of members in an environment  |  The default maximum number of members is equal to the memory of the instance for that environment divided by 60 MB, with results rounded down\. For example, an instance with 1 GiB of memory can have a maximum of 17 members \(which is 1 GiB divided by 60 MB, rounded down\)\. If AWS Cloud9 cannot determine the memory of an instance, it defaults to a maximum of 8 users for each environment associated with that instance\. The absolute maximum number of members for an environment is 25\.  |  No1  | 
|  Maximum editable file size  |  8 MB  |  No  | 

1 You can [move an environment](move-environment.md#move-environment-move) to attempt to increase the default maximum number of members\. However, the absolute maximum number of members for an environment is still 25\.

## Related AWS Service Limits<a name="limits-related"></a>


****  

|  |  | 
| --- |--- |
|  Maximum number of Amazon Elastic Block Store \(Amazon EBS\) volumes  |  5,000 For more information, see [Amazon Elastic Block Store \(Amazon EBS\) Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_ebs) in the *Amazon Web Services General Reference*\.  | 
|  Maximum number of AWS CloudFormation stacks  |  200 For more information, see [AWS CloudFormation Limits](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html) in the *AWS CloudFormation User Guide*\.  | 
|  Amazon EC2 limits  |  See [Amazon Elastic Compute Cloud \(Amazon EC2\) Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_ec2) in the *Amazon Web Services General Reference*\.  | 