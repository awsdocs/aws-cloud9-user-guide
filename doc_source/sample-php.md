# PHP Sample for AWS Cloud9<a name="sample-php"></a>

This sample enables you to run some PHP scripts in an AWS Cloud9 development environment\.

Creating this sample might result in charges to your AWS account\. These include possible charges for services such as Amazon EC2 and Amazon S3\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/) and [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/)\.
+  [Prerequisites](#sample-php-prereqs) 
+  [Step 1: Install Required Tools](#sample-php-install) 
+  [Step 2: Add Code](#sample-php-code) 
+  [Step 3: Run the Code](#sample-php-run) 
+  [Step 4: Install and Configure the AWS SDK for PHP](#sample-php-sdk) 
+  [Step 5: Add AWS SDK Code](#sample-php-sdk-code) 
+  [Step 6: Run the AWS SDK Code](#sample-php-sdk-run) 
+  [Step 7: Clean Up](#sample-php-clean-up) 

## Prerequisites<a name="sample-php-prereqs"></a>

Before you use this sample, be sure to meet the following requirements\.
+  **You must have an existing AWS Cloud9 development environment\.** This sample assumes you already have an AWS Cloud9 EC2 development environment that is connected to an Amazon EC2 instance running Amazon Linux\. If you have a different type of environment or operating system, you might need to adapt this sample's instructions to set up related tools\. See [Creating an Environment](create-environment.md) for details\.
+  **You have the AWS Cloud IDE for the existing environment already open\.** When you open an environment, AWS Cloud9 opens the IDE for that environment in your web browser\. See [Opening an Environment](open-environment.md) for details\.

## Step 1: Install Required Tools<a name="sample-php-install"></a>

In this step, you install PHP, which is required to run this sample\.

**Note**  
The following procedure installs PHP only\. To install related tools such as an Apache web server and a MySQL database, see [Tutorial: Installing a LAMP Web Server on Amazon Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-LAMP.html) in the *Amazon EC2 User Guide for Linux Instances*\.

1. In a terminal session in the AWS Cloud9 IDE, confirm whether PHP is already installed by running the ** `php --version` ** command\. \(To start a new terminal session, on the menu bar, choose **Window**, **New Terminal**\.\) If successful, the output contains the PHP version number\. If PHP is installed, skip ahead to [Step 2: Add Code](#sample-php-code)\.

1. Run the ** `yum update` ** command to help ensure the latest security updates and bug fixes are installed\.

   ```
   sudo yum -y update
   ```

1. Install PHP by running the ** `install` ** command\.

   ```
   sudo yum -y install php56
   ```

   For more information, see [Installation and Configuration](http://php.net/manual/en/install.php) on the PHP website\.

## Step 2: Add Code<a name="sample-php-code"></a>

In the AWS Cloud9 IDE, create a file with this content, and save the file with the name `hello.php`\. \(To create a file, on the menu bar, choose **File**, **New File**\. To save the file, choose **File**, **Save**, type `hello.php` for **Filename**, and then choose **Save**\.\)

```
<?php
  print('Hello, World!');

  print("\nThe sum of 2 and 3 is 5.");

  $sum = (int)$argv[1] + (int)$argv[2];

  print("\nThe sum of $argv[1] and $argv[2] is $sum.");
?>
```

**Note**  
The preceding code doesn't rely on any external files\. However, if you ever include or require other PHP files in your file, and you want AWS Cloud9 to use those files to do code completion as you type, turn on the **Project, PHP Support, Enable PHP code completion** setting in **Preferences**, and then add the paths to those files to the **Project, PHP Support, PHP Completion Include Paths** setting\. \(To view and change your preferences, choose **AWS Cloud9, Preferences** on the menu bar\.\)

## Step 3: Run the Code<a name="sample-php-run"></a>

1. In the AWS Cloud9 IDE, on the menu bar, choose **Run**, **Run Configurations**, **New Run Configuration**\.

1. On the **\[New\] \- Idle** tab, choose **Runner: Auto**, and then choose **PHP \(cli\)**\.

1. For **Command**, type `hello.php 5 9`\. In the code, `5` represents `$argv[1]`, and `9` represents `$argv[2]`\. \(`$argv[0]` represents the name of the file \(`hello.php`\)\.\)

1. Choose the **Run** button, and compare your output\.

   ```
   Hello, World!
   The sum of 2 and 3 is 5.
   The sum of 5 and 9 is 14.
   ```

![\[Output of running the PHP code in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-php-simple.png)

## Step 4: Install and Configure the AWS SDK for PHP<a name="sample-php-sdk"></a>

You can enhance this sample to use the AWS SDK for PHP to create an Amazon S3 bucket, list your available buckets, and then delete the bucket you just created\.

In this step, you install and configure the AWS SDK for PHP, which provides a convenient way to interact with AWS services such as Amazon S3, from your PHP code\. Before you can install the AWS SDK for PHP, you should install [Composer](https://getcomposer.org/)\. After you install the AWS SDK for PHP, you must set up credentials management in your environment\. The AWS SDK for PHP needs these credentials to interact with AWS services\.

### To install Composer<a name="w3aac21c31c17b7"></a>

Run the ** `curl` ** command with the silent \(`-s`\) and show error \(`-S`\) options, piping the Composer installer into a PHP archive \(PHAR\) file, named `composer.phar` by convention\.

```
curl -sS https://getcomposer.org/installer | php
```

### To install the AWS SDK for PHP<a name="w3aac21c31c17b9"></a>

Use the php command to run the Composer installer to install the AWS SDK for PHP\.

```
php composer.phar require aws/aws-sdk-php
```

This command creates several folders and files in your environment\. The primary file you will use is `autoload.php`, which is in the `vendor` folder in your environment\.

For more information, see [Installation](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/installation.html) in the *AWS SDK for PHP Getting Started Guide*\.

### To set up credentials management in your environment<a name="w3aac21c31c17c11"></a>

Each time you use the AWS SDK for PHP to call an AWS service, you must provide a set of credentials with the call\. These credentials determine whether the AWS SDK for PHP has the appropriate permissions to make that call\. If the credentials don't cover the appropriate permissions, the call will fail\.

In this step, you store your credentials within the environment\. To do this, follow the instructions in [Call AWS Services from an Environment](credentials.md), and then return to this topic\.

For additional information, see the "Creating a client" section of [Basic Usage](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/basic-usage.html) in the *AWS SDK for PHP Getting Started Guide*\.

## Step 5: Add AWS SDK Code<a name="sample-php-sdk-code"></a>

In this step, you add some more code, this time to interact with Amazon S3 to create a bucket, list your available buckets, and then delete the bucket you just created\. You will run this code later\.

In the AWS Cloud9 IDE, create a file with this content, and save the file with the name `s3.php`\.

```
<?php
```

```
  require './vendor/autoload.php';

  if ($argc < 4) {
    exit("Usage: php s3.php <the time zone> <the bucket name> <the AWS Region to use>\n" .
      "Example: php s3.php America/Los_Angeles my-test-bucket us-east-2");
  }

  $timeZone = $argv[1];
  $bucketName = $argv[2];
  $region = $argv[3];

  date_default_timezone_set($timeZone);

  $s3 = new Aws\S3\S3Client([
    'region' => $region,
    'version' => '2006-03-01'
  ]);

  # Lists all of your available buckets in this AWS Region.
  function listMyBuckets($s3) {
    print("\nMy buckets now are:\n");

    $promise = $s3->listBucketsAsync();

    $result = $promise->wait();

    foreach ($result['Buckets'] as $bucket) {
      print("\n");
      print($bucket['Name']);
    }
  }

  listMyBuckets($s3);

  # Create a new bucket.
  print("\n\nCreating a new bucket named '$bucketName'...\n");

  try {
    $promise = $s3->createBucketAsync([
      'Bucket' => $bucketName,
      'CreateBucketConfiguration' => [
        'LocationConstraint' => $region
      ]
    ]);

    $promise->wait();

  } catch (Exception $e) {
    if ($e->getCode() == 'BucketAlreadyExists') {
      exit("\nCannot create the bucket. " .
        "A bucket with the name '$bucketName' already exists. Exiting.");
    }
  }

  listMyBuckets($s3);

  # Delete the bucket you just created.
  print("\n\nDeleting the bucket named '$bucketName'...\n");

  $promise = $s3->deleteBucketAsync([
    'Bucket' => $bucketName
  ]);

  $promise->wait();

  listMyBuckets($s3);
```

```
?>
```

## Step 6: Run the AWS SDK Code<a name="sample-php-sdk-run"></a>

1. In the AWS Cloud9 IDE, on the menu bar, choose **Run**, **Run Configurations**, **New Run Configuration**\.

1. On the **\[New\] \- Idle** tab, choose **Runner: Auto**, and then choose **PHP \(cli\)**\.

1. For **Command**, type `s3.php America/Los_Angeles my-test-bucket us-east-2`, where:
   +  `America/Los_Angeles` is your default time zone ID\. For more IDs, see [List of Supported Timezones](http://php.net/manual/en/timezones.php) on the PHP website\.
   +  `my-test-bucket` is the name of the bucket you want to create and then delete\.
**Note**  
Amazon S3 bucket names must be unique across AWS—not just your AWS account\.
   +  `us-east-2` is the ID of the AWS Region you want to create the bucket in\. For more IDs, see [Amazon Simple Storage Service \(Amazon S3\)](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) in the *Amazon Web Services General Reference*\.

1. Choose the **Run** button, and compare your output\.

   ```
   My buckets now are:
   
   Creating a new bucket named 'my-test-bucket'...
   
   My buckets now are:
   
   my-test-bucket
   
   Deleting the bucket named 'my-test-bucket'...
   
   My buckets now are:
   ```

## Step 7: Clean Up<a name="sample-php-clean-up"></a>

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the environment\. For instructions, see [Deleting an Environment](delete-environment.md)\.