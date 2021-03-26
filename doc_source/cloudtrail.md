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
+  `DescribeEnvironmentStatus` 
+  `ListEnvironments` 
+  `ListTagsForResource` 
+  `TagResource` 
+  `UntagResource` 
+  `UpdateEnvironment` 
+  `UpdateEnvironmentMembership` 

**Note**  
Some CloudTrail events for AWS Cloud9 are not triggered by public API operations\. Instead, the following events are initiated by internal updates affecting user authentication and managed temporary credentials:  
`DisableManagedCredentialsByCollaborator`
`EnvironmentTokenSuccessfullyCreated`
`ManagedCredentialsUpdatedOnEnvironment`

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
+  [DescribeEnvironmentStatus](#cloudtrail-understanding-entries-describeenvironmentstatus) 
+  [ListEnvironments](#cloudtrail-understanding-entries-listenvironments) 
+  [ListTagsForResource](#cloudtrail-understanding-entries-listtagsforresource) 
+  [TagResource](#cloudtrail-understanding-entries-tagresource) 
+  [UntagResource](#cloudtrail-understanding-entries-untagresource) 
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

### DescribeEnvironmentStatus<a name="cloudtrail-understanding-entries-describeenvironmentstatus"></a>

The following example shows a CloudTrail log entry that demonstrates the `DescribeEnvironmentStatus` action\.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:sts::123456789012:myuser_role",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDACKCEVSQ6C2EXAMPLE",
                "arn": "arn:aws:sts::123456789012:myuser_role",
                "accountId": "123456789012",
                "userName": "barshane_role"
            },
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2021-03-12T15:10:54Z"
            }
        }
    },
    "eventTime": "2021-03-12T15:13:31Z",
    "eventSource": "cloud9.amazonaws.com",
    "eventName": "DescribeEnvironmentStatus",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "XX.XX.XXX.XX",
    "userAgent": "aws-internal/3 aws-sdk-java/1.11.951 Linux/4.9.230-0.1.ac.223.84.332.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.282-b08 java/1.8.0_282 vendor/Oracle_Corporation",
    "requestParameters": {
        "environmentId": "31ea8a12746a4221b7d8e07d9ef6ee21"
    },
    "responseElements": null,
    "requestID": "68b163fb-aa88-4f40-bafd-4a18bf24cbd5",
    "eventID": "c0fc52a9-7331-4ad0-a8ee-157995dfb5e6",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "123456789012"
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
       "recipientAccountId": "123456789012"
     }
   ]
 }
```

### ListTagsForResource<a name="cloudtrail-understanding-entries-listtagsforresource"></a>

The following example shows a CloudTrail log entry that demonstrates the `ListTagsForResource` action\.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:sts::123456789012:myuser_role",
        "accountId": "123456789012",
        "accessKeyId": "AIDACKCEVSQ6C2EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDACKCEVSQ6C2EXAMPLE",
                "arn": "123456789012:myuser_role",
                "accountId": "123456789012",
                "userName": "barshane_role"
            },
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2021-03-23T16:41:51Z"
            }
        }
    },
    "eventTime": "2021-03-23T16:42:58Z",
    "eventSource": "cloud9.amazonaws.com",
    "eventName": "ListTagsForResource",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "XX.XX.XXX.XX",
    "userAgent": "aws-internal/3 aws-sdk-java/1.11.976 Linux/4.9.230-0.1.ac.224.84.332.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.282-b08 java/1.8.0_282 vendor/Oracle_Corporation cfg/retry-mode/legacy",
    "requestParameters": {
        "resourceARN": "arn:aws:cloud9:us-east-1:123456789012:environment:3XXXXXXXXX6a4221b7d8e07d9ef6ee21"
    },
    "responseElements": {
        "tags": "HIDDEN_DUE_TO_SECURITY_REASONS"
    },
    "requestID": "5750a344-8462-4020-82f9-f1d500a75162",
    "eventID": "188d572d-9a14-4082-b98b-0389964c7c30",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "123456789012"
}
```

### TagResource<a name="cloudtrail-understanding-entries-tagresource"></a>

The following example shows a CloudTrail log entry that demonstrates the `TagResource` action\.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:sts:: 123456789012:myuser_role",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDACKCEVSQ6C2EXAMPLE",
                "arn": "arn:aws:iam::123456789012:role/myuser_role",
                "accountId": "123456789012",
                "userName": "MyUser"
            },
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2021-03-23T15:03:57Z"
            }
        }
    },
    "eventTime": "2021-03-23T15:08:16Z",
    "eventSource": "cloud9.amazonaws.com",
    "eventName": "TagResource",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "54.XXX.XXX.XXX",
    "userAgent": "aws-internal/3 aws-sdk-java/1.11.976 Linux/4.9.230-0.1.ac.224.84.332.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.282-b08 java/1.8.0_282 vendor/Oracle_Corporation cfg/retry-mode/legacy",
    "requestParameters": {
        "resourceARN": "arn:aws:cloud9:us-east-1:123456789012:environment:3XXXXXXXXX6a4221b7d8e07d9ef6ee21",
        "tags": "HIDDEN_DUE_TO_SECURITY_REASONS"
    },
    "responseElements": null,
    "requestID": "658e9d70-91c2-41b8-9a69-c6b4cc6a9456",
    "eventID": "022b2893-73d1-44cb-be6f-d3faa68e83b1",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "123456789012"
}
```

### UntagResource<a name="cloudtrail-understanding-entries-untagresource"></a>

The following example shows a CloudTrail log entry that demonstrates the `UntagResource` action\.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:sts::123456789012/MyUser",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AIDACKCEVSQ6C2EXAMPLE",
                "arn": "arn:aws:iam::123456789012:MyUser",
                "accountId": "123456789012",
                "userName": "MyUser"
            },
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2021-03-23T15:58:36Z"
            }
        }
    },
    "eventTime": "2021-03-23T16:05:08Z",
    "eventSource": "cloud9.amazonaws.com",
    "eventName": "UntagResource",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "3.XX.XX.XXX",
    "userAgent": "aws-internal/3 aws-sdk-java/1.11.976 Linux/4.9.230-0.1.ac.224.84.332.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.282-b08 java/1.8.0_282 vendor/Oracle_Corporation cfg/retry-mode/legacy",
    "requestParameters": {
        "resourceARN": "arn:aws:cloud9:us-east-1:123456789012:environment:3XXXXXXXXX6a4221b7d8e07d9ef6ee21",
        "tagKeys": "HIDDEN_DUE_TO_SECURITY_REASONS"
    },
    "responseElements": null,
    "requestID": "0eadaef3-dc0a-4cd7-85f6-135b8529f75f",
    "eventID": "41f2f2e2-4b17-43d4-96fc-9857981ca1de",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "123456789012"
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
  ]}
```