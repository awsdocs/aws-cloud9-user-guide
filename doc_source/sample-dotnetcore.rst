.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _sample-dotnetcore:

##############################
.NET Core Sample for |AC9long|
##############################

.. meta::
    :description:
        Provides a hands-on sample that you can use to experiment with .NET Core in AWS Cloud9.

This sample enables you to run some .NET Core code in an |envfirst|.

Creating this sample might result in charges to your AWS account. These include possible charges for services such as |EC2| and |S3|. For more information, see
`Amazon EC2 Pricing <https://aws.amazon.com/ec2/pricing/>`_ and `Amazon S3 Pricing <https://aws.amazon.com/s3/pricing/>`_.

* :ref:`sample-dotnetcore-prereqs`
* :ref:`sample-dotnetcore-setup`
* :ref:`sample-dotnetcore-app`
* :ref:`sample-dotnetcore-code`
* :ref:`sample-dotnetcore-run`
* :ref:`sample-dotnetcore-sdk`
* :ref:`sample-dotnetcore-sdk-code`
* :ref:`sample-dotnetcore-sdk-run`
* :ref:`sample-dotnetcore-clean-up`

.. _sample-dotnetcore-prereqs:

Prerequisites
=============

.. include:: _sample-prereqs.txt

.. _sample-dotnetcore-setup:

Step 1: Install Required Tools
==============================

In this step, you install the .NET Core 2 SDK into your |env|, which is required to run this sample.

.. note:: The following procedure shows how to install the .NET Core 2 SDK in an |envec2| that is connected to an |EC2| instance running Amazon Linux. To 
   set up an |envssh| connected to an |EC2| instance running Ubuntu Server with the .NET Core 2 SDK already installed, skip this procedure and 
   watch the 8-minute video 
   `Setting Up a .NET and PowerShell Development Environment with AWS Cloud9 and Amazon EC2 <https://www.youtube.com/watch?v=3ZdvbGArONk>`_ 
   on the YouTube website instead.

#. Confirm whether the .NET Core 2 SDK is already installed in your |env|. To do this, in a terminal session in the |AC9IDE|, run the .NET Core command line interface (CLI)
   with the :command:`-help` option.

   .. code-block:: sh

      dotnet -help

   If the .NET Command Line Tools version is displayed, and the version is 2.0 or greater, skip ahead to :ref:`sample-dotnetcore-app`. If the version is less than 2.0, or if
   an error such as :code:`bash: dotnet: command not found` is displayed, continue on to install the .NET Core 2 SDK.

#. In a terminal session in the |AC9IDE|, run the following commands to help ensure the latest security updates and bug fixes are installed,
   and to install a :code:`libunwind` package that the .NET Core 2 SDK needs. (To start a new terminal session, on the menu bar,
   choose :guilabel:`Window, New Terminal`.)

   .. code-block:: sh

      sudo yum -y update
      sudo yum -y install libunwind

#. Get the URL for the .NET Core 2 SDK file to download into your |env|. To get this URL, do the following from a web browser on your local computer (not from the |IDE|):

   #. Go to `.NET downloads <https://www.microsoft.com/net/download>`_ on the Microsoft website.
   #. On the :guilabel:`.NET downloads` page, choose the :guilabel:`Linux` tab. In the :guilabel:`.NET Core` section, under :guilabel:`Other Linux downloads`, choose the link 
      next to :guilabel:`Binaries` in the :guilabel:`Build apps - SDK` column that starts with :guilabel:`x64`.
   #. On the :guilabel:`Thanks for downloading .NET Core SDK` page, if a download dialog box appears, close it or choose :guilabel:`Cancel`.
      (Do not download the .NET Core 2 SDK file to your local computer.)
   #. Right-click the :guilabel:`Try again` link, and choose the command that copies the download URL to your system clipboard.
      For example, the download URL might be as follows.

      .. code-block:: sh

         https://download.microsoft.com/download/E/8/A/E8AF2EE0-5DDA-4420-A395-D1A50EEFD83E/dotnet-sdk-2.1.401-linux-x64.tar.gz

#. Back in the |IDE|, download the .NET Core 2 SDK file into your |env|. To do this, run the :command:`wget` command in the terminal with the download URL you copied earlier.

   .. code-block:: sh

      wget https://download.microsoft.com/download/E/8/A/E8AF2EE0-5DDA-4420-A395-D1A50EEFD83E/dotnet-sdk-2.1.401-linux-x64.tar.gz

#. Extract the .NET Core 2 SDK download file into a subdirectory named :file:`dotnet` within the home directory of your |env|. To do this, run the :command:`mkdir` command with the
   path to the new :file:`dotnet` subdirectory to create. Then run the :command:`tar` command with the name and location of the .NET Core 2 SDK file to extract along with
   the path to the :file:`dotnet` subdirectory.

   .. code-block:: sh

      mkdir -p $HOME/dotnet
      tar zxf dotnet-sdk-2.1.401-linux-x64.tar.gz -C $HOME/dotnet

   For the :command:`mkdir` command, :code:`-p` creates intermediate directories as needed. The :command:`tar` command uses the following options. 
   
   * :code:`z` specifies to extract a file of type :file:`tar.gz`.
   * :code:`x` extracts the file.
   * :code:`f` specifies the name and location of the file to extract.
   * :code:`-C` extracts the file to the specified location.

#. In the :file:`.bash_profile` file for the |env|, add the :file:`$HOME/dotnet` subdirectory to the :code:`PATH` variable for the |env|, as follows.

   #. Open the :file:`.bash_profile` file for editing by using the :command:`vi` command.

      .. code-block:: sh

         vi ~/.bash_profile

   #. Using the down arrow or :kbd:`j` key, move to the line that starts with :code:`PATH`.
   #. Using the right arrow or :kbd:`$` key, move to the end of that line.
   #. Switch to insert mode by pressing the :kbd:`i` key. (:code:`-- INSERT ---` will appear at the end of the display.)
   #. Add the :file:`~/dotnet` subdirectory to the :command:`PATH` variable by typing :code:`:$HOME/dotnet`. Be sure to include the colon character (:code:`:`). The line should
      now look similar to the following.

      .. code-block:: sh

         PATH=$PATH:$HOME/.local/bin:$HOME/bin:$HOME/dotnet

   #. Save the file. To do this, press the :kbd:`Esc` key (:code:`-- INSERT ---` will disappear from the end of the display),
      type :code:`:wq` (to write to and then quit the file), and then press :kbd:`Enter`.

#. Load the .NET Core 2 SDK by sourcing the :file:`.bash_profile` file.

   .. code-block:: sh

      . ~/.bash_profile

#. Confirm the .NET Core 2 SDK is loaded by running .NET Core CLI with the :command:`--help` option.

   .. code-block:: sh

      dotnet --help

   If successful, the .NET Core 2 SDK version number is displayed, with additional usage information.

#. If you no longer want to keep the .NET Core 2 SDK file in your |env|, you can delete it as follows.

   .. code-block:: sh

      rm dotnet-sdk-2.1.200-linux-x64.tar.gz

.. _sample-dotnetcore-app:

Step 2: Create a .NET Core Console Application Project
======================================================

In this step, you use .NET Core to create a project named :code:`hello`. This project contains all of the files that .NET Core needs to run a simple application from the terminal in the |IDE|. The
application's code is written in C#.

#. In the terminal, run the following commands to create a directory for the project, and then switch to that new directory.

   .. code-block:: sh

      mkdir hello
      cd hello

#. Create a .NET Core console application project. To do this, run the .NET Core CLI with the :command:`new` command, specifying the console application project template type and the
   programming language to use (in this sample, C#).

   .. code-block:: sh

      dotnet new console -lang C#

   The preceding command adds a subdirectory named :file:`obj` with several files, and some additional standalone files, to the :file:`hello` directory. You should note the following two key files:

   * The :file:`hello/hello.csproj` file contains information about the console application project.
   * The :file:`hello/Program.cs` file contains the application's code to run.

.. _sample-dotnetcore-code:

Step 3: Add Code
================

In this step, you add some code to the application.

From the :guilabel:`Environment` window in the |AC9IDE|, open the :file:`hello/Program.cs` file.

In the editor, replace the file's current contents with the following code, and
then save the :file:`Program.cs` file.

.. code-block:: csharp

   using System;

   namespace hello
   {
     class Program
     {
       static void Main(string[] args)
       {
         Console.WriteLine("Hello, World!");

         Console.WriteLine("The sum of 2 and 3 is 5.");

         int sum = Int32.Parse(args[0]) + Int32.Parse(args[1]);

         Console.WriteLine("The sum of {0} and {1} is {2}.",
           args[0], args[1], sum.ToString());
       }
     }
   }

.. _sample-dotnetcore-run:

Step 4: Build and Run the Code
==============================

In this step, you build the project and its dependencies into a set of binary files, including a runnable application file. Then you run the application.

#. In the |IDE|, create a builder for .NET Core as follows.

   #. On the menu bar, choose :guilabel:`Run, Build System, New Build System`.
   #. On the :guilabel:`My Builder.build` tab, replace the tab's contents with the following code.

      .. code-block:: json

         {
           "cmd" : ["dotnet", "build"],
           "info" : "Building..."
         }

   #. Choose :guilabel:`File, Save As`.
   #. For :guilabel:`Filename`, type :code:`.NET Core.build`.
   #. For :guilabel:`Folder`, type :code:`/.c9/builders`.
   #. Choose :guilabel:`Save`.

#. With the contents of the :file:`Program.cs` file displayed in the editor, choose :guilabel:`Run, Build System, .NET Core`. Then choose :guilabel:`Run, Build`.

   This builder adds a subdirectory named :file:`bin` and adds a subdirectory named :file:`Debug` to the :file:`hello/obj` subdirectory. Note the following three key
   files.

   * The :file:`hello/bin/Debug/netcoreapp2.0/hello.dll` file is the runnable application file.
   * The :file:`hello/bin/Debug/netcoreapp2.0/hello.deps.json` file lists the application's dependencies.
   * The :file:`hello/bin/Debug/netcoreapp2.0/hello.runtimeconfig.json` file specifies the shared runtime and its version for the application.

#. Create a runner for .NET Core as follows.

   #. On the menu bar, choose :guilabel:`Run, Run With, New Runner`.
   #. On the :guilabel:`My Runner.run` tab, replace the tab's contents with the following code.

      .. code-block:: json

         {
           "cmd" : ["dotnet", "run", "$args"],
           "working_dir": "$file",
           "info" : "Running..."
         }

   #. Choose :guilabel:`File, Save As`.
   #. For :guilabel:`Filename`, type :code:`.NET Core.run`.
   #. For :guilabel:`Folder`, type :code:`/.c9/runners`.
   #. Choose :guilabel:`Save`.

#. Run the application with two integers to add (for example, :code:`5` and :code:`9`) as follows.

   #. With the contents of the :file:`Program.cs` file displayed in the editor, choose :guilabel:`Run, Run Configurations, New Run Configuration`.
   #. In the :guilabel:`[New] - Idle` tab, choose :guilabel:`Runner: Auto`, and then choose :guilabel:`.NET Core`.
   #. In the :guilabel:`Command` box, type :code:`hello 5 9`.
   #. Choose :guilabel:`Run`.

      By default, this runner instructs .NET Core to run the :file:`hello.dll` file in the :file:`hello/bin/Debug/netcoreapp2.0` directory.

      Compare your output to the following.

      .. code-block:: text

         Hello, World!
         The sum of 2 and 3 is 5.
         The sum of 5 and 9 is 14.

.. _sample-dotnetcore-sdk:

Step 5: Create and Set Up a .NET Core Console Application Project That Uses the |sdk-net|
=========================================================================================

You can enhance this sample to use the |sdk-net| to create an |s3| bucket, list your available buckets, and then delete the bucket you just created.

In this new project, you add a reference to the |sdk-net|. The |sdk-net| provides a convenient way to interact with AWS services such as |s3|,
from your .NET code. You then set up AWS credentials management in your |env|. The |sdk-net| needs these credentials to interact with AWS services.

.. topic:: To create the project

   #. In the terminal, run the following commands to change to the root directory of the |env|, create a directory for a project named :code:`s3`, and then switch to that new directory.

      .. code-block:: sh

         cd ..
         mkdir s3
         cd s3

   #. Create a .NET Core console application project. To do this, run the .NET Core CLI with the :command:`new` command, specifying the console application project template type and the
      programming language to use.

      .. code-block:: sh

         dotnet new console -lang C#

   #. Add a project reference to the |S3| package in the |sdk-net|. To do this, run the .NET Core CLI with the :command:`add package` command, specifying the name of the |S3| package in NuGet.
      (NuGet defines how packages for .NET are created, hosted, and consumed, and provides the tools for each of those roles.)

      .. code-block:: sh

         dotnet add package AWSSDK.S3

      When you add a project reference to the |S3| package, NuGet also adds a project reference to the rest of the |sdk-net|.

      .. note:: For the names and versions of other AWS related packages in NuGet, see `NuGet packages tagged with aws-sdk <https://www.nuget.org/packages?q=Tags%3A%22aws-sdk%22>`_ on the NuGet website.

.. topic:: To set up AWS credentials management

   Each time you use the |sdk-net| to call an AWS service, you must provide a set of AWS credentials with the call. These credentials determine whether the
   |sdk-net| has the appropriate permissions to make that call. If the credentials don't cover the appropriate permissions, the call will fail.

   To store your credentials within the |env|, follow the instructions in :ref:`Call AWS Services from an Environment <credentials>`, and then return to this topic.

   For additional information, see :sdk-net-dg:`Configuring AWS Credentials <net-dg-config-creds>` in the |sdk-net-dg|.

.. _sample-dotnetcore-sdk-code:

Step 6: Add AWS SDK Code
========================

In this step, you add code to interact with |S3| to create a bucket, delete the bucket you just created, and then list your available buckets.

From the :guilabel:`Environment` window in the |AC9IDE|, open the :file:`s3/Program.cs` file. In the editor, replace the file's current contents with the following code, and
then save the :file:`Program.cs` file.

.. code-block:: csharp

   using Amazon;
   using Amazon.S3;
   using Amazon.S3.Model;
   using Amazon.S3.Util;
   using System;
   using System.Threading.Tasks;

   namespace s3
   {
     class Program
     {
       private static RegionEndpoint bucketRegion;
       private static IAmazonS3 s3Client;

       static void Main(string[] args)
       {
         if (args.Length < 2) {
           Console.Write("Usage: <the bucket name> <the AWS Region to use>\n" +
             "Example: my-test-bucket us-east-2\n");
           return;
         }

         if (args[1] == "us-east-2") {
           bucketRegion = RegionEndpoint.USEast2;
         } else {
           Console.WriteLine("Cannot continue. The only supported AWS Region ID is " +
             "'us-east-2'.");
           return;
         }
         // Note: You could add more valid AWS Regions above as needed.

         s3Client = new AmazonS3Client(bucketRegion);
         var bucketName = args[0];

         // Create the bucket.
         try
         {
           if (DoesBucketExist(bucketName))
           {
             Console.WriteLine("Cannot continue. Cannot create bucket. \n" +
               "A bucket named '{0}' already exists.", bucketName);
             return;
           } else {
             Console.WriteLine("\nCreating the bucket named '{0}'...", bucketName);
             s3Client.PutBucketAsync(bucketName).Wait();
           }
         }
         catch (AmazonS3Exception e)
         {
           Console.WriteLine("Cannot continue. {0}", e.Message);
         }
         catch (Exception e)
         {
           Console.WriteLine("Cannot continue. {0}", e.Message);
         }

         // Confirm that the bucket was created.
         if (DoesBucketExist(bucketName))
         {
           Console.WriteLine("Created the bucket named '{0}'.", bucketName);
         } else {
           Console.WriteLine("Did not create the bucket named '{0}'.", bucketName);
         }

         // Delete the bucket.
         Console.WriteLine("\nDeleting the bucket named '{0}'...", bucketName);
         s3Client.DeleteBucketAsync(bucketName).Wait();

         // Confirm that the bucket was deleted.
         if (DoesBucketExist(bucketName))
         {
           Console.WriteLine("Did not delete the bucket named '{0}'.", bucketName);
         } else {
           Console.WriteLine("Deleted the bucket named '{0}'.", bucketName);
         };

         // List current buckets.
         Console.WriteLine("\nMy buckets now are:");
         var response = s3Client.ListBucketsAsync().Result;

         foreach (var bucket in response.Buckets)
         {
           Console.WriteLine(bucket.BucketName);
         }
       }

       static bool DoesBucketExist(string bucketName)
       {
         if ((AmazonS3Util.DoesS3BucketExistAsync(s3Client, bucketName).Result))
         {
           return true;
         } else {
           return false;
         }
       }
     }
   }

.. _sample-dotnetcore-sdk-run:

Step 7: Build and Run the AWS SDK Code
======================================

In this step, you build the project and its dependencies into a set of binary files, including a runnable application file. Then you run the application.

#. Build the project. To do this, with the contents of the :file:`s3/Program.cs` file displayed in the editor, on the menu bar, choose :guilabel:`Run, Build`.
#. Run the application with the name of the |S3| bucket to create and the ID of the AWS Region to
   create the bucket in (for example, :code:`my-test-bucket` and :code:`us-east-2`) as follows.

   #. With the contents of the :file:`s3/Program.cs` file still displayed in the editor, choose :guilabel:`Run, Run Configurations, New Run Configuration`.
   #. In the :guilabel:`[New] - Idle` tab, choose :guilabel:`Runner: Auto`, and then choose :guilabel:`.NET Core`.
   #. In the :guilabel:`Command` box, type the name of the application, the name of the |S3| bucket to create, and the ID of the AWS Region to
      create the bucket in (for example, :code:`s3 my-test-bucket us-east-2`).
   #. Choose :guilabel:`Run`.

      By default, this runner instructs .NET Core to run the :file:`s3.dll` file in the :file:`s3/bin/Debug/netcoreapp2.0` directory.

      Compare your results to the following output.

      .. code-block:: text

         Creating a new bucket named 'my-test-bucket'...
         Created the bucket named 'my-test-bucket'.

         Deleting the bucket named 'my-test-bucket'...
         Deleted the bucket named 'my-test-bucket'.

         My buckets now are:

.. _sample-dotnetcore-clean-up:

Step 8: Clean Up
================

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the |env|.
For instructions, see :doc:`Delete an Environment <delete-environment>`.
