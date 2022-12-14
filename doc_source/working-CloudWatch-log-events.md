# Working with CloudWatch log events in log streams by using the AWS Toolkit<a name="working-CloudWatch-log-events"></a>

After you opened the **Log Steam** window, you can access the log events in each stream\. Log events are records of activity recorded by the application or resource being monitored\.

**Topics**
+ [Viewing and copying log stream information](#viewing-log-events)
+ [Save the contents of the log stream editor to a local file](#saving-CW-logs)

## Viewing and copying log stream information<a name="viewing-log-events"></a>

When you open a log stream, the **Log Stream** window displays that stream's sequence of log events\. 

1. To find a log stream to view, open the **Log Stream** window\. For more information, see [Viewing CloudWatch log groups and log streams](viewing-CloudWatch-logs.md)\.

   Each line listing an event is timestamped to show when it was logged\. 

1. You can view and copy information about the stream's events using the following options:
   + **View events by time: **Display the latest and older log events by choosing **Load newer events** or **Load older events**\. 
**Note**  
The **Log Stream** editor initially loads a batch of the most recent 10,000 lines of log events or 1 MB of log data, whichever is smaller\. If you choose **Load newer events**, the editor displays events that were logged after the last batch was loaded\. If you choose **Load older events**, the editor displays a batch of events that occurred before those currently displayed\. 
   + **Copy log events:** Select the events to copy, then open the context \(right\-click\) menu and select **Copy** from the menu\.
   + **Copy the log stream's name:** Open the context \(right\-click\) menu for the tab of the **Log Stream** window and choose **Copy Log Stream Name**\.

## Save the contents of the log stream editor to a local file<a name="saving-CW-logs"></a>

You can download the contents of the CloudWatch log stream editor to a `log` file on your local machine\.

**Note**  
You can use this option to save to file only those log events that are currently displayed in the log stream editor\. For example, suppose that the total size of a log stream is 5MB and only 2MB is loaded in the editor\. Your saved file also contains only 2MB of log data\. To display more data to be saved, choose **Load newer events** or **Load older events** in the editor\. 

1. To find a log stream to copy, open the **Log Streams** window \(see [Viewing CloudWatch log groups and log streams](viewing-CloudWatch-logs.md)\)\.

1. Open the context \(right\-click\) menu for the tab of the **Log Stream** window and choose **Save Current Log Content to File**

1. Use the dialog box to select or create a download folder for the log file, and choose **Save**\.