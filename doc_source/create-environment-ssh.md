# Creating an SSH Environment<a name="create-environment-ssh"></a>

You create an AWS Cloud9 SSH development environment with the AWS Cloud9 console\. \(You can't create an SSH environment with code\.\)

## Prerequisites<a name="prerequisites"></a>
+ Make sure you completed the steps in [Setting up AWS Cloud9](setting-up.md) first, so that you can sign in to the AWS Cloud9 console and create environments\.
+ Identify an existing cloud compute instance \(for example an Amazon EC2 instance in your AWS account\), or your own server, that you want AWS Cloud9 to connect to the environment\.
+ Make sure that the existing instance or your own server meets all of the [SSH host requirements](ssh-settings.md#ssh-settings-requirements)\. This includes having specific versions of Python, Node\.js, and other components installed, setting specific permissions on the directory that you want AWS Cloud9 to start from after login, and setting up any associated Amazon Virtual Private Cloud\.

## Create the SSH Environment<a name="create-the-envsshtitle"></a>

1. Make sure you completed the preceding prerequisites\.

1. Connect to your existing instance or your own server by using an SSH client, if you aren't already connected to it\. You must do this so that you can add the necessary public SSH key value to the instance or server, as described later in this procedure\.
**Note**  
To connect to an existing AWS Cloud compute instance, see one or more of the following resources:  
For Amazon EC2, see [Connect to Your Linux Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html) in the *Amazon EC2 User Guide for Linux Instances*\.
For Amazon Lightsail, see [Connect to your Linux/Unix\-based Lightsail instance](https://lightsail.aws.amazon.com/ls/docs/how-to/article/lightsail-how-to-connect-to-your-instance-virtual-private-server) in the *Amazon Lightsail Documentation*\.
For AWS Elastic Beanstalk, see [Listing and Connecting to Server Instances](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.ec2connect.html) in the *AWS Elastic Beanstalk Developer Guide*\.
For AWS OpsWorks, see [Using SSH to Log In to a Linux Instance](https://docs.aws.amazon.com/opsworks/latest/userguide/workinginstances-ssh.html) in the *AWS OpsWorks User Guide*\.
For other AWS services, see the specific service [documentation](https://docs.aws.amazon.com/)\.
To connect to your own server, you could search the internet using a phrase such as "connect to a server by using the SSH command" \(from macOS or Linux\) or "connect to a server by using PuTTY" \(from Windows\)\.

1. Sign in to the AWS Cloud9 console, at [https://console\.aws\.amazon\.com/cloud9/](https://console.aws.amazon.com/cloud9/)\.

1. After you sign in to the AWS Cloud9 console, in the top navigation bar, choose an AWS Region to create the environment in\. For a list of available AWS Regions, see [AWS Cloud9](https://docs.aws.amazon.com/general/latest/gr/rande.html#cloud9_region) in the *AWS General Reference*\.  
![\[AWS Region selector in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-region.png)

1. If a welcome page is displayed, for **New AWS Cloud9 environment**, choose **Create environment**\. Otherwise, choose **Create environment**\.  
![\[Choosing the Next step button if the welcome page is displayed\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-welcome-new-env.png)

   Or:  
![\[Choosing the Create environment button if the welcome page isn't displayed\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-new-env.png)

1. On the **Name environment** page, for **Name**, type a name for your environment\.

1. To add a description to your environment, type it in **Description**\.

1. Choose **Next step**\.

1. For **Environment type**, choose **Connect and run in remote server \(SSH\)**\.

1. For **User**, type the login name you used to connect to the instance or server earlier in this procedure\. For example, for an AWS cloud compute instance, it might be `ec2-user`, `ubuntu`, or `root`\.
**Note**  
For best results, we recommend that the login name is associated with administrative permissions or an administrator user on the instance or server\. Specifically, this login name should own the Node\.js installation on the instance or server\. To check this, from the terminal of your instance or server, run the command ** `ls -l $(which node)` ** \(or ** `ls -l $(nvm which node)` ** if you're using nvm\)\. This command displays the owner name of the Node\.js installation, along with the installation's permissions, group name, and location\.

1. For **Host**, type the public IP address \(preferred\) or the hostname of the instance or server\.

1. For **Port**, type the port that you want AWS Cloud9 to use to try to connect to the instance or server, or leave the default port\.

1. To specify the path to the directory on the instance or server that you want AWS Cloud9 to start from after login\. You identified this earlier in the prerequisites to this procedure\. Expand **Advanced settings**, and then type the path in **Environment path**\. If you leave this blank, AWS Cloud9 uses the directory that your instance or server typically starts with after login\. This is usually a home or default directory\.

1. To specify the path to the Node\.js binary on the instance or server, expand **Advanced settings**, and then type the path in **Node\.js binary path**\. To get the path, you can run the command ** `which node` ** \(or ** `nvm which node` ** if you're using nvm\) on your instance or server\. For example, the path might be `/usr/bin/node`\. If you leave this blank, AWS Cloud9 attempts to guess where the Node\.js binary is when it tries to connect\.

1. To specify a jump host that the instance or server uses, expand **Advanced settings**, and then type information about the jump host in **SSH jump host**, using the format `USER_NAME@HOSTNAME:PORT_NUMBER` \(for example, `ec2-user@:ip-192-0-2-0:22`\)

   The jump host must meet the following requirements\.
   + It must be reachable over the public internet using SSH\.
   + It must allow inbound access by any IP address over the specified port\.
   + The public SSH key value that was copied into the `~/.ssh/authorized_keys` file on the existing instance or server must also be copied into the `~/.ssh/authorized_keys` file on the jump host\.
   + Netcat must be installed\.

1. Choose **Copy key to clipboard**\. \(This is between **View public SSH key** and **Advanced settings**\.\) Paste the public SSH key value that was copied, into the `~/.ssh/authorized_keys` file on the existing instance or server that you connected to earlier in this procedure\. \(`~` represents the home directory for the login name that you specified for **User** earlier in this procedure\.\)
**Note**  
To see the public SSH key value that was copied, expand **View public SSH key**\.

1. Choose **Next step**\.

1. On the **Review** page, choose **Create environment**\. Wait while AWS Cloud9 creates your environment\. This can take several minutes\.

If AWS Cloud9 doesn't display the IDE after at least five minutes, there might be a problem with your web browser, your AWS access permissions, the instance, or the associated network\. For possible fixes, see [Cannot open an environment](troubleshooting.md#troubleshooting-env-loading) in *Troubleshooting*\.

**Note**  
If your environment is using a proxy to access the internet, you must provide proxy details to AWS Cloud9 so it can install dependencies\. For more information, see [Notice: Failed to install dependencies for collaboration support](troubleshooting.md#proxy-failed-dependencies)\.