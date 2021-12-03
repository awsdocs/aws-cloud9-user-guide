# Working with resources<a name="more-resources"></a>

In addition to accessing AWS services that are listed by default in the AWS Explorer, you can also go to **Resources** and choose from hundreds of resources to add to the interface\. In AWS, a **resource** is an entity you can work with\. Some of the resources that are added include Amazon AppFlow, Amazon Kinesis Data Streams, AWS IAM roles, Amazon VPC, and Amazon CloudFront distributions\.

To view available resources, go to **Resources** and expand the resource type to list the available resources for that type\. For example, if you select the `AWS::Lambda::Function` resource type, you can access the resources that define different functions, their properties, and their attributes\.

After adding a resource type to **Resources**, you can interact with it and its resources in the following ways:
+ View a list of existing resources that are available in the current AWS Region for this resource type\.
+ View a read\-only version of the JSON file that describes a resource\.
+ Copy the resource identifier for the resource\.
+ View the AWS documentation that explains the purpose of the resource type and the schema \(in JSON and YAML formats\) for modelling a resource\. 

## IAM permissions for accessing resources<a name="cloud-api-permissions"></a>

You require specific AWS Identity and Access Management permissions to access the resources associated with AWS services\. For example, an IAM entity, such as a user or a role, requires Lambda permissions to access `AWS::Lambda::Function` resources\. 

In addition to permissions for service resources, an IAM entity requires permissions to permit the AWS Toolkit to call AWS Cloud Control API operations on its behalf\. Cloud Control API operations allow the IAM user or role to access and update the remote resources\.

The easiest way to grant permissions is to attach the AWS managed policy, **PowerUserAccess**, to the IAM entity that's calling these API operations using the Toolkit interface\. This [managed policy](https://docs.aws.amazon.com/AM/latest/UserGuide/access_policies_job-functions.html#jf_developer-power-user) grants a range of permissions for performing application development tasks, including calling API operations\. 

For specific permissions that define allowable API operations on remote resources, see the [AWS Cloud Control API User Guide\.](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/security.html)

## Interacting with existing resources<a name="configure-resources"></a>

1. In the **AWS Explorer**, choose **Resources**\.

   A list of resource types is displayed under the **Resources** node\.

1. To access the documentation describing the syntax that defines the template for a resource type, right\-click that resource type and choose **View Documentation**\. 
**Note**  
You may be asked to switch off your browser's popup blocker so you can access the documentation page\.

1. To view the resources that already exist for a resource type, expand the entry for that type\.

   A list of available resources is displayed under their resource type\.

1. To interact with a specific resource, right\-click its name and choose one of the following options:
   + **Copy Identifier**: Copy the identifier for the specific resource to the clipboard\. \(For example, the `AWS::DynamoDB::Table` resource can be identified using the `TableName` property\.\) 
   + **Preview**: View a read\-only version of the JSON\-formatted template that describes the resource\.