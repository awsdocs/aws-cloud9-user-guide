# Data encryption<a name="data-encryption"></a>

Data encryption refers to protecting data while in transit \(as it travels between AWS Cloud9 and your AWS account\) and at rest \(while it is stored in AWS Cloud9 configuration stores and AWS cloud\-compute instances\)\.

In the context of AWS Cloud9, the following types of data may require protection through encryption:

***Your content and data***

Information that you manipulate, collect, and store\. The following are examples of this type of data:
+ Your code files
+ Configuration, applications, and data for the attached EC2 environment or SSH environment

***AWS Cloud9 metadata***

 Data that AWS Cloud9 manipulates, collects, and stores\. The following are examples of this type of data:
+ IDE settings such as tab states, open files, and IDE preferences
+ AWS Cloud9 development environment metadata such as environment names and descriptions
+ AWS Cloud service API, and console logs
+ Service logs such as HTTP requests

AWS Cloud9 also transmits some of your content and data through its data plane service\. This includes your files, terminal input, output text, and some IDE commands \(for example, for saving files\)\.

## Encryption at rest<a name="encryption-at-rest"></a>

Encryption at rest refers to protecting your data from unauthorized access by encrypting data while stored\. Any customer data stored in an AWS Cloud9 environment such as code files, packages, or dependencies is always stored in the customer's resources\. If the customer uses an Amazon EC2 environment, the data is stored in the associated Amazon Elastic Block Store \(Amazon EBS\) volume that exists in their AWS account\. If the customer uses an SSH environment, the data is stored in local storage on their Linux server\. 

When Amazon EC2 instances are created for an AWS Cloud9 development environment, an unencrypted Amazon EBS volume is created and attached to that instance\. Customers who want to encrypt their data need to create an encrypted EBS volume and attach it to the EC2 instance\. 

Metadata about the AWS Cloud9 development environments, such as environment names, members of the environments, and IDE settings, is stored by AWS, not in customer resources\. Customer\-specific information, such as environment descriptions and IDE settings, is encrypted\.

## Encryption in transit<a name="encryption-in-transit"></a>

Encryption in transit refers to protecting your data from being intercepted while it moves between communication endpoints\. All data transmitted between the customer's client and the AWS Cloud9 service is encrypted through HTTPS, WSS, and encrypted SSH\.
+ **HTTPS** – Ensures secure requests between the customer's web browser and the AWS Cloud9 service\. AWS Cloud9 also loads assets from Amazon CloudFront sent over HTTPS from the customer's browser\.
+ **WSS \(WebSocket Secure\)** – Enables secure two\-way communications through WebSockets between the customer's web browser and the AWS Cloud9 service\.
+ **Encrypted SSH \(Secure Shell\)**: Enables secure transmission of data between the client's web browser and the AWS Cloud9 service\.

Use of HTTPS, WSS, and SSH protocols depends on your using a browser supported by AWS Cloud9\. See [Supported Browsers for AWS Cloud9](browsers.md)\.

**Note**  
Encryption protocols are implemented by default in AWS Cloud9\. Customers cannot change encryption\-in\-transit settings\.

## Key management<a name="key-management"></a>

AWS Key Management Service \(AWS KMS\) is a managed service for creating and controlling customer master keys \(CMKs\), the encryption keys used to encrypt the customer's data\. AWS Cloud9 generates and manages cryptographic keys for encrypting data on behalf of customers\. 

## Internetwork traffic privacy<a name="internetwork-privacy"></a>

SSH environments connect to on\-premises, customer\-owned compute and storage\. Encrypted SSH, HTTPS, and WSS connections support data transit between the service and SSH environment\.

You can configure AWS Cloud9 EC2 development environments \(backed by Amazon EC2 instances\) to be launched within specific VPCs and subnets\. For more information about Amazon Virtual Private Cloud settings, see [VPC Settings for AWS Cloud9 Development Environments](vpc-settings.md)\.