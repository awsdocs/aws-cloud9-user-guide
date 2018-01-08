.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _menu-commands:

#####################################################
Menu Bar Commands Reference for the |AC9IDElongtitle|
#####################################################

.. meta::
   :description:
      Provides a list of menu bar commands in the AWS Cloud9 IDE.

The following lists describe the default menu bar commands in the |AC9IDE|. If the menu bar isn't
visible, choose the thin bar along the top edge of the IDE to show it.

* :ref:`menu-commands-cloud9`
* :ref:`menu-commands-file`
* :ref:`menu-commands-edit`
* :ref:`menu-commands-find`
* :ref:`menu-commands-view`
* :ref:`menu-commands-goto`
* :ref:`menu-commands-run`
* :ref:`menu-commands-tools`
* :ref:`menu-commands-window`
* :ref:`menu-commands-support`
* :ref:`menu-commands-preview`
* :ref:`menu-commands-other`

.. _menu-commands-cloud9:

AWS Cloud9 Menu
===============

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - Command
     - Description
   * - :guilabel:`Preferences`
     - Do one of the following:

       * Open the :guilabel:`Preferences` tab if it isn't open.
       * Make the :guilabel:`Preferences` tab active if it is open but not active.
       * Hide the :guilabel:`Preferences` tab if it is active.
     
       See :doc:`Working with Project Settings <settings-project>`,
       :doc:`Working with User Settings <settings-user>`,
       :doc:`Working with Keybindings <settings-keybindings>`,
       :doc:`Working with Themes <settings-theme>`, and
       :doc:`Working with Initialization Scripts <settings-init-script>`.
   * - :guilabel:`Go To Your Dashboard`
     - Open the |AC9| console in a separate web browser tab. See
       :doc:`Creating an Environment <create-environment>`,
       :doc:`Opening an Environment <open-environment>`,
       :doc:`Changing Environment Settings <change-environment>`, and
       :doc:`Deleting an Environment <delete-environment>`.
   * - :guilabel:`Welcome Page`
     - Open the :guilabel:`Welcome` tab.
   * - :guilabel:`Open Your Project Settings`
     - Open the :file:`project.settings` file for the current |env|. See :doc:`Working with Project Settings <settings-project>`.
   * - :guilabel:`Open Your User Settings`
     - Open the :file:`user.settings` file for the current user. See :doc:`Working with User Settings <settings-user>`.
   * - :guilabel:`Open Your Keymap`
     - Open the :file:`keybindings.settings` file for the current user. See :doc:`Working with Keybindings <settings-keybindings>`.
   * - :guilabel:`Open Your Init Script`
     - Open the :file:`init.js` file for the current user. See :doc:`Working with Initialization Scripts <settings-init-script>`.
   * - :guilabel:`Open Your Stylesheet`
     - Open the :file:`styles.css` file for the current user. See :doc:`Working with Themes <settings-theme>`.

.. _menu-commands-file:

File Menu
=========

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - Command
     - Description
   * - :guilabel:`New File`
     - Create a new file.
   * - :guilabel:`New From Template`
     - Create a new file, based on the chosen file template.
   * - :guilabel:`Open`
     - Show and go to the :guilabel:`Navigate` window.
   * - :guilabel:`Open Recent`
     - Open the chosen file.
   * - :guilabel:`Save`
     - Save the current file.
   * - :guilabel:`Save As`
     - Save the current file with a different file name, location, or both.
   * - :guilabel:`Save All`
     - Save all unsaved files.
   * - :guilabel:`Revert to Saved`
     - Discard changes for current file since it was last saved.
   * - :guilabel:`Revert All to Saved`
     - Discard changes for all unsaved files since they were last saved.
   * - :guilabel:`Upload Local Files`
     - Show the :guilabel:`Upload Files` dialog box, which enables you to drag files from your
       local computer into the |env|.
   * - :guilabel:`Download Project`
     - Combine the files in the |env| into a .zip file, which you can download to your local computer.
   * - :guilabel:`Line Endings`
     - Use :guilabel:`Windows` (carriage return plus line feed) or :guilabel:`Unix` (line feed only) line endings.
   * - :guilabel:`Close File`
     - Close the current file.
   * - :guilabel:`Close All Files`
     - Close all open files.

.. _menu-commands-edit:

Edit Menu
=========

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - Command
     - Description
   * - :guilabel:`Undo`
     - Undo the last action.
   * - :guilabel:`Redo`
     - Redo the last undone action.
   * - :guilabel:`Cut`
     - Move the selection to the clipboard.
   * - :guilabel:`Copy`
     - Copy the selection to the clipboard.
   * - :guilabel:`Paste`
     - Copy the clipboard's contents to the selection point.
   * - :guilabel:`Keyboard Mode`
     - The set of keybindings to use, such as :code:`Default`, :code:`Vim`, :code:`Emacs`, or :code:`Sublime`. See
       :doc:`Working with Keybindings <settings-keybindings>`.
   * - :guilabel:`Selection, Select All`
     - Select all selectable content.
   * - :guilabel:`Selection, Split Into Lines`
     - Add a cursor at the end of the current line.
   * - :guilabel:`Selection, Single Selection`
     - Clear all previous selections.
   * - :guilabel:`Selection, Multiple Selections, Add Cursor Up`
     - Add a cursor one line above the active cursor. If a cursor is already added, add another cursor above that one.
   * - :guilabel:`Selection, Multiple Selections, Add Cursor Down`
     - Add a cursor one line below the active cursor. If a cursor is already added, add another cursor below that one.
   * - :guilabel:`Selection, Multiple Selections, Move Active Cursor Up`
     - Add a second cursor one line above the active cursor. If a second cursor is already added, move the second cursor up one line.
   * - :guilabel:`Selection, Multiple Selections, Move Active Cursor Down`
     - Add a second cursor one line below the active cursor. If a second cursor is already added, move the second cursor down one line.
   * - :guilabel:`Selection, Multiple Selections, Add Next Selection Match`
     - Include more matching selections that are after the selection.
   * - :guilabel:`Selection, Multiple Selections, Add Previous Selection Match`
     - Include more matching selections that are before the selection.
   * - :guilabel:`Selection, Multiple Selections, Merge Selection Range`
     - Add a cursor at the end of the current line.
   * - :guilabel:`Selection, Select Word Right`
     - Include the next word to the right of the cursor in the selection.
   * - :guilabel:`Selection, Select Word Left`
     - Include the next word to the left of the cursor in the selection.
   * - :guilabel:`Selection, Select to Line End`
     - Include from the cursor to the end of the current line in the selection
   * - :guilabel:`Selection, Select to Line Start`
     - Include from the beginning of the current line to the cursor in the selection.
   * - :guilabel:`Selection, Select to Document End`
     - Include from the cursor down to the end of the current file in the selection.
   * - :guilabel:`Selection, Select to Document Start`
     - Include from the cursor up to the beginning of the current file in the selection.
   * - :guilabel:`Line, Indent`
     - Indent the selection one tab.
   * - :guilabel:`Line, Outdent`
     - Outdent the selection one tab.
   * - :guilabel:`Line, Move Line Up`
     - Move the selection up one line.
   * - :guilabel:`Line, Move Line Down`
     - Move the selection down one line.
   * - :guilabel:`Line, Copy Lines Up`
     - Copy the contents of the line, and paste the copied contents one line up.
   * - :guilabel:`Line, Copy Lines Down`
     - Copy the contents of the line, and paste the copied contents one line down.
   * - :guilabel:`Line, Remove Line`
     - Delete the contents of the current line.
   * - :guilabel:`Line, Remove to Line End`
     - Delete from the cursor to the end of the current line.
   * - :guilabel:`Line, Remove to Line Start`
     - Delete from the beginning of the current line up to the cursor.
   * - :guilabel:`Line, Split Line`
     - Move the contents of the cursor to the end of the line, to its own line.
   * - :guilabel:`Text, Remove Word Right`
     - Delete the word to the right of the cursor.
   * - :guilabel:`Text, Remove Word Left`
     - Delete the word to the left of the cursor.
   * - :guilabel:`Text, Align`
     - Move all cursors to the same space as the active cursor on each of their lines, if they are misaligned.
   * - :guilabel:`Text, Transpose Letters`
     - Transpose the selection.
   * - :guilabel:`Text, To Upper Case`
     - Change the selection to all uppercase.
   * - :guilabel:`Text, To Lower Case`
     - Change the selection to all lowercase.
   * - :guilabel:`Comment, Toggle Comment`
     - Add line comment characters at the start of each selected line, or remove them if they are there.
   * - :guilabel:`Code Folding, Toggle Fold`
     - Fold code, or remove code folding if it is there.
   * - :guilabel:`Code Folding, Unfold`
     - Unfold the selected code.
   * - :guilabel:`Code Folding, Fold Other`
     - Fold all possibly foldable elements, except for the current selection scope.
   * - :guilabel:`Code Folding, Fold All`
     - Fold all possibly foldable elements.
   * - :guilabel:`Code Folding, Unfold All`
     - Unfold code folding for the entire file.
   * - :guilabel:`Code Formatting, Apply Code Formatting`
     - Reformat the selected JavaScript code.
   * - :guilabel:`Code Formatting, Open Language & Formatting Preferences`
     - Open the :guilabel:`Project Settings` section of the :guilabel:`Preferences` tab to programming language settings.

.. _menu-commands-find:

Find Menu
=========

For more information, see :doc:`Finding and Replacing Text <find-replace-text>`.

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - Command
     - Description
   * - :guilabel:`Find`
     - Show the find and replace bar for the current document, with focus on the :guilabel:`Find` expression.
   * - :guilabel:`Find Next`
     - Go to the next match in the current document for the find query you entered last.
   * - :guilabel:`Find Previous`
     - Go to the previous match in the current document for the find query you entered last.
   * - :guilabel:`Replace`
     - Show the find and replace bar for the current document, with focus on the :guilabel:`Replace With` expression.
   * - :guilabel:`Replace Next`
     - Replace the next match for :guilabel:`Find` with :guilabel:`Replace With` in the find and replace bar for the current document .
   * - :guilabel:`Replace Previous`
     - Replace the previous match for :guilabel:`Find` with :guilabel:`Replace With` in the find and replace bar for the current document.
   * - :guilabel:`Replace All`
     - Replace all matches for :guilabel:`Find` with :guilabel:`Replace With` in the find and replace bar for the current document.
   * - :guilabel:`Find in Files`
     - Show the find and replace bar for multiple files.

.. _menu-commands-view:

View Menu
=========

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - Command
     - Description
   * - :guilabel:`Editors`
     - Show the chosen editor.
   * - :guilabel:`Open Files`
     - Show the :guilabel:`Open Files` list in the :guilabel:`Environment` window, or hide if shown.
   * - :guilabel:`Menu Bar`
     - Show the menu bar, or hide if shown.
   * - :guilabel:`Tab Buttons`
     - Show tabs, or hide if shown.
   * - :guilabel:`Gutter`
     - Show the gutter, or hide if shown.
   * - :guilabel:`Status Bar`
     - Show the status bar, or hide if shown.
   * - :guilabel:`Console`
     - Show the :guilabel:`Console` window, or hide if shown.
   * - :guilabel:`Layout, Single`
     - Show a single pane.
   * - :guilabel:`Layout, Vertical Split`
     - Show two panes, top and bottom.
   * - :guilabel:`Layout, Horizontal Split`
     - Show two panes, side by side.
   * - :guilabel:`Layout, Cross Split`
     - Show four panes of equal size.
   * - :guilabel:`Layout, Split 1:2`
     - Show one pane on the left and two panes on the right.
   * - :guilabel:`Layout, Split 2:1`
     - Show two panes on the left and one pane on the right.
   * - :guilabel:`Font Size, Increase Font Size`
     - Increase the font size.
   * - :guilabel:`Font Size, Decrease Font Size`
     - Decrease the font size.
   * - :guilabel:`Syntax`
     - Show the syntax type for the current document.
   * - :guilabel:`Themes`
     - Show the IDE theme type.
   * - :guilabel:`Wrap Lines`
     - Wrap words to the edge of the current pane, or stop wrapping words if they are already wrapping.
   * - :guilabel:`Wrap To Print Margin`
     - Wrap words to the edge of the current print margin, or stop wrapping words if they are already wrapping.

.. _menu-commands-goto:

Goto Menu
=========

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - Command
     - Description
   * - :guilabel:`Goto Anything`
     - Show the :guilabel:`Navigate` window.
   * - :guilabel:`Goto Symbol`
     - Show the :guilabel:`Outline` window.
   * - :guilabel:`Goto Line`
     - Show the go to line box for the current document.
   * - :guilabel:`Goto Command`
     - Show the :guilabel:`Commands` window.
   * - :guilabel:`Next Error`
     - Go to the next error.
   * - :guilabel:`Previous Error`
     - Go to the previous error.
   * - :guilabel:`Word Right`
     - Go one word to the right.
   * - :guilabel:`Word Left`
     - Go one word to the left.
   * - :guilabel:`Line End`
     - Go to the end of the current line.
   * - :guilabel:`Line Start`
     - Go to the start of the current line.
   * - :guilabel:`Jump to Definition`
     - Go to the definition of the variable or function at the cursor.
   * - :guilabel:`Jump to Matching Brace`
     - Go to the matching symbol in the current scope.
   * - :guilabel:`Scroll to Selection`
     - Scroll the selection into better view.

.. _menu-commands-run:

Run Menu
========

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - Command
     - Description
   * - :guilabel:`Run`
     - Run or debug the current application.
   * - :guilabel:`Run Last`
     - Run or debug the last run file.
   * - :guilabel:`Run With`
     - Run or debug using the chosen runner. See
       :doc:`Working with Builders, Runners, and Debuggers <build-run-debug>`.
   * - :guilabel:`Run History`
     - View run history.
   * - :guilabel:`Run Configurations`
     - Choose a run configuration to run or debug with, or create or manage run configurations. See :doc:`Working with Builders, Runners, and Debuggers <build-run-debug>`.
   * - :guilabel:`Show Debugger at Break`
     - When running code reaches a breakpoint, show the :guilabel:`Debugger` window.
   * - :guilabel:`Build`
     - Build the current file.
   * - :guilabel:`Cancel Build`
     - Stop building the current file.
   * - :guilabel:`Build System`
     - Build using the chosen build system.
   * - :guilabel:`Show Build Result`
     - Show the related build result.
   * - :guilabel:`Automatically Build Supported Files`
     - Automatically build supported files.
   * - :guilabel:`Save All on Build`
     - When building, save all related unsaved files.

.. _menu-commands-tools:

Tools Menu
==========

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - Command
     - Description
   * - :guilabel:`Strip Trailing Space`
     - Trim whitespace at the ends of lines.
   * - :guilabel:`Preview, Preview File FILE-NAME`
     - Preview the current document in a preview tab.
   * - :guilabel:`Preview, Preview Running Application`
     - Preview the current application in a separate web browser tab.
   * - :guilabel:`Preview, Configure Preview URL`
     - Open the :guilabel:`Project Settings` section of the :guilabel:`Preferences` tab to the :guilabel:`Run & Debug, Preview URL` box.
   * - :guilabel:`Preview, Show Active Servers`
     - Show a list of available active server addresses in the :guilabel:`Process List` dialog box.
   * - :guilabel:`Process List`
     - Show the :guilabel:`Process List` dialog box.
   * - :guilabel:`Show Autocomplete`
     - Show the code completion context menu.
   * - :guilabel:`Rename Variable`
     - Start a rename refactor for the selection.
   * - :guilabel:`Toggle Macro Recording`
     - Start keystroke recording, of stop if it is already recording.
   * - :guilabel:`Play Macro`
     - Play previously recorded keystrokes.
   * - :guilabel:`Developer, Start in Debug Mode`
     - Reload the IDE in debug mode.

.. _menu-commands-window:

Window Menu
===========

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - Command
     - Description
   * - :guilabel:`New Terminal`
     - Open a new :guilabel:`Terminal` tab.
   * - :guilabel:`New Immediate Window`
     - Open a new :guilabel:`Immediate` tab.
   * - :guilabel:`Share`
     - Show the :guilabel:`Share this environment` dialog box.
   * - :guilabel:`Installer`
     - Show the :guilabel:`AWS Cloud9 Installer` dialog box.
   * - :guilabel:`Collaborate`
     - Show the :guilabel:`Collaborate` window, or hide if shown.
   * - :guilabel:`Outline`
     - Show the :guilabel:`Outline` window, or hide if shown.
   * - :guilabel:`AWS Resources`
     - Show the :guilabel:`AWS Resources` window, or hide if shown.  
   * - :guilabel:`Environment`
     - Show the :guilabel:`Environment` window, or hide if shown.
   * - :guilabel:`Debugger`
     - Show the :guilabel:`Debugger` window, or hide if shown.
   * - :guilabel:`Navigate`
     - Show the :guilabel:`Navigate` window, or hide if shown.
   * - :guilabel:`Commands`
     - Show the :guilabel:`Commands` window, or hide if shown.
   * - :guilabel:`Navigation, Tab to the Right`
     - Go one tab right.
   * - :guilabel:`Navigation, Tab to the Left`
     - Go one tab left.
   * - :guilabel:`Navigation, Next Tab in History`
     - Go to the next tab.
   * - :guilabel:`Navigation, Previous Tab in History`
     - Go to the previous tab.
   * - :guilabel:`Navigation, Move Tab to Right`
     - Move the current tab right. If the tab is already at the far right, create a split tab there.
   * - :guilabel:`Navigation, Move Tab to Left`
     - Move the current tab left. If the tab is already at the far left, create a split tab there.
   * - :guilabel:`Navigation, Move Tab to Up`
     - Move the current tab up one pane. If the tab is already at very top, create a split tab there.
   * - :guilabel:`Navigation, Move Tab to Down`
     - Move the current tab down one pane. If the tab is already at the very bottom, create a split tab
       there.
   * - :guilabel:`Navigation, Go to Pane to Right`
     - Go one pane right.
   * - :guilabel:`Navigation, Go to Pane to Left`
     - Go one pane left.
   * - :guilabel:`Navigation, Go to Pane to Up`
     - Go one pane up.
   * - :guilabel:`Navigation, Go to Pane to Down`
     - Go one pane down.
   * - :guilabel:`Navigation, Switch Between Editor and Terminal`
     - Switch between the editor and the :guilabel:`Terminal` tab .
   * - :guilabel:`Navigation, Next Pane in History`
     - Go to the next pane.
   * - :guilabel:`Navigation, Previous Pane in History`
     - Go to the previous pane.
   * - :guilabel:`Saved Layouts, LAYOUT-ID`
     - Switch to the chosen layout.
   * - :guilabel:`Saved Layouts, Save`
     - Save the current layout. To switch to this layout later, choose :guilabel:`Saved Layouts, LAYOUT-ID`.
   * - :guilabel:`Saved Layouts, Save and Close All`
     - Save the current layout, and then close all tabs and panes.
   * - :guilabel:`Saved Layouts, Show Saved Layouts in File Tree`
     - Show all saved layouts in the :guilabel:`Environment` window.
   * - :guilabel:`Tabs, Close Pane`
     - Close the current pane.
   * - :guilabel:`Tabs, Close All Tabs In All Panes`
     - Close all open tabs in all panes.
   * - :guilabel:`Tabs, Close All But Current Tab`
     - Close all open tabs in the current pane, except the current tab.
   * - :guilabel:`Tabs, TAB-NAME`
     - Go to the chosen tab.
   * - :guilabel:`Tabs, Split Pane in Two Rows`
     - Split the current pane into two panes, top and bottom.
   * - :guilabel:`Tabs, Split Pane in Two Columns`
     - Split the current pane into two panes, left and right.
   * - :guilabel:`Tabs, (visual layout indicator)`
     - Switch to the chosen view.
   * - :guilabel:`Presets, Full IDE`
     - Switch to full IDE mode.
   * - :guilabel:`Presets, Minimal Editor`
     - Switch to minimal editor mode.
   * - :guilabel:`Presets, Sublime Mode`
     - Switch to Sublime mode.

.. _menu-commands-support:

Support Menu
============

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - Command
     - Description
   * - :guilabel:`Welcome Page`
     - Open the :guilabel:`Welcome` tab.
   * - :guilabel:`Get Help (Community)`
     - Opens the |AC9| online community website in a separate web browser tab.
   * - :guilabel:`Read Documentation`
     - Opens the *AWS Cloud9 User Guide* in a separate web browser tab.

.. _menu-commands-preview:

Preview Menu
============

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - Command
     - Description
   * - :guilabel:`Preview File FILE-NAME`
     - Preview the current document in a preview tab.
   * - :guilabel:`Preview Running Application`
     - Preview the current application in a separate web browser tab.
   * - :guilabel:`Configure Preview URL`
     - Open the :guilabel:`Project Settings` section of the :guilabel:`Preferences` tab to the :guilabel:`Run & Debug, Preview URL` box.
   * - :guilabel:`Show Active Servers`
     - Show a list of available active server addresses in the :guilabel:`Process List` dialog box.

.. _menu-commands-other:

Other Menu Bar Commands
=======================

.. list-table::
   :widths: 1 2
   :header-rows: 1

   * - Command
     - Description
   * - :guilabel:`Run`
     - Run or debug the current application.
   * - :guilabel:`Share`
     - Opens the :guilabel:`Share this environment` dialog box.
   * - :guilabel:`Preferences` (gear icon)
     - Open the :guilabel:`Preferences` tab.
