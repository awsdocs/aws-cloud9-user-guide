# Working with User Settings in the AWS Cloud9 IDE<a name="settings-user"></a>

 *User settings* are settings that apply across each AWS Cloud9 development environment associated with your AWS Identity and Access Management \(IAM\) user\. They include the following kinds of settings:
+ General user interface behaviors, such as enabling animations and marking changed tabs
+ File system navigation behaviors
+ File find and search behaviors
+ Color schemes for terminal sessions and output
+ Additional code editor behaviors, such as font sizes, code folding, full line selection, scrolling animations, and font sizes

As you change your user settings, AWS Cloud9 pushes those changes to the cloud and associates them with your IAM user\. AWS Cloud9 also continually scans the cloud for changes to user settings associated with your IAM user, and applies those settings to your current environment\. This behavior enables you to experience the same look and feel no matter what AWS Cloud9 environment you're working in\.

**Note**  
To store and retrieve your IDE settings, AWS Cloud9 uses the internal APIs `GetUserSettings` and `UpdateUserSettings`\.

You can share your user settings with other users, as follows:
+  [View or Change Your User Settings](#settings-user-view) 
+  [Share Your User Settings with Another User](#settings-user-share) 
+  [User Setting Changes You Can Make](#settings-user-change) 

## View or Change Your User Settings<a name="settings-user-view"></a>

1. On the menu bar, choose **AWS Cloud9**, **Preferences**\.

1. To view your user settings across each of your environments, on the **Preferences** tab, in the side navigation pane, choose **User Settings**\.

1. In the **User Settings** pane, change your user settings across each of your environments\.

1. To apply your changes to any other of your environments, simply open that environment\. If that environment is already open, refresh the web browser tab for that environment\.

For more information, see [User Setting Changes You Can Make](#settings-user-change)\.

## Share Your User Settings with Another User<a name="settings-user-share"></a>

1. In both the source and target environment, on the menu bar of the AWS Cloud9 IDE, choose **AWS Cloud9, Open Your User Settings**\.

1. In the source environment, copy the contents of the **user\.settings** tab that is displayed\.

1. In the target environment,overwrite the contents of the **user\.settings** tab with the copied contents from the source environment\.

1. In the target environment, save the **user\.settings** tab\.

## User Setting Changes You Can Make<a name="settings-user-change"></a>

These sections describe the kinds of user settings you can change in the **User Settings** pane on the **Preferences** tab:
+  [General](#settings-user-change-general) 
+  [User Interface](#settings-user-change-user-interface) 
+  [Collaboration](#settings-user-change-collaboration) 
+  [Tree and Go Panel](#settings-user-change-tree-and-navigate) 
+  [Find in Files](#settings-user-change-find-in-files) 
+  [Meta Data](#settings-user-change-meta-data) 
+  [Watchers](#settings-user-change-watchers) 
+  [Terminal](#settings-user-change-terminal) 
+  [Output](#settings-user-change-output) 
+  [Code Editor \(Ace\)](#settings-user-change-code-editor-ace) 
+  [Input](#settings-user-change-input) 
+  [Hints & Warnings](#settings-user-change-hints-and-warnings) 
+  [Run & Debug](#settings-user-change-run-and-debug) 
+  [Preview](#settings-user-change-preview) 
+  [Build](#settings-user-change-build) 

### General<a name="settings-user-change-general"></a>

** **Reset to Factory Settings** **  
If you choose the **Reset to Default** button, AWS Cloud9 resets all of your user settings to the AWS Cloud9 default user settings\. To confirm, choose **Reset settings**\.  
You can't undo this action\.

** **Warn Before Exiting** **  
Whenever you attempt to close the IDE, AWS Cloud9 asks you to confirm that you want to exit\.

### User Interface<a name="settings-user-change-user-interface"></a>

** **Enable UI Animations** **  
AWS Cloud9 uses animations in the IDE\.

** **Use an Asterisk \(\*\) to Mark Changed Tabs** **  
AWS Cloud9 adds an asterisk \(**\***\) to tabs that have changes, but for which the contents have not yet been saved\.

** **Display Title of Active Tab as Browser Title** **  
AWS Cloud9 changes the title of the associated web browser tab to the title of the active tab \(for example, **Untitled1**, **hello\.js**, **Terminal**, **Preferences**, and so on\)\.

** **Automatically Close Empty Panes** **  
Whenever you reload an environment, AWS Cloud9 automatically closes any panes it considers are empty\.

** **Environment Files Icon and Selection Style** **  
The icon AWS Cloud9 uses for environment files, and the file selection behaviors AWS Cloud9 uses\.  
Valid values include:  
+  **Default** – AWS Cloud9 uses default icons and default file selection behaviors\.
+  **Alternative** – AWS Cloud9 uses alternative icons and alternative file selection behaviors\.

### Collaboration<a name="settings-user-change-collaboration"></a>

** **Show Notification Bubbles** **  
AWS Cloud9 displays notifications if the environment is a shared environment and multiple users are actively collaborating in that shared environment\.

** **Disable collaboration security warning** **  
When a read/write member is added to an environment, AWS Cloud9 does not display the security warning dialog box\.

** **Show Authorship Info** **  
AWS Cloud9 underlines text entered by other environment members with related highlights in the gutter\.

### Tree and Go Panel<a name="settings-user-change-tree-and-navigate"></a>

** **Scope Go to Anything to Favorites** **  
**Go to File** in the **Go** window displays results scoped only to **Favorites** in the **Environment** window\.

** **Enable Preview on Go to Anything** **  
**Go to File** in the **Go** window displays matching file contents as you type\.

** **Enable Preview on Tree Selection** **  
AWS Cloud9 displays the chosen file with a single mouse click instead of a double mouse click\.

** **Hidden File Pattern** **  
The types of files for AWS Cloud9 to treat as hidden\.

** **Reveal Active File in Project Tree** **  
AWS Cloud9 highlights the active file in the **Environment** window\.

** **Download Files As** **  
The behavior for AWS Cloud9 to use when downloading files\.  
Valid values include:  
+  **auto** – AWS Cloud9 downloads files without modification\.
+  **tar\.gz** – AWS Cloud9 downloads files as compressed TAR files\.
+  **auto** – AWS Cloud9 downloads files as \.zip files\.

### Find in Files<a name="settings-user-change-find-in-files"></a>

** **Search In This Path When 'Project' Is Selected** **  
On the find in files bar, when **Project** is selected for the search scope, the path to search in\.

** **Show Full Path in Results** **  
Displays the full path to each matching file in the **Search Results** tab\.

** **Clear Results Before Each Search** **  
Clears the **Search Results** tab of the results of any previous searches before the current search begins\.

** **Scroll Down as Search Results Come In** **  
Scrolls the **Search Results** tab to the bottom of the list of results as search results are identified\.

** **Open Files when Navigating Results with \(Up and Down\)** **  
As the up and down arrow keys are pressed in the **Search Results** tab within the list of results, opens each matching file\.

### Meta Data<a name="settings-user-change-meta-data"></a>

** **Maximum of Undo Stack Items in Meta Data** **  
The maximum number of items that AWS Cloud9 keeps in its list of actions that can be undone\.

### Watchers<a name="settings-user-change-watchers"></a>

** **Auto\-Merge Files When a Conflict Occurs** **  
AWS Cloud9 attempts to automatically merge files whenever a merge conflict happens\.

### Terminal<a name="settings-user-change-terminal"></a>

** **Text Color** **  
The color of text in **Terminal** tabs\.

** **Background Color** **  
The background color in **Terminal** tabs\.

** **Selection Color** **  
The color of selected text in **Terminal** tabs\.

** **Font Family** **  
The text font style in **Terminal** tabs\.

** **Font Size** **  
The size of text in **Terminal** tabs\.

** **Antialiased Fonts** **  
AWS Cloud9 attempts to smooth the display of text in **Terminal** tabs\.

** **Blinking Cursor** **  
AWS Cloud9 continuously blinks the cursor in **Terminal** tabs\.

** **Scrollback** **  
The number of lines that you can scroll up or back through in **Terminal** tabs\.

** **Use AWS Cloud9 as the Default Editor** **  
Uses AWS Cloud9 as the default text editor\.

### Output<a name="settings-user-change-output"></a>

** **Text Color** **  
The color of text in tabs that display output\.

** **Background Color** **  
The background color of text in tabs that display output\.

** **Selection Color** **  
The color of selected text in tabs that display output\.

** **Warn Before Closing Unnamed Configuration** **  
AWS Cloud9 prompts you to save any unsaved configuration tab before it is closed\.

** **Preserve log between runs** **  
AWS Cloud9 keeps a log of all attempted runs\.

### Code Editor \(Ace\)<a name="settings-user-change-code-editor-ace"></a>

** **Auto\-pair Brackets, Quotes, etc\.** **  
AWS Cloud9 attempts to add a matching closing character for each related starting character that is typed in editor tabs, such as for brackets, quotation marks, and braces\.

** **Wrap Selection with Brackets, Quote, etc\.** **  
AWS Cloud9 attempts to insert a matching closing character at the end of text in editor tabs after the text is selected and a related started character is typed, such as for brackets, quotation marks, and braces\.

** **Code Folding** **  
AWS Cloud9 attempts to show, expand, hide, or collapse sections of code in editor tabs according to related code syntax rules\.

** **Fade Fold Widgets** **  
AWS Cloud9 displays code folding controls in the gutter whenever you pause the mouse over those controls in editor tabs\.

** **Full Line Selection** **  
 AWS Cloud9 selects an entire line that is triple\-clicked in editor tabs\.

** **Highlight Active Line** **  
AWS Cloud9 highlights the entire active line in editor tabs\.

** **Highlight Gutter Line** **  
AWS Cloud9 highlights the location in the gutter next to the active line in editor tabs\.

** **Show Invisible Characters** **  
AWS Cloud9 displays what it considers to be invisible characters in editor tabs, for example, carriage returns and line feeds, spaces, and tabs\.

** **Show Gutter** **  
AWS Cloud9 displays the gutter\.

** **Show Line Numbers** **  
The behavior for displaying line numbers in the gutter\.  
Valid values include:  
+  **Normal** – Display line numbers\.
+  **Relative** – Display line numbers relative to the active line\.
+  **None** – Hide line numbers\.

** **Show Indent Guides** **  
AWS Cloud9 displays guides to more easily visualize indented text in editor tabs\.

** **Highlight Selected Word** **  
AWS Cloud9 selects an entire word that is double\-clicked in an editor tab\.

** **Scroll Past the End of the Document** **  
The behavior for allowing the user to scroll past the end of the current file in editor tabs\.  
Valid values include:  
+  **Off** – Do not allow any scrolling past the end of the current file\.
+  **Half Editor Height** – Allow scrolling past the end of the current file to up to half the editor's screen height\.
+  **Full Editor Height** – Allow scrolling past the end of the current file to up to the editor's full screen height\.

** **Animate Scrolling** **  
AWS Cloud9 applies animation behaviors during scrolling actions in editor tabs\.

** **Font Family** **  
The style of font to use in editor tabs\.

** **Font Size** **  
The size of the font to use in editor tabs\.

** **Antialiased Fonts** **  
AWS Cloud9 attempts to smooth the display of text in editor tabs\.

** **Show Print Margin** **  
Displays a vertical line in editor tabs after the specified character location\.

** **Mouse Scroll Speed** **  
The relative speed of mouse scrolling in editor tabs\. Larger values result in faster scrolling\.

** **Cursor Style** **  
The style and behavior of the cursor in editor tabs\.  
Valid values include:  
+  **Ace** – Display the cursor as a vertical bar that is relatively wider than **Slim**\.
+  **Slim** – Display the cursor as a relatively slim vertical bar\.
+  **Smooth** – Display the cursor as a vertical bar that is relatively wider than **Slim** and that blinks more smoothly than **Slim**\.
+  **Smooth and Slim** – Display the cursor as a relatively slim vertical bar that blinks more smoothly than **Slim**\.
+  **Wide** – Display the cursor as a relatively wide vertical bar\.

 **Merge Undo Deltas** 
+  **Always** – Allow merge conflicts to be reverted\.
+  **Never** – Never allow merge conflicts to be reverted\.
+  **Timed** – Allow merge conflicts to be reverted after a specified time period\.

** **Enable Wrapping For New Documents** **  
AWS Cloud9 wraps code in new files\.

### Input<a name="settings-user-change-input"></a>

** **Complete As You Type** **  
AWS Cloud9 attempts to display possible text completions as you type\.

** **Complete On Enter** **  
AWS Cloud9 attempts to display possible text completions after you press **Enter**\.

** **Highlight Variable Under Cursor** **  
AWS Cloud9 highlights all references in code to the selected variable\.

** **Use Cmd\-Click for Jump to Definition** **  
AWS Cloud9 goes to any original definition for code that is clicked while pressing and holding **Command** for Mac or **Ctrl** for Windows\.

### Hints & Warnings<a name="settings-user-change-hints-and-warnings"></a>

** **Enable Hints and Warnings** **  
AWS Cloud9 displays applicable hint and warning messages\.

** **Ignore Messages Matching Regex** **  
AWS Cloud9 does not display any messages matching the specified regular expression\. For more information, see [Writing a regular expression pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions#Writing_a_regular_expression_pattern) in the *JavaScript Regular Expressions* topic on the Mozilla Developer Network\.

### Run & Debug<a name="settings-user-change-run-and-debug"></a>

** **Save All Unsaved Tabs Before Running** **  
Before running the associated code, AWS Cloud9 attempts to save all unsaved files with open tabs\.

### Preview<a name="settings-user-change-preview"></a>

** **Preview Running Apps** **  
AWS Cloud9 attempts to display a preview of the output for the code in the active tab whenever the **Preview** button is chosen\.

** **Default Previewer** **  
The format AWS Cloud9 uses to preview code output\.  
Valid values include:  
+  **Raw** – Attempt to display code output in a plain format\.
+  **Browser** – Attempt to display code output in a format that is preferred for web browsers\.

** **When Saving Reload Previewer** **  
The behavior AWS Cloud9 uses for previewing code output whenever a code file is saved\.  
Valid values include:  
+  **Only on Ctrl\-Enter** – Attempt to preview code output whenever **Ctrl\+Enter** is pressed for the current code tab\.
+  **Always** – Attempt to preview code output whenever a code file is saved\.

### Build<a name="settings-user-change-build"></a>

** **Automatically Build Supported Files** **  
AWS Cloud9 attempts to automatically build the current code if a build action is triggered and the code is in a supported format\.