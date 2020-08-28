# Managing initialization scripts in the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="settings-init-script"></a>

**Important**  
AWS Cloud9 no longer supports the experimental feature that allowed users to customize an initialization script that was automatically run in the IDE\. Users can continue to view, edit, and save the `init.js` file using the editor, but customized initialization scripts are no longer permitted to run and can't modify the IDE's behavior\.  
 If AWS Cloud9 detects that the `init.js` file has been modified, the following message is displayed in the IDE:  
Support for initialization scripts has been discontinued\. The contents of this init\.js file will no longer be executed on loading the AWS Cloud9 IDE\.  
If you need to run a custom initialization script for the IDE, please [contact us](https://aws.amazon.com/contact-us/) directly\. 

An *initialization script* defines initialization code to run in your IDE after all plugins are loaded\. This applies across each AWS Cloud9 development environment associated with your IAM user\. AWS Cloud9 also continually scans for changes to the initialization script and alerts users if a modification occurred\.

## Open your initialization script<a name="settings-init-script-view"></a>

To open your initialization script, on the menu bar, choose **AWS Cloud9**, **Open Your Init Script**\.

**Important**  
You can edit and save the `init.js` file using the editor, but your customized script will not be permitted to run in the IDE\. 