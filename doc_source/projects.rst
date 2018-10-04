.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _projects:

#######################################################
Working with Language Projects in the |AC9IDElongtitle|
#######################################################

.. meta::
    :description:
        Describes additional developer productivity features that are available with supported language projects in the AWS Cloud9 IDE.

The |AC9IDE| provides project productivity features for some languages in addition to those languages listed in
:ref:`Language Support <language-support>`. To use these features, you use the |IDE| to create or identify a :dfn:`language project`
(or :dfn:`project`) based on that language. 
A project is a collection of related files, folders, and settings in the |IDE| for an
|envfirstlong|.

To use the |IDE| to create a language project in your |env|, see :ref:`projects-create`.

.. _projects-features:

Available Project Productivity Features
=======================================

The |AC9IDE| provides the following project productivity features by programming language.

.. list-table::
   :widths: 1 2 2 2 2 2
   :header-rows: 1

   * - **Language**
     - :ref:`projects-features-autocomplete`
     - :ref:`projects-features-gutter-icons`
     - :ref:`projects-features-find-refs`
     - :ref:`projects-features-go-to-def`
     - :ref:`projects-features-go-to-symbol`
   * - TypeScript
     - X
     - X
     - X
     - X
     - X

.. _projects-features-autocomplete:

Autocomplete
------------

As you type in a file in the editor, a list of symbols is displayed at the insertion point for that context, if any symbols are available there.

To insert a symbol from the list at the insertion point, if the symbol isn't already chosen, choose it by using your up arrow or down arrow key, and then press :kbd:`Tab`.

Before you press :kbd:`Tab`, you might see a screentip that contains information about the symbol you chose, if information is available.

To close the list without inserting a symbol, press :kbd:`Esc`.

.. _projects-features-gutter-icons:

Gutter Icons
------------

Icons might appear in the gutter for the active file. These icons highlight possible issues such as warnings and errors in code before you run it.

For more information about an issue, pause your mouse pointer on the issue's icon.

.. _projects-features-find-refs:

Find References
---------------

In the active file in the editor, you can display all references to the symbol at the insertion point, if the |IDE| has access to those references.

To do this, at the insertion point anywhere within the symbol, run the :command:`Find References` command. For example:

* Right-click at the insertion point, and then choose :guilabel:`Find References`.
* On the menu bar, choose :guilabel:`Go, Find References`.
* Press :kbd:`Shift-F3` by default for macOS, Windows, or Linux.

If references are available, a pane opens on top of the active file, next to that symbol. The pane contains a list of the files where the symbol is referenced.
The pane displays the first reference in the list. To display a different reference, choose that reference in the list.

To close the pane, choose the close (:guilabel:`X`) icon in the pane, or press :kbd:`Esc`.

The :command:`Find References` command might be disabled, or might not work as expected, under the following conditions:

* There are no references to that symbol in the active file's project.
* The |IDE| can't find some or all of that symbol's references in the active file's project.
* The |IDE| doesn't have access to one or more locations where that symbol is referenced in the active file's project.

.. _projects-features-go-to-def:

Go to Definition
----------------

In the active file in the editor, you can go from a symbol to where that symbol is defined, if the |IDE| has access to that definition.

To do this, at the insertion point anywhere within the symbol, run the :command:`Jump to Definition` command. For example:

* Right-click at the insertion point, and then choose :guilabel:`Jump to Definition`.
* On the menu bar, choose :guilabel:`Go, Jump to Definition`.
* Press :kbd:`F3` by default for macOS, Windows, or Linux.

If the definition is available, the insertion point switches to that definition, even if that definition is in a separate file.

The :command:`Jump to Definition` command might be disabled, or might not work as expected, under the following conditions:

* The symbol is a primitive symbol for that language.
* The |IDE| can't find the definition's location in the active file's project.
* The |IDE| doesn't have access to the definition's location in the active file's project.

.. _projects-features-go-to-symbol:

Go to Symbol
------------

You can go to a specific symbol within a project, as follows.

#. Make one of the files in the project active by opening it in the editor. If the file is already open, choose its tab in the editor to make that file the active one.
#. Run the :command:`Go to Symbol` command. For example:

   * Choose the :guilabel:`Go` window button (magnifying glass icon). In the :guilabel:`Go to Anything` box, type :kbd:`@`, and then start typing the symbol.
   * On the menu bar, choose :guilabel:`Go, Go To Symbol`. In the :guilabel:`Go` window, start typing the symbol after :guilabel:`@`.
   * Press :kbd:`Command-2` or :kbd:`Command-Shift-O` by default for macOS, or :kbd:`Ctrl-Shift-O` by default for Windows or Linux. 
     In the :guilabel:`Go` window, start typing the symbol after :guilabel:`@`.

   For example, to find all symbols in the project named :code:`toString`, start typing :code:`@toString` (or start typing :code:`toString` after :guilabel:`@`, if :guilabel:`@` is already displayed).

#. If you see the symbol you want in the :guilabel:`Symbols` list, choose it by clicking it. Or use your up arrow or down arrow key to select it, and then press :kbd:`Enter`. The
   insertion point then switches to that symbol.

If the symbol that you want to go to isn't in the active file's project, this procedure might not work as expected.

.. _projects-create:

Create a Language Project
=========================

Use the following procedure to create a language project that will work with supported project productivity features in the |AC9IDE|.

.. note:: We recommend that you use supported project productivity features on files that are part of a language project. Although you can 
   use some supported project productivity features on a file that isn't part of a project, those features might behave with unexpected results.

   For example, you might use the |IDE| to search for references and definitions from within a file
   at the root level of an |env| that isn't part of a project. The |IDE| might then search only across files at that same root level.
   This might result in no references or definitions found, even though those references or definitions actually exist in
   language projects elsewhere across the same |env|.

.. _projects-create-typescript:

Create a TypeScript Language Project
------------------------------------

#. Ensure you have TypeScript installed in the |env|. For more information, see :ref:`Step 1: Install Required Tools <sample-typescript-install>` in :ref:`TypeScript Sample <sample-typescript>`.
#. From a terminal session in the |IDE| for the |env|, switch to the directory where you want to create the project. If the directory doesn't exist, create it and then
   switch to it. For example, the following commands create a directory named :file:`my-demo-project` at the root of the |env| (in :file:`~/environment`), and then switch to that directory.

   .. code-block:: sh

      mkdir ~/environment/my-demo-project
      cd ~/environment/my-demo-project

#. At the root of the directory where you want to create the project, run the TypeScript compiler with the :command:`--init` option.

   .. code-block:: sh

      tsc --init

   If this command is successful, the TypeScript compiler creates a :file:`tsconfig.json` file in the root of the directory for the project.
   You can use this file to define various project settings, such as TypeScript compiler options and specific files to include or exclude from the project.

   For more information about the :file:`tsconfig.json` file, see the following:

   * `tsconfig.json Overview <https://www.typescriptlang.org/docs/handbook/tsconfig-json.html>`_ on the TypeScript website.
   * `tsconfig.json Schema <http://json.schemastore.org/tsconfig>`_ on the json.schemastore.org website.