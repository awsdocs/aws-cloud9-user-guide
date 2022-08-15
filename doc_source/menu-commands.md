# Menu bar commands reference for the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="menu-commands"></a>

The following lists describe the default menu bar commands in the AWS Cloud9 IDE\. If the menu bar isn't visible, choose the thin bar along the top edge of the IDE to show it\.
+  [AWS Cloud9 menu](#menu-commands-cloud9) 
+  [File menu](#menu-commands-file) 
+  [Edit menu](#menu-commands-edit) 
+  [Find menu](#menu-commands-find) 
+  [View menu](#menu-commands-view) 
+  [Go menu](#menu-commands-goto) 
+  [Run menu](#menu-commands-run) 
+  [Tools menu](#menu-commands-tools) 
+  [Window menu](#menu-commands-window) 
+  [Support menu](#menu-commands-support) 
+  [Preview menu](#menu-commands-preview) 
+  [Other menu bar commands](#menu-commands-other) 

## AWS Cloud9 menu<a name="menu-commands-cloud9"></a>


****  

| Command | Description | 
| --- | --- | 
|   **Preferences**   |  Do one of the following: [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/menu-commands.html) See [Working with Project Settings](settings-project.md), [Working with User Settings](settings-user.md), [Working with Keybindings](settings-keybindings.md), [Working with Themes](settings-theme.md), and [Working with Initialization Scripts](settings-init-script.md)\.  | 
|   **Go To Your Dashboard**   |  Open the AWS Cloud9 console in a separate web browser tab\. See [Creating an Environment](create-environment.md), [Opening an Environment](open-environment.md), [Changing Environment Settings](change-environment.md), and [Deleting an Environment](delete-environment.md)\.  | 
|   **Welcome Page**   |  Open the **Welcome** tab\.  | 
|   **Open Your Project Settings**   |  Open the `project.settings` file for the current environment\. See [Working with Project Settings](settings-project.md)\.  | 
|   **Open Your User Settings**   |  Open the `user.settings` file for the current user\. See [Working with User Settings](settings-user.md)\.  | 
|   **Open Your Keymap**   |  Open the `keybindings.settings` file for the current user\. See [Working with Keybindings](settings-keybindings.md)\.  | 
|   **Open Your Init Script**   |  Open the `init.js` file for the current user\. See [Working with Initialization Scripts](settings-init-script.md)\.  | 
|   **Open Your Stylesheet**   |  Open the `styles.css` file for the current user\. See [Working with Themes](settings-theme.md)\.  | 

## File menu<a name="menu-commands-file"></a>


****  

| Command | Description | 
| --- | --- | 
|   **New File**   |  Create a new file\.  | 
|   **New From Template**   |  Create a new file, based on the chosen file template\.  | 
|   **Open**   |  Show and go to the **Navigate** window\.  | 
|   **Open Recent**   |  Open the chosen file\.  | 
|   **Save**   |  Save the current file\.  | 
|   **Save As**   |  Save the current file with a different file name, location, or both\.  | 
|   **Save All**   |  Save all unsaved files\.  | 
|   **Revert to Saved**   |  Discard changes for current file since it was last saved\.  | 
|   **Revert All to Saved**   |  Discard changes for all unsaved files since they were last saved\.  | 
|   **Show File Revision History**   |  View and manage changes to the current file in the editor\. See [Working with File Revisions](file-revisions.md)\.  | 
|   **Upload Local Files**   |  Show the **Upload Files** dialog box, which enables you to drag files from your local computer into the environment\.  | 
|   **Download Project**   |  Combine the files in the environment into a \.zip file, which you can download to your local computer\.  | 
|   **Line Endings**   |  Use **Windows** \(carriage return plus line feed\) or **Unix** \(line feed only\) line endings\.  | 
|   **Close File**   |  Close the current file\.  | 
|   **Close All Files**   |  Close all open files\.  | 

## Edit menu<a name="menu-commands-edit"></a>


****  

| Command | Description | 
| --- | --- | 
|   **Undo**   |  Undo the last action\.  | 
|   **Redo**   |  Redo the last undone action\.  | 
|   **Cut**   |  Move the selection to the clipboard\.  | 
|   **Copy**   |  Copy the selection to the clipboard\.  | 
|   **Paste**   |  Copy the clipboard's contents to the selection point\.  | 
|   **Keyboard Mode**   |  The set of keybindings to use, such as `Default`, `Vim`, `Emacs`, or `Sublime`\. See [Working with Keybindings](settings-keybindings.md)\.  | 
|   **Selection, Select All**   |  Select all selectable content\.  | 
|   **Selection, Split Into Lines**   |  Add a cursor at the end of the current line\.  | 
|   **Selection, Single Selection**   |  Clear all previous selections\.  | 
|   **Selection, Multiple Selections, Add Cursor Up**   |  Add a cursor one line above the active cursor\. If a cursor is already added, add another cursor above that one\.  | 
|   **Selection, Multiple Selections, Add Cursor Down**   |  Add a cursor one line below the active cursor\. If a cursor is already added, add another cursor below that one\.  | 
|   **Selection, Multiple Selections, Move Active Cursor Up**   |  Add a second cursor one line above the active cursor\. If a second cursor is already added, move the second cursor up one line\.  | 
|   **Selection, Multiple Selections, Move Active Cursor Down**   |  Add a second cursor one line below the active cursor\. If a second cursor is already added, move the second cursor down one line\.  | 
|   **Selection, Multiple Selections, Add Next Selection Match**   |  Include more matching selections that are after the selection\.  | 
|   **Selection, Multiple Selections, Add Previous Selection Match**   |  Include more matching selections that are before the selection\.  | 
|   **Selection, Multiple Selections, Merge Selection Range**   |  Add a cursor at the end of the current line\.  | 
|   **Selection, Select Word Right**   |  Include the next word to the right of the cursor in the selection\.  | 
|   **Selection, Select Word Left**   |  Include the next word to the left of the cursor in the selection\.  | 
|   **Selection, Select to Line End**   |  Include from the cursor to the end of the current line in the selection  | 
|   **Selection, Select to Line Start**   |  Include from the beginning of the current line to the cursor in the selection\.  | 
|   **Selection, Select to Document End**   |  Include from the cursor down to the end of the current file in the selection\.  | 
|   **Selection, Select to Document Start**   |  Include from the cursor up to the beginning of the current file in the selection\.  | 
|   **Line, Indent**   |  Indent the selection one tab\.  | 
|   **Line, Outdent**   |  Outdent the selection one tab\.  | 
|   **Line, Move Line Up**   |  Move the selection up one line\.  | 
|   **Line, Move Line Down**   |  Move the selection down one line\.  | 
|   **Line, Copy Lines Up**   |  Copy the contents of the line, and paste the copied contents one line up\.  | 
|   **Line, Copy Lines Down**   |  Copy the contents of the line, and paste the copied contents one line down\.  | 
|   **Line, Remove Line**   |  Delete the contents of the current line\.  | 
|   **Line, Remove to Line End**   |  Delete from the cursor to the end of the current line\.  | 
|   **Line, Remove to Line Start**   |  Delete from the beginning of the current line up to the cursor\.  | 
|   **Line, Split Line**   |  Move the contents of the cursor to the end of the line, to its own line\.  | 
|   **Text, Remove Word Right**   |  Delete the word to the right of the cursor\.  | 
|   **Text, Remove Word Left**   |  Delete the word to the left of the cursor\.  | 
|   **Text, Align**   |  Move all cursors to the same space as the active cursor on each of their lines, if they are misaligned\.  | 
|   **Text, Transpose Letters**   |  Transpose the selection\.  | 
|   **Text, To Upper Case**   |  Change the selection to all uppercase\.  | 
|   **Text, To Lower Case**   |  Change the selection to all lowercase\.  | 
|   **Comment, Toggle Comment**   |  Add line comment characters at the start of each selected line, or remove them if they are there\.  | 
|   **Code Folding, Toggle Fold**   |  Fold code, or remove code folding if it is there\.  | 
|   **Code Folding, Unfold**   |  Unfold the selected code\.  | 
|   **Code Folding, Fold Other**   |  Fold all possibly foldable elements, except for the current selection scope\.  | 
|   **Code Folding, Fold All**   |  Fold all possibly foldable elements\.  | 
|   **Code Folding, Unfold All**   |  Unfold code folding for the entire file\.  | 
|   **Code Formatting, Apply Code Formatting**   |  Reformat the selected JavaScript code\.  | 
|   **Code Formatting, Open Language & Formatting Preferences**   |  Open the **Project Settings** section of the **Preferences** tab to programming language settings\.  | 

## Find menu<a name="menu-commands-find"></a>

For more information, see [Finding and Replacing Text](find-replace-text.md)\.


****  

| Command | Description | 
| --- | --- | 
|   **Find**   |  Show the find and replace bar for the current document, with focus on the **Find** expression\.  | 
|   **Find Next**   |  Go to the next match in the current document for the find query you entered last\.  | 
|   **Find Previous**   |  Go to the previous match in the current document for the find query you entered last\.  | 
|   **Replace**   |  Show the find and replace bar for the current document, with focus on the **Replace With** expression\.  | 
|   **Replace Next**   |  Replace the next match for **Find** with **Replace With** in the find and replace bar for the current document \.  | 
|   **Replace Previous**   |  Replace the previous match for **Find** with **Replace With** in the find and replace bar for the current document\.  | 
|   **Replace All**   |  Replace all matches for **Find** with **Replace With** in the find and replace bar for the current document\.  | 
|   **Find in Files**   |  Show the find and replace bar for multiple files\.  | 

## View menu<a name="menu-commands-view"></a>


****  

| Command | Description | 
| --- | --- | 
|   **Editors**   |  Show the chosen editor\.  | 
|   **Open Files**   |  Show the **Open Files** list in the **Environment** window, or hide if shown\.  | 
|   **Menu Bar**   |  Show the menu bar, or hide if shown\.  | 
|   **Tab Buttons**   |  Show tabs, or hide if shown\.  | 
|   **Gutter**   |  Show the gutter, or hide if shown\.  | 
|   **Status Bar**   |  Show the status bar, or hide if shown\.  | 
|   **Console**   |  Show the **Console** window, or hide if shown\.  | 
|   **Layout, Single**   |  Show a single pane\.  | 
|   **Layout, Vertical Split**   |  Show two panes, top and bottom\.  | 
|   **Layout, Horizontal Split**   |  Show two panes, side by side\.  | 
|   **Layout, Cross Split**   |  Show four panes of equal size\.  | 
|   **Layout, Split 1:2**   |  Show one pane on the left and two panes on the right\.  | 
|   **Layout, Split 2:1**   |  Show two panes on the left and one pane on the right\.  | 
|   **Font Size, Increase Font Size**   |  Increase the font size\.  | 
|   **Font Size, Decrease Font Size**   |  Decrease the font size\.  | 
|   **Syntax**   |  Show the syntax type for the current document\.  | 
|   **Themes**   |  Show the IDE theme type\.  | 
|   **Wrap Lines**   |  Wrap words to the edge of the current pane, or stop wrapping words if they are already wrapping\.  | 
|   **Wrap To Print Margin**   |  Wrap words to the edge of the current print margin, or stop wrapping words if they are already wrapping\.  | 

## Go menu<a name="menu-commands-goto"></a>


****  

| Command | Description | 
| --- | --- | 
|   **Go To Anything**   |  Show the **Go** window in **Go to Anything** mode\.  | 
|   **Go To Symbol**   |  Show the **Go** window in **Go to Symbol** mode\.  | 
|   **Go To File**   |  Show the **Go** window in **Go to File** mode\.  | 
|   **Go To Command**   |  Show the **Go** window in **Go to Command** mode\.  | 
|   **Go To Line**   |  Show the **Go** window in **Go to Line** mode\.  | 
|   **Next Error**   |  Go to the next error\.  | 
|   **Previous Error**   |  Go to the previous error\.  | 
|   **Word Right**   |  Go one word to the right\.  | 
|   **Word Left**   |  Go one word to the left\.  | 
|   **Line End**   |  Go to the end of the current line\.  | 
|   **Line Start**   |  Go to the start of the current line\.  | 
|   **Jump to Definition**   |  Go to the definition of the variable or function at the cursor\.  | 
|   **Jump to Matching Brace**   |  Go to the matching symbol in the current scope\.  | 
|   **Scroll to Selection**   |  Scroll the selection into better view\.  | 

## Run menu<a name="menu-commands-run"></a>


****  

| Command | Description | 
| --- | --- | 
|   **Run**   |  Run or debug the current application\.  | 
|   **Run Last**   |  Run or debug the last run file\.  | 
|   **Run With**   |  Run or debug using the chosen runner\. See [Working with Builders, Runners, and Debuggers](build-run-debug.md)\.  | 
|   **Run History**   |  View run history\.  | 
|   **Run Configurations**   |  Choose a run configuration to run or debug with, or create or manage run configurations\. See [Working with Builders, Runners, and Debuggers](build-run-debug.md)\.  | 
|   **Show Debugger at Break**   |  When running code reaches a breakpoint, show the **Debugger** window\.  | 
|   **Build**   |  Build the current file\.  | 
|   **Cancel Build**   |  Stop building the current file\.  | 
|   **Build System**   |  Build using the chosen build system\.  | 
|   **Show Build Result**   |  Show the related build result\.  | 
|   **Automatically Build Supported Files**   |  Automatically build supported files\.  | 
|   **Save All on Build**   |  When building, save all related unsaved files\.  | 

## Tools menu<a name="menu-commands-tools"></a>


****  

| Command | Description | 
| --- | --- | 
|   **Strip Trailing Space**   |  Trim whitespace at the ends of lines\.  | 
|   **Preview, Preview File**   |  Preview the current document in a preview tab\.  | 
|   **Preview, Preview Running Application**   |  Preview the current application in a separate web browser tab\.  | 
|   **Preview, Configure Preview URL**   |  Open the **Project Settings** section of the **Preferences** tab to the **Run & Debug, Preview URL** box\.  | 
|   **Preview, Show Active Servers**   |  Show a list of available active server addresses in the **Process List** dialog box\.  | 
|   **Process List**   |  Show the **Process List** dialog box\.  | 
|   **Show Autocomplete**   |  Show the code completion context menu\.  | 
|   **Rename Variable**   |  Start a rename refactor for the selection\.  | 
|   **Toggle Macro Recording**   |  Start keystroke recording, of stop if it is already recording\.  | 
|   **Play Macro**   |  Play previously recorded keystrokes\.  | 

## Window menu<a name="menu-commands-window"></a>


****  

| Command | Description | 
| --- | --- | 
|   **Go**   |  Show the **Go** window, or hide if shown\.  | 
|   **New Terminal**   |  Open a new **Terminal** tab\.  | 
|   **New Immediate Window**   |  Open a new **Immediate** tab\.  | 
|   **Share**   |  Show the **Share this environment** dialog box\.  | 
|   **Installer**   |  Show the **AWS Cloud9 Installer** dialog box\.  | 
|   **Collaborate**   |  Show the **Collaborate** window, or hide if shown\.  | 
|   **Outline**   |  Show the **Outline** window, or hide if shown\.  | 
|   **AWS Resources**   |  Show the **AWS Resources** window, or hide if shown\.  | 
|   **Environment**   |  Show the **Environment** window, or hide if shown\.  | 
|   **Debugger**   |  Show the **Debugger** window, or hide if shown\.  | 
|   **Navigation, Tab to the Right**   |  Go one tab right\.  | 
|   **Navigation, Tab to the Left**   |  Go one tab left\.  | 
|   **Navigation, Next Tab in History**   |  Go to the next tab\.  | 
|   **Navigation, Previous Tab in History**   |  Go to the previous tab\.  | 
|   **Navigation, Move Tab to Right**   |  Move the current tab right\. If the tab is already at the far right, create a split tab there\.  | 
|   **Navigation, Move Tab to Left**   |  Move the current tab left\. If the tab is already at the far left, create a split tab there\.  | 
|   **Navigation, Move Tab to Up**   |  Move the current tab up one pane\. If the tab is already at very top, create a split tab there\.  | 
|   **Navigation, Move Tab to Down**   |  Move the current tab down one pane\. If the tab is already at the very bottom, create a split tab there\.  | 
|   **Navigation, Go to Pane to Right**   |  Go one pane right\.  | 
|   **Navigation, Go to Pane to Left**   |  Go one pane left\.  | 
|   **Navigation, Go to Pane to Up**   |  Go one pane up\.  | 
|   **Navigation, Go to Pane to Down**   |  Go one pane down\.  | 
|   **Navigation, Switch Between Editor and Terminal**   |  Switch between the editor and the **Terminal** tab \.  | 
|   **Navigation, Next Pane in History**   |  Go to the next pane\.  | 
|   **Navigation, Previous Pane in History**   |  Go to the previous pane\.  | 
|   **Saved Layouts, Save**   |  Save the current layout\. To switch to this layout later, choose **Saved Layouts, LAYOUT\-ID**\.  | 
|   **Saved Layouts, Save and Close All**   |  Save the current layout, and then close all tabs and panes\.  | 
|   **Saved Layouts, Show Saved Layouts in File Tree**   |  Show all saved layouts in the **Environment** window\.  | 
|   **Tabs, Close Pane**   |  Close the current pane\.  | 
|   **Tabs, Close All Tabs In All Panes**   |  Close all open tabs in all panes\.  | 
|   **Tabs, Close All But Current Tab**   |  Close all open tabs in the current pane, except the current tab\.  | 
|   **Tabs, Split Pane in Two Rows**   |  Split the current pane into two panes, top and bottom\.  | 
|   **Tabs, Split Pane in Two Columns**   |  Split the current pane into two panes, left and right\.  | 
|   **Presets, Full IDE**   |  Switch to full IDE mode\.  | 
|   **Presets, Minimal Editor**   |  Switch to minimal editor mode\.  | 
|   **Presets, Sublime Mode**   |  Switch to Sublime mode\.  | 

## Support menu<a name="menu-commands-support"></a>


****  

| Command | Description | 
| --- | --- | 
|   **Welcome Page**   |  Open the **Welcome** tab\.  | 
|   **Get Help \(Community\)**   |  Opens the AWS Cloud9 online community website in a separate web browser tab\.  | 
|   **Read Documentation**   |  Opens the *AWS Cloud9 User Guide* in a separate web browser tab\.  | 

## Preview menu<a name="menu-commands-preview"></a>


****  

| Command | Description | 
| --- | --- | 
|   **Preview File**   |  Preview the current document in a preview tab\.  | 
|   **Preview Running Application**   |  Preview the current application in a separate web browser tab\.  | 
|   **Configure Preview URL**   |  Open the **Project Settings** section of the **Preferences** tab to the **Run & Debug, Preview URL** box\.  | 
|   **Show Active Servers**   |  Show a list of available active server addresses in the **Process List** dialog box\.  | 

## Other menu bar commands<a name="menu-commands-other"></a>


****  

| Command | Description | 
| --- | --- | 
|   **Run**   |  Run or debug the current application\.  | 
|   **Share**   |  Opens the **Share this environment** dialog box\.  | 
|   **Preferences** \(gear icon\)  |  Open the **Preferences** tab\.  | 