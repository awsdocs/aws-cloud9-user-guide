.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _sample-java:

#########################
Java Sample for |AC9long|
#########################

.. meta::
    :description:
        Provides a hands-on sample that you can use to experiment with Java in AWS Cloud9.

This sample enables you to run some Java code in an |envfirst|.

Creating this sample might result in charges to your AWS account. These include possible charges for services such as |EC2| and |S3|. For more information, see
`Amazon EC2 Pricing <https://aws.amazon.com/ec2/pricing/>`_ and `Amazon S3 Pricing <https://aws.amazon.com/s3/pricing/>`_.

* :ref:`sample-java-prerequisites`
* :ref:`sample-java-install`
* :ref:`sample-java-code`
* :ref:`sample-java-run`
* :ref:`sample-java-sdk`
* :ref:`sample-java-sdk-creds`
* :ref:`sample-java-sdk-code`
* :ref:`sample-java-sdk-run`
* :ref:`sample-java-clean-up`

.. _sample-java-prerequisites:

Prerequisites
=============

.. include:: _sample-prereqs.txt

.. _sample-java-install:

Step 1: Install Required Tools
==============================

In this step, you install a set of Java development tools in your |envfirstlong|. If you already have a set of Java development tools such as the Oracle JDK or OpenJDK installed in your
|env|, you can skip ahead to :ref:`sample-java-code`. This sample was developed with OpenJDK 8, which you can install in your |env| by completing the following procedure.

#. Confirm whether OpenJDK 8 is already installed. To do this, in a terminal session in the |AC9IDE|, run the command line version of the Java runner with the :command:`-version` option.
   (To start a new terminal session,
   on the menu bar, choose :menuselection:`Window, New Terminal`.)

   .. code-block:: sh

      java -version

   Based on the output of the preceding command, do one of the following:

   * If the output states that the :code:`java` command isn't found, continue with step 2 in this procedure to install OpenJDK 8.
   * If the output contains values starting with :code:`Java(TM)`, :code:`Java Runtime Environment`, :code:`Java SE`, :code:`J2SE`, or :code:`Java2`, the OpenJDK isn't installed
     or isn't set as the default Java development toolset. Continue with step 2
     in this procedure to install OpenJDK 8, and then switch to using OpenJDK 8.
   * If the output contains values starting with :code:`java version 1.8` and :code:`OpenJDK`,
     skip ahead to :ref:`sample-java-code`. OpenJDK 8 is installed correctly for this sample.
   * If the output contains a :code:`java version` less than :code:`1.8` and values starting with :code:`OpenJDK`,
     continue with step 2 in this procedure to upgrade the installed OpenJDK version to OpenJDK 8.

#. Ensure the latest security updates and bug fixes are installed. To do this, run the yum tool with the :command:`update` command.

   .. code-block:: sh

      sudo yum -y update

#. Install OpenJDK 8. To do this, run the yum tool with the :command:`install` command, specifying the OpenJDK 8 package.

   .. code-block:: sh

      sudo yum -y install java-1.8.0-openjdk-devel

   For more information, see `How to download and install prebuilt OpenJDK packages <http://openjdk.java.net/install/>`_ on the OpenJDK website.

#. Switch or upgrade the default Java development toolset to OpenJDK 8. To do this, run the :command:`update-alternatives` command with the :command:`--config` option. Run this command twice to switch or upgrade
   the command line versions of the Java runner and compiler.

   .. code-block:: sh

      sudo update-alternatives --config java
      sudo update-alternatives --config javac

   At each prompt, type the selection number for OpenJDK 8 (the one that contains :code:`java-1.8`).

#. Confirm that the command line versions of the Java runner and compiler are using OpenJDK 8. To do this, run the command line versions of the Java runner and compiler with
   the :code:`-version` option.

   .. code-block:: sh

      java -version
      javac -version

   If OpenJDK 8 is installed and set correctly, the Java runner version output contains a value starting with :code:`openjdk version 1.8`, and
   the Java compiler version output starts with the value :code:`javac 1.8`.

.. _sample-java-code:

Step 2: Add Code
================

In the |AC9IDE|, create a file with the following code, and save the file with the name :file:`hello.java`.
(To create a file, on the menu bar, choose :menuselection:`File, New File`. To save the file, choose :menuselection:`File, Save`.)

.. code-block:: java

   public class hello {

     public static void main(String []args) {
       System.out.println("Hello, World!");

       System.out.println("The sum of 2 and 3 is 5.");

       int sum = Integer.parseInt(args[0]) + Integer.parseInt(args[1]);

       System.out.format("The sum of %s and %s is %s.\n",
         args[0], args[1], Integer.toString(sum));
     }
   }

.. _sample-java-run:

Step 3: Build and Run the Code
==============================

#. Use the command line version of the Java compiler to compile the :file:`hello.java` file into a :file:`hello.class` file. To do this, using the terminal in the |AC9IDE|,
   from the same directory as the :file:`hello.java` file, run the Java compiler, specifying the :file:`hello.java` file.

   .. code-block:: sh

      javac hello.java

#. Use the command line version of the Java runner to run the :file:`hello.class` file. To do this, from the same directory as the :file:`hello.class` file,
   run the Java runner, specifying the name of the :file:`hello` class that was declared in the :file:`hello.java` file, with two integers to add (for example, :code:`5` and :code:`9`).

   .. code-block:: sh

      java hello 5 9

#. Compare your output.

   .. code-block:: text

      Hello, World!
      The sum of 2 and 3 is 5.
      The sum of 5 and 9 is 14.

.. _sample-java-sdk:

Step 4: Set Up to Use the |sdk-java|
====================================

You can enhance this sample to use the |sdk-java| to create an |s3| bucket, list your available buckets, and then delete the bucket you just created.

In this step, you install `Apache Maven <https://maven.apache.org/>`_ or `Gradle <https://gradle.org/>`_ in your |env|. Maven and Gradle are common build automation systems that can
be used with Java projects. After you install Maven or Gradle, you use it to generate a new Java project.
In this new project, you add a reference to the |sdk-java|. This |sdk-java| provides a convenient way to interact with AWS services such as |s3|,
from your Java code.

* :ref:`sample-java-sdk-maven`
* :ref:`sample-java-sdk-gradle`

.. _sample-java-sdk-maven:

Set Up With Maven
-----------------

#. Install Maven in your |env|. To see whether Maven is already installed, using the terminal in the |AC9IDE|, run Maven with the
   :command:`-version` option.

   .. code-block:: sh

      mvn -version

   If successful, the output contains the Maven version number. If Maven is already installed, skip ahead to step 4 in this procedure 
   to use Maven to generate a new Java project in your |env|.

#. Install Maven by using the terminal to run the following commands. These commands get information about the package repository where
   Maven is stored, and then use this information to install Maven.

   .. code-block:: sh

      sudo wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo
      sudo sed -i s/\$releasever/6/g /etc/yum.repos.d/epel-apache-maven.repo
      sudo yum install -y apache-maven

   For more information about the preceding commands, see `Extra Packages for Enterprise Linux (EPEL) <https://fedoraproject.org/wiki/EPEL>`_ on the Fedora Project Wiki website.

#. Confirm the installation by running Maven with the :command:`-version` option.

   .. code-block:: sh

      mvn -version

#. Use Maven to generate a new Java project. To do this, use the terminal to run the following command from the directory
   where you want Maven to generate the project (for example, the root directory of your |env|).

   .. code-block:: sh

      mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

   The preceding command creates the following directory structure for the project in your |env|.

   .. code-block:: text

      my-app
        |- src
        |   `- main
        |        `- java
        |             `- com
        |                 `- mycompany
        |                      `- app
        |                          `-App.java
        |- test
        |   `- java
        |        `- com
        |            `- mycompany
        |                 `- app
        |                     `- AppTest.java
        `- pom.xml

   For more information about the preceding directory structure, see `Maven Quickstart Archetype <https://maven.apache.org/archetypes/maven-archetype-quickstart/>`_ and
   `Introduction to the Standard Directory Layout <https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html>`_
   on the Apache Maven Project website.

#. Modify the Project Object Model (POM) file for the project. (A POM file defines a Maven project's settings.) To do this, from the :guilabel:`Environment` window, 
   open the :file:`my-app/pom.xml` file. In the editor, replace the file's current contents with the following code, and then save the :file:`pom.xml` file.

   .. code-block:: xml

      <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
        <modelVersion>4.0.0</modelVersion>
        <groupId>com.mycompany.app</groupId>
        <artifactId>my-app</artifactId>
        <packaging>jar</packaging>
        <version>1.0-SNAPSHOT</version>
        <build>
          <plugins>
            <plugin>
              <groupId>org.apache.maven.plugins</groupId>
              <artifactId>maven-assembly-plugin</artifactId>
              <version>3.0.0</version>
              <configuration>
                <descriptorRefs>
                  <descriptorRef>jar-with-dependencies</descriptorRef>
                </descriptorRefs>
                <archive>
                  <manifest>
                    <mainClass>com.mycompany.app.App</mainClass>
                  </manifest>
                </archive>
              </configuration>
              <executions>
                <execution>
                  <phase>package</phase>
                    <goals>
                      <goal>single</goal>
                    </goals>
                </execution>
              </executions>
            </plugin>
          </plugins>
        </build>
        <dependencies>
          <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>3.8.1</version>
            <scope>test</scope>
          </dependency>
          <dependency>
            <groupId>com.amazonaws</groupId>
            <artifactId>aws-java-sdk</artifactId>
            <version>1.11.330</version>
          </dependency>
        </dependencies>
      </project>

   The preceding POM file includes project settings that specify declarations such as the following:

   * The :code:`artifactid` setting of :code:`my-app` sets the project's root directory name, and the :code:`group-id` setting of :code:`com.mycompany.app` sets the :file:`com/mycompany/app`
     subdirectory structure and the :code:`package` declaration in the :file:`App.Java` and :file:`AppTest.java` files.
   * The :code:`artifactId` setting of :code:`my-app`, with the :code:`packaging` setting of :code:`jar`, the :code:`version` setting of :code:`1.0-SNAPSHOT`, and the :code:`descriptorRef` setting of :code:`jar-with-dependencies`
     set the output JAR file's name of :file:`my-app-1.0-SNAPSHOT-jar-with-dependencies.jar`.
   * The :code:`plugin` section declares that a single JAR, which includes all dependencies, will be built.
   * The :code:`dependency` section with the :code:`groupId` setting of :code:`com.amazon.aws` and the :code:`artifactId` setting of :code:`aws-java-sdk` includes the |sdk-java| library files. The
     |sdk-java| version to use is declared by the :code:`version` setting. To use a different version, replace this version number.

Skip ahead to :ref:`sample-java-sdk-creds`.

.. _sample-java-sdk-gradle:

Set Up With Gradle
------------------

#. Install Gradle in your |env|. To see whether Gradle is already installed, using the terminal in the |AC9IDE|, run Gradle with the
   :command:`-version` option.

   .. code-block:: sh

      gradle -version

   If successful, the output contains the Gradle version number. If Gradle is already installed, skip ahead to step 4 in this procedure to 
   use Gradle to generate a new Java project in your |env|.

#. Install Gradle by using the terminal to run the following commands. These commands install and run the SDKMAN! tool, and then use SDKMAN! to install the latest version of Gradle.

   .. code-block:: sh

      curl -s "https://get.sdkman.io" | bash
      source "$HOME/.sdkman/bin/sdkman-init.sh"
      sdk install gradle

   For more information about the preceding commands, see `Installation <https://sdkman.io/install>`_ on the SDKMAN! website and
   `Install with a package manager <https://gradle.org/install/#with-a-package-manager>`_ on the Gradle website.

#. Confirm the installation by running Gradle with the :command:`-version` option.

   .. code-block:: sh

      gradle -version

#. Use Gradle to generate a new Java project in your |env|. To do this, use the terminal to run the following commands to create a directory for the project, 
   and then switch to that directory.

   .. code-block:: sh

      mkdir my-app
      cd my-app

#. Run the following command to have Gradle generate a new Java application project in the :file:`my-app` directory in your |env|.

   .. code-block:: sh

      gradle init --type java-application

   The preceding command creates the following directory structure for the project in your |env|.

   .. code-block:: text

      my-app
        |- .gradle
        |   `- (various supporting project folders and files)
        |- gradle
        |   `- (various supporting project folders and files)
        |- src
        |   |- main
        |   |    `- java
        |   |         `- App.java
        |   `- test
        |        `- java
        |             `- AppTest.java
        |- build.gradle
        |- gradlew
        |- gradlew.bat
        `- settings.gradle

#. Modify the :file:`AppTest.java` for the project. (If you do not do this, the project might not build or run as expected). 
   To do this, from the :guilabel:`Environment` window, open the :file:`my-app/src/test/java/AppTest.java` file. In the editor, replace the file's current contents 
   with the following code, and then save the :file:`AppTest.java` file.

   .. code-block:: java

      import org.junit.Test;
      import static org.junit.Assert.*;

      public class AppTest {
        @Test public void testAppExists () {
          try {
            Class.forName("com.mycompany.app.App");
          } catch (ClassNotFoundException e) {
            fail("Should have a class named App.");
          }
        }
      }

#. Modify the :file:`build.gradle` file for the project. (A :file:`build.gradle` file defines a Gradle project's settings.) To do this, 
   from the :guilabel:`Environment` window, open the :file:`my-app/build.gradle` file. In the editor, replace the file's current contents 
   with the following code, and then save the :file:`build.gradle` file.

   .. code-block:: text

      apply plugin: 'java'
      apply plugin: 'application'

      repositories {
        jcenter()
        mavenCentral()
      }

      buildscript {
        repositories {
          mavenCentral()
        }
        dependencies {
          classpath "io.spring.gradle:dependency-management-plugin:1.0.3.RELEASE"
        }
      }

      apply plugin: "io.spring.dependency-management"

      dependencyManagement {
        imports {
          mavenBom 'com.amazonaws:aws-java-sdk-bom:1.11.330'
        }
      }

      dependencies {
        compile 'com.amazonaws:aws-java-sdk-s3'
        testCompile group: 'junit', name: 'junit', version: '4.12'
      }

      run {
        if (project.hasProperty("appArgs")) {
          args Eval.me(appArgs)
        }
      }

      mainClassName = 'App'

   The preceding :file:`build.gradle` file includes project settings that specify declarations such as the following:

   * The :code:`io.spring.dependency-management` plugin is used to import the |sdk-java| Maven Bill of Materials (BOM) to manage |sdk-java| dependencies for the project.
     :code:`classpath` declares the version to use. To use a different version, replace this version number.
   * :code:`com.amazonaws:aws-java-sdk-s3` includes the |S3| portion of the |sdk-java| library files. :code:`mavenBom` declares the version to use.
     If you want to use a different version, replace this version number.

.. _sample-java-sdk-creds:

Step 5: Set Up AWS Credentials Management in Your |envtitle|
============================================================

Each time you use the |sdk-java| to call an AWS service, you must provide a set of AWS credentials with the call. These credentials determine whether the
|sdk-java| has the appropriate permissions to make that call. If the credentials don't cover the appropriate permissions, the call will fail.

In this step, you store your credentials within the |env|. To do this, follow the instructions in :ref:`Call AWS Services from an Environment <credentials>`, and then return to this topic.

For additional information, see :sdk-java-dg:`Set up AWS Credentials and Region for Development <setup-credentials>` in the
|sdk-java-dg|.

.. _sample-java-sdk-code:

Step 6: Add AWS SDK Code
========================

In this step, you add code to interact with |S3| to create a bucket, list your available buckets, and then delete the bucket you just created.

From the :guilabel:`Environment` window, open the :file:`my-app/src/main/java/com/mycompany/app/App.java` file for Maven or the
:file:`my-app/src/main/java/App.java` file for Gradle. In the editor, replace the file's
current contents with the following code, and then save the :file:`App.java` file.

.. code-block:: java

   package com.mycompany.app;
   import com.amazonaws.auth.profile.ProfileCredentialsProvider;
   import com.amazonaws.services.s3.AmazonS3;
   import com.amazonaws.services.s3.AmazonS3ClientBuilder;
   import com.amazonaws.services.s3.model.AmazonS3Exception;
   import com.amazonaws.services.s3.model.Bucket;
   import com.amazonaws.services.s3.model.CreateBucketRequest;
   import java.util.List;

   public class App
   {

     private static AmazonS3 s3;

     public static void main( String[] args )
     {
       if (args.length < 2) {
         System.out.format("Usage: <the bucket name> <the AWS Region to use>\n" +
           "Example: my-test-bucket us-east-2\n");
         return;
       }

       String bucket_name = args[0];
       String region = args[1];

       s3 = AmazonS3ClientBuilder.standard()
         .withCredentials(new ProfileCredentialsProvider())
         .withRegion(region)
         .build();

       // List current buckets.
       ListMyBuckets();

       // Create the bucket.
       if (s3.doesBucketExistV2(bucket_name)) {
         System.out.format("\nCannot create the bucket. \n" +
           "A bucket named '%s' already exists.", bucket_name);
         return;
        } else {
          try {
            System.out.format("\nCreating a new bucket named '%s'...\n\n", bucket_name);
            s3.createBucket(new CreateBucketRequest(bucket_name, region));
          } catch (AmazonS3Exception e) {
            System.err.println(e.getErrorMessage());
          }
        }

        // Confirm that the bucket was created.
        ListMyBuckets();

        // Delete the bucket.
        try {
          System.out.format("\nDeleting the bucket named '%s'...\n\n", bucket_name);
          s3.deleteBucket(bucket_name);
        } catch (AmazonS3Exception e) {
          System.err.println(e.getErrorMessage());
        }

        // Confirm that the bucket was deleted.
        ListMyBuckets();

     }

     private static void ListMyBuckets() {
       List<Bucket> buckets = s3.listBuckets();
       System.out.println("My buckets now are:");

       for (Bucket b : buckets) {
         System.out.println(b.getName());
       }
     }

   }

.. _sample-java-sdk-run:

Step 7: Build and Run the AWS SDK Code
======================================

To run the code from the previous step, run the following commands from the terminal. These commands use Maven or Gradle to create an executable JAR file for the project,
and then use the Java runner to run the JAR. The JAR runs with the name of the bucket to create in |S3| (for example, :code:`my-test-bucket`) and the ID of the AWS Region
to create the bucket in as input (for example, :code:`us-east-2`).

For Maven, run the following commands.

.. code-block:: sh

   cd my-app
   mvn package
   java -cp target/my-app-1.0-SNAPSHOT-jar-with-dependencies.jar com.mycompany.app.App my-test-bucket us-east-2

For Gradle, run the following commands.

.. code-block:: sh

   gradle build
   gradle run -PappArgs="['my-test-bucket', 'us-east-2']"

Compare your results to the following output.

.. code-block:: text

   My buckets now are:

   Creating a new bucket named 'my-test-bucket'...

   My buckets now are:

   my-test-bucket

   Deleting the bucket named 'my-test-bucket'...

   My buckets now are:

.. _sample-java-clean-up:

Step 8: Clean Up
================

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the |env|.
For instructions, see :doc:`Delete an Environment <delete-environment>`.
