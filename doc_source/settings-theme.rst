.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _settings-theme:

############################################
Working with Themes in the |AC9IDElongtitle|
############################################

.. meta::
    :description:
        Describes how to work with themes in the AWS Cloud9 IDE.

A :dfn:`theme` defines your overall IDE colors. This applies across each |envfirst| associated with your |IAM| user.
As you make changes to your theme, |AC9| pushes those changes to the cloud, and
associates them with your |IAM| user. |AC9| also continually scans the cloud for changes to the theme
associated with your |IAM| user, and applies those changes
to your current |env|.

You can share any custom theme overrides you define with other users.

* :ref:`settings-theme-view`
* :ref:`settings-theme-change`
* :ref:`settings-theme-code`
* :ref:`settings-theme-share`

.. _settings-theme-view:

View or Change Your Theme
=========================

#. On the menu bar, choose :menuselection:`AWS Cloud9, Preferences`.
#. To view your theme across each |env| of yours, on the :guilabel:`Preferences` tab, in the
   side navigation pane, choose :guilabel:`Themes`.
#. To change your theme across each |env| of yours, in the :guilabel:`Themes` pane, change
   the settings you want. To change portions of your theme by using code, choose the
   :guilabel:`your stylesheet` link.
#. To apply your changes to any |env| of yours, simply open that |env|. If that |env| is
   already open, refresh the web browser tab for that |env|.

.. _settings-theme-change:

Overall Theme Settings You Can Change
=====================================

You can change the following kinds of overall theme settings on the :guilabel:`Preferences`
tab in the :guilabel:`Themes` pane.

:guilabel:`Flat Theme`
   Applies the built-in flat theme across the |AC9IDE|.

:guilabel:`Classic Theme`
   Applies the selected built-in classic theme across the |AC9IDE|.

:guilabel:`Syntax Theme`
   Applies the selected theme to code files across the |AC9IDE|.

.. _settings-theme-code:

Theme Overrides You Can Define with Code
========================================

You can override portions of the overall theme in the |AC9IDE|. These overrides will persist even if you change the overall theme itself in the |AC9IDE|.

For example, let's say you want to change the background color of the titles on open tabs to yellow, regardless of the related setting for the current overall theme
that is currently applied to the |AC9IDE|.

First, use your web browser's developer tools to determine the CSS class for the portion of the theme you
want to change. For example, do the following for Google Chrome.

#. Choose :menuselection:`Customize and control Google Chrome, More tools, Developer tools`.
#. In the :guilabel:`Developer tools` pane, choose :guilabel:`Select an element in the page to inspect it`.
#. Pause your mouse over the portion of the IDE you want to change. In this example, pause your mouse
   over the title of an open tab.
#. Note the CSS class name. In this example, the CSS class name for the title of an open tab is :code:`sessiontab_title`.

Next, add a corresponding CSS class selector to your :file:`styles.css` file.

#. On the menu bar, choose :menuselection:`AWS Cloud9, Preferences`. In the side navigation pane, choose
   :guilabel:`Themes`. Then choose the :guilabel:`your stylesheet` link.
#. In the :file:`styles.css` file, add the CSS class selector. In this example, you use the
   :code:`.sessiontab_title` selector to set :code:`background-color` to :code:`yellow`.

   .. code-block:: css

      .sessiontab_title {
        background-color: yellow;
      }

Finally, save the :file:`styles.css` file, and note the change to the theme. In this example, the background color of the titles of open tabs changes to yellow.
Even if you change the overall theme in the |AC9IDE|, the CSS overrides in your :file:`styles.css` file persist.

.. note:: To revert this theme override, remove the preceding code from the :file:`styles.css` file, and then save the file again.

.. _settings-theme-share:

Share Your Theme Overrides with Another User
============================================

#. In both the source and target |env|, on the menu bar of the |AC9IDE|, choose :guilabel:`AWS Cloud9, Open Your Stylesheet`.
#. In the source |env|, copy the contents of the :guilabel:`styles.css` tab that is displayed.
#. In the target |env|, overwrite the contents of the :guilabel:`styles.css` tab with the copied contents from the source |env|.
#. In the target |env|, save the :guilabel:`styles.css` tab.
