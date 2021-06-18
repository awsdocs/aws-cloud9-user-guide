# Windows / Linux Default Keybindings Reference for the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="keybindings-default-windows-linux"></a>

Following is a list of default keyboard mode keybindings for Windows / Linux operating systems in the AWS Cloud9 IDE\.

For more information, in the AWS Cloud9 IDE:

1. On the menu bar, **AWS Cloud9**, **Preferences**\.

1. On the **Preferences** tab, choose **Keybindings**\.

1. For **Keyboard Mode**, choose **Default**\.

1. For **Operating System**, choose **Windows / Linux**\.

See also [Working with Keybindings](settings-keybindings.md)\.
+  [General](#keybindings-default-windows-linux-general) 
+  [Tabs](#keybindings-default-windows-linux-tabs) 
+  [Panels](#keybindings-default-windows-linux-panels) 
+  [Code Editor](#keybindings-default-windows-linux-code-editor) 
+  [emmet](#keybindings-default-windows-linux-emmet) 
+  [Terminal](#keybindings-default-windows-linux-terminal) 
+  [Run and Debug](#keybindings-default-windows-linux-run-debug) 

## General<a name="keybindings-default-windows-linux-general"></a>


****  

| Description | Keybinding | Command | 
| --- | --- | --- | 
|  Add the selection as a watch expression  |   `Ctrl-Shift-C`   |   `addwatchfromselection`   | 
|  Remove the cut selection from the clipboard  |   `Esc`   |   `clearcut`   | 
|  Show the code completion context menu  |   `Ctrl-Space` \| `Alt-Space`   |   `complete`   | 
|  Code complete, and then overwrite  |   `Ctrl-Shift-Space` \| `Alt-Shift-Space`   |   `completeoverwrite`   | 
|  Copy the selection to the clipboard  |   `Ctrl-C`   |   `copy`   | 
|  Cut the selection to the clipboard  |   `Ctrl-X`   |   `cut`   | 
|  Expand code, where applicable  |   `Tab`   |   `expandSnippet`   | 
|  Show the find and replace bar for the current document  |   `Ctrl-F`   |   `find`   | 
|  Select all find matches in the current document  |   `Ctrl-Alt-K`   |   `findall`   | 
|  Go to the next match in the current document for the find query you entered last  |   `Ctrl-K`   |   `findnext`   | 
|  Go to the previous match in the current document for the find query you entered last  |   `Ctrl-Shift-K`   |   `findprevious`   | 
|  Display all known references to the symbol at the insertion point in the active file in the editor  |   `Shift-F3`   |   `findReferences`   | 
|  Open the **Environment** window, and then make the list of files active  |   `Shift-Esc`   |   `focusTree`   | 
|  Reformat the selected JavaScript code  |   `Ctrl-Shift-B`   |   `formatcode`   | 
|  Show the go to line box  |   `Ctrl-G`   |   `gotoline`   | 
|  Hide the find and replace bar, if it is showing  |   `Esc`   |   `hidesearchreplace`   | 
|  Go to the definition of the variable or function at the cursor  |   `F3`   |   `jumptodef`   | 
|  If a local Lambda function is selected in the **Lambda** section of the **AWS Resources** window, attempts to upload the function to Lambda as a remote function  |   `Ctrl-Shift-U`   |   `lambdaUploadFunction`   | 
|  Create a new file  |   `Alt-N`   |   `newfile`   | 
|  Show the **Preferences** tab  |   `Ctrl-,`   |   `openpreferences`   | 
|  Open a **Terminal** tab, and then switch to the parent folder of the selected file in the list of files  |   `Alt-L`   |   `opentermhere`   | 
|  Paste the clipboard's current contents at the cursor  |   `Ctrl-V`   |   `paste`   | 
|  Show suggestions for fixing errors  |   `Ctrl-F3`   |   `quickfix`   | 
|  Redo the last action  |   `Ctrl-Shift-Z` \| `Ctrl-Y`   |   `redo`   | 
|  Refresh the preview pane  |   `Ctrl-Enter`   |   `reloadpreview`   | 
|  Start a rename refactor for the selection  |   `Ctrl-Alt-R`   |   `renameVar`   | 
|  Show the find and replace bar for the current document, with focus on the replace with expression  |   `Alt-Shift-F` \| `Ctrl-H`   |   `replace`   | 
|  Rerun your initialization script  |   `Ctrl-Enter`   |   `rerunInitScript`   | 
|  Restart the environment  |   `Ctrl-R`   |   `restartc9`   | 
|  Reset the current file to its last saved version  |   `Ctrl-Shift-Q`   |   `reverttosaved`   | 
|  Reset each open file to its saved version  |   `Alt-Shift-Q`   |   `reverttosavedall`   | 
|  Save the current file to disk  |   `Ctrl-S`   |   `save`   | 
|  Save the current file to disk with a different file name  |   `Ctrl-Shift-S`   |   `saveas`   | 
|  Show the find and replace bar for multiple files  |   `Ctrl-Shift-F`   |   `searchinfiles`   | 
|  Show the **Process List** dialog box  |   `Ctrl-Alt-P`   |   `showprocesslist`   | 
|  Undo the last action  |   `Ctrl-Z`   |   `undo`   | 

## Tabs<a name="keybindings-default-windows-linux-tabs"></a>


****  

| Description | Keybinding | Command | 
| --- | --- | --- | 
|  Close all open tabs in the current pane, except the current tab  |   `Ctrl-Alt-W`   |   `closeallbutme`   | 
|  Close all open tabs in all panes  |   `Alt-Shift-W`   |   `closealltabs`   | 
|  Close the current pane  |   `Ctrl-W`   |   `closepane`   | 
|  Close the current tab  |   `Alt-W`   |   `closetab`   | 
|  Go one pane down  |   `Ctrl-Meta-Down`   |   `gotopanedown`   | 
|  Go one pane left  |   `Ctrl-Meta-Left`   |   `gotopaneleft`   | 
|  Go one pane right  |   `Ctrl-Meta-Right`   |   `gotopaneright`   | 
|  Go one pane up  |   `Ctrl-Meta-Up`   |   `gottopaneup`   | 
|  Go one tab left  |   `Ctrl-[`   |   `gototableft`   | 
|  Go one tab right  |   `Ctrl-]`   |   `gototabright`   | 
|  Move the current tab down one pane, or if the tab is already at the very bottom, create a split tab there  |   `Ctrl-Meta-Down`   |   `movetabdown`   | 
|  Move the current tab left, or if the tab is already at the far left, create a split tab there  |   `Ctrl-Meta-Left`   |   `movetableft`   | 
|  Move the current tab right, or if the tab is already at the far right, create a split tab there  |   `Ctrl-Meta-Right`   |   `movetabright`   | 
|  Move the current tab up one pane, or if the tab is already at the very top, create a split tab there  |   `Ctrl-Meta-Up`   |   `movetabup`   | 
|  Go to the next pane  |   `Ctrl-``   |   `nextpane`   | 
|  Go to the next tab  |   `Ctrl-Tab \| Alt-``   |   `nexttab`   | 
|  Go to the previous pane  |   `Ctrl-Shift-``   |   `previouspane`   | 
|  Go to the previous tab  |   `Ctrl-Shift-Tab \| Alt-Shift-``   |   `previoustab`   | 
|  Go back to the last tab  |   `Esc`   |   `refocusTab`   | 
|  Open the last tab again  |   `Alt-Shift-T`   |   `reopenLastTab`   | 
|  Show the current tab in the file tree  |   `Ctrl-Shift-L`   |   `revealtab`   | 
|  Go to the tenth tab  |   `Ctrl-0`   |   `tab0`   | 
|  Go to the first tab  |   `Ctrl-1`   |   `tab1`   | 
|  Go to the second tab  |   `Ctrl-2`   |   `tab2`   | 
|  Go to the third tab  |   `Ctrl-3`   |   `tab3`   | 
|  Go to the fourth tab  |   `Ctrl-4`   |   `tab4`   | 
|  Go to the fifth tab  |   `Ctrl-5`   |   `tab5`   | 
|  Go to the sixth tab  |   `Ctrl-6`   |   `tab6`   | 
|  Go to the seventh tab  |   `Ctrl-7`   |   `tab7`   | 
|  Go to the eighth tab  |   `Ctrl-8`   |   `tab8`   | 
|  Go to the ninth tab  |   `Ctrl-9`   |   `tab9`   | 

## Panels<a name="keybindings-default-windows-linux-panels"></a>


****  

| Description | Keybinding | Command | 
| --- | --- | --- | 
|  Show the **Go** window in **Go to Anything** mode  |   `Ctrl-E\|Ctrl-P`   |   `gotoanything`   | 
|  Show the **Go** window in **Go to Command** mode  |   `Ctrl-.\|F1`   |   `gotocommand`   | 
|  Show the **Go** window in **Go to File** mode\.  |   `Ctrl-O`   |   `gotofile`   | 
|  Show the **Go** window in **Go to Symbol** mode\.  |   `Ctrl-Shift-O`   |   `gotosymbol`   | 
|  Show the **Outline** window  |   `Ctrl-Shift-E`   |   `outline`   | 
|  Show the **Console** window if hidden, or hide if shown  |   `F6`   |   `toggleconsole`   | 
|  Show the **Environment** window if hidden, or hide if shown  |   `Ctrl-I`   |   `toggletree`   | 

## Code Editor<a name="keybindings-default-windows-linux-code-editor"></a>


****  

| Description | Keybinding | Command | 
| --- | --- | --- | 
|  Add a cursor one line above the active cursor, or if a cursor is already added, add another cursor above that one  |   `Ctrl-Alt-Up`   |   `addCursorAbove`   | 
|  Add a second cursor one line above the active cursor, or if a second cursor is already added, move the second cursor up one line  |   `Ctrl-Alt-Shift-Up`   |   `addCursorAboveSkipCurrent`   | 
|  Add a cursor one line below the active cursor, or if a cursor is already added, add another cursor below that one  |   `Ctrl-Alt-Down`   |   `addCursorBelow`   | 
|  Add a second cursor one line below the active cursor, or if a second cursor is already added, move the second cursor down one line  |   `Ctrl-Alt-Shift-Down`   |   `addCursorBelowSkipCurrent`   | 
|  Move all cursors to the same space as the active cursor on each of their lines, if they are misaligned  |   `Ctrl-Alt-A`   |   `alignCursors`   | 
|  Backspace one space  |   `Shift-Backspace \| Backspace`   |   `backspace`   | 
|  Indent the selection one tab  |   `Ctrl-]`   |   `blockindent`   | 
|  Outdent the selection one tab  |   `Ctrl-[`   |   `blockoutdent`   | 
|  Control whether focus can be switched from the editor to somewhere else in the IDE  |   `Ctrl-Z \| Ctrl-Shift-Z \| Ctrl-Y`   |   `cancelBrowserUndoInAce`   | 
|  Center the selection  |   `Ctrl-L`   |   `centerselection`   | 
|  Copy the contents of the line, and paste the copied contents one line down  |   `Alt-Shift-Down`   |   `copylinesdown`   | 
|  Copy the contents of the line, and paste the copied contents one line up  |   `Alt-Shift-Up`   |   `copylinesup`   | 
|  Cut the selection, or if there is no selection, delete one space  |   `Shift-Delete`   |   `cut_or_delete`   | 
|  Delete one space  |   `Delete`   |   `del`   | 
|  Copy the contents of the selection, and paste the copied contents immediately after the selection  |   `Ctrl-Shift-D`   |   `duplicateSelection`   | 
|  Include the current line's contents in the selection  |   `Ctrl-Shift-L`   |   `expandtoline`   | 
|  Include up to the next matching symbol in the selection  |   `Ctrl-Shift-M`   |   `expandToMatching`   | 
|  Fold the selected code; if a folded unit is selected, unfold it  |   `Alt-L \| Ctrl-F1`   |   `fold`   | 
|  Fold all possibly foldable elements  |   `Ctrl-Command-Option-0`   |   `foldall`   | 
|  Fold all possibly foldable elements, except for the current selection scope  |   `Alt-0`   |   `foldOther`   | 
|  Go down one line  |   `Down`   |   `golinedown`   | 
|  Go up one line  |   `Up`   |   `golineup`   | 
|  Go to the end of the file  |   `Ctrl-End`   |   `gotoend`   | 
|  Go left one space  |   `Left`   |   `gotoleft`   | 
|  Go to the end of the current line  |   `Alt-Right \| End`   |   `gotolineend`   | 
|  Go to the start of the current line  |   `Alt-Left \| Home`   |   `gotolinestart`   | 
|  Go to the next error  |   `Alt-E`   |   `goToNextError`   | 
|  Go down one page  |   `Page Down`   |   `gotopagedown`   | 
|  Go up one page  |   `Page Up`   |   `gotopageup`   | 
|  Go to the previous error  |   `Alt-Shift-E`   |   `goToPreviousError`   | 
|  Go right one space  |   `Right`   |   `gotoright`   | 
|  Go to the start of the file  |   `Ctrl-Home`   |   `gotostart`   | 
|  Go one word to the left  |   `Ctrl-Left`   |   `gotowordleft`   | 
|  Go one word to the right  |   `Ctrl-Right`   |   `gotowordright`   | 
|  Indent the selection one tab  |   `Tab`   |   `indent`   | 
|  Go to the matching symbol in the current scope  |   `Ctrl-P`   |   `jumptomatching`   | 
|  Increase the font size  |   `Ctrl-+ \| Ctrl-=`   |   `largerfont`   | 
|  Decrease the number to the left of the cursor by 1, if it is a number  |   `Ctrl-Shift-Down`   |   `modifyNumberDown`   | 
|  Increase the number to the left of the cursor by 1, if it is a number  |   `Ctrl-Shift-Up`   |   `modifyNumberUp`   | 
|  Move the selection down one line  |   `Alt-Down`   |   `movelinesdown`   | 
|  Move the selection up one line  |   `Alt-Up`   |   `movelinesup`   | 
|  Outdent the selection one tab  |   `Shift-Tab`   |   `outdent`   | 
|  Turn on overwrite mode, or if on, turn off  |   `Insert`   |   `overwrite`   | 
|  Go down one page  |   `Option-Page Down`   |   `pagedown`   | 
|  Go up one page  |   `Option-Page Up`   |   `pageup`   | 
|  Delete the contents of the current line  |   `Ctrl-D`   |   `removeline`   | 
|  Delete from the cursor to the end of the current line  |   `Alt-Delete`   |   `removetolineend`   | 
|  Delete from the beginning of the current line up to the cursor  |   `Alt-Backspace`   |   `removetolinestart`   | 
|  Delete the word to the left of the cursor  |   `Ctrl-Backspace`   |   `removewordleft`   | 
|  Delete the word to the right of the cursor  |   `Ctrl-Delete`   |   `removewordright`   | 
|  Replay previously recorded keystrokes  |   `Ctrl-Shift-E`   |   `replaymacro`   | 
|  Scroll the current file down by one line  |   `Ctrl-Down`   |   `scrolldown`   | 
|  Scroll the current file up by one line  |   `Ctrl-Up`   |   `scrollup`   | 
|  Select all selectable content  |   `Ctrl-A`   |   `selectall`   | 
|  Include the next line down in the selection  |   `Shift-Down`   |   `selectdown`   | 
|  Include the next space to the left in the selection  |   `Shift-Left`   |   `selectleft`   | 
|  Include the rest of the current line in the selection, starting from the cursor  |   `Shift-End`   |   `selectlineend`   | 
|  Include the beginning of the current line in the selection, up to the cursor  |   `Shift-Home`   |   `selectlinestart`   | 
|  Include more matching selections that are after the selection  |   `Ctrl-Alt-Right`   |   `selectMoreAfter`   | 
|  Include more matching selections that are before the selection  |   `Ctrl-Alt-Left`   |   `selectMoreBefore`   | 
|  Include the next matching selection that is after the selection  |   `Ctrl-Alt-Shift-Right`   |   `selectNextAfter`   | 
|  Include the next matching selection that is before the selection  |   `Ctrl-Alt-Shift-Left`   |   `selectNextBefore`   | 
|  Select or find the next matching selection  |   `Alt-K`   |   `selectOrFindNext`   | 
|  Select or find the previous matching selection  |   `Alt-Shift-K`   |   `selectOrFindPrevious`   | 
|  Include from the cursor down to the end of the current page in the selection  |   `Shift-Page Down`   |   `selectpagedown`   | 
|  Include from the cursor up to the beginning of the current page in the selection  |   `Shift-Page Up`   |   `selectpageup`   | 
|  Include the next space to the right of the cursor in the selection  |   `Shift-Right`   |   `selectright`   | 
|  Include from the cursor down to the end of the current file in the selection  |   `Ctrl-Shift-End`   |   `selecttoend`   | 
|  Include from the cursor to the end of the current line in the selection  |   `Alt-Shift-Right`   |   `selecttolineend`   | 
|  Include from the beginning of the current line to the cursor in the selection  |   `Alt-Shift-Left`   |   `selecttolinestart`   | 
|  Include from the cursor to the next matching symbol in the current scope  |   `Ctrl-Shift-P`   |   `selecttomatching`   | 
|  Include from the cursor up to the beginning of the current file in the selection  |   `Ctrl-Shift-Home`   |   `selecttostart`   | 
|  Include the next line up in the selection  |   `Shift-Up`   |   `selectup`   | 
|  Include the next word to the left of the cursor in the selection  |   `Ctrl-Shift-Left`   |   `selectwordleft`   | 
|  Include the next word to the right of the cursor in the selection  |   `Ctrl-Shift-Right`   |   `selectwordright`   | 
|  Show the **Preferences** tab  |   `Ctrl-,`   |   `showSettingsMenu`   | 
|  Clear all previous selections  |   `Esc`   |   `singleSelection`   | 
|  Decrease the font size  |   `Ctrl--`   |   `smallerfont`   | 
|  If multiple lines are selected, rearrange them into a sorted order  |   `Ctrl-Alt-S`   |   `sortlines`   | 
|  Add a cursor at the end of the current line  |   `Ctrl-Alt-L`   |   `splitIntoLines`   | 
|  Move the contents of the cursor to the end of the line, to its own line  |   `Ctrl-O`   |   `splitline`   | 
|  Surround the selection with block comment characters, or remove them if they are there  |   `Ctrl-Shift-/`   |   `toggleBlockComment`   | 
|  Add line comment characters at the start of each selected line, or remove them if they are there  |   `Ctrl-/`   |   `togglecomment`   | 
|  Fold code, or remove code folding if it is there  |   `F2`   |   `toggleFoldWidget`   | 
|  Fold parent code, or remove folding if it is there  |   `Alt-F2`   |   `toggleParentFoldWidget`   | 
|  Start keystroke recording, or stop if it is already recording  |   `Ctrl-Alt-E`   |   `togglerecording`   | 
|  Wrap words, or stop wrapping words if they are already wrapping  |   `Ctrl-Q`   |   `toggleWordWrap`   | 
|  Change the selection to all lowercase  |   `Ctrl-Shift-U`   |   `tolowercase`   | 
|  Change the selection to all uppercase  |   `Ctrl-U`   |   `touppercase`   | 
|  Transpose the selection  |   `Alt-X`   |   `transposeletters`   | 
|  Unfold the selected code  |   `Alt-Shift-L \| Ctrl-Shift-F1`   |   `unfold`   | 
|  Unfold code folding for the entire file  |   `Alt-Shift-0`   |   `unfoldall`   | 

## emmet<a name="keybindings-default-windows-linux-emmet"></a>


****  

| Description | Keybinding | Command | 
| --- | --- | --- | 
|  Evaluate a simple math expression \(such as `2*4` or `10/2`\), and output its result  |   `Shift-Ctrl-Y`   |   `emmet_evaluate_math_expression`   | 
|  Expand CSS\-like abbreviations into HTML, XML, or CSS code, depending on the current file's syntax  |   `Ctrl-Alt-E`   |   `emmet_expand_abbreviation`   | 
|  Traverse expanded CSS\-like abbreviations, by tab stop  |   `Tab`   |   `emmet_expand_abbreviation_with_tab`   | 
|  Go to the next editable code part  |   `Shift-Ctrl-.`   |   `emmet_select_next_item`   | 
|  Go to the previous editable code part  |   `Shift-Ctrl-,`   |   `emmet_select_previous_item`   | 
|  Expand an abbreviation, and then place the current selection within the last element of the generated snippet  |   `Shift-Ctrl-A`   |   `emmet_wrap_with_abbreviation`   | 

## Terminal<a name="keybindings-default-windows-linux-terminal"></a>


****  

| Description | Keybinding | Command | 
| --- | --- | --- | 
|  Open a new **Terminal** tab  |   `Alt-T`   |   `openterminal`   | 
|  Switch between the editor and the **Terminal** tab  |   `Alt-S`   |   `switchterminal`   | 

## Run and Debug<a name="keybindings-default-windows-linux-run-debug"></a>


****  

| Description | Keybinding | Command | 
| --- | --- | --- | 
|  Build the current file  |   `Ctrl-B`   |   `build`   | 
|  Resume the current paused process  |   `F8`   |   `resume`   | 
|  Run or debug the current application  |   `Alt-F5`   |   `run`   | 
|  Run or debug the last run file  |   `F5`   |   `runlast`   | 
|  Step into the function that is next on the stack  |   `F11`   |   `stepinto`   | 
|  Step out of the current function scope  |   `Shift-F11`   |   `stepout`   | 
|  Step over the current expression on the stack  |   `F10`   |   `stepover`   | 
|  Stop running or debugging the current application  |   `Shift-F5`   |   `stop`   | 
|  Stop building the current file  |   `Ctrl-Shift-C`   |   `stopbuild`   | 