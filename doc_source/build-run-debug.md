# Working with Builders, Runners, and Debuggers in the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="build-run-debug"></a>

A *builder* instructs the AWS Cloud9 IDE how to build a project's files\. A *runner* instructs the AWS Cloud9 IDE how to run files of a specific type\. A runner can use a *debugger* to help find any problems in the source code of the files\.

You can use the AWS Cloud9 IDE to build, run, and debug your code in the following ways:
+ Use a builder to build your project's files\. See [Build Your Project's Files](#build-run-debug-build)\.
+ Use a runner to run \(and optionally, to debug\) your code\. See [Built\-In Build, Run, and Debug Support](#build-run-debug-supported) and [Run Your Code](#build-run-debug-run)\.
+ Change a built\-in runner to run \(and optionally, to debug\) your code in a different way from how it was originally defined\. See [Change a Built\-In Runner](#build-run-debug-change-runner)\.
+ Use a runner to run \(and optionally, to debug\) your code with a custom combination of file name, command line options, debug mode, current working directory, and environment variables\. See [Create a Run Configuration](#build-run-debug-create-run-config)\.
+ Create your own builder or runner\. See [Create a Builder or Runner](#build-run-debug-create-builder-runner)\.

## Built\-In Build, Run, and Debug Support<a name="build-run-debug-supported"></a>

The AWS Cloud9 IDE provides built\-in support for building, running, and debugging code for several languages\. For a complete list, see [Language Support](language-support.md)\.

Built\-in build support is available on the menu bar with the **Run**, **Build System** and **Run**, **Build** menu commands\. To add support for a programming language or tool that isn't listed, see [Create a Builder or Runner](#build-run-debug-create-builder-runner)\.

Built\-in run support is available with the **Run** button, and on the menu bar with the **Run**, **Run With** and **Run**, **Run Configurations** menu commands\. To add support for a programming language or tool that isn't listed, see [Create a Builder or Runner](#build-run-debug-create-builder-runner) and [Create a Run Configuration](#build-run-debug-create-run-config)\.

Built\-in debug support is available through the **Debugger** window\. To display the **Debugger** window, choose the **Debugger** button\. If the **Debugger** button is not visible, choose **Window**, **Debugger** on the menu bar\.

## Build Your Project's Files<a name="build-run-debug-build"></a>

1. Open a file that corresponds to the code you want to build\.

1. On the menu bar, choose **Run, Build System**, and then choose the name of the builder to use, if it isn't already chosen\. If the builder you want to use isn't listed, stop this procedure, complete the steps in [Create a Builder or Runner](#build-run-debug-create-builder-runner), and then return to this procedure\.

1. Choose **Run, Build**\.

## Run Your Code<a name="build-run-debug-run"></a>

1. Open a file that corresponds to the code you want to run, if the file isn't already open and selected\.

1. On the menu bar, choose one of the following:
   + To run the code with the closest matching built\-in runner, choose **Run, Run**\. If AWS Cloud9 cannot find one, this command is disabled\.
   + To run the code with the run configuration that AWS Cloud9 last used, choose **Run, Run Last**\.
   + To run the code with a specific runner, choose **Run, Run With**, and then choose the name of the runner\. If the runner you want to use isn't listed, stop this procedure, complete the steps in [Create a Builder or Runner](#build-run-debug-create-builder-runner), and then return to this procedure\.
   + To run the code with a specific runner with a custom combination of file name, command line options, debug mode, current working directory, and environment variables, choose **Run, Run Configurations**, and then choose the run configuration's name\. In the run configuration tab that is displayed, choose **Runner: Auto**, choose the runner you want to use, and then choose **Run**\. If the runner you want to use isn't listed, stop this procedure, complete the steps in [Create a Builder or Runner](#build-run-debug-create-builder-runner), and then return to this procedure\.

## Debug Your Code<a name="build-run-debug-debug"></a>

1. On the run configuration tab for your code, choose **Run in Debug Mode**\. The bug icon turns to green on a white background\. For more information, see [Run Your Code](#build-run-debug-run) and [Create a Run Configuration](#build-run-debug-create-run-config)\.

1. Set any breakpoints in your code you want to pause at during the run, as follows:

   1. Open each file that you want to set a breakpoint in\.

   1. At each point in a file where you want to set a breakpoint, choose the blank area in the gutter to the left of the line number\. A red circle appears\.

      To remove a breakpoint, choose the existing breakpoint in the gutter\.

      To disable a breakpoint instead of removing it, in the **Debugger** window, in **Breakpoints**, clear the box that corresponds to the breakpoint you want to disable\. To enable the breakpoint again, select the box you cleared\.

      To disable all breakpoints at once, in the **Debugger** window, choose **Deactivate All Breakpoints**\. To enable all breakpoints again, choose **Activate All Breakpoints**\.

      If the **Debugger** window isn't visible, choose the **Debugger** button\. If the **Debugger** button isn't visible, on the menu bar choose **Window**, **Debugger**\.

1. Set any watch expressions for which you want to get the value at the point where a run pauses, as follows:

   1. In the **Debugger** window, in **Watch Expressions**, choose **Type an expression here**\.

   1. Type the expression you want to watch, and then press `Enter`\.

      To change an existing watch expression, right\-click the watch expression, and then choose **Edit Watch Expression**\. Type the change, and then press `Enter`\.

      To remove an existing watch expression, right\-click the watch expression, and then choose **Remove Watch Expression**\.

1. Run your code as described in [Run Your Code](#build-run-debug-run)\.

Whenever a run pauses, you can do the following in the **Debugger** window, as shown\.

![\[The Debugger window menu bar\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-debugger.png)

![\[Debugger window sections\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-debugger-areas.png)
+  **Run your code to the next breakpoint** \(or to the next logical stopping point if there are no more breakpoints\): Choose **Resume**\.
+  **Skip over running statement by statement through the next method or function call**: Choose **Step Over**\.
+  **Run your code to the next statement and then pause again**: Choose **Step Into**\.
+  **Stop running statement by statement in the current method or function call**: Choose **Step Out**\.
+  **Disable all existing breakpoints**: Choose **Deactivate All Breakpoints**\. **Re\-enable all breakpoints**: Choose **Activate All Breakpoints**\.
+  **Don't pause whenever the code throws an exception**: Keep choosing the exceptions behavior button until the tooltip reads **Don't pause on exceptions** \(gray\)\.
+  **Pause whenever the code throws an exception**: Keep choosing the exceptions behavior button until the tooltip reads **Pause on all exceptions** \(red\)\.
+  **Pause only when the code throws an uncaught exception**: Keep choosing the exceptions behavior button until the tooltip reads **Pause on uncaught exceptions** \(blue\)\.
+  **Open an available script**: Choose **Available internal and external scripts**, and then choose the script\.
+  **View the list of current watch expressions**: See the **Watch Expressions** area\.
+  **View the execution path that brought the code to the current breakpoint**: See the **Call Stack** area\.
+  **View the list of local variables**: See the **Local Variables** area\.
+  **Disable individual breakpoints**: In **Breakpoints**, clear the boxes that correspond to the breakpoints you want to disable\. To enable the breakpoints again, select the boxes you cleared earlier\.

Whenever a run pauses, you can also pause your mouse pointer on any displayed piece of code \(for example, a variable\) to show any available information about it in a tooltip\.

## Change a Built\-In Runner<a name="build-run-debug-change-runner"></a>

1. On the menu bar, choose **Run, Run With**, and then choose the built\-in runner you want to change\.

1. Stop the runner from trying to run your code by choosing, **Stop** on the run configuration tab that displays\.

1. Choose **Runner: My Runner**, where **My Runner** is the name of the runner you want to change, and then choose **Edit Runner**\.

1. On the **My Runner\.run** tab that is displayed, change the runner's current definition\. See [Define a Builder or Runner](#build-run-debug-define-builder-runner)\.

1. Choose **File, Save As**\. Save the file with the same name \(**My Runner\.run**\) in the `my-environment/.c9/runners` directory, where `my-environment` is the name of your AWS Cloud9 development environment\.

**Note**  
Any changes you make to a built\-in runner apply only to the environment you made those changes in\. To apply your changes to a separate environment, open the other environment, and then follow the preceding steps to open, edit, and save those same changes to that built\-in runner\.

## Create a Run Configuration<a name="build-run-debug-create-run-config"></a>

On the menu bar, choose **Run, Run Configurations, New Run Configuration**\. On the run configuration tab that is displayed, do the following:

1. In the box next to **Run** and **Restart**, type the name that will display on the **Run, Run Configurations** menu for this run configuration\.

1. In the **Command** box, type any custom command line options you want to use\.

1. To have this run configuration use the runner's predefined debugging settings, choose **Run in Debug Mode**\. The bug icon will turn to green on a white background\.

1. To have this run configuration use a specific working directory, choose **CWD**, choose the directory to use, and then choose **Select**\.

1. To have this run configuration use specific environment variables, choose **ENV**, and then type the name and value of each environment variable\.

To use this run configuration, open the file the corresponds to the code you want to run\. Choose **Run, Run Configurations** on the menu bar, and then choose this run configuration's name\. In the run configuration tab that displays, choose **Runner: Auto**, choose the runner you want to use, and then choose **Run**\.

**Note**  
Any run configuration you create applies only to the environment you created that run configuration in\. To add that run configuration to a separate environment, open the other environment, and then follow the preceding steps to create the same run configuration in that environment\.

## Create a Builder or Runner<a name="build-run-debug-create-builder-runner"></a>

1. To create a builder, on the menu bar, choose **Run, Build System, New Build System**\. To create a runner, on the menu bar, choose **Run, Run With, New Runner**\.

1. On the builder tab \(labeled **My Builder\.build**\) or runner tab \(labeled **My Runner\.run**\) that is displayed, define the builder or runner\. See [Define a Builder or Runner](#build-run-debug-define-builder-runner)\.

1. After you define the builder or runner, choose **File, Save As**\. For a builder, save the file with the `.build` extension in the `my-environment/.c9/builders` directory, where `my-environment` is the name of your environment\. For a runner, save the file with the `.run` file extension in the `my-environment/.c9/runnders` directory, where `my-environment` is the name of your environment\. The file name you specify will be the name that is displayed on the **Run, Build System** menu \(for a builder\) or the **Run, Run With** menu \(for a runner\)\. Therefore, unless you specify a different file name, by default the display name will be **My Builder** \(for a builder\) or **My Runner** \(for a runner\)\.

To use this builder or runner, see [Build Your Project's Files](#build-run-debug-build) or [Run Your Code](#build-run-debug-run)\.

**Note**  
Any builder or runner you create applies only to the environment you created that builder or runner in\. To add that run builder or runner to a separate environment, open the other environment, and then follow the preceding steps to create the same builder or runner in that environment\.

## Define a Builder or Runner<a name="build-run-debug-define-builder-runner"></a>

This procedure assumes you have already begun to create a builder or runner by choosing **Run, Build System, New Build System** \(for a builder\) or **Run, Run With, New Runner** \(for a runner\)\.

On the builder or runner tab that is displayed, use JSON to define the runner or builder\. Start with the following code as a template\.

For a builder, start with this code\.

```
{
  "cmd": [],
  "info": "",
  "env": {},
  "selector": ""
}
```

For a runner, start with this code\.

```
{
  "cmd": [],
  "script": "",
  "working_dir": "",
  "info": "",
  "env": {},
  "selector": "",
  "debugger": "",
  "debugport": ""
}
```

In the preceding code:
+  `cmd`: Represents a comma\-separated list of strings for AWS Cloud9 to run as a single command\.

  When AWS Cloud9 runs this command, each string in the list will be separated by a single space\. For example, AWS Cloud9 will run `"cmd": [ "ls", "$file", "$args"]` as `ls $file $args`, where AWS Cloud9 will replace `$file` with the full path to the current file and `$args` with any arguments entered after the file name\. For more information, see the list of supported variables later in this section\.
+  `script`: Represents a bash script \(which can also be specified as an array of lines as needed for readability\) that the runner executes in the terminal\.
+  `working_dir`: Represents the directory that the runner will run from\.
+  `info`: Represents any string of text you want to display to the user at the beginning of the run\. This string can contain variables, for example `Running $project_path$file_name...`, where AWS Cloud9 will replace `$project_path` with the directory path of the current file and `$file_name` with the name portion of the current file\. See the list of supported variables later in this section\.
+  `env`: Represents any array of command line arguments for AWS Cloud9 to use, for example:

  ```
  "env": {
    "LANG": "en_US.UTF-8",
    "SHLVL": "1"
  }
  ```
+  `selector`: Represents any regular expression that you want AWS Cloud9 to use to identify the file names that apply to this runner\. For example, you could specify `source.py` for Python files\.
+  `debugger`: Represents the name of any available debugger you want AWS Cloud9 to use that is compatible with this runner\. For example, you could specify `v8` for the V8 debugger\.
+  `debugport`: Represents the port number you want AWS Cloud9 to use during debugging\. For example, you could specify `15454` for the port number to use\.

The following table shows the variables you can use\.


****  

|  **Variable**  |  **Description**  | 
| --- | --- | 
|   `$file_path`   |  The directory of the current file, for example, `/home/ec2-user/environment` or `/home/ubuntu/environment`\.  | 
|   `$file`   |  The full path to the current file, for example, `/home/ec2-user/environment/hello.py` or `/home/ubuntu/environment/hello.py`\.  | 
|   `$args`   |  Any arguments entered after the file name, for example, `"5" "9"`\.  | 
|   `$file_name`   |  The name portion of the current file, for example, `hello.py`\.  | 
|   `$file_extension`   |  The extension of the current file, for example, `py`\.  | 
|   `$file_base_name`   |  The name of the current file without the file extension, for example, `hello`\.  | 
|   `$packages`   |  The full path to the packages folder\.  | 
|   `$project`   |  The full path to the current project folder\.  | 
|   `$project_path`   |  The directory of the current project file, for example, `/home/ec2-user/environment/` or `/home/ubuntu/environment/`\.  | 
|   `$project_name`   |  The name of the current project file without the file extension, for example, `my-demo-environment`\.  | 
|   `$project_extension`   |  The extension of the current project file\.  | 
|   `$project_base_name`   |  The name of the current project file without the extension\.  | 
|   `$hostname`   |  The hostname of the environment, for example, `192.0.2.0`\.  | 
|   `$hostname_path`   |  The hostname of the environment with the relative path to the project file, for example, `https://192.0.2.0/hello.js`\.  | 
|   `$url`   |  The full URL to access the environment, for example, `https://192.0.2.0.`\.  | 
|   `$port`   |  The port assigned to the environment, for example, `8080`\.  | 
|   `$ip`   |  The IP address to run a process against the environment, for example, `0.0.0.0`\.  | 

As an example, the following builder file named `G++.build` defines a builder for GCC that runs the ** `g++` ** command with the `-o` option to compile the current file \(for example, `hello.cpp`\) into an object module\. Then it links the object module into a program with the same name as the current file \(for example, `hello`\)\. Here the equivalent command is `g++ -o hello hello.cpp`\.

```
{
  "cmd": [ "g++", "-o", "$file_base_name", "$file_name" ],
  "info": "Compiling $file_name and linking to $file_base_name...",
  "selector": "source.cpp"
}
```

As another example, the following runner file named `Python.run` defines a runner that uses Python to run the current file with any arguments that were provided\. For example, if the current file is named `hello.py` and the arguments `5` and `9` were provided, the equivalent command is `python hello.py 5 9`\.

```
{
  "cmd": [ "python", "$file_name", "$args" ],
  "info": "Running $file_name...",
  "selector": "source.py"
}
```

Finally, the following runner file named `Print Run Variables.run` defines a runner that simply outputs the value of each available variable and then stops\.

```
{
  "info": "file_path = $file_path, file = $file, args = $args, file_name = $file_name, file_extension = $file_extension, file_base_name = $file_base_name, packages = $packages, project = $project, project_path = $project_path, project_name = $project_name, project_extension = $project_extension, project_base_name = $project_base_name, hostname = $hostname, hostname_path = $hostname_path, url = $url, port = $port, ip = $ip"
}
```