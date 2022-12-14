# Working with Amazon ECR in AWS Cloud9 IDE<a name="ecr"></a>

Amazon Elastic Container Registry \(Amazon ECR\) is an AWS managed container\-registry service that's secure and scalable\. Several Amazon ECR service functions are accessible from the AWS Toolkit Explorer:
+ Creating a repository\.
+ Creating an AWS App Runner service for your repository or tagged image\.
+ Accessing image tag and repository URIs or ARNs\.
+ Deleting image tags and repositories\.

You can also access the full\-range of Amazon ECR functions through the AWS Cloud9 console by installing the AWS CLI and other platforms\.

For more information about Amazon ECR, see [What is Amazon ECR?](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) in the Amazon Elastic Container Registry User Guide\.

## Prerequisites<a name="prereqs-awstoolkit-vscode-ecr"></a>

The following are pre\-installed in the AWS Cloud9 IDE for AWS Cloud9 Amazon EC2 environments\. They're required to access the Amazon ECR service from the AWS Cloud9 IDE\. 

### IAM credentials<a name="create-an-iam-user"></a>

The IAM role that you created and used for authentication in the AWS console\. For more information about IAM, see the [AWS Identity and Access Management User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)\.

### Docker configuration<a name="create-an-iam-user"></a>

Docker is pre\-installed in the AWS Cloud9 IDE for AWS Cloud9 Amazon EC2 environments\. For more information about Docker, see [Install Docker Engine](https://docs.docker.com/engine/install/)\.

### AWS CLI version 2 configuration<a name="create-an-iam-user"></a>

AWS CLI version 2 is pre\-installed in the AWS Cloud9 IDE for AWS Cloud9 Amazon EC2 environments\. For more information about AWS CLI version 2, see [Installing, updating, and uninstalling the AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)\.

**Topics**
+ [Prerequisites](#prereqs-awstoolkit-vscode-ecr)
+ [Using Amazon ECR with AWS Cloud9 IDE](ecr-working.md)