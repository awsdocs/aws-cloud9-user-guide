.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _keybindings-emacs-windows-linux:

#####################################################################
Windows / Linux Emacs Keybindings Reference for the |AC9IDElongtitle|
#####################################################################

.. meta::
    :description:
        Provides a list of Emacs keyboard mode keybindings for Windows / Linux operating systems in the AWS Cloud9 IDE.

Following is a list of Emacs keyboard mode keybindings for Windows / Linux operating systems in the |AC9IDE|.

For more information, in the |AC9IDE|:

#. On the menu bar, choose :menuselection:`AWS Cloud9, Preferences`.
#. On the :guilabel:`Preferences` tab, choose :guilabel:`Keybindings`.
#. For :guilabel:`Keyboard Mode`, choose :guilabel:`Emacs`.
#. For :guilabel:`Operating System`, choose :guilabel:`Windows / Linux`.

See also :doc:`Working with Keybindings <settings-keybindings>`.

* :ref:`keybindings-emacs-windows-linux-general`
* :ref:`keybindings-emacs-windows-linux-tabs`
* :ref:`keybindings-emacs-windows-linux-panels`
* :ref:`keybindings-emacs-windows-linux-code-editor`
* :ref:`keybindings-emacs-windows-linux-emmet`
* :ref:`keybindings-emacs-windows-linux-terminal`
* :ref:`keybindings-emacs-windows-linux-run-debug`

.. _keybindings-emacs-windows-linux-general:

General
=======

.. list-table::
   :widths: 2 1 1
   :header-rows: 1

   * - Description
     - Keybinding
     - Command
   * - Add the selection as a watch expression
     - :kbd:`Ctrl-Shift-C`
     - :code:`addwatchfromselection`
   * - Remove the cut selection from the clipboard
     - :kbd:`Esc`
     - :code:`clearcut`
   * - Show the code completion context menu
     - :kbd:`Ctrl-Space` | :kbd:`Alt-Space`
     - :code:`complete`
   * - Code complete, and then overwrite
     - :kbd:`Ctrl-Shift-Space` | :kbd:`Alt-Shift-Space`
     - :code:`completeoverwrite`
   * - Copy the selection to the clipboard
     - :kbd:`Ctrl-C`
     - :code:`copy`
   * - Cut the selection to the clipboard
     - :kbd:`Ctrl-X`
     - :code:`cut`
   * - Expand code, where applicable
     - :kbd:`Tab`
     - :code:`expandSnippet`
   * - Show the find and replace bar for the current document
     - :kbd:`Ctrl-F`
     - :code:`find`
   * - Select all find matches in the current document
     - :kbd:`Ctrl-Alt-K`
     - :code:`findall`
   * - Go to the next match in the current document for the find query you entered last
     - :kbd:`Ctrl-K`
     - :code:`findnext`
   * - Go to the previous match in the current document for the find query you entered last
     - :kbd:`Ctrl-Shift-K`
     - :code:`findprevious`
   * - Display all known references to the symbol at the insertion point in the active file in the editor
     - :kbd:`Shift-F3`
     - :code:`findReferences`
   * - Open the :guilabel:`Environment` window, and then make the list of files active
     - :kbd:`Shift-Esc`
     - :code:`focusTree`
   * - Reformat the selected JavaScript code
     - :kbd:`Ctrl-Shift-B`
     - :code:`formatcode`
   * - Show the go to line box
     - :kbd:`Ctrl-G`
     - :code:`gotoline`
   * - Hide the find and replace bar, if it is showing
     - :kbd:`Esc`
     - :code:`hidesearchreplace`
   * - Go to the definition of the variable or function at the cursor
     - :kbd:`F3`
     - :code:`jumptodef`
   * - If a local |LAM| function is selected in the :guilabel:`Lambda` section of the :guilabel:`AWS Resources` window, attempts to upload the function to |LAM| as a remote function
     - :kbd:`Ctrl-Shift-U`
     - :code:`lambdaUploadFunction`
   * - Create a new file
     - :kbd:`Alt-N`
     - :code:`newfile`
   * - Show the :guilabel:`Preferences` tab
     - :kbd:`Ctrl-,`
     - :code:`openpreferences`
   * - Open a :guilabel:`Terminal` tab, and then switch to the parent folder of the selected file in the list of files
     - :kbd:`Alt-L`
     - :code:`opentermhere`
   * - Paste the clipboard's current contents at the cursor
     - :kbd:`Ctrl-V`
     - :code:`paste`
   * - Show suggestions for fixing errors
     - :kbd:`Ctrl-F3`
     - :code:`quickfix`
   * - Redo the last action
     - :kbd:`Ctrl-Shift-Z` | :kbd:`Ctrl-Y`
     - :code:`redo`
   * - Refresh the preview pane
     - :kbd:`Ctrl-Enter`
     - :code:`reloadpreview`
   * - Start a rename refactor for the selection
     - :kbd:`Ctrl-Alt-R`
     - :code:`renameVar`
   * - Show the find and replace bar for the current document, with focus on the replace with expression
     - :kbd:`Alt-Shift-F` | :kbd:`Ctrl-H`
     - :code:`replace`
   * - Rerun your initialization script
     - :kbd:`Ctrl-Enter`
     - :code:`rerunInitScript`
   * - Restart the |env|
     - :kbd:`Ctrl-R`
     - :code:`restartc9`
   * - Reset the current file to its last saved version
     - :kbd:`Ctrl-Shift-Q`
     - :code:`reverttosaved`
   * - Reset each open file to its saved version
     - :kbd:`Alt-Shift-Q`
     - :code:`reverttosavedall`
   * - Save the current file to disk
     - :kbd:`Ctrl-S`
     - :code:`save`
   * - Save the current file to disk with a different file name
     - :kbd:`Ctrl-Shift-S`
     - :code:`saveas`
   * - Show the find and replace bar for multiple files
     - :kbd:`Ctrl-Shift-F`
     - :code:`searchinfiles`
   * - Show the :guilabel:`Process List` dialog box
     - :kbd:`Ctrl-Alt-P`
     - :code:`showprocesslist`
   * - Undo the last action
     - :kbd:`Ctrl-Z`
     - :code:`undo`

.. _keybindings-emacs-windows-linux-tabs:

Tabs
====

.. list-table::
   :widths: 2 1 1
   :header-rows: 1

   * - Description
     - Keybinding
     - Command
   * - Close all open tabs in the current pane, except the current tab
     - :kbd:`Ctrl-Alt-W`
     - :code:`closeallbutme`
   * - Close all open tabs in all panes
     - :kbd:`Alt-Shift-W`
     - :code:`closealltabs`
   * - Close the current pane
     - :kbd:`Ctrl-W`
     - :code:`closepane`
   * - Close the current tab
     - :kbd:`Alt-W`
     - :code:`closetab`
   * - Go one pane down
     - :kbd:`Ctrl-Meta-Down`
     - :code:`gotopanedown`
   * - Go one pane left
     - :kbd:`Ctrl-Meta-Left`
     - :code:`gotopaneleft`
   * - Go one pane right
     - :kbd:`Ctrl-Meta-Right`
     - :code:`gotopaneright`
   * - Go one pane up
     - :kbd:`Ctrl-Meta-Up`
     - :code:`gottopaneup`
   * - Go one tab left
     - :kbd:`Ctrl-[`
     - :code:`gototableft`
   * - Go one tab right
     - :kbd:`Ctrl-]`
     - :code:`gototabright`
   * - Move the current tab down one pane, or if the tab is already at the very bottom, create a split
       tab there
     - :kbd:`Ctrl-Meta-Down`
     - :code:`movetabdown`
   * - Move the current tab left, or if the tab is already at the far left, create a split tab there
     - :kbd:`Ctrl-Meta-Left`
     - :code:`movetableft`
   * - Move the current tab right, or if the tab is already at the far right, create a split tab there
     - :kbd:`Ctrl-Meta-Right`
     - :code:`movetabright`
   * - Move the current tab up one pane, or if the tab is already at the very top, create a split tab
       there
     - :kbd:`Ctrl-Meta-Up`
     - :code:`movetabup`
   * - Go to the next pane
     - :kbd:`Ctrl-\``
     - :code:`nextpane`
   * - Go to the next tab
     - :kbd:`Ctrl-Tab | Alt-\``
     - :code:`nexttab`
   * - Go to the previous pane
     - :kbd:`Ctrl-Shift-\``
     - :code:`previouspane`
   * - Go to the previous tab
     - :kbd:`Ctrl-Shift-Tab | Alt-Shift-\``
     - :code:`previoustab`
   * - Go back to the last tab
     - :kbd:`Esc`
     - :code:`refocusTab`
   * - Open the last tab again
     - :kbd:`Alt-Shift-T`
     - :code:`reopenLastTab`
   * - Show the current tab in the file tree
     - :kbd:`Ctrl-Shift-L`
     - :code:`revealtab`
   * - Go to the tenth tab
     - :kbd:`Ctrl-0`
     - :code:`tab0`
   * - Go to the first tab
     - :kbd:`Ctrl-1`
     - :code:`tab1`
   * - Go to the second tab
     - :kbd:`Ctrl-2`
     - :code:`tab2`
   * - Go to the third tab
     - :kbd:`Ctrl-3`
     - :code:`tab3`
   * - Go to the fourth tab
     - :kbd:`Ctrl-4`
     - :code:`tab4`
   * - Go to the fifth tab
     - :kbd:`Ctrl-5`
     - :code:`tab5`
   * - Go to the sixth tab
     - :kbd:`Ctrl-6`
     - :code:`tab6`
   * - Go to the seventh tab
     - :kbd:`Ctrl-7`
     - :code:`tab7`
   * - Go to the eighth tab
     - :kbd:`Ctrl-8`
     - :code:`tab8`
   * - Go to the ninth tab
     - :kbd:`Ctrl-9`
     - :code:`tab9`

.. _keybindings-emacs-windows-linux-panels:

Panels
======

.. list-table::
   :widths: 2 1 1
   :header-rows: 1

   * - Description
     - Keybinding
     - Command
   * - Show the :guilabel:`Go` window in :guilabel:`Go to Anything` mode
     - :kbd:`Ctrl-E|Ctrl-P`
     - :code:`gotoanything`
   * - Show the :guilabel:`Go` window in :guilabel:`Go to Command` mode
     - :kbd:`Ctrl-.`
     - :code:`gotocommand`
   * - Show the :guilabel:`Go` window in :guilabel:`Go to File` mode.
     - :kbd:`Ctrl-O`
     - :code:`gotofile`
   * - Show the :guilabel:`Go` window in :guilabel:`Go to Symbol` mode.
     - :kbd:`Ctrl-Shift-O`
     - :code:`gotosymbol`
   * - Show the :guilabel:`Outline` window
     - :kbd:`Ctrl-Shift-E`
     - :code:`outline`
   * - Show the :guilabel:`Console` window if hidden, or hide if shown
     - :kbd:`F6`
     - :code:`toggleconsole`
   * - Show the :guilabel:`Environment` window if hidden, or hide if shown
     - :kbd:`Ctrl-I`
     - :code:`toggletree`

.. _keybindings-emacs-windows-linux-code-editor:

Code Editor
===========

.. list-table::
   :widths: 2 1 1
   :header-rows: 1

   * - Description
     - Keybinding
     - Command
   * - Add a cursor one line above the active cursor, or if a cursor is already added, add another cursor
       above that one
     - :kbd:`Ctrl-Alt-Up`
     - :code:`addCursorAbove`
   * - Add a second cursor one line above the active cursor, or if a second cursor is already added, move
       the second cursor up one line
     - :kbd:`Ctrl-Alt-Shift-Up`
     - :code:`addCursorAboveSkipCurrent`
   * - Add a cursor one line below the active cursor, or if a cursor is already added, add another cursor
       below that one
     - :kbd:`Ctrl-Alt-Down`
     - :code:`addCursorBelow`
   * - Add a second cursor one line below the active cursor, or if a second cursor is already added, move
       the second cursor down one line
     - :kbd:`Ctrl-Alt-Shift-Down`
     - :code:`addCursorBelowSkipCurrent`
   * - Move all cursors to the same space as the active cursor on each of their lines, if they are misaligned
     - :kbd:`Ctrl-Alt-A`
     - :code:`alignCursors`
   * - Backspace one space
     - :kbd:`Shift-Backspace | Backspace`
     - :code:`backspace`
   * - Indent the selection one tab
     - :kbd:`Ctrl-]`
     - :code:`blockindent`
   * - Outdent the selection one tab
     - :kbd:`Ctrl-[`
     - :code:`blockoutdent`
   * - Control whether focus can be switched from the editor to somewhere else in the IDE
     - :kbd:`Ctrl-Z | Ctrl-Shift-Z | Ctrl-Y`
     - :code:`cancelBrowserUndoInAce`
   * - Copy the contents of the line, and paste the copied contents one line down
     - :kbd:`Alt-Shift-Down`
     - :code:`copylinesdown`
   * - Copy the contents of the line, and paste the copied contents one line up
     - :kbd:`Alt-Shift-Up`
     - :code:`copylinesup`
   * - Cut the selection, or if there is no selection, delete one space
     - :kbd:`Shift-Delete`
     - :code:`cut_or_delete`
   * - Delete one space
     - :kbd:`Delete`
     - :code:`del`
   * - Copy the contents of the selection, and paste the copied contents immediately after the selection
     - :kbd:`Ctrl-Shift-D`
     - :code:`duplicateSelection`
   * - Include the current line's contents in the selection
     - :kbd:`Ctrl-Shift-L`
     - :code:`expandtoline`
   * - Include up to the next matching symbol in selection
     - :kbd:`Ctrl-Shift-M`
     - :code:`expandToMatching`
   * - Fold the selected code; if a folded unit is selected, unfold it
     - :kbd:`Alt-L | Ctrl-F1`
     - :code:`fold`
   * - Fold all possibly foldable elements, except for the current selection scope
     - :kbd:`Alt-0`
     - :code:`foldOther`
   * - Go down one line
     - :kbd:`Down`
     - :code:`golinedown`
   * - Go up one line
     - :kbd:`Up`
     - :code:`golineup`
   * - Go to the end of the file
     - :kbd:`Ctrl-End`
     - :code:`gotoend`
   * - Go left one space
     - :kbd:`Left`
     - :code:`gotoleft`
   * - Go to the end of the current line
     - :kbd:`Alt-Right | End`
     - :code:`gotolineend`
   * - Go to the start of the current line
     - :kbd:`Alt-Left | Home`
     - :code:`gotolinestart`
   * - Go to the next error
     - :kbd:`Alt-E`
     - :code:`goToNextError`
   * - Go down one page
     - :kbd:`Page Down`
     - :code:`gotopagedown`
   * - Go up one page
     - :kbd:`Page Up`
     - :code:`gotopageup`
   * - Go to the previous error
     - :kbd:`Alt-Shift-E`
     - :code:`goToPreviousError`
   * - Go right one space
     - :kbd:`Right`
     - :code:`gotoright`
   * - Go to the start of the file
     - :kbd:`Ctrl-Home`
     - :code:`gotostart`
   * - Go one word to the left
     - :kbd:`Ctrl-Left`
     - :code:`gotowordleft`
   * - Go one word to the right
     - :kbd:`Ctrl-Right`
     - :code:`gotowordright`
   * - Indent the selection one tab
     - :kbd:`Tab`
     - :code:`indent`
   * - Go to the matching symbol in the current scope
     - :kbd:`Ctrl-P`
     - :code:`jumptomatching`
   * - Increase the font size
     - :kbd:`Ctrl-+ | Ctrl-=`
     - :code:`largerfont`
   * - Decrease the number to the left of the cursor by 1, if it is a number
     - :kbd:`Ctrl-Shift-Down`
     - :code:`modifyNumberDown`
   * - Increase the number to the left of the cursor by 1, if it is a number
     - :kbd:`Ctrl-Shift-Up`
     - :code:`modifyNumberUp`
   * - Move selection down one line
     - :kbd:`Alt-Down`
     - :code:`movelinesdown`
   * - Move selection up one line
     - :kbd:`Alt-Up`
     - :code:`movelinesup`
   * - Outdent the selection one tab
     - :kbd:`Shift-Tab`
     - :code:`outdent`
   * - Turn on overwrite mode, or if on, turn off
     - :kbd:`Insert`
     - :code:`overwrite`
   * - Delete the contents of the current line
     - :kbd:`Ctrl-D`
     - :code:`removeline`
   * - Delete from the cursor to the end of the current line
     - :kbd:`Alt-Delete`
     - :code:`removetolineend`
   * - Delete from the beginning of the current line up to the cursor
     - :kbd:`Alt-Backspace`
     - :code:`removetolinestart`
   * - Delete the word to the left of the cursor
     - :kbd:`Ctrl-Backspace`
     - :code:`removewordleft`
   * - Delete the word to the right of the cursor
     - :kbd:`Ctrl-Delete`
     - :code:`removewordright`
   * - Replay previously recorded keystrokes
     - :kbd:`Ctrl-Shift-E`
     - :code:`replaymacro`
   * - Scroll the current file down by one line
     - :kbd:`Ctrl-Down`
     - :code:`scrolldown`
   * - Scroll the current file up by one line
     - :kbd:`Ctrl-Up`
     - :code:`scrollup`
   * - Select all selectable content
     - :kbd:`Ctrl-A`
     - :code:`selectall`
   * - Include the next line down in the selection
     - :kbd:`Shift-Down`
     - :code:`selectdown`
   * - Include the next space left in the selection
     - :kbd:`Shift-Left`
     - :code:`selectleft`
   * - Include the rest of the current line in the selection, starting from the cursor
     - :kbd:`Shift-End`
     - :code:`selectlineend`
   * - Include the beginning of the current line in the selection, up to the cursor
     - :kbd:`Shift-Home`
     - :code:`selectlinestart`
   * - Include more matching selections that are after the selection
     - :kbd:`Ctrl-Alt-Right`
     - :code:`selectMoreAfter`
   * - Include more matching selections that are before the selection
     - :kbd:`Ctrl-Alt-Left`
     - :code:`selectMoreBefore`
   * - Include the next matching selection that is after the selection
     - :kbd:`Ctrl-Alt-Shift-Right`
     - :code:`selectNextAfter`
   * - Include the next matching selection that is before the selection
     - :kbd:`Ctrl-Alt-Shift-Left`
     - :code:`selectNextBefore`
   * - Select or find the next matching selection
     - :kbd:`Alt-K`
     - :code:`selectOrFindNext`
   * - Select or find the previous matching selection
     - :kbd:`Alt-Shift-K`
     - :code:`selectOrFindPrevious`
   * - Include from the cursor down to the end of the current page in the selection
     - :kbd:`Shift-Page Down`
     - :code:`selectpagedown`
   * - Include from the cursor up to the beginning of the current page in the selection
     - :kbd:`Shift-Page Up`
     - :code:`selectpageup`
   * - Include the next space to the right of the cursor in the selection
     - :kbd:`Shift-Right`
     - :code:`selectright`
   * - Include from the cursor down to the end of the current file in the selection
     - :kbd:`Ctrl-Shift-End`
     - :code:`selecttoend`
   * - Include from the cursor to the end of the current line in the selection
     - :kbd:`Alt-Shift-Right`
     - :code:`selecttolineend`
   * - Include from the beginning of the current line to the cursor in the selection
     - :kbd:`Alt-Shift-Left`
     - :code:`selecttolinestart`
   * - Include from the cursor to the next matching symbol in the current scope
     - :kbd:`Ctrl-Shift-P`
     - :code:`selecttomatching`
   * - Include from the cursor up to the beginning of the current file in the selection
     - :kbd:`Ctrl-Shift-Home`
     - :code:`selecttostart`
   * - Include the next line up in the selection
     - :kbd:`Shift-Up`
     - :code:`selectup`
   * - Include the next word to the left of the cursor in the selection
     - :kbd:`Ctrl-Shift-Left`
     - :code:`selectwordleft`
   * - Include the next word to the right of the cursor in the selection
     - :kbd:`Ctrl-Shift-Right`
     - :code:`selectwordright`
   * - Show the :guilabel:`Preferences` tab
     - :kbd:`Ctrl-,`
     - :code:`showSettingsMenu`
   * - Clear all previous selections
     - :kbd:`Esc`
     - :code:`singleSelection`
   * - Decrease the font size
     - :kbd:`Ctrl--`
     - :code:`smallerfont`
   * - If multiple lines are selected, rearrange them into a sorted order
     - :kbd:`Ctrl-Alt-S`
     - :code:`sortlines`
   * - Add a cursor at the end of the current line
     - :kbd:`Ctrl-Alt-L`
     - :code:`splitIntoLines`
   * - Move the contents of the cursor to the end of the line, to its own line
     - :kbd:`Ctrl-O`
     - :code:`splitline`
   * - Surround the selection with block comment characters, or remove them if they are there
     - :kbd:`Ctrl-Shift-/`
     - :code:`toggleBlockComment`
   * - Add line comment characters at the start of each selected line, or remove them if they are there
     - :kbd:`Ctrl-/`
     - :code:`togglecomment`
   * - Fold code, or remove code folding if it is there
     - :kbd:`F2`
     - :code:`toggleFoldWidget`
   * - Fold parent code, or remove folding if it is there
     - :kbd:`Alt-F2`
     - :code:`toggleParentFoldWidget`
   * - Start keystroke recording, or stop if it is already recording
     - :kbd:`Ctrl-Alt-E`
     - :code:`togglerecording`
   * - Wrap words, or stop wrapping words if they are already wrapping
     - :kbd:`Ctrl-Q`
     - :code:`toggleWordWrap`
   * - Change the selection to all lowercase
     - :kbd:`Ctrl-Shift-U`
     - :code:`tolowercase`
   * - Change the selection to all uppercase
     - :kbd:`Ctrl-U`
     - :code:`touppercase`
   * - Transpose the selection
     - :kbd:`Alt-X`
     - :code:`transposeletters`
   * - Unfold the selected code
     - :kbd:`Alt-Shift-L | Ctrl-Shift-F1`
     - :code:`unfold`
   * - Unfold code folding for the entire file
     - :kbd:`Alt-Shift-0`
     - :code:`unfoldall`

.. _keybindings-emacs-windows-linux-emmet:

emmet
=====

.. list-table::
   :widths: 2 1 1
   :header-rows: 1

   * - Description
     - Keybinding
     - Command
   * - Evaluate a simple math expression (such as :code:`2*4` or :code:`10/2`), and output its result
     - :kbd:`Shift-Ctrl-Y`
     - :code:`emmet_evaluate_math_expression`
   * - Expand CSS-like abbreviations into HTML, XML, or CSS code, depending on the current file's syntax
     - :kbd:`Ctrl-Alt-E`
     - :code:`emmet_expand_abbreviation`
   * - Traverse expanded CSS-like abbreviations, by tab stop
     - :kbd:`Tab`
     - :code:`emmet_expand_abbreviation_with_tab`
   * - Go to the next editable code part
     - :kbd:`Shift-Ctrl-.`
     - :code:`emmet_select_next_item`
   * - Go to the previous editable code part
     - :kbd:`Shift-Ctrl-,`
     - :code:`emmet_select_previous_item`
   * - Expand an abbreviation, and then place the current selection within the last element of the generated snippet
     - :kbd:`Shift-Ctrl-A`
     - :code:`emmet_wrap_with_abbreviation`

.. _keybindings-emacs-windows-linux-terminal:

Terminal
========

.. list-table::
   :widths: 2 1 1
   :header-rows: 1

   * - Description
     - Keybinding
     - Command
   * - Open a new :guilabel:`Terminal` tab
     - :kbd:`Alt-T`
     - :code:`openterminal`
   * - Switch between the editor and the :guilabel:`Terminal` tab
     - :kbd:`Alt-S`
     - :code:`switchterminal`

.. _keybindings-emacs-windows-linux-run-debug:

Run and Debug
=============

.. list-table::
   :widths: 2 1 1
   :header-rows: 1

   * - Description
     - Keybinding
     - Command
   * - Build the current file
     - :kbd:`Ctrl-B`
     - :code:`build`
   * - Resume the current paused process
     - :kbd:`F8`
     - :code:`resume`
   * - Run or debug the current application
     - :kbd:`Alt-F5`
     - :code:`run`
   * - Run or debug the last run file
     - :kbd:`F5`
     - :code:`runlast`
   * - Step into the function that is next on the stack
     - :kbd:`F11`
     - :code:`stepinto`
   * - Step out of the current function scope
     - :kbd:`Shift-F11`
     - :code:`stepout`
   * - Step over the current expression on the stack
     - :kbd:`F10`
     - :code:`stepover`
   * - Stop running or debugging the current application
     - :kbd:`Shift-F5`
     - :code:`stop`
   * - Stop building the current file
     - :kbd:`Ctrl-Shift-C`
     - :code:`stopbuild`
