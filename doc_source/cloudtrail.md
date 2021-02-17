# Logging AWS Cloud9 API Calls with AWS CloudTrail<a name="cloudtrail"></a>

AWS Cloud9 is integrated with CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS Cloud9\. CloudTrail captures all API calls for AWS Cloud9 as events\. The calls captured include calls from the AWS Cloud9 console and from code calls to the AWS Cloud9 APIs\. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon Simple Storage Service \(Amazon S3\) bucket, including events for AWS Cloud9\. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**\. Using the information collected by CloudTrail, you can determine the request that was made to AWS Cloud9, the IP address from which the request was made, who made the request, when it was made, and additional details\.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/)\.

## AWS Cloud9 Information in CloudTrail<a name="ac9-information-in-ct"></a>

CloudTrail is enabled on your AWS account when you create the account\. When activity occurs in AWS Cloud9, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**\. You can view, search, and download recent events in your AWS account\. For more information, see [Viewing Events with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html)\.

For an ongoing record of events in your AWS account, including events for AWS Cloud9, create a trail\. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket\. By default, when you create a trail in the console, the trail applies to all AWS Regions\. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify\. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs\. For more information, see the following:
+  [Overview for Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) 
+  [CloudTrail Supported Services and Integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html) 
+  [Configuring Amazon SNS Notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html) 
+  [Receiving CloudTrail Log Files from Multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail Log Files from Multiple Accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html) 

AWS Cloud9 supports logging the following actions as events in CloudTrail log files:
+  `CreateEnvironmentEC2` 
+  `CreateEnvironmentSSH` 
+  `CreateEnvironmentMembership` 
+  `DeleteEnvironment` 
+  `DeleteEnvironmentMembership` 
+  `DescribeEnvironmentMemberships` 
+  `DescribeEnvironments` 
+  `ListEnvironments` 
+  `UpdateEnvironment` 
+  `UpdateEnvironmentMembership` 

Every event or log entry contains information about who generated the request\. The identity information helps you determine the following:
+ Whether the request was made with root or AWS Identity and Access Management \(IAM\) user credentials\.
+ Whether the request was made with temporary security credentials for a role or federated user\.
+ Whether the request was made by another AWS service\.

For more information, see the [CloudTrail userIdentity Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html)\.

## Understanding AWS Cloud9 log file entries<a name="cloudtrail-understanding-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify\. CloudTrail log files contain one or more log entries\. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters\. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order\.
+  [CreateEnvironmentEC2](#cloudtrail-understanding-entries-createenvironmentec2) 
+  [CreateEnvironmentSSH](#cloudtrail-understanding-entries-createenvironmentssh) 
+  [CreateEnvironmentMembership](#cloudtrail-understanding-entries-createenvironmentmembership) 
+  [DeleteEnvironment](#cloudtrail-understanding-entries-deleteenvironment) 
+  [DeleteEnvironmentMembership](#cloudtrail-understanding-entries-deleteenvironmentmembership) 
+  [DescribeEnvironmentMemberships](#cloudtrail-understanding-entries-describeenvironmentmemberships) 
+  [DescribeEnvironments](#cloudtrail-understanding-entries-describeenvironments) 
+  [ListEnvironments](#cloudtrail-understanding-entries-listenvironments) 
+  [UpdateEnvironment](#cloudtrail-understanding-entries-updateenvironment) 
+  [UpdateEnvironmentMembership](#cloudtrail-understanding-entries-updateenvironmentmembership) 

### CreateEnvironmentEC2<a name="cloudtrail-understanding-entries-createenvironmentec2"></a>

The following example shows a CloudTrail log entry that demonstrates the `CreateEnvironmentEC2` action\.

```
{
  "Records": [
    {
      "eventVersion": "1.05",
      "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/MyUser",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "MyUser",
        "sessionContext": {
          "attributes": {
            "mfaAuthenticated": "false",
            "creationDate": "2019-01-14T11:29:47Z"
          }
        },
        "invokedBy": "signin.amazonaws.com"
      },
      "eventTime": "2019-01-14T11:33:27Z",
      "eventSource": "cloud9.amazonaws.com",
      "eventName": "CreateEnvironmentEC2",
      "awsRegion": "us-west-2",
      "sourceIPAddress": "192.0.2.0",
      "userAgent": "signin.amazonaws.com",
      "requestParameters": {
        "instanceType": "t2.small",
        "subnetId": "subnet-1d4a9eEX",
        "description": "HIDDEN_DUE_TO_SECURITY_REASONS",
        "dryRun": true,
        "automaticStopTimeMinutes": 30,
        "name": "my-test-environment",
        "clientRequestToken": "cloud9-console-f8e37272-e541-435d-a567-5c684EXAMPLE"
      },
      "responseElements": null,
      "requestID": "f0e629fb-fd37-49bd-b2cc-e9822EXAMPLE",
      "eventID": "8a906445-1b2a-47e9-8d7c-5b242EXAMPLE",
      "eventType": "AwsApiCall",
      "recipientAccountId": "111122223333"
    }
  ]
}
```

### CreateEnvironmentSSH<a name="cloudtrail-understanding-entries-createenvironmentssh"></a>

The following example shows a CloudTrail log entry that demonstrates the `CreateEnvironmentSSH` action\.

```
{
  "Records": [
    {
      "eventVersion": "1.05",
      "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/MyUser",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "MyUser",
        "sessionContext": {
          "attributes": {
            "mfaAuthenticated": "false",
            "creationDate": "2019-01-14T11:29:47Z"
          }
        },
        "invokedBy": "signin.amazonaws.com"
      },
      "eventTime": "2019-01-14T11:33:27Z",
      "eventSource": "cloud9.amazonaws.com",
      "eventName": "CreateEnvironmentSSH",
      "awsRegion": "us-west-2",
      "sourceIPAddress": "192.0.2.0",
      "userAgent": "signin.amazonaws.com",
      "requestParameters": {
        "host": "198.51.100.0",
        "port": 22,
        "name": "my-ssh-environment",
        "description": "HIDDEN_DUE_TO_SECURITY_REASONS",
        "clientRequestToken": "cloud9-console-b015a0e9-469e-43e3-be90-6f432EXAMPLE",
        "loginName": "ec2-user"
      },
      "responseElements": {
        "environmentId": "5c39cc4a85d74a8bbb6e23ed6EXAMPLE"
      },
      "requestID": "f0e629fb-fd37-49bd-b2cc-e9822EXAMPLE",
      "eventID": "8a906445-1b2a-47e9-8d7c-5b242EXAMPLE",
      "eventType": "AwsApiCall",
      "recipientAccountId": "111122223333"
    }
  ]
}
```

### CreateEnvironmentMembership<a name="cloudtrail-understanding-entries-createenvironmentmembership"></a>

The following example shows a CloudTrail log entry that demonstrates the `CreateEnvironmentMembership` action\.

```
{
  "Records": [
    {
      "eventVersion": "1.05",
      "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/MyUser",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "MyUser",
        "sessionContext": {
          "attributes": {
            "mfaAuthenticated": "false",
            "creationDate": "2019-01-14T11:29:47Z"
          }
        },
        "invokedBy": "signin.amazonaws.com"
      },
      "eventTime": "2019-01-14T11:33:27Z",
      "eventSource": "cloud9.amazonaws.com",
      "eventName": "CreateEnvironmentMembership",
      "awsRegion": "us-west-2",
      "sourceIPAddress": "192.0.2.0",
      "userAgent": "signin.amazonaws.com",
      "requestParameters": {
        "environmentId": "2f5ff70a640f49398f67e3bdeEXAMPLE",
        "userArn": "arn:aws:iam::111122223333:user/MyUser",
        "permissions": "read-write"
      },
      "responseElements": {
        "membership": {
          "environmentId": "2f5ff70a640f49398f67e3bdeEXAMPLE",
          "permissions": "read-write",
          "userId": "AIDACKCEVSQ6C2EXAMPLE",
          "userArn": "arn:aws:iam::111122223333:user/MyUser"
        }
      },
      "requestID": "f0e629fb-fd37-49bd-b2cc-e9822EXAMPLE",
      "eventID": "8a906445-1b2a-47e9-8d7c-5b242EXAMPLE",
      "eventType": "AwsApiCall",
      "recipientAccountId": "111122223333"
    }
  ]
}
```

### DeleteEnvironment<a name="cloudtrail-understanding-entries-deleteenvironment"></a>

The following example shows a CloudTrail log entry that demonstrates the `DeleteEnvironment` action\.

```
{
  "Records": [
    {
      "eventVersion": "1.05",
      "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/MyUser",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "MyUser",
        "sessionContext": {
          "attributes": {
            "mfaAuthenticated": "false",
            "creationDate": "2019-01-14T11:29:47Z"
          }
        },
        "invokedBy": "signin.amazonaws.com"
      },
      "eventTime": "2019-01-14T11:33:27Z",
      "eventSource": "cloud9.amazonaws.com",
      "eventName": "DeleteEnvironment",
      "awsRegion": "us-west-2",
      "sourceIPAddress": "192.0.2.0",
      "userAgent": "signin.amazonaws.com",
      "requestParameters": {
        "environmentId": "2f5ff70a640f49398f67e3bdeEXAMPLE"
      },
      "responseElements": null,
      "requestID": "f0e629fb-fd37-49bd-b2cc-e9822EXAMPLE",
      "eventID": "8a906445-1b2a-47e9-8d7c-5b242EXAMPLE",
      "eventType": "AwsApiCall",
      "recipientAccountId": "111122223333"
    }
  ]
}
```

### DeleteEnvironmentMembership<a name="cloudtrail-understanding-entries-deleteenvironmentmembership"></a>

The following example shows a CloudTrail log entry that demonstrates the `DeleteEnvironmentMembership` action\.

```
{
  "Records": [
    {
      "eventVersion": "1.05",
      "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/MyUser",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "MyUser",
        "sessionContext": {
          "attributes": {
            "mfaAuthenticated": "false",
            "creationDate": "2019-01-14T11:29:47Z"
          }
        },
        "invokedBy": "signin.amazonaws.com"
      },
      "eventTime": "2019-01-14T11:33:27Z",
      "eventSource": "cloud9.amazonaws.com",
      "eventName": "DeleteEnvironmentMembership",
      "awsRegion": "us-west-2",
      "sourceIPAddress": "192.0.2.0",
      "userAgent": "signin.amazonaws.com",
      "requestParameters": {
        "environmentId": "2f5ff70a640f49398f67e3bdeEXAMPLE",
        "userArn": "arn:aws:iam::111122223333:user/MyUser",
      },
      "responseElements": null,
      "requestID": "f0e629fb-fd37-49bd-b2cc-e9822EXAMPLE",
      "eventID": "8a906445-1b2a-47e9-8d7c-5b242EXAMPLE",
      "eventType": "AwsApiCall",
      "recipientAccountId": "111122223333"
    }
  ]
}
```

### DescribeEnvironmentMemberships<a name="cloudtrail-understanding-entries-describeenvironmentmemberships"></a>

The following example shows a CloudTrail log entry that demonstrates the `DescribeEnvironmentMemberships` action\.

```
{
  "Records": [
    {
      "eventVersion": "1.05",
      "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/MyUser",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "MyUser",
        "sessionContext": {
          "attributes": {
            "mfaAuthenticated": "false",
            "creationDate": "2019-01-14T11:29:47Z"
          }
        },
        "invokedBy": "signin.amazonaws.com"
      },
      "eventTime": "2019-01-14T11:33:27Z",
      "eventSource": "cloud9.amazonaws.com",
      "eventName": "DescribeEnvironmentMemberships",
      "awsRegion": "us-west-2",
      "sourceIPAddress": "192.0.2.0",
      "userAgent": "signin.amazonaws.com",
      "requestParameters": {
        "nextToken": "NEXT_TOKEN_EXAMPLE",
        "permissions": [ "owner" ],
        "maxResults": 15
      },
      "responseElements": null,
      "requestID": "f0e629fb-fd37-49bd-b2cc-e9822EXAMPLE",
      "eventID": "8a906445-1b2a-47e9-8d7c-5b242EXAMPLE",
      "readOnly": true,
      "eventType": "AwsApiCall",
      "recipientAccountId": "111122223333"
    }
  ]
}
```

### DescribeEnvironments<a name="cloudtrail-understanding-entries-describeenvironments"></a>

The following example shows a CloudTrail log entry that demonstrates the `DescribeEnvironments` action\.

```
{
   "Records": [
     {
       "eventVersion": "1.05",
       "userIdentity": {
         "type": "IAMUser",
         "principalId": "AIDACKCEVSQ6C2EXAMPLE",
         "arn": "arn:aws:iam::111122223333:user/MyUser",
         "accountId": "111122223333",
         "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
         "userName": "MyUser",
         "sessionContext": {
           "attributes": {
             "mfaAuthenticated": "false",
             "creationDate": "2019-01-14T11:29:47Z"
           }
         },
         "invokedBy": "signin.amazonaws.com"
       },
       "eventTime": "2019-01-14T11:33:27Z",
       "eventSource": "cloud9.amazonaws.com",
       "eventName": "DescribeEnvironments",
       "awsRegion": "us-west-2",
       "sourceIPAddress": "192.0.2.0",
       "userAgent": "signin.amazonaws.com",
       "requestParameters": {
         "environmentIds": [
           "2f5ff70a640f49398f67e3bdeb811ab2"
         ]
       },
       "responseElements": null,
       "requestID": "f0e629fb-fd37-49bd-b2cc-e9822EXAMPLE",
       "eventID": "8a906445-1b2a-47e9-8d7c-5b242EXAMPLE",
       "readOnly": true,
       "eventType": "AwsApiCall",
       "recipientAccountId": "111122223333"
     }
   ]
 }
```

### ListEnvironments<a name="cloudtrail-understanding-entries-listenvironments"></a>

The following example shows a CloudTrail log entry that demonstrates the `ListEnvironments` action\.

```
{
   "Records": [
     {
       "eventVersion": "1.05",
       "userIdentity": {
         "type": "IAMUser",
         "principalId": "AIDACKCEVSQ6C2EXAMPLE",
         "arn": "arn:aws:iam::111122223333:user/MyUser",
         "accountId": "111122223333",
         "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
         "userName": "MyUser",
         "sessionContext": {
           "attributes": {
             "mfaAuthenticated": "false",
             "creationDate": "2019-01-14T11:29:47Z"
           }
         },
         "invokedBy": "signin.amazonaws.com"
       },
       "eventTime": "2019-01-14T11:33:27Z",
       "eventSource": "cloud9.amazonaws.com",
       "eventName": "ListEnvironments",
       "awsRegion": "us-west-2",
       "sourceIPAddress": "192.0.2.0",
       "userAgent": "signin.amazonaws.com",
       "requestParameters": {
         "nextToken": "NEXT_TOKEN_EXAMPLE",
         "maxResults": 15
       },
       "responseElements": null,
       "requestID": "f0e629fb-fd37-49bd-b2cc-e9822EXAMPLE",
       "eventID": "8a906445-1b2a-47e9-8d7c-5b242EXAMPLE",
       "readOnly": true,
       "eventType": "AwsApiCall",
       "recipientAccountId": "111122223333"
     }
   ]
 }
```

### UpdateEnvironment<a name="cloudtrail-understanding-entries-updateenvironment"></a>

The following example shows a CloudTrail log entry that demonstrates the `UpdateEnvironment` action\.

```
{
  "Records": [
    {
      "eventVersion": "1.05",
      "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/MyUser",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "MyUser",
        "sessionContext": {
          "attributes": {
            "mfaAuthenticated": "false",
            "creationDate": "2019-01-14T11:29:47Z"
          }
        },
        "invokedBy": "signin.amazonaws.com"
      },
      "eventTime": "2019-01-14T11:33:27Z",
      "eventSource": "cloud9.amazonaws.com",
      "eventName": "UpdateEnvironment",
      "awsRegion": "us-west-2",
      "sourceIPAddress": "192.0.2.0",
      "userAgent": "signin.amazonaws.com",
      "requestParameters": {
        "environmentId": "2f5ff70a640f49398f67e3bdeEXAMPLE",
        "description": "HIDDEN_DUE_TO_SECURITY_REASONS",
        "name": "my-test-environment-renamed"
      },
      "responseElements": null,
      "requestID": "f0e629fb-fd37-49bd-b2cc-e9822EXAMPLE",
      "eventID": "8a906445-1b2a-47e9-8d7c-5b242EXAMPLE",
      "eventType": "AwsApiCall",
      "recipientAccountId": "111122223333"
    }
  ]
}
```

### UpdateEnvironmentMembership<a name="cloudtrail-understanding-entries-updateenvironmentmembership"></a>

The following example shows a CloudTrail log entry that demonstrates the `UpdateEnvironmentMembership` action\.

```
{
  "Records": [
    {
      "eventVersion": "1.05",
      "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/MyUser",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "MyUser",
        "sessionContext": {
          "attributes": {
            "mfaAuthenticated": "false",
            "creationDate": "2019-01-14T11:29:47Z"
          }
        },
        "invokedBy": "signin.amazonaws.com"
      },
      "eventTime": "2019-01-14T11:33:27Z",
      "eventSource": "cloud9.amazonaws.com",
      "eventName": "UpdateEnvironmentMembership",
      "awsRegion": "us-west-2",
      "sourceIPAddress": "192.0.2.0",
      "userAgent": "signin.amazonaws.com",
      "requestParameters": {
        "environmentId": "2f5ff70a640f49398f67e3bdeEXAMPLE",
        "userArn": "arn:aws:iam::111122223333:user/MyUser",
        "permissions": "read-only"
      },
      "responseElements": {
        "membership": {
          "environmentId": "2f5ff70a640f49398f67e3bdeEXAMPLE",
          "permissions": "read-only",
          "userId": "AIDACKCEVSQ6C2EXAMPLE",
          "userArn": "arn:aws:iam::111122223333:user/MyUser"
        }
      },
      "requestID": "f0e629fb-fd37-49bd-b2cc-e9822EXAMPLE",
      "eventID": "8a906445-1b2a-47e9-8d7c-5b242EXAMPLE",
      "eventType": "AwsApiCall",
      "recipientAccountId": "111122223333"
    }
  ]
}
```