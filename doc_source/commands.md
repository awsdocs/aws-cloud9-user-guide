# Commands Reference for the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="commands"></a>

Following is a list of default commands in the AWS Cloud9 IDE\.

To run a command in the AWS Cloud9 IDE:

1. Choose the **Go** button \(magnifying glass\) to display the **Go** window\. If the **Go** button is not visible, choose **Window, Go** on the menu bar\.

1. In the **Go to Anything** box, type a dot \(`.`\) followed by the name of the command\.

1. Do one of the following in the list of matching commands:
   + Choose the command to run\.
   + Use your up and down arrow keys to choose a command, and then press `Enter` to run the chosen command\.


****  

| Command | Description | 
| --- | --- | 
|   `addCursorAbove`   |  Add a cursor one line above the active cursor, or if a cursor is already added, add another cursor above that one  | 
|   `addCursorAboveSkipCurrent`   |  Add a second cursor one line above the active cursor, or if a second cursor is already added, move the second cursor up one line  | 
|   `addCursorBelow`   |  Add a cursor one line below the active cursor, or if a cursor is already added, add another cursor below that one  | 
|   `addCursorBelowSkipCurrent`   |  Add a second cursor one line below the active cursor, or if a second cursor is already added, move the second cursor down one line  | 
|   `addfavorite`   |  Add the selected file or folder to the **Favorites** list in the **Environment** window  | 
|   `addwatchfromselection`   |  Add the selection as a watch expression  | 
|   `alignCursors`   |  Move all cursors to the same space as the active cursor on each of their lines, if they are misaligned  | 
|   `aws-panel`   |  Show the **AWS Resources** window  | 
|   `backspace`   |  Backspace one space  | 
|   `blockindent`   |  Indent the selection one tab  | 
|   `blockoutdent`   |  Outdent the selection one tab  | 
|   `build`   |  Build the current file  | 
|   `cancelBrowserAction`   |  Cancel various built\-in web browser key bindings that can be annoying if triggered accidentally  | 
|   `cancelBrowserUndoInAce`   |  Control whether focus can be switched from the editor to somewhere else in the IDE  | 
|   `centerselection`   |  Center the selection  | 
|   `clearcut`   |  Remove the cut selection from the clipboard  | 
|   `clearterm`   |  Clear the buffer in the **Terminal** pane  | 
|   `clonetab`   |  Create a copy of the current tab in a new tab  | 
|   `closeallbutme`   |  Close all open tabs in the current pane, except the current tab  | 
|   `closealltabs`   |  Close all open tabs in all panes  | 
|   `closealltotheleft`   |  Close all tabs to the left of the current tab  | 
|   `closealltotheright`   |  Close all tabs to the right of the current tab  | 
|   `closepane`   |  Close the current pane  | 
|   `closetab`   |  Close the current tab  | 
|   `complete`   |  Show the code completion context menu  | 
|   `completeoverwrite`   |  Code complete, and then overwrite  | 
|   `convertIndentation`   |  Convert between tabs and spaces in the editor  | 
|   `copy`   |  Copy the selection to the clipboard  | 
|   `copyFilePath`   |  Copy the full path of the current file to the clipboard  | 
|   `copylinesdown`   |  Copy the contents of the line, and paste the copied contents one line down  | 
|   `copylinesup`   |  Copy the contents of the line, and paste the copied contents one line up  | 
|   `cut`   |  Cut the selection to the clipboard  | 
|   `cut_or_delete`   |  Cut the selection to the clipboard, or delete to the right if the selection is empty  | 
|   `del`   |  Delete one space  | 
|   `detectIndentation`   |  Detect the indentation type \(spaces or tabs\) and length, based on the document's contents  | 
|   `duplicateSelection`   |  Copy the contents of the selection, and paste the copied contents immediately after the selection  | 
|   `emmet_decrement_number_by_01`   |  Decrease the selected number by 0\.1, if it is a number  | 
|   `emmet_decrement_number_by_1`   |  Decrease the selected number by 1, if is a number  | 
|   `emmet_decrement_number_by_10`   |  Decrease the selected number by 10, if is a number  | 
|   `emmet_evaluate_math_expression`   |  Evaluate a simple math expression \(such as `2*4` or `10/2`\), and output its result  | 
|   `emmet_expand_abbreviation`   |  Expand CSS\-like abbreviations into HTML, XML, or CSS code, depending on the current file's syntax  | 
|   `emmet_expand_abbreviation_with_tab`   |  Traverse expanded CSS\-like abbreviations, by tab stop  | 
|   `emmet_increment_number_by_01`   |  Increase the selected number by 0\.1, if it is a number  | 
|   `emmet_increment_number_by_1`   |  Increase the selected number by 1, if it is a number  | 
|   `emmet_increment_number_by_10`   |  Increase the selected number by 10, if it is a number  | 
|   `emmet_match_pair_inward`   |  Shrink the selection to the next inner set of matching tags  | 
|   `emmet_match_pair_outward`   |  Expand the selection to include the next outer set of matching tags  | 
|   `emmet_matching_pair`   |  Go between the opening and closing tag, if the selection is a tag  | 
|   `emmet_next_edit_point`   |  Go to the next tag, empty attribute, or newline with indentation  | 
|   `emmet_prev_edit_point`   |  Go to the previous tag, empty attribute, or newline with indentation  | 
|   `emmet_reflect_css_value`   |  Copy the selected CSS property into all matching variations, if the selection is a CSS property  | 
|   `emmet_remove_tag`   |  Delete the selected tag, if the selection is a tag  | 
|   `emmet_select_next_item`   |  Go to the next editable code part  | 
|   `emmet_select_previous_item`   |  Go to the previous editable code part  | 
|   `emmet_split_join_tag`   |  If the selection is an empty tag, replace it with an opening and closing tag pair; if the tag has an opening and closing tag pair, replace it with an empty tag  | 
|   `emmet_toggle_comment`   |  Add comment characters to the current line, or remove them if they are there  | 
|   `emmet_wrap_with_abbreviation`   |  Expand an abbreviation, and then place the selection within the last element of the generated snippet  | 
|   `expandSnippet`   |  Expand code, where applicable  | 
|   `expandtoline`   |  Include the current line's contents in the selection  | 
|   `expandToMatching`   |  Include up to the next matching symbol in the selection  | 
|   `find`   |  Show the find and replace bar for the current document  | 
|   `findAll`   |  Select all find matches in the current document  | 
|   `findnext`   |  Go to the next match in the current document for the find query you entered last  | 
|   `findprevious`   |  Go to the previous match in the current document for the find query you entered last  | 
|   `findReferences`   |  Display all known references to the symbol at the insertion point in the active file in the editor  | 
|   `focusTree`   |  Open the **Environment** window, and then make the list of files active  | 
|   `fold`   |  Fold the selected code; if a folded unit is selected, unfold it  | 
|   `foldall`   |  Fold all possibly foldable elements  | 
|   `foldOther`   |  Fold all possibly foldable elements, except for the selection scope  | 
|   `forceToggleTimeslider`   |  Show the **File Revision History** pane, or hide if shown  | 
|   `formatcode`   |  Reformat the selected JavaScript code  | 
|   `formatprefs`   |  Open the **Project Settings** section of the **Preferences** tab to programming language settings  | 
|   `foursplit`   |  Display a four\-pane layout  | 
|   `gethelp`   |  Display the AWS Discussion Forum for AWS Cloud9  | 
|   `gitcloneterminal`   |  Run the ** `git clone` ** command in a new terminal session  | 
|   `golinedown`   |  Go down one line  | 
|   `golineup`   |  Go up one line  | 
|   `gotoanything`   |  Show the **Go** window in **Go to Anything** mode  | 
|   `gotocommand`   |  Show the **Go** window in **Go to Command** mode  | 
|   `gotoend`   |  Go to the end of the file  | 
|   `gotofile`   |  Show the **Go** window in **Go to File** mode\.  | 
|   `gotoleft`   |  Go left one space  | 
|   `gotoline`   |  Show the go to line box  | 
|   `gotolineend`   |  Go to the end of the current line  | 
|   `gotolinestart`   |  Go to the start of the current line  | 
|   `goToNextError`   |  Go to the next error  | 
|   `gotopagedown`   |  Go down one page  | 
|   `gotopageup`   |  Go up one page  | 
|   `gotopanedown`   |  Go one pane down  | 
|   `gotopaneleft`   |  Go one pane left  | 
|   `gotopaneright`   |  Go one pane right  | 
|   `gotopaneup`   |  Go one pane up  | 
|   `goToPreviousError`   |  Go to the previous error  | 
|   `gotoright`   |  Go right one space  | 
|   `gotostart`   |  Go to the start of the file  | 
|   `gotosymbol`   |  Show the **Go** window in **Go to Symbol** mode\.  | 
|   `gototableft`   |  Go one tab left  | 
|   `gototabright`   |  Go one tab right  | 
|   `gotowordleft`   |  Go one word to the left  | 
|   `gotowordright`   |  Go one word to the right  | 
|   `hideGotoLine`   |  Hide the go to line box, if it is showing  | 
|   `hidesearchreplace`   |  Hide the find and replace bar, if it is showing  | 
|   `hsplit`   |  Split the current pane into two columns, and then move the current tab to the new column  | 
|   `indent`   |  Indent the selection one tab  | 
|   `insertstring`   |  Insert a string of text while typing or pasting  | 
|   `inserttext`   |  Insert text while typing or pasting  | 
|   `invertSelection`   |  Select everything other than the selection  | 
|   `joinlines`   |  Remove all line breaks from the current selection  | 
|   `jumptodef`   |  Go to the definition of the variable or function at the cursor  | 
|   `jumptomatching`   |  Go to the matching symbol in the current scope  | 
|   `lambdaConvertFunction`   |  Show the **Convert to SAM** dialog box  | 
|   `lambdaCreateFunction`   |  Show the **Create serverless application** dialog box  | 
|   `lambdaImportFunction`   |  If a remote AWS Lambda function is selected in the **Lambda** section of the **AWS Resources** window, attempts to import the function into the IDE as a local function  | 
|   `lambdaLinkToCFStack`   |  Show the **Link application to CloudFormation stack** dialog box  | 
|   `lambdaRefreshFunctionsList`   |  Refreshes the **Lambda** section of the **AWS Resources** window if shown  | 
|   `lambdaUploadFunction`   |  If a local Lambda function is selected in the **Lambda** section of the **AWS Resources** window, attempts to upload the function to Lambda as a remote function  | 
|   `largerfont`   |  Increase the font size  | 
|   `maximizeconsole`   |  Expand the console to cover the entire IDE  | 
|   `modifyNumberDown`   |  Decrease the number to the left of the cursor by 1, if it is a number  | 
|   `modifyNumberUp`   |  Increase the number to the left of the cursor by 1, if it is a number  | 
|   `movelinesdown`   |  Move selection down one line  | 
|   `movelinesup`   |  Move selection up one line  | 
|   `movetabdown`   |  Move the current tab down one pane, or if the tab is already at the very bottom, create a split tab there  | 
|   `movetableft`   |  Move the current tab left, or if the tab is already at the far left, create a split tab there  | 
|   `movetabright`   |  Move the current tab right, or if the tab is already at the far right, create a split tab there  | 
|   `movetabup`   |  Move the current tab up one pane, or if the tab is already at very top, create a split tab there  | 
|   `newEnvironment`   |  Show the **Create new environment** wizard in the AWS Cloud9 console  | 
|   `newfile`   |  Create a new file  | 
|   `newfolder`   |  Create a new folder relative to the selection in the **Environment** window  | 
|   `nextpane`   |  Go to the next pane  | 
|   `nexttab`   |  Go to the next tab  | 
|   `nosplit`   |  Combine all split panes into a single pane  | 
|   `opencoverageview`   |  Show the **Code Coverage** tab  | 
|   `openpreferences`   |  Show the **Preferences** tab  | 
|   `opentermhere`   |  Open a **Terminal** tab, and then switch to the parent folder of the selected file in the list of files  | 
|   `openterminal`   |  Open a new **Terminal** tab  | 
|   `outdent`   |  Outdent the selection one tab  | 
|   `outline`   |  Show the **Outline** window  | 
|   `overwrite`   |  Turn on overwrite mode, or if on, turn off  | 
|   `pagedown`   |  Go down one page  | 
|   `pageup`   |  Go up one page  | 
|   `passKeysToBrowser`   |  Enable keys to be handled by the web browser  | 
|   `paste`   |  Paste the clipboard's current contents at the cursor  | 
|   `preview`   |  Show the preview pane  | 
|   `previouspane`   |  Go to the previous pane  | 
|   `previoustab`   |  Go to the previous tab  | 
|   `quickfix`   |  Show suggestions for fixing errors  | 
|   `redo`   |  Redo the last action  | 
|   `refocusTab`   |  Go back to the last tab  | 
|   `reloadpreview`   |  Refresh the preview pane  | 
|   `removefavorite`   |  Delete the item from the **Favorites** list, if the selection is a favorite  | 
|   `removeline`   |  Delete the contents of the current line  | 
|   `removetolineend`   |  Delete from the cursor to the end of the current line  | 
|   `removetolinestart`   |  Delete from the beginning of the current line up to the cursor  | 
|   `removewordleft`   |  Delete the word to the left of the cursor  | 
|   `removewordright`   |  Delete the word to the right of the cursor  | 
|   `renameVar`   |  Start a rename refactor for the selection  | 
|   `reopenLastTab`   |  Open the last tab again  | 
|   `replace`   |  Show the find and replace bar for the current document, with focus on the replace with expression  | 
|   `replaceall`   |  Replace all matches for **Find** with **Replace With** in the find and replace bar for the current document  | 
|   `replacenext`   |  Replace the next match for **Find** with **Replace With** in the find and replace bar for the current document  | 
|   `replaceprevious`   |  Replace the previous match for **Find** with **Replace With** in the find and replace bar for the current document  | 
|   `replaymacro`   |  Replay previously recorded keystrokes  | 
|   `rerunInitScript`   |  Rerun your initialization script  | 
|   `restartc9`   |  Restart the environment  | 
|   `resume`   |  Resume the current paused process  | 
|   `revealtab`   |  Show the current tab in the file tree  | 
|   `reverttosaved`   |  Reset the current file to its last saved version  | 
|   `reverttosavedall`   |  Reset each open file to its saved version  | 
|   `run`   |  Run or debug the current application  | 
|   `runlast`   |  Run or debug the last run file  | 
|   `save`   |  Save the current file to disk  | 
|   `saveall`   |  Save all unsaved files to disk  | 
|   `saveas`   |  Save the current file to disk with a different file name  | 
|   `savePaneLayout`   |  Save the current pane layout in the **Window, Saved Layouts** menu  | 
|   `savePaneLayoutAndCloseTabs`   |  Save the current pane layout in the **Window, Saved Layouts** menu, and then close all open tabs  | 
|   `scrolldown`   |  Scroll down in the current document  | 
|   `scrollup`   |  Scroll up in the current document  | 
|   `searchinfiles`   |  Show the find and replace bar for multiple files  | 
|   `selectall`   |  Select all selectable content  | 
|   `selectdown`   |  Include the next line down in the selection  | 
|   `selectleft`   |  Include the next space to the left in the selection  | 
|   `selectlineend`   |  Include the rest of the current line in the selection, starting from the cursor  | 
|   `selectlinestart`   |  Include the beginning of the current line in the selection, up to the cursor  | 
|   `selectMoreAfter`   |  Include more matching selections that are after the selection  | 
|   `selectMoreBefore`   |  Include more matching selections that are before the selection  | 
|   `selectNextAfter`   |  Include the next matching selection that is after the selection  | 
|   `selectNextBefore`   |  Include the next matching selection that is before the selection  | 
|   `selectOrFindNext`   |  Select or find the next matching selection  | 
|   `selectOrFindPrevious`   |  Select or find the previous matching selection  | 
|   `selectpagedown`   |  Include from the cursor down to the end of the current page in the selection  | 
|   `selectpageup`   |  Include from the cursor up to the beginning of the current page in the selection  | 
|   `selectright`   |  Include the next space to the right of the cursor in the selection  | 
|   `selecttoend`   |  Include from the cursor down to the end of the current file in the selection  | 
|   `selecttolineend`   |  Include from the cursor to the end of the current line in the selection  | 
|   `selecttolinestart`   |  Include from the beginning of the current line to the cursor in the selection  | 
|   `selecttomatching`   |  Include from the cursor to the next matching symbol in the current scope  | 
|   `selecttostart`   |  Include from the cursor up to the beginning of the current file in the selection  | 
|   `selectup`   |  Include the next line up in the selection  | 
|   `selectVar`   |  Select all instances of the variable, if the selection is a variable  | 
|   `selectwordleft`   |  Include the next word to the left of the cursor in the selection  | 
|   `selectwordright`   |  Include the next word to the right of the cursor in the selection  | 
|   `setIndentation`   |  Set the indentation type \(spaces or tabs\) and length  | 
|   `sharedialog`   |  Show the **Share this environment** dialog box  | 
|   `showimmediate`   |  Show the **Immediate** tab  | 
|   `showinstaller`   |  Show the **AWS Cloud9 Installer** dialog box  | 
|   `showoutput`   |  Show the **Output** tab  | 
|   `showprocesslist`   |  Show the **Process List** dialog box  | 
|   `showSettingsMenu`   |  Show the **Preferences** tab  | 
|   `singleSelection`   |  Clear all previous selections  | 
|   `smallerfont`   |  Decrease the font size  | 
|   `sortlines`   |  If multiple lines are selected, rearrange them into a sorted order  | 
|   `splitIntoLines`   |  Add a cursor at the end of the current line  | 
|   `splitline`   |  Move the contents of the cursor to the end of the line, to its own line  | 
|   `stepinto`   |  Step into the function that is next on the stack  | 
|   `stepout`   |  Step out of the current function scope  | 
|   `stepover`   |  Step over the current expression on the stack  | 
|   `stop`   |  Stop running or debugging the current application  | 
|   `stopbuild`   |  Stop building the current file  | 
|   `stripws`   |  Remove whitespace from the end of each line  | 
|   `suspend`   |  Suspend running or debugging the current application  | 
|   `switchterminal`   |  Switch between the editor and the **Terminal** tab  | 
|   `syntax`   |  Set the syntax type  | 
|   `tab0`   |  Go to the tenth tab  | 
|   `tab1`   |  Go to the first tab  | 
|   `tab2`   |  Go to the second tab  | 
|   `tab3`   |  Go to the third tab  | 
|   `tab4`   |  Go to the fourth tab  | 
|   `tab5`   |  Go to the fifth tab  | 
|   `tab6`   |  Go to the sixth tab  | 
|   `tab7`   |  Go to the seventh tab  | 
|   `tab8`   |  Go to the eighth tab  | 
|   `tab9`   |  Go to the ninth tab  | 
|   `term_detach`   |  Detach clients attached to the **Terminal** pane  | 
|   `term_help`   |  Show help for the **Terminal** pane  | 
|   `term_restart`   |  Restart the **Terminal** pane  | 
|   `threeleft`   |  Create a three\-pane layout with two panes on the left and one pane on the right  | 
|   `threeright`   |  Create a three\-pane layout with two panes on the right and one pane on the left  | 
|   `toggle_term_status`   |  Show **Terminal** pane status, or hide if shown  | 
|   `toggleBlockComment`   |  Surround the selection with block comment characters, or remove them if they are there  | 
|   `toggleButtons`   |  Show tabs, or hide if shown  | 
|   `togglecomment`   |  Add line comment characters at the start of each selected line, or remove them if they are there  | 
|   `toggleconsole`   |  Show the **Console** window if hidden, or hide if shown  | 
|   `toggledebugger`   |  Show the **Debugger** window, or hide if shown  | 
|   `toggleFoldWidget`   |  Fold code, or remove code folding if it is there  | 
|   `toggleMenubar`   |  Show the menu bar, or hide if shown  | 
|   `toggleOpenfiles`   |  Show the **Open Files** list in the **Environment** window, or hide if shown  | 
|   `toggleParentFoldWidget`   |  Fold parent code, or remove folding if it is there  | 
|   `togglerecording`   |  Start keystroke recording, or stop if it is already recording  | 
|   `toggletree`   |  Show the **Environment** window if hidden, or hide if shown  | 
|   `toggleWordWrap`   |  Wrap words, or stop wrapping words if they are already wrapping  | 
|   `tolowercase`   |  Change the selection to all lowercase  | 
|   `touppercase`   |  Change the selection to all uppercase  | 
|   `transposeletters`   |  Transpose the selection  | 
|   `trimTrailingSpace`   |  Trim whitespace at the ends of lines  | 
|   `twohsplit`   |  Create a two\-pane layout, with panes side by side  | 
|   `twovsplit`   |  Create a two\-pane layout, with panes top and bottom  | 
|   `undo`   |  Undo the last action  | 
|   `unfold`   |  Unfold selected code  | 
|   `unfoldall`   |  Unfold code folding for the entire file  | 
|   `uploadLocalFiles`   |  Show the **Upload Files** dialog box  | 
|   `vsplit`   |  Split the current pane into two panes, top and bottom, and move the current tab to the top pane  | 