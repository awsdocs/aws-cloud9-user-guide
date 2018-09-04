.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _settings-project:

######################################################
Working with Project Settings in the |AC9IDElongtitle|
######################################################

.. meta::
    :description:
        Describes how to work with project settings in the AWS Cloud9 IDE.

:dfn:`Project settings`, which apply only to the current |envfirst|, include the following kinds of settings:

* Code editor behaviors, such as whether to use soft tabs and new file line ending behavior
* File types to ignore
* The types of hints and warnings to display or suppress
* Code and formatting behaviors for programming languages such as JavaScript, PHP, Python, and Go
* The types of configurations to use when running and building code

Although project settings apply to only a single |env|, you can apply the project settings for one |env|
to any other |env|.

* :ref:`settings-project-view`
* :ref:`settings-project-apply`
* :ref:`settings-project-change`

.. _settings-project-view:

View or Change Project Settings
===============================

#. On the menu bar, choose :menuselection:`AWS Cloud9, Preferences`.
#. To view the project settings for the current |env|, on the :guilabel:`Preferences` tab, in the side navigation pane, choose :guilabel:`Project Settings`.
#. To change the current project settings for the |env|, change the settings you want in the :guilabel:`Project Settings` pane.

See :ref:`settings-project-change`.

.. _settings-project-apply:

Apply the Current Project Settings for an |envtitle| to Another |envtitle|
==========================================================================

#. In both the source and target |env|, on the menu bar of the |AC9IDE|, choose :guilabel:`AWS Cloud9, Open Your Project Settings`.
#. In the source |env|, copy the contents of the :guilabel:`project.settings` tab that is displayed.
#. In the target |env|, overwrite the contents of the :guilabel:`project.settings` tab with the copied contents from the source |env|.
#. In the target |env|, save the :guilabel:`project.settings` tab.

.. _settings-project-change:

Project Setting Changes You Can Make
====================================

These sections describe the kinds of project settings that you can change on the :guilabel:`Preferences`
tab's :guilabel:`Project Settings` pane.

* :ref:`settings-project-change-ec2-instance`
* :ref:`settings-project-change-code-editor-ace`
* :ref:`settings-project-change-find-in-files`
* :ref:`settings-project-change-hints-and-warnings`
* :ref:`settings-project-change-javascript-support`
* :ref:`settings-project-change-build`
* :ref:`settings-project-change-run-and-debug`
* :ref:`settings-project-change-run-configurations`
* :ref:`settings-project-change-code-formatters`
* :ref:`settings-project-change-php-support`
* :ref:`settings-project-change-python-support`
* :ref:`settings-project-change-go-support`

.. _settings-project-change-ec2-instance:

EC2 Instance
------------

:guilabel:`Stop my environment`
   If the |env| is an |envec2|, after all web browser instances that are connected to the |IDE| for the |env| are closed, the amount of time until 
   |AC9| shuts down the |EC2| instance for the |env|.

.. _settings-project-change-code-editor-ace:

Code Editor (Ace)
-----------------

:guilabel:`Soft Tabs`
   If selected, inserts the specified number of spaces instead of a tab character each time you press :kbd:`Tab`.

:guilabel:`Autodetect Tab Size on Load`
   If selected, |AC9| attempts to guess the tab size.

:guilabel:`New File Line Endings`
   The type of line endings to use for new files.

   Valid options include:

   * :guilabel:`Windows (CRLF)` to end lines with a carriage return and then a line feed.
   * :guilabel:`Unix (LF)` to end lines with just a line feed.

:guilabel:`On Save, Strip Whitespace`
   If selected, |AC9| attempts to remove what it considers to be unnecessary spaces and tabs from a file each time that file is saved.

.. _settings-project-change-find-in-files:

Find in Files
-------------

:guilabel:`Ignore these Files`
   When finding in files, the types of files that |AC9| will ignore.

:guilabel:`Maximum number of files to search (in 1000)`
   When finding in files, the maximum number of files, in multiples of 1,000, that |AC9| will find in
   the current scope.

.. _settings-project-change-hints-and-warnings:

Hints & Warnings
----------------

:guilabel:`Warning Level`
   The minimum level of messages to enable.

   Valid values include:

   * :guilabel:`Info` to enable informational, warning, and error messages.
   * :guilabel:`Warning` to enable just warning and error messages.
   * :guilabel:`Error` to enable just error messages.

:guilabel:`Mark Missing Optional Semicolons`
   If enabled, |AC9| flags in a file each time it notices a semicolon that could be used in code, but
   that isn't used.

:guilabel:`Mark Undeclared Variables`
   If enabled, |AC9| flags in a file each time it notices an undeclared variable in code.

:guilabel:`Mark Unused Function Arguments`
   If enabled, |AC9| flags in a file each time it notices an unused argument in a function.

:guilabel:`Ignore Messages Matching Regex`
   |AC9| will not display any messages matching the specified regular expression. For more information, see
   `Writing a regular expression pattern <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions#Writing_a_regular_expression_pattern>`_ in the
   *JavaScript Regular Expressions* topic on the Mozilla Developer Network.

.. _settings-project-change-javascript-support:

JavaScript Support
------------------

:guilabel:`Customize JavaScript Warnings With .eslintrc`
   If enabled, |AC9| uses an :file:`.eslintrc` file to determine which JavaScript warnings to enable or disable.
   For more information, see `Configuration File Formats <http://eslint.org/docs/user-guide/configuring#configuration-file-formats>`_ on the ESLint website.

:guilabel:`JavaScript Library Code Completion`
   The JavaScript libraries |AC9| uses to attempt to suggest or do automatic code completion.

:guilabel:`Format Code on Save`
   If enabled, |AC9| attempts to format the code in a JavaScript file every time that file is saved.

:guilabel:`Use Builtin JSBeautify as Code Formatter`
   If enabled, |AC9| uses its internal implementation of JSBeautify to attempt to increase the readability of code in files.

:guilabel:`Custom Code Formatter`
   The command for |AC9| to attempt to run when formatting code in a JavaScript file.

.. _settings-project-change-build:

Build
-----

:guilabel:`Builder Path in environment`
   The path to any custom build configurations.

.. _settings-project-change-run-and-debug:

Run & Debug
-----------

:guilabel:`Runner Path in Environment`
   The path to any custom run configurations.

:guilabel:`Preview URL`
   The URL to use to preview applications for the |env|.

.. _settings-project-change-run-configurations:

Run Configurations
------------------

The custom run configurations for this |env|.

:guilabel:`Remove Selected Configs`
   Deletes the selected run configurations.

:guilabel:`Add New Config`
   Creates a new run configuration.

:guilabel:`Set As Default`
   Sets the selected run configuration as the default run configuration.

.. _settings-project-change-code-formatters:

Code Formatters
---------------

:guilabel:`JSBeautify settings`
   Settings for increasing the readability of code in files.

   :guilabel:`Format Code on Save`
      If enabled, |AC9| attempts to apply JSBeautify settings whenever code files are saved.

   :guilabel:`Use JSBeautify for JavaScript`
      If enabled, |AC9| attempts to apply JSBeautify settings whenever JavaScript files are saved.

   :guilabel:`Preserve Empty Lines`
      If enabled, |AC9| does not remove empty lines in code files.

   :guilabel:`Keep Array Indentation`
      If enabled, |AC9| preserves the indentation of element declarations in arrays in code files.

   :guilabel:`JSLint Strict Whitespace`
      If enabled, |AC9| attempts to apply JSLint whitespace rules in code files. For more information, see "Whitespace" in `JSLint Help <http://jslint.com/help.html>`_.

   :guilabel:`Braces`
      Specifies the alignment of braces in code.

      Valid values include:

      * :guilabel:`Braces with control statement` to move each beginning and end brace to align with its related control statement, as needed.

        For example, this code:

        .. code-block:: javascript

           for (var i = 0; i < 10; i++) { if (i == 5) { console.log("Halfway done.") }}

        Turns into this code when the file is saved:

        .. code-block:: javascript

           for (var i = 0; i < 10; i++) {
              if (i == 5) {
                 console.log("Halfway done.")
              }
           }

      * :guilabel:`Braces on own line` to move each brace to its own line, as needed.

        For example, this code:

        .. code-block:: javascript

           for (var i = 0; i < 10; i++) { if (i == 5) { console.log("Halfway done.") }}

        Turns into this code when the file is saved:

        .. code-block:: javascript

           for (var i = 0; i < 10; i++) {if (i == 5)
             {
                console.log("Halfway done.")
             }
             }

      * :guilabel:`End braces on own line` to move each end brace to its own line, as needed.

        For example, this code:

        .. code-block:: javascript

           for (var i = 0; i < 10; i++) {
             if (i == 5) { console.log("Halfway done.") }
           }

        Turns into this code when the file is saved:

        .. code-block:: javascript

           for (var i = 0; i < 10; i++) {
              if (i == 5) {
                 console.log("Halfway done.")
              }
           }

   :guilabel:`Space Before Conditionals`
      If enabled, |AC9| adds a space before each conditional declaration, as needed.

   :guilabel:`Unescape Strings`
      If enabled, |AC9| converts escaped strings to their unescaped equivalents. For example, converts
      :code:`\n` to a newline character and converts :code:`\r` to a carriage return character.

   :guilabel:`Indent Inner Html`
      If enabled, |AC9| indents :code:`<head>` and :code:`<body>` sections in HTML code.

.. _settings-project-change-php-support:

PHP Support
-----------

:guilabel:`Enable PHP code Completion`
   If enabled, |AC9| attempts to complete PHP code.

:guilabel:`PHP Completion Include Paths`
   Locations that |AC9| uses to attempt to help complete PHP code. For example, if you have custom PHP files that 
   you want |AC9| to use for completion, and those files are somewhere in the :file:`~/environment` directory, add 
   :code:`~/environment` to this path.

:guilabel:`Format Code on Save`
   If enabled, |AC9| attempts to format PHP code whenever PHP files are saved.

:guilabel:`Custom Code Formatter`
   The path to any custom code formatting configuration for PHP code.

.. _settings-project-change-python-support:

Python Support
--------------

:guilabel:`Enable Python code completion`
   If enabled, |AC9| attempts to complete Python code. To set the paths for |AC9| to use to complete Python code, use the :guilabel:`PYTHONPATH` setting.

:guilabel:`Python Version`
   Specifies the version of Python to use.

:guilabel:`Pylint command-line options`
   Options for |AC9| to use for Pylint wih Python code. For more information, see the `Pylint User Manual <https://pylint.readthedocs.io/en/latest/>`_ on the Pylint website.

:guilabel:`PYTHONPATH`
   The paths to Python libraries and packages for |AC9| to use. For example, if you have custom Python libraries and packages 
   in the :file:`~/environment` directory, add :code:`~/environment` to this path.

:guilabel:`Format Code on Save`
   If enabled, |AC9| attempts to format Python code whenever Python files are saved.

:guilabel:`Custom Code Formatter`
   The path to any custom code formatting configuration for Python code.

.. _settings-project-change-go-support:

Go Support
----------

:guilabel:`Enable Go code completion`
   If enabled, |AC9| attempts to complete Go code.

:guilabel:`Format Code on Save`
   If enabled, |AC9| attempts to format Go code whenever Go files are saved.

:guilabel:`Custom Code Formatter`
   The path to any custom code formatting configuration for Go code.