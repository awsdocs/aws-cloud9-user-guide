# Visual source control with Git panel<a name="source-control-gitpanel"></a>

Git panel for AWS Cloud9 provides a convenient visual interface for using essential Git features\.

Using options from the Git panel interface, you can manage the complete source control lifecycle: initializing a repository or cloning a remote repo, adding files to the staging area, committing staged files to the working directory, and then pushing changes to an upstream repository\. 

Core collaboration and project\-management features of Git, such as creating and merging branches, can quickly be implemented with a few clicks in the Git panel interface\. Moreover, merge conflicts can be identified and resolved using the IDE's editor windows\.

**Important**  
Currently, Git panel is available by default only in new AWS Cloud9 environments that are created after December 11, 2020\. We're working on enabling Git panel for development environments that were created before this date\.

To access and interact with the interface, choose **Window**, **Source Control**\. Alternatively, you can get to the Source Control by right\-clicking anywhere in the IDE's side panels and choosing **Source Control**\. Then, after this, choose the Git icon that's displayed in the IDE interface\.

The key combination **Ctrl\-Shift\-G** can also be used to toggle the display of Git panel\.

![\[Displaying the Git panel interface\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/select-git-panel.png)

**Note**  
Screenshots for Git panel documentation show the AWS Cloud9 IDE with the *Jett Dark* theme applied\. Some interface elements are displayed differently if you're using the IDE with a different theme\. To open the Git panel, you may choose a link with the label **Source Control** instead of the Git icon\. 

**Topics**
+ [Managing source control with Git panel](using-gitpanel.md)
+ [Reference: Git commands available in Git panel](gitpanel-reference.md)