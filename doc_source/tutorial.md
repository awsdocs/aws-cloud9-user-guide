# IDE Tutorial for AWS Cloud9<a name="tutorial"></a>

In this tutorial, you set up an AWS Cloud9 development environment and then tour the AWS Cloud9 integrated development environment \(IDE\)\. Along the way, you use the IDE to code, run, and debug your first app\.

**Note**  
Completing this tutorial might result in charges to your AWS account\. These include possible charges for Amazon EC2\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/)\.
+  [Prerequisites](#tutorial-prereqs) 
+  [Step 1: Create an Environment](#tutorial-create-environment) 
+  [Step 2: Tour the IDE](#tutorial-tour-ide) 
+  [Step 3: Clean Up](#tutorial-clean-up) 
+  [Next Steps](#tutorial-next-steps) 

## Prerequisites<a name="tutorial-prereqs"></a>

To successfully complete this tutorial, you must first complete the steps in [Getting Started](get-started.md)\.

## Step 1: Create an Environment<a name="tutorial-create-environment"></a>

In this step, you use AWS Cloud9 console to create and then open an AWS Cloud9 development environment\.

If you already have an environment, open it, and then skip ahead to [Step 2: Tour the IDE](#tutorial-tour-ide)\.

In AWS Cloud9, a *development environment* \(or just *environment*\) is a place where you store your development project's files and where you run the tools to develop your apps\. In this tutorial, you create a special kind of environment called an *EC2 environment*\. For this kind of environment, AWS Cloud9 creates and manages a new Amazon EC2 instance running Amazon Linux, creates the environment, and then connects the environment to the newly\-created instance\. When you open the environment, AWS Cloud9 displays the AWS Cloud9 IDE that enables you to work with the files and tools in that environment\.

You can create a blank EC2 environment with the [AWS Management Console](#tutorial-create-environment-console) or the [AWS Command Line Interface \(AWS CLI\)](#tutorial-create-environment-cli)\.

**Note**  
When you create an EC2 environment, the environment doesn't contain any sample code by default\. To create an environment along with sample code, see one of the following topics instead\.  
 [Working with Amazon Lightsail Instances](lightsail-instances.md) 
 [Working with AWS CodeStar Projects](codestar-projects.md) 
After you create the environment, skip ahead to [Step 2: Tour the IDE](#tutorial-tour-ide)\.

### Create an EC2 Environment with the Console<a name="tutorial-create-environment-console"></a>

1. Sign in to the AWS Cloud9 console as follows:
   + If you're the only individual using your AWS account or you are an IAM user in a single AWS account, go to [https://console\.aws\.amazon\.com/cloud9/](https://console.aws.amazon.com/cloud9/)\.
   + If your organization uses AWS Single Sign\-On \(SSO\), see your AWS account administrator for sign\-in instructions\.
   + If you're using an AWS Educate Starter Account, see [Step 2: Sign in to the AWS Cloud9 Console](setup-student.md#setup-student-sign-in-ide) in *Individual Student Signup*\.
   + If you're a student in a classroom, see your instructor for sign\-in instructions\.

1. After you sign in to the AWS Cloud9 console, in the top navigation bar, choose an AWS Region to create the environment in\. For a list of available AWS Regions, see [AWS Cloud9](https://docs.aws.amazon.com/general/latest/gr/rande.html#cloud9_region) in the *Amazon Web Services General Reference*\.  
![\[AWS Region selector in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-region.png)

1. If a welcome page is displayed, for **New AWS Cloud9 environment**, choose **Create environment**\. Otherwise, choose **Create environment**\.  
![\[Welcome page in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-welcome-new-env.png)

   Or:  
![\[Create environment button in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-new-env.png)

1. On the **Name environment** page, for **Name**, type a name for your environment\.

   In this tutorial, we use the name `my-demo-environment`\. If you use a different environment name, substitute it throughout this tutorial\.

1. For **Description**, type something about your environment\. For example, `This environment is for the AWS Cloud9 tutorial.` 

1. Choose **Next step**\.

1. On the **Configure settings** page, for **Environment type**, leave the default choice of **Create a new instance for environment \(EC2\)**\.

   Choosing **Create a new instance for enviroment \(EC2\)** means you want AWS Cloud9 to create a new Amazon EC2 instance and then connect the environment to the newly\-created instance\. To use an existing cloud compute instance or your own server instead \(which we call an *SSH environment*\), see [Creating an Environment](create-environment.md)\.
**Note**  
Choosing **Create a new instance for environment \(EC2\)** might result in possible charges to your AWS account for Amazon EC2\.

1. For **Instance type**, leave the default choice\. This choice has relatively low RAM and vCPUs, which is sufficient for this tutorial\.
**Note**  
Choosing instance types with more RAM and vCPUs might result in additional charges to your AWS account for Amazon EC2\.

1. Expand **Network settings \(advanced\)**\.

1. AWS Cloud9 uses Amazon Virtual Private Cloud \(Amazon VPC\) to communicate with the newly\-created Amazon EC2 instance\. Depending on how Amazon VPC is set up, do one of the following\.  
****    
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/tutorial.html)  
****    
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/tutorial.html)

   For more information, see [Amazon VPC Settings](vpc-settings.md)\.

1. For **Cost\-saving setting**, choose the amount of time until AWS Cloud9 shuts down the Amazon EC2 instance for the environment after all web browser instances that are connect to the IDE for the environment have been closed\. Or leave the default choice\.
**Note**  
Choosing a shorter time period might result in fewer charges to your AWS account\. Likewise, choosing a longer time might result in more charges\.

1. Choose **Next step**\.

1. On the **Review choices** page, choose **Create environment**\. Wait while AWS Cloud9 creates your environment\. This can take several minutes\. Please be patient\.

After your environment is created, the AWS Cloud9 IDE is displayed\. You'll learn about the AWS Cloud9 IDE in the next step\.

If AWS Cloud9 doesn't display the IDE after at least five minutes, there might be a problem with your web browser, your AWS access permissions, the instance, or the associated virtual private cloud \(VPC\)\. For possible fixes, see [Cannot Open an Environment](troubleshooting.md#troubleshooting-env-loading) in *Troubleshooting*\.

To learn more about what you can do with an environment after you finish this tutorial, see [Working with Environments](environments.md)\.

Skip ahead to [Step 2: Tour the IDE](#tutorial-tour-ide)\.

### Create an EC2 Environment with the AWS CLI<a name="tutorial-create-environment-cli"></a>

1. Install and configure the AWS CLI, if you have not done so already\. To do this, see the following in the *AWS CLI User Guide*\.
   +  [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/installing.html) 
   +  [Quick Configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-quick-configuration) 

   We recommend you configure the AWS CLI using credentials for one of the following\.
   + The IAM user you created in [Team Setup](setup.md)\.
   + An IAM administrator user in your AWS account, if you will be working regularly with AWS Cloud9 resources for multiple users across the account\. If you cannot configure the AWS CLI as an IAM administrator user, check with your AWS account administrator\. For more information, see [Creating Your First IAM Admin User and Group](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html) in the *IAM User Guide*\.
   + An AWS account root user, but only if you will always be the only one using your own AWS account, and you don't need to share your environments with anyone else\. For more information, see [Creating, Disabling, and Deleting Access Keys for Your AWS Account](https://docs.aws.amazon.com/general/latest/gr/managing-aws-access-keys.html#create-aws-access-key) in the *Amazon Web Services General Reference*\.
   + For other options, see your AWS account administrator or classroom instructor\.

1. Run the AWS Cloud9 `create-environment-ec2` command\.

   ```
   aws cloud9 create-environment-ec2 --name my-demo-environment --description "This environment is for the AWS Cloud9 tutorial." --instance-type t2.micro --region us-east-1 --subnet-id subnet-12a3456b
   ```

   In the preceding command:
   +  `--name` represents the name of the environment\. In this tutorial, we use the name `my-demo-environment`\. If you use a different environment name, substitute it throughout this tutorial\.
   +  `--description` represents an optional description for the environment\.
   +  `--instance-type` represents the type of Amazon EC2 instance AWS Cloud9 will launch and connect to the new environment\. This example specifies `t2.micro`, which has relatively low RAM and vCPUs and is sufficient for this tutorial\. Specifying instance types with more RAM and vCPUs might result in additional charges to your AWS account for Amazon EC2\. For a list of available instance types, see the create environment wizard in the AWS Cloud9 console\.
   +  `--region` represents the ID of the AWS Region for AWS Cloud9 to create the environment in\. For a list of available AWS Regions, see [AWS Cloud9](https://docs.aws.amazon.com/general/latest/gr/rande.html#cloud9_region) in the *Amazon Web Services General Reference*\.
   +  `--subnet-id` represents the subnet you want AWS Cloud9 to use\. Replace `subnet-12a3456b` with the ID of the subnet, which must be compatible with AWS Cloud9\. For more information, see [Amazon VPC Settings](vpc-settings.md)\.
   + By default, AWS Cloud9 shuts down the Amazon EC2 instance for the environment 30 minutes after all web browser instances that are connect to the IDE for the environment have been closed\. To change this, add `--automatic-stop-time-minutes` along with the number of minutes\. A shorter time period might result in fewer charges to your AWS account\. Likewise, a longer time might result in more charges\.
   + By default, the entity that calls this command owns the environment\. To change this, add `--owner-id` along with the Amazon Resource Name \(ARN\) of the owning entity\.

After you successfully run this command, open the AWS Cloud9 IDE for the newly\-created environment\. To do this, see [Opening an Environment](open-environment.md)\. Then return to this topic and continue on with [Step 2: Tour the IDE](#tutorial-tour-ide) to learn how to use the AWS Cloud9 IDE to work with your new environment\.

If you try to open the environment, but AWS Cloud9 doesn't display the IDE after at least five minutes, there might be a problem with your web browser, your AWS access permissions, the instance, or the associated virtual private cloud \(VPC\)\. For possible fixes, see [Cannot Open an Environment](troubleshooting.md#troubleshooting-env-loading) in *Troubleshooting*\.

To learn more about what you can do with an environment after you finish this tutorial, see [Working with Environments](environments.md)\.

## Step 2: Tour the IDE<a name="tutorial-tour-ide"></a>

In the previous step, you created an environment, and the AWS Cloud9 IDE is now displayed\. In this step, you'll learn how to use the IDE\.

The AWS Cloud9 IDE is a collection of tools you use to code, build, run, test, debug, and release software in the cloud\. In this step, you experiment with the most common of these tools\. Toward the end of this tour, you use these tools to code, run, and debug your first app\.
+  [Step 2\.1: Menu Bar](#tutorial-menu-bar) 
+  [Step 2\.2: Dashboard](#tutorial-dashboard) 
+  [Step 2\.3: Environment Window](#tutorial-environment) 
+  [Step 2\.4: Editor, Tabs, and Panes](#tutorial-editor) 
+  [Step 2\.5: Console](#tutorial-console) 
+  [Step 2\.6: Open Files Section](#tutorial-open-files) 
+  [Step 2\.7: Gutter](#tutorial-gutter) 
+  [Step 2\.8: Status Bar](#tutorial-status-bar) 
+  [Step 2\.9: Outline Window](#tutorial-outline) 
+  [Step 2\.10: Go Window](#tutorial-go) 
+  [Step 2\.11: Immediate Tab](#tutorial-immediate) 
+  [Step 2\.12: Process List](#tutorial-process-list) 
+  [Step 2\.13: Preferences](#tutorial-preferences) 
+  [Step 2\.14: Terminal](#tutorial-terminal) 
+  [Step 2\.15: Debugger Window](#tutorial-debugger) 

### Step 2\.1: Menu Bar<a name="tutorial-menu-bar"></a>

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

### Step 2\.2: Dashboard<a name="tutorial-dashboard"></a>

The *dashboard* gives you quick access to each of your environments\. From the dashboard, you can create, open, and change the setting for an environment\.

To open the dashboard, on the menu bar, choose **AWS Cloud9, Go To Your Dashboard**, as follows\.

![\[Opening the AWS Cloud9 dashboard\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-go-dashboard.png)

To view the settings for your environment, choose the title inside of the **my\-demo\-environment** card\.

To return to the IDE for your environment, do one of the following\.
+ Choose your web browser's back button, and then choose **Open IDE** inside of the **my\-demo\-environment** card\.
+ In the navigation breadcrumb, choose **Your environments**, and then choose **Open IDE** inside of the **my\-demo\-environment** card\.

**Note**  
It can take a few moments for the IDE to display again\. Please be patient\.

### Step 2\.3: Environment Window<a name="tutorial-environment"></a>

The **Environment** window shows a list of your folders and files in the environment\. You can also show different types of files, such as hidden files\.

To hide the **Environment** window and the **Environment** button, choose **Window**, **Environment** on the menu bar\.

To show the **Environment** button again, choose **Window**, **Environment** again\.

To show the **Environment** window, choose the **Environment** button\.

![\[The Environment window in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-environment-window.png)

To show hidden files, in the **Environment** window, choose the gear icon, and then choose **Show Hidden Files**, as follows\.

![\[Showing hidden files using the Environment window\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-show-hidden-files.png)

To hide hidden files, choose the gear icon again, and then choose **Show Hidden Files** again\.

### Step 2\.4: Editor, Tabs, and Panes<a name="tutorial-editor"></a>

The *editor* is where you can do things such as write code, run a terminal session, and change IDE settings\. Each instance of an open file, terminal session, and so on is represented by a *tab*\. Tabs can be grouped into *panes*\. Tabs are shown at the edge of their pane, as follows\.

![\[Tabs at the edge of a pane in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-tab-buttons.png)

To hide tabs, choose **View**, **Tab Buttons** on the menu bar\.

To show tabs again, choose **View**, **Tab Buttons** again\.

To open a new tab, choose the **\+** icon at the edge of the row of tabs\. Then choose one of the available commands, for example, **New File**, as follows\.

![\[New tab with commands to choose, such as New File\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-new-file.png)

To display two panes, choose the icon that looks like a drop\-down menu, which is at the edge of the row of tabs\. Then choose **Split Pane in Two Rows**, as follows\.

![\[Showing two panes by splitting one pane into two rows\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-split-pane-two-rows.png)

To return to a single pane, choose the drop\-down menu icon again, and then choose the single square icon, as follows\.

![\[Showing a single pane\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-single-pane-view.png)

### Step 2\.5: Console<a name="tutorial-console"></a>

The *console* is an alternate place for creating and managing tabs, as follows\.

![\[AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-console.png)

You can also change the console's display so that it takes over the entire IDE\.

To hide the console, choose **View**, **Console** on the menu bar\.

To show the console again, choose **View**, **Console** again\.

To expand the console, choose the resize icon, which is at the edge of the console, as follows\.

![\[Expanding the size of the console display\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-console-resize.png)

To shrink the console, choose the resize icon again\.

### Step 2\.6: Open Files Section<a name="tutorial-open-files"></a>

The **Open Files** section shows a list of all files that are currently open in the editor\. **Open Files** is part of the **Environment** window, as follows\.

![\[Open Files section in the Environment window\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-open-files.png)

To open the **Open Files** section, choose **View**, **Open Files** on the menu bar\.

To switch between open files, choose **fish\.txt** and then **cat\.txt** in the **Open Files** section\.

To hide the **Open Files** section, choose **View**, **Open Files** again\.

### Step 2\.7: Gutter<a name="tutorial-gutter"></a>

The *gutter*, at the edge of each file in the editor, shows things like line numbers and contextual symbols as you work with files, as follows\.

![\[Gutter in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-gutter.png)

To hide the gutter, choose **View**, **Gutter** on the menu bar\.

To show the gutter again, choose **View**, **Gutter** again\.

### Step 2\.8: Status Bar<a name="tutorial-status-bar"></a>

The *status bar*, at the edge of each file in the editor, shows things like line and character numbers, file type preference, space and tab settings, and related editor settings, as follows\.

![\[Status bar in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-status-bar.png)

To hide the status bar, choose **View**, **Status Bar** on the menu bar\.

To show the status bar, choose **View**, **Status Bar** again\.

To go to a specific line number, choose a tab such as **cat\.txt** if it's not already selected\. Then in the status bar, choose the line and character number \(it should be something like **7:45**\)\. Type a line number \(like `4`\), and then press `Enter`, as follows\.

![\[Going to specific line numbers using the AWS Cloud9 status bar\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-go-to-line.png)

![\[Going to specific line numbers using the AWS Cloud9 status bar\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-go-to-line.gif)

To change the file type preference, in the status bar, choose a different file type\. For example, for **cat\.txt**, choose **Ruby** to see the syntax colors change\. To go back to plain text colors, choose **Plain Text**, as follows\.

![\[Changing file type preference in the AWS Cloud9 status bar\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-text-color.png)

![\[Changing file type preference in the AWS Cloud9 status bar\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-text-color.gif)

### Step 2\.9: Outline Window<a name="tutorial-outline"></a>

You can use the **Outline** window to quickly go to a specific file location\.

To hide the **Outline** window and **Outline** button, choose **Window**, **Outline** on the menu bar\.

To show the **Outline** button again, choose **Window**, **Outline** again\.

To show the **Outline** window, choose the **Outline** button\.

To see how the **Outline** window works, create a file named `hello.rb`\. Copy the following code into the file\.

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

Then, in the **Outline** window, choose **say\_hello\(i\)**, and then choose **say\_goodbye\(i\)**, as follows\.

![\[Outline window in AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-outline.png)

![\[Outline window in AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-outline.gif)

### Step 2\.10: Go Window<a name="tutorial-go"></a>

You can use the **Go** window to open a file in the editor, go to a symbol's definition, run a command, or go to a line in the active file in the editor\.

To hide the **Go** window and **Go** button \(the magnifying glass icon\), choose **Window**, **Go** on the menu bar\.

To show the **Go** button again, choose **Window**, **Go** again\.

To show the **Go** window, choose the **Go** button \(the magnifying glass\)\.

With the **Go** window showing, you can:
+ Type a forward slash \(`/`\) followed by part or all of a file name\. In the list of matching files that displays, choose a file to open it in the editor\. For example, typing `/fish` lists `fish.txt`, while typing `/.txt` lists both `fish.txt` and `cat.txt`\.
**Note**  
File search is scoped only to non\-hidden files and non\-hidden folders in the **Environment** window\.
+ Type an at symbol \(`@`\) followed by the name of a symbol\. In the list of matching symbols that displays, choose a symbol to go to it in the editor\. For example, with the `hello.rb` file open and active in the editor, type `@hello` to list `say_hello(i)`, or type `@say` to list both `say_hello(i)` and `say_goodbye(i)`\.
**Note**  
If the active file in the editor is part of a supported language project, symbol search is scoped to the current project\. Otherwise, symbol search is scoped only to the active file in the editor\. For more information, see [Working with Language Projects](projects.md)\.
+ Type a dot \(`.`\) followed by the name of a command\. In the list of commands that displays, choose a command to run it\. For example, typing `.closetab` and then pressing `Enter` closes the current tab in the editor\. For a list of available commands, see the [Commands Reference](commands.md)\.
+ Type a colon \(`:`\) followed by a number to go to that line number in the active file in the editor\. For example, with the `hello.rb` file open and active in the editor, type `:11` to go to line 11 in that file\.

![\[Go window in AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-go-window.png)

To see the keybindings for each of these actions based on the current keyboard mode and operating system, see each of the available **Go To** commands on the **Go** menu in the menu bar\.

### Step 2\.11: Immediate Tab<a name="tutorial-immediate"></a>

The **Immediate** tab enables you to test small snippets of JavaScript code\. To see how the **Immediate** tab works, do the following\.

1. Open an **Immediate** tab by choosing **Window**, **New Immediate Window** on the menu bar\.

1. Run some code in the **Immediate** tab\. To try this, type the following code into the window, pressing `Shift-Enter` after typing line 1 and again after line 2\. Press `Enter` after line 3\. \(If you press `Enter` instead of `Shift-Enter` after you type line 1 or line 2, the code will run earlier than you want it to\.\)

   ```
   for (i = 0; i <= 10; i++) { // Press Shift-Enter after typing this line.
     console.log(i)            // Press Shift-Enter after typing this line.
   }                           // Press Enter after typing this line. The numbers 0 to 10 will be printed.
   ```  
![\[Running code in the Immediate tab\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-immediate.png)

### Step 2\.12: Process List<a name="tutorial-process-list"></a>

The **Process List** shows all of the running processes\. You can stop or even forcibly stop processes that you don't want to run anymore\. To see how the **Process List** window works, do the following\.

1. Show the **Process List** by choosing **Tools**, **Process List** on the menu bar\.

1. Find a process\. In the **Process List**, type the name of the process\.

1. Stop or forcibly stop a process\. In the list of processes, choose the process, and then choose **Kill** or **Force Kill**, as follows\.

![\[Process list in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-process-list.png)

### Step 2\.13: Preferences<a name="tutorial-preferences"></a>

 *Preferences* include the following settings\.
+ Settings for the current environment only, such as whether to use soft tabs in the editor, the file types to ignore, and code completion behaviors for languages such as PHP and Python\.
+ Your user settings across each of your environments, such as colors, fonts, and editor behaviors\.
+ Your keybindings, such as which shortcut key combinations you prefer to use to work with files and the editor\.
+ The IDE's overall theme\.

To show preferences, choose **AWS Cloud9**, **Preferences** on the menu bar\. The following is displayed\.

![\[Showing preferences in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-preferences.png)

### Step 2\.14: Terminal<a name="tutorial-terminal"></a>

You can run one or more *terminal* sessions in the IDE\. To start a terminal session, choose **Window**, **New Terminal** on the menu bar\.

You can try running a command in the terminal\. For example, in the terminal, type `echo $PATH` \(to print the value of the `PATH` environment variable\), and then press `Enter`\.

You can also try running additional commands\. For example, try commands such as the following\.
+  ** `pwd` ** to print the path to the current directory\.
+  ** `aws --version` ** to print version information about the AWS CLI\.
+  ** `ls -l` ** to print information about the current directory\.

![\[Using the terminal in the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-terminal.gif)

### Step 2\.15: Debugger Window<a name="tutorial-debugger"></a>

You can use the **Debugger** window to debug your code\. For example, you can step through running code a portion at a time, watch the values of variables over time, and explore the call stack\.

To hide the **Debugger** window and **Debugger** button, choose **Window**, **Debugger** on the menu bar\.

To show the **Debugger** button again, choose **Window**, **Debugger** again\.

To show the **Debugger** window, choose the **Debugger** button\.

You can experiment with using the **Debugger** window and some JavaScript code\. To try this, do the following\.

1. Prepare to use the **Debugger** window to debug JavaScript code by installing Node\.js into your environment, if it isn't already installed\. To confirm whether your environment has Node\.js installed, run the ** `node --version` ** command\. If Node\.js is installed, the Node\.js version number is output, and you can skip ahead to step 3 in this procedure to write some JavaScript code\.

1. To install Node\.js, do the following\.

   1. Run the following two commands, one at a time, to be sure your environment has the latest updates, and then download Node Version Manager \(nvm\)\. \(nvm is a simple Bash shell script that is useful for installing and managing Node\.js versions\. For more information, see [Node Version Manager](https://github.com/creationix/nvm/blob/master/README.md) on GitHub\.\)

      ```
      sudo yum -y update
      curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash
      ```

   1. Use a text editor to update your `~/.bashrc` file to enable nvm to load\. For example, in the **Environment** window of the IDE, choose the gear icon, and then choose **Show Home in Favorites**\. Repeat this step and choose **Show Hidden Files** as well\.

   1. Open the `~/.bashrc` file\.

   1. Type or paste the following code at the end of the file to enable nvm to load\.

      ```
      export NVM_DIR="/home/ec2-user/.nvm"
      [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm.
      ```

   1. Save the file\.

   1. Start a new terminal session, and then run this command to install the latest version of Node\.js\.

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

   1. Show the **Debugger** window, if it's not already displayed\.

   1. Watch the value of the variable named `i` while the code is running\. In the **Debugger** window, for **Watch Expressions**, choose **Type an expression here**\. Type the letter `i`, and then press `Enter`, as follows\.  
![\[Debugger window\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-watch-expression.png)

   1. Begin running the code\. Choose **Run**, **Run With**, **Node\.js**, as follows\.  
![\[Debugger window\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-run-with.png)

   1. The code pauses running on line 6\. The **Debugger** window shows the value of `i` in **Watch Expressions**, which is currently `10`, as follows\.  
![\[Debugger window\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-breakpoint-hit.png)

   1. In the **Debugger** window, choose **Resume**, which is the blue arrow icon, as follows\.  
![\[Resuming debugging in the Debugger window\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-resume.png)

   1. The code pauses running on line 10\. The **Debugger** window now shows the new value of `i`, which is currently `11`\.

   1. Choose **Resume** again\. The code runs to the end\. The output is printed to the console's **hello\.js** tab, as follows\.  
![\[hello.js tab with debug output\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-debugger-output.png)

Compare your results to the following\.

![\[Using the debugger\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/ide-debugger.gif)

## Step 3: Clean Up<a name="tutorial-clean-up"></a>

To prevent ongoing charges to your AWS account related to this tutorial, you should delete the environment\.

**Warning**  
Deleting an environment cannot be undone\.

You can delete the environment with the [AWS Cloud9 console](#tutorial-clean-up-console) or the [AWS CLI](#tutorial-clean-up-cli)\.

### Delete the Environment with the AWS Cloud9 Console<a name="tutorial-clean-up-console"></a>

1. Open the dashboard\. To do this, on the menu bar in the IDE, choose **AWS Cloud9**, **Go To Your Dashboard**\.

1. Do one of the following\.
   + Choose the title inside of the **my\-demo\-environment** card, and then choose **Delete**\.  
![\[Deleting an environment in the environment details page\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-delete-env.png)
   + Select the **my\-demo\-environment** card, and then choose **Delete**\.  
![\[Deleting an environment in the environments list\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-delete-env-card.png)

1. In the **Delete** dialog box, type `Delete`, and then choose **Delete**\.

**Note**  
If the environment was an EC2 environment, AWS Cloud9 also terminates the Amazon EC2 instance that was connected to that environment\.  
However, if the environment was an SSH environment, and that environment was connected to an Amazon EC2 instance, AWS Cloud9 doesn't terminate that instance\. If you don't terminate that instance later, your AWS account might continue to have ongoing charges for Amazon EC2 related to that instance\.

Skip ahead to [Next Steps](#tutorial-next-steps)\.

### Delete the Environment with the AWS CLI<a name="tutorial-clean-up-cli"></a>

Run the AWS Cloud9 `delete-environment` command, specifying the ID of the environment to delete\.

```
aws cloud9 delete-environment --environment-id 12a34567b8cd9012345ef67abcd890e1
```

In the preceding command, replace `12a34567b8cd9012345ef67abcd890e1` with the ID of the environment to delete\.

## Next Steps<a name="tutorial-next-steps"></a>

Explore any or all of the following topics to continue getting familiar with AWS Cloud9\.


****  

|  |  | 
| --- |--- |
|  Learn more about the AWS Cloud9 IDE\.  |   [Working with the IDE](ide.md)   | 
|  Invite others to use your new environment along with you, in real time and with text chat support\.  |   [Working with Shared Environments](share-environment.md)   | 
|  Create SSH environments \(environments that use cloud compute instances or servers that you create, instead of an Amazon EC2 instances that AWS Cloud9 creates for you\)\.  |   [Creating an Environment](create-environment.md) and [SSH Environment Host Requirements](ssh-settings.md)   | 
|  Use AWS Cloud9 with Lambda\.  |   [AWS Lambda Tutorial](tutorial-lambda.md), [Advanced AWS Lambda Tutorial](tutorial-lambda-advanced.md), and [Working with AWS Lambda Functions](lambda-functions.md)   | 
|  Use AWS Cloud9 with Amazon Lightsail\.  |   [Working with Amazon Lightsail Instances](lightsail-instances.md)   | 
|  Use AWS Cloud9 with AWS CodeStar\.  |   [Working with AWS CodeStar Projects](codestar-projects.md)   | 
|  Use AWS Cloud9 with AWS CodePipeline\.  |   [Working with AWS CodePipeline](codepipeline-repos.md)   | 
|  Use AWS Cloud9 with the AWS CLI, the aws\-shell, AWS CodeCommit, the AWS Cloud Development Kit \(AWS CDK\), GitHub, or Amazon DynamoDB, as well as Node\.js, Python, or other programming languages\.  |   [Samples](samples.md)   | 
|  Work with code for intelligent robotics applications in AWS RoboMaker\.  |   [Developing with AWS Cloud9](https://docs.aws.amazon.com/robomaker/latest/dg/cloud9.html) in the *AWS RoboMaker Developer Guide*   | 

To get help with AWS Cloud9 from the community, see the [AWS Cloud9 Discussion Forum](https://forums.aws.amazon.com/forum.jspa?forumID=268)\. \(When you enter this forum, AWS might require you to sign in\.\)

To get help with AWS Cloud9 directly from AWS, see the support options on the [AWS Support](https://aws.amazon.com/premiumsupport) page\.