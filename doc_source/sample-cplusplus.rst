.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _sample-cplusplus:

########################
C++ Sample for |AC9long|
########################

.. meta::
    :description:
        Provides a hands-on sample that you can use to experiment with C++ in AWS Cloud9.

This sample enables you to run some C++ code in an |envfirst|.


Creating this sample might result in charges to your AWS account. These include possible charges for services such as |EC2| and |S3|. For more information, see
`Amazon EC2 Pricing <https://aws.amazon.com/ec2/pricing/>`_ and `Amazon S3 Pricing <https://aws.amazon.com/s3/pricing/>`_.

* :ref:`sample-cplusplus-prereqs`
* :ref:`sample-cplusplus-install`
* :ref:`sample-cplusplus-code`
* :ref:`sample-cplusplus-run`
* :ref:`sample-cplusplus-sdk`
* :ref:`sample-cplusplus-sdk-code`
* :ref:`sample-cplusplus-sdk-run`
* :ref:`sample-cplusplus-clean-up`

.. _sample-cplusplus-prereqs:

Prerequisites
=============

.. include:: _sample-prereqs.txt

.. _sample-cplusplus-install:

Step 1: Install Required Tools
==============================

In this step, you install and configure the `GNU Complier Collection (GCC) <https://gcc.gnu.org/>`_, which is required to run this sample.

#. In a terminal session in the |AC9IDE|, confirm whether GCC is already installed by running the :command:`g++ --version` command. (To start a new terminal session,
   on the menu bar, choose :menuselection:`Window, New Terminal`.) If successful, the output contains the GCC version number. Otherwise, an error message should be output.
   If GCC is installed, skip ahead to :ref:`sample-cplusplus-code`.
#. Run the :command:`yum update` command to help ensure the latest security updates and bug fixes are installed.

   .. code-block:: sh

      sudo yum -y update

#. To install GCC, run the :command:`yum install` command.

   .. code-block:: sh

      sudo yum -y install gcc-c++

#. Confirm that GCC is now successfully installed by running the :command:`g++ --version` command. If successful, the output contains the GCC version number.

.. _sample-cplusplus-code:

Step 2: Add Code
================

In the |AC9IDE|, create a file with this content, and save the file with the name :file:`hello.cpp`.
(To create a file, on the menu bar, choose :menuselection:`File, New File`. To save the file, choose :menuselection:`File, Save`.)

.. code-block:: cpp

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

.. _sample-cplusplus-run:

Step 3: Run the Code
====================

#. Compile the :file:`hello.cpp` source code into an object module, and then link the object module into a program named :file:`hello`.
   Do this by choosing :menuselection:`Run, Build System, G++` followed by :menuselection:`Run, Build` on the menu bar.

   .. note:: If :guilabel:`G++` is not available, you can create a custom builder for G++.

      #. Choose :menuselection:`Run, Build System, New Build System` on the menu bar.
      #. On the :guilabel:`My Builder.build` tab, replace the tab's contents with this code.

         .. code-block:: json

            {
              "cmd": [ "g++", "-o", "$file_base_name", "$file_name" ],
              "info": "Compiling $file_name and linking to $file_base_name...",
              "selector": "source.cpp"
            }

      #. Choose :menuselection:`File, Save As` on the menu bar, and then save the file as :file:`G++.build`
         in the :file:`/.c9/builders` folder.
      #. Choose the :guilabel:`hello.cpp` tab to make it active.
      #. Choose :menuselection:`Run, Build System, G++` followed by :menuselection:`Run, Build`.

#. In the |AC9IDE|, run the code by choosing :menuselection:`Run, Run Configurations, New Run Configuration` on the menu bar.
#. On the :guilabel:`[New] - Idle` tab, choose :guilabel:`Runner: Auto`, and then choose :guilabel:`C++`.

   .. note:: If :guilabel:`C++` isn't available, you can create a custom runner for C++.

      #. On the :guilabel:`[New] - Idle` tab, choose :guilabel:`Runner: Auto`, and then choose :guilabel:`New Runner`.
      #. On the :guilabel:`My Runner.run` tab, replace the tab's contents with this code.

         .. code-block:: json

            {
              "cmd" : ["$file", "$args"],
              "info" : "Running $project_path$file_name...",
              "selector" : "source"
            }

      #. Choose :menuselection:`File, Save As` on the menu bar, and then save the file as :file:`C++.run`
         in the :file:`/.c9/runners` folder.
      #. On the :guilabel:`[New] - Idle` tab, choose :guilabel:`Runner: Auto`, and then choose :guilabel:`C++`.

#. For :guilabel:`Command`, type :samp:`hello 5 9`. In the code, :code:`5` represents :code:`argv[1]`,
   and :code:`9` represents :code:`argv[2]`.
#. Choose the :guilabel:`Run` button, and compare your output.

   .. code-block:: text

      Hello, World!
      The sum of 2 and 3 is 5.
      The sum of 5 and 9 is 14.

.. _sample-cplusplus-sdk:

Step 4: Install and Configure the |sdk-cpp|
===========================================

You can enhance this sample to use the |sdk-cpp| to create an |s3| bucket, list your available buckets, and then delete the bucket you just created.

In this step, you install and configure the |sdk-cpp|, which provides a convenient way to interact with AWS services, such as |s3|, from your C++ code.
Before you install the |sdk-cpp|, you must install some dependencies. After you install the |sdk-cpp|,
you must set up credentials management in your |env|. The |sdk-cpp| needs these credentials to interact with AWS services.

.. note:: The following steps require your |env| to be running on an |EC2| instance or your own server that has at least 4 GB of RAM.

.. topic:: To install |sdk-cpp| dependencies

   From a terminal session in the |AC9IDE|, run the following command to install several packages that the |sdk-cpp| depends on to run correctly.

   .. code-block:: sh

      sudo yum -y install libcurl-devel openssl-devel libuuid-devel cmake3

.. topic:: To download and extract the |sdk-cpp| source code

   #. Run the :command:`wget` command, specifying the location of the |sdk-cpp| source.

      .. code-block:: sh

         wget https://github.com/aws/aws-sdk-cpp/archive/master.zip

   #. Run the :command:`unzip` command, specifying the name of the .zip file you just downloaded.

      .. code-block:: sh

         unzip master.zip

   #. Run the :command:`rm` command to delete the .zip file, as you no longer need it.

      .. code-block:: sh

         rm master.zip

.. topic:: To build the |sdk-cpp|

   .. note:: This step could take up to one or more hours to complete, depending on the computing resources available to your |EC2| instance or your own server and 
      how much of the |sdk-cpp| you choose to build.

   #. Create a folder to build the |sdk-cpp| into.

      .. code-block:: sh

         mkdir sdk_build

   #. Switch to the folder you just created.

      .. code-block:: sh

         cd sdk_build

   #. Prepare to build the |sdk-cpp| into this folder.

      .. code-block:: sh

         cmake3 ../aws-sdk-cpp-master

      .. note:: To build only the |S3| portion of the |sdk-cpp| and its dependencies, run this command instead:

         .. code-block:: sh

            cmake3 ../aws-sdk-cpp-master -DBUILD_ONLY="s3"

   #. Build the |sdk-cpp| into this folder.

      .. code-block:: sh

         make

   #. After the |sdk-cpp| successfully builds, switch to the root of your |env|.

      .. code-block:: sh

         cd ..

.. topic:: To set up credentials management in your |env|

   Each time you use the |sdk-cpp| to call an AWS service, you must provide a set of credentials with the call. These credentials determine whether the
   |sdk-cpp| has the appropriate permissions to make that call. If the credentials don't cover the appropriate
   permissions, the call will fail.

   In this step, you store your credentials within the |env|. To do this, follow the instructions in :ref:`Call AWS Services from an Environment <credentials>`, and then return to this topic.

   For additional information, see :sdk-cpp-dg-v1:`Providing AWS Credentials <credentials>` in the *AWS SDK for C++ Developer Guide*.

.. _sample-cplusplus-sdk-code:

Step 5: Add AWS SDK Code
========================

In this step, you add some more code, this time to interact with |s3| to create a bucket, list your available buckets, and then delete the bucket you just created. You
will run this code later.

#. In the |AC9IDE|, create a file with this content, and save the file with the name :file:`s3-demo.cpp` at the root (:file:`/`) of your |env|.

   .. code-block:: cpp

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

#. Create a file with this content, and save the file with the name :file:`CMakeLists.txt` at the root (:file:`/`) of your |env|. This file enables you to build your
   code into an executable file.

   .. code-block:: text

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

.. _sample-cplusplus-sdk-run:

Step 6: Build and Run the AWS SDK Code
======================================

#. In the terminal, prepare to build your source code.

   .. code-block:: sh

      cmake3 -Daws-sdk-cpp_DIR=sdk_build .

#. Build your source code.

   .. code-block:: sh

      make

#. Run the code by choosing :menuselection:`Run, Run Configurations, New Run Configuration` on the menu bar.
#. On the :guilabel:`[New] - Idle` tab, choose :guilabel:`Runner: Auto`, and then choose :guilabel:`C++`.
#. For :guilabel:`Command`, type :code:`s3-demo my-test-bucket us-east-2`, where :code:`my-test-bucket` is the name of the bucket you want to create 
   and then delete, and :code:`us-east-2` is the ID of the AWS Region you want to create the bucket in. 
   For more IDs, see :aws-gen-ref:`Amazon Simple Storage Service (Amazon S3) <rande.html#s3_region>` in the |AWS-gr|.

   .. note:: |S3| bucket names must be unique across AWS |mdash| not just your AWS account.

#. Choose the :guilabel:`Run` button, and compare your output.

   .. code-block:: text

      My buckets now are:

      Creating a new bucket named 'my-test-bucket'...

      My buckets now are:

      my-test-bucket

      Deleting the bucket named 'my-test-bucket'...

      My buckets now are:

.. _sample-cplusplus-clean-up:

Step 7: Clean Up
================

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the |env|.
For instructions, see :doc:`Deleting an Environment <delete-environment>`.
