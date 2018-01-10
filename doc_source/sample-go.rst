.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _sample-go:

#######################
Go Sample for |AC9long|
#######################

.. meta::
    :description:
        Provides a hands-on sample that you can use to experiment with Go in AWS Cloud9.

This sample enables you to run some Go code in an |envfirst|.

* :ref:`sample-go-install`
* :ref:`sample-go-code`
* :ref:`sample-go-run`
* :ref:`sample-go-sdk`
* :ref:`sample-go-sdk-code`
* :ref:`sample-go-sdk-run`
* :ref:`sample-go-clean-up`

.. note::

   .. include:: _sample-prereqs.txt

   Creating this sample might result in charges to your AWS account. These include possible charges for services such as |EC2| and |S3|. For more information, see
   `Amazon EC2 Pricing <https://aws.amazon.com/ec2/pricing/>`_ and `Amazon S3 Pricing <https://aws.amazon.com/s3/pricing/>`_.

.. _sample-go-install:

Step 1: Install Required Tools
==============================

In this step, you install and configure Go, which is required to run this sample.

#. In a terminal session in the |AC9IDE|, confirm whether Go is already installed by running the :command:`go version` command. (To start a new terminal session,
   on the menu bar, choose :menuselection:`Window, New Terminal`.) If successful, the output should contain the Go version number. Otherwise, an error message should be output.
   If Go is installed, skip ahead to :ref:`sample-go-code`.
#. Run the :command:`yum update` command to help ensure the latest security updates and bug fixes are installed.

   .. code-block:: sh

      sudo yum -y update

#. To install Go, run these commands, one at a time.

   .. code-block:: sh

      wget https://storage.googleapis.com/golang/go1.7.5.linux-amd64.tar.gz # Download Go.
      sudo tar -C /usr/local -xzf ./go1.7.5.linux-amd64.tar.gz # Install Go.
      rm ./go1.7.5.linux-amd64.tar.gz # Delete the installer.

   For more information, see `Downloads <https://golang.org/dl/>`_ on The Go Programming Language website.
#. Add the path to the Go binary to your :code:`PATH` environment variable, like this.

   #. Open your shell profile file (for example, :file:`~/.bashrc` in Amazon Linux) for editing.
   #. At the end of this line of code, type the following, so that the code now looks like this.

      .. code-block:: sh

         PATH=$PATH:/usr/local/go/bin

    #. Save the file.

#. Source the :file:`~/.bashrc` file so that the terminal can now find the Go binary you just referenced.

   .. code-block:: sh

      . ~/.bashrc

#. Confirm that Go is now successfully installed and configured by running the :command:`go version` command. If successful, the output contains the Go version number.

.. _sample-go-code:

Step 2: Add Code
================

In the |AC9IDE|, create a file with this content, and save the file with the name :file:`hello.go`.
(To create a file, on the menu bar, choose :menuselection:`File, New File`. To save the file, choose :menuselection:`File, Save`.)

.. code-block:: go

   package main

   import (
     "fmt"
     "os"
     "strconv"
   )

   func main() {
     fmt.Printf("Hello, World!\n")

     fmt.Printf("The sum of 2 and 3 is 5.\n")

     first, _ := strconv.Atoi(os.Args[1])
     second, _ := strconv.Atoi(os.Args[2])
     sum := first + second

     fmt.Printf("The sum of %s and %s is %s.",
       os.Args[1], os.Args[2], strconv.Itoa(sum))
   }

.. _sample-go-run:

Step 3: Run the Code
====================

#. In the |AC9IDE|, on the menu bar, choose :menuselection:`Run, Run Configurations, New Run Configuration`.
#. On the :guilabel:`[New] - Idle` tab, choose :guilabel:`Runner: Auto`, and then choose :guilabel:`Go`.

   .. note:: If :guilabel:`Go` is not available, you can create a custom runner for Go.

      #. On the :guilabel:`[New] - Idle` tab, choose :guilabel:`Runner: Auto`, and then choose :guilabel:`New Runner`.
      #. On the :guilabel:`My Runner.run` tab, replace the tab's contents with this code.

         .. code-block:: json

            {
              "cmd" : ["go", "run", "$file", "$args"],
              "info" : "Running $project_path$file_name...",
              "selector" : "source.go"
            }

      #. Choose :menuselection:`File, Save As` on the menu bar, and save the file as :file:`Go.run` in the :file:`/.c9/runners` folder.
      #. On the :guilabel:`[New] - Idle` tab, choose :guilabel:`Runner: Auto`, and then choose :guilabel:`Go`.
      #. Choose the :guilabel:`hello.go` tab to make it active.

#. For :guilabel:`Command`, type :samp:`hello.go 5 9`. In the code, :code:`5` represents :code:`os.Args[1]`,
   and :code:`9` represents :code:`os.Args[2]`.

   .. image:: images/ide-go-simple.png
      :alt: Output of running the Go code in the AWS Cloud9 IDE


#. Choose the :guilabel:`Run` button, and compare your output.

   .. code-block:: text

      Hello, World!
      The sum of 2 and 3 is 5.
      The sum of 5 and 9 is 14.

.. _sample-go-sdk:

Step 4: Install and Configure the |sdk-go|
==========================================

You can enhance this sample to use the |sdk-go| to create an |s3| bucket, list your available buckets, and then delete the bucket you just created.

In this step, you install and configure the |sdk-go|, which provides a convenient way to interact with AWS services such as |s3|, from your Go code.
Before you install the |sdk-go|, you must set your :code:`GOPATH` environment variable. After you install the |sdk-go| and set your :code:`GOPATH` environment variable,
you must set up credentials management in your |env|. The |sdk-go| needs these credentials to interact with AWS services.

.. topic:: To set your GOPATH environment variable

   #. Open your :file:`~/.bashrc` file for editing.
   #. After the last line in the file, type this code.

      .. code-block:: sh

         GOPATH=~/environment/go

         export GOPATH

   #. Save the file.
   #. Source the :file:`~/.bashrc` file so that the terminal can now find the :code:`GOPATH` environment variable you just referenced.

      .. code-block:: sh

         . ~/.bashrc

   #. Confirm that the :code:`GOPATH` environment variable is successfully set by running the :command:`echo
      $GOPATH` command. If successful, :code:`/home/ec2-user/environment/go` should be output.

.. topic:: To install the |sdk-go|

   Run the :command:`go get` command, specifying the location of the |sdk-go| source.

   .. code-block:: sh

      go get -u github.com/aws/aws-sdk-go/...

   Go installs the |sdk-go| source into the location specified by your :code:`GOPATH` environment variable, which is the :file:`go` folder in your |env|.

.. topic:: To set up credentials management in your |env|

   Each time you use the |sdk-go| to call an AWS service, you must provide a set of credentials with the call. These credentials determine whether the
   |sdk-go| has the appropriate permissions to make that call. If the credentials don't cover the appropriate
   permissions, the call will fail.

   In this step, you store your credentials within the |env|. To do this, follow the instructions in :ref:`Call AWS Services from an Environment <credentials>`, and then return to this topic.

   For additional information, see :sdk-for-go-dev-guide-v1:`Specifying Credentials <configuring-sdk.html#specifying-credentials>` in the
   |sdk-go-dg|.

.. _sample-go-sdk-code:

Step 5: Add AWS SDK Code
========================

In this step, you add some more code, this time to interact with |s3| to create a bucket, list your available buckets, and then delete the bucket you just created. You
will run this code later.

In the |AC9IDE|, create a file with this content, and save the file with the name :file:`s3.go`.

.. code-block:: go

   package main

   import (
     "fmt"
     "os"
     "github.com/aws/aws-sdk-go/aws"
     "github.com/aws/aws-sdk-go/aws/session"
     "github.com/aws/aws-sdk-go/service/s3"
   )

   func main() {
     sess := session.Must(session.NewSessionWithOptions(session.Options{
       SharedConfigState: session.SharedConfigEnable,
     }))
     region := "YOUR_REGION"
     svc := s3.New(sess, &aws.Config{
       Region: aws.String(region),
     })

     listMyBuckets(svc)
     createMyBucket(svc, os.Args[1], region)
     listMyBuckets(svc)
     deleteMyBucket(svc, os.Args[1])
     listMyBuckets(svc)
   }

   // List all of your available buckets in this AWS Region.
   func listMyBuckets(svc *s3.S3) {
     result, err := svc.ListBuckets(nil)

     if err != nil {
       exitErrorf("Unable to list buckets, %v", err)
     }

     fmt.Println("My buckets now are:\n")

     for _, b := range result.Buckets {
       fmt.Printf(aws.StringValue(b.Name) + "\n")
     }

     fmt.Printf("\n")
   }

   // Create a bucket in this AWS Region.
   func createMyBucket(svc *s3.S3, bucketName string, region string) {
     fmt.Printf("\nCreating a new bucket named '" + bucketName + "'...\n\n")

     _, err := svc.CreateBucket(&s3.CreateBucketInput{
      Bucket: aws.String(bucketName),
      CreateBucketConfiguration: &s3.CreateBucketConfiguration{
        LocationConstraint: aws.String(region),
      },
    })

     if err != nil {
       exitErrorf("Unable to create bucket, %v", err)
     }
   }

   // Delete the bucket you just created.
   func deleteMyBucket(svc *s3.S3, bucketName string) {
     fmt.Printf("\nDeleting the bucket named '" + bucketName + "'...\n\n")

     _, err := svc.DeleteBucket(&s3.DeleteBucketInput{
       Bucket: aws.String(bucketName),
     })

     if err != nil {
       exitErrorf("Unable to delete bucket, %v", err)
     }
   }

   // If there's an error, display it.
   func exitErrorf(msg string, args ...interface{}) {
     fmt.Fprintf(os.Stderr, msg+"\n", args...)
     os.Exit(1)
   }

In the preceding code, replace :samp:`YOUR_REGION` with the ID of an AWS Region. For example,
for the US East (Ohio) Region, use :code:`us-east-2`. For more IDs, see :aws-gen-ref:`Amazon Simple Storage Service (Amazon S3) <rande.html#s3_region>` in the |AWS-gr|.

.. _sample-go-sdk-run:

Step 6: Run the AWS SDK Code
============================

#. In the |AC9IDE|, on the menu bar, choose :menuselection:`Run, Run Configurations, New Run Configuration`.
#. On the :guilabel:`[New] - Idle` tab, choose :guilabel:`Runner: Auto`, and then choose :guilabel:`Go`.
#. For :guilabel:`Command`, type :samp:`s3.go {YOUR-BUCKET-NAME}`, where :samp:`{YOUR-BUCKET-NAME}` is the name of the bucket you want to create and then delete.

   .. note:: |S3| bucket names must be unique across AWS |mdash| not just your AWS account.

   .. image:: images/ide-go-sdk.png
      :alt: Running the AWS SDK for Go code in the AWS Cloud9 IDE

#. Choose the :guilabel:`Run` button, and compare your output.

   .. code-block:: text

      My buckets now are:

      Creating a new bucket named 'my-test-bucket'...

      My buckets now are:

      my-test-bucket

      Deleting the bucket named 'my-test-bucket'...

      My buckets now are:

.. _sample-go-clean-up:

Step 7: Clean Up
================

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the |env|.
For instructions, see :doc:`Deleting an Environment <delete-environment>`.
