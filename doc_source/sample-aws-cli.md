# AWS Command Line Interface and aws\-shell sample for AWS Cloud9<a name="sample-aws-cli"></a>

This sample enables you to set up the AWS Command Line Interface \(AWS CLI\), the aws\-shell, or both in an AWS Cloud9 development environment\. The AWS CLI and the aws\-shell are unified tools that provide a consistent interface for interacting with all parts of AWS\. You can use the AWS CLI or the aws\-shell instead of the AWS Management Console to quickly run commands to interact with AWS, and some of these commands can only be run with the AWS CLI or the aws\-shell\.

For more information about the AWS CLI, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/)\. For the aws\-shell, see the following resources:
+  [aws\-shell](https://github.com/awslabs/aws-shell) on the GitHub website
+  [aws\-shell](https://pypi.python.org/pypi/aws-shell) on the pip website

For a list of commands you can run with the AWS CLI to interact with AWS, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/)\. You use the same commands with the aws\-shell, except that you start commands without the `aws` prefix\.

Creating this sample might result in charges to your AWS account\. These include possible charges for services such as Amazon EC2 and Amazon S3\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/) and [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/)\.

**Topics**
+ [Prerequisites](#sample-aws-cli-prereqs)
+ [Step 1: Install the AWS CLI, the aws\-shell, or both in your environment](#sample-aws-cli-install)
+ [Step 2: Set up credentials management in your environment](#sample-aws-cli-creds)
+ [Step 3: Run basic commands with the AWS CLI or the aws\-shell in your environment](#sample-aws-cli-run)
+ [Step 4: Clean up](#sample-aws-cli-clean-up)

## Prerequisites<a name="sample-aws-cli-prereqs"></a>

Before you use this sample, be sure to meet the following requirements\.
+  **You must have an existing AWS Cloud9 EC2 development environment\.** This sample assumes you already have an EC2 environment that is connected to an Amazon EC2 instance running Amazon Linux or Ubuntu Server\. If you have a different type of environment or operating system, you might need to adapt this sample's instructions to set up related tools\. See [Creating an environment in AWS Cloud9](create-environment.md) for details\.
+  **You have the AWS Cloud9 IDE for the existing environment already open\.** When you open an environment, AWS Cloud9 opens the IDE for that environment in your web browser\. See [Opening an environment in AWS Cloud9](open-environment.md) for details\.

## Step 1: Install the AWS CLI, the aws\-shell, or both in your environment<a name="sample-aws-cli-install"></a>

In this step, you use the AWS Cloud9 IDE to install the AWS CLI, the aws\-shell, or both in your environment so you can run commands to interact with AWS\.

If you are using an AWS Cloud9 EC2 development environment and you only want to use the AWS CLI, you can skip ahead to [Step 3: Run basic commands with the AWS CLI or the aws\-shell in your environment](#sample-aws-cli-run)\. This is because the AWS CLI is already installed in an EC2 environment, and a set of AWS access credentials is already set up in the environment\. For more information, see [AWS managed temporary credentials](how-cloud9-with-iam.md#auth-and-access-control-temporary-managed-credentials)\.

If you are not using an EC2 environment, do the following to install the AWS CLI:

1. With your environment open, in the IDE, check whether the AWS CLI is already installed\. In the terminal, run the ** `aws --version` ** command\. \(To start a new terminal session, on the menu bar, choose **Window**, **New Terminal**\.\) If the AWS CLI is installed, the version number is displayed, with information such as the version numbers of Python and the operating system version number of your Amazon EC2 instance or your own server\. If the AWS CLI is installed, skip ahead to [Step 2: Set up credentials management in your environment](#sample-aws-cli-creds)\.

1. To install the AWS CLI, see [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/installing.html) in the *AWS Command Line Interface User Guide*\. For example, for an EC2 environment running Amazon Linux, run these three commands, one at a time, in the terminal to install the AWS CLI\.

   ```
   sudo yum -y update          # Install the latest system updates.
   sudo yum -y install aws-cli # Install the AWS CLI.
   aws --version               # Confirm the AWS CLI was installed.
   ```

   For an EC2 environment running Ubuntu Server, run these three commands instead, one at a time, in the terminal to install the AWS CLI\.

   ```
   sudo apt update             # Install the latest system updates.
   sudo apt install -y awscli  # Install the AWS CLI.
   aws --version               # Confirm the AWS CLI was installed.
   ```

If you want to install the aws\-shell, do the following:

1. With your environment open, in the IDE, check whether the aws\-shell is already installed\. In the terminal, run the ** `aws-shell` ** command\. \(To start a new terminal session, on the menu bar, choose **Window**, **New Terminal**\.\) If the aws\-shell is installed, the `aws>` prompt is displayed\. If the aws\-shell is installed, skip ahead to [Step 2: Set up credentials management in your environment](#sample-aws-cli-creds)\.

1. To install the aws\-shell, you use pip\. To use pip, you must have Python installed\.

   To check whether Python is already installed \(and to install it if needed\), follow the instructions in [Step 1: Install Python](sample-python.md#sample-python-install) in the *Python Sample*, and then return to this topic\.

   To check whether pip is already installed, in the terminal, run the ** `pip --version` ** command\. If pip is installed, the version number is displayed\. If pip is not installed, install it by run these three commands, one at a time, in the terminal\.

   ```
   wget https://bootstrap.pypa.io/get-pip.py # Get the pip install file.
   sudo python get-pip.py                    # Install pip. (You might need to run 'sudo python2 get-pip.py' or 'sudo python3 get-pip.py' instead, depending on how Python is installed.)
   rm get-pip.py                             # Delete the pip install file, as it is no longer needed.
   ```

1. To use pip to install the aws\-shell, run the following command\.

   ```
   sudo pip install aws-shell
   ```

## Step 2: Set up credentials management in your environment<a name="sample-aws-cli-creds"></a>

Each time you use the AWS CLI or the aws\-shell to call an AWS service, you must provide a set of credentials with the call\. These credentials determine whether the AWS CLI or the aws\-shell has the appropriate permissions to make that call\. If the credentials don't cover the appropriate permissions, the call will fail\.

If you are using an AWS Cloud9 EC2 development environment, you can skip ahead to [Step 3: Run basic commands with the AWS CLI or the aws\-shell in your environment](#sample-aws-cli-run)\. This is because credentials are already set up in an EC2 environment\. For more information, see [AWS managed temporary credentials](how-cloud9-with-iam.md#auth-and-access-control-temporary-managed-credentials)\.

If you are not using an EC2 environment, you must manually store your credentials within the environment\. To do this, follow the instructions in [Calling AWS services from an environment in AWS Cloud9](credentials.md), and then return to this topic\.

## Step 3: Run basic commands with the AWS CLI or the aws\-shell in your environment<a name="sample-aws-cli-run"></a>

In this step, you use the AWS CLI or the aws\-shell in your environment to create a bucket in Amazon S3, list your available buckets, and then delete the bucket\.

1. If you want to use the aws\-shell but haven't started it yet, start the aws\-shell by running the `aws-shell` command\. The `aws>` prompt is displayed\.

1. Create a bucket\. Run the ** `aws s3 mb` ** command with the AWS CLI or ** `s3 mb` ** command with the aws\-shell, supplying the name of the bucket to create\. In this example, we use a bucket named `cloud9-123456789012-bucket`, where `123456789012` is your AWS account ID\. If you use a different name, substitute it throughout this step\.

   ```
   aws s3 mb s3://cloud9-123456789012-bucket # For the AWS CLI.
   s3 mb s3://cloud9-123456789012-bucket     # For the aws-shell.
   ```
**Note**  
Bucket names must be unique across all of AWS, not just your AWS account\. The preceding suggested bucket name can help you come up with a unique bucket name\. If you get a message that contains the error `BucketAlreadyExists`, you must run the command again with a different bucket name\.

1. List your available buckets\. Run the ** `aws s3 ls` ** command with the AWS CLI or the ** `s3 ls` ** command with the aws\-shell\. A list of your available buckets is displayed\.

1. Delete the bucket\. Run the ** `aws s3 rb` ** command with the AWS CLI or the ** `s3 rb` ** command with the aws\-shell, supplying the name of the bucket to delete\.

   ```
   aws s3 rb s3://cloud9-123456789012-bucket # For the AWS CLI.
   s3 rb s3://cloud9-123456789012-bucket     # For the aws-shell.
   ```

   To confirm whether the bucket was deleted, run the ** `aws s3 ls` ** command again with the AWS CLI or the ** `s3 ls` ** command again with the aws\-shell\. The name of the bucket that was deleted should no longer appear in the list\.
**Note**  
You don't have to delete the bucket if you want to keep using it\. For more information, see [Add an Object to a Bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/PuttingAnObjectInABucket.html) in the *Amazon Simple Storage Service Getting Started Guide*\. See also [s3 commands](https://docs.aws.amazon.com/cli/latest/reference/s3/rm.html.html) in the *AWS CLI Command Reference*\. \(Remember, if you don't delete the bucket, it might result in ongoing charges to your AWS account\.\)

To continue experimenting with the AWS CLI, see [Working with Amazon Web Services](https://docs.aws.amazon.com/cli/latest/userguide/chap-working-with-services.html) in the *AWS Command Line Interface User Guide* as well as the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/)\. To continue experimenting with the aws\-shell, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/), noting that you start commands without the `aws` prefix\.

## Step 4: Clean up<a name="sample-aws-cli-clean-up"></a>

If you're using the aws\-shell, you can stop using it by running the ** `.exit` ** or ** `.quit` ** command\.

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the environment\. For instructions, see [Deleting an environment in AWS Cloud9](delete-environment.md)\.