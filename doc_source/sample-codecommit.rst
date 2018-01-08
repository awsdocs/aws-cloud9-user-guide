.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _sample-codecommit:

##############################
|ACClong| Sample for |AC9long|
##############################

.. meta::
    :description:
        Provides a hands-on sample that you can use to experiment with an AWS CodeCommit repository in AWS Cloud9.

This sample enables you to set up an |envfirst| to interact with a remote code repository in |ACC|. |ACC| is
a source code control service that enables you to privately store and manage Git repositories in the AWS Cloud.
For more information about |ACC|, see the |ACC-ug|_.

* :ref:`sample-codecommit-permissions`
* :ref:`sample-codecommit-create-repo`
* :ref:`sample-codecommit-connect-repo`
* :ref:`sample-codecommit-clone-repo`
* :ref:`sample-codecommit-add-files`
* :ref:`sample-codecommit-clean-up`

.. note::

   .. include:: _sample-prereqs-cc.txt

   Creating this sample might result in charges to your AWS account. These include possible charges for services such as |EC2| and |ACC|. For more information, see
   `Amazon EC2 Pricing <https://aws.amazon.com/ec2/pricing/>`_ and `AWS CodeCommit Pricing <https://aws.amazon.com/codecommit/pricing/>`_.

.. _sample-codecommit-permissions:

Step 1: Set Up Your |IAM| Group with Required Access permissions
================================================================

If your AWS credentials are associated with an |IAM| administrator user in your AWS account, and you want to use that user to work with |ACC|, skip ahead to :ref:`sample-codecommit-create-repo`.

#. Sign in to the AWS Management Console, if you are not already signed in.

   For this step, we recommend you sign in using credentials for an |IAM| administrator user in your AWS account. If you cannot
   do this, check with your AWS account administrator.

#. Open the |IAM| console. To do this, in the console's navigation bar, choose :guilabel:`Services`. Then choose :guilabel:`IAM`.
#. Choose :guilabel:`Groups`.
#. Choose the group's name.
#. On the :guilabel:`Permissions` tab, for :guilabel:`Managed Policies`, choose :guilabel:`Attach Policy`.
#. In the list of policy names, select one of the following boxes:

   * Select :guilabel:`AWSCodeCommitPowerUser` for access to all of the functionality of |ACC| and repository-related resources, 
     except it does not allow deletion of |ACC| repositories or create or delete repository-related resources in other AWS services, such as |CWElong|.
   * Select :guilabel:`AWSCodeCommitFullAccess` for full control over |ACC| repositories and related resources in the AWS account, including the ability to delete repositories.

   (If you don't see either of these policy names in the list, type the policy name 
   in the :guilabel:`Filter` box to display it.)
#. Choose :guilabel:`Attach Policy`.

To see the list of access permissions that these AWS managed policies give to a group, see 
:codecommit-user-guide:`AWS Managed (Predefined) Policies for AWS CodeCommit <auth-and-access-control-iam-identity-based-access-control.html#managed-policies>` in the |ACC-ug|.

.. _sample-codecommit-create-repo:

Step 2: Create a Repository in |ACC|
====================================

In this step, you create a remote code repository in |ACC| by using the |ACC| console.

If you already have an |ACC| repository, skip ahead to :ref:`sample-codecommit-connect-repo`.

.. topic:: To create the repository

   #. If you are signed in to the AWS Management Console as an |IAM| administrator user from the previous step, and you do not want to use the |IAM| administrator user to create 
      the repository, sign out of the AWS Management Console.
   #. Open the |ACC| console, at https://console.aws.amazon.com/codecommit.
   #. In the console's navigation bar, use the region selector to choose the AWS Region you want to create the repository in (for example, :guilabel:`US East (Ohio)`).
   #. If a welcome page is displayed, choose :guilabel:`Get started`. Otherwise, choose :guilabel:`Create repository`.
   #. On the :guilabel:`Create repository` page, for :guilabel:`Repository name`, type a name for your new repository, for example :kbd:`MyDemoCloud9Repo`.
      If you choose a different name, substitute it throughout this sample.
   #. (Optional) For :guilabel:`Description`, type something about the repository, for example :kbd:`This is a demonstration repository for the AWS Cloud9 sample.`
   #. Choose :guilabel:`Create repository`. A :guilabel:`Connect to your repository` pane is displayed.
      Choose :guilabel:`Close`, as you will connect to
      your repository in a different way later in this topic.

.. _sample-codecommit-connect-repo:

Step 3: Connect Your |envtitle| to the Remote Repository
========================================================

In this step, you use the |AC9IDE| to connect to the |ACC| repository you created or identified in the previous step. 

Complete one of the following sets of procedures, depending on the type of |envfirst| you have.

.. list-table::
   :widths: 2 1
   :header-rows: 1

   * - **Environment type**
     - **Follow these procedures**
   * - |envec2|
     - 
       #. From a terminal session in the |IDE|, run the following 2 commands:
       
          .. code-block:: sh
          
             git config --global credential.helper '!aws codecommit credential-helper $@'
             git config --global credential.UseHttpPath true
             
          For more information, see 
          :codecommit-user-guide:`Step 2: Configure the AWS CLI Credential Helper On Your AWS Cloud9 EC2 Development Environment <setting-up-ide-c9.html#setting-up-ide-c9-credentials>` 
          in *Integrate AWS Cloud9 with AWS CodeCommit* in the |ACC-ug|.

       #. Skip ahead to :ref:`sample-codecommit-clone-repo`, later in this topic.

   * - |envssh|
     - 
       #. If Git is not already installed in the |env|, use a terminal session in the |IDE| to install it. For more information, see 
          :codecommit-user-guide:`Step 2: Install Git <setting-up-ssh-unixes.html#setting-up-ssh-unixes-install-git>` in *Setup Steps for SSH Connections to AWS CodeCommit Repositories on Linux, macOS, or Unix* 
          in the |ACC-ug|.
       #. Complete :codecommit-user-guide:`Step 3: Configure Credentials on Linux, macOS, or Unix <setting-up-ssh-unixes.html#setting-up-ssh-unixes-install-git>` in *Setup Steps for SSH Connections to AWS CodeCommit Repositories on Linux, macOS, or Unix* 
          in the |ACC-ug|.

          When you are instructed to sign in to the AWS Management Console and open the |IAM| console, we recommend you sign in using credentials for 
          an |IAM| administrator user in your AWS account. If you cannot do this, check with your AWS account administrator.

       #. Skip ahead to :ref:`sample-codecommit-clone-repo`, later in this topic.

.. _sample-codecommit-clone-repo:

Step 4: Clone the Remote Repository into Your |envtitle|
========================================================

In this step, you use the |AC9IDE| to clone the remote repository in |ACC| into your |env|.

To clone the repository, run the :command:`git clone` command, supplying the repository's clone URL, shown here as :samp:`{CLONE_URL}`.

.. code-block:: sh

   git clone CLONE_URL

For an |envec2|, you supply an HTTPS clone URL that starts with :code:`https://`. For an |envssh|, you supply an SSH clone URL that starts with :code:`ssh://`.

To get the repository's full clone URL, see 
:codecommit-user-guide:`Use the AWS CodeCommit Console to View Repository Details <how-to-view-repository-details.html#how-to-view-repository-details-console>` in the |ACC-ug|. 

If your repository doesn't have any files in it, a warning message is displayed, such as :code:`You appear to have cloned an empty repository.`
This is expected behavior, which you will address later.

.. _sample-codecommit-add-files:

Step 5: Add Files to the Repository
===================================

In this step, you create three simple files in the cloned repository in your |env|. Then you add the files
to the Git staging area in your
cloned repository, commit the staged files, and push the commit to your remote repository in |ACC|.

If the cloned repository already has files in it, you're done and can skip the rest of this sample.

.. topic:: To add files to the repository

   #. Create a new file. On the menu bar, choose :menuselection:`File, New File`.
   #. Type the following content into the file, and then choose :menuselection:`File, Save` to save the
      file as :file:`bird.txt` in the :file:`MyDemoCloud9Repo` directory in your |env|.

      .. code-block:: text

         bird.txt
         --------
         Birds are a group of endothermic vertebrates, characterized by feathers,
         toothless beaked jaws, the laying of hard-shelled eggs, a high metabolic
         rate, a four-chambered heart, and a lightweight but strong skeleton.

      .. note:: To confirm you are saving this file in the correct directory, in the
         :guilabel:`Save As` dialog box, choose the :file:`MyDemoCloud9Repo` folder, and
         be sure :guilabel:`Folder` displays :file:`/MyDemoCloud9Repo`.

   #. Create two more files, named :file:`insect.txt` and :file:`reptile.txt`, with the following content,
      and saving them in the same :file:`MyDemoCloud9Repo` directory.

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

   #. In the terminal, run the :command:`cd` command to switch to the :code:`MyDemoCloud9Repo` directory.

      .. code-block:: sh

         cd MyDemoCloud9Repo

   #. Confirm the files were successfully saved in the :code:`MyDemoCloud9Repo` directory by running the :command:`git status` command. All three files will be listed as untracked files.

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
           (use "git rm --cached <file>..." to unstage)

                 new file:   bird.txt
                 new file:   insect.txt
                 new file:   reptile.txt

   #. Commit the staged files by running the :command:`git commit` command.

      .. code-block:: sh

         git commit -m "Added information about birds, insects, and reptiles."

   #. Push the commit to your remote repository in |ACC| by running the :command:`git push` command.

      .. code-block:: sh

         git push -u origin master

   #. Confirm whether the files were successfully pushed. Open the |ACC| console, if it isn't already
      open, at https://console.aws.amazon.com/codecommit.
   #. In the top navigation bar, near the right edge, choose the AWS Region where you created the repository (for example, :guilabel:`US East (Ohio)`).
   #. On the :guilabel:`Dashboard` page, choose :guilabel:`MyDemoCloud9Repo`. The three files are displayed.

To continue experimenting with your |ACC| repository, see :codecommit-user-guide:`Browse the Contents of Your Repository <getting-started-cc.html#getting-started-cc-browse>` in the |ACC-ug|.

If you're new to Git and you don't want to mess up your |ACC| repository, experiment with a sample Git repository on the `Try Git <https://try.github.io/>`_ website.

.. _sample-codecommit-clean-up:

Step 6: Clean Up
================

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the |ACC| repository. For instructions, see
:ACC-ug:`Delete an AWS CodeCommit Repository <how-to-delete-repository>` in the |ACC-ug|.

You should also delete the |env|. For instructions, see :doc:`Deleting an Environment <delete-environment>`.