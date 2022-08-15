# Enhanced support for Java development<a name="enhanced-java"></a>

AWS Cloud9 provides enhanced language support to improve your development experience when working with Java\. Key productivity features include code completion, linting for errors, code lenses, and debugging options such as breakpoints and stepping\.

**Important**  
Enhanced productivity features are available only for AWS Cloud9 development environments that are connected to Amazon EC2 instances\.   
Moreover, to ensure an optimal IDE experience when using enhanced language support for Java, the Amazon EC2 compute instance that backs your AWS Cloud9 environment requires **2 GiB** or more of memory\. If AWS Cloud9 detects that your EC2 compute instance doesn't have sufficient RAM, you're not offered the option to activate enhanced features for Java\. 

## Activating and customizing enhanced Java support<a name="activating-java-support"></a>

The option to activate enhanced support for Java is automatically displayed if the following conditions are met:
+ Your AWS Cloud9 environment is connected to an Amazon EC2 instance with 2 GiB or more of memory\.
+ You're working with a file associated with Java development\. AWS Cloud9 checks the following file names and extensions: `*.java`, `*.gradle` \(associated with the Gradle build tool\), and `pom.xml` \(associated with the Apache Maven build tool\)\.
+ You're working in an AWS Cloud9 environment that was created after **December 11, 2020**\. At present, it's not possible to use Java productivity features in development environments that were created before this date\.

If these conditions are met, a dialog box displays to ask you whether you want to activate the extra productivity features for coding and debugging Java\. If you choose **Activate**, you can start using the features in the IDE\.

![\[Code completion with\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/working_with_java_rework.png)

**Note**  
Amazon EC2 instances which are launched when you create an AWS Cloud9 environment have *Amazon Coretto 11* already installed\. Amazon Coretto is no\-cost, multiplatform, production\-ready distribution of the Open Java Development Kit \(OpenJDK\)\. This means you can start developing and running Java applications in AWS Cloud9 out\-of\-the\-box\.

You can also manually activate and deactivate enhanced language and debugging support using the AWS Cloud9 interface\. Choose **Preferences**, **Java Support**, **Enhanced Java Support**\.

![\[Manually activating and deactivating enhanced Java support\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/activate_java_extensions_update.png)

The enhanced support for Java development in AWS Cloud9 is provided by two extensions to the IDE: 
+ Language Support for Java\(TM\) by Red Hat
+ Debugger for Java

The AWS Cloud9 interface gives you access to wide range of settings that customize these extensions' performance\. To change extension settings, choose **Preferences**, **Java Support**\.

For detailed information on these settings, see the installed versions' ReadMe pages in the extensions' GitHub repositories:
+ [Language Support for Java\(TM\) by Red Hat](https://github.com/redhat-developer/vscode-java/tree/v1.8.0)
+ [Debugger for Java](https://github.com/microsoft/vscode-java-debug/tree/0.40.1)

## Feature highlights<a name="key-java-features"></a>

After you've activated enhanced Java support, you can use a range of productivity\-boosting features\.

** Code completion**

With code completion, the editor makes context\-aware suggestions based on the code you're typing\. For example, if you type the dot \("\."\) operator after an object name, the editor displays the methods or properties available for that object\. 

![\[Code completion with\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/code-complete-java.png)

**Code lenses**

Code lens allow you to access context\-specific actions directly in the source code\. For Java development, code lenses facilitate unit testing by allowing you to run and debug specific methods\. 

![\[Accessing code lenses\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/context-specific-actions.png)

**Code linting**

Code linting describes how the editor highlights potential errors in your code before you've even built it\. For example, the linting tool call out if you're trying to use an uninitialized variable or trying to assign a value to a variable that's expecting a different type\. 

![\[Liniting highlight errors before you build your code\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/linting.png)

**Debugging options**

You can implement breakpoints and watch expressions\. Set your breakpoints in the source code and display the debugger pane to define relevant conditions\. 

![\[Debugging options\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/debugging_options.png)

**Debugging using configuration files**

You can also control your debugging configuration by using launch configurations and tasks which AWS Cloud9 supports via the `launch.json` and `tasks.json` configuration files\. For examples of launch configurations and how they can be used, see [Java debug configuration\.](https://github.com/microsoft/vscode-java-debug/blob/main/Configuration.md)

**Java commands**

You can run commands from the AWS Cloud9 command panel by pressing **Ctrl\+\.** or **F1**\. Then filter the relevant commands by entering "java"\.

![\[Listing available Java commands\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/java_commands.png)

**Quick fixes**

With quick fixes, you can resolve errors caused by using undeclared variables or undefined methods by creating stubs for the missing elements\. 

![\[Implementing a quick fix\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/quick_fix_java.png)

**Refactoring**

Refactoring allows you to restructure your code without changing its behavior\. To access options such as organizing imports or creating constructors, open the context \(right\-click\) menu for the item and choose **Refactoring**\.

![\[Refactoring feature\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/refactoring_java.png)

**Renaming**

Renaming is a refactoring feature that allows you to easily modify the names of selected variables, functions, and classes everywhere that they appear in the code with a single action\. To change a name, open the context \(right\-click\) menu for the item and choose **Rename**\. Renaming affects every instance of the name in your code\. 

![\[Renaming a class name\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/renaming_refactoring_java.png)

## Optional tools for Java development<a name="optional-tools"></a>

The extensions that provide enhanced Java support include features that allow you to integrate the Gradle and Maven automation tools into your project development\. These tools aren't pre\-installed in your AWS Cloud9 development environment\. For more information on installing and using these optional build tools, see the following resources:
+ **Gradle**: [Getting started guide](https://docs.gradle.org/current/userguide/getting_started.html)
+ **Maven**: [Maven in 5 minutes](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)

## <a name="java-projects"></a>