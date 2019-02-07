# Working with File Revisions in the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="file-revisions"></a>

You can use the **File Revision History** pane in the AWS Cloud9 IDE to view and manage changes to a file in an AWS Cloud9 EC2 development environment\. The **File Revision History** pane is not available for files in an AWS Cloud9 SSH development environment\.

![\[The File Revision History pane\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-file-revision.gif)

To show the **File Revision History** pane for a file, open the file in the editor\. Then, on the menu bar, choose **File, Show File Revision History**\.

The **File Revision History** pane begins tracking a file's revision history in the IDE after you first open the file in the editor in an environment, and only for that environment\. The **File Revision History** pane tracks a file's revisions only from the editor itself\. It does not track a file's revisions made in any other way \(for example by the terminal, Git, or other file revision tools\)\.

You cannot edit a file while the **File Revision History** pane is displayed\. To hide the pane, choose **File, Show Revision History** again, or choose the **X** \(**Close timeslider**\) in the corner of the pane\.

To jump to a version of the file that is associated with a file save action, choose a **File Saved on** dot above the revision slider\.

![\[File save points in the File Revision History pane\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-file-revision-save.png)

To go forward or backward one version from the currently selected version of the file on the revision slider, choose one of the step arrows \(**Step revision forward** or **Step revision backward**\)\.

![\[Moving forward and backward through file versions in the File Revision History pane\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-file-revision-move.png)

To go forward automatically one version of the file at a time from the beginning to end of the revision history, choose the play button \(**Playback file history**\)\.

To make the currently selected version of the file the latest version in the revision history, choose **Revert**\.