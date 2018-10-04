.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _keybindings-emacs-apple-osx:

###########################################################
MacOS Emacs Keybindings Reference for the |AC9IDElongtitle|
###########################################################

.. meta::
    :description:
        Provides a list of Emacs keyboard mode keybindings for MacOS operating systems in the AWS Cloud9 IDE.

Following is a list of Emacs keyboard mode keybindings for MacOS operating systems in the |AC9IDE|.

For more information, in the |AC9IDE|:

#. On the menu bar, choose :menuselection:`AWS Cloud9, Preferences`.
#. On the :guilabel:`Preferences` tab, choose :guilabel:`Keybindings`.
#. For :guilabel:`Keyboard Mode`, choose :guilabel:`Emacs`.
#. For :guilabel:`Operating System`, choose :guilabel:`MacOS`.

See also :doc:`Working with Keybindings <settings-keybindings>`.

* :ref:`keybindings-emacs-apple-osx-general`
* :ref:`keybindings-emacs-apple-osx-tabs`
* :ref:`keybindings-emacs-apple-osx-panels`
* :ref:`keybindings-emacs-apple-osx-code-editor`
* :ref:`keybindings-emacs-apple-osx-emmet`
* :ref:`keybindings-emacs-apple-osx-terminal`
* :ref:`keybindings-emacs-apple-osx-run-debug`

.. _keybindings-emacs-apple-osx-general:

General
=======

.. list-table::
   :widths: 2 1 1
   :header-rows: 1

   * - Description
     - Keybinding
     - Command
   * - Add the selection as a watch expression
     - :kbd:`Command-Shift-C`
     - :code:`addwatchfromselection`
   * - Remove the cut selection from the clipboard
     - :kbd:`Esc`
     - :code:`clearcut`
   * - Show the code completion context menu
     - :kbd:`Control-Space` | :kbd:`Option-Space`
     - :code:`complete`
   * - Complete code, and then overwrite
     - :kbd:`Control-Shift-Space` | :kbd:`Option-Shift-Space`
     - :code:`completeoverwrite`
   * - Copy the selection to the clipboard
     - :kbd:`Command-C`
     - :code:`copy`
   * - Cut the selection to the clipboard
     - :kbd:`Command-X`
     - :code:`cut`
   * - Expand code, where applicable
     - :kbd:`Tab`
     - :code:`expandSnippet`
   * - Show the find and replace bar for the current document
     - :kbd:`Command-F`
     - :code:`find`
   * - Select all find matches in the current document
     - :kbd:`Control-Option-G`
     - :code:`findAll`
   * - Go to the next match in the current document for the find query you entered last
     - :kbd:`Command-G`
     - :code:`findnext`
   * - Go to the previous match in the current document for the find query you entered last
     - :kbd:`Command-Shift-G`
     - :code:`findprevious`
   * - Display all known references to the symbol at the insertion point in the active file in the editor
     - :kbd:`Shift-F3`
     - :code:`findReferences`
   * - Open the :guilabel:`Environment` window, and then make the list of files active
     - :kbd:`Shift-Esc`
     - :code:`focusTree`
   * - Reformat the selected JavaScript code
     - :kbd:`Command-Shift-B`
     - :code:`formatcode`
   * - Show the *go to line* box
     - :kbd:`Command-L`
     - :code:`gotoline`
   * - Hide the find and replace bar, if shown
     - :kbd:`Esc`
     - :code:`hidesearchreplace`
   * - Go to the definition of the variable or function at the cursor
     - :kbd:`F3`
     - :code:`jumptodef`
   * - If a local |LAM| function is selected in the :guilabel:`Lambda` section of the :guilabel:`AWS Resources` window, attempts to upload the function to |LAM| as a remote function
     - :kbd:`Command-Shift-U`
     - :code:`lambdaUploadFunction`
   * - Create a new file
     - :kbd:`Control-N`
     - :code:`newfile`
   * - Show the :guilabel:`Preferences` tab
     - :kbd:`Command-,`
     - :code:`openpreferences`
   * - Open a :guilabel:`Terminal` tab, then switch to the parent folder of the selected file in the list of files
     - :kbd:`Command-Option-L`
     - :code:`opentermhere`
   * - Paste the clipboard's current contents at the cursor
     - :kbd:`Command-V`
     - :code:`paste`
   * - Show suggestions for fixing errors
     - :kbd:`Command-F3`
     - :code:`quickfix`
   * - Redo the last action
     - :kbd:`Command-Shift-Z` | :kbd:`Command-Y`
     - :code:`redo`
   * - Refresh the preview pane
     - :kbd:`Command-Enter`
     - :code:`reloadpreview`
   * - Start a rename refactor for the selection
     - :kbd:`Option-Command-R`
     - :code:`renameVar`
   * - Show the find and replace bar for the current document, with focus on the *replace with* expression
     - :kbd:`Option-Command-F`
     - :code:`replace`
   * - Rerun your initialization script
     - :kbd:`Command-Enter`
     - :code:`rerunInitScript`
   * - Restart the |env|
     - :kbd:`Command-R`
     - :code:`restartc9`
   * - Reset the current file to its last saved version
     - :kbd:`Control-Shift-Q`
     - :code:`reverttosaved`
   * - Reset each open file to its saved version
     - :kbd:`Option-Shift-Q`
     - :code:`reverttosavedall`
   * - Save the current file to disk
     - :kbd:`Command-S`
     - :code:`save`
   * - Save the current file to disk with a different file name
     - :kbd:`Command-Shift-S`
     - :code:`saveas`
   * - Show the find and replace bar for multiple files
     - :kbd:`Shift-Command-F`
     - :code:`searchinfiles`
   * - Show the :guilabel:`Process List` dialog box
     - :kbd:`Command-Option-P`
     - :code:`showprocesslist`
   * - Undo the last action
     - :kbd:`Command-Z`
     - :code:`undo`

.. _keybindings-emacs-apple-osx-tabs:

Tabs
====

.. list-table::
   :widths: 2 1 1
   :header-rows: 1

   * - Description
     - Keybinding
     - Command
   * - Close all open tabs in the current pane, except the current tab
     - :kbd:`Option-Control-W`
     - :code:`closeallbutme`
   * - Close all open tabs in all panes
     - :kbd:`Option-Shift-W`
     - :code:`closealltabs`
   * - Close the current pane
     - :kbd:`Command-Control-W`
     - :code:`closepane`
   * - Close the current tab
     - :kbd:`Option-W`
     - :code:`closetab`
   * - Go one pane down
     - :kbd:`Control-Command-Down`
     - :code:`gotopanedown`
   * - Go one pane left
     - :kbd:`Control-Command-Left`
     - :code:`gotopaneleft`
   * - Go one pane right
     - :kbd:`Control-Command-Right`
     - :code:`gotopaneright`
   * - Go one pane up
     - :kbd:`Control-Command-Up`
     - :code:`gottopaneup`
   * - Go one tab left
     - :kbd:`Command-[`
     - :code:`gototableft`
   * - Go one tab right
     - :kbd:`Command-]`
     - :code:`gototabright`
   * - Move the current tab down one pane, or if the tab is already at the very bottom, create a split
       tab there
     - :kbd:`Command-Option-Shift-Down`
     - :code:`movetabdown`
   * - Move the current tab left, or if the tab is already at the far left, create a split tab there
     - :kbd:`Command-Option-Shift-Left`
     - :code:`movetableft`
   * - Move the current tab right, or if the tab is already at the far right, create a split tab there
     - :kbd:`Command-Option-Shift-Right`
     - :code:`movetabright`
   * - Move the current tab up one pane, or if the tab is already at the very top, create a split tab
       there
     - :kbd:`Command-Option-Shift-Up`
     - :code:`movetabup`
   * - Go to the next pane
     - :kbd:`Option-Esc`
     - :code:`nextpane`
   * - Go to the next tab
     - :kbd:`Option-Tab`
     - :code:`nexttab`
   * - Go to the previous pane
     - :kbd:`Option-Shift-Esc`
     - :code:`previouspane`
   * - Go to the previous tab
     - :kbd:`Option-Shift-Tab`
     - :code:`previoustab`
   * - Go back to the last tab
     - :kbd:`Esc`
     - :code:`refocusTab`
   * - Open the last tab again
     - :kbd:`Option-Shift-T`
     - :code:`reopenLastTab`
   * - Show the current tab in the file tree
     - :kbd:`Command-Shift-L`
     - :code:`revealtab`
   * - Go to the tenth tab
     - :kbd:`Command-0`
     - :code:`tab0`
   * - Go to the first tab
     - :kbd:`Command-1`
     - :code:`tab1`
   * - Go to the second tab
     - :kbd:`Command-2`
     - :code:`tab2`
   * - Go to the third tab
     - :kbd:`Command-3`
     - :code:`tab3`
   * - Go to the fourth tab
     - :kbd:`Command-4`
     - :code:`tab4`
   * - Go to the fifth tab
     - :kbd:`Command-5`
     - :code:`tab5`
   * - Go to the sixth tab
     - :kbd:`Command-6`
     - :code:`tab6`
   * - Go to the seventh tab
     - :kbd:`Command-7`
     - :code:`tab7`
   * - Go to the eighth tab
     - :kbd:`Command-8`
     - :code:`tab8`
   * - Go to the ninth tab
     - :kbd:`Command`
     - :code:`tab9`

.. _keybindings-emacs-apple-osx-panels:

Panels
======

.. list-table::
   :widths: 2 1 1
   :header-rows: 1

   * - Description
     - Keybinding
     - Command
   * - Show the :guilabel:`Go` window in :guilabel:`Go to Anything` mode
     - :kbd:`Command-E|Command-P`
     - :code:`gotoanything`
   * - Show the :guilabel:`Go` window in :guilabel:`Go to Command` mode
     - :kbd:`Command-.`
     - :code:`gotocommand`
   * - Show the :guilabel:`Go` window in :guilabel:`Go to File` mode.
     - :kbd:`Command-O`
     - :code:`gotofile`
   * - Show the :guilabel:`Go` window in :guilabel:`Go to Symbol` mode.
     - :kbd:`Command-Shift-O`
     - :code:`gotosymbol`
   * - Show the :guilabel:`Outline` window
     - :kbd:`Command-Shift-E`
     - :code:`outline`
   * - Show the :guilabel:`Console` window if hidden, or hide if shown
     - :kbd:`Control-Esc`
     - :code:`toggleconsole`
   * - Show the :guilabel:`Environment` window if hidden, or hide if shown
     - :kbd:`Command-U`
     - :code:`toggletree`

.. _keybindings-emacs-apple-osx-code-editor:

Code Editor
===========

.. list-table::
   :widths: 2 1 1
   :header-rows: 1

   * - Description
     - Keybinding
     - Command
   * - Add a cursor one line above the active cursor, or if a cursor is already added, add another cursor above that one
     - :kbd:`Control-Option-Up`
     - :code:`addCursorAbove`
   * - Add a second cursor one line above the active cursor, or if a second cursor is already added, move the second cursor up one line
     - :kbd:`Control-Option-Shift-Up`
     - :code:`addCursorAboveSkipCurrent`
   * - Add a cursor one line below the active cursor, or if a cursor is already added, add another cursor below that one
     - :kbd:`Control-Option-Down`
     - :code:`addCursorBelow`
   * - Add a second cursor one line below the active cursor, or if a second cursor is already added, move the second cursor down one line
     - :kbd:`Control-Option-Shift-Down`
     - :code:`addCursorBelowSkipCurrent`
   * - Move all cursors to the same space as the active cursor on each of their lines, if they are misaligned
     - :kbd:`Control-Option-A`
     - :code:`alignCursors`
   * - Backspace one space
     - :kbd:`Control-Backspace | Shift-Backspace | Backspace`
     - :code:`backspace`
   * - Indent selection one tab
     - :kbd:`Control-]`
     - :code:`blockindent`
   * - Outdent selection one tab
     - :kbd:`Control-[`
     - :code:`blockoutdent`
   * - Control whether focus can be switched from the editor to somewhere else in the IDE
     - :kbd:`Command-Z | Command-Shift-Z | Command-Y`
     - :code:`cancelBrowserUndoInAce`
   * - Center the selection
     - :kbd:`Control-L`
     - :code:`centerselection`
   * - Copy the contents of the line, and paste the copied contents one line down
     - :kbd:`Command-Option-Down`
     - :code:`copylinesdown`
   * - Copy the contents of the line, and paste the copied contents one line up
     - :kbd:`Command-Option-Up`
     - :code:`copylinesup`
   * - Delete one space
     - :kbd:`Delete | Control-Delete | Shift-Delete`
     - :code:`del`
   * - Copy the contents of the selection, and paste the copied contents immediately after the selection
     - :kbd:`Command-Shift-D`
     - :code:`duplicateSelection`
   * - Include the current line's contents in the selection
     - :kbd:`Command-Shift-L`
     - :code:`expandtoline`
   * - Include up to the next matching symbol in the selection
     - :kbd:`Control-Shift-M`
     - :code:`expandToMatching`
   * - Fold the selected code; if a folded unit is selected, unfold it
     - :kbd:`Command-Option-L | Command-F1`
     - :code:`fold`
   * - Fold all possibly foldable elements
     - :kbd:`Control-Command-Option-0`
     - :code:`foldall`
   * - Fold all possibly foldable elements, except for the current selection scope
     - :kbd:`Command-Option-0`
     - :code:`foldOther`
   * - Go down one line
     - :kbd:`Down | Control-N`
     - :code:`golinedown`
   * - Go up one line
     - :kbd:`Up | Control-P`
     - :code:`golineup`
   * - Go to the end of the file
     - :kbd:`Command-End | Command-Down`
     - :code:`gotoend`
   * - Go left one space
     - :kbd:`Left | Control-B`
     - :code:`gotoleft`
   * - Go to the end of the current line
     - :kbd:`Command-Right | End | Control-E`
     - :code:`gotolineend`
   * - Go to the start of the current line
     - :kbd:`Command-Left | Home | Control-A`
     - :code:`gotolinestart`
   * - Go to the next error
     - :kbd:`F4`
     - :code:`goToNextError`
   * - Go down one page
     - :kbd:`Page Down | Control-V`
     - :code:`gotopagedown`
   * - Go up one page
     - :kbd:`Page Up`
     - :code:`gotopageup`
   * - Go to the previous error
     - :kbd:`Shift-F4`
     - :code:`goToPreviousError`
   * - Go right one space
     - :kbd:`Right | Control-F`
     - :code:`gotoright`
   * - Go to the start of the file
     - :kbd:`Command-Home | Command-Up`
     - :code:`gotostart`
   * - Go one word to the left
     - :kbd:`Option-Left`
     - :code:`gotowordleft`
   * - Go one word to the right
     - :kbd:`Option-Right`
     - :code:`gotowordright`
   * - Indent the selection one tab
     - :kbd:`Tab`
     - :code:`indent`
   * - Go to the matching symbol in the current scope
     - :kbd:`Control-P`
     - :code:`jumptomatching`
   * - Increase the font size
     - :kbd:`Command-+ | Command-=`
     - :code:`largerfont`
   * - Decrease the number to the left of the cursor by 1, if it is a number
     - :kbd:`Option-Shift-Down`
     - :code:`modifyNumberDown`
   * - Increase the number to the left of the cursor by 1, if it is a number
     - :kbd:`Option-Shift-Up`
     - :code:`modifyNumberUp`
   * - Move the selection down one line
     - :kbd:`Option-Down`
     - :code:`movelinesdown`
   * - Move the selection up one line
     - :kbd:`Option-Up`
     - :code:`movelinesup`
   * - Outdent the selection one tab
     - :kbd:`Shift-Tab`
     - :code:`outdent`
   * - Turn on overwrite mode, or if on, turn off
     - :kbd:`Insert`
     - :code:`overwrite`
   * - Go down one page
     - :kbd:`Option-Page Down`
     - :code:`pagedown`
   * - Go up one page
     - :kbd:`Option-Page Up`
     - :code:`pageup`
   * - Remove the current line
     - :kbd:`Command-D`
     - :code:`removeline`
   * - Delete from the cursor to the end of the current line
     - :kbd:`Control-K`
     - :code:`removetolineend`
   * - Delete from the beginning of the current line up to the cursor
     - :kbd:`Command-Backspace`
     - :code:`removetolinestart`
   * - Delete the word to the left of the cursor
     - :kbd:`Option-Backspace | Control-Option-Backspace`
     - :code:`removewordleft`
   * - Delete the word to the right of the cursor
     - :kbd:`Option-Delete`
     - :code:`removewordright`
   * - Replay previously recorded keystrokes
     - :kbd:`Command-Shift-E`
     - :code:`replaymacro`
   * - Select all selectable content
     - :kbd:`Command-A`
     - :code:`selectall`
   * - Include the next line down in the selection
     - :kbd:`Shift-Down | Control-Shift-N`
     - :code:`selectdown`
   * - Include the next space to the left in the selection
     - :kbd:`Shift-Left | Control-Shift-B`
     - :code:`selectleft`
   * - Include the rest of the current line in the selection, starting from the cursor
     - :kbd:`Shift-End`
     - :code:`selectlineend`
   * - Include the beginning of the current line in the selection, up to the cursor
     - :kbd:`Shift-Home`
     - :code:`selectlinestart`
   * - Include more matching selections that are after the selection
     - :kbd:`Control-Option-Right`
     - :code:`selectMoreAfter`
   * - Include more matching selections that are before the selection
     - :kbd:`Control-Option-Left`
     - :code:`selectMoreBefore`
   * - Include the next matching selection that is after the selection
     - :kbd:`Control-Option-Shift-Right`
     - :code:`selectNextAfter`
   * - Include the next matching selection that is before the selection
     - :kbd:`Control-Option-Shift-Left`
     - :code:`selectNextBefore`
   * - Select or find the next matching selection
     - :kbd:`Control-G`
     - :code:`selectOrFindNext`
   * - Select or find the previous matching selection
     - :kbd:`Control-Shift-G`
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
     - :kbd:`Command-Shift-End | Command-Shift-Down`
     - :code:`selecttoend`
   * - Include from the cursor to the end of the current line in the selection
     - :kbd:`Command-Shift-Right | Shift-End | Control-Shift-E`
     - :code:`selecttolineend`
   * - Include from the beginning of the current line to the cursor in the selection
     - :kbd:`Command-Shift-Left | Control-Shift-A`
     - :code:`selecttolinestart`
   * - Include from the cursor to the next matching symbol in the current scope
     - :kbd:`Control-Shift-P`
     - :code:`selecttomatching`
   * - Include from the cursor up to the beginning of the current file in the selection
     - :kbd:`Command-Shift-Home | Command-Shift-Up`
     - :code:`selecttostart`
   * - Include the next line up in the selection
     - :kbd:`Shift-Up | Control-Shift-Up`
     - :code:`selectup`
   * - Include the next word to the left of the cursor in the selection
     - :kbd:`Option-Shift-Left`
     - :code:`selectwordleft`
   * - Include the next word to the right of the cursor in the selection
     - :kbd:`Option-Shift-Right`
     - :code:`selectwordright`
   * - Show the :guilabel:`Preferences` tab
     - :kbd:`Command-,`
     - :code:`showSettingsMenu`
   * - Clear all previous selections
     - :kbd:`Esc`
     - :code:`singleSelection`
   * - Decrease the font size
     - :kbd:`Command--`
     - :code:`smallerfont`
   * - If multiple lines are selected, rearrange them into a sorted order
     - :kbd:`Command-Option-S`
     - :code:`sortlines`
   * - Add a cursor at the end of the current line
     - :kbd:`Control-Option-L`
     - :code:`splitIntoLines`
   * - Move the contents of the cursor to the end of the line, to its own line
     - :kbd:`Control-O`
     - :code:`splitline`
   * - Surround the selection with block comment characters, or remove them if they are there
     - :kbd:`Command-Shift-/`
     - :code:`toggleBlockComment`
   * - Add line comment characters at the start of each selected line, or remove them if they are there
     - :kbd:`Command-/`
     - :code:`togglecomment`
   * - Fold code, or remove code folding if it is there
     - :kbd:`F2`
     - :code:`toggleFoldWidget`
   * - Fold parent code, or remove folding if it is there
     - :kbd:`Option-F2`
     - :code:`toggleParentFoldWidget`
   * - Start keystroke recording, or stop if it is already recording
     - :kbd:`Command-Option-E`
     - :code:`togglerecording`
   * - Wrap words, or stop wrapping words if they are already wrapping
     - :kbd:`Control-W`
     - :code:`toggleWordWrap`
   * - Change selection to all lowercase
     - :kbd:`Control-Shift-U`
     - :code:`tolowercase`
   * - Change selection to all uppercase
     - :kbd:`Control-U`
     - :code:`touppercase`
   * - Transpose selection
     - :kbd:`Control-T`
     - :code:`transposeletters`
   * - Unfold the selected code
     - :kbd:`Command-Option-Shift-L | Command-Shift-F1`
     - :code:`unfold`
   * - Unfold code folding for the entire file
     - :kbd:`Command-Option-Shift-0`
     - :code:`unfoldall`

.. _keybindings-emacs-apple-osx-emmet:

emmet
=====

.. list-table::
   :widths: 2 1 1
   :header-rows: 1

   * - Description
     - Keybinding
     - Command
   * - Evaluate a simple math expression (such as :code:`2*4` or :code:`10/2`), and output its result
     - :kbd:`Shift-Command-Y`
     - :code:`emmet_evaluate_math_expression`
   * - Expand CSS-like abbreviations into HTML, XML, or CSS code, depending on the current file's syntax
     - :kbd:`Control-Option-E`
     - :code:`emmet_expand_abbreviation`
   * - Traverse expanded CSS-like abbreviations, by tab stop
     - :kbd:`Tab`
     - :code:`emmet_expand_abbreviation_with_tab`
   * - Go to the next editable code part
     - :kbd:`Shift-Command-.`
     - :code:`emmet_select_next_item`
   * - Go to the previous editable code part
     - :kbd:`Shift-Command-,`
     - :code:`emmet_select_previous_item`
   * - Expand an abbreviation, and then place the current selection within the last element of the generated snippet
     - :kbd:`Shift-Control-A`
     - :code:`emmet_wrap_with_abbreviation`

.. _keybindings-emacs-apple-osx-terminal:

Terminal
========

.. list-table::
   :widths: 2 1 1
   :header-rows: 1

   * - Description
     - Keybinding
     - Command
   * - Open a new :guilabel:`Terminal` tab
     - :kbd:`Option-T`
     - :code:`openterminal`
   * - Switch between the editor and the :guilabel:`Terminal` tab
     - :kbd:`Option-S`
     - :code:`switchterminal`

.. _keybindings-emacs-apple-osx-run-debug:

Run and Debug
=============

.. list-table::
   :widths: 2 1 1
   :header-rows: 1

   * - Description
     - Keybinding
     - Command
   * - Build the current file
     - :kbd:`Command-B`
     - :code:`build`
   * - Resume the current paused process
     - :kbd:`F8 | Command-\\`
     - :code:`resume`
   * - Run or debug the current application
     - :kbd:`Option-F5`
     - :code:`run`
   * - Run or debug the last run file
     - :kbd:`F5`
     - :code:`runlast`
   * - Step into the function that is next on the stack
     - :kbd:`F11 | Command-;`
     - :code:`stepinto`
   * - Step out of the current function scope
     - :kbd:`Shift-F11 | Command-Shift-'`
     - :code:`stepout`
   * - Step over the current expression on the stack
     - :kbd:`F10 | Command-'`
     - :code:`stepover`
   * - Stop running or debugging the current application
     - :kbd:`Shift-F5`
     - :code:`stop`
   * - Stop building the current file
     - :kbd:`Control-Shift-C`
     - :code:`stopbuild`
