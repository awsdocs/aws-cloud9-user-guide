# TypeScript Sample for AWS Cloud9<a name="sample-typescript"></a>

This sample shows you how to work with TypeScript in an AWS Cloud9 development environment\.

Creating this sample might result in charges to your AWS account\. These include possible charges for services such as Amazon EC2 and Amazon S3\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/) and [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/)\.

**Topics**
+ [Prerequisites](#sample-typescript-prereqs)
+ [Step 1: Install Required Tools](#sample-typescript-install)
+ [Step 2: Add Code](#sample-typescript-code)
+ [Step 3: Run the Code](#sample-typescript-run)
+ [Step 4: Install and Configure the AWS SDK for JavaScript in Node\.js](#sample-typescript-sdk)
+ [Step 5: Add AWS SDK Code](#sample-typescript-sdk-code)
+ [Step 6: Run the AWS SDK Code](#sample-typescript-sdk-run)
+ [Step 7: Clean Up](#sample-typescript-clean-up)

## Prerequisites<a name="sample-typescript-prereqs"></a>

Before you use this sample, be sure to meet the following requirements\.
+  **You must have an existing AWS Cloud9 EC2 development environment\.** This sample assumes you already have an EC2 environment that is connected to an Amazon EC2 instance running Amazon Linux or Ubuntu Server\. If you have a different type of environment or operating system, you might need to adapt this sample's instructions to set up related tools\. See [Creating an Environment in AWS Cloud9](create-environment.md) for details\.
+  **You have the AWS Cloud9 IDE for the existing environment already open\.** When you open an environment, AWS Cloud9 opens the IDE for that environment in your web browser\. See [Opening an environment in AWS Cloud9](open-environment.md) for details\.

## Step 1: Install Required Tools<a name="sample-typescript-install"></a>

In this step, you install TypeScript by using Node Package Manager \(** `npm` **\)\. To install ** `npm` **, you use Node Version Manager \(** `nvm` **\)\. If you don't have ** `nvm` **, you install it in this step first\.

1. In a terminal session in the AWS Cloud9 IDE, confirm whether TypeScript is already installed by running the command line TypeScript compiler with the ** `--version` ** option\. \(To start a new terminal session, on the menu bar, choose **Window**, **New Terminal**\.\) If successful, the output contains the TypeScript version number\. If TypeScript is installed, skip ahead to [Step 2: Add Code](#sample-typescript-code)\.

   ```
   tsc --version
   ```

1. Confirm whether ** `npm` ** is already installed by running ** `npm` ** with the ** `--version` ** option\. If successful, the output contains the ** `npm` ** version number\. If ** `npm` ** is installed, skip ahead to step 10 in this procedure to use ** `npm` ** to install TypeScript\.

   ```
   npm --version
   ```

1. Run the ** `yum update` ** for \(Amazon Linux\) or ** `apt update` ** for \(Ubuntu Server\) command to help ensure the latest security updates and bug fixes are installed\.

   For Amazon Linux:

   ```
   sudo yum -y update
   ```

   For Ubuntu Server:

   ```
   sudo apt update
   ```

1. To install ** `npm` **, begin by running the following command to download Node Version Manager \(** `nvm` **\)\. \(** `nvm` ** is a simple Bash shell script that's useful for installing and managing Node\.js versions\. For more information, see [Node Version Manager](https://github.com/creationix/nvm/blob/master/README.md) on the GitHub website\.\)

   ```
   curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash
   ```

1. To start using ** `nvm` **, either close the terminal session and start it again, or source the `~/.bashrc` file that contains the commands to load ** `nvm` **\.

   ```
   . ~/.bashrc
   ```

1. Confirm that ** `nvm` ** is installed by running ** `nvm` ** with the ** `--version` ** option\.

   ```
   nvm --version
   ```

1. Install the latest version of Node\.js by running ** `nvm` **\. \(** `npm` ** is included in Node\.js\.\)

   ```
   nvm install node
   ```

1. Confirm that Node\.js is installed by running the command line version of Node\.js with the ** `--version` ** option\.

   ```
   node --version
   ```

1. Confirm that ** `npm` ** is installed by running ** `npm` ** with the ** `--version` ** option\.

   ```
   npm --version
   ```

1. Install TypeScript by running ** `npm` ** with the ** `-g` ** option\. This installs TypeScript as a global package in the environment\.

   ```
   npm install -g typescript
   ```

1. Confirm that TypeScript is installed by running the command line TypeScript compiler with the ** `--version` ** option\.

   ```
   tsc --version
   ```

## Step 2: Add Code<a name="sample-typescript-code"></a>

1. In the AWS Cloud9 IDE, create a file named `hello.ts`\. \(To create a file, on the menu bar, choose **File**, **New File**\. To save the file, choose **File**, **Save**\.\)

1. In a terminal in the IDE, from the same directory as the `hello.ts` file, run ** `npm` ** to install the `@types/node` library\.

   ```
   npm install @types/node
   ```

   This adds a `node_modules/@types/node` folder in the same directory as the `hello.ts` file\. This new folder contains Node\.js type definitions that TypeScript needs later in this procedure for the `console.log` and `process.argv` properties that you will add to the `hello.ts` file\.

1. Add the following code to the `hello.ts` file:

   ```
   console.log('Hello, World!');
   
   console.log('The sum of 2 and 3 is 5.');
   
   const sum: number = parseInt(process.argv[2], 10) + parseInt(process.argv[3], 10);
   
   console.log('The sum of ' + process.argv[2] + ' and ' +
     process.argv[3] + ' is ' + sum + '.');
   ```

## Step 3: Run the Code<a name="sample-typescript-run"></a>

1. In the terminal, from the same directory as the `hello.ts` file, run the TypeScript compiler\. Specify the `hello.ts` file and additional libraries to include\.

   ```
   tsc hello.ts --lib es6
   ```

   TypeScript uses the `hello.ts` file and a set of ECMAScript 6 \(ES6\) library files to transpile the TypeScript code in the `hello.ts` file into equivalent JavaScript code in a file named `hello.js`\.

1. In the **Environment** window, open the `hello.js` file\.

1. On the menu bar, choose **Run**, **Run Configurations**, **New Run Configuration**\.

1. On the **\[New\] \- Idle** tab, choose **Runner: Auto**, and then choose **Node\.js**\.

1. For **Command**, type `hello.js 5 9`\. In the code, `5` represents `process.argv[2]`, and `9` represents `process.argv[3]`\. \(`process.argv[0]` represents the name of the runtime \(`node`\), and `process.argv[1]` represents the name of the file \(`hello.js`\)\.\)

1. Choose **Run**, and compare your output\. When you're done, choose **Stop**\.

   ```
   Hello, World!
   The sum of 2 and 3 is 5.
   The sum of 5 and 9 is 14.
   ```

![\[Node.js output after running the code in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-nodejs-simple.png)

**Note**  
Instead of creating a new run configuration in the IDE, you can also execute this code by running the command ** `node hello.js 5 9` ** from the terminal\.

## Step 4: Install and Configure the AWS SDK for JavaScript in Node\.js<a name="sample-typescript-sdk"></a>

You can enhance this sample to use the AWS SDK for JavaScript in Node\.js to create an Amazon S3 bucket, list your available buckets, and then delete the bucket you just created\.

In this step, you install and configure the AWS SDK for JavaScript in Node\.js\. The SDK provides a convenient way to interact with AWS services such as Amazon S3, from your JavaScript code\. After you install the AWS SDK for JavaScript in Node\.js, you must set up credentials management in your environment\. The SDK needs these credentials to interact with AWS services\.

### To install the AWS SDK for JavaScript in Node\.js<a name="sample-typescript-sdk-install-sdk"></a>

In a terminal session in the AWS Cloud9 IDE, from the same directory as the `hello.js` file from [Step 3: Run the Code](#sample-typescript-run), run ** `npm` ** to install the AWS SDK for JavaScript in Node\.js\.

```
npm install aws-sdk
```

This command adds several folders to the `node_modules` folder from [Step 3: Run the Code](#sample-typescript-run)\. These folders contain source code and dependencies for the AWS SDK for JavaScript in Node\.js\. For more information, see [Installing the SDK for JavaScript](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/installing-jssdk.html) in the *AWS SDK for JavaScript Developer Guide*\.

### To set up credentials management in your environment<a name="sample-typescript-sdk-creds"></a>

Each time you use the AWS SDK for JavaScript in Node\.js to call an AWS service, you must provide a set of credentials with the call\. These credentials determine whether the AWS SDK for JavaScript in Node\.js has the appropriate permissions to make that call\. If the credentials don't cover the appropriate permissions, the call will fail\.

In this step, you store your credentials within the environment\. To do this, follow the instructions in [Calling AWS Services from an Environment in AWS Cloud9](credentials.md), and then return to this topic\.

For additional information, see [Setting Credentials in Node\.js](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/setting-credentials-node.html) in the *AWS SDK for JavaScript Developer Guide*\.

## Step 5: Add AWS SDK Code<a name="sample-typescript-sdk-code"></a>

In this step, you add some more code, this time to interact with Amazon S3 to create a bucket, list your available buckets, and then delete the bucket you just created\. You'll run this code later\.

1. In the AWS Cloud9 IDE, in the same directory as the `hello.js` file in previous steps, create a file named `s3.ts`\.

1. From a terminal in the AWS Cloud9 IDE, in the same directory as the `s3.ts` file, enable the code to call Amazon S3 operations asynchronously by running ** `npm` ** twice to install the async library for TypeScript and again for JavaScript\.

   ```
   npm install @types/async # For TypeScript.
   npm install async        # For JavaScript.
   ```

1. Add the following code to the `s3.ts` file:

   ```
   import * as async from 'async';
   import * as AWS from 'aws-sdk';
   
   if (process.argv.length < 4) {
     console.log('Usage: node s3.js <the bucket name> <the AWS Region to use>\n' +
       'Example: node s3.js my-test-bucket us-east-2');
     process.exit(1);
   }
   
   const AWS = require('aws-sdk'); // To set the AWS credentials and AWS Region.
   const async = require('async'); // To call AWS operations asynchronously.
   
   const s3: AWS.S3 = new AWS.S3({apiVersion: '2006-03-01'});
   const bucket_name: string = process.argv[2];
   const region: string = process.argv[3];
   
   AWS.config.update({
     region: region
   });
   
   const create_bucket_params: any = {
     Bucket: bucket_name,
     CreateBucketConfiguration: {
       LocationConstraint: region
     }
   };
   
   const delete_bucket_params: any = {
     Bucket: bucket_name
   };
   
   // List all of your available buckets in this AWS Region.
   function listMyBuckets(callback): void {
     s3.listBuckets(function(err, data) {
       if (err) {
   
       } else {
         console.log("My buckets now are:\n");
   
         for (let i: number = 0; i < data.Buckets.length; i++) {
           console.log(data.Buckets[i].Name);
         }
       }
   
       callback(err);
     });
   }
   
   // Create a bucket in this AWS Region.
   function createMyBucket(callback): void {
     console.log("\nCreating a bucket named '" + bucket_name + "'...\n");
   
     s3.createBucket(create_bucket_params, function(err, data) {
       if (err) {
         console.log(err.code + ": " + err.message);
       }
   
       callback(err);
     });
   }
   
   // Delete the bucket you just created.
   function deleteMyBucket(callback): void {
     console.log("\nDeleting the bucket named '" + bucket_name + "'...\n");
   
     s3.deleteBucket(delete_bucket_params, function(err, data) {
       if (err) {
         console.log(err.code + ": " + err.message);
       }
   
       callback(err);
     });
   }
   
   // Call the AWS operations in the following order.
   async.series([
     listMyBuckets,
     createMyBucket,
     listMyBuckets,
     deleteMyBucket,
     listMyBuckets
   ]);
   ```

## Step 6: Run the AWS SDK Code<a name="sample-typescript-sdk-run"></a>

1. In the terminal, from the same directory as the `s3.ts` file, run the TypeScript compiler\. Specify the `s3.ts` file and additional libraries to include\.

   ```
   tsc s3.ts --lib es6
   ```

   TypeScript uses the `s3.ts` file, the AWS SDK for JavaScript in Node\.js, the async library, and a set of ECMAScript 6 \(ES6\) library files to transpile the TypeScript code in the `s3.ts` file into equivalent JavaScript code in a file named `s3.js`\.

1. In the **Environment** window, open the `s3.js` file\.

1. On the menu bar, choose **Run**, **Run Configurations**, **New Run Configuration**\.

1. On the **\[New\] \- Idle** tab, choose **Runner: Auto**, and then choose **Node\.js**\.

1. For **Command**, type `s3.js YOUR_BUCKET_NAME THE_AWS_REGION `, where ` YOUR_BUCKET_NAME ` is the name of the bucket you want to create and then delete, and ` THE_AWS_REGION ` is the ID of the AWS Region to create the bucket in\. For example, for the US East \(Ohio\) Region, use `us-east-2`\. For more IDs, see [Amazon Simple Storage Service \(Amazon S3\)](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) in the *Amazon Web Services General Reference*\.
**Note**  
Amazon S3 bucket names must be unique across AWS—not just your AWS account\.

1. Choose **Run**, and compare your output\. When you're done, choose **Stop**\.

   ```
   My buckets now are:
   
   Creating a new bucket named 'my-test-bucket'...
   
   My buckets now are:
   
   my-test-bucket
   
   Deleting the bucket named 'my-test-bucket'...
   
   My buckets now are:
   ```

## Step 7: Clean Up<a name="sample-typescript-clean-up"></a>

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the environment\. For instructions, see [Deleting an Environment in AWS Cloud9](delete-environment.md)\.