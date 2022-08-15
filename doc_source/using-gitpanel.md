# Managing source control with Git panel<a name="using-gitpanel"></a>

The Git panel extension for AWS Cloud9 provides convenient user interface access to both core and advanced Git commands\.

This section demonstrates how to access key Git features for managing source control\. The procedures focus on using the **Git panel** menu to run Git commands against your repository and its content\.

![\[Interface options for initializing and cloning a Git repository\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/git-panel-menu.png)

 You can also access any supported Git command by starting to enter the name in the Git panel search box:

![\[Interface options for initializing and cloning a Git repository\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/git-commands-type.png)

And you can view the actual Git commands that are run when you interact with the Git panel interface\. To view command line activity, go to the **Git panel** menu and choose **Show Git Output**\.

![\[Viewing the Git command output\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/git-output.png)

## Initialize or clone a Git repository<a name="init-clone-repo"></a>

A Git repository \("repo"\) contains the complete history of a project from its beginning\. A repository consists of all the snapshots of project content that were captured each time you committed staged files to that repo\.

Git panel supports both ways of obtaining a Git repository:
+ Initialize an existing directory as a Git repository\.
+ Clone an existing repository and copy it to local directory\.

![\[Interface options for initializing and cloning a Git repository\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/init-clone.png)

**Note**  
The interface options for initializing or cloning a repo are available only if you don't already have a Git repository added to workspace folder in your environment\. If you already have a working directory for a repository, the Git panel window displays the status of the working directory and the staging area\. The **Git panel** menu is also available to provide access to Git commands that you can run against the repository\.<a name="initialize-repo-proc"></a>

## To initialize or clone a repository<a name="initialize-repo-proc"></a>

1. If Git panel isn't already available, access it by choosing **Window**, **Source Control**, and then choosing the Git icon\.
**Note**  
You can also open Git panel using the keyboard shortcut **Ctrl\+Shift\+G**\.

1. Choose whether to initialize a new repo or clone an existing one\.

------
#### [ Initialize a repository ]
   + In the Git panel, choose **Initialize Repository**\.
   + Next, pick a workspace folder where your Git repo will be initialized\. You can enter a path to the folder, choose a path, or choose a folder in a dialog box\.
   + If you're using a dialog box, select the destination folder and choose **Initialize Repository**\.

![\[Selecting a workspace folder for a Git repo\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/init-dialog-box.png)

   After you initialize the Git repo in the selected folder, the Git panel displays any files already in that folder as untracked and ready to be added to the Git staging area\.

![\[Selecting a workspace folder for a Git repo\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/untracked-changes.png)

------
#### [ Clone a repository ]
   + In the Git panel window, choose **Clone Repository**\.
   + Next enter a URL for the remote repo you want to clone \(`https://github.com/my-own-repo/my-repo-project-name.git`, for example, to clone a repo hosted on GitHub\) and press **Return**\.
   + In the dialog box that displays, select a workspace folder for the cloned repo and choose **Select Repository Location**\.

**Note**  
If you're accessing a repository hosted on an external site \(GitHub, for example\), you also need to enter a user name and password for the site to complete the process\.

   After you clone the remote repo in the selected folder, you can run the `git pull` command to sync your local repository with the latest changes in the remote repository\. For more information, see [Working with remote repositories](#working-with-remote-repos)\.

------

## Staging and committing files<a name="staging-and-commit"></a>

After you obtained a Git repository, you can then start to populate it with content using a two\-step process:

1. Add untracked or recently modified content to the staging area\.

1. Commit files in the staging area to the working directory\.

**Important**  
You might not want to commit every file in your working directory to the repository\. For example, you're unlikely to want to add files generated during runtime to your project's repository\. With Git panel, you can mark files to be ignored by adding them to a list in a `.gitignore` file\.  
To update the list in `.gitignore`, right\-click a file that hasn't been added to the staging area and select **Add File to \.gitignore**\. The IDE opens the `.gitignore` file and the name of the selected file is added to the list of ignored files\.  
For information about using pattern matching in `.gitignore` to exclude file types, see the relevant [reference in the git\-scm\.com site](https://git-scm.com/docs/gitignore)\.

------
#### [ Stage files ]

Untracked files \(labelled "U"\) and modified files \(labelled "M"\) that haven't been added to the staging area are listed under **Changes** in the Git panel pane\.

![\[Untracked content in the git repo's workspace folder\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/git-unstaged.png)

Using the Git panel interface, you can add specific files or all untracked and modified files to the staging area:
+ Specific files: Pause on the file and then choose **\+** to add it to the staging area\. Alternatively, right\-click the file and choose **Stage Changes**\.
+ All files: Go to the **Git panel** menu and choose **Stage All Changes**\.

Files added to the repository's index are listed under **Staged Changes**\. Previously untracked files are labelled "A" to indicate that they've been staged\.

![\[Staged content in the git repo's workspace folder\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/staged-changes.png)

**Note**  
You can also unstage specific changes or all changes\. For a single file, pause on the file and then choose **\-**\. Alternatively, right\-click it and choose **Unstage Changes**\. To unstage all changes, go to the **Git panel** menu and choose **Unstage All Changes**\.

------
#### [ Commit files ]

You can use Git's `commit` command to capture staged files as a permanent snapshot in the repository\. Using the Git panel interface, you can choose which files to commit:
+ Commit files in the staging area: Go to **Git panel** menu and choose **Commit** or **Commit Staged**\.
+ Commit all files in working directory: Go to the **Git panel** menu and choose **Commit All**\. \(This option uses the `git add` to add files to the staging area before calling `git commit`\.\) 

**Note**  
You can also use the `amend` and `signed-off` options when committing files with Git panel\. The `amend` option modifies the commit message of the most recent commit\. The `sign-off` option can identify who performed the commit in the Git log\.  
You can also reverse a commit by going to the **Git panel** menu and choosing **Undo Last Commit**

------

## Viewing different file versions<a name="comparing-changes"></a>

You can compare versions of a file that's been modified after it was staged or committed\. 
+ Files listed under **Changes**: Choose the "M" to view the differences between the version in the working directory and the version that was last staged or committed to the repo\. 
+ Files listed under **Staged Changes**: Choose the "M" to view the differences between the version in the staging area and the version that was last committed to the repo\.

After you choose "M", an IDE window displays the differences between the two versions of the file\. One side shows the version that's tracked as current in the repository\. The other side shows the modified version that's not yet committed\.

![\[Diffing versioned content in the git repo\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/git-diff.png)

## Working with branches<a name="working-with-branches"></a>

Git greatly facilitates workflow management by allowing you to work on new features in branches that are independent of the repo's main branch\. You can switch seamlessly between multiple branches while ensuring you always have ready\-to\-build source code in the main branch\.<a name="create-branch-proc"></a>

## Create a branch<a name="create-branch-proc"></a>

Creating a branch involves naming the branch and selecting its starting point\. 

1. In the **Git panel** menu, choose **Checkout to**\. Alternatively, you can choose the name of the current branch displayed at the bottom of the Git panel\.  
![\[Selecting the current Git branch\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/git-current-branch.png)

1. Choose an option for creating a new branch:
   + **Create new branch**: The new branch starts from the last commit of the current branch\.
   + **Create new branch from**: The new branch starts from the last commit of the branch that you select in a subsequent screen\.

1. Enter the new branch's name\.

1. If you're specifying a specific branch as the starting point for your branch, select one from the list\.

After switching to the new branch, you can check the name of the current branch by viewing the bottom of the Git panel\.

**Note**  
If you're working with a remote repository, [publish the new branch](#publish-branch-proc) to the upstream remote repository to allow others to access your content\.<a name="switch-branches-proc"></a>

## Switch branches<a name="switch-branches-proc"></a>

One of the key advantages of managing source control with Git is that you can jump between different projects simply by switching branches\.
**Important**  
You can't switch branches if you have files in the current branch that haven't been committed to your repository\. You must first clean your working directory by [committing](#staging-and-commit) or [stashing](#stashing-work) your work\. 

1. Choose the name of the current branch at the bottom of the Git panel\. Alternatively, go to the **Git panel** and choose **Checkout to**\.

1. Choose a branch from the list displayed\.

After you switch, the repository's working directory is updated with file versions that were most recently committed to the selected branch\. <a name="merge-branch-proc"></a>

## Merge branches<a name="merge-branch-proc"></a>

After you've finished working on a feature in a discrete branch, you'll usually want to integrate your changes into the main project\. With Git, this kind of integration is facilitated by merging one branch \(a feature branch, for example\) into another \(usually the repository’s main or default branch\)\. 

1. To select a branch that you'll merge another branch into, go to the **Git panel** menu and choose **Checkout to**\.

   Alternatively, choose the name of the current branch at the bottom of the Git panel\.

1. From the list that's displayed, choose a branch to switch to\.

1. In the **Search** box for Git panel, start to enter the word "merge"\.

   When Git: Merge Branch displays under the list of **Commands**, choose it\.  
![\[Finding the merge command\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/git-merge.png)

1. From the list displayed, choose a branch to merge into the target branch\.

   If the merge completes without conflicts, the Git panel interface refreshes to show the target branch containing the merged changes\. 

When [merging branches](#working-with-branches), you may encounter merge conflicts that result from incompatible changes that were made to the same content\. If this happens, you're warned that you have to resolve the conflicts before committing the merge\. 

You can use the IDE's code editor window to identify the conflicting content in the two branches and then make changes to resolve the differences\.

![\[IDE window for resolving merge conflicts\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/git-merge-conflicts.png)

## Working with remote repositories<a name="working-with-remote-repos"></a>

Remote repositories that are hosted on the Internet or a network facilitate collaboration by allowing team members to share the changes they've committed to their local responsibilities\. By using Git commands that upload and download data, you ensure the contents of the "downstream" \(local\) repository are synched with those of the "upstream" \(remote\) repository\. <a name="publish-branch-proc"></a>

## Publish a branch to a remote repository<a name="publish-branch-proc"></a>

After you create a branch for a local repository, it's private to you and not available to your collaborators until you push it "upstream" to the remote repository\.

1. To publish the current branch, go to the **Git panel** menu and choose **Publish Branch**\. Alternatively, click the cloud symbol that's next to the branch name at the bottom of the Git panel\.  
![\[Option for publishing a branch to a remote repository\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/publish-branch-image.png)

1. If required, enter your user name and password to access the remote repository\.

If the branch is successfully published to the remote repository, a synchronize symbol displays next to the branch name at the bottom of the Git panel\. Choose it to synchronize the contents of the local and remote repositories\.

![\[Option for synching local and remote branches\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/sync-branch-local-remote.png)

### Push and pull content between local and remote repositories<a name="pushing-and-pulling"></a>

When using Git to collaborate on a shared project, you typically start by pulling recent changes by other team members from the remote repository into your local repo\. And after you committed changes to your local repo, you push them to the remote repository so they can be accessed by the rest of the team\. These actions are performed by the commands `git pull` and `git push`\. 

**Note**  
You need to enter a user name and password when pushing and pulling changes to and from most hosted repositories \(such as those on GitHub, for example\)\.

------
#### [ Pull changes from remote ]

Using the `git pull` command through the Git panel interface, you can update your local repository with the latest changes committed to a branch in the remote repository\. 

1. In the **Git panel** menu, choose **Checkout to**\.

1. In the list of branches, choose the local branch you want to pull changes into\.

1. Next, go to the **Git panel** menu and choose **Pull from**\.

1. Pick a remote repository and then a branch in that repository to pull changes from\.

After doing a pull, you can access the files retrieved from the remote repo in your repository working directory\. After you modify the files, you can then push your changes to the remote branch\. 

------
#### [ Push changes to remote ]

Using the `git push` command through the Git panel interface, you can update the remote repository with the latest changes in a specified branch in your local repository\. 

1. In the **Git panel** menu, choose **Checkout to**\.

1. In the list of branches, choose the local branch you want to push changes from\.

1. Next, go to the **Git panel** menu and choose **Push to**\.

1. Pick a remote repository and then a branch in that repository to push changes to\.

After doing a push, other team members can access your changes by pulling them down to their own local copies of the repository\. 

------

## Stashing and retrieving files<a name="stashing-work"></a>

With the stash feature of Git, you can switch branches without first having to commit staged or modified files\. The stash feature captures the current status of the working directory and staging area and saves it for later use\. This feature is useful whenever you're still working on unfinished content and need to switch branches without delay\.<a name="stash-work-proc"></a>

**Stash work**

1. To stash your working directory's current state, go to the **Git panel** menu and choose one of the following options:
   + **Stash**: All modified or staged files in working directory are added to the stash\. Untracked files aren't added\.
   + **Stash \(include Untracked\)**: All files in the working directory, including those not yet tracked, are added to the stash\.

1. Enter an optional message that will help you identify the stash for future retrieval\. 

After stashing, the Git panel interface refreshes to display the working directory that's been cleaned\.<a name="retrieve-work-proc"></a>

**Retrieve a stash**

1. To retrieve a stash and apply it to your working directory, go to the **Git panel** menu and choose one of the following options:
   + **Apply Stash**: Apply a selected stash to your working directory and keep the stash for later use\.
   + **Pop Stash**: Apply a selected stash to your working directory and delete the stash from the stash stack\. 
**Note**  
You can also choose to apply or pop the last stash that was added to the stash stack\.

1. Select a stash to apply to the working directory\.

The Git panel interface refreshes to display your working directory with the stash applied\.