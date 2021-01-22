# Configuration options for debugging serverless applications<a name="sam-debug-config-ref"></a>

With inline actions, you can easily find and define properties for invoking Lambda functions directly or with the SAM template\. You can also define properties for `"lambda"` \(how the function runs\), `"sam"` \(how the AWS SAM CLI builds the application\), and `"aws"` \(how AWS connection information is provided\)\. 


**AWS SAM: Direct Lambda handler invoke / Template\-based Lambda invoke**  

| Property | Description | 
| --- | --- | 
|  `type`  |  Specifies which extension manages the launch configuration\. Always set to `aws-sam` to use the AWS SAM CLI to build and debug locally\.  | 
|  `name`  |  Specifies a reader\-friendly name to appear in the **Debug launch configuration** list\.  | 
| `request` |  Specifies the type of configuration to be performed by the designated extension \(`aws-sam`\)\. Always set to `direct-invoke` to start the Lambda function\.  | 
|  `invokeTarget`  |  Specifies the entry point for invoking the resource\. For invoking the Lambda function directly, set values for the following `invokeTarget` fields:  [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/sam-debug-config-ref.html) For invoking the Lambda resources with the SAM template, set values for the following `invokeTarget` fields: [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/sam-debug-config-ref.html)  | 


**Lambda \(`"lambda"`\) properties**  

|  Property | Description | 
| --- | --- | 
|  `environmentVariables`  |  Passes operational parameters to your function\. For example, if you're writing to an Amazon S3 bucket, instead of hard\-coding the bucket name you're writing to, configure the bucket name as an environment variable\.   | 
| `payload` |  Describes in a JSON file format the event that triggers a Lambda function\. You can create an event payload by running the following command in the **Terminal** of the IDE: `sam local generate-event apigateway aws-proxy`  | 
|  `memoryMB`  |  Specifies megabytes of memory provided for running an invoked Lambda function\.  | 
| `runtime` |  Specifies the runtime used by the Lambda function\. For more information, see [AWS Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html)\.  | 
|  `timeoutSec`  |  Sets the time allowed, in seconds, before the debug session times out\.  | 

The AWS Toolkit extension uses the AWS SAM CLI to build and debug serverless applications locally\. You can configure the behavior of AWS SAM CLI commands using properties of the `"sam"` configuration in the `launch.json` file\.


**AWS SAM CLI \(`"sam"`\) properties**  

| Property |  Description  |  Default value  | 
| --- | --- | --- | 
|  `buildArguments`  | Configures how the `sam build` command builds your Lambda source code\. To view build options, see [sam build](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-build.html) in the *AWS Serverless Application Model Developer Guide*\. |  Empty string  | 
|  `containerBuild`  |  Indicates whether to build your function inside an AWS Lambda\-like Docker container\.   |  `false`  | 
|  `dockerNetwork`  |  Specifies the name or ID of an existing Docker network that the Lambda Docker containers should connect to, along with the default bridge network\. If not specified, the Lambda containers only connect to the default bridge Docker network\.   |  Empty string  | 
|  `localArguments`  |  Additional local invoke arguments\.  |  Empty string  | 
|  `skipNewImageCheck`  |  Specifies whether the command should skip pulling down the latest Docker image for Lambda runtime\.   |  `false`  | 
|  `template`  |  Customizes your SAM template by using parameters to input customer values to it\. For more information, see [Parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html) in the *AWS CloudFormation User Guide*\.  |  `"parameters":{}`  | 


**AWS connection \(`"aws"`\) properties**  

| Property | Description | Default value | 
| --- | --- | --- | 
| `credentials` |  Selects a specific profile \(for example, `profile:default`\) from your credential file to get AWS credentials\.   | The AWS credentials provided by your existing shared AWS config file or shared AWS credentials file\. | 
| `region` |  Sets the AWS Region of the service \(for example, us\-east\-1\)\.  | The default AWS Region associated with the active credentials profile\.  | 