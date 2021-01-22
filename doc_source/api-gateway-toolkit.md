# Working with API Gateway using the AWS Toolkit<a name="api-gateway-toolkit"></a>

API Gateway enables you to create RESTful APIs and WebSocket APIs that enable real\-time two\-way communication applications\. For more information on creating and managing APIs with API Gateway, see the [https://docs.aws.amazon.com/apigateway/latest/developerguide/](https://docs.aws.amazon.com/apigateway/latest/developerguide/)\.

With the AWS Toolkit, you can configure a call to a REST API by specifying the REST resource, method type, and data that's passed in as input\.

## Invoking REST APIs in API Gateway<a name="api-gateway-toolkit-invoke"></a>

**Important**  
Calling API methods using the AWS Toolkit may result in changes to resources that can't be undone\. For example, if you call a `POST` method, the API's resources are updated if the call is successful\. 

You can invoke an API Gateway on AWS from the AWS Toolkit\.

## To invoke a REST API

1. In the **AWS Explorer** window, choose the API Gateway node to view the list of REST APIs available in the current AWS Region\.

1. Right\-click a REST API, and then choose **Invoke on AWS**\.
**Note**  
The context menu also allows to copy the REST API's URL, name, and Amazon Resource Name \(ARN\)\. 

   The **Invoke methods** window displays, enabling you to configure the call to the API\.

1. For **Select a resource**, choose the REST resource you want to interact with\.

1. For **Select a method**, choose one of the following method types:
   + **GET**: Gets a resource from the backend service that's accessed through the API\.
   + **OPTIONS**: Requests information about the methods and operations that are supported by the API Gateway\.
   + **POST**: Creates a new resource on the backend service that's accessed through the API\.

1. To supply input to your API method call, you can use a query string or JSON\-formatted payload:
   + **Query string**: Enter a query string using the format `parameter1=value1&parameter2=value2`\. \(Before you use query strings, create a [mapping template](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html) to transform incoming web requests before they're sent to the integration back end\.\)
   + JSON format: You can define a JSON\-formatted payload in the large text field in **Invoke methods** window\.

     For example, you can add a new resource with a `POST` method that contains the following payload:

     ```
     {"type": "soda", "price" : 3.99}       
     ```

1. Choose the **Invoke** button to call the REST API resource\.

   The REST API response is displayed in the **AWS Remote Invocations** tab\. The response body contains the JSON\-formatted resource data \.