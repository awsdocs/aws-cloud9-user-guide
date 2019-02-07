# Working with User Settings in the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="settings-user"></a>

 *User settings*, which apply across each AWS Cloud9 development environment associated with your IAM user, include the following kinds of settings:
+ General user interface behaviors, such as whether to enable animations
+ File system navigation behaviors
+ File find and search behaviors
+ Color schemes for terminal sessions and output
+ Additional code editor behaviors, such as code folding, full line selection, scrolling animations, and font sizes

As you make changes to your user settings, AWS Cloud9 pushes those changes to the cloud and associates them with your IAM user\. AWS Cloud9 also continually scans the cloud for changes to user settings associated with your IAM user, and applies those settings to your current environment\.

You can share your user settings with other users\.
+  [View or Change Your User Settings](#settings-user-view) 
+  [Share Your User Settings with Another User](#settings-user-share) 
+  [User Setting Changes You Can Make](#settings-user-change) 

## View or Change Your User Settings<a name="settings-user-view"></a>

1. On the menu bar, choose **AWS Cloud9**, **Preferences**\.

1. To view your user settings across each environment of yours, on the **Preferences** tab, in the side navigation pane, choose **User Settings**\.

1. To change your user settings across each environment of yours, in the **User Settings** pane, change the settings you want\.

1. To apply your changes to any other environment of yours, simply open that environment\. If that environment is already open, refresh the web browser tab for that environment\.

For more information, see [User Setting Changes You Can Make](#settings-user-change)\.

## Share Your User Settings with Another User<a name="settings-user-share"></a>

1. In both the source and target environment, on the menu bar of the AWS Cloud9 IDE, choose **AWS Cloud9, Open Your User Settings**\.

1. In the source environment, copy the contents of the **user\.settings** tab that is displayed\.

1. In the target environment, overwrite the contents of the **user\.settings** tab with the copied contents from the source environment\.

1. In the target environment, save the **user\.settings** tab\.

## User Setting Changes You Can Make<a name="settings-user-change"></a>

These sections describe the kinds of user settings on the **Preferences** tab's **User Settings** pane that you can change\.
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
If the **Reset to Default** button is chosen, AWS Cloud9 resets all of your user settings to the AWS Cloud9 default user settings\. To confirm, choose **Reset settings**\.  
This action cannot be undone\.

** **Warn Before Exiting** **  
If enabled, whenever you attempt to close the IDE, AWS Cloud9 will prompt you about whether you really want to exit AWS Cloud9\.

### User Interface<a name="settings-user-change-user-interface"></a>

** **Enable UI Animations** **  
If enabled, AWS Cloud9 uses animations in the IDE\.

** **Use an Asterisk \(\*\) to Mark Changed Tabs** **  
If enabled, AWS Cloud9 adds an asterisk \(**\***\) to tabs that have changes, but for which the contents have not yet been saved\.

** **Display Title of Active Tab as Browser Title** **  
If enabled, AWS Cloud9 changes the title of the associated web browser tab to the title of the active tab \(for example, **Untitled1**, **hello\.js**, **Terminal**, **Preferences**, and so on\)\.

** **Automatically Close Empty Panes** **  
If enabled, whenever you reload an environment, AWS Cloud9 automatically closes any panes it considers are empty\.

** **Environment Files Icon and Selection Style** **  
The icon AWS Cloud9 uses for environment files, and the file selection behaviors AWS Cloud9 uses\.  
Valid values include:  
+  **Default** for AWS Cloud9 to use default icons and default file selection behaviors\.
+  **Alternative** for AWS Cloud9 to use alternative icons and alternative file selection behaviors\.

### Collaboration<a name="settings-user-change-collaboration"></a>

** **Show Notification Bubbles** **  
If enabled, AWS Cloud9 displays notifications if the environment is a shared environment and multiple users are actively collaborating in that shared environment\.

** **Disable collaboration security warning** **  
If enabled, AWS Cloud9 does not display the security warning dialog box when a read/write member is added to an environment\.

** **Show Authorship Info** **  
If enabled, AWS Cloud9 underlines text entered by other environment members with related highlights in the gutter\.

### Tree and Go Panel<a name="settings-user-change-tree-and-navigate"></a>

** **Scope Go to Anything to Favorites** **  
If enabled, **Go to File** in the **Go** window displays results scoped only to **Favorites** in the **Environment** window\.

** **Enable Preview on Go to Anything** **  
If enabled, **Go to File** in the **Go** window displays matching file contents as you type\.

** **Enable Preview on Tree Selection** **  
If enabled, AWS Cloud9 displays the chosen file with a single mouse click instead of a double mouse click\.

** **Hidden File Pattern** **  
The types of files for AWS Cloud9 to treat as hidden\.

** **Reveal Active File in Project Tree** **  
If enabled, AWS Cloud9 highlights the active file in the **Environment** window\.

** **Download Files As** **  
The behavior for AWS Cloud9 to use when downloading files\.  
Valid values include:  
+  **auto** for AWS Cloud9 to download files without modification\.
+  **tar\.gz** for AWS Cloud9 to download files as compressed TAR files\.
+  **auto** for AWS Cloud9 to download files as \.zip files\.

### Find in Files<a name="settings-user-change-find-in-files"></a>

** **Search In This Path When 'Project' Is Selected** **  
On the find in files bar, when **Project** is selected for the search scope, the path to find in\.

** **Show Full Path in Results** **  
If selected, displays the full path to each matching file in the **Search Results** tab\.

** **Clear Results Before Each Search** **  
If selected, clears the **Search Results** tab of the results of any previous searches before the current search begins\.

** **Scroll Down as Search Results Come In** **  
If selected, scrolls the **Search Results** tab to the bottom of the list of results as search results are identified\.

** **Open Files when Navigating Results with \(Up and Down\)** **  
If selected, as the up and down arrow keys are pressed in the **Search Results** tab within the list of results, opens each matching file\.

### Meta Data<a name="settings-user-change-meta-data"></a>

** **Maximum of Undo Stack Items in Meta Data** **  
The maximum number of items that AWS Cloud9 keeps in its list of action that can be undone\.

### Watchers<a name="settings-user-change-watchers"></a>

** **Auto\-Merge Files When a Conflict Occurs** **  
If enabled, AWS Cloud9 attempts to automatically merge files whenever a merge conflict happens\.

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
If enabled, AWS Cloud9 attempts to smooth the display of text in **Terminal** tabs\.

** **Blinking Cursor** **  
If enabled, AWS Cloud9 continuously blinks the cursor in **Terminal** tabs\.

** **Scrollback** **  
The number of lines that you can scroll up or back through in **Terminal** tabs\.

** **Use AWS Cloud9 as the Default Editor** **  
If selected, uses AWS Cloud9 as the default text editor\.

### Output<a name="settings-user-change-output"></a>

** **Text Color** **  
The color of text in tabs that display output\.

** **Background Color** **  
The background color of text in tabs that display output\.

** **Selection Color** **  
The color of selected text in tabs that display output\.

** **Warn Before Closing Unnamed Configuration** **  
If enabled, AWS Cloud9 prompts you to save any unsaved configuration tab before it is closed\.

** **Preserve log between runs** **  
If enabled, AWS Cloud9 keeps a log of all attempted runs\.

### Code Editor \(Ace\)<a name="settings-user-change-code-editor-ace"></a>

** **Auto\-pair Brackets, Quotes, etc\.** **  
If enabled, AWS Cloud9 attempts to add a matching closing character for each related starting character that is typed in editor tabs, such as for brackets, quotation marks, and braces\.

** **Wrap Selection with Brackets, Quote, etc\.** **  
If enabled, AWS Cloud9 attempts to insert a matching closing character at the end of text in editor tabs after the text is selected and a related started character is typed, such as for brackets, quotation marks, and braces\.

** **Code Folding** **  
If enabled, AWS Cloud9 attempts to show, expand, hide, or collapse sections of code in editor tabs according to related code syntax rules\.

** **Fade Fold Widgets** **  
If enabled, AWS Cloud9 displays code folding controls in the gutter whenever you pause the mouse over those controls in editor tabs\.

** **Full Line Selection** **  
If enabled, AWS Cloud9 selects an entire line that is triple\-clicked in editor tabs\.

** **Highlight Active Line** **  
If enabled, AWS Cloud9 highlights the entire active line in editor tabs\.

** **Highlight Gutter Line** **  
If enabled, AWS Cloud9 highlights the location in the gutter next to the active line in editor tabs\.

** **Show Invisible Characters** **  
If enabled, AWS Cloud9 displays what it considers to be invisible characters in editor tabs, for example carriage returns and line feeds, spaces, and tabs\.

** **Show Gutter** **  
If enabled, AWS Cloud9 displays the gutter\.

** **Show Line Numbers** **  
The behavior for displaying line numbers in the gutter\.  
Valid values include:  
+  **Normal** to display line numbers\.
+  **Relative** to display line numbers relative to the active line\.
+  **None** to hide line numbers\.

** **Show Indent Guides** **  
If enabled, AWS Cloud9 displays guides to more easily visualize indented text in editor tabs\.

** **Highlight Selected Word** **  
If enabled, AWS Cloud9 selects an entire word that is double\-clicked in an editor tab\.

** **Scroll Past the End of the Document** **  
The behavior for allowing the user to scroll past the end of the current file in editor tabs\.  
Valid values include:  
+  **Off** to not allow any scrolling past the end of the current file\.
+  **Half Editor Height** to allow scrolling past the end of the current file to up to half the editor's screen height\.
+  **Full Editor Height** to allow scrolling past the end of the current file to up to the editor's full screen height\.

** **Animate Scrolling** **  
If enabled, AWS Cloud9 applies animation behaviors during scrolling actions in editor tabs\.

** **Font Family** **  
The style of font to use in editor tabs\.

** **Font Size** **  
The size of the font to use in editor tabs\.

** **Antialiased Fonts** **  
If enabled, AWS Cloud9 attempts to smooth the display of text in editor tabs\.

** **Show Print Margin** **  
Displays a vertical line in editor tabs after the specified character location\.

** **Mouse Scroll Speed** **  
The relative speed of mouse scrolling in editor tabs\. Larger values result in faster scrolling\.

** **Cursor Style** **  
The style and behavior of the cursor in editor tabs\.  
Valid values include:  
+  **Ace** to display the cursor as a vertical bar that is relatively wider than **Slim**\.
+  **Slim** to display the cursor as a relatively slim vertical bar\.
+  **Smooth** to display the cursor as a vertical bar that is relatively wider than **Slim** and that blinks more smoothly than **Slim**\.
+  **Smooth and Slim** to display the cursor as a relatively slim vertical bar that blinks more smoothly than **Slim**\.
+  **Wide** to display the cursor as a relatively wide vertical bar\.

 **Merge Undo Deltas** 
+  **Always** to allow merge conflicts to be reverted\.
+  **Never** to never allow merge conflicts to be reverted\.
+  **Timed** to allow merge conflicts to be reverted after a specified time period\.

** **Enable Wrapping For New Documents** **  
If enabled, AWS Cloud9 wraps code in new files\.

### Input<a name="settings-user-change-input"></a>

** **Complete As You Type** **  
If enabled, AWS Cloud9 attempts to display possible text completions as you type\.

** **Complete On Enter** **  
If enabled, AWS Cloud9 attempts to display possible text completions after you press `Enter`\.

** **Highlight Variable Under Cursor** **  
If enabled, AWS Cloud9 highlights all references in code to the selected variable\.

** **Use Cmd\-Click for Jump to Definition** **  
If enabled, AWS Cloud9 goes to any original definition for code that is clicked while pressing and holding `Command` for Mac or `Ctrl` for Windows\.

### Hints & Warnings<a name="settings-user-change-hints-and-warnings"></a>

** **Enable Hints and Warnings** **  
If enabled, AWS Cloud9 displays applicable hint and warning messages\.

** **Ignore Messages Matching Regex** **  
AWS Cloud9 does not display any messages matching the specified regular expression\. For more information, see [Writing a regular expression pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions#Writing_a_regular_expression_pattern) in the *JavaScript Regular Expressions* topic on the Mozilla Developer Network\.

### Run & Debug<a name="settings-user-change-run-and-debug"></a>

** **Save All Unsaved Tabs Before Running** **  
If enabled, before running the associated code, AWS Cloud9 attempts to save all unsaved files with open tabs\.

### Preview<a name="settings-user-change-preview"></a>

** **Preview Running Apps** **  
If enabled, AWS Cloud9 attempts to display a preview of the output for the code in the active tab whenever the **Preview** button is chosen\.

** **Default Previewer** **  
The format AWS Cloud9 uses to preview code output\.  
Valid values include:  
+  **Raw** to attempt to display code output in a plain format\.
+  **Browser** to attempt to display code output in a format that is preferred for web browsers\.

** **When Saving Reload Previewer** **  
The behavior AWS Cloud9 uses for previewing code output whenever a code file is saved\.  
Valid values include:  
+  **Only on Ctrl\-Enter** to attempt to preview code output whenever `Ctrl-Enter` is pressed for the current code tab\.
+  **Always** to attempt to preview code output whenever a code file is saved\.

### Build<a name="settings-user-change-build"></a>

** **Automatically Build Supported Files** **  
If enabled, AWS Cloud9 attempts to automatically build the current code if a build action is triggered and the code is in a supported format\.