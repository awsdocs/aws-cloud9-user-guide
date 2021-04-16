# Java sample for AWS Cloud9<a name="sample-java"></a>

This sample enables you to run some Java code in an AWS Cloud9 development environment\.

Creating this sample might result in charges to your AWS account\. These include possible charges for services such as Amazon EC2 and Amazon S3\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/) and [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/)\.

**Topics**
+ [Prerequisites](#sample-java-prerequisites)
+ [Step 1: Install required tools](#sample-java-install)
+ [Step 2: Add code](#sample-java-code)
+ [Step 3: Build and run the code](#sample-java-run)
+ [Step 4: Set up to use the AWS SDK for Java](#sample-java-sdk)
+ [Step 5: Set up AWS credentials management in your environment](#sample-java-sdk-creds)
+ [Step 6: Add AWS SDK code](#sample-java-sdk-code)
+ [Step 7: Build and run the AWS SDK code](#sample-java-sdk-run)
+ [Step 8: Clean up](#sample-java-clean-up)

## Prerequisites<a name="sample-java-prerequisites"></a>

Before you use this sample, be sure to meet the following requirements\.
+  **You must have an existing AWS Cloud9 EC2 development environment\.** This sample assumes you already have an EC2 environment that is connected to an Amazon EC2 instance running Amazon Linux or Ubuntu Server\. If you have a different type of environment or operating system, you might need to adapt this sample's instructions to set up related tools\. See [Creating an environment in AWS Cloud9](create-environment.md) for details\.
+  **You have the AWS Cloud9 IDE for the existing environment already open\.** When you open an environment, AWS Cloud9 opens the IDE for that environment in your web browser\. See [Opening an environment in AWS Cloud9](open-environment.md) for details\.

## Step 1: Install required tools<a name="sample-java-install"></a>

In this step, you install a set of Java development tools in your AWS Cloud9 development environment\. If you already have a set of Java development tools such as the Oracle JDK or OpenJDK installed in your environment, you can skip ahead to [Step 2: Add code](#sample-java-code)\. This sample was developed with OpenJDK 8, which you can install in your environment by completing the following procedure\.

1. Confirm whether OpenJDK 8 is already installed\. To do this, in a terminal session in the AWS Cloud9 IDE, run the command line version of the Java runner with the ** `-version` ** option\. \(To start a new terminal session, on the menu bar, choose **Window**, **New Terminal**\.\)

   ```
   java -version
   ```

   Based on the output of the preceding command, do one of the following:
   + If the output states that the `java` command isn't found, continue with step 2 in this procedure to install OpenJDK 8\.
   + If the output contains values starting with `Java(TM)`, `Java Runtime Environment`, `Java SE`, `J2SE`, or `Java2`, the OpenJDK isn't installed or isn't set as the default Java development toolset\. Continue with step 2 in this procedure to install OpenJDK 8, and then switch to using OpenJDK 8\.
   + If the output contains values starting with `java version 1.8` and `OpenJDK`, skip ahead to [Step 2: Add code](#sample-java-code)\. OpenJDK 8 is installed correctly for this sample\.
   + If the output contains a `java version` less than `1.8` and values starting with `OpenJDK`, continue with step 2 in this procedure to upgrade the installed OpenJDK version to OpenJDK 8\.

1. Ensure the latest security updates and bug fixes are installed\. To do this, run the yum tool \(for Amazon Linux\) or the apt tool \(for Ubuntu Server\) with the ** `update` ** command\.

   For Amazon Linux:

   ```
   sudo yum -y update
   ```

   For Ubuntu Server:

   ```
   sudo apt update
   ```

1. Install OpenJDK 8\. To do this, run the yum tool \(for Amazon Linux\) or the apt tool \(for Ubuntu Server\) with the ** `install` ** command, specifying the OpenJDK 8 package\.

   For Amazon Linux:

   ```
   sudo yum -y install java-1.8.0-openjdk-devel
   ```

   For Ubuntu Server:

   ```
   sudo apt install -y openjdk-8-jdk
   ```

   For more information, see [How to download and install prebuilt OpenJDK packages](http://openjdk.java.net/install/) on the OpenJDK website\.

1. Switch or upgrade the default Java development toolset to OpenJDK 8\. To do this, run the ** `update-alternatives` ** command with the ** `--config` ** option\. Run this command twice to switch or upgrade the command line versions of the Java runner and compiler\.

   ```
   sudo update-alternatives --config java
   sudo update-alternatives --config javac
   ```

   At each prompt, type the selection number for OpenJDK 8 \(the one that contains `java-1.8`\)\.

1. Confirm that the command line versions of the Java runner and compiler are using OpenJDK 8\. To do this, run the command line versions of the Java runner and compiler with the `-version` option\.

   ```
   java -version
   javac -version
   ```

   If OpenJDK 8 is installed and set correctly, the Java runner version output contains a value starting with `openjdk version 1.8`, and the Java compiler version output starts with the value `javac 1.8`\.

## Step 2: Add code<a name="sample-java-code"></a>

In the AWS Cloud9 IDE, create a file with the following code, and save the file with the name `hello.java`\. \(To create a file, on the menu bar, choose **File**, **New File**\. To save the file, choose **File**, **Save**\.\)

```
public class hello {

  public static void main(String []args) {
    System.out.println("Hello, World!");

    System.out.println("The sum of 2 and 3 is 5.");

    int sum = Integer.parseInt(args[0]) + Integer.parseInt(args[1]);

    System.out.format("The sum of %s and %s is %s.\n",
      args[0], args[1], Integer.toString(sum));
  }
}
```

## Step 3: Build and run the code<a name="sample-java-run"></a>

1. Use the command line version of the Java compiler to compile the `hello.java` file into a `hello.class` file\. To do this, using the terminal in the AWS Cloud9 IDE, from the same directory as the `hello.java` file, run the Java compiler, specifying the `hello.java` file\.

   ```
   javac hello.java
   ```

1. Use the command line version of the Java runner to run the `hello.class` file\. To do this, from the same directory as the `hello.class` file, run the Java runner, specifying the name of the `hello` class that was declared in the `hello.java` file, with two integers to add \(for example, `5` and `9`\)\.

   ```
   java hello 5 9
   ```

1. Compare your output\.

   ```
   Hello, World!
   The sum of 2 and 3 is 5.
   The sum of 5 and 9 is 14.
   ```

## Step 4: Set up to use the AWS SDK for Java<a name="sample-java-sdk"></a>

You can enhance this sample to use the AWS SDK for Java to create an Amazon S3 bucket, list your available buckets, and then delete the bucket you just created\.

In this step, you install [Apache Maven](https://maven.apache.org/) or [Gradle](https://gradle.org/) in your environment\. Maven and Gradle are common build automation systems that can be used with Java projects\. After you install Maven or Gradle, you use it to generate a new Java project\. In this new project, you add a reference to the AWS SDK for Java\. This AWS SDK for Java provides a convenient way to interact with AWS services such as Amazon S3, from your Java code\.

**Topics**
+ [Set up with Maven](#sample-java-sdk-maven)
+ [Set up with Gradle](#sample-java-sdk-gradle)

### Set up with Maven<a name="sample-java-sdk-maven"></a>

1. Install Maven in your environment\. To see whether Maven is already installed, using the terminal in the AWS Cloud9 IDE, run Maven with the ** `-version` ** option\.

   ```
   mvn -version
   ```

   If successful, the output contains the Maven version number\. If Maven is already installed, skip ahead to step 4 in this procedure to use Maven to generate a new Java project in your environment\.

1. Install Maven by using the terminal to run the following commands\. 

   For Amazon Linux, the following commands get information about the package repository where Maven is stored, and then use this information to install Maven\.

   ```
   sudo wget http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo
   sudo sed -i s/\$releasever/6/g /etc/yum.repos.d/epel-apache-maven.repo
   sudo yum install -y apache-maven
   ```

   For more information about the preceding commands, see [Extra Packages for Enterprise Linux \(EPEL\)](https://fedoraproject.org/wiki/EPEL) on the Fedora Project Wiki website\.

   For Ubuntu Server, run the following command instead\.

   ```
   sudo apt install -y maven
   ```

1. Confirm the installation by running Maven with the ** `-version` ** option\.

   ```
   mvn -version
   ```

1. Use Maven to generate a new Java project\. To do this, use the terminal to run the following command from the directory where you want Maven to generate the project \(for example, the root directory of your environment\)\.

   ```
   mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
   ```

   The preceding command creates the following directory structure for the project in your environment\.

   ```
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
   ```

   For more information about the preceding directory structure, see [Maven Quickstart Archetype](https://maven.apache.org/archetypes/maven-archetype-quickstart/) and [Introduction to the Standard Directory Layout](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html) on the Apache Maven Project website\.

1. Modify the Project Object Model \(POM\) file for the project\. \(A POM file defines a Maven project's settings\.\) To do this, from the **Environment** window, open the `my-app/pom.xml` file\. In the editor, replace the file's current contents with the following code, and then save the `pom.xml` file\.

   ```
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
   ```

   The preceding POM file includes project settings that specify declarations such as the following:
   + The `artifactid` setting of `my-app` sets the project's root directory name, and the `group-id` setting of `com.mycompany.app` sets the `com/mycompany/app` subdirectory structure and the `package` declaration in the `App.Java` and `AppTest.java` files\.
   + The `artifactId` setting of `my-app`, with the `packaging` setting of `jar`, the `version` setting of `1.0-SNAPSHOT`, and the `descriptorRef` setting of `jar-with-dependencies` set the output JAR file's name of `my-app-1.0-SNAPSHOT-jar-with-dependencies.jar`\.
   + The `plugin` section declares that a single JAR, which includes all dependencies, will be built\.
   + The `dependency` section with the `groupId` setting of `com.amazon.aws` and the `artifactId` setting of `aws-java-sdk` includes the AWS SDK for Java library files\. The AWS SDK for Java version to use is declared by the `version` setting\. To use a different version, replace this version number\.

Skip ahead to [Step 5: Set up AWS credentials management in your environment](#sample-java-sdk-creds)\.

### Set up with Gradle<a name="sample-java-sdk-gradle"></a>

1. Install Gradle in your environment\. To see whether Gradle is already installed, using the terminal in the AWS Cloud9 IDE, run Gradle with the ** `-version` ** option\.

   ```
   gradle -version
   ```

   If successful, the output contains the Gradle version number\. If Gradle is already installed, skip ahead to step 4 in this procedure to use Gradle to generate a new Java project in your environment\.

1. Install Gradle by using the terminal to run the following commands\. These commands install and run the SDKMAN\! tool, and then use SDKMAN\! to install the latest version of Gradle\.

   ```
   curl -s "https://get.sdkman.io" | bash
   source "$HOME/.sdkman/bin/sdkman-init.sh"
   sdk install gradle
   ```

   For more information about the preceding commands, see [Installation](https://sdkman.io/install) on the SDKMAN\! website and [Install with a package manager](https://gradle.org/install/#with-a-package-manager) on the Gradle website\.

1. Confirm the installation by running Gradle with the ** `-version` ** option\.

   ```
   gradle -version
   ```

1. Use Gradle to generate a new Java project in your environment\. To do this, use the terminal to run the following commands to create a directory for the project, and then switch to that directory\.

   ```
   mkdir my-app
   cd my-app
   ```

1. Run the following command to have Gradle generate a new Java application project in the `my-app` directory in your environment\.

   ```
   gradle init --type java-application
   ```

   The preceding command creates the following directory structure for the project in your environment\.

   ```
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
   ```

1. Modify the `AppTest.java` for the project\. \(If you do not do this, the project might not build or run as expected\)\. To do this, from the **Environment** window, open the `my-app/src/test/java/AppTest.java` file\. In the editor, replace the file's current contents with the following code, and then save the `AppTest.java` file\.

   ```
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
   ```

1. Modify the `build.gradle` file for the project\. \(A `build.gradle` file defines a Gradle project's settings\.\) To do this, from the **Environment** window, open the `my-app/build.gradle` file\. In the editor, replace the file's current contents with the following code, and then save the `build.gradle` file\.

   ```
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
   ```

   The preceding `build.gradle` file includes project settings that specify declarations such as the following:
   + The `io.spring.dependency-management` plugin is used to import the AWS SDK for Java Maven Bill of Materials \(BOM\) to manage AWS SDK for Java dependencies for the project\. `classpath` declares the version to use\. To use a different version, replace this version number\.
   +  `com.amazonaws:aws-java-sdk-s3` includes the Amazon S3 portion of the AWS SDK for Java library files\. `mavenBom` declares the version to use\. If you want to use a different version, replace this version number\.

## Step 5: Set up AWS credentials management in your environment<a name="sample-java-sdk-creds"></a>

Each time you use the AWS SDK for Java to call an AWS service, you must provide a set of AWS credentials with the call\. These credentials determine whether the AWS SDK for Java has the appropriate permissions to make that call\. If the credentials don't cover the appropriate permissions, the call will fail\.

In this step, you store your credentials within the environment\. To do this, follow the instructions in [Calling AWS services from an environment in AWS Cloud9](credentials.md), and then return to this topic\.

For additional information, see [Set up AWS Credentials and Region for Development](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html) in the *AWS SDK for Java Developer Guide*\.

## Step 6: Add AWS SDK code<a name="sample-java-sdk-code"></a>

In this step, you add code to interact with Amazon S3 to create a bucket, list your available buckets, and then delete the bucket you just created\.

From the **Environment** window, open the `my-app/src/main/java/com/mycompany/app/App.java` file for Maven or the `my-app/src/main/java/App.java` file for Gradle\. In the editor, replace the file's current contents with the following code, and then save the `App.java` file\.

```
package com.mycompany.app;

import com.amazonaws.auth.profile.ProfileCredentialsProvider;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.AmazonS3Exception;
import com.amazonaws.services.s3.model.Bucket;
import com.amazonaws.services.s3.model.CreateBucketRequest;

import java.util.List;

public class App {

    private static AmazonS3 s3;

    public static void main(String[] args) {
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
```

## Step 7: Build and run the AWS SDK code<a name="sample-java-sdk-run"></a>

To run the code from the previous step, run the following commands from the terminal\. These commands use Maven or Gradle to create an executable JAR file for the project, and then use the Java runner to run the JAR\. The JAR runs with the name of the bucket to create in Amazon S3 \(for example, `my-test-bucket`\) and the ID of the AWS Region to create the bucket in as input \(for example, `us-east-2`\)\.

For Maven, run the following commands\.

```
cd my-app
mvn package
java -cp target/my-app-1.0-SNAPSHOT-jar-with-dependencies.jar com.mycompany.app.App my-test-bucket us-east-2
```

For Gradle, run the following commands\.

```
gradle build
gradle run -PappArgs="['my-test-bucket', 'us-east-2']"
```

Compare your results to the following output\.

```
My buckets now are:

Creating a new bucket named 'my-test-bucket'...

My buckets now are:

my-test-bucket

Deleting the bucket named 'my-test-bucket'...

My buckets now are:
```

## Step 8: Clean up<a name="sample-java-clean-up"></a>

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the environment\. For instructions, see [Deleting an environment in AWS Cloud9](delete-environment.md)\.