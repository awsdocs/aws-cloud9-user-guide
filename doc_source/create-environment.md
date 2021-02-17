# Creating an environment in AWS Cloud9<a name="create-environment"></a>

To create an AWS Cloud9 development environment, follow one the provided procedures based on how you plan to use AWS Cloud9 use AWS Cloud9\.


****  

|  | 
| --- |
|  If you're not sure what to choose, we recommend [Creating an EC2 Environment](create-environment-main.md)\. Creating an EC2 environment is the easiest option\. AWS Cloud9 automatically creates and sets up a new Amazon EC2 instance in your AWS account\. AWS Cloud9 then automatically connects that new instance to the environment for you\. To understand the key similarities and differences between the development environments, see [EC2 Environments compared with SSH Environments in AWS Cloud9](ec2-env-versus-ssh-env.md)\.  | 


****  

|  **Source code provider**  |  **Development environment host provider**  |  **Relevant procedure**  | 
| --- | --- | --- | 
|  You  |  AWS Cloud9  |  [Create an EC2 environment](create-environment-main.md)  | 
|  You  |  You  |  [Create an SSH environment](create-environment-ssh.md)  | 
|   [Amazon Lightsail](https://aws.amazon.com/lightsail) or you  |  You \(using Lightsail\)  |   [Working with Amazon Lightsail instances in the AWS Cloud9 Integrated Development Environment \(IDE\)](lightsail-instances.md)   | 
|   [AWS CodeStar](https://aws.amazon.com/codestar) or you  |  AWS Cloud9 \(using AWS CodeStar\)  |   [Working with AWS CodeStar Projects in the AWS Cloud9 Integrated Development Environment \(IDE\)](codestar-projects.md)   | 
|  You \(using [AWS CodePipeline](https://aws.amazon.com/codepipeline)\)  |  AWS Cloud9 or you  |  Create an [EC2](create-environment-main.md) or [SSH](create-environment-ssh.md) environment, and [Working with AWS CodePipeline in the AWS Cloud9 Integrated Development Environment \(IDE\)](codepipeline-repos.md)   | 
|  You \(using [AWS CodeCommit](https://aws.amazon.com/codecommit)\)  |  AWS Cloud9 or you  |   [AWS CodeCommit sample for AWS Cloud9](sample-codecommit.md)   | 
|  You \(using [GitHub](https://github.com/)\)  |  AWS Cloud9 or you  |  Create an [EC2](create-environment-main.md) or [SSH](create-environment-ssh.md) environment, and use the [Git panel interface](source-control-gitpanel.md)   | 

**Topics**
+ [Creating an EC2 Environment](create-environment-main.md)
+ [Creating an SSH Environment](create-environment-ssh.md)