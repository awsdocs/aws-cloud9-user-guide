.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _language-support:

#########################################
Language Support in the |AC9IDElongtitle|
#########################################

.. meta::
    :description:
        Describes support for various programming languages in AWS Cloud9.

The |AC9IDE| supports many programming languages. The following table lists the languages that are supported
and to what level.

.. list-table::
   :widths: 2 1 1 1 1 1 1
   :header-rows: 1

   * - Language
     - Syntax highlighting :sup:`1`
     - Run UI :sup:`2`
     - Outline view
     - Code hints and linting
     - Code completion
     - Debugging :sup:`3`
   * - C++
     - X
     - X
     - X
     -
     - X :sup:`5`
     - X :sup:`4`
   * - C#
     - X
     -
     - X
     -
     - X :sup:`5`
     -
   * - CoffeeScript
     - X
     - X
     -
     -
     -
     -
   * - CSS
     - X
     -
     -
     -
     - X
     -
   * - Dart
     - X
     -
     -
     -
     -
     -
   * - Go
     - X
     - X
     - X
     - X
     - X :sup:`4`
     - X :sup:`4`
   * - Haskell
     - X
     -
     -
     -
     -
     -
   * - HTML
     - X
     - X
     - X
     -
     - X
     -
   * - Java
     - X
     -
     - X
     -
     - X :sup:`5`
     -
   * - JavaScript
     - X
     - X
     - X
     - X
     - X
     -
   * - Node.js
     - X
     - X
     - X
     - X
     - X
     - X :sup:`6`
   * - PHP
     - X
     - X
     - X
     - X
     - X :sup:`7`
     - X
   * - Python
     - X
     - X
     - X
     - X
     - X :sup:`8`
     - X
   * - Ruby
     - X
     - X
     - X
     - X
     - X :sup:`5`
     -
   * - Shell script
     - X
     - X
     - X
     - X
     - X :sup:`5`
     -

:sup:`1` The |AC9IDE| provides syntax highlighting for many more languages. For a complete list, in the menu bar of the |IDE|, choose :guilabel:`View, Syntax`.

:sup:`2` You can run programs or scripts at the click of a button for languages marked with an **X**, without using the command line. For languages not marked with an **X** or
not displayed on the :guilabel:`Run, Run With` menu bar in the |IDE|,
you can create a runner for that language. For instructions, see :ref:`build-run-debug-create-builder-runner`.

:sup:`3` You can use the IDE's built-in tools to debug programs or scripts for languages marked with an **X**. For instructions, see :ref:`build-run-debug-debug`.

:sup:`4` This feature is in an experimental state for this language. It is not fully implemented and is not documented or supported.

:sup:`5` This feature supports only local functions for this language.

:sup:`6` This feature is not supported for Node.js versions 7.7.0 and later.

:sup:`7` To specify paths for |AC9| to use for completion of custom PHP code, in the |AC9IDE| turn on the :guilabel:`Project, PHP Support, Enable PHP code completion` setting 
in :guilabel:`Preferences`, and then add the paths to the custom code to the :guilabel:`Project, PHP Support, PHP Completion Include Paths` setting.

:sup:`8` To specify paths for |AC9| to use for completion of custom Python code, in the |AC9IDE| turn on the :guilabel:`Project, Python Support, Enable Python code completion` 
setting in :guilabel:`Preferences`, and then add the paths to the custom code to the :guilabel:`Project, Python Support, PYTHONPATH` setting. 
