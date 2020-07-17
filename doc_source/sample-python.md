# Python Tutorial for AWS Cloud9<a name="sample-python"></a>

This tutorial shows you how to run Python code in an AWS Cloud9 development environment\.

Following this tutorial might result in charges to your AWS account\. These include possible charges for services such as Amazon Elastic Compute Cloud \(Amazon EC2\) and Amazon Simple Storage Service \(Amazon S3\)\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/) and [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/)\.

**Topics**
+ [Prerequisites](#sample-python-prereqs)
+ [Step 1: Install Python 3\.6](#sample-python-install)
+ [Step 2: Add Code](#sample-python-code)
+ [Step 3: Run the Code](#sample-python-run)
+ [Step 4: Install and Configure the AWS SDK for Python \(Boto3\)](#sample-python-sdk)
+ [Step 5: Add AWS SDK Code](#sample-python-sdk-code)
+ [Step 6: Run the AWS SDK Code](#sample-python-sdk-run)
+ [Step 7: Clean Up](#sample-python-clean-up)

## Prerequisites<a name="sample-python-prereqs"></a>

Before you use this tutorial, be sure to meet the following requirements\.
+ **You have an AWS Cloud9 EC2 development environment**

  This tutorial assumes that you have an EC2 environment, and that the environment is connected to an Amazon EC2 instance running Amazon Linux or Ubuntu Server\. See [Creating an EC2 Environment](create-environment-main.md) for details\.

  If you have a different type of environment or operating system, you might need to adapt this tutorial's instructions\.
+ **You have opened the AWS Cloud9 IDE for that environment**

  When you open an environment, AWS Cloud9 opens the IDE for that environment in your web browser\. See [Opening an environment in AWS Cloud9](open-environment.md) for details\.

## Step 1: Install Python 3\.6<a name="sample-python-install"></a>

1. In a terminal session in the AWS Cloud9 IDE, confirm whether Python 3\.6 is already installed by running the ** `python --version` ** command\. \(To start a new terminal session, on the menu bar choose **Window**, **New Terminal**\.\) If Python 3\.6 is installed, skip ahead to [Step 2: Add Code](#sample-python-code)\.

1. Run the ** `yum update`** \(for Amazon Linux\) or **`apt update`** \(for Ubuntu Server\) command to help ensure the latest security updates and bug fixes are installed\.

   For Amazon Linux:

   ```
   sudo yum -y update
   ```

   For Ubuntu Server:

   ```
   sudo apt update
   ```

1. Install Python 3\.6 by running the ** `install` ** command\.

   For Amazon Linux:

   ```
   sudo yum -y install python36
   ```

   For Ubuntu Server:

   ```
   sudo apt -y install python3
   ```

## Step 2: Add Code<a name="sample-python-code"></a>

In the AWS Cloud9 IDE, create a file with the following content and save the file with the name `hello.py`\. \(To create a file, on the menu bar choose **File**, **New File**\. To save the file, choose **File**, **Save**\.\)

```
import sys

print('Hello, World!')

print('The sum of 2 and 3 is 5.')

sum = int(sys.argv[1]) + int(sys.argv[2])

print('The sum of {0} and {1} is {2}.'.format(sys.argv[1], sys.argv[2], sum))
```

## Step 3: Run the Code<a name="sample-python-run"></a>

1. In the AWS Cloud9 IDE, on the menu bar choose **Run**, **Run Configurations**, **New Run Configuration**\.

1. On the **\[New\] \- Stopped** tab, enter `hello.py 5 9` for **Command**\. In the code, `5` represents `sys.argv[1]`, and `9` represents `sys.argv[2]`\.

1. Choose **Run** and compare your output\.

   ```
   Hello, World!
   The sum of 2 and 3 is 5.
   The sum of 5 and 9 is 14.
   ```

1. By default, AWS Cloud9 automatically selects a runner for your code\. To change the runner, choose **Runner**, and then choose **Python 2** or **Python 3**\.
**Note**  
You can create custom runners for specific versions of Python\. For details, see [Create a Builder or Runner](build-run-debug.md#build-run-debug-create-builder-runner)\.

## Step 4: Install and Configure the AWS SDK for Python \(Boto3\)<a name="sample-python-sdk"></a>

The AWS SDK for Python \(Boto3\) enables you to use Python code to interact with AWS services like Amazon S3\. For example, you can use the SDK to create an Amazon S3 bucket, list your available buckets, and then delete the bucket you just created\.

### Install pip<a name="sample-python-sdk-install-pip"></a>

In the AWS Cloud9 IDE, confirm whether `pip` is already installed for the active version of Python by running the ** `python -m pip --version` ** command\. If `pip` is installed, skip to the next section\.

To install `pip`, run the following commands\. Because sudo is in a different environment from your user, you must specify the version of Python to use if it differs from the current aliased version\.

```
curl -O https://bootstrap.pypa.io/get-pip.py # Get the install script.
sudo python36 get-pip.py                     # Install pip for Python 3.6.
python -m pip --version                      # Verify pip is installed.
rm get-pip.py                                # Delete the install script.
```

For more information, see [Installation](https://pip.pypa.io/en/stable/installing/) on the `pip` website\.

### Install the AWS SDK for Python \(Boto3\)<a name="sample-python-sdk-install-sdk"></a>

After you install `pip`, install the AWS SDK for Python \(Boto3\) by running the ** `pip install` ** command\.

```
sudo python36 -m pip install boto3  # Install boto3 for Python 3.6.
python -m pip show boto3            # Verify boto3 is installed for the current version of Python.
```

For more information, see the "Installation" section of [Quickstart](http://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) in the AWS SDK for Python \(Boto3\)\.

### Set Up Credentials in Your Environment<a name="sample-python-sdk-credentials"></a>

Each time you use the AWS SDK for Python \(Boto3\) to call an AWS service, you must provide a set of credentials with the call\. These credentials determine whether the SDK has the necessary permissions to make the call\. If the credentials don't cover the necessary permissions, the call fails\.

To store your credentials within the environment, follow the instructions in [Calling AWS Services from an Environment in AWS Cloud9](credentials.md), and then return to this topic\.

For additional information, see [Credentials](http://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html) in the AWS SDK for Python \(Boto3\)\.

## Step 5: Add AWS SDK Code<a name="sample-python-sdk-code"></a>

Add code that uses Amazon S3 to create a bucket, list your available buckets, and optionally delete the bucket you just created\.

In the AWS Cloud9 IDE, create a file with the following content and save the file with the name `s3.py`\.

```
import sys
import boto3
from botocore.exceptions import ClientError


def get_s3(region=None):
    """
    Get a Boto 3 Amazon S3 resource with a specific AWS Region or with your
    default AWS Region.
    """
    return boto3.resource('s3', region_name=region) if region else boto3.resource('s3')


def list_my_buckets(s3):
    print('Buckets:\n\t', *[b.name for b in s3.buckets.all()], sep="\n\t")


def create_and_delete_my_bucket(bucket_name, region, keep_bucket):
    s3 = get_s3(region)

    list_my_buckets(s3)

    try:
        print('\nCreating new bucket:', bucket_name)
        bucket = s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': region
            }
        )
    except ClientError as e:
        print(e)
        sys.exit('Exiting the script because bucket creation failed.')

    bucket.wait_until_exists()
    list_my_buckets(s3)

    if not keep_bucket:
        print('\nDeleting bucket:', bucket.name)
        bucket.delete()

        bucket.wait_until_not_exists()
        list_my_buckets(s3)
    else:
        print('\nKeeping bucket:', bucket.name)


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('bucket_name', help='The name of the bucket to create.')
    parser.add_argument('region', help='The region in which to create your bucket.')
    parser.add_argument('--keep_bucket', help='Keeps the created bucket. When not '
                                              'specified, the bucket is deleted '
                                              'at the end of the demo.',
                        action='store_true')

    args = parser.parse_args()

    create_and_delete_my_bucket(args.bucket_name, args.region, args.keep_bucket)


if __name__ == '__main__':
    main()
```

## Step 6: Run the AWS SDK Code<a name="sample-python-sdk-run"></a>

1. On the menu bar, choose **Run**, **Run Configurations**, **New Run Configuration**\.

1. For **Command**, enter `s3.py my-test-bucket us-west-2`, where `my-test-bucket` is the name of the bucket to create, and `us-west-2` is the ID of the AWS Region where your bucket is created\. By default, your bucket is deleted before the script exits\. To keep your bucket, add `--keep_bucket` to your command\. For a list of AWS Region IDs, see [Amazon Simple Storage Service Endpoints and Quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html) in the *AWS General Reference*\.
**Note**  
Amazon S3 bucket names must be unique across AWS—not just your AWS account\.

1. Choose **Run**, and compare your output\.

   ```
   Buckets:
   
           a-pre-existing-bucket
   
   Creating new bucket: my-test-bucket
   Buckets:
   
           a-pre-existing-bucket
           my-test-bucket
   
   Deleting bucket: my-test-bucket
   Buckets:
   
           a-pre-existing-bucket
   ```

## Step 7: Clean Up<a name="sample-python-clean-up"></a>

To prevent ongoing charges to your AWS account after you're done with this tutorial, delete the AWS Cloud9 environment\. For instructions, see [Deleting an Environment in AWS Cloud9](delete-environment.md)\.