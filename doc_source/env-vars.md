# Working with Custom Environment Variables in the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="env-vars"></a>

The AWS Cloud9 IDE supports getting and setting custom environment variables\. You can get and set custom environment variables in the AWS Cloud9 IDE in the following ways\.
+  [Set Command\-Level Custom Environment Variables](#env-vars-command-level) 
+  [Set Custom User Environment Variables in \~/\.bash\_profile](#env-vars-bash-profile) 
+  [Set Local Custom Environment Variables](#env-vars-local) 
+  [Set Custom User Environment Variables in \~/\.bashrc](#env-vars-bashrc) 
+  [Set Custom Environment Variables in the ENV List](#env-vars-env-list) 

## Set Command\-Level Custom Environment Variables<a name="env-vars-command-level"></a>

You can set command\-level custom environment variables as you run a command in your AWS Cloud9 development environment\. To test this behavior, create a file named `script.sh` with the following code:

```
#!/bin/bash

echo $MY_ENV_VAR
```

If you run the following command, the terminal displays `Terminal session`:

```
MY_ENV_VAR='Terminal session' sh ./script.sh
```

If you set the custom environment variable by using multiple approaches described in this topic, then when you try to get the custom environment variable's value, this setting takes priority over all of the others\.

## Set Custom User Environment Variables in \~/\.bash\_profile<a name="env-vars-bash-profile"></a>

You can set custom user environment variables in the `~/.bash_profile` file in your environment\. To test this behavior, add the following code to the `~/.bash_profile` file in your environment:

```
export MY_ENV_VAR='.bash_profile file'
```

If you then choose the **Run**, **Run With**, **Shell script** command on the menu bar, type `./script.sh` in the **Command** box of the runner tab, and then choose **Run**, the runner tab displays `.bash_profile file`\. \(This assumes you created the `script.sh` file as described earlier\.\)

## Set Local Custom Environment Variables<a name="env-vars-local"></a>

You can set local custom environment variables in a terminal session by running the ** `export` ** command\. To test this behavior, run the following command in a terminal session:

```
export MY_ENV_VAR='Command line export'
```

If you then choose the **Run**, **Run With**, **Shell script** command on the menu bar, type `./script.sh` in the **Command** box of the runner tab, and then choose **Run**, the runner tab displays `Command line export`\. \(This assumes you created the `script.sh` file as described earlier\.\)

If you set the same custom environment variable in your `~/.bash_profile` file and with the ** `export` ** command, then when you try to get the customer environment variable's value, the `~/.bash_profile` file setting takes priority\.

## Set Custom User Environment Variables in \~/\.bashrc<a name="env-vars-bashrc"></a>

You can set custom user environment variables in `~/.bashrc` file in your environment\. To test this behavior, add the following code to the `~/.bashrc` file in your environment:

```
export MY_ENV_VAR='.bashrc file'
```

If you then choose the **Run**, **Run With**, **Shell script** command on the menu bar, type `./script.sh` in the **Command** box of the runner tab, and then choose **Run**, the runner tab displays `.bashrc file`\. \(This assumes you created the `script.sh` file as described earlier\.\)

If you set the same custom environment variable with the ** `export` ** command and in your `~/.bashrc` file, then when you try to get the custom environment variable's value, the ** `export` ** command setting takes priority\.

## Set Custom Environment Variables in the ENV List<a name="env-vars-env-list"></a>

You can set custom environment variables in the **ENV** list on the **Run** tab\.

To test this behavior, do the following:

1. On the menu bar, choose **Run**, **Run Configurations**, **New Run Configuration**\.

1. On the **\[New\] \- Idle** tab, Choose **Runner: Auto**, and then choose **Shell script**\.

1. Choose **ENV**, and then type `MY_ENV_VAR` for **Name** and `ENV list` for **Value**\.

1. For **Command**, type `./script.sh`\.

1. Choose the **Run** button\. the runner tab displays `ENV list`\. \(This assumes you created the `script.sh` file as described earlier\.\)

If you set the same custom environment variable in your `~/.bash_profile` file, with the ** `export` ** command, in your `~/.bashrc` file, and in the **ENV** list, then when you try to get the custom environment variable's value, the `~/.bash_profile` file setting takes first priority, followed by the ** `export` ** command setting, the `~/.bashrc` file setting, and the **ENV** list setting\.

**Note**  
The **ENV** list is the only approach for getting and setting custom environment variables by using code, separate from a shell script\.