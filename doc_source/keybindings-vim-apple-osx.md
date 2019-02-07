# MacOS Vim Keybindings Reference for the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="keybindings-vim-apple-osx"></a>

Following is a list of Vim keyboard mode keybindings for MacOS operating systems in the AWS Cloud9 IDE\.

For more information, in the AWS Cloud9 IDE:

1. On the menu bar, choose **AWS Cloud9**, **Preferences**\.

1. On the **Preferences** tab, choose **Keybindings**\.

1. For **Keyboard Mode**, choose **Vim**\.

1. For **Operating System**, choose **MacOS**\.

See also [Working with Keybindings](settings-keybindings.md)\.
+  [General](#keybindings-vim-apple-osx-general) 
+  [Tabs](#keybindings-vim-apple-osx-tabs) 
+  [Panels](#keybindings-vim-apple-osx-panels) 
+  [Code Editor](#keybindings-vim-apple-osx-code-editor) 
+  [emmet](#keybindings-vim-apple-osx-emmet) 
+  [Terminal](#keybindings-vim-apple-osx-terminal) 
+  [Run and Debug](#keybindings-vim-apple-osx-run-debug) 

## General<a name="keybindings-vim-apple-osx-general"></a>


****  

| Description | Keybinding | Command | 
| --- | --- | --- | 
|  Add the selection as a watch expression  |   `Command-Shift-C`   |   `addwatchfromselection`   | 
|  Remove the cut selection from the clipboard  |   `Esc`   |   `clearcut`   | 
|  Show the code completion context menu  |   `Control-Space` \| `Option-Space`   |   `complete`   | 
|  Code complete, and then overwrite  |   `Control-Shift-Space` \| `Option-Shift-Space`   |   `completeoverwrite`   | 
|  Copy the selection to the clipboard  |   `Command-C`   |   `copy`   | 
|  Cut the selection to the clipboard  |   `Command-X`   |   `cut`   | 
|  Expand code, where applicable  |   `Tab`   |   `expandSnippet`   | 
|  Show the find and replace bar for the current document  |   `Command-F`   |   `find`   | 
|  Select all find matches in the current document  |   `Control-Option-G`   |   `findAll`   | 
|  Go to the next match in the current document for the find query you entered last  |   `Command-G`   |   `findnext`   | 
|  Go to the previous match in the current document for the find query you entered last  |   `Command-Shift-G`   |   `findprevious`   | 
|  Display all known references to the symbol at the insertion point in the active file in the editor  |   `Shift-F3`   |   `findReferences`   | 
|  Open the **Environment** window, and then make the list of files active  |   `Shift-Esc`   |   `focusTree`   | 
|  Reformat the selected JavaScript code  |   `Command-Shift-B`   |   `formatcode`   | 
|  Show the *go to line* box  |   `Command-L`   |   `gotoline`   | 
|  Hide the find and replace bar, if it is showing  |   `Esc`   |   `hidesearchreplace`   | 
|  Go to the definition of the variable or function at the cursor  |   `F3`   |   `jumptodef`   | 
|  If a local Lambda function is selected in the **Lambda** section of the **AWS Resources** window, attempts to upload the function to Lambda as a remote function  |   `Command-Shift-U`   |   `lambdaUploadFunction`   | 
|  Create a new file  |   `Control-N`   |   `newfile`   | 
|  Show the **Preferences** tab  |   `Command-,`   |   `openpreferences`   | 
|  Open a **Terminal** tab, and then switch to the parent folder of the selected file in the list of files  |   `Command-Option-L`   |   `opentermhere`   | 
|  Paste the clipboard's current contents at the cursor  |   `Command-V`   |   `paste`   | 
|  Show suggestions for fixing errors  |   `Command-F3`   |   `quickfix`   | 
|  Redo the last action  |   `Command-Shift-Z` \| `Command-Y`   |   `redo`   | 
|  Refresh the preview pane  |   `Command-Enter`   |   `reloadpreview`   | 
|  Start a rename refactor for the selection  |   `Option-Command-R`   |   `renameVar`   | 
|  Show the find and replace bar for the current document, with focus on the *replace with* expression  |   `Option-Command-F`   |   `replace`   | 
|  Rerun your initialization script  |   `Command-Enter`   |   `rerunInitScript`   | 
|  Restart the environment  |   `Command-R`   |   `restartc9`   | 
|  Reset the current file to its last saved version  |   `Control-Shift-Q`   |   `reverttosaved`   | 
|  Reset each open file to its saved version  |   `Option-Shift-Q`   |   `reverttosavedall`   | 
|  Save the current file to disk  |   `Command-S`   |   `save`   | 
|  Save the current file to disk with a different file name  |   `Command-Shift-S`   |   `saveas`   | 
|  Show the find and replace bar for multiple files  |   `Shift-Command-F`   |   `searchinfiles`   | 
|  Show the **Process List** dialog box  |   `Command-Option-P`   |   `showprocesslist`   | 
|  Undo the last action  |   `Command-Z`   |   `undo`   | 

## Tabs<a name="keybindings-vim-apple-osx-tabs"></a>


****  

| Description | Keybinding | Command | 
| --- | --- | --- | 
|  Close all open tabs in the current pane, except the current tab  |   `Option-Control-W`   |   `closeallbutme`   | 
|  Close all open tabs in all panes  |   `Option-Shift-W`   |   `closealltabs`   | 
|  Close the current pane  |   `Command-Control-W`   |   `closepane`   | 
|  Close the current tab  |   `Option-W`   |   `closetab`   | 
|  Go one pane down  |   `Control-Command-Down`   |   `gotopanedown`   | 
|  Go one pane left  |   `Control-Command-Left`   |   `gotopaneleft`   | 
|  Go one pane right  |   `Control-Command-Right`   |   `gotopaneright`   | 
|  Go one pane up  |   `Control-Command-Up`   |   `gottopaneup`   | 
|  Go one tab left  |   `Command-[`   |   `gototableft`   | 
|  Go one tab right  |   `Command-]`   |   `gototabright`   | 
|  Move the current tab down one pane, or if the tab is already at the very bottom, create a split tab there  |   `Command-Option-Shift-Down`   |   `movetabdown`   | 
|  Move the current tab left, or if the tab is already at the far left, create a split tab there  |   `Command-Option-Shift-Left`   |   `movetableft`   | 
|  Move the current tab right, or if the tab is already at the far right, create a split tab there  |   `Command-Option-Shift-Right`   |   `movetabright`   | 
|  Move the current tab up one pane, or if the tab is already at the very top, create a split tab there  |   `Command-Option-Shift-Up`   |   `movetabup`   | 
|  Go to the next pane  |   `Option-Esc`   |   `nextpane`   | 
|  Go to the next tab  |   `Option-Tab`   |   `nexttab`   | 
|  Go to the previous pane  |   `Option-Shift-Esc`   |   `previouspane`   | 
|  Go to the previous tab  |   `Option-Shift-Tab`   |   `previoustab`   | 
|  Go back to the last tab  |   `Esc`   |   `refocusTab`   | 
|  Open the last tab again  |   `Option-Shift-T`   |   `reopenLastTab`   | 
|  Show the current tab in the file tree  |   `Command-Shift-L`   |   `revealtab`   | 
|  Go to the tenth tab  |   `Command-0`   |   `tab0`   | 
|  Go to the first tab  |   `Command-1`   |   `tab1`   | 
|  Go to the second tab  |   `Command-2`   |   `tab2`   | 
|  Go to the third tab  |   `Command-3`   |   `tab3`   | 
|  Go to the fourth tab  |   `Command-4`   |   `tab4`   | 
|  Go to the fifth tab  |   `Command-5`   |   `tab5`   | 
|  Go to the sixth tab  |   `Command-6`   |   `tab6`   | 
|  Go to the seventh tab  |   `Command-7`   |   `tab7`   | 
|  Go to the eighth tab  |   `Command-8`   |   `tab8`   | 
|  Go to the ninth tab  |   `Command`   |   `tab9`   | 

## Panels<a name="keybindings-vim-apple-osx-panels"></a>


****  

| Description | Keybinding | Command | 
| --- | --- | --- | 
|  Show the **Go** window in **Go to Anything** mode  |   `Command-E\|Command-P`   |   `gotoanything`   | 
|  Show the **Go** window in **Go to Command** mode  |   `Command-.`   |   `gotocommand`   | 
|  Show the **Go** window in **Go to File** mode\.  |   `Command-O`   |   `gotofile`   | 
|  Show the **Go** window in **Go to Symbol** mode\.  |   `Command-Shift-O`   |   `gotosymbol`   | 
|  Show the **Outline** window  |   `Command-Shift-E`   |   `outline`   | 
|  Show the **Console** window if hidden, or hide if shown  |   `Control-Esc`   |   `toggleconsole`   | 
|  Show the **Environment** window if hidden, or hide if shown  |   `Command-U`   |   `toggletree`   | 

## Code Editor<a name="keybindings-vim-apple-osx-code-editor"></a>


****  

| Description | Keybinding | Command | 
| --- | --- | --- | 
|  Add a cursor one line above the active cursor, or if a cursor is already added, add another cursor above that one  |   `Control-Option-Up`   |   `addCursorAbove`   | 
|  Add a second cursor one line above the active cursor, or if a second cursor is already added, move the second cursor up one line  |   `Control-Option-Shift-Up`   |   `addCursorAboveSkipCurrent`   | 
|  Add a cursor one line below the active cursor, or if a cursor is already added, add another cursor below that one  |   `Control-Option-Down`   |   `addCursorBelow`   | 
|  Add a second cursor one line below the active cursor, or if a second cursor is already added, move the second cursor down one line  |   `Control-Option-Shift-Down`   |   `addCursorBelowSkipCurrent`   | 
|  Move all cursors to the same space as the active cursor on each of their lines, if they are misaligned  |   `Control-Option-A`   |   `alignCursors`   | 
|  Backspace one space  |   `Control-Backspace \| Shift-Backspace \| Backspace`   |   `backspace`   | 
|  Indent selection one tab  |   `Control-]`   |   `blockindent`   | 
|  Outdent selection one tab  |   `Control-[`   |   `blockoutdent`   | 
|  Control whether focus can be switched from the editor to somewhere else in the IDE  |   `Command-Z \| Command-Shift-Z \| Command-Y`   |   `cancelBrowserUndoInAce`   | 
|  Center the selection  |   `Control-L`   |   `centerselection`   | 
|  Copy the contents of the line, and paste the copied contents one line down  |   `Command-Option-Down`   |   `copylinesdown`   | 
|  Copy the contents of the line, and paste the copied contents one line up  |   `Command-Option-Up`   |   `copylinesup`   | 
|  Delete one space  |   `Delete \| Control-Delete \| Shift-Delete`   |   `del`   | 
|  Copy the contents of the selection, and paste the copied contents immediately after the selection  |   `Command-Shift-D`   |   `duplicateSelection`   | 
|  Include the current line's contents in the selection  |   `Command-Shift-L`   |   `expandtoline`   | 
|  Include up to the next matching symbol in selection  |   `Control-Shift-M`   |   `expandToMatching`   | 
|  Fold the selected code, or if a folded unit is selected, unfold it  |   `Command-Option-L \| Command-F1`   |   `fold`   | 
|  Fold all possibly foldable elements  |   `Control-Command-Option-0`   |   `foldall`   | 
|  Fold all possibly foldable elements, except for the current selection scope  |   `Command-Option-0`   |   `foldOther`   | 
|  Go down one line  |   `Down \| Control-N`   |   `golinedown`   | 
|  Go up one line  |   `Up \| Control-P`   |   `golineup`   | 
|  Go to the end of the file  |   `Command-End \| Command-Down`   |   `gotoend`   | 
|  Go left one space  |   `Left \| Control-B`   |   `gotoleft`   | 
|  Go to the end of the current line  |   `Command-Right \| End \| Control-E`   |   `gotolineend`   | 
|  Go to the start of the current line  |   `Command-Left \| Home \| Control-A`   |   `gotolinestart`   | 
|  Go to the next error  |   `F4`   |   `goToNextError`   | 
|  Go down one page  |   `Page Down \| Control-V`   |   `gotopagedown`   | 
|  Go up one page  |   `Page Up`   |   `gotopageup`   | 
|  Go to the previous error  |   `Shift-F4`   |   `goToPreviousError`   | 
|  Go right one space  |   `Right \| Control-F`   |   `gotoright`   | 
|  Go to the start of the file  |   `Command-Home \| Command-Up`   |   `gotostart`   | 
|  Go one word to the left  |   `Option-Left`   |   `gotowordleft`   | 
|  Go one word to the right  |   `Option-Right`   |   `gotowordright`   | 
|  Indent the selection one tab  |   `Tab`   |   `indent`   | 
|  Go to the matching symbol in the current scope  |   `Control-P`   |   `jumptomatching`   | 
|  Increase the font size  |   `Command-+ \| Command-=`   |   `largerfont`   | 
|  Decrease the number to the left of the cursor by 1, if it is a number  |   `Option-Shift-Down`   |   `modifyNumberDown`   | 
|  Increase the number to the left of the cursor by 1, if it is a number  |   `Option-Shift-Up`   |   `modifyNumberUp`   | 
|  Move selection down one line  |   `Option-Down`   |   `movelinesdown`   | 
|  Move selection up one line  |   `Option-Up`   |   `movelinesup`   | 
|  Outdent selection one tab  |   `Shift-Tab`   |   `outdent`   | 
|  Turn on overwrite mode, or turn off if on  |   `Insert`   |   `overwrite`   | 
|  Go down one page  |   `Option-Page Down`   |   `pagedown`   | 
|  Go up one page  |   `Option-Page Up`   |   `pageup`   | 
|  Remove the current line  |   `Command-D`   |   `removeline`   | 
|  Delete from the cursor to the end of the current line  |   `Control-K`   |   `removetolineend`   | 
|  Delete from the beginning of the current line up to the cursor  |   `Command-Backspace`   |   `removetolinestart`   | 
|  Delete the word to the left of the cursor  |   `Option-Backspace \| Control-Option-Backspace`   |   `removewordleft`   | 
|  Delete the word to the right of the cursor  |   `Option-Delete`   |   `removewordright`   | 
|  Replay previously recorded keystrokes  |   `Command-Shift-E`   |   `replaymacro`   | 
|  Select all selectable content  |   `Command-A`   |   `selectall`   | 
|  Include the next line down in the selection  |   `Shift-Down \| Control-Shift-N`   |   `selectdown`   | 
|  Include the next space to the left in the selection  |   `Shift-Left \| Control-Shift-B`   |   `selectleft`   | 
|  Include the rest of the current line in the selection, starting from the cursor  |   `Shift-End`   |   `selectlineend`   | 
|  Include the beginning of the current line in the selection, up to the cursor  |   `Shift-Home`   |   `selectlinestart`   | 
|  Include more matching selections that are after the selection  |   `Control-Option-Right`   |   `selectMoreAfter`   | 
|  Include more matching selections that are before the selection  |   `Control-Option-Left`   |   `selectMoreBefore`   | 
|  Include the next matching selection that is after the selection  |   `Control-Option-Shift-Right`   |   `selectNextAfter`   | 
|  Include the next matching selection that is before the selection  |   `Control-Option-Shift-Left`   |   `selectNextBefore`   | 
|  Select or find the next matching selection  |   `Control-G`   |   `selectOrFindNext`   | 
|  Select or find the previous matching selection  |   `Control-Shift-G`   |   `selectOrFindPrevious`   | 
|  Include from the cursor down to the end of the current page in the selection  |   `Shift-Page Down`   |   `selectpagedown`   | 
|  Include from the cursor up to the beginning of the current page in the selection  |   `Shift-Page Up`   |   `selectpageup`   | 
|  Include the next space to the right of the cursor in the selection  |   `Shift-Right`   |   `selectright`   | 
|  Include from the cursor down to the end of the current file in the selection  |   `Command-Shift-End \| Command-Shift-Down`   |   `selecttoend`   | 
|  Include from the cursor to the end of the current line in the selection  |   `Command-Shift-Right \| Shift-End \| Control-Shift-E`   |   `selecttolineend`   | 
|  Include from the beginning of the current line to the cursor in the selection  |   `Command-Shift-Left \| Control-Shift-A`   |   `selecttolinestart`   | 
|  Include from the cursor to the next matching symbol in the current scope  |   `Control-Shift-P`   |   `selecttomatching`   | 
|  Include from the cursor up to the beginning of the current file in the selection  |   `Command-Shift-Home \| Command-Shift-Up`   |   `selecttostart`   | 
|  Include the next line up in the selection  |   `Shift-Up \| Control-Shift-P`   |   `selectup`   | 
|  Include the next word to the left of the cursor in the selection  |   `Option-Shift-Left`   |   `selectwordleft`   | 
|  Include the next word to the right of the cursor in the selection  |   `Option-Shift-Right`   |   `selectwordright`   | 
|  Show the **Preferences** tab  |   `Command-,`   |   `showSettingsMenu`   | 
|  Clear all previous selections  |   `Esc`   |   `singleSelection`   | 
|  Decrease the font size  |   `Command--`   |   `smallerfont`   | 
|  If multiple lines are selected, rearrange them into a sorted order  |   `Command-Option-S`   |   `sortlines`   | 
|  Add a cursor at the end of the current line  |   `Control-Option-L`   |   `splitIntoLines`   | 
|  Move the contents of the cursor to the end of the line, to its own line  |   `Control-O`   |   `splitline`   | 
|  Surround the selection with block comment characters, or remove them if they are there  |   `Command-Shift-/`   |   `toggleBlockComment`   | 
|  Add line comment characters at the start of each selected line, or remove them if they are there  |   `Command-/`   |   `togglecomment`   | 
|  Fold code, or remove code folding if it is there  |   `F2`   |   `toggleFoldWidget`   | 
|  Fold parent code, or remove folding if it is there  |   `Option-F2`   |   `toggleParentFoldWidget`   | 
|  Start keystroke recording, or stop if it is already recording  |   `Command-Option-E`   |   `togglerecording`   | 
|  Wrap words, or stop wrapping words if they are already wrapping  |   `Control-W`   |   `toggleWordWrap`   | 
|  Change the selection to all lowercase  |   `Control-Shift-U`   |   `tolowercase`   | 
|  Change the selection to all uppercase  |   `Control-U`   |   `touppercase`   | 
|  Transpose the selection  |   `Control-T`   |   `transposeletters`   | 
|  Unfold the selected code  |   `Command-Option-Shift-L \| Command-Shift-F1`   |   `unfold`   | 
|  Unfold code folding for the entire file  |   `Command-Option-Shift-0`   |   `unfoldall`   | 

## emmet<a name="keybindings-vim-apple-osx-emmet"></a>


****  

| Description | Keybinding | Command | 
| --- | --- | --- | 
|  Evaluate a simple math expression \(such as `2*4` or `10/2`\), and output its result  |   `Shift-Command-Y`   |   `emmet_evaluate_math_expression`   | 
|  Expand CSS\-like abbreviations into HTML, XML, or CSS code, depending on the current file's syntax  |   `Control-Option-E`   |   `emmet_expand_abbreviation`   | 
|  Traverse expanded CSS\-like abbreviations, by tab stop  |   `Tab`   |   `emmet_expand_abbreviation_with_tab`   | 
|  Go to the next editable code part  |   `Shift-Command-.`   |   `emmet_select_next_item`   | 
|  Go to the previous editable code part  |   `Shift-Command-,`   |   `emmet_select_previous_item`   | 
|  Expand an abbreviation, and then place the current selection within the last element of the generated snippet  |   `Shift-Control-A`   |   `emmet_wrap_with_abbreviation`   | 

## Terminal<a name="keybindings-vim-apple-osx-terminal"></a>


****  

| Description | Keybinding | Command | 
| --- | --- | --- | 
|  Open a new **Terminal** tab  |   `Option-T`   |   `openterminal`   | 
|  Switch between the editor and the **Terminal** tab  |   `Option-S`   |   `switchterminal`   | 

## Run and Debug<a name="keybindings-vim-apple-osx-run-debug"></a>


****  

| Description | Keybinding | Command | 
| --- | --- | --- | 
|  Build the current file  |   `Command-B`   |   `build`   | 
|  Resume the current paused process  |   `F8 \| Command-\`   |   `resume`   | 
|  Run or debug the current application  |   `Option-F5`   |   `run`   | 
|  Run or debug the last run file  |   `F5`   |   `runlast`   | 
|  Step into the function that is next on the stack  |   `F11 \| Command-;`   |   `stepinto`   | 
|  Step out of the current function scope  |   `Shift-F11 \| Command-Shift-'`   |   `stepout`   | 
|  Step over the current expression on the stack  |   `F10 \| Command-'`   |   `stepover`   | 
|  Stop running or debugging the current application  |   `Shift-F5`   |   `stop`   | 
|  Stop building the current file  |   `Control-Shift-C`   |   `stopbuild`   | 