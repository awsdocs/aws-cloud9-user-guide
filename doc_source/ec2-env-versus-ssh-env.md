# EC2 environments compared with SSH environments in AWS Cloud9<a name="ec2-env-versus-ssh-env"></a>

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
|  [AWS managed temporary credentials](security-iam.md#auth-and-access-control-temporary-managed-credentials-supported) are available in EC2 environments, allowing you to easily turn on or off all AWS actions for all AWS resources in the caller's AWS account \(with some restrictions\)\. You don't need to configure instance profiles for your environment's Amazon EC2 instance or store permanent AWS access credentials of an AWS entity \(for example, an IAM user\)\.  |  [AWS managed temporary credentials](security-iam.md#auth-and-access-control-temporary-managed-credentials-supported) aren't available in SSH environments\. You must use [AWS Identity and Access Management](security-iam.md) to manage the permissions that allow you to work with both AWS Cloud9 and other AWS services and resources\.  | 
|  [AWS Toolkit](toolkit-welcome.md), [Git panel](source-control-gitpanel.md), and [enhanced Java support](enhanced-java.md) are available for use\.  |  AWS Toolkit, Git panel, and enhanced Java support aren't available\.  | 