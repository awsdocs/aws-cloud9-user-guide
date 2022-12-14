# Editing the repository devfile for a Dev Environment<a name="ide-toolkits-edit-devfile-cloud9"></a>

To change the configuration of a Dev Environment, edit the devfile\. A devfile is an open standard that allows your to standardize development Dev Environments using a YAML file in which your codify the required development tools\. Devfiles enable you to standardize your development Dev Environment across your team\. You can edit the devfile from the root of the source repository in CodeCatalyst\. Alternatively, you can edit the devfile in a supported IDE\. If you edit the devfile in a supported IDE, commit and push your changes to the source repository or create a pull request\. That way, a team member can review and approve the devfile edits\. 

**Note**  
You can only include public container images in your devfile\.

**Note**  
Certain AWS Cloud9 IDE features might not work in custom devfiles if dependencies are missing\. It might require additional effort to make them work on certain platforms other than Linux x64\. <a name="ide-toolkits-edit-devfile-cloud9-steps"></a>

**To edit the repository devfile for a Dev Environment in AWS Cloud9**

1. From the CodeCatalyst console, navigate to your Dev Environment through the AWS Cloud9 IDE\.

1. Choose **aws\-explorer** from the AWS Cloud9 sidebar\.

1. From the **Developer Tools** navigation pane, choose the **CodeCatalyst toolkit** menu\.

1. Choose **Open Devfile**\.

1. Edit the devfile, and save the file\.

1. Choose **Source Control**, which is the git extension from the menu side\-bar\.

1. In the **Message** text field, enter a message before staging changes\.

1. To prepare for a commit, choose the **Stage All Changes \(\+\)** icon\.

1. To view Git commands, choose the **menu** icon that's next to the repository name\.

1. Choose **Commit** and **Push**\.

1. Choose **Update Dev Environment** from the AWS Toolkit menu\.

**Note**  
If the Dev Environment you want to launch using a custom devfile does not work, it may be because the devfile is not compatible with AWS Cloud9\. Please review the devfile, and if the issue persists, delete it and try creating a new one\.

You can also edit the devfile for a Dev Environment through CodeCatalyst\. For more information, see [Configuring your Dev Environment](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment-devfile.html) in the *Amazon CodeCatalyst guide*\.