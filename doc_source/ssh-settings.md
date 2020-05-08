# AWS Cloud9 SSH Development Environment Host Requirements<a name="ssh-settings"></a>

To instruct AWS Cloud9 to connect an environment to an existing cloud compute instance or your own server, you create an *AWS Cloud9 SSH development environment*\. However, before you create an SSH environment, you should consider the benefits of creating EC2 environments instead\. 

When you create an EC2 environment, AWS Cloud9 creates a new environment, requests Amazon EC2 to launch a new instance, and then connects the newly launched instance to the new environment\. Creating an EC2 environment has the following benefits:
+  **Automatic instance launching\.** When you create an EC2 environment, AWS Cloud9 requests Amazon EC2 to create a new instance at the same time\. In an SSH environment, you must provide an existing cloud compute instance \(for example an Amazon EC2 instance\) or your own server yourself\.
+  **Automatic instance shutdown\.** By default, AWS Cloud9 automatically shuts down the EC2 environment 30 minutes after all web browser instances that are connected to the IDE for the EC2 environment are closed\. \(You can change this behavior at any time\.\) This helps reduce additional charges to your AWS account for using Amazon EC2\.
+  **Automatic instance cleanup\.** When you delete an EC2 environment, the connected Amazon EC2 instance is automatically deleted\. This also helps reduce additional charges to your AWS account for using Amazon EC2\. In an SSH environment that is connected to cloud compute instance, you must remember to delete the instance yourself\.

If you want to create an EC2 environment instead, see [Creating an EC2 Environment](create-environment-main.md)\. Otherwise, continue reading for information about creating SSH environments\.

## When and How to Create an SSH Environment<a name="when-and-how-to-create-an-envsshtitle"></a>

You must create an SSH environment instead of an EC2 environment whenever any of the following is true:


****  

|  **Requirement**  |  **Directions**  | 
| --- | --- | 
|  You don't want to incur additional charges to your AWS account for using AWS cloud compute instances, so you decide to connect AWS Cloud9 to an existing cloud compute instance outside of AWS or your own server instead\.  |  [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/ssh-settings.html)  | 
|  You want to use an existing AWS cloud compute instance \(for example an Amazon EC2 instance\) in your AWS account instead of having AWS Cloud9 to launch a new instance at the same time the environment is created\.  |  [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/ssh-settings.html)  | 
|  You want to use an Amazon EC2 instance type that AWS Cloud9 currently doesn't support for an EC2 environment \(for example, R4\)\.  |  [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/ssh-settings.html)  | 
|  You want to use an Amazon EC2 instance that is based on an Amazon Machine Image \(AMI\) other than Amazon Linux or Ubuntu Server\.  |  [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/ssh-settings.html)  | 
|  You want to connect multiple environments to a single existing cloud compute instance or your own server\.  |  [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/ssh-settings.html)  | 

**Note**  
Launching an Amazon EC2 instance might result in possible charges to your AWS account for Amazon EC2\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/)\.

## SSH Host Requirements<a name="ssh-settings-requirements"></a>

The existing cloud compute instance or your own server must meet the following requirements for AWS Cloud9 to connect it to an SSH environment\.
+ It must run Linux\. \(AWS Cloud9 doesn't support Windows\.\)
+ It must be reachable over the public internet by using SSH\. If it is reachable only through a virtual private cloud \(VPC\) or virtual private network \(VPN\), that VPC or VPN must have access to the public internet\.
+ If the host is an existing AWS cloud compute instance that is part of an Amazon Virtual Private Cloud \(Amazon VPC\), there are additional requirements\. See [Amazon VPC Settings](vpc-settings.md)\.
+ It must have Python installed, and the **version must be 2\.7**\. To check the version, from the existing instance's or server's terminal, run the command ** `python --version` **\. To install Python 2\.7 on the instance or server, see one of the following:
  +  [Step 1: Install Required Tools](sample-python.md#sample-python-install) in the *Python Sample*\.
  +  [Download Python](https://www.python.org/downloads/) from the Python website and see [Installing Packages](https://packaging.python.org/installing/) in the *Python Packaging User Guide*\.
**Note**  
To connect to an existing AWS cloud compute instance to verify and meet requirements, see one or more of the following resources:  
For Amazon EC2, see [Connect to Your Linux Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html) in the *Amazon EC2 User Guide for Linux Instances*\.
For Amazon Lightsail, see [Connect to your Linux/Unix\-based Lightsail instance](https://lightsail.aws.amazon.com/ls/docs/how-to/article/lightsail-how-to-connect-to-your-instance-virtual-private-server) in the *Amazon Lightsail Documentation*\.
For AWS Elastic Beanstalk, see [Listing and Connecting to Server Instances](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.ec2connect.html) in the *AWS Elastic Beanstalk Developer Guide*\.
For AWS OpsWorks, see [Using SSH to Log In to a Linux Instance](https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-ssh.html) in the *AWS OpsWorks User Guide*\.
For other AWS services, see the service's [documentation](https://aws.amazon.com/documentation/)\.
To connect to your own server to verify and meet requirements, you could search the internet using a phrase such as "connect to a server by using the ssh command" \(from macOS or Linux\) or "connect to a server by using PuTTY" \(from Windows\)\.
+ It must have Node\.js installed, and the **version must be 0\.6\.16 or later**\. To check the version, from the existing instance's or server's terminal, run the command ** `node --version` **\. To install Node\.js on the instance or server, see one of the following:
  +  [Step 1: Install Required Tools](sample-nodejs.md#sample-nodejs-install) in the *Node\.js Sample*\.
  +  [Installing Node\.js via package manager](https://nodejs.org/en/download/package-manager/) on the Node\.js website\.
  +  [Node Version Manager](http://nvm.sh) on GitHub\.
+ The path to the directory on the existing instance or server that you want AWS Cloud9 to start from after login must have its access permissions set to `rwxr-xr-x`\. This means read\-write\-execute permissions for the owner that corresponds to the login name that you specify in the [create environment wizard](create-environment-ssh.md) for **User** on the **Configure settings** page, read\-execute permissions for the group that this owner belongs to, and read\-execute permissions for others\.

  For example, if the directory's path is `~` \(where `~` represents the home directory for the login name that you specify for **User** on the **Configure settings** page\), you can set these permissions on the directory by running the ** `chmod` ** command on the instance or server, as follows\.

  ```
  sudo chmod u=rwx,g=rx,o=rx ~
  ```
+  [Download and run the AWS Cloud9 Installer](installer.md#installer-download-run) on the existing instance or server\.
+ Optionally, you can restrict inbound traffic over SSH to only the IP addresses that AWS Cloud9 uses\. To do this, set inbound SSH traffic to the IP ranges as described in [Inbound SSH IP address ranges for AWS Cloud9](ip-ranges.md)\.

After you are sure your instance or server meets the preceding requirements, [create an SSH environment](create-environment-ssh.md) for AWS Cloud9 to connect it to\.