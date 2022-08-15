# Language support in the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="language-support"></a>

The AWS Cloud9 IDE supports many programming languages\. The following table lists the languages that are supported and to what level\.


****  

| Language | Syntax highlighting 1  | Run UI 2  | Outline view | Code hints and linting | Code completion | Debugging 3  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  C\+\+  |  ✓  |  ✓  |  ✓  |  |  ✓ 5   |  ✓ 4   | 
|  C\#  |  ✓  |  |  ✓  |  |  ✓ 5   |  | 
|  CoffeeScript  |  ✓  |  ✓  |  |  |  |  | 
|  CSS  |  ✓  |  |  |  |  ✓  |  | 
|  Dart  |  ✓  |  |  |  |  |  | 
|  Go  |  ✓  |  ✓  |  ✓  |  ✓  |  ✓ 4   |  ✓ 4   | 
|  Haskell  |  ✓  |  |  |  |  |  | 
|  HTML  |  ✓  |  ✓  |  ✓  |  |  ✓  |  | 
|  Java6  |  ✓  | ✓ |  ✓  | ✓ |  ✓   | ✓ | 
|  JavaScript  |  ✓  |  ✓  |  ✓  |  ✓  |  ✓  |  | 
|  Node\.js  |  ✓  |  ✓  |  ✓  |  ✓  |  ✓  |  ✓   | 
|  PHP  |  ✓  |  ✓  |  ✓  |  ✓  |  ✓ 7   |  ✓  | 
|  Python  |  ✓  |  ✓  |  ✓  |  ✓  |  ✓ 8   |  ✓  | 
|  Ruby  |  ✓  |  ✓  |  ✓  |  ✓  |  ✓ 5   |  | 
|  Shell script  |  ✓  |  ✓  |  ✓  |  ✓  |  ✓ 5   |  | 
|  TypeScript9  |  ✓  |  ✓  |  ✓  |  ✓  |  ✓   |  | 

 **Notes** 

 1 The AWS Cloud9 IDE provides syntax highlighting for many more languages\. For a complete list, in the menu bar of the IDE, choose **View, Syntax**\.

 2 You can run programs or scripts at the click of a button for languages marked with a **✓**, without using the command line\. For languages not marked with a **✓** or not displayed on the **Run, Run With** menu bar in the IDE, you can create a runner for that language\. For instructions, see [Create a Builder or Runner](build-run-debug.md#build-run-debug-create-builder-runner)\.

 3 You can use the IDE's built\-in tools to debug programs or scripts for languages marked with a **✓**\. For instructions, see [Debug Your Code](build-run-debug.md#build-run-debug-debug)\.

 4 This feature is in an experimental state for this language\. It is not fully implemented and is not documented or supported\.

 5 This feature supports only local functions for this language\.

 6 Enhanced support for *Java SE 11* features can be activated in AWS Cloud9 EC2 development environments with 2 GiB or more of memory\. For more information, see [Enhanced support for Java development](enhanced-java.md)\.

 7 To specify paths for AWS Cloud9 to use for completion of custom PHP code, in the AWS Cloud9 IDE turn on the **Project, PHP Support, Enable PHP code completion** setting in **Preferences**, and then add the paths to the custom code to the **Project, PHP Support, PHP Completion Include Paths** setting\.

 8 To specify paths for AWS Cloud9 to use for completion of custom Python code, in the AWS Cloud9 IDE turn on the **Project, Python Support, Enable Python code completion** setting in **Preferences**, and then add the paths to the custom code to the **Project, Python Support, PYTHONPATH** setting\.

 9 The AWS Cloud9 IDE provides additional support for some programming languages, such as TypeScript \(version 3\.7\.5 supported in the AWS Cloud9 IDE\), within the context of a language project\. For more information, see [Working with Language Projects](projects.md)\.