# Working with AWS IoT in AWS Cloud9 IDE<a name="iot-start"></a>

With AWS IoT in AWS Cloud9 IDE, you can interact with the AWS IoT service while minimizing interruptions to your work flow in AWS Cloud9\. This guide covers how you can get started using the AWS IoT service features that are available in the AWS Cloud9 IDE\. For more information, see [What is AWS IoT?](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html) in the *AWS IoT Developer Guide*\.

## AWS IoT prerequisites<a name="iot-cloud9-prereq"></a>

To get started using AWS IoT in AWS Cloud9 IDE, make sure your AWS account and AWS Cloud9 setup meet all the requirements\. For information about the AWS account requirements and AWS user permissions specific to the AWS IoT service, see the [Getting Started with AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/setting-up.html) in the *AWS IoT Developer Guide*\.

## AWS IoT Things<a name="iot-cloud9-things"></a>

AWS IoT connects devices to AWS services and AWS resources\. You can connect your devices to AWS IoT by using objects called **things**\. A thing is a representation of a specific device or logical entity\. It can be a physical device or sensor \(for example, a light bulb or a switch on a wall\)\. For more information about AWS IoT things, see [Managing devices with AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html) in the *AWS IoT Developer Guide*\. 

### Managing AWS IoT things<a name="iot-cloud9-things-actions"></a>

The AWS Cloud9 IDE has several features that make your thing management efficient\. To manage your AWS IoT things, follow these steps: 
+ [Create a thing](#thing-create)
+ [Attach a certificate to a thing](#thing-certificate-attach)
+ [Detach a certificate from a thing](#thing-certificate-detach)
+ [Delete a thing](#thing-delete)<a name="thing-create"></a>

**To create a thing**

1. From the AWS Explorer, expand the **IoT** service section\.

1. Open the context \(right\-click\) menu for the **thing** and choose **Create Thing**\.

1. Enter a name for the **thing** in the **Thing Name** field and follow the prompt\.

1. When this step is complete, a **thing icon** followed by the name that you specified is visible in the **Thing** section\.<a name="thing-certificate-attach"></a>

**To attach a certificate to a thing**

1. From the AWS Explorer, expand the **IoT** service section\.

1. Under the **Things** subsection, locate the **thing** where you're attaching the certificate\. 

1. Open the context \(right\-click\) menu for the **thing** and choose **Attach Certificate** from the context\-menu, to open an input selector with a list of your certificates\.

1. From the list, choose the **certificate ID** that corresponds to the certificate that you want to attach to your thing\.

1. After this step is complete, your certificate is accessible in the AWS Explorer as an item of the thing that you attached it to\.<a name="thing-certificate-detach"></a>

**To detach a certificate from a thing**

1. From the AWS Explorer, expand the **IoT** service section\.

1. In the **Things** subsection, locate the **thing** that you want to detach a certificate from\. 

1. Open the context \(right\-click\) menu for the **thing** and choose **Attach Certificate**\.

1. After this step is complete, the detached certificate is no longer displayed under the thing in the AWS Explorer\. However, it's still accessible from the **Certificates** subsection\.<a name="thing-delete"></a>

**To delete a thing**

1. From the AWS Explorer, expand the **IoT** service section\.

1. In the **Things** subsection, locate the **thing** that you want to delete\.

1. Open the context \(right\-click\) menu for the **thing** and choose **Delete Thing**\.

1. After this step is completed, the deleted **thing** is no longer available from the **Things** subsection\.
**Note**  
You can only delete a thing that doesn't have a certificate attached to it\.

## AWS IoT certificates<a name="iot-cloud9-cert"></a>

Certificates are a common way to create a secure connection between your AWS IoT services and devices\. X\.509 certificates are digital certificates that use the X\.509 public key infrastructure standard to associate a public key with an identity contained in a certificate\. For more information about AWS IoT certificates, see [Authentication \(IoT\)](https://docs.aws.amazon.com/iot/latest/developerguide/authentication.html) in the *AWS IoT Developer Guide*\.

### Managing certificates<a name="iot-cloud9-cert-actions"></a>

The AWS toolkit offers a variety of ways for you to manage your AWS IoT certificates directly from the AWS Explorer\. They're outlined in the following steps:
+ [Create a certificate](#cert-create)
+ [Change a certificate status](#cert-status)
+ [Attach a policy to a certificate](#cert-attach-policy)
+ [Delete a certificate](#cert-delete)<a name="cert-create"></a>

**To create an AWS IoT certificate**

An X\.509 certificate is used to connect with your instance of AWS IoT\. 

1. From the AWS Explorer, expand the **IoT** service section, and open \(right\-click\) **Certificates**\.

1. To open a dialog box, choose **Create Certificate** from the context\-menu\.

1. To save your RSA key pair and X\.509 certificate, select a directory in your local file system\.
**Note**  
The default file names contain the certificate ID as a prefix\.
Only the X\.509 certificate is stored with your AWS account, through the AWS IoT service\.
Your RSA key pair can only be issued once, save them to a secure location in your file system when you're prompted\.
If the certificate or the key pair can't be saved to your file system, then the AWS Toolkit deletes the certificate from your AWS account\.<a name="cert-status"></a>

**To modify a certificate status**

The status of an individual certificate is displayed next to the certificate ID in the AWS Explorer and can be set to **active**, **inactive**, or **revoked**\.
**Note**  
Your certificate needs an **active** status before you can use it to connect your device to your AWS IoT service\.
An **inactive** certificate can be activated, whether it was deactivated previously or is inactive by default\.
A certificate that has been **revoked** can't be reactivated\.

1. From the AWS Explorer, expand the **IoT** service section\.

1. In the **Certificates** subsection, locate the certificate that you want to modify\.

1. Open the context \(right\-click\) menu for the certificate that displays the status change options available for that certificate\.
+ If a certificate has the status **inactive**, choose **activate** to change the status to **active**\.
+ If a certificate has the status **active**, choose **deactivate** to change the status to **inactive**\.
+ If a certificate has either an **active** or **inactive** status, choose **revoke** to change the status to **revoked**\.

**Note**  
Each of these status\-changing actions is available if you select a certificate that is attached to a thing while displayed in the **Things** subsection\.<a name="cert-attach-policy"></a>

**To attach an IoT policy to a certificate**

1. From the AWS Explorer, expand the **IoT** service section\.

1. In the **Certificates** subsection, locate the certificate that you want to modify\.

1. Open the context \(right\-click\) menu for the certificate and choose **Attach Policy** to open an input selector with a list of your available policies\.

1. Choose the policy that you want to attach to the certificate\.

1. When this step is completed, the policy that you selected is added to the certificate as a sub\-menu item\.<a name="cert-detach-policy"></a>

**To detach an IoT policy from a certificate**

1. From the AWS Explorer, expand the **IoT** service section\.

1. In the **Certificates** subsection, locate the certificate that you want to modify\.

1. Expand the certificate and locate the policy that you want to detach\.

1. Open the context \(right\-click\) menu for the policy and choose **Detach** from the context menu\.

1. When this step is completed, the policy is no longer accessible from your certificate, it's available from the **Policy** subsection\.<a name="cert-delete"></a>

**To delete a certificate**

1. From the AWS Explorer, expand the **IoT** service heading\.

1. In the **Certificates** subsection, locate the certificate that you want to delete\.

1. Open the context \(right\-click\) menu for the certificate and choose **Delete Certificate** from the context menu\.
**Note**  
You can't delete a certificate if it's attached to a thing or has an active status\. You can delete a certificate that has attached policies\.

## AWS IoT policies<a name="iot-vsctoolkit-policy"></a>

AWS IoT Core policies are defined through JSON documents\. Each contains at least one policy statement\. Policies define how AWS IoT, AWS, and your device can interact with each other\. For more information about how to create a policy document, see [IoT Polices](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html) in the *AWS IoT Developer Guide*\.

**Note**  
Named policies are versioned so that you can roll them back\. In the AWS Explorer, your IoT polices are listed under the **Policies** subsection in the AWS IoT service\. You can view policy versions by expanding a policy\. The default version is denoted by an asterisk \(\*\)\.

### Managing policies<a name="iot-vsctoolkit-policy-actions"></a>

The AWS Cloud9 IDE offers several ways for you to manage your AWS IoT service policies\. These are ways that you can manage or modify your policies directly from the AWS Explorer in VS Code: 
+ [Create a policy](#policy-create)
+ [Upload a new policy version](#policy-version-upload)
+ [Edit a policy version](#policy-version-edit)
+ [Change the policy version defualt](#policy-version-default)
+ [Change the policy version defualt](#policy-delete)<a name="policy-create"></a>

**To create an AWS IoT policy**
**Note**  
You can create a new policy from the AWS Explorer\. However, the JSON document that defines the policy must already exist in your file system\.

1. From the AWS Explorer, expand the **IoT** service section\.

1. Open the context \(right\-click\) menu for the **Policies** subsection and to open the **Policy Name** input field choose **Create Policy from Document**\.

1. Enter a name and follow the prompts to open a dialog asking you to select a JSON document from your file system\.

1. Choose the JSON file that contains your policy definitions, the policy is available in the AWS explorer after this is complete\.<a name="policy-version-upload"></a>

**To upload a new AWS IoT policy version**

You can create a new version of a policy by uploading a JSON document to the policy\.
**Note**  
The new JSON document must be present on your file system to create a new version using the AWS Explorer\.

1. From the AWS Explorer, expand the **IoT** service section\.

1.  Expand the **Policies** subsection to view your AWS IoT policies\.

1. Open the context \(right\-click\) menu for the policy that you want to update and choose **Create new version from Document**\.

1. When the dialog opens, choose the JSON file that contains the updates to your policy definitions\. 

   The new version is accessible from your policy in the AWS Explorer\.<a name="policy-version-edit"></a>

**To edit an AWS IoT policy version**

You can open and edit a policy document using AWS Cloud9\. When you finished editing the document, save it to your file system\. Then, upload it to your AWS IoT service from the AWS Explorer\.

1. From the AWS Explorer, expand the **IoT** service section\.

1. Expand the **Policies** subsection and locate the policy you want to update\.

1. To open the **Policy Name**, choose **Create Policy** from **Document**\.

1. Expand the policy that you want to update and then open the context \(right\-click\) menu for the policy version that you want to edit\.

1. To open the policy version in AWS Cloud9, choose **View** from the context\-menu to open the policy version\.

1. When the policy document is opened, edit and save the changes\.
**Note**  
At this point, the changes that you made to the policy are only saved to your local file system\. To update the version and track it with the AWS Explorer, repeat the steps in [Upload a new policy version](#policy-version-upload)\.<a name="policy-version-default"></a>

**To select a new policy version default**

1. From the AWS Explorer, expand the **IoT** service section\.

1. Expand the **Policies** subsection and locate the policy that you want to update\.

1. Expand the policy that you want to update, and then open the context \(right\-click\) menu for the policy version that you want to set and choose **Set as Default**\. 

   When this is complete, the new default version that you selected has a star next to it\.<a name="policy-delete"></a>

**To delete policies**
**Note**  
Before you can delete a policy or a policy version, make sure that the following conditions are met:  
You can't delete a policy if that policy is attached to a certificate\.
You can't delete a policy if that policy has any non\-default versions\.
You can only delete the default version of a policy if a new default version is selected or the entire policy is deleted\.
Before you delete an entire policy, you must delete all of the non\-default version of that same policy\.

1. From the AWS Explorer, expand the **IoT** service section\.

1. Expand the **Policies** subsection and locate the policy that you want to update\.

1. Expand the policy that you want to update, and open the context \(right\-click\) menu for the policy version that you want delete and choose **Delete**\.

1. When a version is deleted, it's no longer visible from the AWS Explorer\.

1. If only the default version of a policy is left, open the context \(right\-click\) menu for the parent policy and choose **Delete**\.