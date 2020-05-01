# Security best practices for AWS Cloud9<a name="security-best-practices"></a>

The following best practices are general guidelines and don’t represent a complete security solution\. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations instead of prescriptions\.

**Some security best practices for AWS Cloud9**
+ Store your code securely in a version control system, for example, [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/)\.
+ For your AWS Cloud9 EC2 development environments, configure and use [Amazon Elastic Block Store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) encrypted volumes\.
+ For your EC2 environments, use [tags](tags.md) to control access to your AWS Cloud9 resources\.
+ For your shared AWS Cloud9 development environments, follow the [best practices](share-environment.md#share-environment-best-practices) for them\.