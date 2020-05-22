# \.NET Core Sample for AWS Cloud9<a name="sample-dotnetcore"></a>

This sample enables you to run some \.NET Core code in an AWS Cloud9 development environment\.

Creating this sample might result in charges to your AWS account\. These include possible charges for services such as Amazon EC2 and Amazon S3\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/) and [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/)\.

**Topics**
+ [Prerequisites](#sample-dotnetcore-prereqs)
+ [Step 1: Install Required Tools](#sample-dotnetcore-setup)
+ [Step 2: Create a \.NET Core Console Application Project](#sample-dotnetcore-app)
+ [Step 3: Add Code](#sample-dotnetcore-code)
+ [Step 4: Build and Run the Code](#sample-dotnetcore-run)
+ [Step 5: Create and Set Up a \.NET Core Console Application Project That Uses the AWS SDK for \.NET](#sample-dotnetcore-sdk)
+ [Step 6: Add AWS SDK Code](#sample-dotnetcore-sdk-code)
+ [Step 7: Build and Run the AWS SDK Code](#sample-dotnetcore-sdk-run)
+ [Step 8: Clean Up](#sample-dotnetcore-clean-up)

## Prerequisites<a name="sample-dotnetcore-prereqs"></a>

Before you use this sample, be sure to meet the following requirements\.
+  **You must have an existing AWS Cloud9 EC2 development environment\.** This sample assumes you already have an EC2 environment that is connected to an Amazon EC2 instance running Amazon Linux or Ubuntu Server\. If you have a different type of environment or operating system, you might need to adapt this sample's instructions to set up related tools\. See [Creating an Environment in AWS Cloud9](create-environment.md) for details\.
+  **You have the AWS Cloud9 IDE for the existing environment already open\.** When you open an environment, AWS Cloud9 opens the IDE for that environment in your web browser\. See [Opening an Environment in AWS Cloud9](open-environment.md) for details\.

## Step 1: Install Required Tools<a name="sample-dotnetcore-setup"></a>

In this step, you install the \.NET Core 2 SDK into your environment, which is required to run this sample\.

1. Confirm whether the \.NET Core 2 SDK is already installed in your environment\. To do this, in a terminal session in the AWS Cloud9 IDE, run the \.NET Core command line interface \(CLI\) with the ** `--version` ** option\.

   ```
   dotnet --version
   ```

   If the \.NET Command Line Tools version is displayed, and the version is 2\.0 or greater, skip ahead to [Step 2: Create a \.NET Core Console Application Project](#sample-dotnetcore-app)\. If the version is less than 2\.0, or if an error such as `bash: dotnet: command not found` is displayed, continue on to install the \.NET Core 2 SDK\.

1. For Amazon Linux, in a terminal session in the AWS Cloud9 IDE, run the following commands to help ensure the latest security updates and bug fixes are installed, and to install a `libunwind` package that the \.NET Core 2 SDK needs\. \(To start a new terminal session, on the menu bar, choose **Window, New Terminal**\.\)

   ```
   sudo yum -y update
   sudo yum -y install libunwind
   ```

   For Ubuntu Server, in a terminal session in the AWS Cloud9 IDE, run the following command to help ensure the latest security updates and bug fixes are installed\. \(To start a new terminal session, on the menu bar, choose **Window, New Terminal**\.\)

   ```
   sudo apt -y update
   ```

1. Download the \.NET Core 2 SDK installer script into your environment by running the following command\.

   ```
   curl -O https://dot.net/v1/dotnet-install.sh
   ```

1. Make the installer script executable by the current user by running the following command\.

   ```
   sudo chmod u=rx dotnet-install.sh
   ```

1. Run the installer script, which downloads and installs the \.NET Core 2 SDK, by running the following command\.

   ```
   ./dotnet-install.sh -c Current
   ```

1. Add the \.NET Core 2 SDK to your `PATH`\. To do this, in the shell profile for the environment \(for example, the `.bashrc` file\), add the `$HOME/.dotnet` subdirectory to the `PATH` variable for the environment, as follows\.

   1. Open the `.bashrc` file for editing by using the ** `vi` ** command\.

      ```
      vi ~/.bashrc
      ```

   1. For Amazon Linux, using the down arrow or `j` key, move to the line that starts with `export PATH`\.

      For Ubuntu Server, move to the last line of the file by typing `G`\.

   1. Using the right arrow or `$` key, move to the end of that line\.

   1. Switch to insert mode by pressing the `i` key\. \(`-- INSERT ---` will appear at the end of the display\.\)

   1. For Amazon Linux, add the `$HOME/.dotnet` subdirectory to the ** `PATH` ** variable by typing `:$HOME/.dotnet`\. Be sure to include the colon character \(`:`\)\. The line should now look similar to the following\.

      ```
      export PATH=$PATH:$HOME/.local/bin:$HOME/bin:$HOME/.dotnet
      ```

      For Ubuntu Server, press the right arrow key and then press `Enter` twice, followed by typing the following line by itself at the end of the file\.

      ```
      export PATH=$HOME/.dotnet:$PATH
      ```

   1. Save the file\. To do this, press the `Esc` key \(`-- INSERT ---` will disappear from the end of the display\), type `:wq` \(to write to and then quit the file\), and then press `Enter`\.

1. Load the \.NET Core 2 SDK by sourcing the `.bashrc` file\.

   ```
   . ~/.bashrc
   ```

1. Confirm the \.NET Core 2 SDK is loaded by running \.NET Core CLI with the ** `--help` ** option\.

   ```
   dotnet --help
   ```

   If successful, the \.NET Core 2 SDK version number is displayed, with additional usage information\.

1. If you no longer want to keep the \.NET Core 2 SDK installer script in your environment, you can delete it as follows\.

   ```
   rm dotnet-install.sh
   ```

## Step 2: Create a \.NET Core Console Application Project<a name="sample-dotnetcore-app"></a>

In this step, you use \.NET Core to create a project named `hello`\. This project contains all of the files that \.NET Core needs to run a simple application from the terminal in the IDE\. The application's code is written in C\#\.

1. In the terminal, run the following commands to create a directory for the project, and then switch to that new directory\.

   ```
   mkdir hello
   cd hello
   ```

1. Create a \.NET Core console application project\. To do this, run the \.NET Core CLI with the ** `new` ** command, specifying the console application project template type and the programming language to use \(in this sample, C\#\)\.

   ```
   dotnet new console -lang C#
   ```

   The preceding command adds a subdirectory named `obj` with several files, and some additional standalone files, to the `hello` directory\. You should note the following two key files:
   + The `hello/hello.csproj` file contains information about the console application project\.
   + The `hello/Program.cs` file contains the application's code to run\.

## Step 3: Add Code<a name="sample-dotnetcore-code"></a>

In this step, you add some code to the application\.

From the **Environment** window in the AWS Cloud9 IDE, open the `hello/Program.cs` file\.

In the editor, replace the file's current contents with the following code, and then save the `Program.cs` file\.

```
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
```

## Step 4: Build and Run the Code<a name="sample-dotnetcore-run"></a>

In this step, you build the project and its dependencies into a set of binary files, including a runnable application file\. Then you run the application\.

1. In the IDE, create a builder for \.NET Core as follows\.

   1. On the menu bar, choose **Run, Build System, New Build System**\.

   1. On the **My Builder\.build** tab, replace the tab's contents with the following code\.

      ```
      {
        "cmd" : ["dotnet", "build"],
        "info" : "Building..."
      }
      ```

   1. Choose **File, Save As**\.

   1. For **Filename**, type `.NET Core.build`\.

   1. For **Folder**, type `/.c9/builders`\.

   1. Choose **Save**\.

1. With the contents of the `Program.cs` file displayed in the editor, choose **Run, Build System, \.NET Core**\. Then choose **Run, Build**\.

   This builder adds a subdirectory named `bin` and adds a subdirectory named `Debug` to the `hello/obj` subdirectory\. Note the following three key files\.
   + The `hello/bin/Debug/netcoreapp2.0/hello.dll` file is the runnable application file\.
   + The `hello/bin/Debug/netcoreapp2.0/hello.deps.json` file lists the application's dependencies\.
   + The `hello/bin/Debug/netcoreapp2.0/hello.runtimeconfig.json` file specifies the shared runtime and its version for the application\.

1. Create a runner for \.NET Core as follows\.

   1. On the menu bar, choose **Run, Run With, New Runner**\.

   1. On the **My Runner\.run** tab, replace the tab's contents with the following code\.

      ```
      {
        "cmd" : ["dotnet", "run", "$args"],
        "working_dir": "$file",
        "info" : "Running..."
      }
      ```

   1. Choose **File, Save As**\.

   1. For **Filename**, type `.NET Core.run`\.

   1. For **Folder**, type `/.c9/runners`\.

   1. Choose **Save**\.

1. Run the application with two integers to add \(for example, `5` and `9`\) as follows\.

   1. With the contents of the `Program.cs` file displayed in the editor, choose **Run, Run Configurations, New Run Configuration**\.

   1. In the **\[New\] \- Idle** tab, choose **Runner: Auto**, and then choose **\.NET Core**\.

   1. In the **Command** box, type `hello 5 9`\.

   1. Choose **Run**\.

      By default, this runner instructs \.NET Core to run the `hello.dll` file in the `hello/bin/Debug/netcoreapp2.0` directory\.

      Compare your output to the following\.

      ```
      Hello, World!
      The sum of 2 and 3 is 5.
      The sum of 5 and 9 is 14.
      ```

## Step 5: Create and Set Up a \.NET Core Console Application Project That Uses the AWS SDK for \.NET<a name="sample-dotnetcore-sdk"></a>

You can enhance this sample to use the AWS SDK for \.NET to create an Amazon S3 bucket, list your available buckets, and then delete the bucket you just created\.

In this new project, you add a reference to the AWS SDK for \.NET\. The AWS SDK for \.NET provides a convenient way to interact with AWS services such as Amazon S3, from your \.NET code\. You then set up AWS credentials management in your environment\. The AWS SDK for \.NET needs these credentials to interact with AWS services\.

### To create the project<a name="sample-dotnetcore-sdk-create"></a>

1. In the terminal, run the following commands to change to the root directory of the environment, create a directory for a project named `s3`, and then switch to that new directory\.

   ```
   cd ..
   mkdir s3
   cd s3
   ```

1. Create a \.NET Core console application project\. To do this, run the \.NET Core CLI with the ** `new` ** command, specifying the console application project template type and the programming language to use\.

   ```
   dotnet new console -lang C#
   ```

1. Add a project reference to the Amazon S3 package in the AWS SDK for \.NET\. To do this, run the \.NET Core CLI with the ** `add package` ** command, specifying the name of the Amazon S3 package in NuGet\. \(NuGet defines how packages for \.NET are created, hosted, and consumed, and provides the tools for each of those roles\.\)

   ```
   dotnet add package AWSSDK.S3
   ```

   When you add a project reference to the Amazon S3 package, NuGet also adds a project reference to the rest of the AWS SDK for \.NET\.
**Note**  
For the names and versions of other AWS related packages in NuGet, see [NuGet packages tagged with aws\-sdk](https://www.nuget.org/packages?q=Tags%3A%22aws-sdk%22) on the NuGet website\.

### To set up AWS credentials management<a name="sample-dotnetcore-sdk-creds"></a>

Each time you use the AWS SDK for \.NET to call an AWS service, you must provide a set of AWS credentials with the call\. These credentials determine whether the AWS SDK for \.NET has the appropriate permissions to make that call\. If the credentials don't cover the appropriate permissions, the call will fail\.

To store your credentials within the environment, follow the instructions in [Calling AWS Services from an Environment in AWS Cloud9](credentials.md), and then return to this topic\.

For additional information, see [Configuring AWS Credentials](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/net-dg-config-creds.html) in the *AWS SDK for \.NET Developer Guide*\.

## Step 6: Add AWS SDK Code<a name="sample-dotnetcore-sdk-code"></a>

In this step, you add code to interact with Amazon S3 to create a bucket, delete the bucket you just created, and then list your available buckets\.

From the **Environment** window in the AWS Cloud9 IDE, open the `s3/Program.cs` file\. In the editor, replace the file's current contents with the following code, and then save the `Program.cs` file\.

```
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
```

## Step 7: Build and Run the AWS SDK Code<a name="sample-dotnetcore-sdk-run"></a>

In this step, you build the project and its dependencies into a set of binary files, including a runnable application file\. Then you run the application\.

1. Build the project\. To do this, with the contents of the `s3/Program.cs` file displayed in the editor, on the menu bar, choose **Run, Build**\.

1. Run the application with the name of the Amazon S3 bucket to create and the ID of the AWS Region to create the bucket in \(for example, `my-test-bucket` and `us-east-2`\) as follows\.

   1. With the contents of the `s3/Program.cs` file still displayed in the editor, choose **Run, Run Configurations, New Run Configuration**\.

   1. In the **\[New\] \- Idle** tab, choose **Runner: Auto**, and then choose **\.NET Core**\.

   1. In the **Command** box, type the name of the application, the name of the Amazon S3 bucket to create, and the ID of the AWS Region to create the bucket in \(for example, `s3 my-test-bucket us-east-2`\)\.

   1. Choose **Run**\.

      By default, this runner instructs \.NET Core to run the `s3.dll` file in the `s3/bin/Debug/netcoreapp2.0` directory\.

      Compare your results to the following output\.

      ```
      Creating a new bucket named 'my-test-bucket'...
      Created the bucket named 'my-test-bucket'.
      
      Deleting the bucket named 'my-test-bucket'...
      Deleted the bucket named 'my-test-bucket'.
      
      My buckets now are:
      ```

## Step 8: Clean Up<a name="sample-dotnetcore-clean-up"></a>

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the environment\. For instructions, see [Deleting an Environment in AWS Cloud9](delete-environment.md)\.