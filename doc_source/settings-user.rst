.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _settings-user:

###################################################
Working with User Settings in the |AC9IDElongtitle|
###################################################

.. meta::
    :description:
        Describes how to work with user settings in the AWS Cloud9 IDE.

:dfn:`User settings`, which apply across each |envfirst| associated with your |IAM| user, include the following kinds of settings:

* General user interface behaviors, such as whether to enable animations
* File system navigation behaviors
* File find and search behaviors
* Color schemes for terminal sessions and output
* Additional code editor behaviors, such as code folding, full line selection, scrolling animations, and font sizes

As you make changes to your user settings, |AC9| pushes those changes to the cloud and
associates them with your |IAM| user. |AC9| also continually scans the cloud for changes to user settings
associated with your |IAM| user, and applies those settings
to your current |env|.

You can share your user settings with other users.

* :ref:`settings-user-view`
* :ref:`settings-user-share`
* :ref:`settings-user-change`

.. _settings-user-view:

View or Change Your User Settings
=================================

#. On the menu bar, choose :menuselection:`AWS Cloud9, Preferences`.
#. To view your user settings across each |env| of yours, on the :guilabel:`Preferences` tab, in the side navigation pane, choose :guilabel:`User Settings`.
#. To change your user settings across each |env| of yours, in the :guilabel:`User Settings` pane, change
   the settings you want.
#. To apply your changes to any other |env| of yours, simply open that |env|. If that |env| is
   already open, refresh the web browser tab for that |env|.

For more information, see :ref:`settings-user-change`.

.. _settings-user-share:

Share Your User Settings with Another User
==========================================

#. In both the source and target |env|, on the menu bar of the |AC9IDE|, choose :guilabel:`AWS Cloud9, Open Your User Settings`.
#. In the source |env|, copy the contents of the :guilabel:`user.settings` tab that is displayed.
#. In the target |env|, overwrite the contents of the :guilabel:`user.settings` tab with the copied contents from the source |env|.
#. In the target |env|, save the :guilabel:`user.settings` tab.

.. _settings-user-change:

User Setting Changes You Can Make
=================================

These sections describe the kinds of user settings on the :guilabel:`Preferences` tab's :guilabel:`User
Settings` pane that you can change.

* :ref:`settings-user-change-general`
* :ref:`settings-user-change-user-interface`
* :ref:`settings-user-change-collaboration`
* :ref:`settings-user-change-tree-and-navigate`
* :ref:`settings-user-change-find-in-files`
* :ref:`settings-user-change-meta-data`
* :ref:`settings-user-change-watchers`
* :ref:`settings-user-change-terminal`
* :ref:`settings-user-change-output`
* :ref:`settings-user-change-code-editor-ace`
* :ref:`settings-user-change-input`
* :ref:`settings-user-change-hints-and-warnings`
* :ref:`settings-user-change-run-and-debug`
* :ref:`settings-user-change-preview`
* :ref:`settings-user-change-build`

.. _settings-user-change-general:

General
-------

:guilabel:`Reset to Factory Settings`
   If the :guilabel:`Reset to Default` button is chosen, |AC9| resets all of your user settings to the |AC9| default user settings.
   To confirm, choose :guilabel:`Reset settings`.

   .. caution:: This action cannot be undone.

:guilabel:`Warn Before Exiting`
   If enabled, whenever you attempt to close the IDE, 
   |AC9| will prompt you about whether you really want to exit |AC9|.

.. _settings-user-change-user-interface:

User Interface
--------------

:guilabel:`Enable UI Animations`
   If enabled, |AC9| uses animations in the IDE.

:guilabel:`Use an Asterisk (*) to Mark Changed Tabs`
   If enabled, |AC9| adds an asterisk (:guilabel:`*`) to tabs that have changes, but for which the contents
   have not yet been saved.

:guilabel:`Display Title of Active Tab as Browser Title`
   If enabled, |AC9| changes the title of the associated web browser tab to the title of the active tab (for example, :guilabel:`Untitled1`,
   :guilabel:`hello.js`, :guilabel:`Terminal`, :guilabel:`Preferences`, and so on).

:guilabel:`Automatically Close Empty Panes`
   If enabled, whenever you reload an |env|, |AC9| automatically closes any panes it considers are empty.

:guilabel:`Environment Files Icon and Selection Style`
   The icon |AC9| uses for |env| files, and the file selection behaviors |AC9| uses.

   Valid values include:

   * :guilabel:`Default` for |AC9| to use default icons and default file selection behaviors.
   * :guilabel:`Alternative` for |AC9| to use alternative icons and alternative file selection behaviors.

.. _settings-user-change-collaboration:

Collaboration
-------------

:guilabel:`Show Notification Bubbles`
   If enabled, |AC9| displays notifications if the |env| is a shared |env| and multiple users are actively collaborating in that shared |env|.

:guilabel:`Disable collaboration security warning`
   If enabled, |AC9| does not display the security warning dialog box when a |memrw| member is added to an |env|.

:guilabel:`Show Authorship Info`
   If enabled, |AC9| underlines text entered by other |env| members with related highlights in the gutter.

.. _settings-user-change-tree-and-navigate:

Tree & Navigate
---------------

:guilabel:`Scope Navigate to Favorites`
   If enabled, the :guilabel:`Navigate` window only works with items in the :guilabel:`Environment` window's :guilabel:`Favorites` section.

:guilabel:`Enable Preview on Navigation`
   If enabled, |AC9| displays the chosen file in the :guilabel:`Navigate` window with a single mouse click instead of a double mouse click.

:guilabel:`Enable Preview on Tree Selection`
   If enabled, |AC9| displays the chosen file with a single mouse click instead of a double mouse click.

:guilabel:`Hidden File Pattern`
   The types of files for |AC9| to treat as hidden.

:guilabel:`Reveal Active File in Project Tree`
   If enabled, |AC9| highlights the active file in the :guilabel:`Environment` window.

:guilabel:`Download Files As`
   The behavior for |AC9| to use when downloading files.
 
   Valid values include:
 
   * :guilabel:`auto` for |AC9| to download files without modification.
   * :guilabel:`tar.gz` for |AC9| to download files as compressed TAR files.
   * :guilabel:`zip` for |AC9| to download files as .zip files.

.. _settings-user-change-find-in-files:

Find in Files
-------------

:guilabel:`Search In This Path When 'Project' Is Selected`
   On the find in files bar, when :guilabel:`Project` is selected for the search scope, the path to find in.

:guilabel:`Show Full Path in Results`
   If selected, displays the full path to each matching file in the :guilabel:`Search Results` tab.

:guilabel:`Clear Results Before Each Search`
   If selected, clears the :guilabel:`Search Results` tab of the results of any previous searches before the current search begins.

:guilabel:`Scroll Down as Search Results Come In`
   If selected, scrolls the :guilabel:`Search Results` tab to the bottom of the list of results as search results are identified.

:guilabel:`Open Files when Navigating Results with (Up and Down)`
   If selected, as the up and down arrow keys are pressed in the :guilabel:`Search Results` tab within the list of results, opens each matching file.

.. _settings-user-change-meta-data:

Meta Data
---------

:guilabel:`Maximum of Undo Stack Items in Meta Data`
   The maximum number of items that |AC9| keeps in its list of action that can be undone.

.. _settings-user-change-watchers:

Watchers
--------

:guilabel:`Auto-Merge Files When a Conflict Occurs`
   If enabled, |AC9| attempts to automatically merge files whenever a merge conflict happens.

.. _settings-user-change-terminal:

Terminal
--------

:guilabel:`Text Color`
   The color of text in :guilabel:`Terminal` tabs.

:guilabel:`Background Color`
   The background color in :guilabel:`Terminal` tabs.

:guilabel:`Selection Color`
   The color of selected text in :guilabel:`Terminal` tabs.

:guilabel:`Font Family`
   The text font style in :guilabel:`Terminal` tabs.

:guilabel:`Font Size`
   The size of text in :guilabel:`Terminal` tabs.

:guilabel:`Antialiased Fonts`
   If enabled, |AC9| attempts to smooth the display of text in :guilabel:`Terminal` tabs.

:guilabel:`Blinking Cursor`
   If enabled, |AC9| continuously blinks the cursor in :guilabel:`Terminal` tabs.

:guilabel:`Scrollback`
   The number of lines that you can scroll up or back through in :guilabel:`Terminal` tabs.

:guilabel:`Use Cloud9 as the Default Editor`
   If selected, uses |AC9| as the default text editor.

.. _settings-user-change-output:

Output
------

:guilabel:`Text Color`
   The color of text in tabs that display output.

:guilabel:`Background Color`
   The background color of text in tabs that display output.

:guilabel:`Selection Color`
   The color of selected text in tabs that display output.

:guilabel:`Warn Before Closing Unnamed Configuration`
   If enabled, |AC9| prompts you to save any unsaved configuration tab before it is closed.

:guilabel:`Preserve log between runs`
   If enabled, |AC9| keeps a log of all attempted runs.

.. _settings-user-change-code-editor-ace:

Code Editor (Ace)
-----------------

:guilabel:`Auto-pair Brackets, Quotes, etc.`
   If enabled, |AC9| attempts to add a matching closing character for each related starting character
   that is typed in editor tabs, such as for brackets, quotation marks, and braces.

:guilabel:`Wrap Selection with Brackets, Quote, etc.`
   If enabled, |AC9| attempts to insert a matching closing character at the end of text in editor tabs
   after the text is selected and a related started character is typed, such as for brackets, quotation
   marks, and braces.

:guilabel:`Code Folding`
   If enabled, |AC9| attempts to show, expand, hide, or collapse sections of code in editor tabs according to related code syntax rules.

:guilabel:`Fade Fold Widgets`
   If enabled, |AC9| displays code folding controls in the gutter whenever you pause the mouse
   over those controls in editor tabs.

:guilabel:`Full Line Selection`
   If enabled, |AC9| selects an entire line that is triple-clicked in editor tabs.

:guilabel:`Highlight Active Line`
   If enabled, |AC9| highlights the entire active line in editor tabs.

:guilabel:`Highlight Gutter Line`
   If enabled, |AC9| highlights the location in the gutter next to the active line in editor tabs.

:guilabel:`Show Invisible Characters`
   If enabled, |AC9| displays what it considers to be invisible characters in editor tabs, for example carriage returns and line feeds, spaces, and tabs.

:guilabel:`Show Gutter`
   If enabled, |AC9| displays the gutter.

:guilabel:`Show Line Numbers`
   The behavior for displaying line numbers in the gutter.

   Valid values include:

   * :guilabel:`Normal` to display line numbers.
   * :guilabel:`Relative` to display line numbers relative to the active line.
   * :guilabel:`None` to hide line numbers.

:guilabel:`Show Indent Guides`
   If enabled, |AC9| displays guides to more easily visualize indented text in editor tabs.

:guilabel:`Highlight Selected Word`
   If enabled, |AC9| selects an entire word that is double-clicked in an editor tab.

:guilabel:`Scroll Past the End of the Document`
   The behavior for allowing the user to scroll past the end of the current file in editor tabs.

   Valid values include:

   * :guilabel:`Off` to not allow any scrolling past the end of the current file.
   * :guilabel:`Half Editor Height` to allow scrolling past the end of the current file to up to half the editor's screen height.
   * :guilabel:`Full Editor Height` to allow scrolling past the end of the current file to up to the editor's full screen height.

:guilabel:`Animate Scrolling`
   If enabled, |AC9| applies animation behaviors during scrolling actions in editor tabs.

:guilabel:`Font Family`
   The style of font to use in editor tabs.

:guilabel:`Font Size`
   The size of the font to use in editor tabs.

:guilabel:`Antialiased Fonts`
   If enabled, |AC9| attempts to smooth the display of text in editor tabs.

:guilabel:`Show Print Margin`
   Displays a vertical line in editor tabs after the specified character location.

:guilabel:`Mouse Scroll Speed`
   The relative speed of mouse scrolling in editor tabs. Larger values result in faster scrolling.

:guilabel:`Cursor Style`
   The style and behavior of the cursor in editor tabs.

   Valid values include:

   * :guilabel:`Ace` to display the cursor as a vertical bar that is relatively wider than :guilabel:`Slim`.
   * :guilabel:`Slim` to display the cursor as a relatively slim vertical bar.
   * :guilabel:`Smooth` to display the cursor as a vertical bar that is relatively wider than :guilabel:`Slim`
     and that blinks more smoothly than :guilabel:`Slim`.
   * :guilabel:`Smooth and Slim` to display the cursor as a relatively slim vertical bar that blinks more
     smoothly than :guilabel:`Slim`.
   * :guilabel:`Wide` to display the cursor as a relatively wide vertical bar.

:guilabel:`Merge Undo Deltas`

   * :guilabel:`Always` to allow merge conflicts to be reverted.
   * :guilabel:`Never` to never allow merge conflicts to be reverted.
   * :guilabel:`Timed` to allow merge conflicts to be reverted after a specified time period.

:guilabel:`Enable Wrapping For New Documents`
   If enabled, |AC9| wraps code in new files.

.. _settings-user-change-input:

Input
-----

:guilabel:`Complete As You Type`
   If enabled, |AC9| attempts to display possible text completions as you type.

:guilabel:`Complete On Enter`
   If enabled, |AC9| attempts to display possible text completions after you press :kbd:`Enter`.

:guilabel:`Highlight Variable Under Cursor`
   If enabled, |AC9| highlights all references in code to the selected variable.

:guilabel:`Use Cmd-Click for Jump to Definition`
   If enabled, |AC9| goes to any original definition for code that is clicked while pressing and holding
   :kbd:`Command` for Mac or :kbd:`Ctrl` for Windows.

.. _settings-user-change-hints-and-warnings:

Hints & Warnings
----------------

:guilabel:`Enable Hints and Warnings`
   If enabled, |AC9| displays applicable hint and warning messages.

:guilabel:`Ignore Messages Matching Regex`
   |AC9| does not display any messages matching the specified regular expression. For more information,
   see
   `Writing a regular expression pattern <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions#Writing_a_regular_expression_pattern>`_ in the
   *JavaScript Regular Expressions* topic on the Mozilla Developer Network.

.. _settings-user-change-run-and-debug:

Run & Debug
-----------

:guilabel:`Save All Unsaved Tabs Before Running`
   If enabled, before running the associated code, |AC9| attempts to save all unsaved files with open tabs.

.. _settings-user-change-preview:

Preview
-------

:guilabel:`Preview Running Apps`
   If enabled, |AC9| attempts to display a preview of the output for the code in the active tab whenever the :guilabel:`Preview` button is chosen.

:guilabel:`Default Previewer`
   The format |AC9| uses to preview code output.

   Valid values include:

   * :guilabel:`Raw` to attempt to display code output in a plain format.
   * :guilabel:`Browser` to attempt to display code output in a format that is preferred for web browsers.

:guilabel:`When Saving Reload Previewer`
   The behavior |AC9| uses for previewing code output whenever a code file is saved.

   Valid values include:

   * :guilabel:`Only on Ctrl-Enter` to attempt to preview code output whenever :kbd:`Ctrl-Enter` is pressed for the current code tab.
   * :guilabel:`Always` to attempt to preview code output whenever a code file is saved.

.. _settings-user-change-build:

Build
-----

:guilabel:`Automatically Build Supported Files`
   If enabled, |AC9| attempts to automatically build the current code if a build action is triggered and the code is in a supported format.
