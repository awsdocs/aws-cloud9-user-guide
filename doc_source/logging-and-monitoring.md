# Logging and monitoring in AWS Cloud9<a name="logging-and-monitoring"></a>

## Monitoring activity with CloudTrail<a name="cloudtrail-activity"></a>

AWS Cloud9 is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS Cloud9\. CloudTrail captures all API calls for AWS Cloud9 as events\. The calls captured include calls from the AWS Cloud9 console and from code calls to the AWS Cloud9 APIs\.

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon Simple Storage Service \(Amazon S3\) bucket, including events for AWS Cloud9\. 

If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**\. Using the information collected by CloudTrail, you can determine the request that was made to AWS Cloud9, the IP address from which the request was made, who made the request, when it was made, and additional details\.

For more information, see [Logging AWS Cloud9 API Calls with AWS CloudTrail](cloudtrail.md)\.

## Monitoring EC2 environment performance<a name="ec2-performance"></a>

If you're using an AWS Cloud9 EC2 development environment, you can monitor the reliability, availability, and performance of the associated Amazon EC2 instance\. With instance status monitoring, for example, you can quickly determine whether Amazon EC2 has detected any problems that might prevent your instances from running applications\. 

For more information, see [Monitoring Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring_ec2.html) in the *Amazon EC2 User Guide for Linux Instances*\.