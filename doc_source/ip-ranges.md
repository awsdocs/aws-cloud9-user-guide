# Inbound SSH IP Address Ranges for AWS Cloud9<a name="ip-ranges"></a>

You can restrict incoming traffic to just the IP address ranges that AWS Cloud9 uses to connect over SSH to AWS cloud compute instances \(for example Amazon EC2 instances\) in an Amazon VPC or your own servers in your network\.

**Note**  
For an EC2 environment created on or after July 31 2018, you can skip this topic\. This is because AWS Cloud9 automatically restricts inbound SSH traffic for that environment to only those IP addresses that are described later in this topic\. AWS Cloud9 does this by automatically adding a rule to the security group that is associated with the Amazon EC2 instance for the environment\. This rule restricts inbound SSH traffic over port 22 to only those IP addresses for the associated AWS Region\.

These IP address ranges are in the `ip-ranges.json` file, as described in [AWS IP Address Ranges](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html) in the *AWS General Reference*\. To find the IP ranges in that file:
+ For Windows, using the AWS Tools for Windows PowerShell, run the following command\.

  ```
  Get-AWSPublicIpAddressRange -ServiceKey CLOUD9
  ```
+ For Linux, download the [ip\-ranges\.json](https://ip-ranges.amazonaws.com/ip-ranges.json) file\. Then you can query it by using a tool such as ** `jq` **, for example by running the following command\.

  ```
  jq '.prefixes[] | select(.service=="CLOUD9")' < ip-ranges.json
  ```

These IP ranges might change occasionally\. Whenever there's a change, we send notifications to subscribers of the `AmazonIpSpaceChanged` topic\. To get these notifications, see [AWS IP Address Ranges Notifications](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html#subscribe-notifications) in the *AWS General Reference*\.

To use these IP address ranges when configuring environments that use AWS cloud compute instances, see [VPC Settings for AWS Cloud9 Development Environments](vpc-settings.md)\. Also, if you choose to restrict incoming traffic for EC2 environments, or for SSH environments associated with Amazon EC2 instances running Amazon Linux or Ubuntu Server, be sure to also allow at minimum all IP addresses using TCP over ports 32768\-61000\. For more information, as well as port ranges for other AWS cloud compute instance types, see [Ephemeral Ports](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_ACLs.html#VPC_ACLs_Ephemeral_Ports) in the *Amazon VPC User Guide*\.

To use these IP address ranges when configuring SSH environments that use your own network, see your network's documentation or your network administrator\.