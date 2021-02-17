# Reference: Git commands available in Git panel<a name="gitpanel-reference"></a>

The Git panel menu for AWS Cloud9 provides convenient user interface access to both core and advanced git commands\.

Certain git commands—such as those used to merge and delete branches, for example—are only available through the Git panel search field\.

You can also customize how Git panel runs commands and interacts with repositories\. To modify the default settings, first choose **AWS Cloud9**, **Preferences**\. Next, in the **Preferences** window, under **Project Settings**, choose **Git**\. 

Pause over the information icons to read brief descriptions of the settings\.

![\[Displaying the Git panel interface\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/git-preferences.png)

**Note**  
You can access detailed documentation on the Git commands listed from the official Git site: [https://git\-scm\.com/doc](https://git-scm.com/doc)\.

## Reference for Git commands available from Git panel menu<a name="git-menu-options"></a>

You access the options on the **Git panel** menu by choosing the symbol opposite the repository's name\.

![\[Displaying the Git panel interface\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/git-menu-access.png)


**Git panel menu**  

| Menu option | Description | 
| --- | --- | 
|  **Commit**  |  Commits the content added the staging area to the working directory of the repo\. Adds a commit message\.   | 
|  **Refresh**  |  Refreshes the GitPanel interface to show the status of the working directory and the staging area\.   | 
|  **Pull**  |  Pulls the latest changes from a remote repository to the local repository\.  | 
|  **Pull \(Rebase\)**  |  Reapplies your local changes to the remote changes pulled from a remote branch\.  | 
|  **Push from\.\.\.**  |  Pushes the changes committed to a branch in your local repository to the branch in the remote repository\.  | 
|  **Push**  |  Pushes changes committed to the local repository to the remote repository\.  | 
|  **Push to\.\.\.**  |  Pushes the changes committed to a branch in your local repository to the branch in the remote repository\.  | 
|  **Sync**  |  Syncs the contents of the local and remote repositories by running a `git pull` command followed by a `git push` command\.  | 
|  **Checkout to\.\.\.**  |  Switches to an existing branch or creates a branch and switches to it\.  | 
|  **Publish Branch**  |  Publishes a private branch created on the local repository and makes it available on the remote repository\.   | 
|  **Commit All**  |  Commits both staged and unstaged files to the repository\. \(A `git add -A` command is run to add files to the staging area before the `git commit` command is run\.\)  | 
|  **Commit All \(Amend\)**  |  Modifies the message of the last commit\. \(Adds the `-amend` option when running the `git commit` command\.\)  | 
|  **Commit All \(Signed Off\)**  |  Identifies who performed the commit in the Git log\. \(Adds the `-signed-off` option when running the `git commit` command\.\)   | 
|  **Commit Staged**  |  Commits only staged files to the repository\.  | 
|  **Commit Staged \(Amend\)**  |  Modifies the message of the last commit\. \(Adds the `-amend` option when running the `git commit` command\.\)  | 
|  **Commit Staged \(Signed Off\)**  |  Identifies who performed the commit in the Git log\. \(Adds the `-signed-off` option when running the `git commit` command\.\)  | 
|  **Undo Last Commit **  |  Undoes the previous commit\. Files are moved back into the staging area\.  | 
|  **Discard All Changes**  |  Deletes all files and folders from the staging area of the repository\.  | 
|  **Stage All Changes**  | Adds untracked and modified content to the staging area\.  | 
|  **Unstage All Changes**  |  Moves all files out of the staging area\. Unstaged files can't be committed to the repository\.   | 
|  **Apply Latest Stash**  |  Applies the last stash that was added to the stack stash to the working directory\. The stash remains on the stack\.  | 
|  **Apply Stash\.\.\.**  |  Applies a stash that's selected from the stash stack to the working directory\. The stash remains on the stack\.  | 
|  **Pop Latest Stash**  |  Applies the last stash that was added to the stack stash to the working directory\. The stash is then deleted from the stack\.  | 
|  **Pop Stash\.\.\.**  |  Applies a selected stash to the working directory\. The stash is then deleted from the stack\.  | 
|  **Stash**  |  Adds modified and staged files in the working directory to a named stash\.  | 
|  **Stash \(include Untracked\)**  |  Adds all files, including untracked files, in the working directory to a named stash\.  | 
|  **Show Git Output**  |  Displays a window showing the Git commands that are run when you interact with the Git panel interface\.  | 

## Git commands available from the Git panel search field<a name="git-commands-search.title"></a>

 You can also access some supported Git command that aren't available in the Git panel menu by typing "git" in the search box:

![\[Interface options for initializing and cloning a Git repository\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/git-filter.png)

The following table provides a description of selected Git commands that you can access this way\. 


**Selected Git commands**  

| Menu option | Description | 
| --- | --- | 
|  **Git: Add Remote**  |  Adds a connection to a remote repository to your Git config file   | 
|  **Git: Delete Branch**  |  Deletes a specified branch\.   | 
|  **Git: Fetch**  |  Downloads the content from a branch in remote repository\. In contrast with a `git pull`, the remote changes aren't merged into local repository\.   | 
|  **Git: Merge Branch**  |  Integrates the changes made in one branch into another branch\. For more information, see the [merge branches procedure](using-gitpanel.md#merge-branch-proc)\.  | 