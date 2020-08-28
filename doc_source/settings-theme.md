# Working with themes in the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="settings-theme"></a>

A *theme* defines your overall IDE colors\. This applies across each AWS Cloud9 development environment associated with your IAM user\. As you make changes to your theme, AWS Cloud9 pushes those changes to the cloud, and associates them with your IAM user\. AWS Cloud9 also continually scans the cloud for changes to the theme associated with your IAM user, and applies those changes to your current environment\.
+  [View or change your theme](#settings-theme-view) 
+  [Overall theme settings you can change](#settings-theme-change) 
+  [Theme overrides](#settings-theme-code) 

## View or change your theme<a name="settings-theme-view"></a>

1. On the menu bar, choose **AWS Cloud9**, **Preferences**\.

1. To view your theme across each environment of yours, on the **Preferences** tab, in the side navigation pane, choose **Themes**\.

1. To change your theme across each environment of yours, in the **Themes** pane, change the settings you want\. To change portions of your theme by using code, choose the **your stylesheet** link\.

1. To apply your changes to any environment of yours, simply open that environment\. If that environment is already open, refresh the web browser tab for that environment\.

## Overall theme settings you can change<a name="settings-theme-change"></a>

You can change the following kinds of overall theme settings on the **Preferences** tab in the **Themes** pane\.

** **Flat Theme** **  
Applies the built\-in flat theme across the AWS Cloud9 IDE\.

** **Classic Theme** **  
Applies the selected built\-in classic theme across the AWS Cloud9 IDE\.

** **Syntax Theme** **  
Applies the selected theme to code files across the AWS Cloud9 IDE\.

## Theme overrides<a name="settings-theme-code"></a>

**Important**  
AWS Cloud9 no longer supports the feature that allowed users to override IDE themes by updating the `styles.css` file\. Users can continue to view, edit, and save the `styles.css` file using the editor, but no theme overrides are applied when the AWS Cloud9 IDE loads\.   
 If AWS Cloud9 detects that the `styles.css` file has been modified, the following message is displayed in the IDE:  
Support for theme overrides has been discontinued\. The contents of this styles\.css file will no longer be applied on loading the AWS Cloud9 IDE\.  
If you need to use style sheets to define themes for the IDE, please [contact us](https://aws.amazon.com/contact-us/) directly\. 