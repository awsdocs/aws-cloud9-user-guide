# Amazon Machine Image \(AMI\) contents for an AWS Cloud9 EC2 Development Environment<a name="ami-contents"></a>

Use the following information to get details about Amazon Machine Images \(AMIs\) that AWS Cloud9 uses for an EC2 environment\.

**Topics**
+ [Amazon Linux 2/Amazon Linux](#ami-contents-amazon-linux)
+ [Ubuntu Server](#ami-contents-ubuntu-server)

## Amazon Linux 2/Amazon Linux<a name="ami-contents-amazon-linux"></a>

**Important**  
We recommend that you choose the **Amazon Linux 2** option when [creating an Amazon EC2 environment using the console](create-environment-main.md#create-environment-console)\. As well as providing a secure, stable, and high\-performance execution environment for developing and running cloud and enterprise applications, Amazon Linux 2 AMI includes long\-term support through 2023\.  
 The older Amazon Linux AMI will end\-of\-life its standard support on December 31,2020 and enter a maintenance support phase\. For more information, see the [Amazon Linux 2 page](https://aws.amazon.com/amazon-linux-2/)\.  
 Unless otherwise specified, references to Amazon Linux in the text below refer to both Amazon Linux and Amazon Linux 2 instances\.

To display the version of an Amazon Linux instance, run the following command from the AWS Cloud9 IDE for the connected environment or from an SSH utility such as the ssh command or PuTTY\.

```
cat /etc/system-release
```

To display a list of packages that are installed on an Amazon Linux instance, run one or more of the following commands\.

To display all installed packages as a single list:

```
sudo yum list installed
```

To display a list of installed packages with package names containing the specified text:

```
sudo yum list installed | grep YOUR_SEARCH_TERM
```

In the preceding command, replace `YOUR_SEARCH_TERM` with some portion of the package name\. For example, to display a list of all installed packages with names containing `sql`:

```
sudo yum list installed | grep sql
```

To display a list of all installed packages, displayed one page at a time:

```
sudo yum list installed | less
```

To scroll through the displayed pages:
+ To move down a line, press **j**\.
+ To move up a line, press **k**\.
+ To move down a page, press **Ctrl\-F**\.
+ To move up a page, press **Ctrl\-B**\.
+ To quit, press **q**\.

**Note**  
With Amazon Linux 2, you can use the Extras Library to install application and software updates on your instances\. These software updates are known as topics\. For more information, see [Extras library \(Amazon Linux 2\)](Amazon EC2 User Guide for Linux Instancesamazon-linux-ami-basics.html#extras-library) in the *Amazon EC2 User Guide for Linux Instances*\.

For additional options, run the man yum command\. See also the following resources:
+ Amazon Linux 2: [Release notes]()\. 
+ Amazon Linux: [Amazon Linux AMI 2018\.03 Packages](https://aws.amazon.com/amazon-linux-ami/2018-03-packages/)\.

## Ubuntu Server<a name="ami-contents-ubuntu-server"></a>

To display the version of an Ubuntu Server instance, run the following command from the AWS Cloud9 IDE for the connected environment or from an SSH utility such as the ssh command or PuTTY\.

```
lsb_release -a
```

The version will display next to the **Description** field\.

To display a list of packages that are installed on an Ubuntu Server, run one or more of the following commands\.

To display all installed packages as a single list:

```
sudo apt list --installed
```

To display a list of installed packages with package names containing the specified text:

```
sudo apt list --installed | grep YOUR_SEARCH_TERM
```

In the preceding command, replace `YOUR_SEARCH_TERM` with some portion of the package name\. For example, to display a list of all installed packages with names containing `sql`:

```
sudo apt list --installed grep sql
```

To display a list of all installed packages, one page at a time:

```
sudo apt list --installed | less
```

To scroll through the displayed pages:
+ To move down a line, press **j**\.
+ To move up a line, press **k**\.
+ To move down a page, press **Ctrl\-F**\.
+ To move up a page, press **Ctrl\-B**\.
+ To quit, press **q**\.

For additional options, run the man apt command\. See also [Ubuntu Packages Search](https://packages.ubuntu.com/) on the Ubuntu website\.