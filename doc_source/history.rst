.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _history:

#################################
Document History for the |AC9-ug|
#################################

.. meta::
    :description:
        Lists the history of significant changes to the AWS Cloud9 User Guide. 
        
Here is a list of significant changes to the *AWS Cloud9 User Guide*.

**Latest documentation update:** December 7, 2018

.. list-table::
   :widths: 2 3 2
   :header-rows: 1

   * - **Change**
     - **Description**
     - **Date Changed**
   * - New content
     - |AC9| now supports shared VPCs in |VPC|. For more information, see :ref:`Amazon VPC Requirements for AWS Cloud9 <vpc-settings-requirements>`.
     - December 7, 2018
   * - AWS RoboMaker integration
     - |AC9| now supports AWS RoboMaker, a service that makes it easy to develop, test, and deploy intelligent robotics applications at scale. For more information, see 
       `Getting Started with AWS RoboMaker <https://docs.aws.amazon.com/robomaker/latest/dg/getting-started.html>`_ and 
       `Developing with AWS Cloud9 <https://docs.aws.amazon.com/robomaker/latest/dg/cloud9.html>`_ in the *AWS RoboMaker Developer Guide*.
     - November 26, 2018
   * - New topic
     - The |AC9IDE| now provides additional productivity features for some languages in the context of a language project.
       For more information, see :ref:`Working with Language Projects <projects>`.
     - October 2, 2018
   * - Changed content
     - The :guilabel:`Go` window was added to the |AC9IDE| for |envplural| created on or after October 2, 2018. This new window replaces the :guilabel:`Navigate` and :guilabel:`Commands` windows, 
       which were both removed from the |IDE| for |envplural| created on or after October 2, 2018. For more information, see :ref:`tutorial-go` in the *IDE Tutorial*.
     - October 2, 2018
   * - New topic
     - Added a new sample demonstrating how to use |AC9| with the AWS Cloud Development Kit (AWS CDK). For more information, see the 
       :ref:`AWS CDK Sample <sample-cdk>`.
     - August 30, 2018
   * - New content
     - For |envfirstec2plural| created on or after July 31 2018, |AC9| now automatically restricts incoming SSH traffic to just the IP address ranges that 
       |AC9| uses to connect over SSH. For more information, see :ref:`Inbound SSH IP Address Ranges <ip-ranges>`.
     - July 31, 2018
   * - New topic
     - Added new sample demonstrating how to use |AC9| with Docker. For more information, see the 
       :ref:`Docker Sample <sample-docker>`.
     - June 19, 2018
   * - New content
     - Added information about additional options for deploying |LAMlong| functions from the |AC9IDE|, depending on how the |LAM| function was originally created. 
       For more information, see :ref:`lambda-functions-upload-code`.
     - May 29, 2018
   * - New topics
     - Added new samples demonstrating how to use |AC9| with Java, .NET Core, and TypeScript. For more information, see the 
       :ref:`Java Sample <sample-java>`, :ref:`.NET Core Sample <sample-dotnetcore>`, and :ref:`TypeScript Sample <sample-typescript>`.
     - May 29, 2018
   * - New topic
     - Added information about supported browsers for |AC9|. For more information, see :ref:`Supported Browsers <browsers>`.
     - May 23, 2018
   * - New topics
     - Added new tutorials demonstrating how to create |LAM| functions with |AC9|. For more information, see the 
       :ref:`AWS Lambda Tutorial <tutorial-lambda>` and :ref:`Advanced AWS Lambda Tutorial <tutorial-lambda-advanced>`.
     - April 19, 2018
   * - New topic
     - Added information about how to restrict incoming traffic to just the IP address ranges that |AC9| uses to connect to hosts over SSH. 
       For more information, see :ref:`Inbound SSH IP Address Ranges <ip-ranges>`.
     - April 19, 2018
   * - New content
     - Added information about how to use the AWS Serverless Application Repository with |AC9|. For more information, see :ref:`lambda-functions-create-repo`.
     - April 19, 2018
   * - New content
     - Added new troubleshooters for previewing applications and sharing running applications. For more information, see 
       :ref:`troubleshooting-app-preview` and :ref:`troubleshooting-app-sharing`.
     - April 19, 2018
   * - New topic
     - Added information about how to use the :guilabel:`File Revision History` pane in the |IDE|. For more information, see :ref:`Working with File Revisions <file-revisions>`.
     - April 19, 2018
   * - New content
     - Added information about how to debug |LAM| functions that use Python. 
       For more information, see :ref:`Debug the Local Version of a Lambda Function or Its Related API Gateway API <lambda-functions-debug>`.
     - March 22, 2018
   * - New content
     - Added a new troubleshooter for opening |envfirstlongplural|. For more information, see :ref:`troubleshooting-env-loading`.
     - March 19, 2018
   * - New content
     - Added a new troubleshooter for the |AC9| Installer. For more information, see :ref:`troubleshooting-ssh-installer`.
     - March 19, 2018
   * - New topic
     - Added information about how to use |AC9| with |ACPlong|. 
       For more information, see :ref:`Working with AWS CodePipeline <codepipeline-repos>`.
     - February 13, 2018
   * - New content
     - Added information about how to share |envfirstplural| across AWS accounts. 
       For more information, see :ref:`Invite an IAM User in Another Account to Your Environment <share-environment-invite-user-cross-account>`.
     - February 5, 2018
   * - New content
     - Added information about how to use |AC9| with the aws-shell. 
       For more information, see the :ref:`AWS CLI and aws-shell Sample <sample-aws-cli>`.
     - January 19, 2018
   * - GitHub availability
     - This guide is now available on GitHub. You can also use GitHub to submit feedback and change requests for this guide's content. 
       For more information, choose the :guilabel:`Edit on GitHub` icon in the guide's navigation bar, 
       or see the `awsdocs/aws-cloud9-user-guide <https://github.com/awsdocs/aws-cloud9-user-guide>`_ repository on the GitHub website.
     - January 10, 2018
   * - Kindle format availability
     - This guide is now available in Amazon Kindle format. 
       For more information, choose the :guilabel:`Open Kindle` icon in the guide's navigation bar, 
       or see `AWS Cloud9: User Guide Kindle Edition <https://www.amazon.com/AWS-Cloud9-Amazon-Web-Services-ebook/dp/B078XBZMWS>`_ on the Amazon website.
     - January 2, 2018
   * - New topic
     - Added information about how to use |AC9| with |lightsaillong|. 
       For more information, see :ref:`Working with Amazon Lightsail Instances <lightsail-instances>`.
     - December 19, 2017
   * - New topic
     - Added descriptions of specific AWS settings for |envfirstplural|. 
       For more information, see :ref:`Working with AWS Project and User Settings <settings-aws>`.
     - December 7, 2017
   * - New topics
     - Added setup steps for using |AC9| with an AWS account root user. Added advanced setup steps for using |AC9| with teams.
       For more information, see :ref:`Getting Started <get-started>`.
     - December 5, 2017
   * - New topic
     - Expanded coverage of requirements for an |EC2| instance or your own server to connect to an |envfirstlongssh|. 
       For more information, see :ref:`SSH Environment Host Requirements <ssh-settings>`.
     - December 4, 2017
   * - Initial release
     - This is the initial release of the *AWS Cloud9 User Guide*.
     - November 30, 2017