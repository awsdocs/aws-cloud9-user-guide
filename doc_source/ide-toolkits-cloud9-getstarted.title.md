# Getting started<a name="ide-toolkits-cloud9-getstarted.title"></a>

The topics contained in this section discuss creating a CodeCatalyst Dev Environment and accessing it using the AWS Cloud9 IDE\. For more information about a Dev Environment, see [Dev Environment](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment.html) in the *Amazon CodeCatalyst Guide*\.

AWS Toolkits are IDE\-specific software development kits \(SDKs\) that provide quick access to AWS Cloud accounts, services, and resources\. From your CodeCatalyst account you can view, edit, and manage your CodeCatalyst Dev Environments in a convenient interface, without the need to leave your IDE\. To learn more about the AWS Cloud services and features that are available through AWS Toolkits, see the [What is the AWS Toolkit for Visual Studio Code?](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html), [AWS Toolkit for AWS Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/toolkit-welcome.html), and [What is the AWS Toolkit for JetBrains](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html) guides\.

## Prerequisites<a name="ide-toolkits-cloud9-getstarted-prereq"></a>

To use CodeCatalyst with the AWS Cloud9 IDE, you must have an existing Dev Environment that you created within the CodeCatalyst console\. 

**Note**  
It is not currently possible to create a subfolder named **projects** within a folder of the same name within the File System of the AWS Cloud9 IDE forCodeCatalyst\. You will not be able to access any files within this directory\. Please use an alternative folder name\. This issue only affects the file path **/projects/projects**, file paths such as **/test/projects **and **/projects/test/projects **should work\. This is a known issue and only affects the AWS Cloud9 IDE File Explorer\.