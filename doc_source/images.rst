.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _images:

##################################################
Working with Images Files in the |AC9IDElongtitle|
##################################################

.. meta::
    :description:
        Describes how to work with image files in the AWS Cloud9 IDE. 

You can use the |AC9IDE| to view and edit image files.

* :ref:`images-view-edit`
* :ref:`images-resize`
* :ref:`images-crop`
* :ref:`images-rotate`
* :ref:`images-flip`
* :ref:`images-zoom`
* :ref:`images-smooth`

.. _images-view-edit:

View or Edit an Image
=====================

In the |AC9IDE|, open the file for the image you want to view or edit. Supported image file types include the following:

* :file:`.bmp`
* :file:`.gif` (view only)
* :file:`.ico` (view only)
* :file:`.jpeg`
* :file:`.jpg`
* :file:`.png`
* :file:`.tiff`

.. _images-resize:

Resize an Image
===============

#. Open the image file in the IDE.
#. On the image editing bar, choose :guilabel:`Resize`.
#. To change the image width, type a new :guilabel:`Width` in pixels. Or choose ":guilabel:`-`" or ":guilabel:`+`" next to :guilabel:`Width` to change the current width one pixel at a time.
#. To change the image height, type a new :guilabel:`Height` in pixels. Or choose ":guilabel:`-`" or
   ":guilabel:`+`" next to :guilabel:`Height` to change the current height one pixel at a time.
#. To maintain the image ratio of width to height, leave :guilabel:`Maintain Aspect Ratio` checked.
#. To confirm the image's new size, on the image editing bar, see the width (:guilabel:`W`) and height (:guilabel:`H`) measurements in pixels.
#. Choose :guilabel:`Resize`.
#. To discard the resizing, on the menu bar, choose :guilabel:`Edit`, :guilabel:`Undo`. To keep the new
   size, choose :guilabel:`File`, :guilabel:`Save`.

.. _images-crop:

Crop an Image
=============

#. Open the image file in the IDE.
#. Drag the mouse pointer over the portion of the image that you want to keep.
#. To confirm the selection's dimensions, on the image editing bar, see the :guilabel:`Selection` dimensions,
   as follows:

   * The distance in pixels from the original image's left edge to the left edge of the selection (:guilabel:`L`)
   * The distance in pixels from the original image's top edge to the top edge of the selection (:guilabel:`T`)
   * The selection's width in pixels (:guilabel:`W`)
   * The selection's height in pixels (:guilabel:`H`)

#. On the image editing bar, choose :guilabel:`Crop`.
#. To discard the crop, on the menu bar, choose :guilabel:`Edit`, :guilabel:`Undo`. To keep the new cropped image, choose :guilabel:`File`, :guilabel:`Save`.

.. _images-rotate:

Rotate an Image
===============

#. Open the image file in the IDE.
#. To rotate the image counterclockwise, on the image editing bar, choose :guilabel:`Rotate 90 Degrees Left`.
#. To rotate the image clockwise, on the image editing bar, choose :guilabel:`Rotate 90 Degrees Right`.
#. To discard the rotation, on the menu bar, choose :guilabel:`Edit`, :guilabel:`Undo`. To keep the new rotated image, choose :guilabel:`File`, :guilabel:`Save`.

.. _images-flip:

Flip an Image
=============

#. Open the image file in the IDE.
#. To flip the image horizontally, on the image editing bar, choose :guilabel:`FlipH`.
#. To flip the image vertically, on the image editing bar, choose :guilabel:`FlipV`.
#. To discard the flip, on the menu bar, choose :guilabel:`Edit`, :guilabel:`Undo`. To keep the new flipped image, choose :guilabel:`File`, :guilabel:`Save`.

.. _images-zoom:

Zoom an Image
=============

#. Open the image file in the IDE.
#. On the image editing bar, choose one of the available zoom factors (for example, :guilabel:`75%`, :guilabel:`100%`, or :guilabel:`200%`).

.. _images-smooth:

Smooth an Image
===============

#. Open the image file in the IDE.
#. On the image editing bar, select :guilabel:`Smooth` to reduce the amount of pixelation in the image. To discard the smoothing, deselect :guilabel:`Smooth`.
#. On the menu bar, choose :guilabel:`File`, :guilabel:`Save`.