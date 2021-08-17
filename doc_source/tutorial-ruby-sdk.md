# Step 4: Install and configure the AWS SDK for Ruby<a name="tutorial-ruby-sdk"></a>

\(Previous step: [Step 3: Run the code](tutorial-ruby-run.md)\)

**Note**  
If you don't want to perform these enhanced procedures, be sure to at least perform [Step 7: Clean up](tutorial-ruby-clean-up.md)\.

You can enhance this tutorial to use the AWS SDK for Ruby to create an Amazon S3 bucket, list your available buckets, and then delete the bucket you just created\.

In this step, you install and configure the AWS SDK for Ruby, which provides a convenient way to interact with AWS services such as Amazon S3 from your Ruby code\.
+ Before you can install the AWS SDK for Ruby, you must install RubyGems\.
+ After you install the AWS SDK for Ruby, you must set up credentials management in your environment\. The AWS SDK for Ruby needs these credentials to interact with AWS services\.

## 4\.1 Install RubyGems<a name="tutorial-ruby-sdk-install-gems"></a>

1. In a terminal session in the AWS Cloud9 IDE, confirm whether RubyGems is already installed by running the ** `gem --version` ** command\. If successful, the output contains the RubyGems version number\. Otherwise, an error message is displayed\.

   If RubyGems is installed, skip ahead to [4\.2: Install the AWS SDK for Ruby](#tutorial-ruby-sdk-install-sdk)\.

1. To install RubyGems, run the **`install`** command as follows\.

   For Amazon Linux:

   ```
   sudo yum -y install gem
   ```

   For Ubuntu Server:

   ```
   sudo apt install -y gem
   ```

   For more information, see [Download RubyGems](https://rubygems.org/pages/download) on the RubyGems website\.

## 4\.2: Install the AWS SDK for Ruby<a name="tutorial-ruby-sdk-install-sdk"></a>

After you install RubyGems, run the RubyGems ** `install` ** command in a terminal session as follows\.

**Note**  
The installation of the full aws\-sdk package might run several minutes before it starts showing progress in the terminal window\.

```
gem install aws-sdk
```

**Note**  
If you are not using an EC2 instance that is managed by AWS Cloud9 \(that is, an *EC2 environment*\), depending on the permissions and user configuration on your instance, you might need to use `sudo` to install the SDK, as shown in the following command\.  

```
sudo gem install aws-sdk
```
If this is the case, use standard Unix\-based practices\.

For more information, see [Installing the AWS SDK for Ruby](https://docs.aws.amazon.com/sdk-for-ruby/latest/developer-guide/setup-install.html) in the *AWS SDK for Ruby Developer Guide*\.

## 4\.3: Set up credentials management in your environment<a name="tutorial-ruby-sdk-creds"></a>

Each time you use the AWS SDK for Ruby to call an AWS service, you must provide a set of credentials with the call\. These credentials determine whether the AWS SDK for Ruby has the appropriate permissions to make that call\. If the credentials don't cover the appropriate permissions, the call will fail\.

If you are following this tutorial strictly, you will have allowed AWS Cloud9 to create and manage your EC2 instance\. If this is the case for you, AWS Cloud9 is also managing temporary credentials for you, so you can skip this step\.

If this is NOT the case for you, you need to store your credentials within the environment\. To do this, follow the instructions in [Calling AWS services from an environment in AWS Cloud9](credentials.md), and then return to this topic\.

For additional information, see [Configuring the AWS SDK for Ruby](https://docs.aws.amazon.com/sdk-for-ruby/latest/developer-guide/setup-config.html) in the *AWS SDK for Ruby Developer Guide*\.

## Next Step<a name="tutorial-ruby-sdk-next"></a>

[Step 5: Add AWS SDK code](tutorial-ruby-sdk-code.md)