.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _commands:

############################################
Commands Reference for the |AC9IDElongtitle|
############################################

.. meta::
   :description:
      Provides a list of default commands in the AWS Cloud9 IDE.

Following is a list of default commands in the |AC9IDE|.

For more information, in the |AC9IDE|, choose the :guilabel:`Commands` button to display the :guilabel:`Commands` window. If the :guilabel:`Commands` button is not visible, choose
:guilabel:`Window, Commands` on the menu bar.

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - Command
     - Description
   * - :code:`addCursorAbove`
     - Add a cursor one line above the active cursor, or if a cursor is already added, add another cursor
       above that one
   * - :code:`addCursorAboveSkipCurrent`
     - Add a second cursor one line above the active cursor, or if a second cursor is already added, move
       the second cursor up one line
   * - :code:`addCursorBelow`
     - Add a cursor one line below the active cursor, or if a cursor is already added, add another cursor
       below that one
   * - :code:`addCursorBelowSkipCurrent`
     - Add a second cursor one line below the active cursor, or if a second cursor is already added, move
       the second cursor down one line
   * - :code:`addfavorite`
     - Add the selected file or folder to the :guilabel:`Favorites` list in the :guilabel:`Environment`
       window
   * - :code:`addwatchfromselection`
     - Add the selection as a watch expression
   * - :code:`alignCursors`
     - Move all cursors to the same space as the active cursor on each of their lines, if they are misaligned
   * - :code:`backspace`
     - Backspace one space
   * - :code:`blockindent`
     - Indent the selection one tab
   * - :code:`blockoutdent`
     - Outdent the selection one tab
   * - :code:`build`
     - Build the current file
   * - :code:`cancelBrowserAction`
     - Cancel various built-in web browser key bindings that can be annoying if triggered accidentally
   * - :code:`cancelBrowserUndoInAce`
     - Control whether focus can be switched from the editor to somewhere else in the IDE
   * - :code:`centerselection`
     - Center the selection
   * - :code:`clearcut`
     - Remove the cut selection from the clipboard
   * - :code:`clearterm`
     - Clear the buffer in the :guilabel:`Terminal` pane
   * - :code:`clonetab`
     - Create a copy of the current tab in a new tab
   * - :code:`closeallbutme`
     - Close all open tabs in the current pane, except the current tab
   * - :code:`closealltabs`
     - Close all open tabs in all panes
   * - :code:`closealltotheleft`
     - Close all tabs to the left of the current tab
   * - :code:`closealltotheright`
     - Close all tabs to the right of the current tab
   * - :code:`closepane`
     - Close the current pane
   * - :code:`closetab`
     - Close the current tab
   * - :code:`commands`
     - Show the :guilabel:`Commands` window
   * - :code:`complete`
     - Show the code completion context menu
   * - :code:`completeoverwrite`
     - Code complete, and then overwrite
   * - :code:`convertIndentation`
     - Convert between tabs and spaces in the editor
   * - :code:`copy`
     - Copy the selection to the clipboard
   * - :code:`copyFilePath`
     - Copy the full path of the current file to the clipboard
   * - :code:`copylinesdown`
     - Copy the contents of the line, and paste the copied contents one line down
   * - :code:`copylinesup`
     - Copy the contents of the line, and paste the copied contents one line up
   * - :code:`cut`
     - Cut the selection to the clipboard
   * - :code:`cut_or_delete`
     - Cut the selection to the clipboard, or delete to the right if the selection is empty
   * - :code:`del`
     - Delete one space
   * - :code:`detectIndentation`
     - Detect the indentation type (spaces or tabs) and length, based on the document's contents
   * - :code:`duplicateSelection`
     - Copy the contents of the selection, and paste the copied contents immediately after the selection
   * - :code:`emmet_decrement_number_by_01`
     - Decrease the selected number by 0.1, if it is a number
   * - :code:`emmet_decrement_number_by_1`
     - Decrease the selected number by 1, if is a number
   * - :code:`emmet_decrement_number_by_10`
     - Decrease the selected number by 10, if is a number
   * - :code:`emmet_evaluate_math_expression`
     - Evaluate a simple math expression (such as :code:`2*4` or :code:`10/2`), and output its result
   * - :code:`emmet_expand_abbreviation`
     - Expand CSS-like abbreviations into HTML, XML, or CSS code, depending on the current file's syntax
   * - :code:`emmet_expand_abbreviation_with_tab`
     - Traverse expanded CSS-like abbreviations, by tab stop
   * - :code:`emmet_increment_number_by_01`
     - Increase the selected number by 0.1, if it is a number
   * - :code:`emmet_increment_number_by_1`
     - Increase the selected number by 1, if it is a number
   * - :code:`emmet_increment_number_by_10`
     - Increase the selected number by 10, if it is a number
   * - :code:`emmet_match_pair_inward`
     - Shrink the selection to the next inner set of matching tags
   * - :code:`emmet_match_pair_outward`
     - Expand the selection to include the next outer set of matching tags
   * - :code:`emmet_matching_pair`
     - Go between the opening and closing tag, if the selection is a tag
   * - :code:`emmet_next_edit_point`
     - Go to the next tag, empty attribute, or newline with indentation
   * - :code:`emmet_prev_edit_point`
     - Go to the previous tag, empty attribute, or newline with indentation
   * - :code:`emmet_reflect_css_value`
     - Copy the selected CSS property into all matching variations, if the selection is a CSS property
   * - :code:`emmet_remove_tag`
     - Delete the selected tag, if the selection is a tag
   * - :code:`emmet_select_next_item`
     - Go to the next editable code part
   * - :code:`emmet_select_previous_item`
     - Go to the previous editable code part
   * - :code:`emmet_split_join_tag`
     - If the selection is an empty tag, replace it with an opening and closing tag pair; if the tag has an opening and closing tag pair, replace it with an empty tag
   * - :code:`emmet_toggle_comment`
     - Add comment characters to the current line, or remove them if they are there
   * - :code:`emmet_wrap_with_abbreviation`
     - Expand an abbreviation, and then place the selection within the last element of the generated snippet
   * - :code:`expandSnippet`
     - Expand code, where applicable
   * - :code:`expandtoline`
     - Include the current line's contents in the selection
   * - :code:`expandToMatching`
     - Include up to the next matching symbol in the selection
   * - :code:`find`
     - Show the find and replace bar for the current document
   * - :code:`findAll`
     - Select all find matches in the current document
   * - :code:`findnext`
     - Go to the next match in the current document for the find query you entered last
   * - :code:`findprevious`
     - Go to the previous match in the current document for the find query you entered last
   * - :code:`focusTree`
     - Open the :guilabel:`Environment` window, and then make the list of files active
   * - :code:`fold`
     - Fold the selected code; if a folded unit is selected, unfold it
   * - :code:`foldall`
     - Fold all possibly foldable elements
   * - :code:`foldOther`
     - Fold all possibly foldable elements, except for the selection scope
   * - :code:`formatcode`
     - Reformat the selected JavaScript code
   * - :code:`formatprefs`
     - Open the :guilabel:`Project Settings` section of the :guilabel:`Preferences` tab to programming language settings
   * - :code:`foursplit`
     - Display a four-pane layout
   * - :code:`golinedown`
     - Go down one line
   * - :code:`golineup`
     - Go up one line
   * - :code:`gotoend`
     - Go to the end of the file
   * - :code:`gotoleft`
     - Go left one space
   * - :code:`gotoline`
     - Show the go to line box
   * - :code:`gotolineend`
     - Go to the end of the current line
   * - :code:`gotolinestart`
     - Go to the start of the current line
   * - :code:`goToNextError`
     - Go to the next error
   * - :code:`gotopagedown`
     - Go down one page
   * - :code:`gotopageup`
     - Go up one page
   * - :code:`gotopanedown`
     - Go one pane down
   * - :code:`gotopaneleft`
     - Go one pane left
   * - :code:`gotopaneright`
     - Go one pane right
   * - :code:`gotopaneup`
     - Go one pane up
   * - :code:`goToPreviousError`
     - Go to the previous error
   * - :code:`gotoright`
     - Go right one space
   * - :code:`gotostart`
     - Go to the start of the file
   * - :code:`gototableft`
     - Go one tab left
   * - :code:`gototabright`
     - Go one tab right
   * - :code:`gotowordleft`
     - Go one word to the left
   * - :code:`gotowordright`
     - Go one word to the right
   * - :code:`hideGotoLine`
     - Hide the go to line box, if it is showing
   * - :code:`hidesearchreplace`
     - Hide the find and replace bar, if it is showing
   * - :code:`hsplit`
     - Split the current pane into two columns, and then move the current tab to the new column
   * - :code:`indent`
     - Indent the selection one tab
   * - :code:`insertstring`
     - Insert a string of text while typing or pasting
   * - :code:`inserttext`
     - Insert text while typing or pasting
   * - :code:`invertSelection`
     - Select everything other than the selection
   * - :code:`joinlines`
     - Remove all line breaks from the current selection
   * - :code:`jumptodef`
     - Go to the definition of the variable or function at the cursor
   * - :code:`jumptomatching`
     - Go to the matching symbol in the current scope
   * - :code:`largerfont`
     - Increase the font size
   * - :code:`maximizeconsole`
     - Expand the console to cover the entire IDE
   * - :code:`modifyNumberDown`
     - Decrease the number to the left of the cursor by 1, if it is a number
   * - :code:`modifyNumberUp`
     - Increase the number to the left of the cursor by 1, if it is a number
   * - :code:`movelinesdown`
     - Move selection down one line
   * - :code:`movelinesup`
     - Move selection up one line
   * - :code:`movetabdown`
     - Move the current tab down one pane, or if the tab is already at the very bottom, create a split
       tab there
   * - :code:`movetableft`
     - Move the current tab left, or if the tab is already at the far left, create a split tab there
   * - :code:`movetabright`
     - Move the current tab right, or if the tab is already at the far right, create a split tab there
   * - :code:`movetabup`
     - Move the current tab up one pane, or if the tab is already at very top, create a split tab there
   * - :code:`navigate`
     - Show the :guilabel:`Navigate` window
   * - :code:`navigate_altkey`
     - Show the :guilabel:`Navigate` window
   * - :code:`newEnvironment`
     - Show the :guilabel:`Create new environment` wizard in the |AC9| console
   * - :code:`newfile`
     - Create a new file
   * - :code:`newfolder`
     - Create a new folder relative to the selection in the :guilabel:`Environment` window
   * - :code:`nextpane`
     - Go to the next pane
   * - :code:`nexttab`
     - Go to the next tab
   * - :code:`nosplit`
     - Combine all split panes into a single pane
   * - :code:`opencoverageview`
     - Show the :guilabel:`Code Coverage` tab
   * - :code:`openpreferences`
     - Show the :guilabel:`Preferences` tab
   * - :code:`opentermhere`
     - Open a :guilabel:`Terminal` tab, and then switch to the parent folder of the selected file in the list of files
   * - :code:`openterminal`
     - Open a new :guilabel:`Terminal` tab
   * - :code:`outdent`
     - Outdent the selection one tab
   * - :code:`outline`
     - Show the :guilabel:`Outline` window
   * - :code:`overwrite`
     - Turn on overwrite mode, or if on, turn off
   * - :code:`pagedown`
     - Go down one page
   * - :code:`pageup`
     - Go up one page
   * - :code:`passKeysToBrowser`
     - Enable keys to be handled by the web browser
   * - :code:`paste`
     - Paste the clipboard's current contents at the cursor
   * - :code:`preview`
     - Show the preview pane
   * - :code:`previouspane`
     - Go to the previous pane
   * - :code:`previoustab`
     - Go to the previous tab
   * - :code:`quickfix`
     - Show suggestions for fixing errors
   * - :code:`redo`
     - Redo the last action
   * - :code:`refocusTab`
     - Go back to the last tab
   * - :code:`reloadpreview`
     - Refresh the preview pane
   * - :code:`removefavorite`
     - Delete the item from the :guilabel:`Favorites` list, if the selection is a favorite
   * - :code:`removeline`
     - Delete the contents of the current line
   * - :code:`removetolineend`
     - Delete from the cursor to the end of the current line
   * - :code:`removetolinestart`
     - Delete from the beginning of the current line up to the cursor
   * - :code:`removewordleft`
     - Delete the word to the left of the cursor
   * - :code:`removewordright`
     - Delete the word to the right of the cursor
   * - :code:`renameVar`
     - Start a rename refactor for the selection
   * - :code:`reopenLastTab`
     - Open the last tab again
   * - :code:`replace`
     - Show the find and replace bar for the current document, with focus on the replace with expression
   * - :code:`replaceall`
     - Replace all matches for :guilabel:`Find` with :guilabel:`Replace With` in the find and replace bar for the current document
   * - :code:`replacenext`
     - Replace the next match for :guilabel:`Find` with :guilabel:`Replace With` in the find and replace bar for the current document
   * - :code:`replaceprevious`
     - Replace the previous match for :guilabel:`Find` with :guilabel:`Replace With` in the find and replace bar for the current document
   * - :code:`replaymacro`
     - Replay previously recorded keystrokes
   * - :code:`rerunInitScript`
     - Rerun your initialization script
   * - :code:`restartc9`
     - Restart the |env|
   * - :code:`restartc9vm`
     - Restart the |env|
   * - :code:`resume`
     - Resume the current paused process
   * - :code:`revealtab`
     - Show the current tab in the file tree
   * - :code:`reverttosaved`
     - Reset the current file to its last saved version
   * - :code:`reverttosavedall`
     - Reset each open file to its saved version
   * - :code:`run`
     - Run or debug the current application
   * - :code:`runlast`
     - Run or debug the last run file
   * - :code:`save`
     - Save the current file to disk
   * - :code:`saveall`
     - Save all unsaved files to disk
   * - :code:`saveas`
     - Save the current file to disk with a different file name
   * - :code:`savePaneLayout`
     - Save the current pane layout in the :guilabel:`Window, Saved Layouts` menu
   * - :code:`savePaneLayoutAndCloseTabs`
     - Save the current pane layout in the :guilabel:`Window, Saved Layouts` menu, and then close all open tabs
   * - :code:`scrolldown`
     - Scroll down in the current document
   * - :code:`scrollPreviewElementIntoView`
     - If a preview page and the related HTML file are both open, scroll the preview page to the location that matches the current element under the cursor in the HTML file
   * - :code:`scrollup`
     - Scroll up in the current document
   * - :code:`searchinfiles`
     - Show the find and replace bar for multiple files
   * - :code:`selectall`
     - Select all selectable content
   * - :code:`selectdown`
     - Include the next line down in the selection
   * - :code:`selectleft`
     - Include the next space to the left in the selection
   * - :code:`selectlineend`
     - Include the rest of the current line in the selection, starting from the cursor
   * - :code:`selectlinestart`
     - Include the beginning of the current line in the selection, up to the cursor
   * - :code:`selectMoreAfter`
     - Include more matching selections that are after the selection
   * - :code:`selectMoreBefore`
     - Include more matching selections that are before the selection
   * - :code:`selectNextAfter`
     - Include the next matching selection that is after the selection
   * - :code:`selectNextBefore`
     - Include the next matching selection that is before the selection
   * - :code:`selectOrFindNext`
     - Select or find the next matching selection
   * - :code:`selectOrFindPrevious`
     - Select or find the previous matching selection
   * - :code:`selectpagedown`
     - Include from the cursor down to the end of the current page in the selection
   * - :code:`selectpageup`
     - Include from the cursor up to the beginning of the current page in the selection
   * - :code:`selectright`
     - Include the next space to the right of the cursor in the selection
   * - :code:`selecttoend`
     - Include from the cursor down to the end of the current file in the selection
   * - :code:`selecttolineend`
     - Include from the cursor to the end of the current line in the selection
   * - :code:`selecttolinestart`
     - Include from the beginning of the current line to the cursor in the selection
   * - :code:`selecttomatching`
     - Include from the cursor to the next matching symbol in the current scope
   * - :code:`selecttostart`
     - Include from the cursor up to the beginning of the current file in the selection
   * - :code:`selectup`
     - Include the next line up in the selection
   * - :code:`selectVar`
     - Select all instances of the variable, if the selection is a variable
   * - :code:`selectwordleft`
     - Include the next word to the left of the cursor in the selection
   * - :code:`selectwordright`
     - Include the next word to the right of the cursor in the selection
   * - :code:`setIndentation`
     - Set the indentation type (spaces or tabs) and length
   * - :code:`showimmediate`
     - Show the :guilabel:`Immediate` tab
   * - :code:`showinstaller`
     - Show the :guilabel:`AWS Cloud9 Installer` dialog box
   * - :code:`showoutput`
     - Show the :guilabel:`Output` tab
   * - :code:`showprocesslist`
     - Show the :guilabel:`Process List` dialog box
   * - :code:`showSettingsMenu`
     - Show the :guilabel:`Preferences` tab
   * - :code:`singleSelection`
     - Clear all previous selections
   * - :code:`smallerfont`
     - Decrease the font size
   * - :code:`sortlines`
     - If multiple lines are selected, rearrange them into a sorted order
   * - :code:`splitIntoLines`
     - Add a cursor at the end of the current line
   * - :code:`splitline`
     - Move the contents of the cursor to the end of the line, to its own line
   * - :code:`stepinto`
     - Step into the function that is next on the stack
   * - :code:`stepout`
     - Step out of the current function scope
   * - :code:`stepover`
     - Step over the current expression on the stack
   * - :code:`stop`
     - Stop running or debugging the current application
   * - :code:`stopbuild`
     - Stop building the current file
   * - :code:`stripws`
     - Remove whitespace from the end of each line
   * - :code:`suspend`
     - Suspend running or debugging the current application
   * - :code:`switchterminal`
     - Switch between the editor and the :guilabel:`Terminal` tab
   * - :code:`syntax`
     - Set the syntax type
   * - :code:`tab0`
     - Go to the tenth tab
   * - :code:`tab1`
     - Go to the first tab
   * - :code:`tab2`
     - Go to the second tab
   * - :code:`tab3`
     - Go to the third tab
   * - :code:`tab4`
     - Go to the fourth tab
   * - :code:`tab5`
     - Go to the fifth tab
   * - :code:`tab6`
     - Go to the sixth tab
   * - :code:`tab7`
     - Go to the seventh tab
   * - :code:`tab8`
     - Go to the eighth tab
   * - :code:`tab9`
     - Go to the ninth tab
   * - :code:`term_detach`
     - Detach clients attached to the :guilabel:`Terminal` pane
   * - :code:`term_help`
     - Show help for the :guilabel:`Terminal` pane
   * - :code:`term_restart`
     - Restart the :guilabel:`Terminal` pane
   * - :code:`threeleft`
     - Create a three-pane layout with two panes on the left and one pane on the right
   * - :code:`threeright`
     - Create a three-pane layout with two panes on the right and one pane on the left
   * - :code:`toggle_term_status`
     - Show :guilabel:`Terminal` pane status, or hide if shown
   * - :code:`toggleBlockComment`
     - Surround the selection with block comment characters, or remove them if they are there
   * - :code:`toggleButtons`
     - Show tabs, or hide if shown
   * - :code:`togglecomment`
     - Add line comment characters at the start of each selected line, or remove them if they are there
   * - :code:`toggleconsole`
     - Show the :guilabel:`Console` window if hidden, or hide if shown
   * - :code:`toggledebugger`
     - Show the :guilabel:`Debugger` window, or hide if shown
   * - :code:`toggleFoldWidget`
     - Fold code, or remove code folding if it is there
   * - :code:`toggleMenubar`
     - Show the menu bar, or hide if shown
   * - :code:`toggleOpenfiles`
     - Show the :guilabel:`Open Files` list in the :guilabel:`Environment` window, or hide if shown
   * - :code:`toggleParentFoldWidget`
     - Fold parent code, or remove folding if it is there
   * - :code:`togglerecording`
     - Start keystroke recording, or stop if it is already recording
   * - :code:`toggletree`
     - Show the :guilabel:`Environment` window if hidden, or hide if shown
   * - :code:`toggleWordWrap`
     - Wrap words, or stop wrapping words if they are already wrapping
   * - :code:`tolowercase`
     - Change the selection to all lowercase
   * - :code:`touppercase`
     - Change the selection to all uppercase
   * - :code:`transposeletters`
     - Transpose the selection
   * - :code:`trimTrailingSpace`
     - Trim whitespace at the ends of lines
   * - :code:`twohsplit`
     - Create a two-pane layout, with panes side by side
   * - :code:`twovsplit`
     - Create a two-pane layout, with panes top and bottom
   * - :code:`undo`
     - Undo the last action
   * - :code:`unfold`
     - Unfold selected code
   * - :code:`unfoldall`
     - Unfold code folding for the entire file
   * - :code:`vsplit`
     - Split the current pane into two panes, top and bottom, and move the current tab to the top pane
