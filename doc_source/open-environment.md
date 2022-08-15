# Opening an environment in AWS Cloud9<a name="open-environment"></a>

This procedure describes how to open an environment in AWS Cloud9\.

**Note**  
This procedure assumes you have already created an AWS Cloud9 development environment\. To create an environment, see [Creating an Environment](create-environment.md)\.

1. Sign in to the AWS Cloud9 console as follows:
   + If you're the only one using your AWS account or you're an IAM user in a single AWS account, go to [https://console\.aws\.amazon\.com/cloud9/](https://console.aws.amazon.com/cloud9/)\.
   + If your organization uses AWS IAM Identity Center \(successor to AWS Single Sign\-On\), ask your AWS account administrator for sign\-in instructions\.
**Important**  
If you [sign out of your AWS Account](https://aws.amazon.com/premiumsupport/knowledge-center/sign-out-account/), the AWS Cloud9 IDE can still be accessed for up to five minutes afterwards\. Access is then denied when the required permissions expire\.

1. In the top navigation bar, choose the AWS Region where the environment is located\.  
![\[AWS Region selector in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-region.png)

1. In the list of environments, for the environment that you want to open, do one of the following actions\.
   + Inside of the card, choose the **Open IDE** link\.  
![\[Choosing an environment using the Open IDE link\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/open-environment-context.png)
   + Select the card, and then choose the **Open IDE** button\.  
![\[Choosing an environment using the Open IDE button\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-open-ide-card.png)

If your environment isn't displayed in the console, try doing one or more of the following actions to have it be displayed\.
+ In the side navigation bar, choose one or more of the following\.
  + Choose **Your environments** to display all environments that your AWS entity owns within the selected AWS Region and AWS account\.
  + Choose **Shared with you** to display all environments your AWS entity has been invited to within the selected AWS Region and AWS account\.
  + Choose **Account environments** to display all environments within the selected AWS Region and AWS account that your AWS entity has permissions to display\.  
![\[Environment list scope in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-env-list.png)
+ Choose the previous arrow, next arrow, or page number button to display more environments in the current scope\.  
![\[Environment list page control in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-find-env.png)
+ If you think you should be a member of an environment, but the environment isn't displayed in the **Shared with you** list, check with the environment owner\.
+ In the top navigation bar, choose a different AWS Region\.  
![\[AWS Region selector in the AWS Cloud9 console\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-region.png)