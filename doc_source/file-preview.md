# Previewing Files in the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="file-preview"></a>

You can use the AWS Cloud9 IDE to preview the files in a AWS Cloud9 development environment from within the IDE\.
+  [Open a File for Preview](#file-preview-file-open) 
+  [Reload a File Preview](#file-preview-file-reload) 
+  [Change the File Preview Type](#file-preview-file-preview-type) 
+  [Open a File Preview in a Separate Web Browser Tab](#file-preview-file-open-tab) 
+  [Switch to a Different File Preview](#file-preview-file-switch) 

## Open a File for Preview<a name="file-preview-file-open"></a>

Do one of the following in the AWS Cloud9 IDE to open a file preview tab within the environment:
+ In the **Environment** window, right\-click the file you want to preview, and then choose **Preview**\.
**Note**  
Although you can use this approach to preview any file, preview works best with files that have the following file extensions:  
 `.htm` 
 `.html` 
 `.pdf` 
 `.svg` 
 `.xhtml` 
Any file containing content in Markdown format\.
+ Open a file with one of the following file extensions:
  +  `.pdf` 
  +  `.svg` 
+ With the file you want to preview already open and active, on the menu bar, choose **Preview, Preview File FILE\_NAME**\. Or choose **Tools, Preview, Preview File FILE\_NAME**, where **FILE\_NAME** is the name of the file you want to preview\.
**Note**  
These commands work only with the following file types:  
 `.htm` 
 `.html` 
 `.markdown` 
 `.md` 
 `.pdf` 
 `.svg` 
 `.txt`: Preview works best if the file's content is in Markdown format\.
 `.xhtml`: Preview works best if the file contains or references content presentation information\.

**Note**  
The **Preview Settings** menu in the file preview tab is currently not functional and choosing any of its menu commands will have no effect\.

## Reload a File Preview<a name="file-preview-file-reload"></a>

On the file preview tab, choose the **Refresh** button \(the circular arrow\)\.

## Change the File Preview Type<a name="file-preview-file-preview-type"></a>

On the file preview tab, choose one of the following in the preview type list:
+  **Browser**: Previews the file in a web browser format, for the following file types only:
  +  `.htm` 
  +  `.html` 
  +  `.pdf` 
  +  `.svg` 
  +  `.xhtml`: Preview works best if the file contains or references content presentation information\.
+  **Raw Content \(UTF\-8\)**: Previews the file's original contents in Unicode Transformation Format 8\-bit \(UTF\-8\) format\. This might display unexpected content for some file types\.
+  **Markdown**: Previews any file containing Markdown format\. Attempts to preview any other file type, but might display unexpected content\.

## Open a File Preview in a Separate Web Browser Tab<a name="file-preview-file-open-tab"></a>

On the file preview tab, choose **Pop Out Into New Window**\.

## Switch to a Different File Preview<a name="file-preview-file-switch"></a>

On the file preview tab, type the path to a different file path in the address bar\. The address bar is located between the **Refresh** button and the preview type list\.