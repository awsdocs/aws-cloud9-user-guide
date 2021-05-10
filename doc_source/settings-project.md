# Working with Project Settings in the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="settings-project"></a>

 *Project settings*, which apply only to the current AWS Cloud9 development environment, include the following kinds of settings:
+ Code editor behaviors, such as whether to use soft tabs and new file line ending behavior
+ File types to ignore
+ The types of hints and warnings to display or suppress
+ Code and formatting behaviors for programming languages such as JavaScript, PHP, Python, and Go
+ The types of configurations to use when running and building code

Although project settings apply to only a single environment, you can apply the project settings for one environment to any other environment\.
+  [View or Change Project Settings](#settings-project-view) 
+  [Apply the Current Project Settings for an Environment to Another Environment](#settings-project-apply) 
+  [Project Setting Changes You Can Make](#settings-project-change) 

## View or change Project Settings<a name="settings-project-view"></a>

1. On the menu bar, choose **AWS Cloud9**, **Preferences**\.

1. To view the project settings for the current environment, on the **Preferences** tab, in the side navigation pane, choose **Project Settings**\.

1. To change the current project settings for the environment, change the settings you want in the **Project Settings** pane\.

See [Project Setting Changes You Can Make](#settings-project-change)\.

## Apply the current Project Settings for an environment to another environment<a name="settings-project-apply"></a>

1. In both the source and target environment, on the menu bar of the AWS Cloud9 IDE, choose **AWS Cloud9, Open Your Project Settings**\.

1. In the source environment, copy the contents of the **project\.settings** tab that is displayed\.

1. In the target environment, overwrite the contents of the **project\.settings** tab with the copied contents from the source environment\.

1. In the target environment, save the **project\.settings** tab\.

## Project Settings you can change<a name="settings-project-change"></a>

These sections describe the kinds of project settings that you can change on the **Preferences** tab's **Project Settings** pane\.
+  [EC2 Instance](#settings-project-change-ec2-instance) 
+  [Code Editor \(Ace\)](#settings-project-change-code-editor-ace) 
+  [Find in Files](#settings-project-change-find-in-files) 
+  [Hints & Warnings](#settings-project-change-hints-and-warnings) 
+  [JavaScript Support](#settings-project-change-javascript-support) 
+  [Build](#settings-project-change-build) 
+  [Run & Debug](#settings-project-change-run-and-debug) 
+  [Run Configurations](#settings-project-change-run-configurations) 
+  [Code Formatters](#settings-project-change-code-formatters) 
+  [TypeScript Support](#settings-project-change-typescript-support) 
+  [PHP Support](#settings-project-change-php-support) 
+  [Python Support](#settings-project-change-python-support) 
+  [Go Support](#settings-project-change-go-support) 

### EC2 Instance<a name="settings-project-change-ec2-instance"></a>

** **Stop my environment** **  
Choose when to automatically stop your environment's Amazon EC2 instance \(if used\) after you close all web browser instances that are connected to the IDE for that environment\. You can choose a range of time periods from a week to 30 minutes\. You can also choose never to automatically stop the Amazon EC2 instance after exiting the AWS Cloud9 IDE\.  
If you want to stop the instance even sooner than 30 minutes after finishing with the IDE, you can [stop it manually using the console interface](#stopping-instance-manually)\.

### Code Editor \(Ace\)<a name="settings-project-change-code-editor-ace"></a>

** **Soft Tabs** **  
If selected, inserts the specified number of spaces instead of a tab character each time you press `Tab`\.

** **Autodetect Tab Size on Load** **  
If selected, AWS Cloud9 attempts to guess the tab size\.

** **New File Line Endings** **  
The type of line endings to use for new files\.  
Valid options include:  
+  **Windows \(CRLF\)** to end lines with a carriage return and then a line feed\.
+  **Unix \(LF\)** to end lines with just a line feed\.

** **On Save, Strip Whitespace** **  
If selected, AWS Cloud9 attempts to remove what it considers to be unnecessary spaces and tabs from a file each time that file is saved\.

### Find in Files<a name="settings-project-change-find-in-files"></a>

** **Ignore these Files** **  
When finding in files, the types of files that AWS Cloud9 will ignore\.

** **Maximum number of files to search \(in 1000\)** **  
When finding in files, the maximum number of files, in multiples of 1,000, that AWS Cloud9 will find in the current scope\.

### Hints & Warnings<a name="settings-project-change-hints-and-warnings"></a>

** **Warning Level** **  
The minimum level of messages to enable\.  
Valid values include:  
+  **Info** to enable informational, warning, and error messages\.
+  **Warning** to enable just warning and error messages\.
+  **Error** to enable just error messages\.

** **Mark Missing Optional Semicolons** **  
If enabled, AWS Cloud9 flags in a file each time it notices a semicolon that could be used in code, but that isn't used\.

** **Mark Undeclared Variables** **  
If enabled, AWS Cloud9 flags in a file each time it notices an undeclared variable in code\.

** **Mark Unused Function Arguments** **  
If enabled, AWS Cloud9 flags in a file each time it notices an unused argument in a function\.

** **Ignore Messages Matching Regex** **  
AWS Cloud9 will not display any messages matching the specified regular expression\. For more information, see [Writing a regular expression pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions#Writing_a_regular_expression_pattern) in the *JavaScript Regular Expressions* topic on the Mozilla Developer Network\.

### JavaScript Support<a name="settings-project-change-javascript-support"></a>

** **Customize JavaScript Warnings With \.eslintrc** **  
If enabled, AWS Cloud9 uses an `.eslintrc` file to determine which JavaScript warnings to enable or disable\. For more information, see [Configuration File Formats](http://eslint.org/docs/user-guide/configuring#configuration-file-formats) on the ESLint website\.

** **JavaScript Library Code Completion** **  
The JavaScript libraries AWS Cloud9 uses to attempt to suggest or do automatic code completion\.

** **Format Code on Save** **  
If enabled, AWS Cloud9 attempts to format the code in a JavaScript file every time that file is saved\.

** **Use Builtin JSBeautify as Code Formatter** **  
If enabled, AWS Cloud9 uses its internal implementation of JSBeautify to attempt to increase the readability of code in files\.

** **Custom Code Formatter** **  
The command for AWS Cloud9 to attempt to run when formatting code in a JavaScript file\.

### Build<a name="settings-project-change-build"></a>

** **Builder Path in environment** **  
The path to any custom build configurations\.

### Run & Debug<a name="settings-project-change-run-and-debug"></a>

** **Runner Path in Environment** **  
The path to any custom run configurations\.

** **Preview URL** **  
The URL to use to preview applications for the environment\.

### Run Configurations<a name="settings-project-change-run-configurations"></a>

The custom run configurations for this environment\.

** **Remove Selected Configs** **  
Deletes the selected run configurations\.

** **Add New Config** **  
Creates a new run configuration\.

** **Set As Default** **  
Sets the selected run configuration as the default run configuration\.

### Code Formatters<a name="settings-project-change-code-formatters"></a>

** **JSBeautify settings** **  
Settings for increasing the readability of code in files\.    
** **Format Code on Save** **  
If enabled, AWS Cloud9 attempts to apply JSBeautify settings whenever code files are saved\.  
** **Use JSBeautify for JavaScript** **  
If enabled, AWS Cloud9 attempts to apply JSBeautify settings whenever JavaScript files are saved\.  
** **Preserve Empty Lines** **  
If enabled, AWS Cloud9 does not remove empty lines in code files\.  
** **Keep Array Indentation** **  
If enabled, AWS Cloud9 preserves the indentation of element declarations in arrays in code files\.  
** **JSLint Strict Whitespace** **  
If enabled, AWS Cloud9 attempts to apply JSLint whitespace rules in code files\. For more information, see "Whitespace" in [JSLint Help](http://jslint.com/help.html)\.  
** **Braces** **  
Specifies the alignment of braces in code\.  
Valid values include:  
+  **Braces with control statement** to move each beginning and end brace to align with its related control statement, as needed\.

  For example, this code:

  ```
  for (var i = 0; i < 10; i++) { if (i == 5) { console.log("Halfway done.") }}
  ```

  Turns into this code when the file is saved:

  ```
  for (var i = 0; i < 10; i++) {
     if (i == 5) {
        console.log("Halfway done.")
     }
  }
  ```
+  **Braces on own line** to move each brace to its own line, as needed\.

  For example, this code:

  ```
  for (var i = 0; i < 10; i++) { if (i == 5) { console.log("Halfway done.") }}
  ```

  Turns into this code when the file is saved:

  ```
  for (var i = 0; i < 10; i++) {if (i == 5)
    {
       console.log("Halfway done.")
    }
    }
  ```
+  **End braces on own line** to move each end brace to its own line, as needed\.

  For example, this code:

  ```
  for (var i = 0; i < 10; i++) {
    if (i == 5) { console.log("Halfway done.") }
  }
  ```

  Turns into this code when the file is saved:

  ```
  for (var i = 0; i < 10; i++) {
     if (i == 5) {
        console.log("Halfway done.")
     }
  }
  ```  
** **Preserve Inline Blocks** **  
If enabled, AWS Cloud9 does not attempt to move the beginning and ending braces for inline blocks to separate lines, if those braces are on the same line\.  
** **Space Before Conditionals** **  
If enabled, AWS Cloud9 adds a space before each conditional declaration, as needed\.  
** **Unescape Strings** **  
If enabled, AWS Cloud9 converts escaped strings to their unescaped equivalents\. For example, converts `\n` to a newline character and converts `\r` to a carriage return character\.  
** **Indent Inner Html** **  
If enabled, AWS Cloud9 indents `<head>` and `<body>` sections in HTML code\.

### TypeScript Support<a name="settings-project-change-typescript-support"></a>

** **Format Code on Save** **  
If enabled, AWS Cloud9 attempts to format TypeScript code whenever TypeScript files are saved\.

** **Custom Code Formatter** **  
The path to any custom code formatting configuration for TypeScript code\.

### PHP Support<a name="settings-project-change-php-support"></a>

** **Enable PHP code Completion** **  
If enabled, AWS Cloud9 attempts to complete PHP code\.

** **PHP Completion Include Paths** **  
Locations that AWS Cloud9 uses to attempt to help complete PHP code\. For example, if you have custom PHP files that you want AWS Cloud9 to use for completion, and those files are somewhere in the `~/environment` directory, add `~/environment` to this path\.

** **Format Code on Save** **  
If enabled, AWS Cloud9 attempts to format PHP code whenever PHP files are saved\.

** **Custom Code Formatter** **  
The path to any custom code formatting configuration for PHP code\.

### Python Support<a name="settings-project-change-python-support"></a>

** **Enable Python code completion** **  
If enabled, AWS Cloud9 attempts to complete Python code\. To set the paths for AWS Cloud9 to use to complete Python code, use the **PYTHONPATH** setting\.

** **Python Version** **  
Specifies the version of Python to use\.

** **Pylint command line options** **  
Options for AWS Cloud9 to use for Pylint with Python code\. For more information, see the [Pylint User Manual](https://pylint.readthedocs.io/en/latest/) on the Pylint website\.

** **PYTHONPATH** **  
The paths to Python libraries and packages for AWS Cloud9 to use\. For example, if you have custom Python libraries and packages in the `~/environment` directory, add `~/environment` to this path\.

** **Format Code on Save** **  
If enabled, AWS Cloud9 attempts to format Python code whenever Python files are saved\.

** **Custom Code Formatter** **  
The path to any custom code formatting configuration for Python code\.

### Go Support<a name="settings-project-change-go-support"></a>

** **Enable Go code completion** **  
If enabled, AWS Cloud9 attempts to complete Go code\.

** **Format Code on Save** **  
If enabled, AWS Cloud9 attempts to format Go code whenever Go files are saved\.

** **Custom Code Formatter** **  
The path to any custom code formatting configuration for Go code\.

## Manually stopping your environment's EC2 instance<a name="stopping-instance-manually"></a>

The [EC2 Instance](#settings-project-change-ec2-instance) setting allows you to automatically stop your environment's Amazon EC2 instance as quickly as 30 minutes after you close all web browser instances that are connected to the IDE\.

But you also can manually stop the instance immediately using the console\.

## To manually stop an environment's EC2 instance

1. After you've closed all web browser instances that are connected to the IDE, choose **Your environments** in the AWS Cloud9 console\.

1. Choose the button in the top\-right of the pane that shows details of the environment that you were using, and choose **View details**\.

1. In **Environment details**, under **EC2 Instance**, choose **Go To Instance**\.

1. In the Amazon EC2 console, under **Instance state**, choose the check box to select your environment's instance \(the **Instance state** may indicate that the instance is still running\)\.

1. Choose **Instance state** and select **Stop instance**\.

1. When prompted for confirmation, choose **Stop**\. It can take a few minutes for the instance to stop\.