.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _welcome:

##################
What Is |AC9long|?
##################

.. meta::
    :description:
        Introduction to AWS Cloud9.

|AC9| contains a collection of tools that you use to code, build, run, test, debug, and
release software in the cloud. To work with these tools, you use the 
|AC9| integrated development environment, or :dfn:`IDE`.

You access the |AC9IDE| through a web browser. The |IDE| offers a rich code-editing experience with
support for several programming languages and runtime debuggers, as well as a built-in
terminal. 
You can configure the |IDE| to your preferences. You can switch color themes, bind shortcut keys,
enable programming language-specific syntax coloring and code formatting, and more.

You use the |IDE| to interact with an |envfirst|. An :dfn:`environment` is a place where you store your project's files and where you run the tools to develop your apps. 
In the background, you can instruct |AC9| to have |EC2| launch an |EC2| instance and then connect the |env| to the newly-launched instance. 
We call this type of setup an :dfn:`EC2 environment`. 
You can also instruct |AC9| to connect an |env| to an existing |EC2| instance or your own server. We call this type of setup an :dfn:`SSH environment`. 

You can create and switch between multiple |envplural|, 
with each |env| set up for a specific development project. By storing the |env| 
in the cloud, your projects no longer need to be tied to a single computer or server setup. This
enables you to do things such as easily switch between computers and more quickly onboard developers to your team.

To watch related videos, see the 9-minute video `AWS re:Invent 2017 - Introducing AWS Cloud9: Werner Vogels Keynote <https://www.youtube.com/watch?v=fwFoU_Wb-fU>`_ and 
the 15-minute video `AWS re:Invent Launchpad 2017 - AWS Cloud9 <https://www.youtube.com/watch?v=NNqVBo9k8n4>`_, both on the YouTube website.

* :ref:`how-does-it-work`
* :ref:`pricing`
* :ref:`how-to-get-started`
* :ref:`versions`

.. _how-does-it-work:

How Does |AC9| Work?
====================

The following diagram shows a high-level overview of how |AC9| works.

.. image:: images/arch.png
   :alt: Diagram that provides an overview of how AWS Cloud9 works

You use the |AC9IDE|, running in a web browser on your local computer, to interact with your |env|. An |EC2| instance
or your own server connects to the |env|. An :dfn:`environment` is a place where you store your project's files and where you run the tools to develop your apps.

You use the |AC9IDE| to work with files in the |env|. You can:

* Store these files locally on the instance or server.
* Clone a remote code repository |mdash| such as a repo in |ACClong| |mdash| into your |env|.
* Work with a combination of local and cloned files in the |env|.

.. _pricing:

Pricing for |AC9|
=================

For information, see `AWS Cloud9 Pricing <https://aws.amazon.com/cloud9/pricing/>`_.

For education options, explore the `AWS Educate <https://aws.amazon.com/education/awseducate/>`_ program.

.. _how-to-get-started:

How Do I Get Started with |AC9|?
================================

Set up to start using |AC9| by following one of the sets of setup steps in :doc:`Getting Started <get-started>`.

After you get set up, follow the steps in the :doc:`Tutorial <tutorial>` to begin experimenting with |AC9|.

.. _versions:

About Cloud9 Versions
=====================

There are currently two versions of Cloud9 available: c9.io and |AC9long|. This :title:`AWS Cloud9 User Guide` only covers |AC9long|.

c9.io is available only to existing c9.io users. For more information, 
see `Cloud9 now runs on and integrates with AWS <https://c9.io/announcement>`_ on the c9.io website.

c9.io and |AC9long| are not interoperable. You can't use an account or workspace in c9.io with an account or |env| in |AC9long|.