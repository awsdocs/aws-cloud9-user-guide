# AWS CDK sample for AWS Cloud9<a name="sample-cdk"></a>

This sample shows you how to work with the AWS Cloud Development Kit \(CDK\) in an AWS Cloud9 development environment\. The AWS CDK is a set of software tools and libraries that developers can use to model AWS infrastructure components as code\.

The AWS CDK includes the AWS Construct Library that you can use to quickly resolve many tasks on AWS\. For example, you can use the `Fleet` construct to fully and securely deploy code to a fleet of hosts\. You can create your own constructs to model various elements of your architectures, share them with others, or publish them to the community\. For more information, see the [AWS Cloud Development Kit Developer Guide](https://docs.aws.amazon.com/cdk/latest/guide/)\.

Creating this sample might result in charges to your AWS account\. These include possible charges for services such as Amazon EC2, Amazon SNS, and Amazon SQS\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/), [Amazon SNS Pricing](https://aws.amazon.com/sns/pricing/), and [Amazon SQS Pricing](https://aws.amazon.com/sqs/pricing/)\.

**Topics**
+ [Prerequisites](#sample-cdk-prereqs)
+ [Step 1: Install required tools](#sample-cdk-install)
+ [Step 2: Add code](#sample-cdk-code)
+ [Step 3: Run the code](#sample-cdk-run)
+ [Step 4: Clean up](#sample-cdk-clean-up)

## Prerequisites<a name="sample-cdk-prereqs"></a>

Before you use this sample, be sure to meet the following requirements\.
+  **You must have an existing AWS Cloud9 EC2 development environment\.** This sample assumes you already have an EC2 environment that is connected to an Amazon EC2 instance running Amazon Linux or Ubuntu Server\. If you have a different type of environment or operating system, you might need to adapt this sample's instructions to set up related tools\. See [Creating an environment in AWS Cloud9](create-environment.md) for details\.
+  **You have the AWS Cloud9 IDE for the existing environment already open\.** When you open an environment, AWS Cloud9 opens the IDE for that environment in your web browser\. See [Opening an environment in AWS Cloud9](open-environment.md) for details\.

## Step 1: Install required tools<a name="sample-cdk-install"></a>

In this step, you install all of the tools in your environment that the AWS CDK needs to run a sample that is written in the TypeScript programming language\.

1.  [Node Version Manager](#sample-cdk-install-nvm), or ** `nvm` **, which you use to install Node\.js later\.

1.  [Node\.js](#sample-cdk-install-nodejs), which is required by the sample and contains Node Package Manager, or ** `npm` **, which you use to install TypeScript and the AWS CDK later\.

1.  [TypeScript](#sample-cdk-install-typescript), which is required by this sample\. \(The AWS CDK also provides support for several other programming languages\.\)

1. The [AWS CDK](#sample-cdk-install-cdk)\.

### Step 1\.1: Install Node Version Manager \(nvm\)<a name="sample-cdk-install-nvm"></a>

1. In a terminal session in the AWS Cloud9 IDE, ensure the latest security updates and bug fixes are installed\. To do this, run the ** `yum update` ** \(for Amazon Linux\) or ** `apt update` ** command \(for Ubuntu Server\)\. \(To start a new terminal session, on the menu bar, choose **Window**, **New Terminal**\.\)

   For Amazon Linux:

   ```
   sudo yum -y update
   ```

   For Ubuntu Server:

   ```
   sudo apt update
   ```

1. Confirm whether ** `nvm` ** is already installed\. To do this, run the ** `nvm` ** command with the ** `--version` ** option\.

   ```
   nvm --version
   ```

   If successful, the output contains the ** `nvm` ** version number, and you can skip ahead to [Step 1\.2: Install Node\.js](#sample-cdk-install-nodejs)\.

1. Download and install ** `nvm` **\. To do this, run the install script\. In this example, v0\.33\.0 is installed, but you can check for the latest version of ** `nvm` ** [here](https://github.com/nvm-sh/nvm#installing-and-updating)\.

   ```
   curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash
   ```

1. Start using ** `nvm` **\. You can either close the terminal session and then restart it, or source the `~/.bashrc` file that contains the commands to load ** `nvm` **\.

   ```
   . ~/.bashrc
   ```

### Step 1\.2: Install Node\.js<a name="sample-cdk-install-nodejs"></a>

1. Confirm whether you already have Node\.js installed, and if you do, confirm that the installed version is 10\.3\.0 or greater\. **This sample has been tested with Node\.js 10\.3\.0\.** To check, with the terminal session still open in the IDE, run the ** `node` ** command with the ** `--version` ** option\.

   ```
   node --version
   ```

   If you do have Node\.js installed, the output contains the version number\. If the version number is v10\.3\.0, skip ahead to [Step 1\.3: Install TypeScript](#sample-cdk-install-typescript)\.

1. Install Node\.js 10\.3\.0 by running the ** `nvm` ** command with the ** `install` ** action\.
**Note**  
You can also run **`nvm install stable`** to install the long\-term support \(LTS\) version of Node\.js\. AWS Cloud9 support tracks the LTS version of Node\.js\. 

   ```
   nvm install v10.3.0
   ```

1. Start using Node\.js 10\.3\.0\. To do this, run the ** `nvm` ** command with the ** `alias` ** action, the version number to alias, and the version to use for that alias, as follows\.

   ```
   nvm alias default 10.3.0
   ```
**Note**  
The preceding command sets Node\.js 10\.3\.0 as the default version of Node\.js\. Alternatively, you can run the ** `nvm` ** command along with the ** `use` ** action instead of the ** `alias` ** action \(for example, ** `nvm use 10.3.0` **\)\. However, the ** `use` ** action causes that version of Node\.js to run only while the current terminal session is running\.

1. To confirm that you're using Node\.js 10\.3\.0, run the ** `node --version` ** command again\. If the correct version is installed, the output contains version v10\.3\.0\.

### Step 1\.3: Install TypeScript<a name="sample-cdk-install-typescript"></a>

1. Confirm whether you already have TypeScript installed\. To do this, with the terminal session still open in the IDE, run the command line TypeScript compiler with the ** `--version` ** option\.

   ```
   tsc --version
   ```

   If you do have TypeScript installed, the output contains the TypeScript version number\. If TypeScript is installed, skip ahead to [Step 1\.4: Install the AWS CDK](#sample-cdk-install-cdk)\.

1. Install TypeScript\. To do this, run the ** `npm` ** command with the ** `install` ** action, the ** `-g` ** option, and the name of the TypeScript package\. This installs TypeScript as a global package in the environment\.

   ```
   npm install -g typescript
   ```

1. Confirm that TypeScript is installed\. To do this, run the command line TypeScript compiler with the ** `--version` ** option\.

   ```
   tsc --version
   ```

   If TypeScript is installed, the output contains the TypeScript version number\.

### Step 1\.4: Install the AWS CDK<a name="sample-cdk-install-cdk"></a>

1. Confirm whether you already have the AWS CDK installed\. To do this, with the terminal session still open in the IDE, run the ** `cdk` ** command with the ** `--version` ** option\.

   ```
   cdk --version
   ```

   If the AWS CDK is installed, the output contains the AWS CDK version and build numbers\. Skip ahead to [Step 2: Add code](#sample-cdk-code)\.

1. Install the AWS CDK by running the ** `npm` ** command along with the `install` action, the name of the AWS CDK package to install, and the `-g` option to install the package globally in the environment\.

   ```
   npm install -g aws-cdk
   ```

1. Confirm that the AWS CDK is installed and correctly referenced\. To do this, run the ** `cdk` ** command with the ** `--version` ** option\.

   ```
   cdk --version
   ```

   If successful, the AWS CDK version and build numbers are displayed\.

## Step 2: Add code<a name="sample-cdk-code"></a>

In this step, you create a sample TypeScript project that contains all of the source code you need for the AWS CDK to programmatically deploy an AWS CloudFormation stack\. This stack creates an Amazon SNS topic and an Amazon SQS queue in your AWS account and then subscribes the queue to the topic\.

1. With the terminal session still open in the IDE, create a directory to store the project's source code, for example a `~/environment/hello-cdk` directory in your environment\. Then switch to that directory\.

   ```
   rm -rf ~/environment/hello-cdk # Remove this directory if it already exists.
   mkdir ~/environment/hello-cdk  # Create the directory.
   cd ~/environment/hello-cdk     # Switch to the directory.
   ```

1. Set up the directory as a TypeScript language project for the AWS CDK\. To do this, run the ** `cdk` ** command with the ** `init` ** action, the ** `sample-app` ** template, and the ** `--language` ** option along with the name of the programming language\.

   ```
   cdk init sample-app --language typescript
   ```

   This creates the following files and subdirectories in the directory\.
   + A hidden `.git` subdirectory and a hidden `.gitignore` file, which makes the project compatible with source control tools such as Git\.
   + A `lib` subdirectory, which includes a `hello-cdk-stack.ts` file\. This file contains the code for your AWS CDK stack\. This code is described in the next step in this procedure\.
   + A `bin` subdirectory, which includes a `hello-cdk.ts` file\. This file contains the entry point for your AWS CDK app\.
   + A `node_modules` subdirectory, which contains supporting code packages that the app and stack can use as needed\.
   + A hidden `.npmignore` file, which lists the types of subdirectories and files that ** `npm` ** doesn't need when it builds the code\.
   + A `cdk.json` file, which contains information to make running the ** `cdk` ** command easier\.
   + A `package-lock.json` file, which contains information that ** `npm` ** can use to reduce possible build and run errors\.
   + A `package.json` file, which contains information to make running the ** `npm` ** command easier and with possibly fewer build and run errors\.
   + A `README.md` file, which lists useful commands you can run with ** `npm` ** and the AWS CDK\.
   + A `tsconfig.json` file, which contains information to make running the ** `tsc` ** command easier and with possibly fewer build and run errors\.

1. In the **Environment** window, open the `lib/hello-cdk-stack.ts` file, and browse the following code in that file\.

   ```
   import sns = require('@aws-cdk/aws-sns');
   import sqs = require('@aws-cdk/aws-sqs');
   import cdk = require('@aws-cdk/cdk');
   
   export class HelloCdkStack extends cdk.Stack {
     constructor(parent: cdk.App, name: string, props?: cdk.StackProps) {
       super(parent, name, props);
   
       const queue = new sqs.Queue(this, 'HelloCdkQueue', {
         visibilityTimeoutSec: 300
       });
   
       const topic = new sns.Topic(this, 'HelloCdkTopic');
   
       topic.subscribeQueue(queue);
     }
   }
   ```
   + The `Stack`, `App`, `StackProps`, `Queue`, and `Topic` classes represent an AWS CloudFormation stack and its properties, an executable program, an Amazon SQS queue, and an Amazon SNS topic, respectively\.
   + The `HelloCdkStack` class represents the AWS CloudFormation stack for this application\. This stack contains the new Amazon SQS queue and Amazon SNS topic for this application\.

1. In the **Environment** window, open the `bin/hello-cdk.ts` file, and browse the following code in that file\.

   ```
   #!/usr/bin/env node
   import cdk = require('@aws-cdk/cdk');
   import { HelloCdkStack } from '../lib/hello-cdk-stack';
   
   const app = new cdk.App();
   new HelloCdkStack(app, 'HelloCdkStack');
   app.run();
   ```

   This code loads, instantiates, and then runs the `HelloCdkStack` class from the `lib/hello-cdk-stack.ts` file\.

1. Use ** `npm` ** to run the TypeScript compiler to check for coding errors, and then enable the AWS CDK to execute the project's `bin/hello-cdk.js` file\. To do this, from the project's root directory, run the ** `npm` ** command with the ** `run` ** action, specifying the ** `build` ** command value in the `package.json` file, as follows\.

   ```
   npm run build
   ```

   The preceding command runs the TypeScript compiler, which adds supporting `bin/hello-cdk.d.ts` and `lib/hello-cdk-stack.d.ts` files\. The compiler also transpiles the `hello-cdk.ts` and `hello-cdk-stack.ts` files into `hello-cdk.js` and `hello-cdk-stack.js` files\.

## Step 3: Run the code<a name="sample-cdk-run"></a>

In this step, you instruct the AWS CDK to create a AWS CloudFormation stack template based on the code in the `bin/hello-cdk.js` file\. You then instruct the AWS CDK to deploy the stack, which creates the Amazon SNS topic and Amazon SQS queue and then subscribes the queue to the topic\. You then confirm that the topic and queue were successfully deployed by sending a message from the topic to the queue\.

1. Have the AWS CDK create the AWS CloudFormation stack template\. To do this, with the terminal session still open in the IDE, from the project's root directory, run the ** `cdk` ** command with the ** `synth` ** action and the name of the stack\.

   ```
   cdk synth HelloCdkStack
   ```

   If successful, the output displays the AWS CloudFormation stack template's `Resources` section\.

1. The first time that you deploy an AWS CDK app into an environment for a specific AWS account and AWS Region combination, you must install a *bootstrap stack*\. This stack includes various resources that the AWS CDK needs to complete its various operations\. For example, this stack includes an Amazon S3 bucket that the AWS CDK uses to store templates and assets during its deployment processes\. To install the bootstrap stack, run the ** `cdk` ** command with the ** `bootstrap` ** action\.

   ```
   cdk bootstrap
   ```
**Note**  
If you run `cdk bootstrap` without specifying any options, the default AWS account and AWS Region are used\. You can also bootstrap a specific environment by specifying a profile and account/Region combination\. For example:  

   ```
   cdk bootstrap --profile test 123456789012/us-east-1
   ```

1. Have the AWS CDK run the AWS CloudFormation stack template to deploy the stack\. To do this, from the project's root directory, run the ** `cdk` ** command with the ** `deploy` ** action and the name of the stack\.

   ```
   cdk deploy HelloCdkStack
   ```

   If successful, the output displays that the `HelloCdkStack` stack deployed without errors\.
**Note**  
If the output displays a message that the stack does not define an environment and that AWS credentials could not be obtained from standard locations or no region was configured, make sure that your AWS credentials are set correctly in the IDE, and then run the ** `cdk deploy` ** command again\. For more information, see [Calling AWS services from an environment in AWS Cloud9](credentials.md)\.

1. To confirm that the Amazon SNS topic and Amazon SQS queue were successfully deployed, send a message to the topic, and then check the queue for the received message\. To do this, you can use a tool such as the AWS Command Line Interface \(AWS CLI\) or the aws\-shell\. For more information about these tools, see the [AWS Command Line Interface and aws\-shell sample for AWS Cloud9](sample-aws-cli.md)\.

   For example, to send a message to the topic, with the terminal session still open in the IDE, use the AWS CLI to run the Amazon SNS** `publish` ** command, supplying the message's subject and body, the AWS Region for the topic, and the topic's Amazon Resource Name \(ARN\)\.

   ```
   aws sns publish --subject "Hello from the AWS CDK" --message "This is a message from the AWS CDK." --topic-arn arn:aws:sns:us-east-2:123456789012:HelloCdkStack-HelloCdkTopic1A234567-8BCD9EFGHIJ0K
   ```

   In the preceding command, replace `arn:aws:sns:us-east-2:123456789012:HelloCdkStack-HelloCdkTopic1A234567-8BCD9EFGHIJ0K` with the ARN that AWS CloudFormation assigns to the topic\. To get the ID, you can run the Amazon SNS** `list-topics` ** command\.

   ```
   aws sns list-topics --output table --query 'Topics[*].TopicArn'
   ```

   If successful, the output of the ** `publish` ** command displays the `MessageId` value for the message that was published\.

   To check the queue for the received message, run the Amazon SQS** `receive-message` ** command, supplying the queue's URL\.

   ```
   aws sqs receive-message --queue-url https://queue.amazonaws.com/123456789012/HelloCdkStack-HelloCdkQueue1A234567-8BCD9EFGHIJ0K
   ```

   In the preceding command, replace `https://queue.amazonaws.com/123456789012/HelloCdkStack-HelloCdkQueue1A234567-8BCD9EFGHIJ0K` with the ARN that AWS CloudFormation assigns to the queue\. To get the URL, you can run the Amazon SQS** `list-queues` ** command\.

   ```
   aws sqs list-queues --output table --query 'QueueUrls[*]'
   ```

   If successful, the output of the ** `receive-message` ** command displays information about the message that was received\.

## Step 4: Clean up<a name="sample-cdk-clean-up"></a>

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the AWS CloudFormation stack\. This deletes the the Amazon SNS topic and Amazon SQS queue\. You should also delete the environment\.

### Step 4\.1: Delete the stack<a name="step-4-1-delete-the-stack"></a>

With the terminal session still open in the IDE, from the project's root directory, run the ** `cdk` ** command with the ** `destroy` ** action and the stack's name\.

```
cdk destroy HelloCdkStack
```

When prompted to delete the stack, type `y`, and then press `Enter`\.

If successful, the output displays that the `HelloCdkStack` stack was deleted without errors\.

### Step 4\.2: Delete the environment<a name="step-4-2-delete-the-envtitle"></a>

To delete the environment, see [Deleting an environment in AWS Cloud9](delete-environment.md)\.