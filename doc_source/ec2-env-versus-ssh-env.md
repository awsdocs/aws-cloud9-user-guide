# EC2 Environments compared with SSH Environments in AWS Cloud9<a name="ec2-env-versus-ssh-env"></a>

As discussed in the [introduction for environments and computing resources](welcome.md#env-intro) and [working with environments](environments.md), your AWS Cloud9 environments can be set up as either EC2 environments or SSH environments\.

The following table highlights both the similarities and differences between using EC2 environments and SSH environments in AWS Cloud9\.


****  

|  **EC2 environments**  |  **SSH environments**  | 
| --- | --- | 
|  AWS Cloud9 creates an associated Amazon EC2 instance and manages that the lifecycle of the instance \(including the start, stop, and terminate operations\)\.  |  You use an existing cloud compute instance or your own server\. You're responsible for managing its lifecycle\.   | 
|  The instance runs on Amazon Linux or Ubuntu Server\.  |  You can use any cloud compute instance that runs Linux, or you can use your own server running Linux\.  | 
|  AWS Cloud9 automatically sets up the instance to start working with AWS Cloud9\.  |  You must manually configure the instance or your own server to work with AWS Cloud9\.  | 
|  AWS Cloud9 automatically sets up the AWS Command Line Interface \(AWS CLI\) on the instance\.  |  If you want to use the AWS CLI on the instance or your own server, you're responsible for setting it up yourself\.  | 
|  The instance has access to hundreds of useful packages, with some common packages already installed and configured, such as Git, Docker, Node\.js, and Python\.  |  You might need to download, install, and configure additional packages to complete common tasks\.  | 
|  You maintain the instance, for example by periodically applying system updates\.  |  You maintain the instance or your own server\.  | 
|  When you delete the environment, AWS Cloud9 automatically terminates the associated instance\.  |  When you delete the environment, the instance or your own server remains\.  | 