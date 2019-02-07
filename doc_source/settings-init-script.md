# Working with Initialization Scripts in the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="settings-init-script"></a>


****  

|  | 
| --- |
|   Adding code to an initialization script in the IDE is currently an experimental feature and is not fully supported\. If you add code to an initialization script, you do so at your own risk\. AWS Cloud9 reserves the right to change this functionality at any time\.   | 

An *initialization script* defines custom initialization code to run in your IDE after all plugins are loaded\. This applies across each AWS Cloud9 development environment associated with your IAM user\. As you make changes to your initialization script, AWS Cloud9 pushes those changes to the cloud and associates them with your IAM user\. AWS Cloud9 also continually scans the cloud for changes to the initialization script associated with your IAM user, and applies those changes to your current environment\.

You can share your initialization script with other users\.
+  [View or Change Your Initialization Script](#settings-init-script-view) 
+  [Share Your Initialization Script with Another User](#settings-init-script-share) 

## View or Change Your Initialization Script<a name="settings-init-script-view"></a>

1. To view your initialization script, on the menu bar, choose **AWS Cloud9**, **Open Your Init Script**\.

1. To change your initialization script, on the **init\.js** tab, use code to change your initialization script's behavior\.

1. To apply your changes to any other environment, simply open the environment you want to apply the changes to\. If that environment is already open, refresh the web browser tab for that environment\.

## Share Your Initialization Script with Another User<a name="settings-init-script-share"></a>

1. In both the source and target environment, on the menu bar of the AWS Cloud9 IDE, choose **AWS Cloud9, Open Your Init Script**\.

1. In the source environment, copy the contents of the **init\.js** tab that is displayed\.

1. In the target environment, overwrite the contents of the **init\.js** tab with the copied contents from the source environment\.

1. In the target environment, save the **init\.js** tab\.