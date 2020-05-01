# Resilience in AWS Cloud9<a name="disaster-recovery-resiliency"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones\. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low\-latency, high\-throughput, and highly redundant networking\. With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption\. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures\. 

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](http://aws.amazon.com/about-aws/global-infrastructure/)\.

In addition to the AWS global infrastructure, AWS Cloud9 supports specific features to support your data resiliency and backup needs\.
+ Integrate AWS Cloud9 with AWS CodeCommit, a version control service hosted by Amazon Web Services that you can use to privately store and manage assets \(such as documents, source code, and binary files\) in the cloud\. For more information, see [Integrate AWS Cloud9 with AWS CodeCommit ](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-ide-c9.html) in the *AWS CodeCommit User Guide*\.
+ Use the Git version control system on AWS Cloud9 development environments to back up files and data on a remote GitHub repository\. For more information, see [GitHub Sample for AWS Cloud9](sample-github.md)\.