# C\+\+ sample for AWS Cloud9<a name="sample-cplusplus"></a>

This sample allows you to run C\+\+ code in an AWS Cloud9 development environment\. The code also uses resources provided by the [AWS SDK for C\+\+](https://docs.aws.amazon.com/sdk-for-cpp/latest/developer-guide/), a modularized, cross\-platform, open\-source library you can use to connect to Amazon Web Services\.

Creating this sample might result in charges to your AWS account\. These include possible charges for services such as Amazon EC2 and Amazon S3\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/) and [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/)\.

**Topics**
+ [Prerequisites](#sample-cplusplus-prereqs)
+ [Step 1: Install g\+\+ and required dev packages](#sample-cplusplus-install)
+ [Step 2: Install CMake](#install-cmake)
+ [Step 3: Obtain and build the SDK for C\+\+](#install-cmake)
+ [Step 4: Create C\+\+ and CMakeLists files](#sample-cplusplus-sdk-code)
+ [Step 5: Build and run the C\+\+ code](#build-and-run-cpp)
+ [Step 6: Clean up](#sample-cplusplus-clean-up)

## Prerequisites<a name="sample-cplusplus-prereqs"></a>

Before you use this sample, make sure your setup meets the following requirements:
+  **You must have an existing AWS Cloud9 EC2 development environment\.** This sample assumes you already have an EC2 environment that is connected to an Amazon EC2 instance running Amazon Linux or Ubuntu Server\. If you have a different type of environment or operating system, you might need to adapt this sample's instructions to set up related tools\. See [Creating an environment in AWS Cloud9](create-environment.md) for details\.
+  **You have the AWS Cloud9 IDE for the existing environment already open\.** When you open an environment, AWS Cloud9 opens the IDE for that environment in your web browser\. See [Opening an environment in AWS Cloud9](open-environment.md) for details\.

## Step 1: Install g\+\+ and required dev packages<a name="sample-cplusplus-install"></a>

To build and run a C\+\+ application, you need a utility such as `g++`, which is a C\+\+ compiler provided by the [GNU Complier Collection \(GCC\)](https://gcc.gnu.org/)\.

You also need to add header files \(`-dev` packages\) for `libcurl`, `libopenssl`, `libuuid`, `zlib`, and, optionally, `libpulse` for Amazon Polly support\. 

The process of installing development tools varies slightly depending on whether you're using an Amazon Linux/Amazon Linux 2 instance or an Ubuntu instance\.

------
#### [ Amazon Linux\-based systems ]

You can check if you already have `gcc` installed by running the following command in the AWS Cloud9 terminal:

```
g++ --version
```

If `g++` isn't installed, you can easily install it part of the package group called "Development Tools"\. These tools are added to an instance with the `yum groupinstall` command:

```
sudo yum groupinstall "Development Tools"
```

Run `g++ --version` again to confirm that the compiler has been installed\.

Now install the packages for the required libraries using your system’s package manager: 

```
sudo yum install libcurl-devel openssl-devel libuuid-devel pulseaudio-libs-devel
```

------
#### [ Ubuntu\-based systems ]

You can check if you already have `gcc` installed by running the following command in the AWS Cloud9 terminal:

```
g++ --version
```

If gcc is not installed, you can install it on an Ubuntu\-based system by running the following commands:

```
sudo apt update
sudo apt install build-essential
sudo apt-get install manpages-dev
```

Run `g++ --version` again to confirm that the compiler has been installed\.

Now install the packages for the required libraries using your system’s package manager: 

```
sudo apt-get install libcurl4-openssl-dev libssl-dev uuid-dev zlib1g-dev libpulse-dev
```

------

## Step 2: Install CMake<a name="install-cmake"></a>

 You need to install the `cmake` tool, which automates the process of building executable files from source code\. 

1. In the IDE terminal window, run the following command to obtain the required archive:

   ```
   wget https://cmake.org/files/v3.18/cmake-3.18.0.tar.gz
   ```

1. Extract the files from the archive and navigate to the directory that contains the unpacked files:

   ```
   tar xzf cmake-3.18.0.tar.gz
   cd cmake-3.18.0
   ```

1. Next, run a bootstrap script and install `cmake` by running the following commands:

   ```
   ./bootstrap
   make
   sudo make install
   ```

1. Confirm you've installed the tool by running the following command:

   ```
   cmake --version
   ```

## Step 3: Obtain and build the SDK for C\+\+<a name="install-cmake"></a>

To set up the AWS SDK for C\+\+, you can either build the SDK yourself directly from the source or download the libraries using a package manager\. You can find details on the available options in [Getting Started Using the AWS SDK for C\+\+](https://docs.aws.amazon.com/sdk-for-cpp/latest/developer-guide/getting-started.html) in the *AWS SDK for C\+\+ Developer Guide*\. 

This sample demonstrating using `git` to clone the SDK source code and `cmake` to build the SDK for C\+\+\.

1. Clone the remote repository and get all git submodules recursively for your AWS Cloud9 environment by running the following command in the terminal:

   ```
   git clone --recurse-submodules https://github.com/aws/aws-sdk-cpp
   ```

1. Navigate to the new `aws-sdk-cpp` directory, create a sub\-directory to build the AWS SDK for C\+\+ into, and then navigate to that:

   ```
   cd aws-sdk-cpp
   mkdir sdk_build
   cd sdk_build
   ```

1. 
**Note**  
To save time, this step builds only the Amazon S3 portion of the AWS SDK for C\+\+\. If you want to build the complete SDK, omit the `-DBUILD_ONLY=s3` from the `cmake` command\.  
Building the complete SDK for C\+\+ can take more than an hour to complete, depending on the computing resources available to your Amazon EC2 instance or your own server\.

   Use `cmake` to build the Amazon S3 portion of the SDK for C\+\+ into the `sdk_build` directory by running the following command:

   ```
   cmake .. -DBUILD_ONLY=s3
   ```

1. Now run the `make install` command so that the built SDK can be accessed:

   ```
   sudo make install
   cd ..
   ```

## Step 4: Create C\+\+ and CMakeLists files<a name="sample-cplusplus-sdk-code"></a>

In this step, you create a `C++` file that allows users of the project to interact with Amazon S3 buckets\.

You also create a `CMakeLists.txt` file that provides instructions that are used by `cmake` to build your C\+\+ library\.

1. In the AWS Cloud9 IDE, create a file with this content, and save the file with the name `s3-demo.cpp` at the root \(`/`\) of your environment\.

   ```
   #include <iostream>
   #include <aws/core/Aws.h>
   #include <aws/s3/S3Client.h>
   #include <aws/s3/model/Bucket.h>
   #include <aws/s3/model/CreateBucketConfiguration.h>
   #include <aws/s3/model/CreateBucketRequest.h>
   #include <aws/s3/model/DeleteBucketRequest.h>
   
   // Look for a bucket among all currently available Amazon S3 buckets.
   bool FindTheBucket(const Aws::S3::S3Client& s3Client,
       const Aws::String& bucketName) {
   
       Aws::S3::Model::ListBucketsOutcome outcome = s3Client.ListBuckets();
   
       if (outcome.IsSuccess()) {
   
           std::cout << "Looking for a bucket named '" << bucketName << "'..." 
               << std::endl << std::endl;
   
           Aws::Vector<Aws::S3::Model::Bucket> bucket_list =
               outcome.GetResult().GetBuckets();
   
           for (Aws::S3::Model::Bucket const& bucket : bucket_list) 
           {
               if (bucket.GetName() == bucketName)
               {
                   std::cout << "Found the bucket." << std::endl << std::endl; 
   
                   return true;
               }
           }
   
           std::cout << "Could not find the bucket." << std::endl << std::endl;
   
           return true;
       }
       else {
           std::cout << "ListBuckets error: "
               << outcome.GetError().GetMessage() << std::endl;
       }
   
       return false;
   }
   
   // Create an Amazon S3 bucket.
   bool CreateTheBucket(const Aws::S3::S3Client& s3Client, 
       const Aws::String& bucketName) {
   
       std::cout << "Creating a bucket named '"
           << bucketName << "'..." << std::endl << std::endl;
   
       Aws::S3::Model::CreateBucketRequest request;
       request.SetBucket(bucketName);
   
       Aws::S3::Model::CreateBucketOutcome outcome = 
           s3Client.CreateBucket(request);
   
       if (outcome.IsSuccess()) {
           std::cout << "Bucket created." << std::endl << std::endl;
   
           return true;
       }
       else {
           std::cout << "CreateBucket error: "
               << outcome.GetError().GetMessage() << std::endl;
   
           return false;
       }
   }
   
   // Delete an existing Amazon S3 bucket.
   bool DeleteTheBucket(const Aws::S3::S3Client& s3Client, 
       const Aws::String& bucketName) {
   
       std::cout << "Deleting the bucket named '"
           << bucketName << "'..." << std::endl << std::endl;
   
       Aws::S3::Model::DeleteBucketRequest request;
       request.SetBucket(bucketName);
   
       Aws::S3::Model::DeleteBucketOutcome outcome = 
           s3Client.DeleteBucket(request);
   
       if (outcome.IsSuccess()) {
           std::cout << "Bucket deleted." << std::endl << std::endl;
   
           return true;
       }
       else {
           std::cout << "DeleteBucket error: "
               << outcome.GetError().GetMessage() << std::endl;
   
           return false;
       }
   }
   
   // Create an Amazon S3 bucket and then delete it. 
   // Before and after creating the bucket, and then after deleting the bucket, 
   // try to determine whether that bucket still exists. 
   int main(int argc, char* argv[]) {
   
       if (argc < 3) {
           std::cout << "Usage: s3-demo <bucket name> <AWS Region>" << std::endl
               << "Example: s3-demo my-bucket us-east-1" << std::endl;
           return false;
       }
   
       Aws::SDKOptions options;
       Aws::InitAPI(options);
       {
           Aws::String bucket_name = argv[1];
           Aws::String region = argv[2];
   
           Aws::Client::ClientConfiguration config;
   
           config.region = region;
   
           Aws::S3::S3Client s3_client(config);
   
           if (!FindTheBucket(s3_client, bucket_name)) {
               return 1;
           }
   
           if (!CreateTheBucket(s3_client, bucket_name)) {
               return 1;
           }
   
           if (!FindTheBucket(s3_client, bucket_name)) {
               return 1;
           }
   
           if (!DeleteTheBucket(s3_client, bucket_name)) {
               return 1;
           }
   
           if (!FindTheBucket(s3_client, bucket_name)) {
               return 1;
           }
       }
       Aws::ShutdownAPI(options);
   
       return 0;
   }
   ```

1. Create a second file with this content, and save the file with the name `CMakeLists.txt` at the root \(`/`\) of your environment\. This file enables you to build your code into an executable file\.

   ```
   # A minimal CMakeLists.txt file for the AWS SDK for C++.
   
   # The minimum version of CMake that will work.
   cmake_minimum_required(VERSION 2.8)
   
   # The project name.
   project(s3-demo)
   
   # Locate the AWS SDK for C++ package.
   set(AWSSDK_ROOT_DIR, "/usr/local/")
   set(BUILD_SHARED_LIBS ON)
   find_package(AWSSDK REQUIRED COMPONENTS s3)
   
   # The executable name and its source files.
   add_executable(s3-demo s3-demo.cpp)
   
   # The libraries used by your executable.
   target_link_libraries(s3-demo ${AWSSDK_LINK_LIBRARIES})
   ```

## Step 5: Build and run the C\+\+ code<a name="build-and-run-cpp"></a>

1. In the root directory of your environment in which you've saved the `s3-demo.cpp` and `CMakeLists.txt`, run `cmake` to build your project:

   ```
   cmake . 
   make
   ```

1. You can now run your program from the command line\. In the following command, replace `my-unique-bucket-name` with a unique name for the Amazon S3 bucket and, if necessary, replace `us-east-1` with the identifier of another AWS Region where you want to create a bucket\.

   ```
   ./s3-demo my-unique-bucket-name us-east-1
   ```

   If the program runs successfully, output similar to the following is returned: 

   ```
   Looking for a bucket named 'my-unique-bucket-name'...
   
   Could not find the bucket.
   
   Creating a bucket named 'my-unique-bucket-name'...
   
   Bucket created.
   
   Looking for a bucket named 'my-unique-bucket-name'...
   
   Found the bucket.
   
   Deleting the bucket named 'my-unique-bucket-name'...
   
   Bucket deleted.
   
   Looking for a bucket named 'my-unique-bucket-name'...
   
   Could not find the bucket.
   ```

## Step 6: Clean up<a name="sample-cplusplus-clean-up"></a>

To prevent ongoing charges to your AWS account after you're finished with this sample, delete the environment\. For instructions, see [Deleting an environment in AWS Cloud9](delete-environment.md)\.