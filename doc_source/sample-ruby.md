# Ruby Sample for AWS Cloud9<a name="sample-ruby"></a>

This sample enables you to run some Ruby scripts in an AWS Cloud9 development environment\.

Creating this sample might result in charges to your AWS account\. These include possible charges for services such as Amazon EC2 and Amazon S3\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/) and [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/)\.

**Topics**
+ [Prerequisites](#sample-ruby-prereqs)
+ [Step 1: Install Required Tools](#sample-ruby-install)
+ [Step 2: Add Code](#sample-ruby-code)
+ [Step 3: Run the Code](#sample-ruby-run)
+ [Step 4: Install and Configure the AWS SDK for Ruby](#sample-ruby-sdk)
+ [Step 5: Add AWS SDK Code](#sample-ruby-sdk-code)
+ [Step 6: Run the AWS SDK Code](#sample-ruby-sdk-run)
+ [Step 7: Clean Up](#sample-ruby-clean-up)

## Prerequisites<a name="sample-ruby-prereqs"></a>

Before you use this sample, be sure to meet the following requirements\.
+  **You must have an existing AWS Cloud9 EC2 development environment\.** This sample assumes you already have an EC2 environment that is connected to an Amazon EC2 instance running Amazon Linux or Ubuntu Server\. If you have a different type of environment or operating system, you might need to adapt this sample's instructions to set up related tools\. See [Creating an Environment in AWS Cloud9](create-environment.md) for details\.
+  **You have the AWS Cloud9 IDE for the existing environment already open\.** When you open an environment, AWS Cloud9 opens the IDE for that environment in your web browser\. See [Opening an Environment in AWS Cloud9](open-environment.md) for details\.

## Step 1: Install Required Tools<a name="sample-ruby-install"></a>

In this step, you install Ruby, which is required to run this sample\.

1. In a terminal session in the AWS Cloud9 IDE, confirm whether Ruby is already installed by running the ** `ruby --version` ** command\. \(To start a new terminal session, on the menu bar, choose **Window**, **New Terminal**\.\) If successful, the output contains the Ruby version number\. If Ruby is installed, skip ahead to [Step 2: Add Code](#sample-ruby-code)\.

1. Run the ** `yum update` ** for \(Amazon Linux\) or ** `apt update` ** for \(Ubuntu Server\) command to help ensure the latest security updates and bug fixes are installed\.

   For Amazon Linux:

   ```
   sudo yum -y update
   ```

   For Ubuntu Server:

   ```
   sudo apt update
   ```

1. Install Ruby by running the ** `install` ** command\.

   For Amazon Linux:

   ```
   sudo yum -y install ruby
   ```

   For Ubuntu Server:

   ```
   sudo apt install -y ruby
   ```

   For more information, see [Installing Ruby](https://www.ruby-lang.org/en/documentation/installation) on the Ruby website\.

## Step 2: Add Code<a name="sample-ruby-code"></a>

In the AWS Cloud9 IDE, create a file with this content, and save the file with the name `hello.rb`\. \(To create a file, on the menu bar, choose **File**, **New File**\. To save the file, choose **File**, **Save**\.\)

```
puts "Hello, World!"

puts "The sum of 2 and 3 is 5."

argv0 = ARGV[0]
argv1 = ARGV[1]
sum = argv0.to_i + argv1.to_i

puts "The sum of #{argv0} and #{argv1} is #{sum}."
```

## Step 3: Run the Code<a name="sample-ruby-run"></a>

1. In the AWS Cloud9 IDE, on the menu bar, choose **Run**, **Run Configurations**, **New Run Configuration**\.

1. On the **\[New\] \- Idle** tab, choose **Runner: Auto**, and then choose **Ruby**\.

1. For **Command**, type `hello.rb 5 9`\. In the code, `5` represents `ARGV[0]`, and `9` represents `ARGV[1]`\.

1. Choose the **Run** button, and compare your output\.

   ```
   Hello, World!
   The sum of 2 and 3 is 5.
   The sum of 5 and 9 is 14.
   ```

![\[Output of running the Ruby code in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-ruby-simple.png)

## Step 4: Install and Configure the AWS SDK for Ruby<a name="sample-ruby-sdk"></a>

You can enhance this sample to use the AWS SDK for Ruby to create an Amazon S3 bucket, list your available buckets, and then delete the bucket you just created\.

In this step, you install and configure the AWS SDK for Ruby, which provides a convenient way to interact with AWS services such as Amazon S3, from your Ruby code\. Before you can install the AWS SDK for Ruby, you must install RubyGems\. After you install the AWS SDK for Ruby, you must set up credentials management in your environment\. The AWS SDK for Ruby needs these credentials to interact with AWS services\.

### To install RubyGems<a name="sample-ruby-sdk-install-gems"></a>

1. In the AWS Cloud9 IDE, confirm whether RubyGems is already installed by running the ** `gem --version` ** command\. If successful, the output contains the RubyGems version number\. Otherwise, an error message should be output\. If RubyGems is installed, skip ahead to "Step 4\.2: Install the AWS SDK for Ruby\."

1. To install RubyGems, run the ** `install` ** command\.

   For Amazon Linux:

   ```
   sudo yum -y install gem
   ```

   For Ubuntu Server:

   ```
   sudo apt install -y gem
   ```

   For more information, see [Download RubyGems](https://rubygems.org/pages/download) on the RubyGems website\.

### To install the AWS SDK for Ruby<a name="sample-ruby-sdk-install-sdk"></a>

After you install RubyGems, run the ** `gem install` ** command\.

```
sudo gem install aws-sdk
```

For more information, see [Installing the AWS SDK for Ruby](https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/setup-install.html) in the *AWS SDK for Ruby Developer Guide*\.

### To set up credentials management in your environment<a name="sample-ruby-sdk-creds"></a>

Each time you use the AWS SDK for Ruby to call an AWS service, you must provide a set of credentials with the call\. These credentials determine whether the AWS SDK for Ruby has the appropriate permissions to make that call\. If the credentials don't cover the appropriate permissions, the call will fail\.

In this step, you will store your credentials within the environment\. To do this, follow the instructions in [Calling AWS Services from an Environment in AWS Cloud9](credentials.md), and then return to this topic\.

For additional information, see [Configuring the AWS SDK for Ruby](https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/setup-config.html) in the *AWS SDK for Ruby Developer Guide*\.

## Step 5: Add AWS SDK Code<a name="sample-ruby-sdk-code"></a>

In this step, you will add some more code, this time to interact with Amazon S3 to create a bucket, list your available buckets, and then delete the bucket you just created\. You will run this code later\.

In the AWS Cloud9 IDE, create a file with this content, and save the file with the name `s3.rb`\.

```
require 'aws-sdk'

if ARGV.length < 2
  puts "Usage: ruby s3.rb <the bucket name> <the AWS Region to use>\n" +
    "Example: ruby s3.rb my-test-bucket us-east-2"
end

bucket_name = ARGV[0]
region = ARGV[1]
s3 = Aws::S3::Client.new(region: region)

# Lists all of your available buckets in this AWS Region.
def list_my_buckets(s3)
  resp = s3.list_buckets()
  puts "My buckets now are:\n\n"

  resp.buckets.each do |bucket|
    puts bucket.name
  end

end

list_my_buckets(s3)

# Create a new bucket.
begin
  puts "\nCreating a new bucket named '#{bucket_name}'...\n\n"
  s3.create_bucket({
    bucket: bucket_name,
    create_bucket_configuration: {
      location_constraint: region
    }
  })
  
  s3.wait_until(:bucket_exists, {bucket: bucket_name,})
rescue Aws::S3::Errors::BucketAlreadyExists
  puts "Cannot create the bucket. " +
    "A bucket with the name '#{bucket_name}' already exists. Exiting."
  exit(false)
end

list_my_buckets(s3)

# Delete the bucket you just created.
puts "\nDeleting the bucket named '#{bucket_name}'...\n\n"
s3.delete_bucket(bucket: bucket_name)

s3.wait_until(:bucket_not_exists, {bucket: bucket_name,})

list_my_buckets(s3)
```

## Step 6: Run the AWS SDK Code<a name="sample-ruby-sdk-run"></a>

1. In the AWS Cloud9 IDE, on the menu bar, choose **Run**, **Run Configurations**, **New Run Configuration**\.

1. In the **\[New\] \- Idle** tab, choose **Runner: Auto**, and then choose **Ruby**\.

1. For **Command**, type `s3.rb YOUR_BUCKET_NAME THE_AWS_REGION `, where ` YOUR_BUCKET_NAME ` is the name of the bucket you want to create and then delete, and ` THE_AWS_REGION ` is the ID of the AWS Region you want to create the bucket in\. For example, for the US East \(Ohio\) Region, use `us-east-2`\. For more IDs, see [Amazon Simple Storage Service \(Amazon S3\)](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) in the *Amazon Web Services General Reference*\.
**Note**  
Amazon S3 bucket names must be unique across AWS—not just your AWS account\.

1. Choose the **Run** button, and compare your output\.

   ```
   My buckets now are:
   
   Creating a new bucket named 'my-test-bucket'...
   
   My buckets now are:
   
   my-test-bucket
   
   Deleting the bucket named 'my-test-bucket'...
   
   My buckets now are:
   ```

## Step 7: Clean Up<a name="sample-ruby-clean-up"></a>

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the environment\. For instructions, see [Deleting an Environment in AWS Cloud9](delete-environment.md)\.