.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _settings-keybindings:

#################################################
Working with Keybindings in the |AC9IDElongtitle|
#################################################

.. meta::
    :description:
        Describes how to work with keybindings in the AWS Cloud9 IDE.

:dfn:`Keybindings` define your shortcut key combinations. Keybindings apply across each |envfirst| associated with your |IAM| user.
As you make changes to your keybindings, |AC9| pushes those changes to the cloud,
and associates them with your |IAM| user. |AC9| also continually scans the cloud for changes to keybindings
associated with your |IAM| user, and applies those changes
to your current |env|.

You can share your keybindings with other users.

* :ref:`settings-keybindings-view`
* :ref:`settings-keybindings-share`
* :ref:`settings-keybindings-mode`
* :ref:`settings-keybindings-os`
* :ref:`settings-keybindings-change`
* :ref:`settings-keybindings-reset`

.. _settings-keybindings-view:

View or Change Your Keybindings
===============================

#. On the menu bar, choose :menuselection:`AWS Cloud9, Preferences`.
#. To view your keybindings across each |env| of yours, on the :guilabel:`Preferences` tab, in the
   side navigation pane, choose :guilabel:`Keybindings`.
#. To change your keybindings across each |env| of yours, in the :guilabel:`Keybindings` pane,
   change the settings you want.
#. To apply your changes to any |env|, simply open that |env|. If that |env| is
   already open, refresh the web browser tab for that |env|.

For more information, see the following:

* :doc:`Apple OSX Default Keybindings Reference <keybindings-default-apple-osx>`
* :doc:`Apple OSX Vim Keybindings Reference <keybindings-vim-apple-osx>`
* :doc:`Apple OSX Emacs Keybindings Reference <keybindings-emacs-apple-osx>`
* :doc:`Apple OSX Sublime Keybindings Reference <keybindings-sublime-apple-osx>`
* :doc:`Windows / Linux Default Keybindings Reference <keybindings-default-windows-linux>`
* :doc:`Windows / Linux Vim Keybindings Reference <keybindings-vim-windows-linux>`
* :doc:`Windows / Linux Emacs Keybindings Reference <keybindings-emacs-windows-linux>`
* :doc:`Windows / Linux Sublime Keybindings Reference <keybindings-sublime-windows-linux>`

.. _settings-keybindings-share:

Share Your Keybindings with Another User
========================================

#. In both the source and target |env|, on the menu bar of the |AC9IDE|, choose :guilabel:`AWS Cloud9, Open Your Keymap`.
#. In the source |env|, copy the contents of the :guilabel:`keybindings.settings` tab that is displayed.
#. In the target |env|, overwrite the contents of the :guilabel:`keybindings.settings` tab with the copied contents from the source |env|.
#. In the target |env|, save the :guilabel:`keybindings.settings` tab.

.. _settings-keybindings-mode:

Change Your Keyboard Mode
=========================

You can change the keyboard mode that the |AC9IDE| uses for interacting with text in the editor across
each |env| associated with your |IAM| user.

#. On the menu bar, choose :menuselection:`AWS Cloud9, Preferences`.
#. On the :guilabel:`Preferences` tab, in the side navigation pane, choose :guilabel:`Keybindings`.
#. For :guilabel:`Keyboard Mode`, choose one of these keyboard modes:

   * :guilabel:`Default` to use a set of default keybindings.
   * :guilabel:`Vim` to use Vim mode. For more information, see the `Vim help files <https://vimhelp.appspot.com/>`_ website.
   * :guilabel:`Emacs` to use Emacs mode. For more information, see `The Emacs Editor <https://www.gnu.org/software/emacs/manual/html_node/emacs/index.html>`_ on the GNU Operating System website.
   * :guilabel:`Sublime` to use Sublime mode. For more information, see the `Sublime Text Documentation <https://www.sublimetext.com/docs/3/>`_ website.

.. _settings-keybindings-os:

Change Your Operating System Keybindings
========================================

You can change the set of operating system keybindings the |AC9IDE| recognizes across each |env| associated with your |IAM| user.

#. On the menu bar, choose :menuselection:`AWS Cloud9, Preferences`.
#. On the :guilabel:`Preferences` tab, in the side navigation pane, choose :guilabel:`Keybindings`.
#. For :guilabel:`Operating System`, choose one of these operating systems:

   * :guilabel:`Auto` for the |AC9IDE| to attempt to detect which set of operating system keybindings to use.
   * :guilabel:`Apple OSX` for the |AC9IDE| to use the keybindings listed in Mac format.
   * :guilabel:`Windows / Linux` for the |AC9IDE| to use the keybindings listed in Windows and Linux formats.

.. _settings-keybindings-change:

Change Specific Keybindings
===========================

You can change individual keybindings across each |env| associated with your |IAM| user.

.. topic:: To change one keybinding at a time

   #. On the menu bar, choose :menuselection:`AWS Cloud9, Preferences`.
   #. On the :guilabel:`Preferences` tab, in the side navigation pane, choose :guilabel:`Keybindings`.
   #. In the list of keybindings, double-click the keybinding in the :guilabel:`Keystroke` column you want to change.
   #. Use the keyboard to specify the replacement key combination, and then press :kbd:`Enter`.

      .. note:: To completely remove the current key combination, press :kbd:`Backspace` for Windows or Linux, or :kbd:`Delete` for Mac.

.. topic:: To change multiple keybindings at once

   #. On the menu bar, choose :menuselection:`AWS Cloud9, Open Your Keymap`.
   #. In the :file:`keybindings.settings` file, define each keybinding to be changed, for example:

      .. code-block:: json

         [
           {
             "command": "addfavorite",
             "keys": {
               "win": ["Ctrl-Alt-F"],
               "mac": ["Ctrl-Option-F"]
             }
           },
           {
             "command": "copyFilePath",
             "keys": {
               "win": ["Ctrl-Shift-F"],
               "mac": ["Alt-Shift-F"]
             }
           }
         ]

      In the example, :code:`addFavorite` and :code:`copyFilePath` are the names of keybindings
      in the :guilabel:`Keystroke` column in the :guilabel:`Keybindings` pane on the :guilabel:`Preferences`
      tab.
      The keybindings you want are :code:`win` and :code:`mac` for Windows
      or Linux and Mac, respectively.

      To apply your changes, save the :file:`keybindings.settings` file. Your changes should appear in the :guilabel:`Keybindings` pane after a short delay.

.. _settings-keybindings-reset:

Remove All of Your Custom Keybindings
=====================================

You can remove all custom keybindings and restore all keybindings to their default values, across each |env| associated with your |IAM| user.

.. caution:: You cannot undo this action.

#. On the menu bar, choose :menuselection:`AWS Cloud9, Preferences`.
#. On the :guilabel:`Preferences` tab, in the side navigation pane, choose :guilabel:`Keybindings`.
#. Choose :guilabel:`Reset to Defaults`.
