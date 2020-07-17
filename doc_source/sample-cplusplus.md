# C\+\+ Sample for AWS Cloud9<a name="sample-cplusplus"></a>

This sample enables you to run some C\+\+ code in an AWS Cloud9 development environment\.

Creating this sample might result in charges to your AWS account\. These include possible charges for services such as Amazon EC2 and Amazon S3\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/) and [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/)\.

**Topics**
+ [Prerequisites](#sample-cplusplus-prereqs)
+ [Step 1: Install Required Tools](#sample-cplusplus-install)
+ [Step 2: Add Code](#sample-cplusplus-code)
+ [Step 3: Run the Code](#sample-cplusplus-run)
+ [Step 4: Install and Configure the AWS SDK for C\+\+](#sample-cplusplus-sdk)
+ [Step 5: Add AWS SDK Code](#sample-cplusplus-sdk-code)
+ [Step 6: Build and Run the AWS SDK Code](#sample-cplusplus-sdk-run)
+ [Step 7: Clean Up](#sample-cplusplus-clean-up)

## Prerequisites<a name="sample-cplusplus-prereqs"></a>

Before you use this sample, be sure to meet the following requirements\.
+  **You must have an existing AWS Cloud9 EC2 development environment\.** This sample assumes you already have an EC2 environment that is connected to an Amazon EC2 instance running Amazon Linux or Ubuntu Server\. If you have a different type of environment or operating system, you might need to adapt this sample's instructions to set up related tools\. See [Creating an Environment in AWS Cloud9](create-environment.md) for details\.
+  **You have the AWS Cloud9 IDE for the existing environment already open\.** When you open an environment, AWS Cloud9 opens the IDE for that environment in your web browser\. See [Opening an environment in AWS Cloud9](open-environment.md) for details\.

## Step 1: Install Required Tools<a name="sample-cplusplus-install"></a>

In this step, you install and configure the [GNU Complier Collection \(GCC\)](https://gcc.gnu.org/), which is required to run this sample\.

1. In a terminal session in the AWS Cloud9 IDE, confirm whether GCC is already installed by running the ** `g++ --version` ** command\. \(To start a new terminal session, on the menu bar, choose **Window**, **New Terminal**\.\) If successful, the output contains the GCC version number\. Otherwise, an error message should be output\. If GCC is installed, skip ahead to [Step 2: Add Code](#sample-cplusplus-code)\.

1. Run the ** `yum update` ** command \(on Amazon Linux\) or the ** `apt update` ** command \(on Ubuntu Server\) to help ensure the latest security updates and bug fixes are installed\.

   For Amazon Linux:

   ```
   sudo yum -y update
   ```

   For Ubuntu Server:

   ```
   sudo apt update
   ```

1. To install GCC, run the ** `yum install` ** command \(for Amazon Linux\) or the ** `apt install` ** command \(for Ubuntu Server\)\.

   For Amazon Linux:

   ```
   sudo yum -y install gcc-c++
   ```

   For Ubuntu Server:

   ```
   sudo apt install -y g++
   ```

1. Confirm that GCC is now successfully installed by running the ** `g++ --version` ** command\. If successful, the output contains the GCC version number\.

## Step 2: Add Code<a name="sample-cplusplus-code"></a>

In the AWS Cloud9 IDE, create a file with this content, and save the file with the name `hello.cpp`\. \(To create a file, on the menu bar, choose **File**, **New File**\. To save the file, choose **File**, **Save**\.\)

```
#include <iostream>
#include <stdlib.h>

int main( int argc, char *argv[] )
{
  std::cout << "Hello, World!\n";
  std::cout << "The sum of 2 and 3 is 5.\n";

  if (argc > 2) {
    std::cout << "The sum of " << argv[1] << " and " << argv[2]
      << " is " << atoi(argv[1]) + atoi(argv[2]) << ".\n";
  }

  return 0;
}
```

## Step 3: Run the Code<a name="sample-cplusplus-run"></a>

1. Compile the `hello.cpp` source code into an object module, and then link the object module into a program named `hello`\. Do this by choosing **Run**, **Build System**, **G\+\+** followed by **Run**, **Build** on the menu bar\.
**Note**  
If **G\+\+** is not available, you can create a custom builder for G\+\+\.  
Choose **Run**, **Build System**, **New Build System** on the menu bar\.
On the **My Builder\.build** tab, replace the tab's contents with this code\.  

      ```
      {
        "cmd": [ "g++", "-o", "$file_base_name", "$file_name" ],
        "info": "Compiling $file_name and linking to $file_base_name...",
        "selector": "source.cpp"
      }
      ```
Choose **File**, **Save As** on the menu bar, and then save the file as `G++.build` in the `/.c9/builders` folder\.
Choose the **hello\.cpp** tab to make it active\.
Choose **Run**, **Build System**, **G\+\+** followed by **Run**, **Build**\.

1. In the AWS Cloud9 IDE, run the code by choosing **Run**, **Run Configurations**, **New Run Configuration** on the menu bar\.

1. On the **\[New\] \- Idle** tab, choose **Runner: Auto**, and then choose **C\+\+**\.
**Note**  
If **C\+\+** isn't available, you can create a custom runner for C\+\+\.  
On the **\[New\] \- Idle** tab, choose **Runner: Auto**, and then choose **New Runner**\.
On the **My Runner\.run** tab, replace the tab's contents with this code\.  

      ```
      {
        "cmd" : ["$file", "$args"],
        "info" : "Running $project_path$file_name...",
        "selector" : "source"
      }
      ```
Choose **File**, **Save As** on the menu bar, and then save the file as `C++.run` in the `/.c9/runners` folder\.
On the **\[New\] \- Idle** tab, choose **Runner: Auto**, and then choose **C\+\+**\.

1. For **Command**, type `hello 5 9`\. In the code, `5` represents `argv[1]`, and `9` represents `argv[2]`\.

1. Choose the **Run** button, and compare your output\.

   ```
   Hello, World!
   The sum of 2 and 3 is 5.
   The sum of 5 and 9 is 14.
   ```

## Step 4: Install and Configure the AWS SDK for C\+\+<a name="sample-cplusplus-sdk"></a>

You can enhance this sample to use the AWS SDK for C\+\+ to create an Amazon S3 bucket, list your available buckets, and then delete the bucket you just created\.

In this step, you install and configure the AWS SDK for C\+\+, which provides a convenient way to interact with AWS services, such as Amazon S3, from your C\+\+ code\. Before you install the AWS SDK for C\+\+, you must install some dependencies\. After you install the AWS SDK for C\+\+, you must set up credentials management in your environment\. The AWS SDK for C\+\+ needs these credentials to interact with AWS services\.

**Note**  
The following steps require your environment to be running on an Amazon EC2 instance or your own server that has at least 4 GB of RAM\.

### To install AWS SDK for C\+\+ dependencies<a name="sample-cplusplus-sdk-install-deps"></a>

From a terminal session in the AWS Cloud9 IDE, run the following command to install several packages that the AWS SDK for C\+\+ depends on to run correctly\.

For Amazon Linux:

```
sudo yum -y install libcurl-devel openssl-devel libuuid-devel cmake3
```

For Ubuntu Server:

```
sudo apt install -y libcurl4-openssl-dev libssl-dev uuid-dev zlib1g-dev libpulse-dev cmake
```

### To download and extract the AWS SDK for C\+\+ source code<a name="sample-cplusplus-sdk-download"></a>

1. Run the ** `wget` ** command, specifying the location of the AWS SDK for C\+\+ source\.

   ```
   wget https://github.com/aws/aws-sdk-cpp/archive/master.zip
   ```

1. Run the ** `unzip` ** command, specifying the name of the \.zip file you just downloaded\.

   ```
   unzip master.zip
   ```

1. Run the ** `rm` ** command to delete the \.zip file, as you no longer need it\.

   ```
   rm master.zip
   ```

### To build the AWS SDK for C\+\+<a name="sample-cplusplus-sdk-build"></a>

**Note**  
This step could take up to one or more hours to complete, depending on the computing resources available to your Amazon EC2 instance or your own server and how much of the AWS SDK for C\+\+ you choose to build\.

1. Create a folder to build the AWS SDK for C\+\+ into\.

   ```
   mkdir sdk_build
   ```

1. Switch to the folder you just created\.

   ```
   cd sdk_build
   ```

1. Prepare to build the AWS SDK for C\+\+ into this folder\.

   For Amazon Linux:

   ```
   cmake3 ../aws-sdk-cpp-master
   ```

   For Ubuntu Server:

   ```
   cmake ../aws-sdk-cpp-master
   ```
**Note**  
To build only the Amazon S3 portion of the AWS SDK for C\+\+ and its dependencies, run this command instead:  
For Amazon Linux:  

   ```
   cmake3 ../aws-sdk-cpp-master -DBUILD_ONLY="s3"
   ```
For Ubuntu Server:  

   ```
   cmake ../aws-sdk-cpp-master -DBUILD_ONLY="s3"
   ```

1. Build the AWS SDK for C\+\+ into this folder\.

   ```
   make
   ```

1. After the AWS SDK for C\+\+ successfully builds, switch to the root of your environment\.

   ```
   cd ..
   ```

### To set up credentials management in your environment<a name="sample-cplusplus-sdk-creds"></a>

Each time you use the AWS SDK for C\+\+ to call an AWS service, you must provide a set of credentials with the call\. These credentials determine whether the AWS SDK for C\+\+ has the appropriate permissions to make that call\. If the credentials don't cover the appropriate permissions, the call will fail\.

In this step, you store your credentials within the environment\. To do this, follow the instructions in [Calling AWS Services from an Environment in AWS Cloud9](credentials.md), and then return to this topic\.

For additional information, see [Providing AWS Credentials](https://docs.aws.amazon.com/sdk-for-cpp/latest/developer-guide/credentials.html) in the *AWS SDK for C\+\+ Developer Guide*\.

## Step 5: Add AWS SDK Code<a name="sample-cplusplus-sdk-code"></a>

In this step, you add some more code, this time to interact with Amazon S3 to create a bucket, list your available buckets, and then delete the bucket you just created\. You will run this code later\.

1. In the AWS Cloud9 IDE, create a file with this content, and save the file with the name `s3-demo.cpp` at the root \(`/`\) of your environment\.

   ```
   #include <aws/core/Aws.h>
   #include <aws/s3/S3Client.h>
   #include <aws/s3/model/Bucket.h>
   #include <aws/s3/model/CreateBucketConfiguration.h>
   #include <aws/s3/model/CreateBucketRequest.h>
   #include <aws/s3/model/DeleteBucketRequest.h>
   #include <string>
   
   bool ListMyBuckets(Aws::S3::S3Client s3_client);
   bool CreateMyBucket(Aws::S3::S3Client s3_client, Aws::String bucket_name,
     Aws::S3::Model::BucketLocationConstraint region);
   bool DeleteMyBucket(Aws::S3::S3Client s3_client, Aws::String bucket_name);
   void Cleanup(Aws::SDKOptions options);
   
   int main(int argc, char** argv) {
   
     if (argc < 3) {
       std::cout << "Usage: ./s3-demo <the bucket name> <the AWS Region to use>" << std::endl
                 << "Example: ./s3-demo my-test-bucket us-west-1" << std::endl;
       return false;
     }
   
     Aws::String bucket_name = argv[1];
     Aws::Client::ClientConfiguration client_configuration;
     Aws::S3::Model::BucketLocationConstraint region;
   
     // Set the AWS Region to use, based on the user's AWS Region input ID.
     if (strcmp(argv[2], "ap-northeast-1") == 0) {
       client_configuration.region = Aws::Region::AP_NORTHEAST_1;
       region = Aws::S3::Model::BucketLocationConstraint::ap_northeast_1;
     } else if (strcmp(argv[2], "ap-northeast-2") == 0) {
       client_configuration.region = Aws::Region::AP_NORTHEAST_2;
       region = Aws::S3::Model::BucketLocationConstraint::ap_northeast_2;
     } else if (strcmp(argv[2], "ap-south-1") == 0) {
       client_configuration.region = Aws::Region::AP_SOUTH_1;
       region = Aws::S3::Model::BucketLocationConstraint::ap_south_1;
     } else if (strcmp(argv[2], "ap-southeast-1") == 0) {
       client_configuration.region = Aws::Region::AP_SOUTHEAST_1;
       region = Aws::S3::Model::BucketLocationConstraint::ap_southeast_1;
     } else if (strcmp(argv[2], "ap-southeast-2") == 0) {
       client_configuration.region = Aws::Region::AP_SOUTHEAST_2;
       region = Aws::S3::Model::BucketLocationConstraint::ap_southeast_2;
     } else if (strcmp(argv[2], "cn-north-1") == 0) {
       client_configuration.region = Aws::Region::CN_NORTH_1;
       region = Aws::S3::Model::BucketLocationConstraint::cn_north_1;
     } else if (strcmp(argv[2], "eu-central-1") == 0) {
       client_configuration.region = Aws::Region::EU_CENTRAL_1;
       region = Aws::S3::Model::BucketLocationConstraint::eu_central_1;
     } else if (strcmp(argv[2], "eu-west-1") == 0) {
       client_configuration.region = Aws::Region::EU_WEST_1;
       region = Aws::S3::Model::BucketLocationConstraint::eu_west_1;
     } else if (strcmp(argv[2], "sa-east-1") == 0) {
       client_configuration.region = Aws::Region::SA_EAST_1;
       region = Aws::S3::Model::BucketLocationConstraint::sa_east_1;
     } else if (strcmp(argv[2], "us-west-1") == 0) {
       client_configuration.region = Aws::Region::US_WEST_1;
       region = Aws::S3::Model::BucketLocationConstraint::us_west_1;
     } else if (strcmp(argv[2], "us-west-2") == 0) {
       client_configuration.region = Aws::Region::US_WEST_2;
       region = Aws::S3::Model::BucketLocationConstraint::us_west_2;
     } else {
       std::cout << "Unrecognized AWS Region ID '" << argv[2] << "'" << std::endl;
       return false;
     }
   
     Aws::SDKOptions options;
   
     Aws::InitAPI(options);
     {
       Aws::S3::S3Client s3_client(client_configuration);
   
       if (!ListMyBuckets(s3_client)) {
         Cleanup(options);
       }
   
       if (!CreateMyBucket(s3_client, bucket_name, region)) {
         Cleanup(options);
       }
   
       if (!ListMyBuckets(s3_client)) {
         Cleanup(options);
       }
   
       if (!DeleteMyBucket(s3_client, bucket_name)) {
         Cleanup(options);
       }
   
       if (!ListMyBuckets(s3_client)) {
         Cleanup(options);
       }
     }
     Cleanup(options);
   }
   
   // List all of your available buckets.
   bool ListMyBuckets(Aws::S3::S3Client s3_client) {
     auto outcome = s3_client.ListBuckets();
   
     if (outcome.IsSuccess()) {
       std::cout << "My buckets now are:" << std::endl << std::endl;
   
       Aws::Vector<Aws::S3::Model::Bucket> bucket_list =
         outcome.GetResult().GetBuckets();
   
       for (auto const &bucket: bucket_list) {
         std::cout << bucket.GetName() << std::endl;
       }
   
       std::cout << std::endl;
       return true;
     } else {
       std::cout << "ListBuckets error: "
                 << outcome.GetError().GetExceptionName() << std::endl
                 << outcome.GetError().GetMessage() << std::endl;
   
       return false;
     }
   }
   
   // Create a bucket in this AWS Region.
   bool CreateMyBucket(Aws::S3::S3Client s3_client, Aws::String bucket_name,
       Aws::S3::Model::BucketLocationConstraint region) {
     std::cout << "Creating a new bucket named '"
               << bucket_name
               << "'..." << std::endl << std::endl;
   
     Aws::S3::Model::CreateBucketConfiguration bucket_configuration;
     bucket_configuration.WithLocationConstraint(region);
   
     Aws::S3::Model::CreateBucketRequest bucket_request;
     bucket_request.WithBucket(bucket_name).WithCreateBucketConfiguration(bucket_configuration);
   
     auto outcome = s3_client.CreateBucket(bucket_request);
   
     if (outcome.IsSuccess()) {
       return true;
     } else {
       std::cout << "CreateBucket error: "
                 << outcome.GetError().GetExceptionName() << std::endl
                 << outcome.GetError().GetMessage() << std::endl;
   
       return false;
     }
   }
   
   // Delete the bucket you just created.
   bool DeleteMyBucket(Aws::S3::S3Client s3_client, Aws::String bucket_name) {
     std::cout << "Deleting the bucket named '"
               << bucket_name
               << "'..." << std::endl << std::endl;
   
     Aws::S3::Model::DeleteBucketRequest bucket_request;
     bucket_request.WithBucket(bucket_name);
   
     auto outcome = s3_client.DeleteBucket(bucket_request);
   
     if (outcome.IsSuccess()) {
       return true;
     } else {
       std::cout << "DeleteBucket error: "
                 << outcome.GetError().GetExceptionName() << std::endl
                 << outcome.GetError().GetMessage() << std::endl;
   
       return false;
     }
   }
   
   void Cleanup(Aws::SDKOptions options) {
     Aws::ShutdownAPI(options);
   }
   ```

1. Create a file with this content, and save the file with the name `CMakeLists.txt` at the root \(`/`\) of your environment\. This file enables you to build your code into an executable file\.

   ```
   # A minimal CMakeLists.txt file for the AWS SDK for C++.
   
   # The minimum version of CMake that will work.
   cmake_minimum_required(VERSION 2.8)
   
   # The project name.
   project(s3-demo)
   
   # Locate the AWS SDK for C++ package.
   # Requires that you build with:
   #   -Daws-sdk-cpp_DIR=/path/to/sdk_build
   # or export/set:
   #   CMAKE_PREFIX_PATH=/path/to/sdk_build
   find_package(aws-sdk-cpp)
   
   # Link to the AWS SDK for C++ shared libraries.
   add_definitions(-DUSE_IMPORT_EXPORT)
   
   # The executable name and its source files.
   add_executable(s3-demo s3-demo.cpp)
   
   # The libraries used by your executable.
   target_link_libraries(s3-demo aws-cpp-sdk-s3)
   ```

## Step 6: Build and Run the AWS SDK Code<a name="sample-cplusplus-sdk-run"></a>

1. In the terminal, prepare to build your source code\.

   For Amazon Linux:

   ```
   cmake3 -Daws-sdk-cpp_DIR=sdk_build .
   ```

   For Ubuntu Server:

   ```
   cmake -Daws-sdk-cpp_DIR=sdk_build .
   ```

1. Build your source code\.

   ```
   make
   ```

1. Run the code by choosing **Run**, **Run Configurations**, **New Run Configuration** on the menu bar\.

1. On the **\[New\] \- Idle** tab, choose **Runner: Auto**, and then choose **C\+\+**\.

1. For **Command**, type `s3-demo my-test-bucket us-east-2`, where `my-test-bucket` is the name of the bucket you want to create and then delete, and `us-east-2` is the ID of the AWS Region you want to create the bucket in\. For more IDs, see [Amazon Simple Storage Service \(Amazon S3\)](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) in the *Amazon Web Services General Reference*\.
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

## Step 7: Clean Up<a name="sample-cplusplus-clean-up"></a>

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the environment\. For instructions, see [Deleting an Environment in AWS Cloud9](delete-environment.md)\.