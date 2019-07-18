# Amazon DynamoDB Sample for AWS Cloud9<a name="sample-dynamodb"></a>

This sample enables you to set up an AWS Cloud9 development environment to work with Amazon DynamoDB\.

DynamoDB is a fully managed NoSQL database service\. You can use DynamoDB to create a database table that can store and retrieve any amount of data, and serve any level of request traffic\. DynamoDB automatically spreads the data and traffic for the table over a sufficient number of servers to handle the request capacity specified and the amount of data stored, while maintaining consistent and fast performance\. For more information, see [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) on the AWS website\.

Creating this sample might result in charges to your AWS account\. These include possible charges for services such as Amazon EC2 and DynamoDB\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/) and [Amazon DynamoDB Pricing](https://aws.amazon.com/dynamodb/pricing/)\.

For information about additional AWS database offerings, see [Amazon Relational Database Service \(RDS\)](https://aws.amazon.com/rds/), [Amazon ElastiCache](https://aws.amazon.com/elasticache/), and [Amazon Redshift](https://aws.amazon.com/redshift/) on the AWS website\. See also [AWS Database Migration Service](https://aws.amazon.com/dms/) on the AWS website\.
+  [Prerequisites](#sample-dynamodb-prereqs) 
+  [Step 1: Install and Configure the AWS CLI, the aws\-shell, or Both in Your Environment](#sample-dynamodb-cli-setup) 
+  [Step 2: Create a Table](#sample-dynamodb-create-table) 
+  [Step 3: Add an Item to the Table](#sample-dynamodb-add-item) 
+  [Step 4: Add Multiple Items to the Table](#sample-dynamodb-add-items) 
+  [Step 5: Create a Global Secondary Index](#sample-dynamodb-create-index) 
+  [Step 6: Get Items from the Table](#sample-dynamodb-get-items) 
+  [Step 7: Clean Up](#sample-dynamodb-clean-up) 

## Prerequisites<a name="sample-dynamodb-prereqs"></a>

Before you use this sample, be sure to meet the following requirements\.
+  **You must have an existing AWS Cloud9 EC2 development environment\.** This sample assumes you already have an EC2 environment that is connected to an Amazon EC2 instance running Amazon Linux or Ubuntu Server\. If you have a different type of environment or operating system, you might need to adapt this sample's instructions to set up related tools\. See [Creating an Environment in AWS Cloud9](create-environment.md) for details\.
+  **You have the AWS Cloud9 IDE for the existing environment already open\.** When you open an environment, AWS Cloud9 opens the IDE for that environment in your web browser\. See [Opening an Environment in AWS Cloud9](open-environment.md) for details\.

## Step 1: Install and Configure the AWS CLI, the aws\-shell, or Both in Your Environment<a name="sample-dynamodb-cli-setup"></a>

In this step, you use the AWS Cloud9 IDE to install and configure the AWS CLI, the aws\-shell, or both in your environment so you can run commands to interact with DynamoDB\. Then you use the AWS CLI to run a basic DynamoDB command to test your installation and configuration\.

1. To set up credentials management for the AWS CLI or the aws\-shell and to install the AWS CLI, the aws\-shell, or both in your environment, follow Steps 1 and 2 in the [AWS CLI and aws\-shell Sample](sample-aws-cli.md), and then return to this topic\. If you already installed and configured the AWS CLI, the aws\-shell, or both in your environment, you don't need to do it again\.

1. Test the installation and configuration of the AWS CLI, the aws\-shell, or both by running the DynamoDB** `list-tables` ** command from a terminal session in your environment to list your existing DynamoDB tables, if there are any\. To start a new terminal session, on the menu bar, choose **Windows**, **New Terminal**\.

   ```
   aws dynamodb list-tables # For the AWS CLI.
   dynamodb list-tables     # For the aws-shell.
   ```
**Note**  
Throughout this sample, if you're using the aws\-shell, omit `aws` from each command that starts with `aws`\. To start the aws\-shell, run the ** `aws-shell` ** command\. To stop using the aws\-shell, run the ** `.exit` ** or ** `.quit` ** command\.

   If this command succeeds, it outputs a `TableNames` array containing a list of existing DynamoDB tables that you might already have\. If you have no DynamoDB tables yet, the `TableNames` array will be empty\.

   ```
   {
     "TableNames": []
   }
   ```

   If you do have any DynamoDB tables, the `TableNames` array contains a list of the table names\.

## Step 2: Create a Table<a name="sample-dynamodb-create-table"></a>

In this step, you create a table in DynamoDB and specify the table's name, layout, simple primary key, and data throughput settings\.

This sample table, named `Weather`, contains information about weather forecasts for a few cities in the United States\. The table holds the following types of information \(in DynamoDB, each piece of information is known as an *attribute*\):
+ Required unique city ID \(`CityID`\)
+ Required forecast date \(`Date`\)
+ City name \(`City`\)
+ State name \(`State`\)
+ Forecast weather conditions \(`Conditions`\)
+ Forecast temperatures \(`Temperatures`\)
  + Forecast high, in degrees Fahrenheit \(`HighF`\)
  + Forecast low, in degrees Fahrenheit \(`LowF`\)

To create the table, in a terminal session in the AWS Cloud9 IDE, run the DynamoDB** `create-table` ** command\.

```
aws dynamodb create-table \
--table-name Weather \
--attribute-definitions \
  AttributeName=CityID,AttributeType=N AttributeName=Date,AttributeType=S \
--key-schema \
  AttributeName=CityID,KeyType=HASH AttributeName=Date,KeyType=RANGE \
--provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
```

In this command:
+  `--table-name` represents the table name \(`Weather` in this sample\)\. Table names must be unique within each AWS Region in your AWS account\.
+  `--attribute-definitions` represents the attributes that are used to uniquely identify the table items\. Each of this table's items are uniquely identified by a combination of a numerical `ID` attribute and a `Date` attribute represented as an ISO\-8601 formatted string\.
+  `--key-schema` represents the table's key schema\. This table has a composite primary key of `CityID` and `Date`\. This means that each of the table items must have a `CityID` attribute value and a `Date` attribute value, but no two items in the table can have both the same `CityID` attribute value and `Date` attribute value\.
+  `--provisioned-throughput` represents the table's read\-write capacity\. DynamoDB allows up to 5 strongly consistent reads per second for items up to 4 KB in size, or up to 5 eventually consistent reads per second for items up to 4 KB in size\. DynamoDB also allows up to 5 writes per second for items up to 1 KB in size\.
**Note**  
Setting higher provisioned throughput might result in additional charges to your AWS account\.  
For more information about this and other DynamoDB commands, see [dynamodb](https://docs.aws.amazon.com/cli/latest/reference/dynamodb/index.html) in the *AWS CLI Command Reference*\.

If this command succeeds, it displays summary information about the new table that is being created\. To confirm the table is successfully created, run the DynamoDB** `describe-table` ** command, specifying the table's name \(`--table-name`\)\.

```
aws dynamodb describe-table --table-name Weather
```

When the table is successfully created, the `TableStatus` value changes from `CREATING` to `ACTIVE`\. Do not proceed past this step until the table is successfully created\.

## Step 3: Add an Item to the Table<a name="sample-dynamodb-add-item"></a>

In this step, you add an item to the table you just created\.

1. Create a file named `weather-item.json` with the following content\. To create a new file, on the menu bar, choose **File**, **New File**\. To save the file, choose **File**, **Save**\.

   ```
   {
     "CityID": { "N": "1" },
     "Date": { "S": "2017-04-12" },
     "City": { "S": "Seattle" },
     "State": { "S": "WA" },
     "Conditions": { "S": "Rain" },
     "Temperatures": { "M": {
         "HighF": { "N": "59" },
         "LowF": { "N": "46" }
       }
     }
   }
   ```

   In this code, `N` represents an attribute value that is a number\. `S` is a string attribute value\. `M` is a map attribute, which is a set of attribute\-value pairs\. You must specify an attribute's data type whenever you work with items\. For additional available attribute data types, see [Data Types](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes) in the *Amazon DynamoDB Developer Guide*\.

1. Run the DynamoDB** `put-item` ** command, specifying the table's name \(`--table-name`\) and the path to the JSON\-formatted item \(`--item`\)\.

   ```
   aws dynamodb put-item \
   --table-name Weather \
   --item file://weather-item.json
   ```

   If the command succeeds, it runs without error, and no confirmation message is displayed\.

1. To confirm the table's current contents, run the DynamoDB** `scan` ** command, specifying the table's name \(`--table-name`\)\.

   ```
   aws dynamodb scan --table-name Weather
   ```

   If the command succeeds, summary information about the table and the item you just added is displayed\.

## Step 4: Add Multiple Items to the Table<a name="sample-dynamodb-add-items"></a>

In this step, you add several more items to the `Customers` table\.

1. Create a file named `more-weather-items.json` with the following content\.

   ```
   {
     "Weather": [
       {
         "PutRequest": {
           "Item": {
             "CityID": { "N": "1" },
             "Date": { "S": "2017-04-13" },
             "City": { "S": "Seattle" },
             "State": { "S": "WA" },
             "Conditions": { "S": "Rain" },
             "Temperatures": { "M": {
                 "HighF": { "N": "52" },
                 "LowF": { "N": "43" }
               }
             }
           }
         }
       },
       {
         "PutRequest": {
           "Item": {
             "CityID": { "N": "1" },
             "Date": { "S": "2017-04-14" },
             "City": { "S": "Seattle" },
             "State": { "S": "WA" },
             "Conditions": { "S": "Rain" },
             "Temperatures": { "M": {
                 "HighF": { "N": "49" },
                 "LowF": { "N": "43" }
               }
             }
           }
         }
       },
       {
         "PutRequest": {
           "Item": {
             "CityID": { "N": "2" },
             "Date": { "S": "2017-04-12" },
             "City": { "S": "Portland" },
             "State": { "S": "OR" },
             "Conditions": { "S": "Thunderstorms" },
             "Temperatures": { "M": {
                 "HighF": { "N": "59" },
                 "LowF": { "N": "43" }
               }
             }
           }
         }
       },
       {
         "PutRequest": {
           "Item": {
             "CityID": { "N": "2" },
             "Date": { "S": "2017-04-13" },
             "City": { "S": "Portland" },
             "State": { "S": "OR" },
             "Conditions": { "S": "Rain" },
             "Temperatures": { "M": {
                 "HighF": { "N": "51" },
                 "LowF": { "N": "41" }
               }
             }
           }
         }
       },
       {
         "PutRequest": {
           "Item": {
             "CityID": { "N": "2" },
             "Date": { "S": "2017-04-14" },
             "City": { "S": "Portland" },
             "State": { "S": "OR" },
             "Conditions": { "S": "Rain Showers" },
             "Temperatures": { "M": {
                 "HighF": { "N": "49" },
                 "LowF": { "N": "39" }
               }
             }
           }
         }
       },
       {
         "PutRequest": {
           "Item": {
             "CityID": { "N": "3" },
             "Date": { "S": "2017-04-12" },
             "City": { "S": "Portland" },
             "State": { "S": "ME" },
             "Conditions": { "S": "Rain" },
             "Temperatures": { "M": {
                 "HighF": { "N": "59" },
                 "LowF": { "N": "40" }
               }
             }
           }
         }
       },
       {
         "PutRequest": {
           "Item": {
             "CityID": { "N": "3" },
             "Date": { "S": "2017-04-13" },
             "City": { "S": "Portland" },
             "State": { "S": "ME" },
             "Conditions": { "S": "Partly Sunny" },
             "Temperatures": { "M": {
                 "HighF": { "N": "54" },
                 "LowF": { "N": "37" }
               }
             }
           }
         }
       },
       {
         "PutRequest": {
           "Item": {
             "CityID": { "N": "3" },
             "Date": { "S": "2017-04-14" },
             "City": { "S": "Portland" },
             "State": { "S": "ME" },
             "Conditions": { "S": "Mostly Sunny" },
             "Temperatures": { "M": {
                 "HighF": { "N": "53" },
                 "LowF": { "N": "37" }
               }
             }
           }
         }
       }
     ]
   }
   ```

   In this code, 8 `Item` objects define the 8 items to add to the table, similar to the single item defined in the previous step\. However, when you run the DynamoDB** `batch-write-item` ** command in the next step, you must provide a JSON\-formatted object that includes each `Item` object in a containing `PutRequest` object\. Then you must include those `PutRequest` objects in a parent array that has the same name as the table\.

1. Run the DynamoDB** `batch-write-item` ** command, specifying the path to the JSON\-formatted items to add \(`--request-items`\)\.

   ```
   aws dynamodb batch-write-item \
   --request-items file://more-weather-items.json
   ```

   If the command succeeds, it displays the following message, confirming that the items were successfully added\.

   ```
   {
     "UnprocessedItems": {}
   }
   ```

1. To confirm the table's current contents, run the DynamoDB** `scan` ** command again\.

   ```
   aws dynamodb scan --table-name Weather
   ```

   If the command succeeds, 9 items are now displayed\.

## Step 5: Create a Global Secondary Index<a name="sample-dynamodb-create-index"></a>

Running the DynamoDB** `scan` ** command to get information about items can be slow, especially as a table grows in size or if the type of information you want to get is complex\. You can create one or more secondary indexes to speed things up and make getting information easier\. In this step, you learn about two types of secondary indexes that DynamoDB supports to do just that\. These are known as a *local secondary index* and a *global secondary index*\. Then you create a global secondary index\.

To understand these secondary index types, you first need to know about primary keys, which uniquely identify a table's items\. DynamoDB supports a *simple primary key* or a *composite primary key*\. A simple primary key has a single attribute, and that attribute value must be unique for each item in the table\. This attribute is also known as a *partition key* \(or a *hash attribute*\), which DynamoDB can use to partition items for faster access\. A table can also have a composite primary key, which contains two attributes\. The first attribute is the partition key, and the second is a *sort key* \(also known as a *range attribute*\)\. In a table with a composite primary key, any two items can have the same partition key value, but they cannot also have the same sort key value\. The `Weather` table has a composite primary key\.

A local secondary index has the same partition key as the table itself, but this index type can have a different sort key\. A global secondary index can have a partition key and a sort key that are both different from the table itself\.

For example, you can already use the primary key to access `Weather` items by `CityID`\. To access `Weather` items by `State`, you could create a local secondary index that has a partition key of `CityID` \(it must be the same as the table itself\) and a sort key of `State`\. To access `Weather` items by `City`, you could create a global secondary index that has a partition key of `City` and a sort key of `Date`\.

You can create local secondary indexes only while you are creating a table\. Because the `Weather` table already exists, you cannot add any local secondary indexes to it\. However, you can add global secondary indexes\. Practice adding one now\.

**Note**  
Creating secondary indexes might result in additional charges to your AWS account\.

1. Create a file named `weather-global-index.json` with the following content\.

   ```
   [
     {
       "Create": {
         "IndexName": "weather-global-index",
         "KeySchema": [
           {
             "AttributeName": "City",
             "KeyType": "HASH"
           },
           {
             "AttributeName": "Date",
             "KeyType": "RANGE"
           }
         ],
         "Projection": {
           "ProjectionType": "INCLUDE",
           "NonKeyAttributes": [
             "State",
             "Conditions",
             "Temperatures"
           ]
         },
         "ProvisionedThroughput": {
           "ReadCapacityUnits": 5,
           "WriteCapacityUnits": 5
         }
       }
     }
   ]
   ```

   In this code:
   + The name of the global secondary index is `weather-global-index`\.
   + The `City` attribute is the partition key \(hash attribute\), and the `Date` attribute is the sort key \(range attribute\)\.
   +  `Projection` defines the attributes to retrieve by default \(in addition to the hash attribute and any range attribute\) for every item matching a table search that uses this index\. In this sample, the `State`, `Conditions`, `HighF` \(part of `Temperatures`\), and `LowF` \(also part of `Temperatures`\) attributes \(as well as the `City` and `Date` attributes\) are retrieved for every matching item\.
   + Similar to tables, a global secondary index must define its provisioned throughput settings\.
   + The `IndexName`, `KeySchema`, `Projection`, and `ProvisionedThroughput` settings must be contained in a `Create` object, which defines the global secondary index to create when you run the DynamoDB** `update-table` ** command in the next step\.

1. Run the DynamoDB** `update-table` ** command\.

   ```
   aws dynamodb update-table \
   --table-name Weather \
   --attribute-definitions \
     AttributeName=City,AttributeType=S AttributeName=Date,AttributeType=S \
   --global-secondary-index-updates file://weather-global-index.json
   ```

   In this command:
   +  `--table-name` is the name of the table to update\.
   +  `--attribute-definitions` are the attributes to include in the index\. The partition key is always listed first, and any sort key is always listed second\.
   +  `--global-secondary-index-updates` is the path to the file that defines the global secondary index\.

   If this command succeeds, it displays summary information about the new global secondary index that is being created\. To confirm the global secondary index is successfully created, run the DynamoDB** `describe-table` ** command, specifying the table's name \(`--table-name`\)\.

   ```
   aws dynamodb describe-table --table-name Weather
   ```

   When the global secondary index is successfully created, the `TableStatus` value changes from `UPDATING` to `ACTIVE`, and the `IndexStatus` value changes from `CREATING` to `ACTIVE`\. Do not proceed past this step until the global secondary index is successfully created\. This can take several minutes\.

## Step 6: Get Items from the Table<a name="sample-dynamodb-get-items"></a>

There are many ways to get items from tables\. In this step, you get items by using the table's primary key, by using the table's other attributes, and by using the global secondary index\.

### To get a single item from a table based on the item's primary key value<a name="w14aac23c15c25b5"></a>

If you know an item's primary key value, you can get the matching item by running the DynamoDB command ** `get-item` **, ** `scan` **, or ** `query` **\. The following are the main differences in these commands:
+  ** `get-item` ** returns a set of attributes for the item with the given primary key\.
+  ** `scan` ** returns one or more items and item attributes by accessing every item in a table or a secondary index\.
+  ** `query` ** finds items based on primary key values\. You can query any table or secondary index that has a composite primary key \(a partition key and a sort key\)\.

In this sample, here's how to use each of these commands to get the item that contains the `CityID` attribute value of `1` and the `Date` attribute value of `2017-04-12`\.

1. To run the DynamoDB** `get-item` ** command, specify the name of the table \(`--table-name`\), the primary key value \(`--key`\), and the attribute values for the item to display \(`--projection-expression`\)\. Because `Date` is a reserved keyword in DynamoDB, you must also provide an alias for the `Date` attribute value \(`--expression-attribute-names`\)\. \(`State` is also a reserved keyword, and so you will see an alias provided for it in later steps\.\)

   ```
   aws dynamodb get-item \
   --table-name Weather \
   --key '{ "CityID": { "N": "1" }, "Date": { "S": "2017-04-12" } }' \
   --projection-expression \
     "City, #D, Conditions, Temperatures.HighF, Temperatures.LowF" \
   --expression-attribute-names '{ "#D": "Date" }'
   ```

   In this and the other commands, to display all of the item's attributes, don't include `--projection-expression`\. In this example, because you are not including `--projection-expression`, you also don't need to include `--expression-attribute-names`\.

   ```
   aws dynamodb get-item \
   --table-name Weather \
   --key '{ "CityID": { "N": "1" }, "Date": { "S": "2017-04-12" } }'
   ```

1. To run the DynamoDB** `scan` ** command, specify:
   + The name of the table \(`--table-name`\)\.
   + The search to run \(`--filter-expression`\)\.
   + The search criteria to use \(`--expression-attribute-values`\)\.
   + The kinds of attributes to display for the matching item \(`--select`\)\.
   + The attribute values for the item to display \(`--projection-expression`\)\.
   + If any of your attributes are using reserved keywords in DynamoDB, aliases for those attributes \(`--expression-attribute-names`\)\.

   ```
   aws dynamodb scan \
   --table-name Weather \
   --filter-expression "(CityID = :cityID) and (#D = :date)" \
   --expression-attribute-values \
     '{ ":cityID": { "N": "1" }, ":date": { "S": "2017-04-12" } }' \
   --select SPECIFIC_ATTRIBUTES \
   --projection-expression \
     "City, #D, Conditions, Temperatures.HighF, Temperatures.LowF" \
   --expression-attribute-names '{ "#D": "Date" }'
   ```

1. To run the DynamoDB** `query` ** command, specify:
   + The name of the table \(`--table-name`\)\.
   + The search to run \(`--key-condition-expression`\)\.
   + The attribute values to use in the search \(`--expression-attribute-values`\)\.
   + The kinds of attributes to display for the matching item \(`--select`\)\.
   + The attribute values for the item to display \(`--projection-expression`\)\.
   + If any of your attributes are using reserved keywords in DynamoDB, aliases for those attributes \(`--expression-attribute-names`\)\.

   ```
   aws dynamodb query \
   --table-name Weather \
   --key-condition-expression "(CityID = :cityID) and (#D = :date)" \
   --expression-attribute-values \
     '{ ":cityID": { "N": "1" }, ":date": { "S": "2017-04-12" } }' \
   --select SPECIFIC_ATTRIBUTES \
   --projection-expression \
     "City, #D, Conditions, Temperatures.HighF, Temperatures.LowF" \
   --expression-attribute-names '{ "#D": "Date" }'
   ```

   Notice that the ** `scan` ** command needed to scan all 9 items to get the result, while the ** `query` ** command only needed to scan for 1 item\.

### To get multiple items from a table based on the items' primary key values<a name="w14aac23c15c25b7"></a>

If you know the items' primary key values, you can get the matching items by running the DynamoDB** `batch-get-item` ** command\. In this sample, here's how to get the items that contain the `CityID` attribute value of `3` and `Date` attribute values of `2017-04-13` or `2017-04-14`\.

Run the DynamoDB** `batch-get-item` ** command, specifying the path to a file describing the items to get \(`--request-items`\)\.

```
aws dynamodb batch-get-item --request-items file://batch-get-item.json
```

For this sample, the code in the `batch-get-item.json` file specifies to search the `Weather` table for items with a `CityID` of `3` and a `Date` of `2017-04-13` or `2017-04-14`\. For each item found, the attribute values for `City`, `State`, `Date`, and `HighF` \(part of `Temperatures`\) are displayed, if they exist\.

```
{
  "Weather" : {
    "Keys": [
      {
        "CityID": { "N": "3" },
        "Date": { "S": "2017-04-13" }
      },
      {
        "CityID": { "N": "3" },
        "Date": { "S": "2017-04-14" }
      }
    ],
    "ProjectionExpression": "City, #S, #D, Temperatures.HighF",
    "ExpressionAttributeNames": { "#S": "State", "#D": "Date" }
  }
}
```

### To get all matching items from a table<a name="w14aac23c15c25b9"></a>

If you know something about the attributes' values in the table, you can get matching items by running the DynamoDB** `scan` ** command\. In this sample, here's how to get the dates when the `Conditions` attribute value contains `Sunny` and the `HighF` attribute value \(part of `Temperatures`\) is greater than `53`\.

Run the DynamoDB** `scan` ** command, specifying:
+ The name of the table \(`--table-name`\)\.
+ The search to run \(`--filter-expression`\)\.
+ The search criteria to use \(`--expression-attribute-values`\)\.
+ The kinds of attributes to display for the matching item \(`--select`\)\.
+ The attribute values for the item to display \(`--projection-expression`\)\.
+ If any of your attributes are using reserved keywords in DynamoDB, aliases for those attributes \(`--expression-attribute-names`\)\.

```
aws dynamodb scan \
--table-name Weather \
--filter-expression \
  "(contains (Conditions, :sun)) and (Temperatures.HighF > :h)" \
--expression-attribute-values \
  '{ ":sun": { "S" : "Sunny" }, ":h": { "N" : "53" } }' \
--select SPECIFIC_ATTRIBUTES \
--projection-expression "City, #S, #D, Conditions, Temperatures.HighF" \
--expression-attribute-names '{ "#S": "State", "#D": "Date" }'
```

### To get all matching items from a global secondary index<a name="w14aac23c15c25c11"></a>

To search using a global secondary index, use the DynamoDB** `query` ** command\. In this sample, here's how to use the `weather-global-index` secondary index to get the forecast conditions for cities named `Portland` for the dates of `2017-04-13` and `2017-04-14`\.

Run the DynamoDB** `query` ** command, specifying:
+ The name of the table \(`--table-name`\)\.
+ The name of the global secondary index \(`--index-name`\)\.
+ The search to run \(`--key-condition-expression`\)\.
+ The attribute values to use in the search \(`--expression-attribute-values`\)\.
+ The kinds of attributes to display for the matching item \(`--select`\)\.
+ If any of your attributes are using reserved keywords in DynamoDB, aliases for those attributes \(`--expression-attribute-names`\)\.

```
aws dynamodb query \
--table-name Weather \
--index-name weather-global-index \
--key-condition-expression "(City = :city) and (#D between :date1 and :date2)" \
--expression-attribute-values \
  '{ ":city": { "S" : "Portland" }, ":date1": { "S": "2017-04-13" }, ":date2": { "S": "2017-04-14" } }' \
--select SPECIFIC_ATTRIBUTES \
--projection-expression "City, #S, #D, Conditions, Temperatures.HighF" \
--expression-attribute-names '{ "#S": "State", "#D": "Date" }'
```

## Step 7: Clean Up<a name="sample-dynamodb-clean-up"></a>

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the table\. Deleting the table deletes the global secondary index as well\. You should also delete your environment\.

To delete the table, run the DynamoDB** `delete-table` ** command, specifying the table's name \(`--table-name`\)\.

```
aws dynamodb delete-table --table-name Weather
```

If the command succeeds, information about the table is displayed, including the `TableStatus` value of `DELETING`\.

To confirm the table is successfully deleted, run the DynamoDB** `describe-table` ** command, specifying the table's name \(`--table-name`\)\.

```
aws dynamodb describe-table --table-name Weather
```

If the table is successfully deleted, a message containing the phrase `Requested resource not found` is displayed\.

To delete your environment, see [Deleting an Environment](delete-environment.md)\.