# Inbound SSH IP address ranges for AWS Cloud9<a name="ip-ranges"></a>

You can restrict incoming traffic to only the IP address ranges that AWS Cloud9 uses to connect over SSH to AWS cloud compute instances \(for example Amazon EC2 instances\) in an Amazon VPC or your own servers in your network\.

**Note**  
You can restrict incoming traffic to only the IP address ranges that AWS Cloud9 uses to connect over SSH\. For an EC2 environment created on or after July 31 2018, you can skip this topic\. This is because AWS Cloud9 automatically restricts inbound SSH traffic for that environment to only those IP addresses that are described later in this topic\. AWS Cloud9 does this by automatically adding a rule to the security group that's associated with the Amazon EC2 instance for the environment\. This rule restricts inbound SSH traffic over port 22 to only those IP addresses for the associated AWS Region\. For your own servers in your network you still have to follow the steps described later in this topic\.

IP address ranges for most AWS Regions are in the `ip-ranges.json` file, as described in [AWS IP Address Ranges](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html) in the *AWS General Reference*\.

**Note**  
See [below](#non-file-IP) for IP address ranges for the Asia Pacific \(Hong Kong\), Europe \(Milan\), and Middle East \(Bahrain\) Regions thataren't currently included in the `ip-ranges.json` file\. 

 To find the IP ranges in the `ip-ranges.json` file:
+ For Windows, using the AWS Tools for Windows PowerShell, run the following command\.

  ```
  Get-AWSPublicIpAddressRange -ServiceKey CLOUD9
  ```
+ For Linux, download the [ip\-ranges\.json](https://ip-ranges.amazonaws.com/ip-ranges.json) file\. Then, you can query it by using a tool such as ** `jq` ** by running the following command\.

  ```
  jq '.prefixes[] | select(.service=="CLOUD9")' < ip-ranges.json
  ```

These IP ranges might change occasionally\. Whenever there's a change, we send notifications to subscribers of the `AmazonIpSpaceChanged` topic\. To get these notifications, see [AWS IP Address Ranges Notifications](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html#subscribe-notifications) in the *AWS General Reference*\.

To use these IP address ranges when configuring environments that use AWS cloud compute instances, see [VPC settings for AWS Cloud9 Development Environments](vpc-settings.md)\. Also, if you choose to restrict incoming traffic for EC2 environments, or for SSH environments associated with Amazon EC2 instances that are running Amazon Linux or Ubuntu Server, be sure to also allow at minimum all IP addresses using TCP over ports 32768\-61000\. For more information, and port ranges for other AWS cloud compute instance types, see [Ephemeral ports](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_ACLs.html#VPC_ACLs_Ephemeral_Ports) in the *Amazon VPC User Guide*\.

To use these IP address ranges when configuring SSH environments that use your own network, see the documentation for your network or your network administrator\.

## IP addresses not in `ip-ranges.json`<a name="non-file-IP"></a>

AWS Cloud9 IP address ranges for the following AWS Regions aren't currently provided in the `ip-ranges.json` file: Asia Pacific \(Hong Kong\), Europe \(Milan\), and Middle East \(Bahrain\)\. The following table lists the IP ranges for those Regions\.

**Note**  
Each Region has two IP address ranges to support the AWS Cloud9 control plane \(information routing\) and data plane \(information processing\) services\. 


| AWS Region | Code | IP ranges \(CIDR notation\) | 
| --- | --- | --- | 
|  Asia Pacific \(Hong Kong\)  |  `ap-east1`  |  `18.163.201.96/27` `18.163.139.32/27`  | 
|  Europe \(Milan\)  |  `eu-south-1`  |  `15.161.135.64/27` `15.161.135.96/27`  | 
|  Middle East \(Bahrain\)  |  `me-south-1`  |  `15.185.141.160/27` `15.185.91.32/27`  | 