# Working with Images Files in the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="images"></a>

You can use the AWS Cloud9 IDE to view and edit image files\.
+  [View or Edit an Image](#images-view-edit) 
+  [Resize an Image](#images-resize) 
+  [Crop an Image](#images-crop) 
+  [Rotate an Image](#images-rotate) 
+  [Flip an Image](#images-flip) 
+  [Zoom an Image](#images-zoom) 
+  [Smooth an Image](#images-smooth) 

## View or Edit an Image<a name="images-view-edit"></a>

In the AWS Cloud9 IDE, open the file for the image you want to view or edit\. Supported image file types include the following:
+  `.bmp` 
+  `.gif` \(view only\)
+  `.ico` \(view only\)
+  `.jpeg` 
+  `.jpg` 
+  `.png` 
+  `.tiff` 

## Resize an Image<a name="images-resize"></a>

1. Open the image file in the IDE\.

1. On the image editing bar, choose **Resize**\.

1. To change the image width, type a new **Width** in pixels\. Or choose "**\-**" or "**\+**" next to **Width** to change the current width one pixel at a time\.

1. To change the image height, type a new **Height** in pixels\. Or choose "**\-**" or "**\+**" next to **Height** to change the current height one pixel at a time\.

1. To maintain the image ratio of width to height, leave **Maintain Aspect Ratio** checked\.

1. To confirm the image's new size, on the image editing bar, see the width \(**W**\) and height \(**H**\) measurements in pixels\.

1. Choose **Resize**\.

1. To discard the resizing, on the menu bar, choose **Edit**, **Undo**\. To keep the new size, choose **File**, **Save**\.

## Crop an Image<a name="images-crop"></a>

1. Open the image file in the IDE\.

1. Drag the mouse pointer over the portion of the image that you want to keep\.

1. To confirm the selection's dimensions, on the image editing bar, see the **Selection** dimensions, as follows:
   + The distance in pixels from the original image's left edge to the left edge of the selection \(**L**\)
   + The distance in pixels from the original image's top edge to the top edge of the selection \(**T**\)
   + The selection's width in pixels \(**W**\)
   + The selection's height in pixels \(**H**\)

1. On the image editing bar, choose **Crop**\.

1. To discard the crop, on the menu bar, choose **Edit**, **Undo**\. To keep the new cropped image, choose **File**, **Save**\.

## Rotate an Image<a name="images-rotate"></a>

1. Open the image file in the IDE\.

1. To rotate the image counterclockwise, on the image editing bar, choose **Rotate 90 Degrees Left**\.

1. To rotate the image clockwise, on the image editing bar, choose **Rotate 90 Degrees Right**\.

1. To discard the rotation, on the menu bar, choose **Edit**, **Undo**\. To keep the new rotated image, choose **File**, **Save**\.

## Flip an Image<a name="images-flip"></a>

1. Open the image file in the IDE\.

1. To flip the image horizontally, on the image editing bar, choose **FlipH**\.

1. To flip the image vertically, on the image editing bar, choose **FlipV**\.

1. To discard the flip, on the menu bar, choose **Edit**, **Undo**\. To keep the new flipped image, choose **File**, **Save**\.

## Zoom an Image<a name="images-zoom"></a>

1. Open the image file in the IDE\.

1. On the image editing bar, choose one of the available zoom factors \(for example, **75%**, **100%**, or **200%**\)\.

## Smooth an Image<a name="images-smooth"></a>

1. Open the image file in the IDE\.

1. On the image editing bar, select **Smooth** to reduce the amount of pixelation in the image\. To discard the smoothing, deselect **Smooth**\.

1. On the menu bar, choose **File**, **Save**\.