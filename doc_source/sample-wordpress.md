# WordPress Sample for AWS Cloud9<a name="sample-wordpress"></a>

This sample enables you to run WordPress within an AWS Cloud9 development environment\.

Creating this sample might result in charges to your AWS account\. These include possible charges for services such as Amazon Elastic Compute Cloud \(Amazon EC2\)\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/)\.

**Topics**
+ [Prerequisites](#sample-wordpress-prereqs)
+ [Step 1: Install the Required Tools](#sample-wordpress-install-tools)
+ [Step 2: Set Up MySQL](#sample-wordpress-setup-mysql)
+ [Step 3: Set Up the WordPress Website](#sample-wordpress-setup-wordpress)
+ [Step 4: Share the WordPress website over the internet](#sample-wordpress-share-wordpress)
+ [Step 5: Clean Up](#sample-wordpress-clean-up)

## Prerequisites<a name="sample-wordpress-prereqs"></a>

Before you use this sample, be sure to meet the following requirements\.
+  **You must have an existing AWS Cloud9 EC2 development environment\.** This sample assumes you already have an EC2 environment that is connected to an Amazon EC2 instance running Amazon Linux or Ubuntu Server\. If you have a different type of environment or operating system, you might need to adapt this sample's instructions to set up related tools\. See [Creating an environment in AWS Cloud9](create-environment.md) for details\.
+  **You have the AWS Cloud9 IDE for the existing environment already open\.** When you open an environment, AWS Cloud9 opens the IDE for that environment in your web browser\. See [Opening an environment in AWS Cloud9](open-environment.md) for details\.

## Step 1: Install the Required Tools<a name="sample-wordpress-install-tools"></a>

In this step, you install the following tools, which WordPress depends on:
+ Apache HTTP Server, which hosts WordPress websites\.
+ PHP, which WordPress uses for scripting on the websites\.
+ MySQL, which WordPress uses to store and retrieve information for the websites\.

You then finish this step by starting Apache HTTP Server and MySQL and then installing WordPress\.

1. Ensure that the latest security updates and bug fixes are installed\. To do this, in a terminal session in the AWS Cloud9 IDE, run the ** `yum update` ** for \(Amazon Linux\) or ** `apt update` ** for \(Ubuntu Server\) command\. \(To start a new terminal session, on the menu bar, choose **Window**, **New Terminal**\.\) 

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

1. Download WordPress by running the following command\.

   ```
   wget http://wordpress.org/latest.tar.gz
   ```

1. Install WordPress by running the following command\.

   ```
   tar -xzvf latest.tar.gz
   ```

   If you run the preceding command from the default location in your environment, you can find the WordPress installation files within a folder named `wordpress` in the **Environment** window in the AWS Cloud9 IDE\. You can also get to these files from a terminal session by changing to the following location\.

   For Amazon Linux:

   ```
   cd /home/ec2-user/environment/wordpress/ 
   ```

   For Ubuntu Server:

   ```
   cd /home/ubuntu/environment/wordpress/
   ```

## Step 2: Set Up MySQL<a name="sample-wordpress-setup-mysql"></a>

In this step, you set up MySQL to follow MySQL security best practices\. These security best practices include setting a password for root accounts, removing root accounts that are accessible from outside the local host, removing anonymous user accounts, removing the test database, and removing privileges that permit anyone to access databases with names that start with `test_`\. 

You then finish this step by setting up MySQL to store and retrieve information for a new WordPress website\.

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

1. Start the MySQL command line client as the root user by running the following command\. When prompted, type the root user's password that you set earlier, and then press `Enter`\. \(The prompt changes to `mysql>` while you are in the MySQL command line client\.\)

   ```
   sudo mysql -uroot -p
   ```

1. Create a MySQL database for the WordPress site to use\. To do this, run the following command, replacing *my\_db\_name* with a name for the new database, for example, `mysite`\. \(Be sure to save this database name in a secure location for later use\.\)

   ```
   CREATE DATABASE my_db_name;
   ```

1. Create a MySQL user for the WordPress site to use\. To do this, run the following command, replacing *my\_user\_name* with the user's name \(for example, `wordpress-user`\) and replacing *my\_password* with a password for the user\. \(Be sure to save this user name and password in a secure location for later use\.\)

   ```
   GRANT ALL PRIVILEGES ON *.* TO 'my_user_name'@'localhost' IDENTIFIED BY 'my_password';
   ```

1. Exit the MySQL command line client by running the following command\. \(The prompt changes back to `$`\.\)

   ```
   exit;
   ```

## Step 3: Set Up the WordPress Website<a name="sample-wordpress-setup-wordpress"></a>

In this step, you set up a WordPress website by setting its base configuration details, such as MySQL database connection information\. 

You then finish this step by opening the website and specifying its display title, user name and password, and other settings\.

1. Rename the `wp-config-sample.php` file to `wp-config.php` within the WordPress installation, as follows\.

   1. In the **Environment** window, expand the `wordpress` folder\.

   1. Right\-click the `wp-config-sample.php` file\.

   1. Choose **Rename**\.

   1. Type `wp-config` to rename this file to `wp-config.php`, and then press `Enter`\.

1. Configure the `wp-config.php` file for the WordPress website\. To do this, double\-click the `wp-config.php` file to open it in the editor, replace the following values, and then save and close the file\.
   + Replace *database\_name\_here* with the name of the MySQL database that you created earlier, for example, `mysite`\. 
   + Replace *username\_here* with the name of the MySQL user that you created earlier, for example, `wordpress-user`\. 
   + Replace *password\_here* with the password for the MySQL user that you created earlier\.

   ```
   /** The name of the database for WordPress */
   define( 'DB_NAME', 'database_name_here' );
   
   /** MySQL database username */
   define( 'DB_USER', 'username_here' );
   
   /** MySQL database password */
   define( 'DB_PASSWORD', 'password_here' );
   ```

1. Start the WordPress website\. To do this, double\-click the `index.php` file to open it in the editor\. Then, on the main menu bar, choose **Run**\. The **PHP \(built\-in web server\)** runner starts, which also starts the WordPress website\.
**Note**  
To stop the WordPress website, on this runner tab, choose **Stop**\.

1. View the WordPress website from within the AWS Cloud9 IDE\. To do this, on the main menu bar, choose **Preview, Preview Running Application**\. A new window opens in the IDE and displays a **Not Found** page \(which is expected at this point\)\.

1. Open the WordPress website in a new tab within the same web browser as the AWS Cloud9 IDE\. To do this, on the address bar in the new window, choose **Pop Out Into New Window**\. The new tab displays the same **Not Found** page \(which is still expected at this point\)\.

1. Set the WordPress website's language, user name, password, and other settings\. To do this, in the new tab within the same web browser as the AWS Cloud9 IDE, add `/wordpress/` to the end of the existing URL, and then press `Enter`\. The **WordPress > Installation** webpage is displayed\. Follow the on\-screen instructions to finish specifying the website's settings\.
**Important**  
In the **Information needed** section, for **Username** and **Password**, enter the user name \(for example, `wordpress-user`\) and password of the MySQL user that you set earlier for WordPress to use\.

1. At the end of installation, use the user name and password that you specified to log in to the WordPress website\. Then follow the on\-screen instructions to further customize the website\.

   To return to this dashboard at any time, be sure to add `/wordpress/wp-admin/` to the end of the existing URL, and then press `Enter`\. \(Or, from the website's home page, choose ***My Site's Name*, Dashboard**\)\. 

   To return to the website's home page at any time, be sure to add `/wordpress/` to the end of the existing URL, and then press `Enter`\. \(Or, from the website's dashboard, choose ***My Site's Name*, Visit Site**\)\.

## Step 4: Share the WordPress website over the internet<a name="sample-wordpress-share-wordpress"></a>

In this step, you set up the Apache HTTP Server with recommended ports, file locations, owners, and access permissions for the WordPress website\. 

You then enable incoming web traffic to view that website by setting up the security group in Amazon EC2 and network access control list \(network ACL\) in Amazon Virtual Private Cloud \(Amazon VPC\) that are associated with this EC2 environment\. Each EC2 environment must be associated with both a security group in Amazon EC2 and a network ACL in Amazon VPC\. However, while the default network ACL in an AWS account allows all incoming and outgoing traffic for the environment, the default security group allows only incoming traffic using SSH over port 22\. For more information, see [VPC settings for AWS Cloud9 Development Environments](vpc-settings.md)\.

You then finish this step by successfully viewing the website from outside of the AWS Cloud9 IDE\.

1. Stop the WordPress website\. To do this, on the **PHP \(built\-in web server\)** runner tab in the AWS Cloud9 IDE, choose **Stop**\.

1. Make backup copies of key Apache HTTP Server configuration files that you'll be modifying later in this procedure, in case you accidentally make the original files inoperable\. To do this, run the following file copy commands\.

   For Amazon Linux, run the following single file copy command only:

   ```
   sudo cp /etc/httpd/conf/httpd.conf /etc/httpd/conf/httpd.conf.bak
   ```

   For Ubuntu Server, run the following three file copy commands, one after another in the following order:

   ```
   sudo cp /etc/apache2/ports.conf /etc/apache2/ports.conf.bak
   
   sudo cp /etc/apache2/sites-enabled/000-default.conf /etc/apache2/sites-enabled/000-default.conf.bak
   
   sudo cp /etc/apache2/apache2.conf /etc/apache2/apache2.conf.bak
   ```

1. Bind Apache HTTP Server to port 8080, instead of the default port of 80\. To do this, run the following file search\-and\-replace command\.

   For Amazon Linux:

   ```
   sudo sed -i 's/Listen 80/Listen 8080/g' /etc/httpd/conf/httpd.conf
   ```

   For Ubuntu Server:

   ```
   sudo sed -i 's/Listen 80/Listen 8080/g' /etc/apache2/ports.conf
   ```

1. Add or change virtual host settings to listen on port 8080, instead of the default port of 80\. To do this, run the following file append or search\-and\-replace command\.

   For Amazon Linux, append the virtual host settings to the existing configuration file:

   ```
   sudo echo -e "<VirtualHost *:8080>\n    DocumentRoot /var/www/html\n</VirtualHost>" | sudo tee -a /etc/httpd/conf/httpd.conf
   ```

   For Ubuntu Server, search and replace existing virtual host settings in an existing configuration file:

   ```
   sudo sed -i 's/<VirtualHost \*:80>/<VirtualHost \*:8080>/g' /etc/apache2/sites-enabled/000-default.conf
   ```

1. Restart the Apache HTTP Server to have it use the new settings\. To do this, run the following command\.

   For Amazon Linux \(you might need to run this command twice\):

   ```
   sudo service httpd restart && sudo service httpd status
   ```

   For Ubuntu Server \(to return to the command prompt, press `q`\):

   ```
   sudo service apache2 restart && sudo service apache2 status
   ```

1. View the Apache HTTP Server default information webpage from within the AWS Cloud9 IDE\. To do this, on the main menu bar, choose **Preview, Preview Running Application**\. A new window opens in the IDE and displays the Apache HTTP Server default information webpage\.

1. Now switch the Apache HTTP Server to use the WordPress website's root directory by running the following file search\-and\-replace command\.

   For Amazon Linux:

   ```
   sudo sed -i 's/<Directory "\/var\/www\/html">/<Directory "\/home\/ec2-user\/environment\/wordpress">/g' /etc/httpd/conf/httpd.conf
   ```

   For Ubuntu Server:

   ```
   sudo sed -i 's/<Directory \/var\/www\/>/<Directory \/home\/ubuntu\/environment\/wordpress\/>/g' /etc/apache2/apache2.conf
   ```

1. Switch the Apache HTTP Server to specify using the document root for the WordPress website by running the following file search\-and\-replace command\.

   For Amazon Linux:

   ```
   sudo sed -i 's/DocumentRoot \/var\/www\/html/DocumentRoot \/home\/ec2-user\/environment\/wordpress/g' /etc/httpd/conf/httpd.conf
   ```

   For Ubuntu Server:

   ```
   sudo sed -i 's/DocumentRoot \/var\/www\/html/DocumentRoot \/home\/ubuntu\/environment\/wordpress/g' /etc/apache2/sites-enabled/000-default.conf
   ```

1. Set up the website root with recommended owners and access permissions\. To do this, run the following six commands, one at a time in the following order\. To understand what each command does, read the information after the `#` character after each command\.

   For Amazon Linux:

   ```
   sudo groupadd web-content # Create a group named web-content.
   
   sudo usermod -G web-content -a ec2-user # Add the user ec2-user (your default user for this environment) to the group web-content.
   
   sudo usermod -G web-content -a apache # Add the user apache (Apache HTTP Server) to the group web-content.
   
   sudo chown -R ec2-user:web-content /home/ec2-user/environment/wordpress # Change the owner of /home/ec2-user/environment/wordpress and its files to user ec2-user and group web-content.
   
   sudo find /home/ec2-user/environment/wordpress -type f -exec chmod u=rw,g=rx,o=rx {} \; # Change all file permissions within /home/ec2-user/environment/wordpress to user read/write, group read-only, and others read/execute. 
   
   sudo find /home/ec2-user/environment/wordpress -type d -exec chmod u=rwx,g=rx,o=rx {} \; # Change /home/ec2-user/environment/wordpress directory permissions to user read/write/execute, group read/execute, and others read/execute.
   ```

   For Ubuntu Server:

   ```
   sudo groupadd web-content # Create a group named web-content.
   
   sudo usermod -G web-content -a ubuntu # Add the user ubuntu (your default user for this environment) to the group web-content.
   
   sudo usermod -G web-content -a www-data # Add the user www-data (Apache HTTP Server) to the group web-content.
   
   sudo chown -R ubuntu:web-content /home/ubuntu/environment/wordpress # Change the owner of /home/ubuntu/environment/wordpress and its files to user ubuntu and group web-content.
   
   sudo find /home/ubuntu/environment/wordpress -type f -exec chmod u=rw,g=rx,o=rx {} \; # Change all file permissions within /home/ubuntu/environment/wordpress to user read/write, group read-only, and others read/execute. 
   
   sudo find /home/ubuntu/environment/wordpress -type d -exec chmod u=rwx,g=rx,o=rx {} \; # Change /home/ubuntu/environment/wordpress directory permissions to user read/write/execute, group read/execute, and others read/execute.
   ```

1. Restart the Apache HTTP Server to have it use the new settings\. To do this, run the following command\.

   For Amazon Linux \(you might need to run this command twice\):

   ```
   sudo service httpd restart && sudo service httpd status
   ```

   For Ubuntu Server \(to return to the command prompt, press `q`\):

   ```
   sudo service apache2 restart && sudo service apache2 status
   ```

1. View the WordPress website from within the AWS Cloud9 IDE\. To do this, on the main menu bar, choose **Preview, Preview Running Application**\. A new window opens in the IDE and displays a **Not Found** page \(which is expected at this point\)\.

1. Open the WordPress website in a new tab within the same web browser as the AWS Cloud9 IDE\. To do this, on the address bar in the new window, choose **Pop Out Into New Window**\. The new tab displays the same **Not Found** page \(which is still expected at this point\)\.

1. In the new tab within the same web browser as the AWS Cloud9 IDE, add `/index.php` to the end of the existing URL, and then press `Enter`\. The WordPress website's home page is displayed\.

1. Enable incoming web traffic over port 8080 to view the new webpage by setting up the network ACL in Amazon VPC and the security group Amazon EC2 that is associated with this EC2 environment\. To do this, run the following eight commands, one at a time in the following order\. To understand what each command does, read the information after the `#` character for each command\.
**Important**  
Running the following commands enables incoming web traffic over port 8080 for **all** EC2 environments and Amazon EC2 instances that are associated with the security group and network ACL for this environment\. This might result in unexpectedly enabling incoming web traffic over port 8080 for EC2 environments and Amazon EC2 instances other than this one\.
**Note**  
The following second through fourth commands enable the security group to allow incoming web traffic over port 8080\. If you have a default security group, which only allows incoming SSH traffic over port 22, then you must run the first command followed by these second through fourth commands\. However, if you have a custom security group already allows incoming web traffic over port 8080, you can safely skip running those commands\.  
The following fifth through eighth commands enable the network ACL to allow incoming web traffic over port 8080\. If you have a default network ACL, which already allows all incoming traffic over all ports, then you can safely skip running those commands\. However, if you have a custom network ACL that doesn't allow incoming web traffic over port 80, then you must run the first command followed by these fifth through eighth commands\. 

   ```
   MY_INSTANCE_ID=$(curl http://169.254.169.254/latest/meta-data/instance-id) # Get the ID of the instance for the environment, and store it temporarily.
              
   MY_SECURITY_GROUP_ID=$(aws ec2 describe-instances --instance-id $MY_INSTANCE_ID --query 'Reservations[].Instances[0].SecurityGroups[0].GroupId' --output text) # Get the ID of the security group associated with the instance, and store it temporarily.
   
   aws ec2 authorize-security-group-ingress --group-id $MY_SECURITY_GROUP_ID --protocol tcp --cidr 0.0.0.0/0 --port 8080 # Add an inbound rule to the security group to allow all incoming IPv4-based traffic over port 8080.
   
   aws ec2 authorize-security-group-ingress --group-id $MY_SECURITY_GROUP_ID --ip-permissions IpProtocol=tcp,Ipv6Ranges='[{CidrIpv6=::/0}]',FromPort=8080,ToPort=8080 # Add an inbound rule to the security group to allow all incoming IPv6-based traffic over port 8080.
   
   MY_SUBNET_ID=$(aws ec2 describe-instances --instance-id $MY_INSTANCE_ID --query 'Reservations[].Instances[0].SubnetId' --output text) # Get the ID of the subnet associated with the instance, and store it temporarily.
   
   MY_NETWORK_ACL_ID=$(aws ec2 describe-network-acls --filters Name=association.subnet-id,Values=$MY_SUBNET_ID --query 'NetworkAcls[].Associations[0].NetworkAclId' --output text) # Get the ID of the network ACL associated with the subnet, and store it temporarily.
   
   aws ec2 create-network-acl-entry --network-acl-id $MY_NETWORK_ACL_ID --ingress --protocol tcp --rule-action allow --rule-number 10000 --cidr-block 0.0.0.0/0 --port-range From=8080,To=8080 # Add an inbound rule to the network ACL to allow all IPv4-based traffic over port 8080. Advanced users: change this suggested rule number as desired.
   
   aws ec2 create-network-acl-entry --network-acl-id $MY_NETWORK_ACL_ID --ingress --protocol tcp --rule-action allow --rule-number 10100 --ipv6-cidr-block ::/0 --port-range From=8080,To=8080 # Add an inbound rule to the network ACL to allow all IPv6-based traffic over port 8080. Advanced users: change this suggested rule number as desired.
   ```

1. Get the URL to the `index.php` file within the web server root\. To do this, run the following command, and use a new web browser tab or a different web browser separate from the AWS Cloud9 IDE to go to the URL that is displayed\. If successful, the webpage displays the WordPress website home page\.

   ```
   MY_PUBLIC_IP=$(curl http://169.254.169.254/latest/meta-data/public-ipv4) && echo http://$MY_PUBLIC_IP:8080/index.php # Get the URL to the index.php file within the web server root.
   ```

## Step 5: Clean Up<a name="sample-wordpress-clean-up"></a>

If you want to keep using this environment but you want to disable incoming web traffic over port 8080, then run the following eight commands, one at a time in the following order, to delete the corresponding incoming traffic rules that you set earlier in the security group and network ACL that are associated with the environment\. To understand what each command does, read the information after the `#` character for each command\.

**Important**  
Running the following commands disables incoming web traffic over port 8080 for **all** EC2 environments and Amazon EC2 instances that are associated with the security group and network ACL for this environment\. This might result in unexpectedly disabling incoming web traffic over port 8080 for EC2 environments and Amazon EC2 instances other than this one\.

**Note**  
The following fifth through eighth commands remove existing rules in order to block the network ACL from allowing incoming web traffic over port 8080\. If you have a default network ACL, which already allows all incoming traffic over all ports, then you can safely skip running those commands\. However, if you have a custom network ACL with existing rules that allow incoming web traffic over port 8080 and you want to delete those rules, then you must run the first command followed by these fifth through eighth commands\. 

```
MY_INSTANCE_ID=$(curl http://169.254.169.254/latest/meta-data/instance-id) # Get the ID of the instance for the environment, and store it temporarily.
           
MY_SECURITY_GROUP_ID=$(aws ec2 describe-instances --instance-id $MY_INSTANCE_ID --query 'Reservations[].Instances[0].SecurityGroups[0].GroupId' --output text) # Get the ID of the security group associated with the instance, and store it temporarily.

aws ec2 revoke-security-group-ingress --group-id $MY_SECURITY_GROUP_ID --protocol tcp --cidr 0.0.0.0/0 --port 8080 # Delete the existing inbound rule from the security group to block all incoming IPv4-based traffic over port 8080.

aws ec2 revoke-security-group-ingress --group-id $MY_SECURITY_GROUP_ID --ip-permissions IpProtocol=tcp,Ipv6Ranges='[{CidrIpv6=::/0}]',FromPort=8080,ToPort=8080 # Delete the existing inbound rule from the security group to block all incoming IPv6-based traffic over port 8080.

MY_SUBNET_ID=$(aws ec2 describe-instances --instance-id $MY_INSTANCE_ID --query 'Reservations[].Instances[0].SubnetId' --output text) # Get the ID of the subnet associated with the instance, and store it temporarily.

MY_NETWORK_ACL_ID=$(aws ec2 describe-network-acls --filters Name=association.subnet-id,Values=$MY_SUBNET_ID --query 'NetworkAcls[].Associations[0].NetworkAclId' --output text) # Get the ID of the network ACL associated with the subnet, and store it temporarily.

aws ec2 delete-network-acl-entry --network-acl-id $MY_NETWORK_ACL_ID --ingress --rule-number 10000 # Delete the existing inbound rule from the network ACL to block all IPv4-based traffic over port 8080. Advanced users: if you originally created this rule with a different number, change this suggested rule number to match.

aws ec2 delete-network-acl-entry --network-acl-id $MY_NETWORK_ACL_ID --ingress --rule-number 10100 # Delete the existing inbound rule from the network ACL to block all IPv6-based traffic over port 8080. Advanced users: if you originally created this rule with a different number, change this suggested rule number to match.
```

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the environment\. For instructions, see [Deleting an environment in AWS Cloud9](delete-environment.md)\.