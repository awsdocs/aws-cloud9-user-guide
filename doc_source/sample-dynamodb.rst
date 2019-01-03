.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _sample-dynamodb:

##############################
|DDBlong| Sample for |AC9long|
##############################

.. meta::
    :description:
        Provides a hands-on sample that you can use to experiment with Amazon DynamoDB in AWS Cloud9.

This sample enables you to set up an |envfirst| to work with |DDBlong|.

|DDB| is a fully managed NoSQL database service.
You can use |DDB| to create a database table that can store and retrieve any amount of data, and serve any level of request traffic.
|DDB| automatically spreads the data and traffic for the table over a sufficient number of servers to handle the request capacity
specified and the amount of data stored, while maintaining consistent and fast performance. For more information, see
`Amazon DynamoDB <https://aws.amazon.com/dynamodb/>`_ on the AWS website.

Creating this sample might result in charges to your AWS account. These include possible charges for services such as |EC2| and |DDB|. For more information, see
`Amazon EC2 Pricing <https://aws.amazon.com/ec2/pricing/>`_ and `Amazon DynamoDB Pricing <https://aws.amazon.com/dynamodb/pricing/>`_.

For information about additional AWS database offerings, see `Amazon Relational Database Service (RDS) <https://aws.amazon.com/rds/>`_,
`Amazon ElastiCache <https://aws.amazon.com/elasticache/>`_, and `Amazon Redshift <https://aws.amazon.com/redshift/>`_ on the AWS website. See also
`AWS Database Migration Service <https://aws.amazon.com/dms/>`_ on the AWS website.

* :ref:`sample-dynamodb-prereqs`
* :ref:`sample-dynamodb-cli-setup`
* :ref:`sample-dynamodb-create-table`
* :ref:`sample-dynamodb-add-item`
* :ref:`sample-dynamodb-add-items`
* :ref:`sample-dynamodb-create-index`
* :ref:`sample-dynamodb-get-items`
* :ref:`sample-dynamodb-clean-up`

.. _sample-dynamodb-prereqs:

Prerequisites
=============

.. include:: _sample-prereqs.txt

.. _sample-dynamodb-cli-setup:

Step 1: Install and Configure the |cli|, the aws-shell, or Both in Your |envtitle|
==================================================================================

In this step, you use the |AC9IDE| to install and configure the |cli|, the aws-shell, or both in your |env| so you can run commands
to interact with |DDB|. Then you use the |cli| to run a basic |DDB| command to test your installation and configuration.

#. To set up credentials management for the |cli| or the aws-shell and to install the |cli|, the aws-shell, or both in your |env|, follow Steps 1 and 2 in the :doc:`AWS CLI and aws-shell Sample <sample-aws-cli>`, and then return to this topic.
   If you already installed and configured the |cli|, the aws-shell, or both in your |env|, you don't need to do it again.
#. Test the installation and configuration of the |cli|, the aws-shell, or both by running the |DDB| :command:`list-tables` command from a terminal session in your |env| to list your existing |DDB| tables, if there are any.
   To start a new terminal session, on the menu bar, choose :menuselection:`Windows, New Terminal`.

   .. code-block:: sh

      aws dynamodb list-tables # For the AWS CLI.
      dynamodb list-tables     # For the aws-shell.

   .. note:: Throughout this sample, if you're using the aws-shell, omit :code:`aws` from each command that starts with :code:`aws`. To start the aws-shell, run the :command:`aws-shell` command. To 
      stop using the aws-shell, run the :command:`.exit` or :command:`.quit` command.

   If this command succeeds, it outputs a :code:`TableNames` array containing a list of existing
   |DDB|
   tables that you might already have. If you have no |DDB| tables yet, the
   :code:`TableNames` array will be empty.

   .. code-block:: sh

      {
        "TableNames": []
      }

   If you do have any |DDB| tables, the :code:`TableNames` array contains a list of the table names.

.. _sample-dynamodb-create-table:

Step 2: Create a Table
======================

In this step, you create a table in |DDB| and specify the table's name, layout, simple primary key,
and data throughput settings.

This sample table, named :code:`Weather`, contains information about weather forecasts for a few cities
in the United States. The table holds the following types of information
(in |DDB|, each piece of information is known as an *attribute*):

* Required unique city ID (:code:`CityID`)
* Required forecast date (:code:`Date`)
* City name (:code:`City`)
* State name (:code:`State`)
* Forecast weather conditions (:code:`Conditions`)
* Forecast temperatures (:code:`Temperatures`)

  * Forecast high, in degrees Fahrenheit (:code:`HighF`)
  * Forecast low, in degrees Fahrenheit (:code:`LowF`)

To create the table, in a terminal session in the |AC9IDE|, run the |DDB| :command:`create-table` command.

.. code-block:: sh

   aws dynamodb create-table \
   --table-name Weather \
   --attribute-definitions \
     AttributeName=CityID,AttributeType=N AttributeName=Date,AttributeType=S \
   --key-schema \
     AttributeName=CityID,KeyType=HASH AttributeName=Date,KeyType=RANGE \
   --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5

In this command:

* :code:`--table-name` represents the table name (:code:`Weather` in this sample). Table names must be unique within each AWS Region in your AWS account.
* :code:`--attribute-definitions` represents the attributes that are used to uniquely identify the table
  items. Each of this table's items
  are uniquely identified by a combination of a numerical :code:`ID` attribute and a :code:`Date` attribute
  represented as an ISO-8601 formatted string.
* :code:`--key-schema` represents the table's key schema. This table has a composite primary key of :code:`CityID`
  and :code:`Date`.
  This means that each of the table items must have a :code:`CityID` attribute value and a :code:`Date` attribute value, but no two items in the table can have both the
  same :code:`CityID` attribute value and :code:`Date` attribute value.
* :code:`--provisioned-throughput` represents the table's read-write capacity. |DDB| allows up to 5
  strongly consistent reads per second for
  items up to 4 KB in size, or up to 5 eventually consistent reads per second for items up to 4 KB
  in size. |DDB| also allows up to 5 writes per second
  for items up to 1 KB in size.

  .. note:: Setting higher provisioned throughput might result in additional charges to your AWS account.

     For more information about this and other |DDB| commands, see :dynamodb-cli-ref:`dynamodb <index.html>` in the |cli-ref|.

If this command succeeds, it displays summary information about the new table that is being created.
To
confirm the table is
successfully created, run the |DDB| :command:`describe-table` command, specifying the table's name (:code:`--table-name`).

.. code-block:: sh

   aws dynamodb describe-table --table-name Weather

When the table is successfully created, the :code:`TableStatus` value changes from :code:`CREATING` to
:code:`ACTIVE`. Do not proceed past
this step until the table is successfully created.

.. _sample-dynamodb-add-item:

Step 3: Add an Item to the Table
================================

In this step, you add an item to the table you just created.

#. Create a file named :file:`weather-item.json` with the following content. To create a new file, on the menu bar, choose :menuselection:`File, New File`. To
   save the file, choose :menuselection:`File, Save`.

   .. code-block:: json

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

   In this code, :code:`N` represents an attribute value that is a number. :code:`S` is a string attribute value. :code:`M` is a map attribute, which is a set of attribute-value pairs.
   You must specify an attribute's data type whenever you work with items. For additional available attribute data types, see
   :dynamodb-dev-guide:`Data Types <HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes>` in the |DDB-dg|.

#. Run the |DDB| :command:`put-item` command, specifying the table's name (:code:`--table-name`) and the path to the JSON-formatted item (:code:`--item`).

   .. code-block:: sh

      aws dynamodb put-item \
      --table-name Weather \
      --item file://weather-item.json

   If the command succeeds, it runs without error, and no confirmation message is displayed.

#. To confirm the table's current contents, run the |DDB| :command:`scan` command, specifying the table's name (:code:`--table-name`).

   .. code-block:: sh

      aws dynamodb scan --table-name Weather

   If the command succeeds, summary information about the table and the item you just added is
   displayed.

.. _sample-dynamodb-add-items:

Step 4: Add Multiple Items to the Table
=======================================

In this step, you add several more items to the :code:`Customers` table.

#. Create a file named :file:`more-weather-items.json` with the following content.

   .. code-block:: json

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

   In this code, 8 :code:`Item` objects define the 8 items to add to the table, similar to
   the single item defined in the previous step. However, when you run the
   |DDB| :command:`batch-write-item` command in the next step, you must provide a JSON-formatted object that includes each :code:`Item` object in a containing
   :code:`PutRequest` object. Then you must include those :code:`PutRequest` objects in a parent array that has the same name as the table.

#. Run the |DDB| :command:`batch-write-item` command, specifying the path to the JSON-formatted items to add (:code:`--request-items`).

   .. code-block:: sh

      aws dynamodb batch-write-item \
      --request-items file://more-weather-items.json

   If the command succeeds, it displays the following message, confirming that the items were
   successfully added.

   .. code-block:: sh

      {
        "UnprocessedItems": {}
      }

#. To confirm the table's current contents, run the |DDB| :command:`scan` command again.

   .. code-block:: sh

      aws dynamodb scan --table-name Weather

   If the command succeeds, 9 items are now displayed.

.. _sample-dynamodb-create-index:

Step 5: Create a Global Secondary Index
=======================================

Running the |DDB| :command:`scan` command to get information about items can be slow, especially as a
table grows in size or if the type of information you want to get is complex.
You can create one or more secondary indexes to speed things up and make getting information easier. In
this step, you learn about two types of secondary indexes that |DDB| supports to do just that. These are
known as a *local secondary index*
and a *global secondary index*. Then you create a global secondary index.

To understand these secondary index types, you first need to know about primary keys, which uniquely identify a table's items. |DDB| supports a *simple primary key* or
a *composite primary key*. A simple primary key has a single attribute, and that attribute value must be unique for each item in the table.
This attribute is also known as a *partition key* (or a *hash attribute*), which |DDB| can use to partition items for faster access. A table can
also have a composite primary key, which contains two attributes. The first attribute is the partition key, and the second is a *sort key* (also known as a
*range attribute*). In a table with a composite
primary key, any two items can have the same partition key value, but they cannot also have the same sort key value. The :code:`Weather` table has a composite primary key.

A local secondary index has the same partition key as the table itself, but this index type can have a different sort key. A global secondary index can have a partition key and
a sort key that are both different from the table itself.

For example, you can already use the primary key to access :code:`Weather` items by :code:`CityID`. To access :code:`Weather` items by :code:`State`,
you could create a local secondary index that has a partition key of :code:`CityID` (it must be the same as the
table itself) and a sort key of :code:`State`. To access :code:`Weather` items by :code:`City`, you could create a global secondary index that has a
partition key of :code:`City` and a sort key of :code:`Date`.

You can create local secondary indexes only while you are creating a table. Because the :code:`Weather`
table already exists, you cannot add any local secondary indexes to it.
However, you can add global secondary indexes. Practice adding one now.

.. note:: Creating secondary indexes might result in additional charges to your AWS account.

#. Create a file named :file:`weather-global-index.json` with the following content.

   .. code-block:: json

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

   In this code:

   * The name of the global secondary index is :code:`weather-global-index`.
   * The :code:`City` attribute is the partition key (hash attribute), and the :code:`Date` attribute
     is the sort key (range attribute).
   * :code:`Projection` defines the attributes to retrieve by default (in addition to the hash attribute and any range attribute) for every item matching a table search that uses this index.
     In this sample, the :code:`State`, :code:`Conditions`, :code:`HighF` (part of :code:`Temperatures`), and :code:`LowF` (also part of :code:`Temperatures`) attributes
     (as well as the :code:`City` and :code:`Date` attributes) are retrieved for every matching item.
   * Similar to tables, a global secondary index must define its provisioned throughput settings.
   * The :code:`IndexName`, :code:`KeySchema`, :code:`Projection`, and :code:`ProvisionedThroughput` settings must be contained in a :code:`Create` object, which defines the global secondary
     index to create when you run the |DDB| :command:`update-table` command in the next step.

#. Run the |DDB| :command:`update-table` command.

   .. code-block:: sh

      aws dynamodb update-table \
      --table-name Weather \
      --attribute-definitions \
        AttributeName=City,AttributeType=S AttributeName=Date,AttributeType=S \
      --global-secondary-index-updates file://weather-global-index.json

   In this command:

   * :code:`--table-name` is the name of the table to update.
   * :code:`--attribute-definitions` are the attributes to include in the index. The partition key is always listed first, and any sort key is always listed second.
   * :code:`--global-secondary-index-updates` is the path to the file that defines the global secondary index.

   If this command succeeds, it displays summary information about the new global secondary index that
   is being created. To confirm the global secondary index is
   successfully created, run the |DDB| :command:`describe-table` command, specifying the table's name (:code:`--table-name`).

   .. code-block:: sh

      aws dynamodb describe-table --table-name Weather

   When the global secondary index is successfully created, the :code:`TableStatus` value changes from
   :code:`UPDATING` to :code:`ACTIVE`, and the :code:`IndexStatus`
   value changes from :code:`CREATING` to :code:`ACTIVE`. Do not proceed past this step until the global
   secondary index is successfully created. This can take several minutes.

.. _sample-dynamodb-get-items:

Step 6: Get Items from the Table
================================

There are many ways to get items from tables. In this step, you get items by using the table's primary key, by using the table's other attributes, and by using the global secondary index.

.. topic:: To get a single item from a table based on the item's primary key value

   If you know an item's primary key value, you can get the matching item by running the |DDB| command
   :command:`get-item`, :command:`scan`, or :command:`query`. The following are the main differences in
   these commands:

   * :command:`get-item` returns a set of attributes for the item with the given primary key.
   * :command:`scan` returns one or more items and item attributes by accessing every item in a table or a secondary index.
   * :command:`query` finds items based on primary key values. You can query any table or secondary index that has a composite primary key (a partition key and a sort key).

   In this sample, here's how
   to use each of these commands to get the item that contains the :code:`CityID` attribute value of :code:`1` and the :code:`Date` attribute value of :code:`2017-04-12`.

   #. To run the |DDB| :command:`get-item` command, specify the name of the table (:code:`--table-name`), the primary key value (:code:`--key`),
      and the attribute values for the item to display (:code:`--projection-expression`). Because :code:`Date` is a reserved keyword in |DDB|, you must also
      provide an alias for the :code:`Date` attribute value (:code:`--expression-attribute-names`). (:code:`State` is also a reserved keyword, and so you will see an alias
      provided for it in later steps.)

      .. code-block:: sh

         aws dynamodb get-item \
         --table-name Weather \
         --key '{ "CityID": { "N": "1" }, "Date": { "S": "2017-04-12" } }' \
         --projection-expression \
           "City, #D, Conditions, Temperatures.HighF, Temperatures.LowF" \
         --expression-attribute-names '{ "#D": "Date" }'

      In this and the other commands, to display all of the item's attributes, don't include :code:`--projection-expression`.
      In this example, because
      you are not including :code:`--projection-expression`, you also don't need to include :code:`--expression-attribute-names`.

      .. code-block:: sh

         aws dynamodb get-item \
         --table-name Weather \
         --key '{ "CityID": { "N": "1" }, "Date": { "S": "2017-04-12" } }'

   #. To run the |DDB| :command:`scan` command, specify:

      * The name of the table (:code:`--table-name`).
      * The search to run (:code:`--filter-expression`).
      * The search criteria to use (:code:`--expression-attribute-values`).
      * The kinds of attributes to display for the matching item (:code:`--select`).
      * The attribute values for the item to display (:code:`--projection-expression`).
      * If any of your attributes are using reserved keywords in |DDB|, aliases for those attributes (:code:`--expression-attribute-names`).

      .. code-block:: sh

         aws dynamodb scan \
         --table-name Weather \
         --filter-expression "(CityID = :cityID) and (#D = :date)" \
         --expression-attribute-values \
           '{ ":cityID": { "N": "1" }, ":date": { "S": "2017-04-12" } }' \
         --select SPECIFIC_ATTRIBUTES \
         --projection-expression \
           "City, #D, Conditions, Temperatures.HighF, Temperatures.LowF" \
         --expression-attribute-names '{ "#D": "Date" }'

   #. To run the |DDB| :command:`query` command, specify:

      * The name of the table (:code:`--table-name`).
      * The search to run (:code:`--key-condition-expression`).
      * The attribute values to use in the search (:code:`--expression-attribute-values`).
      * The kinds of attributes to display for the matching item (:code:`--select`).
      * The attribute values for the item to display (:code:`--projection-expression`).
      * If any of your attributes are using reserved keywords in |DDB|, aliases for those attributes (:code:`--expression-attribute-names`).

      .. code-block:: sh

         aws dynamodb query \
         --table-name Weather \
         --key-condition-expression "(CityID = :cityID) and (#D = :date)" \
         --expression-attribute-values \
           '{ ":cityID": { "N": "1" }, ":date": { "S": "2017-04-12" } }' \
         --select SPECIFIC_ATTRIBUTES \
         --projection-expression \
           "City, #D, Conditions, Temperatures.HighF, Temperatures.LowF" \
         --expression-attribute-names '{ "#D": "Date" }'

      Notice that the :command:`scan` command needed to scan all 9 items to get the result, while the
      :command:`query` command only needed to scan for 1 item.

.. topic:: To get multiple items from a table based on the items' primary key values

   If you know the items' primary key values, you can get the matching items by running the |DDB| :command:`batch-get-item` command. In this sample, here's how
   to get the items that contain the :code:`CityID` attribute value of :code:`3` and :code:`Date` attribute values of :code:`2017-04-13` or :code:`2017-04-14`.

   Run the |DDB| :command:`batch-get-item` command, specifying the path to a file describing the items to get (:code:`--request-items`).

   .. code-block:: sh

      aws dynamodb batch-get-item --request-items file://batch-get-item.json

   For this sample, the code in the :file:`batch-get-item.json` file specifies to search the :code:`Weather` table for items with a :code:`CityID` of :code:`3` and
   a :code:`Date` of :code:`2017-04-13` or :code:`2017-04-14`. For each item found, the
   attribute values for :code:`City`, :code:`State`, :code:`Date`, and :code:`HighF` (part of :code:`Temperatures`) are displayed, if they exist.

   .. code-block:: json

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

.. topic:: To get all matching items from a table

   If you know something about the attributes' values in the table, you can get matching items by running the |DDB| :command:`scan` command. In this sample, here's how
   to get the dates when the :code:`Conditions` attribute value contains :code:`Sunny` and the :code:`HighF` attribute value (part of :code:`Temperatures`) is greater than :code:`53`.

   Run the |DDB| :command:`scan` command, specifying:

   * The name of the table (:code:`--table-name`).
   * The search to run (:code:`--filter-expression`).
   * The search criteria to use (:code:`--expression-attribute-values`).
   * The kinds of attributes to display for the matching item (:code:`--select`).
   * The attribute values for the item to display (:code:`--projection-expression`).
   * If any of your attributes are using reserved keywords in |DDB|, aliases for those attributes (:code:`--expression-attribute-names`).

   .. code-block:: sh

      aws dynamodb scan \
      --table-name Weather \
      --filter-expression \
        "(contains (Conditions, :sun)) and (Temperatures.HighF > :h)" \
      --expression-attribute-values \
        '{ ":sun": { "S" : "Sunny" }, ":h": { "N" : "53" } }' \
      --select SPECIFIC_ATTRIBUTES \
      --projection-expression "City, #S, #D, Conditions, Temperatures.HighF" \
      --expression-attribute-names '{ "#S": "State", "#D": "Date" }'

.. topic:: To get all matching items from a global secondary index

   To search using a global secondary index, use the |DDB| :command:`query` command. In this sample, here's how
   to use the :code:`weather-global-index` secondary index to get the forecast conditions for cities named :code:`Portland` for the
   dates of :code:`2017-04-13` and :code:`2017-04-14`.

   Run the |DDB| :command:`query` command, specifying:

   * The name of the table (:code:`--table-name`).
   * The name of the global secondary index (:code:`--index-name`).
   * The search to run (:code:`--key-condition-expression`).
   * The attribute values to use in the search (:code:`--expression-attribute-values`).
   * The kinds of attributes to display for the matching item (:code:`--select`).
   * If any of your attributes are using reserved keywords in |DDB|, aliases for those attributes (:code:`--expression-attribute-names`).

   .. code-block:: sh

      aws dynamodb query \
      --table-name Weather \
      --index-name weather-global-index \
      --key-condition-expression "(City = :city) and (#D between :date1 and :date2)" \
      --expression-attribute-values \
        '{ ":city": { "S" : "Portland" }, ":date1": { "S": "2017-04-13" }, ":date2": { "S": "2017-04-14" } }' \
      --select SPECIFIC_ATTRIBUTES \
      --projection-expression "City, #S, #D, Conditions, Temperatures.HighF" \
      --expression-attribute-names '{ "#S": "State", "#D": "Date" }'

.. _sample-dynamodb-clean-up:

Step 7: Clean Up
================

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the table. Deleting the table deletes the global secondary index as well.
You should also delete your |env|.

To delete the table, run the |DDB| :command:`delete-table` command, specifying the table's name (:code:`--table-name`).

.. code-block:: sh

   aws dynamodb delete-table --table-name Weather

If the command succeeds, information about the table is displayed, including the :code:`TableStatus` value
of :code:`DELETING`.

To confirm the table is successfully deleted, run the |DDB| :command:`describe-table` command, specifying
the
table's name (:code:`--table-name`).

.. code-block:: sh

   aws dynamodb describe-table --table-name Weather

If the table is successfully deleted, a message containing the phrase :code:`Requested resource not found`
is displayed.

To delete your |env|, see :doc:`Deleting an Environment <delete-environment>`.