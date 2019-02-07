# Working with Keybindings in the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="settings-keybindings"></a>

 *Keybindings* define your shortcut key combinations\. Keybindings apply across each AWS Cloud9 development environment associated with your IAM user\. As you make changes to your keybindings, AWS Cloud9 pushes those changes to the cloud, and associates them with your IAM user\. AWS Cloud9 also continually scans the cloud for changes to keybindings associated with your IAM user, and applies those changes to your current environment\.

You can share your keybindings with other users\.
+  [View or Change Your Keybindings](#settings-keybindings-view) 
+  [Share Your Keybindings with Another User](#settings-keybindings-share) 
+  [Change Your Keyboard Mode](#settings-keybindings-mode) 
+  [Change Your Operating System Keybindings](#settings-keybindings-os) 
+  [Change Specific Keybindings](#settings-keybindings-change) 
+  [Remove All of Your Custom Keybindings](#settings-keybindings-reset) 

## View or Change Your Keybindings<a name="settings-keybindings-view"></a>

1. On the menu bar, choose **AWS Cloud9**, **Preferences**\.

1. To view your keybindings across each environment of yours, on the **Preferences** tab, in the side navigation pane, choose **Keybindings**\.

1. To change your keybindings across each environment of yours, in the **Keybindings** pane, change the settings you want\.

1. To apply your changes to any environment, simply open that environment\. If that environment is already open, refresh the web browser tab for that environment\.

For more information, see the following:
+  [MacOS Default Keybindings Reference](keybindings-default-apple-osx.md) 
+  [MacOS Vim Keybindings Reference](keybindings-vim-apple-osx.md) 
+  [MacOS Emacs Keybindings Reference](keybindings-emacs-apple-osx.md) 
+  [MacOS Sublime Keybindings Reference](keybindings-sublime-apple-osx.md) 
+  [Windows / Linux Default Keybindings Reference](keybindings-default-windows-linux.md) 
+  [Windows / Linux Vim Keybindings Reference](keybindings-vim-windows-linux.md) 
+  [Windows / Linux Emacs Keybindings Reference](keybindings-emacs-windows-linux.md) 
+  [Windows / Linux Sublime Keybindings Reference](keybindings-sublime-windows-linux.md) 

## Share Your Keybindings with Another User<a name="settings-keybindings-share"></a>

1. In both the source and target environment, on the menu bar of the AWS Cloud9 IDE, choose **AWS Cloud9, Open Your Keymap**\.

1. In the source environment, copy the contents of the **keybindings\.settings** tab that is displayed\.

1. In the target environment, overwrite the contents of the **keybindings\.settings** tab with the copied contents from the source environment\.

1. In the target environment, save the **keybindings\.settings** tab\.

## Change Your Keyboard Mode<a name="settings-keybindings-mode"></a>

You can change the keyboard mode that the AWS Cloud9 IDE uses for interacting with text in the editor across each environment associated with your IAM user\.

1. On the menu bar, choose **AWS Cloud9**, **Preferences**\.

1. On the **Preferences** tab, in the side navigation pane, choose **Keybindings**\.

1. For **Keyboard Mode**, choose one of these keyboard modes:
   +  **Default** to use a set of default keybindings\.
   +  **Vim** to use Vim mode\. For more information, see the [Vim help files](https://vimhelp.appspot.com/) website\.
   +  **Emacs** to use Emacs mode\. For more information, see [The Emacs Editor](https://www.gnu.org/software/emacs/manual/html_node/emacs/index.html) on the GNU Operating System website\.
   +  **Sublime** to use Sublime mode\. For more information, see the [Sublime Text Documentation](https://www.sublimetext.com/docs/3/) website\.

## Change Your Operating System Keybindings<a name="settings-keybindings-os"></a>

You can change the set of operating system keybindings the AWS Cloud9 IDE recognizes across each environment associated with your IAM user\.

1. On the menu bar, choose **AWS Cloud9**, **Preferences**\.

1. On the **Preferences** tab, in the side navigation pane, choose **Keybindings**\.

1. For **Operating System**, choose one of these operating systems:
   +  **Auto** for the AWS Cloud9 IDE to attempt to detect which set of operating system keybindings to use\.
   +  **MacOS** for the AWS Cloud9 IDE to use the keybindings listed in Mac format\.
   +  **Windows / Linux** for the AWS Cloud9 IDE to use the keybindings listed in Windows and Linux formats\.

## Change Specific Keybindings<a name="settings-keybindings-change"></a>

You can change individual keybindings across each environment associated with your IAM user\.

**To change one keybinding at a time**

1. On the menu bar, choose **AWS Cloud9**, **Preferences**\.

1. On the **Preferences** tab, in the side navigation pane, choose **Keybindings**\.

1. In the list of keybindings, double\-click the keybinding in the **Keystroke** column you want to change\.

1. Use the keyboard to specify the replacement key combination, and then press `Enter`\.
**Note**  
To completely remove the current key combination, press `Backspace` for Windows or Linux, or `Delete` for Mac\.

**To change multiple keybindings at once**

1. On the menu bar, choose **AWS Cloud9**, **Open Your Keymap**\.

1. In the `keybindings.settings` file, define each keybinding to be changed, for example:

   ```
   [
     {
       "command": "addfavorite",
       "keys": {
         "win": ["Ctrl-Alt-F"],
         "mac": ["Ctrl-Option-F"]
       }
     },
     {
       "command": "copyFilePath",
       "keys": {
         "win": ["Ctrl-Shift-F"],
         "mac": ["Alt-Shift-F"]
       }
     }
   ]
   ```

   In the example, `addFavorite` and `copyFilePath` are the names of keybindings in the **Keystroke** column in the **Keybindings** pane on the **Preferences** tab\. The keybindings you want are `win` and `mac` for Windows or Linux and Mac, respectively\.

   To apply your changes, save the `keybindings.settings` file\. Your changes should appear in the **Keybindings** pane after a short delay\.

## Remove All of Your Custom Keybindings<a name="settings-keybindings-reset"></a>

You can remove all custom keybindings and restore all keybindings to their default values, across each environment associated with your IAM user\.

**Warning**  
You cannot undo this action\.

1. On the menu bar, choose **AWS Cloud9**, **Preferences**\.

1. On the **Preferences** tab, in the side navigation pane, choose **Keybindings**\.

1. Choose **Reset to Defaults**\.