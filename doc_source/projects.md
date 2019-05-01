# Working with Language Projects in the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="projects"></a>

The AWS Cloud9 IDE provides project productivity features for some languages in addition to those languages listed in [Language Support in the AWS Cloud9 Integrated Development Environment \(IDE\)](language-support.md)\. To use these features, you use the IDE to create or identify a *language project* \(or *project*\) based on that language\. A project is a collection of related files, folders, and settings in the IDE for an AWS Cloud9 development environment\.

To use the IDE to create a language project in your environment, see [Create a Language Project](#projects-create)\.

## Available Project Productivity Features<a name="projects-features"></a>

The AWS Cloud9 IDE provides the following project productivity features by programming language\.


****  

|  **Language**  |  [Autocomplete](#projects-features-autocomplete)  |  [Gutter Icons](#projects-features-gutter-icons)  |  [Quick Fixes](#projects-features-quick-fixes)  |  [Find References](#projects-features-find-refs)  |  [Go to Definition](#projects-features-go-to-def)  |  [Go to Symbol](#projects-features-go-to-symbol)  | 
| --- | --- | --- | --- | --- | --- | --- | 
|  TypeScript  |  X  |  X  |  X  |  X  |  X  |  X  | 

### Autocomplete<a name="projects-features-autocomplete"></a>

As you type in a file in the editor, a list of symbols is displayed at the insertion point for that context, if any symbols are available there\.

To insert a symbol from the list at the insertion point, if the symbol isn't already chosen, choose it by using your up arrow or down arrow key, and then press `Tab`\.

Before you press `Tab`, you might see a screentip that contains information about the symbol you chose, if information is available\.

To close the list without inserting a symbol, press `Esc`\.

### Gutter Icons<a name="projects-features-gutter-icons"></a>

Icons might appear in the gutter for the active file\. These icons highlight possible issues such as warnings and errors in code before you run it\.

For more information about an issue, pause your mouse pointer on the issue's icon\.

### Quick Fixes<a name="projects-features-quick-fixes"></a>

In the active file in the editor, you can display information about coding errors and warnings, with possible fixes that you can automatically apply to that code\. To display error or warning information and possible fixes, choose any part of the code that has a red dotted underline \(for errors\), or a gray dotted underline \(for warnings\)\. Or, with the cursor resting on code that has a red or gray dotted underline, press `Option-Enter` \(for macOS\), or `Alt-Enter` \(for Linux or Windows\)\. To apply a proposed fix, choose the fix in the list, or use the arrow keys to select the fix and then press `Enter`\. To turn choosing quick fixes with mouse clicks on or off, choose **AWS Cloud9**, **Preferences**, **User Settings**, **Language**, **Hints & Warnings**, **Show Available Quick Fixes on Click**\.

### Find References<a name="projects-features-find-refs"></a>

In the active file in the editor, you can display all references to the symbol at the insertion point, if the IDE has access to those references\.

To do this, at the insertion point anywhere within the symbol, run the ** `Find References` ** command\. For example:
+ Right\-click at the insertion point, and then choose **Find References**\.
+ On the menu bar, choose **Go, Find References**\.
+ Press `Shift-F3` by default for macOS, Windows, or Linux\.

If references are available, a pane opens on top of the active file, next to that symbol\. The pane contains a list of the files where the symbol is referenced\. The pane displays the first reference in the list\. To display a different reference, choose that reference in the list\.

To close the pane, choose the close \(**X**\) icon in the pane, or press `Esc`\.

The ** `Find References` ** command might be disabled, or might not work as expected, under the following conditions:
+ There are no references to that symbol in the active file's project\.
+ The IDE can't find some or all of that symbol's references in the active file's project\.
+ The IDE doesn't have access to one or more locations where that symbol is referenced in the active file's project\.

### Go to Definition<a name="projects-features-go-to-def"></a>

In the active file in the editor, you can go from a symbol to where that symbol is defined, if the IDE has access to that definition\.

To do this, at the insertion point anywhere within the symbol, run the ** `Jump to Definition` ** command\. For example:
+ Right\-click at the insertion point, and then choose **Jump to Definition**\.
+ On the menu bar, choose **Go, Jump to Definition**\.
+ Press `F3` by default for macOS, Windows, or Linux\.

If the definition is available, the insertion point switches to that definition, even if that definition is in a separate file\.

The ** `Jump to Definition` ** command might be disabled, or might not work as expected, under the following conditions:
+ The symbol is a primitive symbol for that language\.
+ The IDE can't find the definition's location in the active file's project\.
+ The IDE doesn't have access to the definition's location in the active file's project\.

### Go to Symbol<a name="projects-features-go-to-symbol"></a>

You can go to a specific symbol within a project, as follows\.

1. Make one of the files in the project active by opening it in the editor\. If the file is already open, choose its tab in the editor to make that file the active one\.

1. Run the ** `Go to Symbol` ** command\. For example:
   + Choose the **Go** window button \(magnifying glass icon\)\. In the **Go to Anything** box, type `@`, and then start typing the symbol\.
   + On the menu bar, choose **Go, Go To Symbol**\. In the **Go** window, start typing the symbol after **@**\.
   + Press `Command-2` or `Command-Shift-O` by default for macOS, or `Ctrl-Shift-O` by default for Windows or Linux\. In the **Go** window, start typing the symbol after **@**\.

   For example, to find all symbols in the project named `toString`, start typing `@toString` \(or start typing `toString` after **@**, if **@** is already displayed\)\.

1. If you see the symbol you want in the **Symbols** list, choose it by clicking it\. Or use your up arrow or down arrow key to select it, and then press `Enter`\. The insertion point then switches to that symbol\.

If the symbol that you want to go to isn't in the active file's project, this procedure might not work as expected\.

## Create a Language Project<a name="projects-create"></a>

Use the following procedure to create a language project that will work with supported project productivity features in the AWS Cloud9 IDE\.

**Note**  
We recommend that you use supported project productivity features on files that are part of a language project\. Although you can use some supported project productivity features on a file that isn't part of a project, those features might behave with unexpected results\.  
For example, you might use the IDE to search for references and definitions from within a file at the root level of an environment that isn't part of a project\. The IDE might then search only across files at that same root level\. This might result in no references or definitions found, even though those references or definitions actually exist in language projects elsewhere across the same environment\.

### Create a TypeScript Language Project<a name="projects-create-typescript"></a>

1. Ensure you have TypeScript installed in the environment\. For more information, see [Step 1: Install Required Tools](sample-typescript.md#sample-typescript-install) in the [TypeScript Sample for AWS Cloud9](sample-typescript.md)\.

1. From a terminal session in the IDE for the environment, switch to the directory where you want to create the project\. If the directory doesn't exist, create it and then switch to it\. For example, the following commands create a directory named `my-demo-project` at the root of the environment \(in `~/environment`\), and then switch to that directory\.

   ```
   mkdir ~/environment/my-demo-project
   cd ~/environment/my-demo-project
   ```

1. At the root of the directory where you want to create the project, run the TypeScript compiler with the ** `--init` ** option\.

   ```
   tsc --init
   ```

   If this command is successful, the TypeScript compiler creates a `tsconfig.json` file in the root of the directory for the project\. You can use this file to define various project settings, such as TypeScript compiler options and specific files to include or exclude from the project\.

   For more information about the `tsconfig.json` file, see the following:
   +  [tsconfig\.json Overview](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html) on the TypeScript website\.
   +  [tsconfig\.json Schema](http://json.schemastore.org/tsconfig) on the json\.schemastore\.org website\.