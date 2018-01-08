.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _sample-github:

###########################
GitHub Sample for |AC9long|
###########################

.. meta::
    :description:
        Provides a hands-on sample that you can use to experiment with a GitHub repository in AWS Cloud9.

This sample enables you to set up an |envfirst| to interact with a remote code repository in GitHub. For more information about
GitHub, see the `GitHub <https://github.com/>`_ and `GitHub Help <https://help.github.com/>`_ websites.

* :ref:`sample-github-create-account`
* :ref:`sample-github-create-repo`
* :ref:`sample-github-install-git`
* :ref:`sample-github-clone-repo`
* :ref:`sample-github-add-files`
* :ref:`sample-github-explore`
* :ref:`sample-github-clean-up`

.. note::

   .. include:: _sample-prereqs.txt

   Creating this sample might result in charges to your AWS account. These include possible charges for services such as |EC2|. For more information, see
   `Amazon EC2 Pricing <https://aws.amazon.com/ec2/pricing/>`_.

Start with the following step, depending on what you already have.

.. list-table::
   :widths: 1 1 1 3
   :header-rows: 1

   * - **Do you have a GitHub account?**
     - **Do you have a GitHub repository?**
     - **Do you have Git installed?**
     - **Start with this step**
   * - No
     - --
     - --
     - :ref:`sample-github-create-account`
   * - Yes
     - No
     - --
     - :ref:`sample-github-create-repo`
   * - Yes
     - Yes
     - No (or Not Sure)
     - :ref:`sample-github-install-git`
   * - Yes
     - Yes
     - Yes
     - :ref:`sample-github-clone-repo`

.. _sample-github-create-account:

Step 1: Create a GitHub Account
===============================

If you already have a GitHub account, skip ahead to :ref:`sample-github-create-repo`.

To create a GitHub account, see `Join GitHub <https://github.com/join>`_ on the GitHub website.

.. _sample-github-create-repo:

Step 2: Create a GitHub Repository
==================================

If you already have a GitHub repository, skip ahead to :ref:`sample-github-install-git`.

To create the repository, see `Create A Repo <https://help.github.com/articles/create-a-repo/>`_ on the GitHub Help website.

.. _sample-github-install-git:

Step 3: Install Git in Your |envtitle|
======================================

In this step, you use the |AC9IDE| to install Git in your |env| so that you can clone your remote repository into the |env| later.

If you already have Git installed in your |env|, skip ahead to :ref:`sample-github-clone-repo`. To check whether you already have Git installed, run the
:command:`git --version` command as described in this step.

#. With your |env| open, in the |AC9IDE|, start a new terminal session, if one isn't already started.
   (To start a new terminal session, on the
   menu bar, choose :menuselection:`Window, New Terminal`.)
#. Check whether Git is already installed. In the terminal, run the :command:`git --version` command.
   If Git is installed, the version number is displayed,
   for example, :samp:`git version {N.N.N}`. The installed version must be 1.7.9 or later. If it is, skip ahead to step 4 in this procedure to set your Git name and email address.
#. To install Git, see `Git Downloads <https://git-scm.com/downloads>`_ on the Git website. For example, for an |envec2| running Amazon Linux,
   run these three commands in the terminal, one at a time, to install Git.

   .. code-block:: sh

      sudo yum -y update      # Install the latest system updates.
      sudo yum -y install git # Install Git.
      git --version           # Confirm Git was installed.

#. Set your Git name and email address. In the terminal, run these two commands, one at a time, substituting your Git name and email address for :samp:`{USER_NAME}` and
   :samp:`{EMAIL_ADDRESS}`.

   .. code-block:: sh

      git config --global user.name "USER_NAME"
      git config --global user.email EMAIL_ADDRESS

.. _sample-github-clone-repo:

Step 4: Clone the Remote Repository into Your |envtitle|
========================================================

In this step, you use the |AC9IDE| to clone the remote repository in GitHub into your |env|.

To clone the repository, see `Cloning a Repository <https://help.github.com/articles/cloning-a-repository/#platform-linux>`_ on the GitHub website.

.. note:: The rest of this sample assumes the current working directory that you clone the repository
   into is the |env| root directory. If you clone it somewhere else,
   substitute that location wherever you see :samp:`/{YOUR_CLONED_REPO_NAME}`.

.. _sample-github-add-files:

Step 5: Add Files to the Repository
===================================

In this step, you create three simple files in the cloned repository in your |env|. Then you add the files
to the Git staging area in your cloned repository, commit the staged files, and push the
commit to your remote repository in GitHub.

If the cloned repository already has files in it, skip ahead to :ref:`sample-github-explore`.

#. Create a new file. On the menu bar, choose :menuselection:`File, New File`.
#. Type the following content into the file, and then choose :menuselection:`File, Save` to save the file
   as :file:`bird.txt`
   in the :samp:`/{YOUR_CLONED_REPO_NAME}` directory in your |env|.

   .. code-block:: text

      bird.txt
      --------
      Birds are a group of endothermic vertebrates, characterized by feathers,
      toothless beaked jaws, the laying of hard-shelled eggs, a high metabolic
      rate, a four-chambered heart, and a lightweight but strong skeleton.

   .. note:: To confirm you are saving this file in the correct directory, in the :guilabel:`Save As` dialog box, choose the :samp:`{YOUR_CLONED_REPO_NAME}` folder, and
      be sure :guilabel:`Folder` displays :samp:`/{YOUR_CLONED_REPO_NAME}`.

#. Create two more files, named :file:`insect.txt` and :file:`reptile.txt`, with the following content,
   saving them also in the same :samp:`/{YOUR_CLONED_REPO_NAME}` directory.

   .. code-block:: text

      insect.txt
      ----------
      Insects are a class of invertebrates within the arthropod phylum that
      have a chitinous exoskeleton, a three-part body (head, thorax, and abdomen),
      three pairs of jointed legs, compound eyes, and one pair of antennae.

   .. code-block:: text

      reptile.txt
      -----------
      Reptiles are tetrapod (four-limbed vertebrate) animals in the class
      Reptilia, comprising today's turtles, crocodilians, snakes,
      amphisbaenians, lizards, tuatara, and their extinct relatives.

#. In the terminal, run the :command:`cd` command to switch to the :samp:`/{YOUR_CLONED_REPO_NAME}` directory.

   .. code-block:: sh

      cd YOUR_CLONED_REPO_NAME

#. Confirm the files were successfully saved in the :samp:`/{YOUR_CLONED_REPO_NAME}` directory by running
   the :command:`git status` command. All three files are listed as untracked files.

   .. code-block:: text

      Untracked files:
        (use "git add <file>..." to include in what will be committed)

              bird.txt
              insect.txt
              reptile.txt

#. Add the files to the Git staging area by running the :command:`git add` command.

   .. code-block:: sh

      git add --all

#. Confirm the files were successfully added to the Git staging area by running the :command:`git status`
   command again. All three files are now listed as changes to commit.

   .. code-block:: text

      Changes to be committed:
        (use "git reset HEAD <file>..." to unstage)

              new file:   bird.txt
              new file:   insect.txt
              new file:   reptile.txt

#. Commit the staged files by running the :command:`git commit` command.

   .. code-block:: sh

      git commit -m "Added information about birds, insects, and reptiles."

#. Push the commit to your remote repository in |ACC| by running the :command:`git push` command.

   .. code-block:: sh

      git push

   .. note:: You are prompted for your GitHub user name and password. As you continue to work with GitHub,
      you might be prompted again. To keep from being prompted each time you try to interact with the
      remote repository in the future, consider
      installing and configuring a Git credentials manager. For example, you can run this command in the terminal to be prompted no sooner than every 15 minutes:
      :code:`git config credential.helper 'cache --timeout 900'`. Or you can run this command to never be prompted again, although Git stores your credentials in clear text in
      a plain file in your home directory: :code:`git config credential.helper 'store --file ~/.git-credentials'`.
      For more information, see `Git Tools - Credential Storage <https://git-scm.com/book/en/v2/Git-Tools-Credential-Storage>`_ on the Git website.

      If you use GitHub two-factor authentication, you must enter a personal access token whenever you are prompted for a password. If you enter a password instead of a personal
      access token, an "invalid user name or password" message is displayed, and the operation fails.
      For more information, see `Creating a personal access token for the command line <https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/>`_ on the GitHub Help website.

      You will not see your password or personal access token whenever you enter it in the terminal. This is by design.

#. To confirm whether the files were successfully pushed from your local copy of the repository to the remote repository, open your repository in the GitHub console, and look for the three files you just pushed.

.. _sample-github-explore:

Step 6: Keep Working with the |IDE| and GitHub
==============================================

Use the |AC9IDE| and GitHub to keep working with your code. Here are some things to try.

* Use the :guilabel:`Environment` window and editor tabs in the |IDE| to view, change, and save code. For more information, see :ref:`tutorial-environment` and
  :ref:`tutorial-editor` in the *Tutorial for AWS Cloud9*.
* Use the |IDE| to run, debug, and build your code. For more information, see :ref:`Working with Builders, Runners, and Debuggers <build-run-debug>`.
* Use Git in the terminal session in the |IDE| to continue pushing more code changes to the
  GitHub repository, as well as periodically pull code changes from others from the repository.
  For more information, see `Pushing to a Remote <https://help.github.com/articles/pushing-to-a-remote/>`_
  and `Fetching a remote <https://help.github.com/articles/fetching-a-remote/>`_ on the GitHub Help website.
* Use additional Git commands as you need them. For a list of these commands, see `Git cheatsheet <https://help.github.com/articles/git-cheatsheet/>`_ on the GitHub Help website.
* If you're new to Git and you don't want to mess up your GitHub repository, experiment with a sample Git repository on the `Try Git <https://try.github.io/>`_ website.
* Invite others to work on your code with you in the same |env|, in real time and with text chat. For more information, see :ref:`Sharing an Environment <share-environment>`.

.. _sample-github-clean-up:

Step 7: Clean Up
================

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the |env|. For instructions, see :doc:`Deleting an Environment <delete-environment>`.

To delete the GitHub repository, see `Deleting a Repository <https://help.github.com/articles/deleting-a-repository/>`_ on the GitHub Help website.
