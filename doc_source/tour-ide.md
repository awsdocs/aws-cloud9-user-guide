# Tour the AWS Cloud9 IDE<a name="tour-ide"></a>

This topic provides a basic tour of the AWS Cloud9 integrated development environment \(IDE\)\. To take full advantage of this tour, follow the steps shown below in sequence\.

**Topics**
+ [Prerequisites](#tour-ide-prereqs)
+ [Step 1: Menu bar](#tour-ide-menu-bar)
+ [Step 2: Dashboard](#tour-ide-dashboard)
+ [Step 3: Environment window](#tour-ide-environment)
+ [Step 4: Editor, tabs, and panes](#tour-ide-editor)
+ [Step 5: Console](#tour-ide-console)
+ [Step 6: Open files section](#tour-ide-open-files)
+ [Step 7: Gutter](#tour-ide-gutter)
+ [Step 8: Status bar](#tour-ide-status-bar)
+ [Step 9: Outline window](#tour-ide-outline)
+ [Step 10: Go window](#tour-ide-go)
+ [Step 11: Immediate tab](#tour-ide-immediate)
+ [Step 12: Process list](#tour-ide-process-list)
+ [Step 13: Preferences](#tour-ide-preferences)
+ [Step 14: Terminal](#tour-ide-terminal)
+ [Step 15: Debugger window](#tour-ide-debugger)
+ [Final thoughts](#tour-ide-cleanup)

## Prerequisites<a name="tour-ide-prereqs"></a>

To go on this tour, you must have an AWS account and an open AWS Cloud9 development environment\. To learn how to do these things, you can follow the steps in [Getting started: basic tutorials for AWS Cloud9](tutorials-basic.md)\. Alternatively, you can explore separate related topics such as [Setting up AWS Cloud9](setting-up.md) and [Working with environments in AWS Cloud9](environments.md)\.

**Warning**  
Having an AWS Cloud9 development environment might result in charges to your AWS account\. These include possible charges for Amazon EC2 if you are using an EC2 environment\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/)\.

## Step 1: Menu bar<a name="tour-ide-menu-bar"></a>

The *menu bar*, at the top edge of the IDE, contains common commands for working with files and code and changing IDE settings\. You can also preview and run code from the menu bar\.

![\[The menu bar in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-menu-bar.png)

You can hide the menu bar by choosing the arrow at its edge, as follows\.

![\[Hiding the menu bar in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-hide-menu-bar.png)

You can show the menu bar again by choosing the arrow in the middle of where the menu bar was earlier, as follows\.

![\[Showing the menu bar again in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-show-menu-bar.png)

Compare your results to the following\.

![\[Hiding and showing the menu bar in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-hide-show-menu-bar.gif)

You can use the IDE to work with a set of files in the next several sections in this tutorial\. To set up these files, choose **File**, **New File**\.

Next, copy the following text into the `Untitled1` editor tab\.

```
fish.txt
--------
A fish is any member of a group of organisms that consist of
all gill-bearing aquatic craniate animals that lack limbs with
digits. They form a sister group to the tunicates, together
forming the olfactores. Included in this definition are
lampreys and cartilaginous and bony fish as well as various
extinct related groups.
```

To save the file, choose **File**, **Save**\. Name the file `fish.txt`, and then choose **Save**\.

Repeat these instructions, saving the second file as `cat.txt`, with the following contents\.

```
cat.txt
-------
The domestic cat is a small, typically furry, carnivorous mammal.
They are often called house cats when kept as indoor pets or
simply cats when there is no need to distinguish them from
other felids and felines. Cats are often valued by humans for
companionship and for their ability to hunt.
```

There are often several ways to do things in the IDE\. For example, to hide the menu bar, instead of choosing the arrow at its edge, you can choose **View**, **Menu Bar**\. To create a new file, instead of choosing **File, New File** you can press `Alt-N` \(for Windows/Linux\) or `Control-N` \(for MacOS\)\. To reduce this tutorial's length, we only describe one way to do things\. As you get more comfortable with the IDE, feel free to experiment and figure out the way that works best for you\.

## Step 2: Dashboard<a name="tour-ide-dashboard"></a>

The *dashboard* gives you quick access to each of your environments\. From the dashboard, you can create, open, and change the setting for an environment\.

To open the dashboard, on the menu bar, choose **AWS Cloud9**, **Go To Your Dashboard**\.

![\[Opening the AWS Cloud9 dashboard\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-go-dashboard.png)

To view the settings for your environment, choose the title inside of the **my\-demo\-environment** card\. To go back to the dashboard, use your web browser's back button or the navigation breadcrumb called **Environments**\.

To open to the IDE for your environment, choose **Open IDE** inside of the **my\-demo\-environment** card\.

**Note**  
It can take a few moments for the IDE to display again\.

## Step 3: Environment window<a name="tour-ide-environment"></a>

The **Environment** window shows a list of your folders and files in the environment\. You can also show different types of files, such as hidden files\.

To show or hide the contents of the **Environment** window, choose the **Environment** button\.

To show or hide the **Environment** window and the **Environment** button, choose **Window**, **Environment** on the menu bar\.

![\[The Environment window in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-environment-window.png)

To show or hide hidden files, in the **Environment** window, choose the gear icon, and then choose **Show Hidden Files**\.

![\[Showing hidden files using the Environment window\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-show-hidden-files.png)

## Step 4: Editor, tabs, and panes<a name="tour-ide-editor"></a>

The *editor* is where you can do things such as write code, run a terminal session, and change IDE settings\. Each instance of an open file, terminal session, and so on is represented by a *tab*\. Tabs can be grouped into *panes*\. Tabs are shown at the edge of their pane\.

![\[Tabs at the edge of a pane in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-tab-buttons.png)

To show or hide tabs, choose **View**, **Tab Buttons** on the menu bar\.

To open a new tab, choose the **\+** icon at the edge of the row of tabs\. Then choose one of the available commands, for example, **New File**, as follows\.

![\[New tab with commands to choose, such as New File\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-new-file.png)

To display two panes, choose the icon that looks like a drop\-down menu, which is at the edge of the row of tabs\. Then choose **Split Pane in Two Rows**, as follows\.

![\[Showing two panes by splitting one pane into two rows\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-split-pane-two-rows.png)

To return to a single pane, choose the drop\-down menu icon again, and then choose the single square icon, as follows\.

![\[Showing a single pane\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-single-pane-view.png)

## Step 5: Console<a name="tour-ide-console"></a>

The *console* is an alternate place for creating and managing tabs\. By default, it contains a Terminal tab, but can also contain other types of tabs\.

![\[AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-console.png)

To show or hide the console, choose **View**, **Console** on the menu bar\.

To expand or shrink the console, choose the resize icon, which is at the edge of the console, as follows\.

![\[Expanding the size of the console display\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-console-resize.png)

## Step 6: Open files section<a name="tour-ide-open-files"></a>

The **Open Files** section shows a list of all files that are currently open in the editor\. **Open Files** is part of the **Environment** window\.

![\[Open Files section in the Environment window\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-open-files.png)

To show or hide the **Open Files** section, choose **View**, **Open Files** on the menu bar\.

To switch between open files, choose the file of interest from the list\.

## Step 7: Gutter<a name="tour-ide-gutter"></a>

The *gutter*, at the edge of each file in the editor, shows things like line numbers and contextual symbols as you work with files\.

![\[Gutter in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-gutter.png)

To show or hide the gutter, choose **View**, **Gutter** on the menu bar\.

## Step 8: Status bar<a name="tour-ide-status-bar"></a>

The *status bar*, at the edge of each file in the editor, shows things like line and character numbers, file type preference, space and tab settings, and related editor settings\.

![\[Status bar in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-status-bar.png)

To show or hide the status bar, choose **View**, **Status Bar** on the menu bar\.

To go to a specific line number, choose a tab with the file of interest\. Then in the status bar, choose the line and character number \(it should be something like **7:45**\)\. Type a line number \(like `4`\), and then press `Enter`, as follows\.

![\[Going to specific line numbers using the AWS Cloud9 IDE status bar\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-go-to-line.png)

![\[Going to specific line numbers using the AWS Cloud9 IDE status bar\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-go-to-line.gif)

To change the file type preference, in the status bar, choose a different file type\. For example, for **cat\.txt**, choose **Ruby** to see the syntax colors change\. To go back to plain text colors, choose **Plain Text**, as follows\.

![\[Changing file type preference in the AWS Cloud9 IDE status bar\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-text-color.png)

![\[Changing file type preference in the AWS Cloud9 IDE status bar\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-text-color.gif)

## Step 9: Outline window<a name="tour-ide-outline"></a>

You can use the **Outline** window to quickly go to a specific file location\.

To show or hide the **Outline** window and the **Outline** button, choose **Window**, **Outline** on the menu bar\.

To see how the **Outline** window works, create a file named `hello.rb`\. Copy the following code into the file and save it\.

```
def say_hello(i)
  puts "Hello!"
  puts "i is #{i}"
end

def say_goodbye(i)
  puts "i is now #{i}"
  puts "Goodbye!"
end

i = 1
say_hello(i)
i += 1
say_goodbye(i)
```

To show or hide the contents of the **Outline** window, choose the **Outline** button\.

In the **Outline** window, choose **say\_hello\(i\)**, and then choose **say\_goodbye\(i\)**, as follows\.

![\[Outline window in AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-outline.png)

![\[Outline window in AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-outline.gif)

## Step 10: Go window<a name="tour-ide-go"></a>

You can use the **Go** window to open a file in the editor, go to a symbol's definition, run a command, or go to a line in the active file in the editor\.

![\[Go window.\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-go-window-first.png)

To show the contents of the **Go** window, choose the **Go** button \(the magnifying glass icon\)\.

To show or hide the **Go** window and the **Go** button, choose **Window**, **Go** on the menu bar\.

With the **Go** window open, you can:
+ Type a forward slash \(`/`\) followed by part or all of a file name\. In the list of matching files that displays, choose a file to open it in the editor\. For example, typing `/fish` lists `fish.txt`, while typing `/.txt` lists both `fish.txt` and `cat.txt`\.
**Note**  
File search is scoped only to non\-hidden files and non\-hidden folders in the **Environment** window\.
+ Type an at symbol \(`@`\) followed by the name of a symbol\. In the list of matching symbols that displays, choose a symbol to go to it in the editor\. For example, with the `hello.rb` file open and active in the editor, type `@hello` to list `say_hello(i)`, or type `@say` to list both `say_hello(i)` and `say_goodbye(i)`\.
**Note**  
If the active file in the editor is part of a supported language project, symbol search is scoped to the current project\. Otherwise, symbol search is scoped only to the active file in the editor\. For more information, see [Working with Language Projects in the AWS Cloud9 Integrated Development Environment \(IDE\)](projects.md)\.
+ Type a dot \(`.`\) followed by the name of a command\. In the list of commands that displays, choose a command to run it\. For example, typing `.closetab` and then pressing `Enter` closes the current tab in the editor\. For a list of available commands, see the [Commands reference for the AWS Cloud9 Integrated Development Environment \(IDE\)](commands.md)\.
+ Type a colon \(`:`\) followed by a number to go to that line number in the active file in the editor\. For example, with the `hello.rb` file open and active in the editor, type `:11` to go to line 11 in that file\.

![\[Go window in AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-go-window.png)

To see the keybindings for each of these actions based on the current keyboard mode and operating system, see each of the available **Go To** commands on the **Go** menu in the menu bar\.

## Step 11: Immediate tab<a name="tour-ide-immediate"></a>

The **Immediate** tab enables you to test small snippets of JavaScript code\. To see how the **Immediate** tab works, do the following\.

1. Open an **Immediate** tab by choosing **Window**, **New Immediate Window** on the menu bar\.

1. Run some code in the **Immediate** tab\. To try this, type the following code into the window, pressing `Shift-Enter` after typing line 1 and again after line 2\. Press `Enter` after line 3\. \(If you press `Enter` instead of `Shift-Enter` after you type line 1 or line 2, the code will run earlier than you want it to\.\)

   ```
   for (i = 0; i <= 10; i++) { // Press Shift-Enter after typing this line.
     console.log(i)            // Press Shift-Enter after typing this line.
   }                           // Press Enter after typing this line. The numbers 0 to 10 will be printed.
   ```  
![\[Running code in the Immediate tab\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-immediate.png)

## Step 12: Process list<a name="tour-ide-process-list"></a>

The **Process List** shows all of the running processes\. You can stop or even forcibly stop processes that you don't want to run anymore\. To see how the **Process List** window works, do the following\.

1. Show the **Process List** by choosing **Tools**, **Process List** on the menu bar\.

1. Find a process\. In the **Process List**, type the name of the process\.

1. Stop or forcibly stop a process\. In the list of processes, choose the process, and then choose **Kill** or **Force Kill**\.

![\[Process list in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-process-list.png)

## Step 13: Preferences<a name="tour-ide-preferences"></a>

 *Preferences* include the following settings\.
+ Settings for the current environment only, such as whether to use soft tabs in the editor, the file types to ignore, and code completion behaviors for languages such as PHP and Python\.
+ Your user settings across each of your environments, such as colors, fonts, and editor behaviors\.
+ Your keybindings, such as which shortcut key combinations you prefer to use to work with files and the editor\.
+ The IDE's overall theme\.

To show preferences, choose **AWS Cloud9**, **Preferences** on the menu bar\. Something like the following is displayed\.

![\[Showing preferences in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-preferences.png)

## Step 14: Terminal<a name="tour-ide-terminal"></a>

You can run one or more *terminal* sessions in the IDE\. To start a terminal session, choose **Window**, **New Terminal** on the menu bar\. Or, choose the "plus" icon next to the Console tabs and choose **New Terminal**\.

You can try running a command in the terminal\. For example, in the terminal, type `echo $PATH` and then press `Enter` to print the value of the `PATH` environment variable\.

You can also try running additional commands\. For example, try commands such as the following\.
+  ** `pwd` ** to print the path to the current directory\.
+  ** `aws --version` ** to print version information about the AWS CLI\.
+  ** `ls -l` ** to print information about the current directory\.

![\[Using the terminal in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-terminal.gif)

## Step 15: Debugger window<a name="tour-ide-debugger"></a>

You can use the **Debugger** window to debug your code\. For example, you can step through running code a portion at a time, watch the values of variables over time, and explore the call stack\.

**Note**  
This procedure is similar to [Step 2: Basic tour of the IDE](tutorial-tour-ide.md) from either of the [basic IDE tutorials](tutorials-basic.md)\.

To show or hide the **Debugger** window and the **Debugger** button, choose **Window**, **Debugger** on the menu bar\.

For this tutorial, you can experiment with the **Debugger** window and some JavaScript code by doing the following\.

1. Check the Node\.js installation in your environment by running the following command in a terminal session: **`node --version`**\. If Node\.js is installed, the Node\.js version number is shown in the output, and you can skip ahead to step 3 in this procedure \("Write some JavaScript code\.\.\."\)\.

1. If you need to install Node\.js, do the following\.

   1. Run the following two commands, one at a time, to be sure your environment has the latest updates and then download Node Version Manager \(nvm\)\. \(nvm is a simple Bash shell script that is useful for installing and managing Node\.js versions\. For more information, see [Node Version Manager](https://github.com/creationix/nvm/blob/master/README.md) on GitHub\.\)

      For Amazon Linux:

      ```
      sudo yum -y update
      curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash
      ```

      For Ubuntu Server:

      ```
      sudo apt update
      curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash
      ```

   1. Use a text editor to update your shell profile file \(for example, `~/.bashrc`\) to enable nvm to load\. For example, in the **Environment** window of the IDE, choose the gear icon, and then choose **Show Home in Favorites**\. Repeat this step and choose **Show Hidden Files** as well\.

   1. Open the `~/.bashrc` file\.

   1. Type or paste the following code at the end of the file to enable nvm to load\.

      For Amazon Linux:

      ```
      export NVM_DIR="/home/ec2-user/.nvm"
      [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm.
      ```

      For Ubuntu Server:

      ```
      export NVM_DIR="/home/ubuntu/.nvm"
      [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm.
      ```

   1. Save the file\.

   1. Close that terminal session and start a new one\. Then run the following command to install the latest version of Node\.js\.

      ```
      nvm install node
      ```

1. Write some JavaScript code to debug\. For example, create a file, add the following code to the file, and save it as `hello.js`\.

   ```
   var i;
   
   i = 10;
   
   console.log("Hello!");
   console.log("i is " + i);
   
   i += 1;
   
   console.log("i is now " + i);
   console.log("Goodbye!");
   ```

1. Add some breakpoints to the code\. For example, in the gutter, choose the margin next to lines 6 and 10\. A red circle is displayed next to each of these line numbers, as follows\.  
![\[Adding breakpoints to code in the Debugger window\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-breakpoints.png)

1. Now you're ready to debug the JavaScript code\. To try this, do the following\.

   1. To show or hide the contents of the **Debugger** window, choose the **Debugger** button, as shown in the next step\.

   1. Watch the value of the variable named `i` while the code is running\. In the **Debugger** window, for **Watch Expressions**, choose **Type an expression here**\. Type the letter `i`, and then press `Enter`, as follows\.  
![\[Debugger window\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-watch-expression.png)

   1. Begin running the code\. Choose **Run**, **Run With**, **Node\.js**, as follows\.  
![\[Debugger window\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-run-with.png)

   1. The code pauses running on line 6\. The **Debugger** window shows the value of `i` in **Watch Expressions**, which is currently `10`\.  
![\[Debugger window\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-breakpoint-hit.png)

   1. In the **Debugger** window, choose **Resume**, which is the blue arrow icon, as follows\.  
![\[Resuming debugging in the Debugger window\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-resume.png)

   1. The code pauses running on line 10\. The **Debugger** window now shows the new value of `i`, which is currently `11`\.

   1. Choose **Resume** again\. The code runs to the end\. The output is printed to the console's **hello\.js** tab, as follows\.  
![\[hello.js tab with debug output\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-debugger-output.png)

Compare your results to the following\.

![\[Using the debugger\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-debugger.gif)

## Final thoughts<a name="tour-ide-cleanup"></a>

**Warning**  
Remember that having an AWS Cloud9 development environment might result in charges to your AWS account\. These include possible charges for Amazon EC2 if you are using an EC2 environment\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/)\.  
There are additional topics in the parent section \(*[Working with the IDE](ide.md)*\) that you might want to explore\. However, when you are finished touring the AWS Cloud9 IDE and no longer need the environment, be sure to delete it and its associated resources, as described in [Deleting an Environment](delete-environment.md)\.