.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _env-vars:

##################################################################
Working with Custom Environment Variables in the |AC9IDElongtitle|
##################################################################

.. meta::
    :description:
        Describes support for getting and setting custom environment variables in the AWS Cloud9 IDE.

The |AC9IDE| supports getting and setting custom environment variables. You can get and set custom environment variables in the |AC9IDE| in the following ways.

* :ref:`env-vars-command-level`
* :ref:`env-vars-bash-profile`
* :ref:`env-vars-local`
* :ref:`env-vars-bashrc`
* :ref:`env-vars-env-list`

.. _env-vars-command-level:

Set Command-Level Custom Environment Variables
==============================================

You can set command-level custom environment variables as you run a command in your |envfirst|. To test this behavior, create a file named :file:`script.sh` with the following code: 

.. code-block:: sh

   #!/bin/bash

   echo $MY_ENV_VAR

If you run the following command, the terminal displays :code:`Terminal session`:

.. code-block:: sh

   MY_ENV_VAR='Terminal session' sh ./script.sh

If you set the custom environment variable by using multiple approaches described in this topic, then when you try to get the custom environment variable's value,
this setting takes priority over all of the others.

.. _env-vars-bash-profile:

Set Custom User Environment Variables in ~/.bash_profile
========================================================

You can set custom user environment variables in the :file:`~/.bash_profile` file in your |env|. To test this behavior, add the following code to the :file:`~/.bash_profile` file in your |env|:

.. code-block:: sh

   export MY_ENV_VAR='.bash_profile file'

If you then choose the :menuselection:`Run, Run With, Shell script` command on the menu bar, type :code:`./script.sh` in the :guilabel:`Command` box of the runner tab, and then choose :guilabel:`Run`, the runner tab displays :code:`.bash_profile file`. (This 
assumes you created the :file:`script.sh` file as described earlier.)

.. _env-vars-local:

Set Local Custom Environment Variables
======================================

You can set local custom environment variables in a terminal session by running the :command:`export` command. To test this behavior, run the following command in a terminal session:

.. code-block:: sh

   export MY_ENV_VAR='Command line export'

If you then choose the :menuselection:`Run, Run With, Shell script` command on the menu bar, type :code:`./script.sh` in the :guilabel:`Command` box of the runner tab, and then choose :guilabel:`Run`, the runner tab displays :code:`Command line export`. (This 
assumes you created the :file:`script.sh` file as described earlier.)

If you set the same custom environment variable in your :file:`~/.bash_profile` file and with the :command:`export` command, then when you try to get the 
customer environment variable's value, the :file:`~/.bash_profile` file setting takes priority.

.. _env-vars-bashrc:

Set Custom User Environment Variables in ~/.bashrc
==================================================

You can set custom user environment variables in :file:`~/.bashrc` file in your |env|. To test this behavior, add the following code to the :file:`~/.bashrc` file in your |env|:

.. code-block:: sh

   export MY_ENV_VAR='.bashrc file'

If you then choose the :menuselection:`Run, Run With, Shell script` command on the menu bar, type :code:`./script.sh` in the :guilabel:`Command` box of the runner tab, and then choose :guilabel:`Run`, the runner tab displays :code:`.bashrc file`. (This 
assumes you created the :file:`script.sh` file as described earlier.)

If you set the same custom environment variable with the :command:`export` command and in your :file:`~/.bashrc` file, then when you try to get the custom environment variable's value, 
the :command:`export` command setting takes priority.

.. _env-vars-env-list:

Set Custom Environment Variables in the ENV List
================================================

You can set custom environment variables in the :guilabel:`ENV` list on the :guilabel:`Run` tab. 

To test this behavior, do the following:

  #. On the menu bar, choose :menuselection:`Run, Run Configurations, New Run Configuration`.
  #. On the :guilabel:`[New] - Idle` tab,  Choose :guilabel:`Runner: Auto`, and then choose :guilabel:`Shell script`. 
  #. Choose :guilabel:`ENV`, and then type :kbd:`MY_ENV_VAR` for :guilabel:`Name` and :kbd:`ENV list` for :guilabel:`Value`.
  #. For :guilabel:`Command`, type :kbd:`./script.sh`. 
  #. Choose the :guilabel:`Run` button. the runner tab displays :code:`ENV list`. (This assumes you created the :file:`script.sh` file as described earlier.)

If you set the same custom environment variable in your :file:`~/.bash_profile` file, with the :command:`export` command, in your :file:`~/.bashrc` file, and in the :guilabel:`ENV` list, 
then when you try to get the custom environment variable's value, the 
:file:`~/.bash_profile` file setting takes first priority, followed by the :command:`export` command setting, the :file:`~/.bashrc` file setting, and the :guilabel:`ENV` list setting.  

.. note:: The :guilabel:`ENV` list is the only approach for getting and setting custom environment variables by using code, separate from a shell script. 