# Accessing no\-ingress EC2 instances with AWS Systems Manager<a name="ec2-ssm"></a>

A "no\-ingress EC2 instance" that's created for an EC2 environment enables AWS Cloud9 to connect to its Amazon EC2 instance without the need to open any inbound ports on that instance\. You can select the no\-ingress option when creating an EC2 environment using the [console](create-environment-main.md#create-environment-console), the [command line interface](tutorial-create-environment-cli-step1.md), or a [AWS CloudFormation stack](#cfn-role-and-permissions)\.

**Important**  
There are no additional charges for using Systems Manager Session Manager to manage connections to your EC2 instance\.

![\[Selecting a new no-ingress EC2 instance for your environment\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/EC2-options-with-SSM.png)

When selecting an environment type in the **Environment settings** section of the console, you can choose a new EC2 instance that requires inbound connectivity or a new no\-ingress EC2 instance that doesn't:
+ **[Create a new EC2 instance for environment \(direct access\)](create-environment-main.md#create-environment-console)** – With this setup, the security group for the instance has a rule to allow incoming networking traffic\. An open inbound port enables AWS Cloud9 to connect over SSH to its instance\. Incoming network traffic is restricted to [ IP addresses approved for AWS Cloud9 connections](ip-ranges.md)\.
+ **[Create a new no\-ingress EC2 instance for environment \(access via Systems Manager\)](create-environment-main.md#create-environment-console)** – With this setup, the security group for the instance has no inbound rule\. This means no inbound traffic originating from another host to the instance is allowed\. So AWS Cloud9 doesn't directly connect to the instance over SSH\. Instead, the environment connects through AWS Systems Manager Session Manager\. For more information, see [Benefits of using Systems Manager for EC2 environments](#ssm-benefits)\.

**Note**  
You also have a third option of selecting **Create and run in remote server \(SSH connection\)**\. For more information about having AWS Cloud9 connect to an *existing* EC2 instance or your own server, see [Creating an SSH Environment](create-environment-ssh.md)\.

If creating an environment using the [AWS CLI](tutorial-create-environment-cli-step1.md), you can configure a no\-ingress EC2 instance by setting the `--connection-type CONNECT_SSM` option when calling the `create-environment-ec2` command\. For more information about creating the required service role and instance profile, see [Managing instance profiles for Systems Manager with the AWS CLI](#aws-cli-instance-profiles)\. 

After you complete the creation of an environment that uses a no\-ingress EC2 instance, confirm the following:
+ Systems Manager Session Manager has permissions to perform actions on the EC2 instance on your behalf \(see [Managing Systems Manager permissions](#service-role-ssm)\)\.
+ AWS Cloud9 users can access the instance managed by Session Manager \(see [Giving users access to instances managed by Session Manager](#access-ec2-session)\)\.

## Benefits of using Systems Manager for EC2 environments<a name="ssm-benefits"></a>

Allowing [Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) to handle the secure connection between AWS Cloud9 and its EC2 instance offers two key benefits: 
+ No requirement to open inbound ports for the instance
+ Option to launch the instance into a public or private subnet

------
#### [ No open inbound ports ]

Secure connections between AWS Cloud9 and its EC2 instance are handled by [Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)\. Session Manager is a fully managed Systems Manager capability that enables AWS Cloud9 to connect to its EC2 instance without the need to open inbound ports\. 

**Important**  
The option to use Systems Manager for no\-ingress connections is currently available only when creating new EC2 environments\.

 With the start of a Session Manager session, a connection is made to the target instance\. With the connection in place, the environment can now interact with the instance through the Systems Manager service\. The Systems Manager service communicates with the instance through the Systems Manager Agent \([SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html)\)\.

 SSM Agent is installed, by default, on all instances used by EC2 environments\.

------
#### [ Private/public subnets ]

When selecting a subnet for your instance in the **Network settings \(advanced\)** section, you can select a private or public subnet if the instance for your environment is accessed through Systems Manager\.

![\[Selecting a new no-ingress EC2 instance for your environment\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/private-subnet-option.png)

**Private subnets**

For a private subnet, the interface text reminds that you to add a network address translation \(NAT\) gateway to allow the instance to connect to AWS Cloud9 and the internet\.

The advantage of using the NAT gateway is that it prevents the internet from initiating a connection to the instance in the private subnet\. Because the instance for your environment is assigned a private IP address instead of a public one, the NAT gateway forwards traffic from the instance to the internet or other AWS services, and then sends the response back to the instance\.

**Important**  
Currently, if the EC2 instance for your environment is launched into a private subnet, you can't use [AWS managed temporary credentials](how-cloud9-with-iam.md#auth-and-access-control-temporary-managed-credentials) to allow the EC2 environment to access an AWS service on behalf of an AWS entity \(an IAM user, for example\)\.

**Public subnets**

If your development environment is using SSM to access an EC2 instance, ensure that the instance is assigned a public IP address by the public subnet it's launched into\. To do so, you can specify your own IP address or enable the automatic assignment of a public IP address\. For the steps involved in modifying auto\-assign IP settings, see [IP Addressing in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html) in the *Amazon VPC User Guide*\. 

For more information on configuring private and public subnets for your environment instances, see [Create a subnet for AWS Cloud9](vpc-settings.md#vpc-settings-create-subnet)\. 

------

## Managing Systems Manager permissions<a name="service-role-ssm"></a>

By default, Systems Manager doesn't have permission to perform actions on EC2 instances\. Access is provided through an AWS Identity and Access Management \(IAM\) instance profile\. \(An instance profile is a container that passes IAM role information to an EC2 instance at launch\.\)

When you create the no\-ingress EC2 instance using the AWS Cloud9 console, both the service role \(`AWSCloud9SSMAccessRole`\) and the IAM instance profile \(`AWSCloud9SSMInstanceProfile`\) are created automatically for you\. \(You can view `AWSCloud9SSMAccessRole` in the IAM Management console\. Instance profiles aren't displayed in the IAM console\.\) 

**Important**  
 If you create a no\-ingress EC2 environment for the first time with AWS CLI, you must explicitly define the required service role and instance profile\. For more information, see [Managing instance profiles for Systems Manager with the AWS CLI](#aws-cli-instance-profiles)\.

For extra security protection, the AWS Cloud9 service\-linked role, `AWSServiceRoleforAWSCloud9`, features a `PassRole` restriction in its `AWSCloud9ServiceRolePolicy` policy\. When you *pass* an IAM role to a service, it allows that service to assume the role and perform actions on your behalf\. In this case, the `PassRole` permission ensures that AWS Cloud9 can pass only the `AWSCloud9SSMAccessRole` role \(and its permission\) to an EC2 instance\. This restricts the actions that can performed on the EC2 instance to only those required by AWS Cloud9\. 

**Note**  
 If you no longer need to use Systems Manager to access an instance, you can delete the `AWSCloud9SSMAccessRole` service role\. For more information, see [Deleting roles or instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html) in the *IAM User Guide*\. 

### Managing instance profiles for Systems Manager with the AWS CLI<a name="aws-cli-instance-profiles"></a>

You can also create a no\-ingress EC2 environment with the AWS CLI\. When you call `create-environment-ec2`, set the `--connection-type` option to `CONNECT_SSM`\.

 If you use this option, the `AWSCloud9SSMAccessRole` service role and `AWSCloud9SSMInstanceProfile` aren't automatically created\. So to create the required service profile and instance profile, do one of the following: 
+ Create an EC2 environment using the console once have the `AWSCloud9SSMAccessRole` service role and `AWSCloud9SSMInstanceProfile` created automatically afterward\. After they're created, the service role and instance profile are available for any additional EC2 Environments created using the AWS CLI\. 
+ Run the following AWS CLI commands to create the service role and instance profile\.

  ```
  aws iam create-role --role-name AWSCloud9SSMAccessRole --path /service-role/ --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{"Effect": "Allow","Principal": {"Service": ["ec2.amazonaws.com","cloud9.amazonaws.com"]      },"Action": "sts:AssumeRole"}]}'
  aws iam attach-role-policy --role-name AWSCloud9SSMAccessRole --policy-arn arn:aws:iam::aws:policy/AWSCloud9SSMInstanceProfile
  aws iam create-instance-profile --instance-profile-name AWSCloud9SSMInstanceProfile --path /cloud9/
  aws iam add-role-to-instance-profile --instance-profile-name AWSCloud9SSMInstanceProfile --role-name AWSCloud9SSMAccessRole
  ```

## Giving users access to instances managed by Session Manager<a name="access-ec2-session"></a>

To open an AWS Cloud9 environment that's connected to an EC2 instance through Systems Manager, a user must have permission for the API operation, `StartSession`\. This operation initiates a connection to the managed EC2 instance for a Session Manager session\. You can give users access by using an AWS Cloud9 specific managed policy \(recommended\) or by editing an IAM policy and adding the necessary permissions\. 


****  

| Method | Description | 
| --- | --- | 
|  Use AWS Cloud9\-specific managed policy  |  We recommend using AWS managed policies to allow users to access EC2 instances managed by Systems Manager\. Managed policies provide a set of permissions for standard AWS Cloud9 use cases and can be easily attached to an IAM entity\. All the managed policies also include the permissions to run the `StartSession` API operation\. The following are managed policies specific to AWS Cloud9: [\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/ec2-ssm.html) For more information, see [AWS managed \(predefined\) policies for AWS Cloud9](how-cloud9-with-iam.md#auth-and-access-control-managed-policies)\.  | 
|  Edit an IAM policy and add required policy statements  |  To edit an existing policy, you can add a permissions for the `StartSession` API\. To edit a policy using the AWS Management Console or AWS CLI, follow the instructions provided by [Editing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/#edit-managed-policy-console) in the *IAM User Guide*\. When editing the policy, add the [policy statement](#policy-statement) \(see the following\) that allows the `ssm:startSession` API operation to run\.  | 

The following permissions enable you to run the `StartSession` API operation\. The `ssm:resourceTag` condition key specifies that a Session Manager session can be started for any instance \(`Resource: arn:aws:ec2:*:*:instance/*`\) on the condition that the instance is an AWS Cloud9 EC2 development environment \(`aws:cloud9:environment`\)\. 

**Note**  
The following managed policies also include these policy statements: `AWSCloud9Administrator`, `AWSCloud9User`, and `AWSCloud9EnvironmentMember`\.

```
{
            "Effect": "Allow",
            "Action": "ssm:StartSession",
            "Resource": "arn:aws:ec2:*:*:instance/*",
            "Condition": {
                "StringLike": {
                    "ssm:resourceTag/aws:cloud9:environment": "*"
                },
                "StringEquals": {
                    "aws:CalledViaFirst": "cloud9.amazonaws.com"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:StartSession"
            ],
            "Resource": [
                "arn:aws:ssm:*:*:document/*"
            ]
        }
```

## Using AWS CloudFormation to create no\-ingress EC2 environments<a name="cfn-role-and-permissions"></a>

When using an [AWS CloudFormation template](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html) to define a no\-ingress Amazon EC2 development environment, do the following before creating the stack:

1. Create the `AWSCloud9SSMAccessRole` service role and `AWSCloud9SSMInstanceProfile` instance profile\. For more information, see [Creating service role and instance profile with an AWS CloudFormation template](#creating-cfn-instance-profile)\.

1. Update the policy for the IAM entity calling AWS CloudFormation so it can start a Session Manager session that connects to the EC2 instance\. For more information, see [Adding Systems Manager permissions to an IAM policy](#updating-IAM-policy)\.

### Creating service role and instance profile with an AWS CloudFormation template<a name="creating-cfn-instance-profile"></a>

You need to create the service role `AWSCloud9SSMAccessRole` and the instance profile `AWSCloud9SSMInstanceProfile` to enable Systems Manager to manage the EC2 instance that backs your development environment\. 

If you've previously created `AWSCloud9SSMAccessRole` and `AWSCloud9SSMInstanceProfile` by creating a no\-ingress EC2 environment [with the console](#using-the-console) or [running AWS CLI commands](#aws-cli-instance-profiles), the service role and instance profile are already available for use\.

**Note**  
If you try to create an AWS CloudFormation stack for a no\-ingress EC2 environment without first creating the required service role and instance profile, the stack isn't created and the following error message is displayed:   
Instance profile AWSCloud9SSMInstanceProfile does not exist in account\.

When creating a no\-ingress EC2 environment for the first time using AWS CloudFormation, you can define the `AWSCloud9SSMAccessRole` and `AWSCloud9SSMInstanceProfile` as IAM resources in the template\.

This excerpt from a sample template shows how you can define these resources\. \(The `AssumeRole` action returns security credentials that provides access to both the AWS Cloud9 environment and its EC2 instance\.\) 

```
AWSTemplateFormatVersion: 2010-09-09
Resources: 
  AWSCloud9SSMAccessRole:
    Type: AWS::IAM::Role
    Properties: 
      AssumeRolePolicyDocument:
        Version: 2012-10-17
        Statement:
          - Effect: Allow
            Principal:
              Service:
              - cloud9.amazonaws.com
              - ec2.amazonaws.com
            Action:
              - 'sts:AssumeRole'
      Description: 'Service linked role for AWS Cloud9'
      Path: '/service-role/'
      ManagedPolicyArns: 
        - arn:aws:iam::aws:policy/AWSCloud9SSMInstanceProfile
      RoleName: 'AWSCloud9SSMAccessRole'

  AWSCloud9SSMInstanceProfile:
    Type: "AWS::IAM::InstanceProfile"
    Properties: 
      InstanceProfileName: AWSCloud9SSMInstanceProfile
      Path: "/cloud9/"
      Roles: 
        - 
          Ref: AWSCloud9SSMAccessRole
```

### Adding Systems Manager permissions to an IAM policy<a name="updating-IAM-policy"></a>

After [defining a service role and instance profile](#creating-cfn-instance-profile) in the [AWS CloudFormation template](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html), you also need to ensure that the IAM entity creating the stack has permission to start a Session Manager session\. \(A session is a connection made to the EC2 instance using Session Manager\.\) 

**Note**  
 If you don't add permissions to start a Session Manager session before creating a stack for a no\-ingress EC2 environment, an `AccessDeniedException` error is returned\.

Add the following permissions to the policy for the IAM entity calling AWS CloudFormation:

```
{
            "Effect": "Allow",
            "Action": "ssm:StartSession",
            "Resource": "arn:aws:ec2:*:*:instance/*",
            "Condition": {
                "StringLike": {
                    "ssm:resourceTag/aws:cloud9:environment": "*"
                },
                "StringEquals": {
                    "aws:CalledViaFirst": "cloudformation.amazonaws.com"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:StartSession"
            ],
            "Resource": [
                "arn:aws:ssm:*:*:document/*"
            ]
        }
```

## Configuring VPC endpoints for private connectivity<a name="configure-no-egress"></a>

When you launch an instance into a subnet with the **access via Systems Manager** option, its security group doesn't have an inbound rule to allow incoming network traffic\. The security group does, however, have an outbound rule that permits outbound traffic from the instance\. This is required to download packages and libraries required to keep the AWS Cloud9 IDE up to date\. 

To prevent outbound as well as inbound traffic for the instance, you need to create and configure Amazon VPC endpoints for Systems Manager\. An interface VPC endpoint \(interface endpoint\) enables you to connect to services powered by [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-service.html), a technology that enables you to privately access Amazon EC2 and Systems Manager APIs by using private IP addresses\. To configure VPC endpoints to use Systems Manager, follow the instructions provided by this [Knowledge Center resource](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-systems-manager-vpc-endpoints/)\.

**Warning**  
If you configure a security group that doesn't permit inbound or outbound networking traffic, the EC2 instance that supports your AWS Cloud9 IDE doesn't have internet access by default\. So, you can't download and install the packages and libraries that ensure your development environment remains up to date\. Moreover, some AWS services, such as AWS Lambda functions, might not work as intended without internet access\.  
With AWS PrivateLink there are data processing charges for each gigabyte processed through the VPC endpoint, regardless of the traffic’s source or destination\. For more information, see [AWS PrivateLink pricing](https://aws.amazon.com/privatelink/pricing/)\.