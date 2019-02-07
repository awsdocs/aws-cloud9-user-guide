# Working with Environments in AWS Cloud9<a name="environments"></a>

A *development environment* is a place in AWS Cloud9 where you store your project's files and where you run the tools to develop your apps\.

AWS Cloud9 provides two types of development environments: *EC2 environments* and *SSH environments*\. Here are the key similarities and differences between them\.


****  

|  **EC2 environments**  |  **SSH environments**  | 
| --- | --- | 
|  AWS Cloud9 creates an associated Amazon EC2 instance and manages that instance's lifecycle \(for example, start, stop, and terminate\)\.  |  You use an existing cloud compute instance or your own server\. You manage that instance's or server's lifecycle\.  | 
|  The instance runs on Amazon Linux\.  |  You can use any cloud compute instance that runs Linux, or your own server running Linux\.  | 
|  AWS Cloud9 automatically sets up the instance to start working with AWS Cloud9\.  |  You must manually configure the instance or your own server to work with AWS Cloud9\.  | 
|  AWS Cloud9 automatically sets up the AWS Command Line Interface \(AWS CLI\) on the instance for you to start using\.  |  If you want to use the AWS CLI on the instance or your own server, you must set it up yourself\.  | 
|  The instance has access to hundreds of useful packages, with some common packages already installed and configured, such as Git, Docker, Node\.js, and Python\.  |  You might need to download, install, and configure additional packages to complete common tasks\.  | 
|  You maintain the instance, for example by periodically applying system updates\.  |  You maintain the instance or your own server\.  | 
|  When you delete the environment, AWS Cloud9 automatically terminates the associated instance\.  |  When you delete the environment, the instance or your own server remains\.  | 

Learn how to work with an environment in AWS Cloud9 by reading one or more of these topics\.

**Topics**
+ [Creating an Environment](create-environment.md)
+ [Opening an Environment](open-environment.md)
+ [Call AWS Services from an Environment](credentials.md)
+ [Changing Environment Settings](change-environment.md)
+ [Working with Shared Environments](share-environment.md)
+ [Moving or Resizing an Environment](move-environment.md)
+ [Deleting an Environment](delete-environment.md)