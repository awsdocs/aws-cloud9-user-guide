# Python Sample for AWS Cloud9<a name="sample-python"></a>

This sample enables you to run some Python scripts in an AWS Cloud9 development environment\.

Creating this sample might result in charges to your AWS account\. These include possible charges for services such as Amazon EC2 and Amazon S3\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/) and [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/)\.

**Topics**
+ [Prerequisites](#sample-python-prereqs)
+ [Step 1: Install Required Tools](#sample-python-install)
+ [Step 2: Add Code](#sample-python-code)
+ [Step 3: Run the Code](#sample-python-run)
+ [Step 4: Install and Configure the AWS SDK for Python \(Boto\)](#sample-python-sdk)
+ [Step 5: Add AWS SDK Code](#sample-python-sdk-code)
+ [Step 6: Run the AWS SDK Code](#sample-python-sdk-run)
+ [Step 7: Clean Up](#sample-python-clean-up)

## Prerequisites<a name="sample-python-prereqs"></a>

Before you use this sample, be sure to meet the following requirements\.
+  **You must have an existing AWS Cloud9 EC2 development environment\.** This sample assumes you already have an EC2 environment that is connected to an Amazon EC2 instance running Amazon Linux or Ubuntu Server\. If you have a different type of environment or operating system, you might need to adapt this sample's instructions to set up related tools\. See [Creating an Environment in AWS Cloud9](create-environment.md) for details\.
+  **You have the AWS Cloud9 IDE for the existing environment already open\.** When you open an environment, AWS Cloud9 opens the IDE for that environment in your web browser\. See [Opening an Environment in AWS Cloud9](open-environment.md) for details\.

## Step 1: Install Required Tools<a name="sample-python-install"></a>

In this step, you install Python, which is required to run this sample\.

1. In a terminal session in the AWS Cloud9 IDE, confirm whether Python is already installed by running the ** `python --version` ** command\. \(To start a new terminal session, on the menu bar, choose **Window**, **New Terminal**\.\) If successful, the output contains the Python version number\. If Python is installed, skip ahead to [Step 2: Add Code](#sample-python-code)\.

1. Run the ** `yum update`** \(for Amazon Linux\) or **`apt update`** \(for Ubuntu Server\) command to help ensure the latest security updates and bug fixes are installed\.

   For Amazon Linux:

   ```
   sudo yum -y update
   ```

   For Ubuntu Server:

   ```
   sudo apt update
   ```

1. Install Python by running one or more of these ** `install` ** commands\.

   For Amazon Linux:

   ```
   sudo yum -y install python27 # Installs Python 2.7.
   sudo yum -y install python36 # Installs Python 3.6.
   ```

   For Ubuntu Server:

   ```
   sudo apt -y install python  # Installs Python 2.7.
   sudo apt -y install python3 # Installs Python 3.6.
   ```
**Note**  
If you have Python 2 and 3 installed, and you want to use Python 3 but running the ** `python --version` ** command outputs a version of Python 2, you can use Python 3 in one or more of the following ways:  
Instead of using the built\-in Python 2 runner in the IDE, use the built\-in Python 3 runner\. For more information, see [Step 3: Run the Code](#sample-python-run)\.
Instead of running the `python` command in a terminal session in the IDE, run the `python3` command instead\.
To set up the `python` command to use Python 3, use a tool such as virtualenv to create a virtual environment for Python 3, and then activate the new virtual environment\. For example, you can run commands similar to the following to create and then activate the virtual environment:  

     ```
     virtualenv --version                  # If a version number is not output, see https://virtualenv.pypa.io/en/stable/installation/.
     which python                          # If the 'python' command is aliased to something like '/usr/bin/python27', prepare to unalias it.
     unalias python                        # If the 'python' command is aliased to something like '/usr/bin/python27', unalias it.
     python --version                      # Output the current Python version, for example 'Python 2.7.12'.
     python3 --version                     # Output the current version of Python 3, for example 'Python 3.6.2'.
     which python36                        # Output the path to the python36 binary, for example '/usr/bin/python36'.
     cd ~/environment/                     # Prepare to create a virtual environment in this path.
     virtualenv -p /usr/bin/python36 vpy36 # Create a virtual environment for Python 3.6 in this path.
     source vpy36/bin/activate             # Switch to use Python 3.6 instead of Python 2.7.12 when you run the 'python --version' command.
     python --version                      # Output the current Python version, for example 'Python 3.6.2'.
     deactivate                            # If and when you are done using Python 3.6, prepare to make Python 2.7.12 active again.
     alias python=/usr/bin/python27        # Switch back to outputting '/usr/bin/python27' when you run the 'which python' command.
     ```
For more information, see [Installation](https://virtualenv.pypa.io/en/stable/installation/) and [Usage](https://virtualenv.pypa.io/en/stable/userguide/) on the virtualenv website\.

   For more information, see [Download Python](https://www.python.org/downloads/) on the Python website and [Installing Packages](https://packaging.python.org/installing/) in the *Python Packaging User Guide*\.

## Step 2: Add Code<a name="sample-python-code"></a>

In the AWS Cloud9 IDE, create a file with this content, and save the file with the name `hello.py`\. \(To create a file, on the menu bar, choose **File**, **New File**\. To save the file, choose **File**, **Save**\.\)

```
import sys

print('Hello, World!')

print('The sum of 2 and 3 is 5.')

sum = int(sys.argv[1]) + int(sys.argv[2])

print('The sum of {0} and {1} is {2}.'.format(sys.argv[1], sys.argv[2], sum))
```

**Note**  
The preceding code doesn't rely on any custom Python modules or packages\. However, if you ever import custom Python modules or packages, and you want AWS Cloud9 to use those modules or packages to do code completion as you type, turn on the **Project, Python Support, Enable Python code completion** setting in **Preferences**, and then add the paths to those modules or packages to the **Project, Python Support, PYTHONPATH** setting\. \(To view and change your preferences, choose **AWS Cloud9, Preferences** on the menu bar\.\)

## Step 3: Run the Code<a name="sample-python-run"></a>

1. In the AWS Cloud9 IDE, on the menu bar, choose **Run**, **Run Configurations**, **New Run Configuration**\.

1. On the **\[New\] \- Idle** tab, choose **Runner: Auto**, and then choose **Python 2** or **Python 3**, depending on which version of Python you want to use\.
**Note**  
If **Python 2** or **Python 3** isn't available, you can create a custom runner for the version of Python that is installed in your environment\.  
On the **\[New\] \- Idle** tab, choose **Runner: Auto**, and then choose **New Runner**\.
On the **My Runner\.run** tab, replace the tab's contents with this code\.  

      ```
      {
        "cmd" : ["python", "$file", "$args"],
        "info" : "Running $project_path$file_name...",
        "selector" : "source.py"
      }
      ```
Choose **File**, **Save As** on the menu bar, and save the file as `Python.run` in the `/.c9/runners` folder\.
On the **\[New\] \- Idle** tab, choose **Runner: Auto**, and then choose **Python**\.
Choose the **hello\.py** tab to make it active\.
To use a specific version of Python that is installed in your environment, change `python` to the path to the Python executable in the preceding custom runner definition \(for example, `/usr/bin/python27`, `/usr/bin/python36`, or similar\)\.

1. For **Command**, type `hello.py 5 9`\. In the code, `5` represents `sys.argv[1]`, and `9` represents `sys.argv[2]`\.

1. Choose the **Run** button, and compare your output\.

   ```
   Hello, World!
   The sum of 2 and 3 is 5.
   The sum of 5 and 9 is 14.
   ```

## Step 4: Install and Configure the AWS SDK for Python \(Boto\)<a name="sample-python-sdk"></a>

You can enhance this sample to use the AWS SDK for Python \(Boto\) to create an Amazon S3 bucket, list your available buckets, and then delete the bucket you just created\.

In this step, you install and configure the AWS SDK for Python \(Boto\), which provides a convenient way to interact with AWS services, such as Amazon S3, from your Python code\. Before you can install the AWS SDK for Python \(Boto\), you must install pip\. After you install the AWS SDK for Python \(Boto\), you must set up credentials management in your environment\. The AWS SDK for Python \(Boto\) needs these credentials to interact with AWS services\.

**To install pip**

1. In the AWS Cloud9 IDE, confirm whether pip is already installed by running the ** `pip --version` ** command\. If successful, the output contains the pip version number\. Otherwise, an error message should be output\. If pip is installed, skip ahead to the next procedure, "To install the AWS SDK for Python \(Boto\)\."

1. To install pip, run these commands, one at a time\.

   ```
   curl -O https://bootstrap.pypa.io/get-pip.py # Get the install script.
   sudo python get-pip.py                       # Install pip.
   rm get-pip.py                                # Delete the install script.
   ```

   For more information, see [pip Installation](https://pip.pypa.io/en/stable/installing/) on the pip website\.

### To install the AWS SDK for Python \(Boto\)<a name="sample-python-sdk-install-sdk"></a>

After you install pip, use Python to run the ** `pip install` ** command\.

```
sudo python -m pip install boto3
```

For more information, see the "Installation" section of [Quickstart](http://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) in *AWS SDK for Python \(Boto 3\) Getting Started*\.

### To set up credentials management in your environment<a name="sample-python-sdk-credentials"></a>

Each time you use the AWS SDK for Python \(Boto\) to call an AWS service, you must provide a set of credentials with the call\. These credentials determine whether the AWS SDK for Python \(Boto\) has the appropriate permissions to make that call\. If the credentials don't cover the appropriate permissions, the call will fail\.

In this step, you store your credentials within the environment\. To do this, follow the instructions in [Calling AWS Services from an Environment in AWS Cloud9](credentials.md), and then return to this topic\.

For additional information, see [Credentials](http://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html) in *AWS SDK for Python \(Boto 3\) Getting Started*\.

## Step 5: Add AWS SDK Code<a name="sample-python-sdk-code"></a>

In this step, you add some more code, this time to interact with Amazon S3 to create a bucket, list your available buckets, and then delete the bucket you just created\. You will run this code later\.

In the AWS Cloud9 IDE, create a file with this content, and save the file with the name `s3.py`\.

```
import boto3
import sys
import botocore

if len(sys.argv) < 3:
  print('Usage: python s3.py <the bucket name> <the AWS Region to use>\n' +
    'Example: python s3.py my-test-bucket us-east-2')
  sys.exit()

bucket_name = sys.argv[1]
region = sys.argv[2]

s3 = boto3.client(
  's3',
  region_name = region
)

# Lists all of your available buckets in this AWS Region.
def list_my_buckets(s3):
  resp = s3.list_buckets()

  print('My buckets now are:\n')

  for bucket in resp['Buckets']:
    print(bucket['Name'])

  return

list_my_buckets(s3)

# Create a new bucket.
try:
  print("\nCreating a new bucket named '" + bucket_name + "'...\n")
  s3.create_bucket(Bucket = bucket_name,
    CreateBucketConfiguration = {
      'LocationConstraint': region
    }
  )
except botocore.exceptions.ClientError as e:
  if e.response['Error']['Code'] == 'BucketAlreadyExists':
    print("Cannot create the bucket. A bucket with the name '" +
      bucket_name + "' already exists. Exiting.")
  sys.exit()

list_my_buckets(s3)

# Delete the bucket you just created.
print("\nDeleting the bucket named '" + bucket_name + "'...\n")
s3.delete_bucket(Bucket = bucket_name)

list_my_buckets(s3)
```

## Step 6: Run the AWS SDK Code<a name="sample-python-sdk-run"></a>

1. On the menu bar, choose **Run**, **Run Configurations**, **New Run Configuration**\.

1. On the **\[New\] \- Idle** tab, choose **Runner: Auto**, and then choose **Python 2** or **Python 3**, depending on which version of Python you want to use and is installed in your environment\.

1. For **Command**, type `s3.py my-test-bucket us-east-2`, where `my-test-bucket` is the name of the bucket you want to create and then delete, and `us-east-2` is the ID of the AWS Region you want to create the bucket in\. For more IDs, see [Amazon Simple Storage Service \(Amazon S3\)](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) in the *Amazon Web Services General Reference*\.
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

## Step 7: Clean Up<a name="sample-python-clean-up"></a>

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the environment\. For instructions, see [Deleting an Environment in AWS Cloud9](delete-environment.md)\.