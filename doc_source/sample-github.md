# GitHub Sample for AWS Cloud9<a name="sample-github"></a>

This sample enables you to set up an AWS Cloud9 development environment to interact with a remote code repository in GitHub\. For more information about GitHub, see the [GitHub](https://github.com/) and [GitHub Help](https://help.github.com/) websites\.

Creating this sample might result in charges to your AWS account\. These include possible charges for services such as Amazon EC2\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/)\.

**Topics**
+ [Prerequisites](#sample-github-prereqs)
+ [Step 1: Create a GitHub Account](#sample-github-create-account)
+ [Step 2: Create a GitHub Repository](#sample-github-create-repo)
+ [Step 3: Install Git in Your Environment](#sample-github-install-git)
+ [Step 4: Clone the Remote Repository into Your Environment](#sample-github-clone-repo)
+ [Step 5: Add Files to the Repository](#sample-github-add-files)
+ [Step 6: Keep Working with the IDE and GitHub](#sample-github-explore)
+ [Step 7: Clean Up](#sample-github-clean-up)

## Prerequisites<a name="sample-github-prereqs"></a>

Before you use this sample, be sure to meet the following requirements\.
+  **You must have an existing AWS Cloud9 EC2 development environment\.** This sample assumes you already have an EC2 environment that is connected to an Amazon EC2 instance running Amazon Linux or Ubuntu Server\. If you have a different type of environment or operating system, you might need to adapt this sample's instructions to set up related tools\. See [Creating an Environment in AWS Cloud9](create-environment.md) for details\.
+  **You have the AWS Cloud9 IDE for the existing environment already open\.** When you open an environment, AWS Cloud9 opens the IDE for that environment in your web browser\. See [Opening an Environment in AWS Cloud9](open-environment.md) for details\.

Start with the following step, depending on what you already have\.


****  

|  **Do you have a GitHub account?**  |  **Do you have a GitHub repository?**  |  **Do you have Git installed?**  |  **Start with this step**  | 
| --- | --- | --- | --- | 
|  No  |  \-\-  |  \-\-  |   [Step 1: Create a GitHub Account](#sample-github-create-account)   | 
|  Yes  |  No  |  \-\-  |   [Step 2: Create a GitHub Repository](#sample-github-create-repo)   | 
|  Yes  |  Yes  |  No \(or Not Sure\)  |   [Step 3: Install Git in Your Environment](#sample-github-install-git)   | 
|  Yes  |  Yes  |  Yes  |   [Step 4: Clone the Remote Repository into Your Environment](#sample-github-clone-repo)   | 

## Step 1: Create a GitHub Account<a name="sample-github-create-account"></a>

If you already have a GitHub account, skip ahead to [Step 2: Create a GitHub Repository](#sample-github-create-repo)\.

To create a GitHub account, see [Join GitHub](https://github.com/join) on the GitHub website\.

## Step 2: Create a GitHub Repository<a name="sample-github-create-repo"></a>

If you already have a GitHub repository, skip ahead to [Step 3: Install Git in Your Environment](#sample-github-install-git)\.

To create the repository, see [Create A Repo](https://help.github.com/articles/create-a-repo/) on the GitHub Help website\.

## Step 3: Install Git in Your Environment<a name="sample-github-install-git"></a>

In this step, you use the AWS Cloud9 IDE to install Git in your environment so that you can clone your remote repository into the environment later\.

If you already have Git installed in your environment, skip ahead to [Step 4: Clone the Remote Repository into Your Environment](#sample-github-clone-repo)\. To check whether you already have Git installed, run the ** `git --version` ** command as described in this step\.

1. With your environment open, in the AWS Cloud9 IDE, start a new terminal session, if one isn't already started\. \(To start a new terminal session, on the menu bar, choose **Window**, **New Terminal**\.\)

1. Check whether Git is already installed\. In the terminal, run the ** `git --version` ** command\. If Git is installed, the version number is displayed, for example, `git version N.N.N `\. The installed version must be 1\.7\.9 or later\. If it is, skip ahead to step 4 in this procedure to set your Git name and email address\.

1. To install Git, see [Git Downloads](https://git-scm.com/downloads) on the Git website\. For example, for an EC2 environment running Amazon Linux, run these three commands in the terminal, one at a time, to install Git\.

   ```
   sudo yum -y update      # Install the latest system updates.
   sudo yum -y install git # Install Git.
   git --version           # Confirm Git was installed.
   ```

   For an EC2 environment running Ubuntu Server, run these three commands in the terminal instead, one at a time, to install Git\.

   ```
   sudo apt update      # Install the latest system updates.
   sudo apt install -y git # Install Git.
   git --version               # Confirm Git was installed.
   ```

1. Set your Git name and email address\. In the terminal, run these two commands, one at a time, substituting your Git name and email address for ` USER_NAME ` and ` EMAIL_ADDRESS `\.

   ```
   git config --global user.name "USER_NAME"
   git config --global user.email EMAIL_ADDRESS
   ```

## Step 4: Clone the Remote Repository into Your Environment<a name="sample-github-clone-repo"></a>

In this step, you use the AWS Cloud9 IDE to clone the remote repository in GitHub into your environment\.

To clone the repository, see [Cloning a Repository](https://help.github.com/articles/cloning-a-repository/#platform-linux) on the GitHub website\.

**Note**  
The rest of this sample assumes the current working directory that you clone the repository into is the environment root directory\. If you clone it somewhere else, substitute that location wherever you see `/YOUR_CLONED_REPO_NAME `\.

## Step 5: Add Files to the Repository<a name="sample-github-add-files"></a>

In this step, you create three simple files in the cloned repository in your environment\. Then you add the files to the Git staging area in your cloned repository, commit the staged files, and push the commit to your remote repository in GitHub\.

If the cloned repository already has files in it, skip ahead to [Step 6: Keep Working with the IDE and GitHub](#sample-github-explore)\.

1. Create a new file\. On the menu bar, choose **File**, **New File**\.

1. Type the following content into the file, and then choose **File**, **Save** to save the file as `bird.txt` in the `/YOUR_CLONED_REPO_NAME ` directory in your environment\.

   ```
   bird.txt
   --------
   Birds are a group of endothermic vertebrates, characterized by feathers,
   toothless beaked jaws, the laying of hard-shelled eggs, a high metabolic
   rate, a four-chambered heart, and a lightweight but strong skeleton.
   ```
**Note**  
To confirm you are saving this file in the correct directory, in the **Save As** dialog box, choose the ` YOUR_CLONED_REPO_NAME ` folder, and be sure **Folder** displays `/YOUR_CLONED_REPO_NAME `\.

1. Create two more files, named `insect.txt` and `reptile.txt`, with the following content, saving them also in the same `/YOUR_CLONED_REPO_NAME ` directory\.

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

1. In the terminal, run the ** `cd` ** command to switch to the `/YOUR_CLONED_REPO_NAME ` directory\.

   ```
   cd YOUR_CLONED_REPO_NAME
   ```

1. Confirm the files were successfully saved in the `/YOUR_CLONED_REPO_NAME ` directory by running the ** `git status` ** command\. All three files are listed as untracked files\.

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
     (use "git reset HEAD <file>..." to unstage)
   
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
   git push
   ```
**Note**  
You are prompted for your GitHub user name and password\. As you continue to work with GitHub, you might be prompted again\. To keep from being prompted each time you try to interact with the remote repository in the future, consider installing and configuring a Git credentials manager\. For example, you can run this command in the terminal to be prompted no sooner than every 15 minutes: `git config credential.helper 'cache --timeout 900'`\. Or you can run this command to never be prompted again, although Git stores your credentials in clear text in a plain file in your home directory: `git config credential.helper 'store --file ~/.git-credentials'`\. For more information, see [Git Tools \- Credential Storage](https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage) on the Git website\.  
If you use GitHub two\-factor authentication, you must enter a personal access token whenever you are prompted for a password\. If you enter a password instead of a personal access token, an "invalid user name or password" message is displayed, and the operation fails\. For more information, see [Creating a personal access token for the command line](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) on the GitHub Help website\.  
You will not see your password or personal access token whenever you enter it in the terminal\. This is by design\.

1. To confirm whether the files were successfully pushed from your local copy of the repository to the remote repository, open your repository in the GitHub console, and look for the three files you just pushed\.

## Step 6: Keep Working with the IDE and GitHub<a name="sample-github-explore"></a>

Use the AWS Cloud9 IDE and GitHub to keep working with your code\. Here are some things to try\.
+ Use the **Environment** window and editor tabs in the IDE to view, change, and save code\. For more information, see [Step 2\.3: Environment Window](tutorial.md#tutorial-environment) and [Step 2\.4: Editor, Tabs, and Panes](tutorial.md#tutorial-editor) in the *IDE Tutorial for AWS Cloud9*\.
+ Use the IDE to run, debug, and build your code\. For more information, see [Working with Builders, Runners, and Debuggers in the AWS Cloud9 Integrated Development Environment \(IDE\)](build-run-debug.md)\.
+ Use Git in the terminal session in the IDE to continue pushing more code changes to the GitHub repository, as well as periodically pull code changes from others from the repository\. For more information, see [Pushing to a Remote](https://help.github.com/articles/pushing-to-a-remote/) and [Fetching a remote](https://help.github.com/articles/fetching-a-remote/) on the GitHub Help website\.
+ Use additional Git commands as you need them\. For a list of these commands, see [Git cheatsheet](https://help.github.com/articles/git-cheatsheet/) on the GitHub Help website\.
+ If you're new to Git and you don't want to mess up your GitHub repository, experiment with a sample Git repository on the [Try Git](https://try.github.io/) website\.
+ Invite others to work on your code with you in the same environment, in real time and with text chat\. For more information, see [Working with Shared Environments in AWS Cloud9](share-environment.md)\.

## Step 7: Clean Up<a name="sample-github-clean-up"></a>

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the environment\. For instructions, see [Deleting an Environment in AWS Cloud9](delete-environment.md)\.

To delete the GitHub repository, see [Deleting a Repository](https://help.github.com/articles/deleting-a-repository/) on the GitHub Help website\.