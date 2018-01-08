.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _file-preview:

#########################################
Previewing Files in the |AC9IDElongtitle|
#########################################

.. meta::
    :description:
        Describes how to preview a file from within the AWS Cloud9 IDE.

You can use the |AC9IDE| to preview the files in a |envfirst| from within the IDE.

* :ref:`file-preview-file-open`
* :ref:`file-preview-file-reload`
* :ref:`file-preview-file-preview-type`
* :ref:`file-preview-file-open-tab`
* :ref:`file-preview-file-switch`

.. _file-preview-file-open:

Open a File for Preview
=======================

Do one of the following in the |AC9IDE| to open a file preview tab within the |env|:

* In the :guilabel:`Environment` window, right-click the file you want to preview, and then choose :guilabel:`Preview`.

  .. note:: Although you can use this approach to preview any file, preview works best with files that
     have the following file extensions:

     * :file:`.htm`
     * :file:`.html`
     * :file:`.pdf`
     * :file:`.svg`
     * :file:`.xhtml`
     * Any file containing content in Markdown format.

* Open a file with one of the following file extensions:

  * :file:`.pdf`
  * :file:`.svg`

* With the file you want to preview already open and active, on the menu bar, choose :guilabel:`Preview, Preview File FILE_NAME`. Or
  choose :guilabel:`Tools, Preview, Preview File FILE_NAME`, where :guilabel:`FILE_NAME` is the name of
  the file you want to preview.

  .. note:: These commands work only with the following file types:

     * :file:`.htm`
     * :file:`.html`
     * :file:`.markdown`
     * :file:`.md`
     * :file:`.pdf`
     * :file:`.svg`
     * :file:`.txt`: Preview works best if the file's content is in Markdown format.
     * :file:`.xhtml`: Preview works best if the file contains or references content presentation
       information.

.. note:: The :guilabel:`Preview Settings` menu in the file preview tab is currently not functional and
   choosing any of its menu commands will have no effect.

.. _file-preview-file-reload:

Reload a File Preview
=====================

On the file preview tab, choose the :guilabel:`Refresh` button (the circular arrow).

.. _file-preview-file-preview-type:

Change the File Preview Type
============================

On the file preview tab, choose one of the following in the preview type list:

  * :guilabel:`Browser`: Previews the file in a web browser format, for the following file types
    only:

    * :file:`.htm`
    * :file:`.html`
    * :file:`.pdf`
    * :file:`.svg`
    * :file:`.xhtml`: Preview works best if the file contains or references content presentation
      information.

  * :guilabel:`Raw Content (UTF-8)`: Previews the file's original contents in Unicode Transformation
    Format 8-bit (UTF-8) format.
    This might display unexpected content for some file types.
  * :guilabel:`Markdown`: Previews any file containing Markdown format. Attempts to preview any
    other file type, but might display unexpected content.

.. _file-preview-file-open-tab:

Open a File Preview in a Separate Web Browser Tab
=================================================

On the file preview tab, choose :guilabel:`Pop Out Into New Window`.

.. _file-preview-file-switch:

Switch to a Different File Preview
==================================

On the file preview tab, type the path to a different file path in the address bar. The address bar is
located between the :guilabel:`Refresh` button and the preview type list.

