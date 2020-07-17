# Troubleshooting AWS Cloud9<a name="troubleshooting"></a>

Use the following information to help you identify and address issues with AWS Cloud9\.

If your issue is not listed, or if you need additional help, see the [AWS Cloud9 Discussion Forum](https://forums.aws.amazon.com/forum.jspa?forumID=268)\. \(When you enter this forum, AWS might require you to sign in\.\) You can also [contact us](https://aws.amazon.com/contact-us/) directly\.

**Topics**
+ [Environment creation error: "We are unable to create EC2 instances \.\.\."](#troubleshooting-account-verification)
+ [Environment creation error: "Not authorized to perform sts:AssumeRole"](#troubleshooting-sts-assume-role)
+ [Console error: "User is not authorized to perform action on resource"](#troubleshooting-access-not-authorized)
+ [Federated identities cannot create environments](#troubleshooting-federated-service-role)
+ [Cannot open an environment](#troubleshooting-env-loading)
+ [The AWS Cloud9 installer hangs or fails](#troubleshooting-ssh-installer)
+ [SSH environment error: "Python version 2\.7 is required to install pty\.js"](#troubleshooting-python-ssh)
+ [Application preview or file preview notice: "Third\-party cookies disabled"](#troubleshooting-preview)
+ [Application preview tab displays an error or is blank](#troubleshooting-app-preview)
+ [Cannot display your running application outside of the IDE](#troubleshooting-app-sharing)
+ [After reloading an environment, you must refresh application preview](#troubleshooting-app-preview-refresh)
+ [Unable to preview application in the AWS Cloud9 IDE with HTTP](#troubleshooting-app-preview-http)
+ [Cannot run some commands or scripts in an EC2 environment](#troubleshooting-rhel-ubuntu)
+ [AWS CLI / aws\-shell error: "The security token included in the request is invalid" in an EC2 environment](#troubleshooting-cli-invalid-token)
+ [Amazon EC2 instances are not automatically updated](#troubleshooting-update-ami)
+ [Lambda local function run error: Cannot install SAM Local](#troubleshooting-install-sam-local)
+ [IDE warning: "This environment is running low on memory" or "This environment has high CPU load"](#troubleshooting-ide-low-memory)
+ [Previewing a file returns a 499 error](#troubleshooting-file-preview-script-block)
+ [Environment deletion error: "One or more environments failed to delete"](#troubleshooting-delete-environment)
+ [Console warning: "Switching to the minimal code completion engine\.\.\."](#troubleshooting-minimal-code-completion)
+ [AWS Cloud9 installer doesn't finish after displaying: "Package Cloud9 IDE 1"](#cloud9-installer-failed)
+ [VPC error for EC2\-Classic accounts: "Unable to access your environment"](#ec2-classic-issue)

## Environment creation error: "We are unable to create EC2 instances \.\.\."<a name="troubleshooting-account-verification"></a>

 **Issue:** When you try to create an AWS Cloud9 development environment, a message appears with the phrase "We are unable to create EC2 instances in your account during account verification and activation\." 

 **Cause:** AWS is currently verifying and activating your AWS account\. Until activation is complete, which could take up to 24 hours, you can't create this or other environments\. 

 **Solution:** Try creating the environment again later\. If you're still receiving this message after 24 hours, email [aws\-verification@amazon\.com](mailto:aws-verification@amazon.com)\. Be advised that AWS CloudFormation creates a related stack in your account, even though the attempt to create an environment fails\. These stacks count against the stack creation limit in your account\. To help avoid the stack creation limit, you can safely delete these failed stacks\. For more information, see [Deleting a Stack on the AWS CloudFormation Console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.html) in the *AWS CloudFormation User Guide*\.

\([back to top](#troubleshooting)\)

## Environment creation error: "Not authorized to perform sts:AssumeRole"<a name="troubleshooting-sts-assume-role"></a>

 **Issue:** When you try to create a new environment, you see this error: "Not authorized to perform sts:AssumeRole," and the environment is not created\.

 **Possible causes:** An AWS Cloud9 service\-linked role doesn't exist in your AWS account\.

 **Recommended solutions:** Create an AWS Cloud9 service\-linked role in your AWS account by running the following command with the AWS Command Line Interface \(AWS CLI\) or the aws\-shell\.

```
aws iam create-service-linked-role --aws-service-name cloud9.amazonaws.com # For the AWS CLI.
iam create-service-linked-role --aws-service-name cloud9.amazonaws.com     # For the aws-shell.
```

If you cannot do this, check with your AWS account administrator\.

After you run this command, try creating the environment again\.

\([back to top](#troubleshooting)\)

## Console error: "User is not authorized to perform action on resource"<a name="troubleshooting-access-not-authorized"></a>

 **Issue:** When you try to use the AWS Cloud9 console to create or manage an AWS Cloud9 development environment, you see an error that contains a phrase similar to "User arn:aws:iam::123456789012:user/MyUser is not authorized to perform cloud9:action on resource arn:aws:cloud9:us\-east\-2:123456789012:environment:12a34567b8cd9012345ef67abcd890e1," where:
+  `arn:aws:iam::123456789012:user/MyUser` is the Amazon Resource Name \(ARN\) of the requesting user\.
+  `action` is the name of the operation that the user requested\.
+  `arn:aws:cloud9:us-east-2:123456789012:environment:12a34567b8cd9012345ef67abcd890e1` is the ARN of the environment that the user requested to run the operation\.

 **Cause:** The user you signed in to the AWS Cloud9 console with doesn't have the correct AWS access permissions to perform the action\.

 **Solution:** Ensure the user has the correct AWS access permissions, and then try to perform the action again\. For more information, see one or more of the following:
+  [Step 3: Add AWS Cloud9 Access Permissions to the Group](setup.md#setup-give-user-access) in *Team Setup* 
+  [Step 6\. Enable Groups and Users within the Organization to Use AWS Cloud9](setup-enterprise.md#setup-enterprise-groups-users-access) in *Enterprise Setup* 
+  [About Environment Member Access Roles](share-environment.md#share-environment-member-roles) in *Working with Shared Environments* 

\([back to top](#troubleshooting)\)

## Federated identities cannot create environments<a name="troubleshooting-federated-service-role"></a>

 **Issue:** When you try to use an AWS federated identity to create an AWS Cloud9 development environment, an access error message is displayed, and the environment isn't created\.

 **Cause:** : AWS Cloud9 uses service\-linked roles\. The service\-linked role is created the first time an environment is created in an account using the `iam:CreateServiceLinkedRole` call\. However, federated users can't call IAM APIs\. For more information, see [GetFederationToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_API_GetFederationToken.html) in the *AWS Security Token Service API Reference*\.

 **Solution:** Ask an AWS account administrator to create the service\-linked role for AWS Cloud9 either in the IAM console or by running this command with the AWS Command Line Interface \(AWS CLI\):

```
aws iam create-service-linked-role --aws-service-name cloud9.amazonaws.com
```

Or this command with the aws\-shell:

```
iam create-service-linked-role --aws-service-name cloud9.amazonaws.com
```

For more information, see [Using Service\-Linked Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) in the *IAM User Guide*\.

\([back to top](#troubleshooting)\)

## Cannot open an environment<a name="troubleshooting-env-loading"></a>

 **Issue:** When you try to open an environment, the IDE does not display for a long time \(after at least five minutes\)\.

 **Possible causes:** 
+ The IAM user that is signed in to the AWS Cloud9 console does not have the required AWS access permissions to open the environment\.
+ If the environment is associated with an AWS cloud compute instance \(for example an Amazon EC2 instance\):
  + The instance's associated VPC is not set to the correct settings for AWS Cloud9\.
  + The instance is transitioning between states or is failing automated status checks, during the time when AWS Cloud9 is trying to connect to the instance\.
+ If the environment is an SSH environment, the associated cloud compute instance or your own server is not set up correctly to allow AWS Cloud9 to access it\.

 **Recommended solutions:** 
+ Make sure the IAM user that is signed in to the AWS Cloud9 console has the required AWS access permissions to open the environment, and then try opening the environment again\. For more information see the following, or check with your AWS account administrator:
  +  [Step 3: Add AWS Cloud9 Access Permissions to the Group](setup.md#setup-give-user-access) in *Team Setup* 
  +  [AWS managed \(predefined\) policies for AWS Cloud9](how-cloud9-with-iam.md#sec-auth-and-access-control-managed-policies) in *Authentication and Access Control* 
  +  [Customer\-Managed Policy Examples for Teams Using AWS Cloud9](setup-teams.md#setup-teams-policy-examples) in *Advanced Team Setup* 
  +  [Customer\-Managed Policy Examples](auth-and-access-control.md#auth-and-access-control-customer-policies-examples) in *Authentication and Access Control* 
  +  [Changing Permissions for an IAM User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html) in the *IAM User Guide*
  +  [Troubleshoot IAM Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_policies.html) in the *IAM User Guide*

  If the signed\-in IAM user still cannot open the environment, you could try signing out and then signing back in as either the AWS account root user or an IAM administrator user in the account\. Then try opening the environment again\. If you are able to open the environment in this way, then there is most likely a problem with the IAM user's access permissions\.
+ If the environment is associated with an AWS cloud compute instance \(for example an Amazon EC2 instance\):
  + Make sure the instance's associated VPC is set to the correct settings for AWS Cloud9, and then try opening the environment again\. For details, see [Amazon VPC requirements for AWS Cloud9](vpc-settings.md#vpc-settings-requirements)\.

    If the AWS cloud compute instance's associated VPC is set to the correct settings for AWS Cloud9 and you still cannot open the environment, the instance's security group might be preventing access to AWS Cloud9\. **As a troubleshooting technique only**, check the security group to make sure that at minimum, inbound SSH traffic is allowed over port 22 for all IP addresses \(`Anywhere` or `0.0.0.0/0`\)\. For instructions, see [Describing Your Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html#describing-security-group) and [Updating Security Group Rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html#updating-security-group-rules) in the *Amazon EC2 User Guide for Linux Instances*\.

    For additional VPC troubleshooting steps, watch the related 5\-minute video [AWS Knowledge Center Videos: What can I check if I cannot connect to an instance in a VPC?](https://www.youtube.com/watch?v=--BoDeCF5Dw) on the YouTube website\.
**Warning**  
When you have finished troubleshooting, be sure to set the inbound rules to an appropriate address range, as described in [Inbound SSH IP address ranges for AWS Cloud9](ip-ranges.md)\.
  + Restart the instance, make sure the instance is running and has passed all system checks, and then try opening the environment again\. For details, see [Reboot Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-reboot.html) and [Viewing Status Checks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html#viewing_status) in the *Amazon EC2 User Guide for Linux Instances*\.
+ If the environment is an SSH environment, make sure the associated cloud compute instance or your own server is set up correctly to allow AWS Cloud9 to access it, and then try opening the environment again\. For details, see [AWS Cloud9 SSH Development Environment host requirements](ssh-settings.md)\.

\([back to top](#troubleshooting)\)

## The AWS Cloud9 installer hangs or fails<a name="troubleshooting-ssh-installer"></a>

 **Issue:** When you [download and run the AWS Cloud9 Installer](installer.md#installer-download-run), one or more error messages display, and the installer script does not show `Done`\.

 **Cause:** The AWS Cloud9 Installer has encountered one or more errors that it cannot recover from and therefore fails\.

 **Solution:** See common issues, their possible causes, and recommended solutions, in [Troubleshooting the AWS Cloud9 Installer](installer.md#installer-troubleshooting)\.

\([back to top](#troubleshooting)\)

## SSH environment error: "Python version 2\.7 is required to install pty\.js"<a name="troubleshooting-python-ssh"></a>

 **Issue:** After you open an AWS Cloud9 SSH development environment, the terminal in the AWS Cloud9 IDE displays a message that begins with "Python version 2\.7 is required to install pty\.js\."

 **Cause:** To work as expected, an SSH environment requires that Python version 2\.7 is installed\.

 **Solution:** Install Python version 2\.7 in the environment\. To check your version, from your server's terminal, run the command ** `python --version` **\. To install Python 2\.7 on your server, see one of the following:
+  [Step 1: Install Python 3\.6](sample-python.md#sample-python-install) in the *Python Sample*\.
+  [Download Python](https://www.python.org/downloads/) on the Python website and [Installing Packages](https://packaging.python.org/installing/) in the *Python Packaging User Guide*\.

\([back to top](#troubleshooting)\)

## Application preview or file preview notice: "Third\-party cookies disabled"<a name="troubleshooting-preview"></a>

**Issue:** When you attempt to preview [an application](app-preview.md) or [a file](file-preview.md), a notice is displayed with the following message: "Preview functionality is disabled because your browser has third\-party cookies disabled\."

**Cause:** Although third\-party cookies are not needed to open the AWS Cloud9 IDE, you must enable third\-party cookies to use the Application Preview or File Preview features\.

**Solution:** Enable third\-party cookies in your web browser, reload your IDE, and then try opening the preview again\.
+ Apple Safari: [Manage cookies and website data in Safari](https://support.apple.com/guide/safari/manage-cookies-and-website-data-sfri11471/mac) on the Apple Support website\.
+ Google Chrome: **Change your cookie settings** in [Clear, enable, and manage cookies in Chrome](https://support.google.com/chrome/answer/95647) on the Google Chrome Help website\.
+ Internet Explorer: **Block or allow cookies** in [Delete and manage cookies](https://support.microsoft.com/en-us/help/17442) on the Microsoft Support website\.
+ Microsoft Edge: [Blocking third\-party cookies](https://support.microsoft.com/en-us/help/4464209/issue-with-blocking-third-party-cookies) on the Microsoft Support website\.
+ Mozilla Firefox: **Accept third party cookies** setting in [Enable and disable cookies that websites use to track your preferences](https://support.mozilla.org/kb/enable-and-disable-cookies-website-preferences) on the Mozilla Support website\.
+ Any other web browser: see that web browser's documentation\.

To enable third\-party cookies only for AWS Cloud9 \(if your web browser allows this granularity\), specify the following domains, depending on the supported AWS Regions where you want to use AWS Cloud9\.


****  

|  **AWS Region**  |  **Domains**  | 
| --- | --- | 
|  US East \(N\. Virginia\)  |   `*.vfs.cloud9.us-east-1.amazonaws.com`   `vfs.cloud9.us-east-1.amazonaws.com`   | 
| US East \(Ohio\) |   `*.vfs.cloud9.us-east-2.amazonaws.com`   `vfs.cloud9.us-east-2.amazonaws.com`   | 
| US West \(N\. California\) |   `*.vfs.cloud9.us-west-1.amazonaws.com`   `vfs.cloud9.us-west-1.amazonaws.com`   | 
| US West \(Oregon\) |   `*.vfs.cloud9.us-west-2.amazonaws.com`   `vfs.cloud9.us-west-2.amazonaws.com`   | 
|  Asia Pacific \(Hong Kong\)  |   `*.vfs.cloud9.ap-east-1.amazonaws.com`   `vfs.cloud9.ap-east-1.amazonaws.com`   | 
|  Asia Pacific \(Mumbai\)  |   `*.vfs.cloud9.ap-south-1.amazonaws.com`   `vfs.cloud9.ap-south-1.amazonaws.com`   | 
|  Asia Pacific \(Seoul\)  |   `*.vfs.cloud9.ap-northeast-2.amazonaws.com`   `vfs.cloud9.ap-northeast-2.amazonaws.com`   | 
|  Asia Pacific \(Singapore\)  |   `*.vfs.cloud9.ap-southeast-1.amazonaws.com`   `vfs.cloud9.ap-southeast-1.amazonaws.com`   | 
|  Asia Pacific \(Sydney\)  |   `*.vfs.cloud9.ap-southeast-2.amazonaws.com`   `vfs.cloud9.ap-southeast-2.amazonaws.com`   | 
|  Asia Pacific \(Tokyo\)  |   `*.vfs.cloud9.ap-northeast-1.amazonaws.com`   `vfs.cloud9.ap-northeast-1.amazonaws.com`   | 
|  Canada \(Central\)  |   `*.vfs.cloud9.ca-central-1.amazonaws.com`   `vfs.cloud9.ca-central-1.amazonaws.com`   | 
| Europe \(Frankfurt\) |   `*.vfs.cloud9.eu-central-1.amazonaws.com`   `vfs.cloud9.eu-central-1.amazonaws.com`   | 
| Europe \(Ireland\) |   `*.vfs.cloud9.eu-west-1.amazonaws.com`   `vfs.cloud9.eu-west-1.amazonaws.com`   | 
|  Europe \(London\)  |   `*.vfs.cloud9.eu-west-2.amazonaws.com`   `vfs.cloud9.eu-west-2.amazonaws.com`   | 
|  Europe \(Paris\)  |   `*.vfs.cloud9.eu-west-3.amazonaws.com`   `vfs.cloud9.eu-west-3.amazonaws.com`   | 
|  Europe \(Stockholm\)  |   `*.vfs.cloud9.eu-north-1.amazonaws.com`   `vfs.cloud9.eu-north-1.amazonaws.com`   | 
|  Middle East \(Bahrain\)  |   `*.vfs.cloud9.me-south-1.amazonaws.com`   `vfs.cloud9.me-south-1.amazonaws.com`   | 
|  South America \(São Paulo\)  |   `*.vfs.cloud9.sa-east-1.amazonaws.com`   `vfs.cloud9.sa-east-1.amazonaws.com`   | 

\([back to top](#troubleshooting)\)

## Application preview tab displays an error or is blank<a name="troubleshooting-app-preview"></a>

 **Issue:** On the menu bar in the IDE, when you choose **Preview, Preview Running Application** or **Tools, Preview, Preview Running Application** to try to display your application on a preview tab in the IDE, the tab displays an error, or the tab is blank\.

 **Possible causes:** 
+ Your application is not running in the IDE\.
+ Your application is not running using HTTP\.
+ Your application is running over more than one port\.
+ Your application is running over a port other than `8080`, `8081`, or `8082`\.
+ Your application is running with an IP other than `127.0.0.1`, `localhost`, or `0.0.0.0`\.
+ The port \(`8080`, `8081`, or `8082`\) is not specified in the URL on the preview tab\.
+ Your network blocks inbound traffic to ports `8080`, `8081`, or `8082`\.
+ You are trying to go to an address that contains an IP of `127.0.0.1`, `localhost`, or `0.0.0.0`\. The default, built\-in behavior of the AWS Cloud9 IDE is that this will attempt to go to your local computer instead of attempting to go the instance or your own server that is connected to the environment\.

 **Recommended solutions:** 
+ Ensure that the application is running in the IDE\.
+ Ensure that the application is running using HTTP\. For examples in Node\.js and Python, see [Run an application](app-preview.md#app-preview-run-app)\.
+ Ensure that the application is running over only one port\. For examples in Node\.js and Python, see [Run an application](app-preview.md#app-preview-run-app)\.
+ Ensure that the application is running over port `8080`, `8081`, or `8082`\. For examples in Node\.js and Python, see [Run an application](app-preview.md#app-preview-run-app)\.
+ Ensure that the application is running with an IP of `127.0.0.1`, `localhost`, or `0.0.0.0`\. For examples in Node\.js and Python, see [Run an application](app-preview.md#app-preview-run-app)\.
+ Add `:8080`, `:8081`, or `:8082` to the URL on the preview tab\.
+ Ensure that your network allows inbound traffic over ports `8080`, `8081`, or `8082`\. If you cannot make changes to your network, see your network administrator\.
+ If you are trying to go to an address that contains an IP of `127.0.0.1`, `localhost`, or `0.0.0.0`, try going to the following address instead: `https://12a34567b8cd9012345ef67abcd890e1.vfs.cloud9.us-east-2.amazonaws.com/`, where `12a34567b8cd9012345ef67abcd890e1` is the ID that AWS Cloud9 assigns to the environment, and `us-east-2` is the ID of the AWS Region for the environment\. You can also try to go to this address outside of the IDE, but it works only when the IDE for the environment is open and the application is running in the same web browser\.
+ After you are sure that all of the preceding conditions are met, try stopping the application and then starting it again\.
+ If you stopped the application and then started it again, try choosing **Preview, Preview Running Application** or **Tools, Preview, Preview Running Application** on the menu bar again\. Or try choosing the **Refresh** button \(the circular arrow\) on the corresponding application preview tab, if the tab is already visible\.

\([back to top](#troubleshooting)\)

## Cannot display your running application outside of the IDE<a name="troubleshooting-app-sharing"></a>

 **Issue:** When you or others try to display your running application in a web browser tab outside of the IDE, that web browser tab displays an error, or the tab is blank\.

 **Possible causes:** 
+ The application is not running in the IDE\.
+ The application is running with an IP of `127.0.0.1` or `localhost`\.
+ The application is running in an AWS Cloud9 EC2 development environment, and one or more security groups that are associated with the corresponding Amazon EC2 instance do not allow inbound traffic over the protocols, ports, or IP addresses that the application requires\.
+ The application is running in an AWS Cloud9 SSH development environment for an AWS cloud compute instance \(for example an Amazon EC2 instance\), and the network ACL for the subnet in the virtual private cloud \(VPC\) that is associated with the corresponding instance does not allow inbound traffic over the protocols, ports, or IP addresses that the application requires\.
+ The URL is incorrect\.
+ The URL in the application preview tab is being requested instead of the instance's public IP address\.
+ You are trying to go to an address that contains an IP of `127.0.0.1` or `localhost`\. These IPs will attempt to access resources on your local computer instead of resources in the environment\.
+ The instance's public IP address has changed\.
+ The web request originates from a virtual private network \(VPN\) that blocks traffic over the protocols, ports, or IP addresses that the application requires\.
+ The application is running in an SSH environment, and your server or the associated network does not allow traffic over the protocols, ports, or IP addresses that the application requires\.

 **Recommended solutions:** 
+ Ensure that the application is running in the IDE\.
+ Ensure that the application is not running with an IP of `127.0.0.1` or `localhost`\. For some examples in Node\.js and Python, see [Run an application](app-preview.md#app-preview-run-app)\.
+ If the application is running on an AWS cloud compute instance \(for example an Amazon EC2 instance\), ensure all security groups that are associated with the corresponding instance allow inbound traffic over the protocols, ports, and IP addresses that the application requires\. For instructions, see [Step 2: Set up the security group for the instance](app-preview.md#app-preview-share-security-group) in *Share a Running Application over the Internet*\. See also [Security Groups for Your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) in the *Amazon VPC User Guide*\.
+ If the application is running on an AWS cloud compute instance, and a network ACL exists for the subnet in the VPC that is associated with the corresponding instance, ensure that network ACL allows inbound traffic over the protocols, ports, and IP addresses that the application requires\. For instructions, see [Step 3: Set up the subnet for the instance](app-preview.md#app-preview-share-subnet) in *Share a Running Application over the Internet*\. See also [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_ACLs.html) in the *Amazon VPC User Guide*\.
+ Ensure that the requesting URL, including the protocol \(and port, if it must be specified\), is correct\. For more information, see [Step 5: Share the running application URL](app-preview.md#app-preview-share-url) in *Share a Running Application over the Internet*\.
+ We do not recommend requesting a URL with the format `https://12a34567b8cd9012345ef67abcd890e1.vfs.cloud9.us-east-2.amazonaws.com/` \(where `12a34567b8cd9012345ef67abcd890e1` is the ID that AWS Cloud9 assigns to the environment, and `us-east-2` is the ID of the AWS Region for the environment\)\. This URL works only when the IDE for the environment is open and the application is running in the same web browser\.
+ If you are trying to go to an address that contains an IP of `127.0.0.1` or `localhost`, try going to the correct non\-local address for the running application instead\. For more information, see [Share a running application over the internet](app-preview.md#app-preview-share)\.
+ If the application is running on an AWS cloud compute instance, determine whether the instance's public IP address has changed\. The instance's public IP address might change anytime the instance restarts\. To prevent this IP address from changing, you can allocate an Elastic IP address and assign it to the running instance\. For more information, see [Step 5: Share the running application URL](app-preview.md#app-preview-share-url) in *Share a Running Application over the Internet*\.
+ If the web request originates from a VPN, ensure that VPN allows traffic over the protocols, ports, and IP addresses that the application requires\. If you cannot make changes to your VPN, see your network administrator\. Or make the web request from a different network if possible\.
+ If the application is running in an SSH environment for your own server, ensure your server and the associated network allow traffic over the protocols, ports, and IP addresses that the application requires\. If you cannot make changes to your server or the associated network, see your server or network administrator\.
+ Try running the application from a terminal in the environment by running the `curl` command, followed by the URL\. If this command displays an error message, there might be some other issue that is not related to AWS Cloud9\.

\([back to top](#troubleshooting)\)

## After reloading an environment, you must refresh application preview<a name="troubleshooting-app-preview-refresh"></a>

 **Issue:** After you reload an environment that displays an application preview tab, the tab doesn't display the application preview\.

 **Cause:** Sometimes users write code that can run an infinite loop or that otherwise uses so much memory that the AWS Cloud9 IDE can pause or stop when the application preview is running\. To keep this from happening, AWS Cloud9 doesn't reload application preview tabs whenever an environment is reloaded\.

 **Solution:** After you reload an environment that displays an application preview tab, to display the application preview, choose the **Click to load the page** button on the tab\.

\([back to top](#troubleshooting)\)

## Unable to preview application in the AWS Cloud9 IDE with HTTP<a name="troubleshooting-app-preview-http"></a>

 **Issue:** In the address box of an application preview tab in the AWS Cloud9 IDE, the URL always starts with `https`\. If you try to change `https` in the box to `http` and then press `Enter`, the tab doesn't display the application preview\.

 **Cause:** To help improve code safety, in the address box of the application preview tab in the IDE, AWS Cloud9 always uses `https`\. This behavior cannot be changed\.

 **Solution:** To view an application preview with an address starting with `http` instead of `https`, change `https` in the address box of the tab to `http` and then press `Enter`\. Then choose the `Open your page in a new tab` button\. This displays the application preview in a separate web browser tab using HTTP\.

\([back to top](#troubleshooting)\)

## Cannot run some commands or scripts in an EC2 environment<a name="troubleshooting-rhel-ubuntu"></a>

 **Issue:** After you open an AWS Cloud9 EC2 development environment, you cannot install some types of packages, run commands such as `yum` or `apt`, or run scripts containing commands that typically work with other Linux operating systems\.

 **Cause:** The Amazon EC2 instances that AWS Cloud9 uses for an EC2 environment rely on either Amazon Linux \(which is based on Red Hat Enterprise Linux \(RHEL\)\) or Ubuntu Server\.

 **Solution:** If you install or manage packages or run commands or scripts in the IDE for an EC2 environment, ensure they are compatible with either RHEL \(for Amazon Linux\) or Ubuntu Server, depending on the instance for that environment\.

\([back to top](#troubleshooting)\)

## AWS CLI / aws\-shell error: "The security token included in the request is invalid" in an EC2 environment<a name="troubleshooting-cli-invalid-token"></a>

 **Issue:** When you try to use the AWS Command Line Interface \(AWS CLI\) or the aws\-shell to run a command in the AWS Cloud9 IDE for an EC2 environment, an error displays: "The security token included in the request is invalid\."

 **Possible causes:** 
+ If you have AWS managed temporary credentials enabled, you are trying to run a command that is not allowed with those AWS managed temporary credentials\. For a list of allowed commands, see [Actions supported by AWS managed temporary credentials](how-cloud9-with-iam.md#sec-auth-and-access-control-temporary-managed-credentials-supported)\.
+ If you have AWS managed temporary credentials enabled and the environment is a shared environment, the environment owner has not opened the environment within the past 12 hours so that AWS Cloud9 can refresh AWS managed temporary credentials in the environment\. \(AWS Cloud9 sets this 12\-hour limit as an AWS security best practice\.\)

 **Recommended solutions:** 
+ If you have AWS managed temporary credentials enabled, run allowed commands only\. If you must run a command that is not allowed by AWS managed temporary credentials, one approach would be to configure the AWS CLI or aws\-shell in the environment with a set of permanent credentials, which removes this limitation\. For instructions, see [Create and Store Permanent Access Credentials in an Environment](credentials.md#credentials-permanent-create)\.
+ Have the environment owner open the environment so that AWS Cloud9 can refresh temporary credentials in the environment\.

For more information, see [AWS managed temporary credentials](how-cloud9-with-iam.md#sec-auth-and-access-control-temporary-managed-credentials)\.

\([back to top](#troubleshooting)\)

## Amazon EC2 instances are not automatically updated<a name="troubleshooting-update-ami"></a>

 **Issue:** Recent system updates are not automatically applied to an Amazon EC2 instance that connects to an AWS Cloud9 development environment\.

 **Cause:** Automatically applying recent system updates could cause your code or the Amazon EC2 instance to behave in unexpected ways, without your prior knowledge or approval\.

 **Recommended solutions:** 

Apply system updates to the Amazon EC2 instance on a regular basis by following the instructions in [Updating Instance Software](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-updates.html) in the *Amazon EC2 User Guide for Linux Instances*\.

To run commands on the instance, you can use a terminal session in the AWS Cloud9 IDE from the environment that is connected to the instance\.

Alternatively, you can use an SSH remote access utility such as **ssh** or PuTTY to connect to the instance\. To do this, from your local computer, use an SSH key pair creation utility such as **ssh\-keygen** or PuTTYgen\. Use the AWS Cloud9 IDE from the environment that is connected to the instance to store the generated public key on the instance\. Then use the SSH remote access utility along with the generate private key to access the instance\. For more information, see your utility's documentation\.

\([back to top](#troubleshooting)\)

## Lambda local function run error: Cannot install SAM Local<a name="troubleshooting-install-sam-local"></a>

 **Issue:** After you try to run the local version of an AWS Lambda function in the AWS Cloud9 IDE, a dialog box is displayed, stating that AWS Cloud9 is having trouble installing SAM Local\. AWS Cloud9 needs SAM Local to run local versions of AWS Lambda functions in the IDE\. Until SAM Local is installed, you cannot run local versions of Lambda functions in the IDE\.

 **Cause:** AWS Cloud9 can't find SAM Local at the expected path in the environment, which is `~/.c9/bin/sam`\. This is because SAM Local is not yet installed, or if it is installed, AWS Cloud9 can't find it at that location\.

 **Recommended solutions:** You can wait for AWS Cloud9 to try to finish installing SAM Local, or you can install it yourself\.

To see how AWS Cloud9 is doing with attempting to install SAM Local, choose **Window, Installer** on the menu bar\.

To install SAM Local yourself, run the following commands, one at a time in the following order, from a terminal session in the IDE\.

```
npm install -g aws-sam-local        # Use Node Package Manager (npm) to install SAM Local as a global package in the environment.
ln -sfn $(which sam) ~/.c9/bin/sam  # Create a symbolic link (a shortcut) from the path that AWS Cloud9 expects to where SAM Local is installed.
```

If, after running the previous commands, you're still having SAM Local install issues, try running the following additional commands, one at a time in the following order, from a terminal session in the IDE\.

```
npm uninstall -g aws-sam-local  # Use npm to uninstall the globally-installed SAM Local from the environment.
rm -rf $(which sam)             # Remove the related symbolic link.
pip install --user aws-sam-cli  # Use pip to re-install the AWS SAM CLI from the context of the user (not globally).
hash -r                         # Reset the bash cache (removes all current tracked aliases).
sam –-version                   # Verify that your installation worked.
```

For more information, see the [awslabs/aws\-sam\-cli](https://github.com/awslabs/aws-sam-cli/blob/develop/README.md) repository on the GitHub website\.

\([back to top](#troubleshooting)\)

## IDE warning: "This environment is running low on memory" or "This environment has high CPU load"<a name="troubleshooting-ide-low-memory"></a>

 **Issue:** While the IDE is running, you see a message that contains the phrase "this environment is running low on memory" or "this environment has high CPU load\."

 **Cause:** The IDE might not have enough compute resources available to continue running without delays or hangs\.

 **Recommended solutions:** 
+ Stop one or more running processes to free up available memory\. To do this, on the menu bar in the IDE for the environment, choose **Tools, Process List**\. For each process you want to stop, choose the process, and then choose **Force Kill**\.
+ Create a swap file in the environment\. A *swap file* is a file in the environment that the operating system can use as virtual memory\.

  To confirm whether the environment is currently using swap memory, run the ** `top` ** command in a terminal session in the environment\. If swap memory is being used, the output displays non\-zero `Swap` memory statistics \(for example, `Swap: 499996k total, 1280k used, 498716 free, 110672k cached`\)\. To stop showing real\-time memory information, press `Ctrl + C`\.

  To create a swap file, you could run a command such as the following in the environment\.

  ```
  sudo fallocate --length 512MB /var/swapfile && sudo chmod 600 /var/swapfile && sudo mkswap /var/swapfile && echo '/var/swapfile swap swap defaults 0 0' | sudo tee -a /etc/fstab > /dev/null
  ```

  The preceding command does the following:

  1. Creates a 512 MB file named `swapfile` in the `/var` directory\.

  1. Changes access permissions for the `swapfile` file to read\-write for the owner only\.

  1. Sets up the `swapfile` file as a swap file\.

  1. Writes information to the `/etc/fstab file`, which makes this swap file available whenever the system reboots\.

  After you run the preceding command, to make this swap file available immediately instead of waiting for a reboot, run the following command\.

  ```
  sudo swapon /var/swapfile
  ```
+ Move or resize the environment to an instance or server with more compute resources\. To move or resize Amazon EC2 instances, see [Moving an environment and resizing or encrypting Amazon EBS volumes](move-environment.md)\. For other instance or server types, refer to your instance's or server's documentation\.

\([back to top](#troubleshooting)\)

## Previewing a file returns a 499 error<a name="troubleshooting-file-preview-script-block"></a>

 **Issue:** When you try to use the AWS Cloud9 IDE to preview a file that contains a `<script>` element containing the `src` attribute and with the `type` attribute set to `module`, a 499 error occurs and the script doesn't run as expected\.

 **Cause:** File preview fetch requests in the AWS Cloud9 IDE require cookies to be sent by the web browser to authenticate\. By default, web browsers send cookies for regular script requests, but not for module script requests, unless you add the `crossorigin` attribute\.

 **Solution:** Add the `crossorigin` attribute to the `<script>` element\. For example, `<script type="module" src="index.js" crossorigin></script>`\. Then save the changed file, and try to preview the it again\.

\([back to top](#troubleshooting)\)

## Environment deletion error: "One or more environments failed to delete"<a name="troubleshooting-delete-environment"></a>

**Issue:** When you try to delete one or more environments in the AWS Cloud9 console, a message is displayed that reads "one or more environments failed to delete," and at least one of the environments is not deleted\.

**Possible cause:** AWS CloudFormation might have a problem deleting one or more of the environments\. \(AWS Cloud9 relies on AWS CloudFormation to create and delete environments\.\)

**Recommended solution:** Try using AWS CloudFormation to delete each of the undeleted environments, as follows\.

1. Open the AWS CloudFormation console at [https://console\.aws\.amazon\.com/cloudformation](https://console.aws.amazon.com/cloudformation/)\.

1. On the AWS navigation bar, choose the AWS Region for the environment\.

1. In the list of AWS CloudFormation stacks, select the entry where **Stack name** contains the undeleted environment name and **Status** is **DELETE\_FAILED**\. For example, if the environment name is **my\-demo\-environment**, choose the stack that begins with the name **aws\-cloud9\-my\-demo\-environment**\. \(Choose the box or option next to the environment name, not the environment name itself\.\)

1. Choose **Actions, Delete Stack**\.

1. If prompted, choose **Yes, Delete**\.

The process of deleting a stack might take a few minutes\.

If the stack disappears from the list, the environment is now deleted\.

If the stack is still displays displayed with **DELETE\_FAILED** after a few minutes, the environment is still not deleted\. In this case, you can try to manually delete each of the failed stack's resources\.

**Note**  
Manually deleting a failed stack's resources doesn't remove the stack itself from your AWS account\.

To manually delete these resources, in the AWS CloudFormation console, choose the failed stack, and then select the **Resources** section\. Go to the console in AWS for each resource in this list, and then use that console to manually delete the resource\.

\([back to top](#troubleshooting)\)

## Console warning: "Switching to the minimal code completion engine\.\.\."<a name="troubleshooting-minimal-code-completion"></a>

**Issue:** When working in the AWS Cloud9 console \(for example, when opening the IDE or refreshing the IDE's web page\), you see this message: "One or more sessions or collaborators are active on this environment\. Switching to the minimal code completion engine to conserve memory\." In correlation with this message, the code\-completion behavior might be slow or intermittent\.

**Cause:** Running the code\-completion engine takes memory and CPU cycles from the environment\. Additionally, a separate code\-completion engine is required for each collaborator and each additional session\. To avoid using too many resources, especially on small instance sizes like t2\.nano and t2\.micro, AWS Cloud9 switches to the minimal code\-completion engine\.

**Recommended solution:** If you will be collaborating often and for long periods of time, choose a larger Amazon EC2 instance when creating your EC2 environment \(or connect your SSH environment to an instance with more capacity\)\.

**Note**  
Choosing a larger Amazon EC2 instance might result in additional charges to your AWS account\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/)\.

\([back to top](#troubleshooting)\)

## AWS Cloud9 installer doesn't finish after displaying: "Package Cloud9 IDE 1"<a name="cloud9-installer-failed"></a>

**Issue:** AWS Cloud9 is installed on your existing Amazon EC2 instance or on your own server as part of the process of creating an SSH development environment\. The installation stalls after you see this message in the **AWS Cloud9 Installer** dialog box: "Package Cloud9 IDE 1"\. If you choose **Cancel**, you see the following message: "Installation Failed\." This error occurs when AWS Cloud9 packages can't be installed on the customer's SSH host\.

**Cause:** An SSH host requires that you have Node\.js installed\. We currently support versions from **Node\.js 0\.6\.16** to **Node\.js 12\.x** An installation error can occur if you have a version of Node\.js on your host that AWS Cloud9 doesn't support\.

**Recommended solution: **Install a version of **Node\.js** that AWS Cloud9 supports on your SSH host\.

## VPC error for EC2\-Classic accounts: "Unable to access your environment"<a name="ec2-classic-issue"></a>

**Issue:** EC2\-Classic was introduced in the original release of Amazon EC2\. If you're using an AWS account that was set up before December 4, 2013, this error might occur if you don't explicitly configure a *virtual private cloud* \(Amazon VPC\) and subnet when creating an AWS Cloud9 EC2 development environment\.

 If you accept the default VPC settings, the Amazon EC2 instance is launched into the EC2\-Classic network and not into a subnet of the default VPC\. The following message is displayed when the creation of the environment fails: 

 Environment Error

Unable to access your environment

The environment creation failed with the error: The following resource\(s\) failed to create: \[Instance\]\. \. Rollback requested by user\.\.

You can confirm that the error is caused by the EC2 instance not being in the default VPC\. Use AWS CloudFormation to view the stack event history for the development environment\.

1. Open the AWS CloudFormation console\. For more information, see [Logging in to the AWS CloudFormation console\.](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-login.html)

1. In the AWS CloudFormation console, choose **Stacks**\.

1. On the **Stacks** page, choose the name of the development environment that failed to create\.

1. On the **Stack details** page, choose the **Events** tab and check for the following entry****:

    Status: CREATE\_FAILED

   Status reason: The AssociatePublicIpAddress parameter is only supported by VPC launches\. \[\.\.\.\] 

**Cause:** An AWS Cloud9 development environment must be associated with an Amazon VPC that meets specific VPC requirements\. For accounts with EC2\-Classic enabled, accepting the default network settings when [creating an EC2 environment](create-environment.md) means that the required EC2 instance isn't launched into the VPC\. Instead, the instance is launched into the EC2\-Classic network\.

 **Recommended solution:** With an EC2\-Classic account, you must select a VPC and subnet when [creating an EC2 environment](create-environment.md)\. On the **Configure settings** page, in the **Network settings \(advanced\)** section, select the VPC and subnet that you can launch your EC2 instance into\.