# Working with AWS CodePipeline in the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="codepipeline-repos"></a>

You can use the AWS Cloud9 IDE to work with source code in repositories that are compatible with AWS CodePipeline\.

AWS CodePipeline is a continuous delivery service you can use to model, visualize, and automate the steps required to release your software and ongoing changes you make to it\. You can use AWS CodePipeline to quickly model and configure the different stages of a software release process\. For more information, see the [AWS CodePipeline User Guide](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)\.

**Note**  
Completing these procedures might result in charges to your AWS account\. These include possible charges for services such as Amazon EC2, AWS CodePipeline, Amazon S3, and AWS services supported by AWS CodePipeline\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/), [AWS CodePipeline Pricing](https://aws.amazon.com/codepipeline/pricing/), [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/), and [Cloud Services Pricing](https://aws.amazon.com/pricing/services/)\.  
AWS CodeStar provides additional features along with pipelines, such as project templates, dashboards, and teams\. To use AWS CodeStar instead of AWS CodePipeline, skip the rest of this topic, and see [Working with AWS CodeStar Projects](codestar-projects.md) instead\.
+  [Step 1: Create or Identify Your Source Code Repository](#codepipeline-repos-create-source-code) 
+  [Step 2: Create an AWS Cloud9 Development Environment, Connect It to the Code Repository, and Upload Your Code](#codepipeline-repos-connect-to-repo) 
+  [Step 3: Prepare to Work with AWS CodePipeline](#codepipeline-repos-setup) 
+  [Step 4: Create a Pipeline in AWS CodePipeline](#codepipeline-repos-create-pipeline) 

## Step 1: Create or Identify Your Source Code Repository<a name="codepipeline-repos-create-source-code"></a>

In this step, you create or identify a source code repository that is compatible with AWS CodePipeline\.

Later in this topic, you upload your software's source code to that repository\. AWS CodePipeline will build, test, and deploy the uploaded source code in that repository by using related pipelines that you also create\.

Your source code repository must be one of the following repository types that AWS CodePipeline supports:
+  **AWS CodeCommit**\. If you already have a repository in AWS CodeCommit that you want to use, skip ahead to [Step 2: Create an AWS Cloud9 Development Environment, Connect It to the Code Repository, and Upload Your Code](#codepipeline-repos-connect-to-repo)\. Otherwise, to use AWS CodeCommit, follow these instructions in the *AWS CodeCommit Sample* in this order, and then return to this topic:
  +  [Step 1: Set Up Your IAM Group with Required Access Permissions](sample-codecommit.md#sample-codecommit-permissions) 
  +  [Step 2: Create a Repository in AWS CodeCommit](sample-codecommit.md#sample-codecommit-create-repo) 
+  **Amazon S3**\. If you already have a bucket in Amazon S3 that you want to use, skip ahead to [Step 2: Create an AWS Cloud9 Development Environment, Connect It to the Code Repository, and Upload Your Code](#codepipeline-repos-connect-to-repo)\. Otherwise, to use Amazon S3, follow these instructions in the *Amazon Simple Storage Service Getting Started Guide* in this order, and then return to this topic:
  +  [Sign Up for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/gsg/SigningUpforS3.html) 
  +  [Create a Bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) 
+  **GitHub**\. If you already have a repository in GitHub that you want to use, skip ahead to [Step 2: Create an AWS Cloud9 Development Environment, Connect It to the Code Repository, and Upload Your Code](#codepipeline-repos-connect-to-repo)\. Otherwise, to use GitHub, follow these instructions in the *GitHub Sample* in this order, and then return to this topic:
  +  [Step 1: Create a GitHub Account](sample-github.md#sample-github-create-account) 
  +  [Step 2: Create a GitHub Repository](sample-github.md#sample-github-create-repo) 

## Step 2: Create an AWS Cloud9 Development Environment, Connect It to the Code Repository, and Upload Your Code<a name="codepipeline-repos-connect-to-repo"></a>

In this step, you create an AWS Cloud9 development environment in the AWS Cloud9 console\. You then connect the environment to the repository that AWS CodePipeline will use\. Finally, you use the AWS Cloud9 IDE for the environment to upload your source code to the repository\.

To create the environment, follow the instructions in [Creating an Environment](create-environment.md), and then return to this topic\. \(If you already have an environment, you can use it\. You don't need to create a new one\.\)

To connect the environment to the repository, and then upload your source code to the repository if it isn't already there, use one of the following sets of instructions\. The set you choose depends on the type of repository that stores the source code\.


****  

|  **Repository type**  |  **Instructions**  | 
| --- | --- | 
|  AWS CodeCommit  |  Follow these instructions in the *AWS CodeCommit Sample*: [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/codepipeline-repos.html)  | 
|  Amazon S3  |  [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/codepipeline-repos.html)  | 
|  GitHub  |  Follow these instructions in the *GitHub Sample*: [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/codepipeline-repos.html)  | 

After you connect the environment to the repository, whenever you push source code changes from the AWS Cloud9 IDE to the repository, AWS CodePipeline automatically sends those changes through related pipelines to be built, tested, and deployed\. You create a related pipeline later in this topic\.

## Step 3: Prepare to Work with AWS CodePipeline<a name="codepipeline-repos-setup"></a>

In this step, you attach a specific AWS managed policy to the IAM group you created or identified in [Team Setup](setup.md)\. This enables the group's users to begin creating and working with pipelines in AWS CodePipeline\.

If you have used AWS CodePipeline before, skip ahead to [Step 4: Create a Pipeline in AWS CodePipeline](#codepipeline-repos-create-pipeline)\.

For this step, follow these instructions in [Step 3: Use an IAM Managed Policy to Assign AWS CodePipeline Permissions to the IAM User](https://docs.aws.amazon.com/codepipeline/latest/userguide/getting-started-codepipeline.html#assign-permissions) in the *AWS CodePipeline User Guide*, and then return to this topic\.

## Step 4: Create a Pipeline in AWS CodePipeline<a name="codepipeline-repos-create-pipeline"></a>

In this step, you create a pipeline in AWS CodePipeline that uses the repository you created or identified earlier in this topic\.

For this step, follow the instructions in [Create a Pipeline in AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create.html) in the *AWS CodePipeline User Guide*\.

After you create the pipeline, AWS CodePipeline sends the current version of the source code in the repository through the pipeline to be built, tested, and deployed\. Then, whenever you push source code changes from the AWS Cloud9 IDE to the repository, AWS CodePipeline automatically sends those changes through the pipeline to be built, tested, and deployed\.

To view the pipeline, follow the instructions in [View Pipeline Details and History in AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-view.html) in the *AWS CodePipeline User Guide*\.