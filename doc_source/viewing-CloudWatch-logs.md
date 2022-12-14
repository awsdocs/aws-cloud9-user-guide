# Viewing CloudWatch log groups and log streams using the AWS Toolkit<a name="viewing-CloudWatch-logs"></a>

A *log stream* is a sequence of log events that share the same source\. Each separate source of logs into CloudWatch Logs makes up a separate log stream\.

A *log group* is a group of log streams that share the same retention, monitoring, and access control settings\. You can define log groups and specify which streams to put into each group\. There's no limit on the number of log streams that can belong to one log group\. 

For more information, see [Working with Log Groups and Log Streams ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Working-with-log-groups-and-streams.html) in the *Amazon CloudWatch User Guide*\.

**Topics**
+ [Viewing log groups and log streams with the **CloudWatch Logs** node](#viewing-log-groups)

## Viewing log groups and log streams with the **CloudWatch Logs** node<a name="viewing-log-groups"></a>

1. Open AWS Explorer, if it isn't already open\.

1. Click the **CloudWatch Logs** node to expand the list of log groups\.

   The log groups for the current AWS Region are displayed under the **CloudWatch Logs** node\.

1. To view the log streams in a specific log group, open the context \(right\-click\) menu for the name of the log group, and then choose **View Log Streams**\.

1. The log group's contents are displayed under the **Select a log stream** heading\. 

   You can choose a specific stream from the list or filter the streams by entering text in the field\.

   After you choose a stream, the events in that stream are displayed in the IDE's **Log Streams** window\. For information about interacting with the log events in each stream, see [Working with CloudWatch log events](working-CloudWatch-log-events.md)\.