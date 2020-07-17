# LAMP Sample for AWS Cloud9<a name="sample-lamp"></a>

This sample enables you to set up and run LAMP \(Linux, Apache HTTP Server, MySQL, and PHP\) within an AWS Cloud9 development environment\.

Creating this sample might result in charges to your AWS account\. These include possible charges for services such as Amazon Elastic Compute Cloud \(Amazon EC2\)\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/)\.

**Topics**
+ [Prerequisites](#sample-lamp-prereqs)
+ [Step 1: Install the Tools](#sample-lamp-install-tools)
+ [Step 2: Set Up MySQL](#sample-lamp-setup-mysql)
+ [Step 3: Set Up a Website](#sample-lamp-apache)
+ [Step 4: Clean Up](#sample-lamp-clean-up)

## Prerequisites<a name="sample-lamp-prereqs"></a>

Before you use this sample, be sure to meet the following requirements\.
+  **You must have an existing AWS Cloud9 EC2 development environment\.** This sample assumes you already have an EC2 environment that is connected to an Amazon EC2 instance running Amazon Linux or Ubuntu Server\. If you have a different type of environment or operating system, you might need to adapt this sample's instructions to set up related tools\. See [Creating an Environment in AWS Cloud9](create-environment.md) for details\.
+  **You have the AWS Cloud9 IDE for the existing environment already open\.** When you open an environment, AWS Cloud9 opens the IDE for that environment in your web browser\. See [Opening an environment in AWS Cloud9](open-environment.md) for details\.

## Step 1: Install the Tools<a name="sample-lamp-install-tools"></a>

In this step, you install the following tools:
+ Apache HTTP Server, a web server host\.
+ PHP, a scripting language that is especially suited for web development and can be embedded into HTML\. 
+ MySQL, a database management system\.

You then finish this step by starting Apache HTTP Server and then MySQL\.

1. Ensure that the latest security updates and bug fixes are installed on the instance\. To do this, in a terminal session in the AWS Cloud9 IDE, run the ** `yum update` ** for \(Amazon Linux\) or ** `apt update` ** for \(Ubuntu Server\) command\. \(To start a new terminal session, on the menu bar, choose **Window**, **New Terminal**\.\) 

   For Amazon Linux:

   ```
   sudo yum -y update
   ```

   For Ubuntu Server:

   ```
   sudo apt -y update
   ```

1. Check whether Apache HTTP Server is already installed\. To do this, run the ** `httpd -v`** \(for Amazon Linux\) or **`apache2 -v`** \(for Ubuntu Server\) command\. 

   If successful, the output contains the Apache HTTP Server version number\. 

   If you see an error, then install Apache HTTP Server by running the ** `install` ** command\.

   For Amazon Linux:

   ```
   sudo yum install -y httpd24
   ```

   For Ubuntu Server:

   ```
   sudo apt install -y apache2
   ```

1. Confirm whether PHP is already installed by running the ** `php -v` ** command\. 

   If successful, the output contains the PHP version number\. 

   If you see an error, then install PHP by running the ** `install` ** command\.

   For Amazon Linux:

   ```
   sudo yum install -y php56
   ```

   For Ubuntu Server:

   ```
   sudo apt install -y php libapache2-mod-php php-xml
   ```

1. Confirm whether MySQL is already installed by running the ** `mysql --version` ** command\. 

   If successful, the output contains the MySQL version number\. 

   If you see an error, then install MySQL by running the ** `install` ** command\.

   For Amazon Linux:

   ```
   sudo yum install -y mysql-server
   ```

   For Ubuntu Server:

   ```
   sudo apt install -y mysql-server
   ```

1. After you install Apache HTTP Server, PHP, and MySQL, start Apache HTTP Server, and then confirm it has started, by running the following command\.

   For Amazon Linux \(you might need to run this command twice\):

   ```
   sudo service httpd start && sudo service httpd status
   ```

   For Ubuntu Server \(to return to the command prompt, press `q`\):

   ```
   sudo service apache2 start && sudo service apache2 status
   ```

1. Start MySQL, and then confirm it has started, by running the following command\.

   For Amazon Linux:

   ```
   sudo service mysqld start && sudo service mysqld status
   ```

   For Ubuntu Server \(to return to the command prompt, press `q`\):

   ```
   sudo service mysql start && sudo service mysql status
   ```

## Step 2: Set Up MySQL<a name="sample-lamp-setup-mysql"></a>

In this step, you set up MySQL to follow MySQL security best practices\. These security best practices include setting a password for root accounts, removing root accounts that are accessible from outside the local host, removing anonymous user accounts, removing the test database, and removing privileges that permit anyone to access databases with names that start with `test_`\. 

You then finish this step by practicing the starting and then exiting of the MySQL command\-line client\.

1. Implement MySQL security best practices for the MySQL installation by running the following command in a terminal session in the AWS Cloud9 IDE\.

   ```
   sudo mysql_secure_installation
   ```

1. When prompted, answer the following questions as specified\.

   For Amazon Linux: 

   1. **Enter current password for root \(enter for none\)** – Press `Enter` \(for no password\)\.

   1. **Set root password** – Type `Y`, and then press `Enter`\.

   1. **New password** – Type a password, and then press `Enter`\.

   1. **Re\-enter new password** – Type the password again, and then press `Enter`\. \(Be sure to store the password in a secure location for later use\.\)

   1. **Remove anonymous users** – Type `Y`, and then press `Enter`\.

   1. **Disallow root login remotely** – Type `Y`, and then press `Enter`\.

   1. **Remove test database and access to it** – Type `Y`, and then press `Enter`\.

   1. **Reload privilege tables now** – Type `Y`, and then press `Enter`\.

   For Ubuntu Server:

   1. **Would you like to setup VALIDATE PASSWORD plugin** – Type `y`, and then press `Enter`\.

   1. **There are three levels of password validation policy** – Type `0`, `1`, or `2`, and then press `Enter`\.

   1. **New password** – Type a password, and then press `Enter`\.

   1. **Re\-enter new password** – Type the password again, and then press `Enter`\. \(Be sure to store the password in a secure location for later use\.\)

   1. **Do you wish to continue with the password provided** – Type `y`, and then press `Enter`\.

   1. **Remove anonymous users** – Type `y`, and then press `Enter`\.

   1. **Disallow root login remotely** – Type `y`, and then press `Enter`\.

   1. **Remove test database and access to it** – Type `y`, and then press `Enter`\.

   1. **Reload privilege tables now** – Type `y`, and then press `Enter`\.

1. To interact directly with MySQL, start the MySQL command\-line client as the root user by running the following command\. When prompted, type the root user's password that you set earlier, and then press `Enter`\. \(The prompt changes to `mysql>` while you are in the MySQL command\-line client\.\)

   ```
   sudo mysql -uroot -p
   ```

1. To exit the MySQL command\-line client, run the following command\. \(The prompt changes back to `$`\.\)

   ```
   exit;
   ```

## Step 3: Set Up a Website<a name="sample-lamp-apache"></a>

In this step, you set up the default website root for the Apache HTTP Server with recommended owners and access permissions\. You then create a PHP\-based webpage within that default website root\. 

You then enable incoming web traffic to view that webpage by setting up the security group in Amazon EC2 and network access control list \(network ACL\) in Amazon Virtual Private Cloud \(Amazon VPC\) that are associated with this EC2 environment\. Each EC2 environment must be associated with both a security group in Amazon EC2 and a network ACL in Amazon VPC\. However, while the default network ACL in an AWS account allows all incoming and outgoing traffic for the environment, the default security group allows only incoming traffic using SSH over port 22\. For more information, see [VPC settings for AWS Cloud9 Development Environments](vpc-settings.md)\.

You then finish this step by successfully viewing the webpage from outside of the AWS Cloud9 IDE\.

1. Set up the default website root for the Apache HTTP Server \(`/var/www/html`\) with recommended owners and access permissions\. To do this, run the following six commands, one at a time in the following order, in a terminal session in the AWS Cloud9 IDE\. To understand what each command does, read the information after the `#` character after each command\.

   For Amazon Linux:

   ```
   sudo groupadd web-content # Create a group named web-content.
   
   sudo usermod -G web-content -a ec2-user # Add the user ec2-user (your default user for this environment) to the group web-content.
   
   sudo usermod -G web-content -a apache # Add the user apache (Apache HTTP Server) to the group web-content.
   
   sudo chown -R ec2-user:web-content /var/www/html # Change the owner of /var/www/html and its files to user ec2-user and group web-content.
   
   sudo find /var/www/html -type f -exec chmod u=rw,g=rx,o=rx {} \; # Change all file permissions within /var/www/html to user read/write, group read-only, and others read/execute. 
   
   sudo find /var/www/html -type d -exec chmod u=rwx,g=rx,o=rx {} \; # Change /var/www/html directory permissions to user read/write/execute, group read/execute, and others read/execute.
   ```

   For Ubuntu Server:

   ```
   sudo groupadd web-content # Create a group named web-content.
   
   sudo usermod -G web-content -a ubuntu # Add the user ubuntu (your default user for this environment) to the group web-content.
   
   sudo usermod -G web-content -a www-data # Add the user www-data (Apache HTTP Server) to the group web-content.
   
   sudo chown -R ubuntu:web-content /var/www/html # Change the owner of /var/www/html and its files to user ubuntu and group web-content.
   
   sudo find /var/www/html -type f -exec chmod u=rw,g=rx,o=rx {} \; # Change all file permissions within /var/www/html to user read/write, group read-only, and others read/execute. 
   
   sudo find /var/www/html -type d -exec chmod u=rwx,g=rx,o=rx {} \; # Change /var/www/html directory permissions to user read/write/execute, group read/execute, and others read/execute.
   ```

1. Create a PHP\-based webpage named `index.php` in the default website root folder for the Apache HTTP Server \(which is `/var/www/html`\) by running the following command\.

   For Amazon Linux:

   ```
   sudo touch /var/www/html/index.php && sudo chown -R ec2-user:web-content /var/www/html/index.php && sudo chmod u=rw,g=rx,o=rx /var/www/html/index.php && sudo printf '%s\n%s\n%s' '<?php' '  phpinfo();' '?>' >> /var/www/html/index.php
   ```

   The preceding command for Amazon Linux also changes the file's owner to `ec2-user`, changes the file's group to `web-content`, and changes the file's permissions to read/write for the user, and read/execute for the group and others\. 

   For Ubuntu Server:

   ```
   sudo touch /var/www/html/index.php && sudo chown -R ubuntu:web-content /var/www/html/index.php && sudo chmod u=rw,g=rx,o=rx /var/www/html/index.php && sudo printf '%s\n%s\n%s' '<?php' '  phpinfo();' '?>' >> /var/www/html/index.php
   ```

   The preceding command for Ubuntu Server also changes the file's owner to `ubuntu`, changes the file's group to `web-content`, and changes the file's permissions to read/write for the user, and read/execute for the group and others\. 

   If successful, the preceding commands create the `index.php` file with the following contents\.

   ```
   <?php
     phpinfo();
   ?>
   ```

1. Enable incoming web traffic over port 80 to view the new webpage by setting up the network ACL in Amazon VPC and the security group Amazon EC2 that is associated with this EC2 environment\. To do this, run the following eight commands, one at a time in the following order\. To understand what each command does, read the information after the `#` character for each command\.
**Important**  
Running the following commands enables incoming web traffic over port 80 for **all** EC2 environments and Amazon EC2 instances that are associated with the security group and network ACL for this environment\. This might result in unexpectedly enabling incoming web traffic over port 80 for EC2 environments and Amazon EC2 instances other than this one\.
**Note**  
The following second through fourth commands enable the security group to allow incoming web traffic over port 80\. If you have a default security group, which only allows incoming SSH traffic over port 22, then you must run the first command followed by these second through fourth commands\. However, if you have a custom security group already allows incoming web traffic over port 80, you can safely skip running those commands\.  
The following fifth through eighth commands enable the network ACL to alow incoming web traffic over port 80\. If you have a default network ACL, which already allows all incoming traffic over all ports, then you can safely skip running those commands\. However, if you have a custom network ACL that doesn't allow incoming web traffic over port 80, then you must run the first command followed by these fifth through eighth commands\. 

   ```
   MY_INSTANCE_ID=$(curl http://169.254.169.254/latest/meta-data/instance-id) # Get the ID of the instance for the environment, and store it temporarily.
              
   MY_SECURITY_GROUP_ID=$(aws ec2 describe-instances --instance-id $MY_INSTANCE_ID --query 'Reservations[].Instances[0].SecurityGroups[0].GroupId' --output text) # Get the ID of the security group associated with the instance, and store it temporarily.
   
   aws ec2 authorize-security-group-ingress --group-id $MY_SECURITY_GROUP_ID --protocol tcp --cidr 0.0.0.0/0 --port 80 # Add an inbound rule to the security group to allow all incoming IPv4-based traffic over port 80.
   
   aws ec2 authorize-security-group-ingress --group-id $MY_SECURITY_GROUP_ID --ip-permissions IpProtocol=tcp,Ipv6Ranges='[{CidrIpv6=::/0}]',FromPort=80,ToPort=80 # Add an inbound rule to the security group to allow all incoming IPv6-based traffic over port 80.
   
   MY_SUBNET_ID=$(aws ec2 describe-instances --instance-id $MY_INSTANCE_ID --query 'Reservations[].Instances[0].SubnetId' --output text) # Get the ID of the subnet associated with the instance, and store it temporarily.
   
   MY_NETWORK_ACL_ID=$(aws ec2 describe-network-acls --filters Name=association.subnet-id,Values=$MY_SUBNET_ID --query 'NetworkAcls[].Associations[0].NetworkAclId' --output text) # Get the ID of the network ACL associated with the subnet, and store it temporarily.
   
   aws ec2 create-network-acl-entry --network-acl-id $MY_NETWORK_ACL_ID --ingress --protocol tcp --rule-action allow --rule-number 10000 --cidr-block 0.0.0.0/0 --port-range From=80,To=80 # Add an inbound rule to the network ACL to allow all IPv4-based traffic over port 80. Advanced users: change this suggested rule number as desired.
   
   aws ec2 create-network-acl-entry --network-acl-id $MY_NETWORK_ACL_ID --ingress --protocol tcp --rule-action allow --rule-number 10100 --ipv6-cidr-block ::/0 --port-range From=80,To=80 # Add an inbound rule to the network ACL to allow all IPv6-based traffic over port 80. Advanced users: change this suggested rule number as desired.
   ```

1. Get the URL to the `index.php` file within the web server root\. To do this, run the following command, and use a new web browser tab or a different web browser separate from the AWS Cloud9 IDE to go to the URL that is displayed\. If successful, the webpage displays information about Apache HTTP Server, MySQL, PHP, and other related settings\.

   ```
   MY_PUBLIC_IP=$(curl http://169.254.169.254/latest/meta-data/public-ipv4) && echo http://$MY_PUBLIC_IP/index.php # Get the URL to the index.php file within the web server root.
   ```

## Step 4: Clean Up<a name="sample-lamp-clean-up"></a>

If you want to keep using this environment but you want to disable incoming web traffic over port 80, then run the following eight commands, one at a time in the following order, to delete the corresponding incoming traffic rules that you set earlier in the security group and network ACL that are associated with the environment\. To understand what each command does, read the information after the `#` character for each command\.

**Important**  
Running the following commands disables incoming web traffic over port 80 for **all** EC2 environments and Amazon EC2 instances that are associated with the security group and network ACL for this environment\. This might result in unexpectedly disabling incoming web traffic over port 80 for EC2 environments and Amazon EC2 instances other than this one\.

**Note**  
The following fifth through eighth commands remove existing rules in order to block the network ACL from allowing incoming web traffic over port 80\. If you have a default network ACL, which already allows all incoming traffic over all ports, then you can safely skip running those commands\. However, if you have a custom network ACL with existing rules that allow incoming web traffic over port 80 and you want to delete those rules, then you must run the first command followed by these fifth through eighth commands\. 

```
MY_INSTANCE_ID=$(curl http://169.254.169.254/latest/meta-data/instance-id) # Get the ID of the instance for the environment, and store it temporarily.
           
MY_SECURITY_GROUP_ID=$(aws ec2 describe-instances --instance-id $MY_INSTANCE_ID --query 'Reservations[].Instances[0].SecurityGroups[0].GroupId' --output text) # Get the ID of the security group associated with the instance, and store it temporarily.

aws ec2 revoke-security-group-ingress --group-id $MY_SECURITY_GROUP_ID --protocol tcp --cidr 0.0.0.0/0 --port 80 # Delete the existing inbound rule from the security group to block all incoming IPv4-based traffic over port 80.

aws ec2 revoke-security-group-ingress --group-id $MY_SECURITY_GROUP_ID --ip-permissions IpProtocol=tcp,Ipv6Ranges='[{CidrIpv6=::/0}]',FromPort=80,ToPort=80 # Delete the existing inbound rule from the security group to block all incoming IPv6-based traffic over port 80.

MY_SUBNET_ID=$(aws ec2 describe-instances --instance-id $MY_INSTANCE_ID --query 'Reservations[].Instances[0].SubnetId' --output text) # Get the ID of the subnet associated with the instance, and store it temporarily.

MY_NETWORK_ACL_ID=$(aws ec2 describe-network-acls --filters Name=association.subnet-id,Values=$MY_SUBNET_ID --query 'NetworkAcls[].Associations[0].NetworkAclId' --output text) # Get the ID of the network ACL associated with the subnet, and store it temporarily.

aws ec2 delete-network-acl-entry --network-acl-id $MY_NETWORK_ACL_ID --ingress --rule-number 10000 # Delete the existing inbound rule from the network ACL to block all IPv4-based traffic over port 80. Advanced users: if you originally created this rule with a different number, change this suggested rule number to match.

aws ec2 delete-network-acl-entry --network-acl-id $MY_NETWORK_ACL_ID --ingress --rule-number 10100 # Delete the existing inbound rule from the network ACL to block all IPv6-based traffic over port 80. Advanced users: if you originally created this rule with a different number, change this suggested rule number to match.
```

If you are done using this environment, you should delete it to prevent ongoing charges to your AWS account\. For instructions, see [Deleting an Environment in AWS Cloud9](delete-environment.md)\.