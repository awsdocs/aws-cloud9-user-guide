# Step 1: Install required tools<a name="tutorial-ruby-install"></a>

\(First step of [Tutorial: Ruby in AWS Cloud9](tutorial-ruby.md)\)

In this step, you install Ruby, which is required to run this tutorial\.

1. In a terminal session in the AWS Cloud9 IDE, confirm whether Ruby is already installed by running the ** `ruby --version` ** command\. \(To start a new terminal session, on the menu bar, choose **Window**, **New Terminal**\.\) If successful, the output contains the Ruby version number\. If Ruby is installed, skip ahead to [Step 2: Add code](tutorial-ruby-code.md)\.

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

## Next Step<a name="tutorial-ruby-install-next"></a>

[Step 2: Add code](tutorial-ruby-code.md)