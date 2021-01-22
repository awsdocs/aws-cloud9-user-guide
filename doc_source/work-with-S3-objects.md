# Working with Amazon S3 objects<a name="work-with-S3-objects"></a>

Objects are the fundamental entities stored in Amazon S3\. Objects consist of object data and metadata\.

**Topics**
+ [Uploading a file to an Amazon S3 bucket](#uploading-s3-object-to-bucket)
+ [Downloading an Amazon S3 object](#downloading-s3-object)
+ [Deleting an Amazon S3 object](#deleting-s3-object)

## Uploading a file to an Amazon S3 bucket<a name="uploading-s3-object-to-bucket"></a>

This procedure uploads a file from a user's environment and stores it as an S3 object in the AWS Cloud\. You can upload a file to a bucket or to a folder that organizes that bucket's contents\.

1. In the **AWS Explorer**, choose the **S3** node to view the list of buckets\.

1. Open the context menu \(right\-click\) for a bucket or a folder in that bucket, and then choose **Upload File**\. 
**Note**  
If you open the context menu \(right\-click\) an S3 object, you can choose **Upload to Parent**\. This enables you to add a file to the folder or bucket that contains the selected file\.

1. Using your environment's file manager, select a file, and then choose **Upload**\.

   The selected file is uploaded as an S3 object to the bucket or folder\. Each object's entry describes the size of the stored object and how long ago it was uploaded\. You can pause over the object's listing to view the path, size, and time when it was last modified\.

## Downloading an Amazon S3 object<a name="downloading-s3-object"></a>

You can download objects in an Amazon S3 bucket from the AWS Cloud to a folder in your AWS Cloud9 environment\.

1. In the **AWS Explorer**, choose the **S3** node to view the list of buckets\.

1. In a bucket or in a folder in a bucket, open the context menu \(right\-click\) for an object, and then choose **Download As**\.

1. Using your environment's file manager, select a destination folder, enter a file name, and then choose **Download**\.

After a file is downloaded, you can open it in AWS Cloud9\.

## Deleting an Amazon S3 object<a name="deleting-s3-object"></a>

You can permanently delete an object if it's in a non\-versioned bucket\. But for versioning\-enabled buckets, a delete request does not permanently delete that object\. Instead, Amazon S3 inserts a delete marker in the bucket\. For more information, see [Deleting object versions](https://docs.aws.amazon.com/AmazonS3/latest/dev/DeletingObjectVersions.html) in the *Amazon Simple Storage Service Developer Guide*\.

1. In the **AWS Explorer**, choose the **S3** node to view the list of buckets\.

1. In a bucket or a folder in a bucket, open the context menu \(right\-click\) for an object, and then choose **Delete**\.

1. Choose **Delete** to confirm the deletion\.