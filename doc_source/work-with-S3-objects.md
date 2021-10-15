# Working with Amazon S3 objects<a name="work-with-S3-objects"></a>

Objects are the fundamental entities stored in Amazon S3\. Objects consist of object data and metadata\.

**Topics**
+ [Uploading a file to an Amazon S3 bucket](#uploading-s3-object-to-bucket)
+ [Downloading an Amazon S3 object](#downloading-s3-object)
+ [Deleting an Amazon S3 object](#deleting-s3-object)
+ [Generating a presigned URL for an Amazon S3 object](#presigned-s3-object)

## Uploading a file to an Amazon S3 bucket<a name="uploading-s3-object-to-bucket"></a>

You can use the Toolkit interface or a command to upload a file to a bucket 

Both methods allow you to upload a file from a user's environment and store it as an S3 object in the AWS Cloud\. You can upload a file to a bucket or to a folder that organizes that bucket's contents\.

## Upload a file to an S3 bucket using the interface

1. In the **AWS Explorer**, choose the **S3** node to view the list of buckets\.

1. Open the context menu \(right\-click\) for a bucket or a folder in that bucket, and then choose **Upload File**\. 
**Note**  
If you open the context menu \(right\-click\) an S3 object, you can choose **Upload to Parent**\. This enables you to add a file to the folder or bucket that contains the selected file\.

1. Using your environment's file manager, select a file, and then choose **Upload**\.

   The selected file is uploaded as an S3 object to the bucket or folder\. Each object's entry describes the size of the stored object and how long ago it was uploaded\. You can pause over the object's listing to view the path, size, and time when it was last modified\.

## Upload the current file to an S3 bucket using a command

1. To select a file for upload, choose the file's tab\.

1. Press **Ctrl\+P** to display the **Commands** pane\.

1. For **Go To Anything**, start to enter the phrase `upload file` to display the `AWS: Upload File` command\. Choose the command when it appears\.

1. For **Step 1: Select a file to upload**, you can choose the file you've selected or browse for another file\.

1. For **Step 2: Select an S3 bucket to upload to**, choose a bucket from the list\.

   The selected file is uploaded as an S3 object to the bucket or folder\. Each object's entry describes the size of the stored object and how long ago it was uploaded\. You can pause over the object's listing to view the path, size, and time when it was last modified\.

## Downloading an Amazon S3 object<a name="downloading-s3-object"></a>

You can download objects in an Amazon S3 bucket from the AWS Cloud to a folder in your AWS Cloud9 environment\.

1. In the **AWS Explorer**, choose the **S3** node to view the list of buckets\.

1. In a bucket or in a folder in a bucket, open the context menu \(right\-click\) for an object, and then choose **Download As**\.

1. Using your environment's file manager, select a destination folder, enter a file name, and then choose **Download**\.

After a file is downloaded, you can open it in AWS Cloud9\.

## Deleting an Amazon S3 object<a name="deleting-s3-object"></a>

You can permanently delete an object if it's in a non\-versioned bucket\. But for versioning\-enabled buckets, a delete request does not permanently delete that object\. Instead, Amazon S3 inserts a delete marker in the bucket\. For more information, see [Deleting object versions](https://docs.aws.amazon.com/AmazonS3/latest/dev/DeletingObjectVersions.html) in the *Amazon Simple Storage Service User Guide*\.

1. In the **AWS Explorer**, choose the **S3** node to view the list of buckets\.

1. In a bucket or a folder in a bucket, open the context menu \(right\-click\) for an object, and then choose **Delete**\.

1. Choose **Delete** to confirm the deletion\.

## Generating a presigned URL for an Amazon S3 object<a name="presigned-s3-object"></a>

With presigned URLS, an object owner can share private Amazon S3 objects with others by granting time\-limited permission to download the objects\. For more information, see [Sharing an object with a presigned URL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html) in the *Amazon S3 User Guide*\.

1. In the **AWS Explorer**, choose the **S3** node to view the list of buckets\.

1. In a bucket or a folder in a bucket, right\-click an object, and then choose **Generate Presigned URL**\.

1. In the AWS Toolkit command pane, enter the number of minutes that the URL can be used to access the object\. Press **Enter** to confirm\.

   The status at the bottom of the IDE confirms that presigned URL for the object was copied to your clipboard\.