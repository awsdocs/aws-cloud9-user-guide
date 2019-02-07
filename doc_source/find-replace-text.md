# Finding and Replacing Text in the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="find-replace-text"></a>

You can use the find and replace bar in the AWS Cloud9 IDE to find and replace text in a single file or multiple files\.
+  [Find Text in a Single File](#find-replace-text-find-single) 
+  [Replace Text in a Single File](#find-replace-text-replace-single) 
+  [Find Text in Multiple Files](#find-replace-text-find-multiple) 
+  [Replace Text in Multiple Files](#find-replace-text-replace-multiple) 
+  [Find and Replace Options](#find-replace-text-replace-options) 

## Find Text in a Single File<a name="find-replace-text-find-single"></a>

1. Open the file you want to find text in\. If the file is already open, choose the file's tab to make the file active\.

1. On the menu bar, choose **Find, Find**\.

1. In the find and replace bar, for **Find**, type the text you want to find\.

1. To specify additional find options, see [Find and Replace Options](#find-replace-text-replace-options)\.

1. If there are any matches, **0 of 0** in the **Find** box changes to non\-zero numbers\. If there are any matches, the editor goes to the first match\. If there is more than one match, to go to the next match, choose the right arrow in the **Find** box or choose **Find, Find Next** on the menu bar\. To go to the previous match, choose the left arrow in the **Find** box or choose **Find, Find Previous** on the menu bar\.

## Replace Text in a Single File<a name="find-replace-text-replace-single"></a>

1. Open the file you want to replace text in\. If the file is already open, choose the file's tab to make the file active\.

1. On the menu bar, choose **Find, Replace**\.

1. In the find and replace bar, for **Find**, type the text you want to find\.

1. For **Replace With**, type the text you want to replace the text in **Find** with\.

1. To specify additional find and replace options, see [Find and Replace Options](#find-replace-text-replace-options)\.

1. If there are any matches, **0 of 0** in the **Find** box changes to non\-zero numbers\. If there are any matches, the editor goes to the first match\. If there is more than one match, to go to the next match, choose the right arrow in the **Find** box or choose **Find, Find Next** on the menu bar\. To go to the previous match, choose the left arrow in the **Find** box or choose **Find, Find Previous** on the menu bar\.

1. To replace the current match with the text in **Replace With** and then go to the next match, choose **Replace**\. To replace all matches with the text in **Replace With**, choose **Replace All**\.

## Find Text in Multiple Files<a name="find-replace-text-find-multiple"></a>

1. On the menu bar, choose **Find, Find in Files**\.

1. In the find and replace bar, for **Find**, type the text you want to find\.

1. To specify additional find options, see [Find and Replace Options](#find-replace-text-replace-options)\.

1. In the box to the right of the **Find** button \(the box with `*.*, -.*`\), type any set of files to include or exclude in the find\. For example:
   + Blank, `*`, or `*.*`: Find all files\.
   +  `my-file.txt`: Find only the file named `my-file.txt`\.
   +  `my*`: Find only files with file names starting with `my`\.
   +  `my*.txt`: Find only files with file names starting with `my` and that have the file extension `.txt`\.
   +  `my*.htm*`: Find all files with file names starting with `my` and a file extension starting with `.htm`\.
   +  `my*.htm, my*.html`: Find all files with file names starting with `my` and the file extension `.htm` or `.html`\.
   +  `-my-file.txt`: Do not search the file named `my-file.txt`\.
   +  `-my*`: Do not search any files starting with `my`\.
   +  `-my*.htm*`: Do not search any files with file names starting with `my` and a file extension starting with `.htm`\.
   +  `my*.htm*, -my*.html`: Search all files with file names starting with `my` and a file extension starting with `.htm`\. However, do not search any files with file names starting with `my` and a file extension of `.html`\.

1. In the drop\-down list next to the preceding box, choose one of the following to further restrict the find to only specific locations:
   +  **Environment**: Find only files in the **Environment** window\.
   +  **Project \(excludes \.gitignore'd\)**: Find any file in the environment, except for files or file types listed in the `.gitignore` file in the environment, if a `.gitignore` file exists\.
   +  **Selection:**: Find only files that are currently selected in the **Environment** window\.
**Note**  
To further restrict the find to only a single folder, choose a folder in the **Environment** window and then choose **Selection**\. Alternatively, you can right\-click the folder in the **Environment** window, and then choose **Search In This Folder** on the context menu\.
   +  **Favorites**: Find only files in the **Favorites** list in the **Environment** window\.
   +  **Active File**: Find only the active file\.
   +  **Open Files**: Find only files in the **Open Files** list in the **Environment** window\.

1. Choose **Find**\.

1. To go to a file containing matches, double\-click the file name on the **Search Results** tab\. To go to a specific match, double\-click the match in the **Search Results** tab\.

## Replace Text in Multiple Files<a name="find-replace-text-replace-multiple"></a>

1. On the menu bar, choose **Find, Find in Files**\.

1. In the find and replace bar, for **Find**, type the text you want to find\.

1. To specify additional find options, see [Find and Replace Options](#find-replace-text-replace-options)\.

1. In the box to the right of the **Find** button \(the box with `*.*, -.*`\), type any set of files to include or exclude in the find\. For example:
   + Blank, `*`, or `*.*`: All files\.
   +  `my-file.txt`: Only the file named `my-file.txt`\.
   +  `my*`: Only files with file names staring with `my`\.
   +  `my*.txt`: Only files with file names starting with `my` and that have the file extension `.txt`\.
   +  `my*.htm*`: All files with file names starting with `my` and a file extension starting with `.htm`\.
   +  `my*.htm, my*.html`: All files with file names starting with `my` and the file extension `.htm` or `.html`\.
   +  `-my-file.txt`: Do not search the file named `my-file.txt`\.
   +  `-my*`: Do not search any files starting with `my`\.
   +  `-my*.htm*`: Do not search any files with file names starting with `my` and a file extension starting with `.htm`\.
   +  `my*.htm*, -my*.html`: Search all files with file names starting with `my` and a file extension starting with `.htm`\. However, do not search any files with file names starting with `my` and a file extension of `.html`\.

1. In the drop\-down list next to the preceding box, choose one of the following to further restrict the find to only specific locations:
   +  **Environment**: Only files in the **Environment** window\.
   +  **Project \(excludes \.gitignore'd\)**: Any file in the environment, except for files or file types listed in the `.gitignore` file in the environment, if a `.gitignore` file exists\.
   +  **Selection: /**: Only files that are currently selected\.
   +  **Favorites**: Only files in the **Favorites** list in the **Environment** window\.
   +  **Active File**: Only the active file\.
   +  **Open Files**: Only files in the **Open Files** list in the **Environment** window\.

1. For **Replace With**, type the text you want to replace **Find** with\.

1. Choose **Replace**\.
**Note**  
The replace operation happens immediately across all files in scope\. This operation cannot be easily undone\. If you want to see what will be changed before you start the replace operation, choose **Find** instead\.

1. To go to a file containing replacements, double\-click the file name in the **Search Results** tab\. To go to a specific replacement, double\-click the replacement in the **Search Results** pane\.

## Find and Replace Options<a name="find-replace-text-replace-options"></a>

Choose any of the following buttons on the find and replace bar to modify find and replace operations\.

![\[Searching in a single file\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-search-single.png)

![\[Searching in multiple files\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-search-multiple.png)
+  **Regular Expressions**: Find text matching the specified regular expression in **Find** or **Find in Files**\. See [Writing a regular expression pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions#Writing_a_regular_expression_pattern) in the *JavaScript Regular Expressions* topic on the Mozilla Developer Network\.
+  **Match Case**: Find text matching the specified casing in **Find** or **Find in Files**\.
+  **Whole Words**: Use standard word character rules to find text in **Find** or **Find in Files**\.
+  **Wrap Around**: For a single file only, do not stop at the end or beginning of the file when going to the next or previous match\.
+  **Search Selection**: For a single file only, find only in the selection\.
+  **Show in Console**: For multiple files, show the **Search Results** tab in the **Console** instead of the active pane\.
+  **Preserve Case**: For a single file only, preserve casing as applicable when replacing text\.