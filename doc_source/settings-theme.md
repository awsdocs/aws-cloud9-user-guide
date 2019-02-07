# Working with Themes in the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="settings-theme"></a>

A *theme* defines your overall IDE colors\. This applies across each AWS Cloud9 development environment associated with your IAM user\. As you make changes to your theme, AWS Cloud9 pushes those changes to the cloud, and associates them with your IAM user\. AWS Cloud9 also continually scans the cloud for changes to the theme associated with your IAM user, and applies those changes to your current environment\.

You can share any custom theme overrides you define with other users\.
+  [View or Change Your Theme](#settings-theme-view) 
+  [Overall Theme Settings You Can Change](#settings-theme-change) 
+  [Theme Overrides You Can Define with Code](#settings-theme-code) 
+  [Share Your Theme Overrides with Another User](#settings-theme-share) 

## View or Change Your Theme<a name="settings-theme-view"></a>

1. On the menu bar, choose **AWS Cloud9**, **Preferences**\.

1. To view your theme across each environment of yours, on the **Preferences** tab, in the side navigation pane, choose **Themes**\.

1. To change your theme across each environment of yours, in the **Themes** pane, change the settings you want\. To change portions of your theme by using code, choose the **your stylesheet** link\.

1. To apply your changes to any environment of yours, simply open that environment\. If that environment is already open, refresh the web browser tab for that environment\.

## Overall Theme Settings You Can Change<a name="settings-theme-change"></a>

You can change the following kinds of overall theme settings on the **Preferences** tab in the **Themes** pane\.

** **Flat Theme** **  
Applies the built\-in flat theme across the AWS Cloud9 IDE\.

** **Classic Theme** **  
Applies the selected built\-in classic theme across the AWS Cloud9 IDE\.

** **Syntax Theme** **  
Applies the selected theme to code files across the AWS Cloud9 IDE\.

## Theme Overrides You Can Define with Code<a name="settings-theme-code"></a>

You can override portions of the overall theme in the AWS Cloud9 IDE\. These overrides will persist even if you change the overall theme itself in the AWS Cloud9 IDE\.

For example, let's say you want to change the background color of the titles on open tabs to yellow, regardless of the related setting for the current overall theme that is currently applied to the AWS Cloud9 IDE\.

First, use your web browser's developer tools to determine the CSS class for the portion of the theme you want to change\. For example, do the following for Google Chrome\.

1. Choose **Customize and control Google Chrome**, **More tools**, **Developer tools**\.

1. In the **Developer tools** pane, choose **Select an element in the page to inspect it**\.

1. Pause your mouse over the portion of the IDE you want to change\. In this example, pause your mouse over the title of an open tab\.

1. Note the CSS class name\. In this example, the CSS class name for the title of an open tab is `sessiontab_title`\.

Next, add a corresponding CSS class selector to your `styles.css` file\.

1. On the menu bar, choose **AWS Cloud9**, **Preferences**\. In the side navigation pane, choose **Themes**\. Then choose the **your stylesheet** link\.

1. In the `styles.css` file, add the CSS class selector\. In this example, you use the `.sessiontab_title` selector to set `background-color` to `yellow`\.

   ```
   .sessiontab_title {
     background-color: yellow;
   }
   ```

Finally, save the `styles.css` file, and note the change to the theme\. In this example, the background color of the titles of open tabs changes to yellow\. Even if you change the overall theme in the AWS Cloud9 IDE, the CSS overrides in your `styles.css` file persist\.

**Note**  
To revert this theme override, remove the preceding code from the `styles.css` file, and then save the file again\.

## Share Your Theme Overrides with Another User<a name="settings-theme-share"></a>

1. In both the source and target environment, on the menu bar of the AWS Cloud9 IDE, choose **AWS Cloud9, Open Your Stylesheet**\.

1. In the source environment, copy the contents of the **styles\.css** tab that is displayed\.

1. In the target environment, overwrite the contents of the **styles\.css** tab with the copied contents from the source environment\.

1. In the target environment, save the **styles\.css** tab\.