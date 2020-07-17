# AWS CodeCommit Sample for AWS Cloud9<a name="sample-codecommit"></a>

This sample enables you to set up an AWS Cloud9 development environment to interact with a remote code repository in CodeCommit\. CodeCommit is a source code control service that enables you to privately store and manage Git repositories in the AWS Cloud\. For more information about CodeCommit, see the [AWS CodeCommit User Guide](https://docs.aws.amazon.com/codecommit/latest/userguide/)\.

Creating this sample might result in charges to your AWS account\. These include possible charges for services such as Amazon EC2 and CodeCommit\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/) and [AWS CodeCommit Pricing](https://aws.amazon.com/codecommit/pricing/)\.
+  [Prerequisites](#sample-codecommit-prereqs) 
+  [Step 1: Set Up Your IAM Group with Required Access Permissions](#sample-codecommit-permissions) 
+  [Step 2: Create a Repository in AWS CodeCommit](#sample-codecommit-create-repo) 
+  [Step 3: Connect Your Environment to the Remote Repository](#sample-codecommit-connect-repo) 
+  [Step 4: Clone the Remote Repository into Your Environment](#sample-codecommit-clone-repo) 
+  [Step 5: Add Files to the Repository](#sample-codecommit-add-files) 
+  [Step 6: Clean Up](#sample-codecommit-clean-up) 

## Prerequisites<a name="sample-codecommit-prereqs"></a>

Before you use this sample, be sure to meet the following requirements\.
+  **You must have an existing AWS Cloud9 EC2 development environment\.** This sample assumes you already have an EC2 environment that is connected to an Amazon EC2 instance running Amazon Linux or Ubuntu Server\. If you have a different type of environment or operating system, you might need to adapt this sample's instructions to set up related tools\. See [Creating an Environment in AWS Cloud9](create-environment.md) for details\.
+  **You have the AWS Cloud9 IDE for the existing environment already open\.** When you open an environment, AWS Cloud9 opens the IDE for that environment in your web browser\. See [Opening an environment in AWS Cloud9](open-environment.md) for details\.

## Step 1: Set Up Your IAM Group with Required Access Permissions<a name="sample-codecommit-permissions"></a>

If your AWS credentials are associated with an IAM administrator user in your AWS account, and you want to use that user to work with CodeCommit, skip ahead to [Step 2: Create a Repository in AWS CodeCommit](#sample-codecommit-create-repo)\.

You can complete this step using the [AWS Management Console](#sample-codecommit-permissions-console) or the [AWS Command Line Interface \(AWS CLI\)](#sample-codecommit-permissions-cli)\.

### Set Up Your IAM Group with Required Access Permissions Using the Console<a name="sample-codecommit-permissions-console"></a>

1. Sign in to the AWS Management Console, if you are not already signed in\.

   For this step, we recommend you sign in using credentials for an IAM administrator user in your AWS account\. If you cannot do this, check with your AWS account administrator\.

1. Open the IAM console\. To do this, in the console's navigation bar, choose **Services**\. Then choose **IAM**\.

1. Choose **Groups**\.

1. Choose the group's name\.

1. On the **Permissions** tab, for **Managed Policies**, choose **Attach Policy**\.

1. In the list of policy names, select one of the following boxes:
   + Select **AWSCodeCommitPowerUser** for access to all of the functionality of CodeCommit and repository\-related resources, except it does not allow deletion of CodeCommit repositories or create or delete repository\-related resources in other AWS services, such as Amazon CloudWatch Events\.
   + Select **AWSCodeCommitFullAccess** for full control over CodeCommit repositories and related resources in the AWS account, including the ability to delete repositories\.

   \(If you don't see either of these policy names in the list, type the policy name in the **Filter** box to display it\.\)

1. Choose **Attach Policy**\.

To see the list of access permissions that these AWS managed policies give to a group, see [AWS Managed \(Predefined\) Policies for AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#managed-policies) in the *AWS CodeCommit User Guide*\.

Skip ahead to [Step 2: Create a Repository in AWS CodeCommit](#sample-codecommit-create-repo)\.

### Set Up Your IAM Group with Required Access Permissions Using the AWS CLI<a name="sample-codecommit-permissions-cli"></a>

Run the IAM `attach-group-policy` command, specifying the group's name and the Amazon Resource Name \(ARN\) of the AWS managed policy that describes the required access permissions, for example:

```
aws iam attach-group-policy --group-name MyGroup --policy-arn POLICY_ARN
```

In the preceding command, replace `MyGroup` with the name of the group\. Replace `POLICY_ARN` with the ARN of the AWS managed policy, as follows:
+  `arn:aws:iam::aws:policy/AWSCodeCommitPowerUser` for access to all of the functionality of CodeCommit and repository\-related resources, except it does not allow deletion of CodeCommit repositories or create or delete repository\-related resources in other AWS services, such as Amazon CloudWatch Events\.
+  `arn:aws:iam::aws:policy/AWSCodeCommitFullAccess` for full control over CodeCommit repositories and related resources in the AWS account, including the ability to delete repositories\.

To see the list of access permissions that these AWS managed policies give to a group, see [AWS Managed \(Predefined\) Policies for AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#managed-policies) in the *AWS CodeCommit User Guide*\.

## Step 2: Create a Repository in CodeCommit<a name="sample-codecommit-create-repo"></a>

In this step, you create a remote code repository in CodeCommit by using the CodeCommit console\.

If you already have a CodeCommit repository, skip ahead to [Step 3: Connect Your Environment to the Remote Repository](#sample-codecommit-connect-repo)\.

You can complete this step using the [AWS Management Console](#sample-codecommit-create-repo-console) or the [AWS Command Line Interface \(AWS CLI\)](#sample-codecommit-create-repo-cli)\.

### Create a Repository in CodeCommit Using the Console<a name="sample-codecommit-create-repo-console"></a>

1. If you are signed in to the AWS Management Console as an IAM administrator user from the previous step, and you do not want to use the IAM administrator user to create the repository, sign out of the AWS Management Console\.

1. Open the CodeCommit console, at [https://console\.aws\.amazon\.com/codecommit](https://console.aws.amazon.com/codecommit)\.

1. In the console's navigation bar, use the region selector to choose the AWS Region you want to create the repository in \(for example, **US East \(Ohio\)**\)\.

1. If a welcome page is displayed, choose **Get started**\. Otherwise, choose **Create repository**\.

1. On the **Create repository** page, for **Repository name**, type a name for your new repository, for example `MyDemoCloud9Repo`\. If you choose a different name, substitute it throughout this sample\.

1. \(Optional\) For **Description**, type something about the repository, for example `This is a demonstration repository for the AWS Cloud9 sample.` 

1. Choose **Create repository**\. A **Connect to your repository** pane is displayed\. Choose **Close**, as you will connect to your repository in a different way later in this topic\.

Skip ahead to [Step 3: Connect Your Environment to the Remote Repository](#sample-codecommit-connect-repo)\.

### Create a Repository in CodeCommit Using the AWS CLI<a name="sample-codecommit-create-repo-cli"></a>

Run the AWS CodeCommit `create-repository` command, specifying the repository's name, an optional description, and the AWS Region to create the repository in, for example:

```
aws codecommit create-repository --repository-name MyDemoCloud9Repo --repository-description "This is a demonstration repository for the AWS Cloud9 sample." --region us-east-2
```

In the preceding command, replace `us-east-2` with the ID of the AWS Region to create the repository in\. For a list of supported regions, see [AWS CodeCommit](https://docs.aws.amazon.com/general/latest/gr/rande.html#codecommit_region) in the *Amazon Web Services General Reference*\.

If you choose to use a different repository name, substitute it throughout this sample\.

## Step 3: Connect Your Environment to the Remote Repository<a name="sample-codecommit-connect-repo"></a>

In this step, you use the AWS Cloud9 IDE to connect to the CodeCommit repository you created or identified in the previous step\.

Complete one of the following sets of procedures, depending on the type of AWS Cloud9 development environment you have\.


****  

|  **Environment type**  |  **Follow these procedures**  | 
| --- | --- | 
|  EC2 environment  |  [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/sample-codecommit.html)  | 
|  SSH environment  |  [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/sample-codecommit.html)  | 

## Step 4: Clone the Remote Repository into Your Environment<a name="sample-codecommit-clone-repo"></a>

In this step, you use the AWS Cloud9 IDE to clone the remote repository in CodeCommit into your environment\.

To clone the repository, run the ** `git clone` ** command, supplying the repository's clone URL, shown here as ` CLONE_URL `\.

```
git clone CLONE_URL
```

For an EC2 environment, you supply an HTTPS clone URL that starts with `https://`\. For an SSH environment, you supply an SSH clone URL that starts with `ssh://`\.

To get the repository's full clone URL, see [Use the AWS CodeCommit Console to View Repository Details](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-view-repository-details.html#how-to-view-repository-details-console) in the *AWS CodeCommit User Guide*\.

If your repository doesn't have any files in it, a warning message is displayed, such as `You appear to have cloned an empty repository.` This is expected behavior, which you will address later\.

## Step 5: Add Files to the Repository<a name="sample-codecommit-add-files"></a>

In this step, you create three simple files in the cloned repository in your AWS Cloud9 environment\. Then you add the files to the Git staging area in your cloned repository, commit the staged files, and push the commit to your remote repository in CodeCommit\.

If the cloned repository already has files in it, you're done and can skip the rest of this sample\.

**To add files to the repository**

1. Create a new file\. On the menu bar, choose **File**, **New File**\.

1. Type the following content into the file, and then choose **File**, **Save** to save the file as `bird.txt` in the `MyDemoCloud9Repo` directory in your AWS Cloud9 environment\.

   ```
   bird.txt
   --------
   Birds are a group of endothermic vertebrates, characterized by feathers,
   toothless beaked jaws, the laying of hard-shelled eggs, a high metabolic
   rate, a four-chambered heart, and a lightweight but strong skeleton.
   ```
**Note**  
To confirm you are saving this file in the correct directory, in the **Save As** dialog box, choose the `MyDemoCloud9Repo` folder, and be sure **Folder** displays `/MyDemoCloud9Repo`\.

1. Create two more files, named `insect.txt` and `reptile.txt`, with the following content, and saving them in the same `MyDemoCloud9Repo` directory\.

   ```
   insect.txt
   ----------
   Insects are a class of invertebrates within the arthropod phylum that
   have a chitinous exoskeleton, a three-part body (head, thorax, and abdomen),
   three pairs of jointed legs, compound eyes, and one pair of antennae.
   ```

   ```
   reptile.txt
   -----------
   Reptiles are tetrapod (four-limbed vertebrate) animals in the class
   Reptilia, comprising today's turtles, crocodilians, snakes,
   amphisbaenians, lizards, tuatara, and their extinct relatives.
   ```

1. In the terminal, run the ** `cd` ** command to switch to the `MyDemoCloud9Repo` directory\.

   ```
   cd MyDemoCloud9Repo
   ```

1. Confirm the files were successfully saved in the `MyDemoCloud9Repo` directory by running the ** `git status` ** command\. All three files will be listed as untracked files\.

   ```
   Untracked files:
     (use "git add <file>..." to include in what will be committed)
   
           bird.txt
           insect.txt
           reptile.txt
   ```

1. Add the files to the Git staging area by running the ** `git add` ** command\.

   ```
   git add --all
   ```

1. Confirm the files were successfully added to the Git staging area by running the ** `git status` ** command again\. All three files are now listed as changes to commit\.

   ```
   Changes to be committed:
     (use "git rm --cached <file>..." to unstage)
   
           new file:   bird.txt
           new file:   insect.txt
           new file:   reptile.txt
   ```

1. Commit the staged files by running the ** `git commit` ** command\.

   ```
   git commit -m "Added information about birds, insects, and reptiles."
   ```

1. Push the commit to your remote repository in CodeCommit by running the ** `git push` ** command\.

   ```
   git push -u origin master
   ```

1. Confirm whether the files were successfully pushed\. Open the CodeCommit console, if it isn't already open, at [https://console\.aws\.amazon\.com/codecommit](https://console.aws.amazon.com/codecommit)\.

1. In the top navigation bar, near the right edge, choose the AWS Region where you created the repository \(for example, **US East \(Ohio\)**\)\.

1. On the **Dashboard** page, choose **MyDemoCloud9Repo**\. The three files are displayed\.

To continue experimenting with your CodeCommit repository, see [Browse the Contents of Your Repository](https://docs.aws.amazon.com/codecommit/latest/userguide/getting-started-cc.html#getting-started-cc-browse) in the *AWS CodeCommit User Guide*\.

If you're new to Git and you don't want to mess up your CodeCommit repository, experiment with a sample Git repository on the [Try Git](https://try.github.io/) website\.

## Step 6: Clean Up<a name="sample-codecommit-clean-up"></a>

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the CodeCommit repository\. For instructions, see [Delete an AWS CodeCommit Repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-delete-repository.html) in the *AWS CodeCommit User Guide*\.

You should also delete the environment\. For instructions, see [Deleting an Environment](delete-environment.md)\.