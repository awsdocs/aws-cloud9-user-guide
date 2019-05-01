# WordPress Sample for AWS Cloud9<a name="sample-wordpress"></a>

This sample enables you to run WordPress within an AWS Cloud9 development environment\.

Creating this sample might result in charges to your AWS account\. These include possible charges for services such as Amazon Elastic Compute Cloud \(Amazon EC2\)\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/)\.

**Topics**
+ [Prerequisites](#sample-wordpress-prereqs)
+ [Step 1: Install the Required Tools](#sample-wordpress-install-tools)
+ [Step 2: Set Up MySQL](#sample-wordpress-setup-mysql)
+ [Step 3: Set Up the WordPress Website](#sample-wordpress-setup-wordpress)
+ [Step 4: Clean Up](#sample-wordpress-clean-up)

## Prerequisites<a name="sample-wordpress-prereqs"></a>

Before you use this sample, be sure to meet the following requirements\.
+  **You must have an existing AWS Cloud9 EC2 development environment\.** This sample assumes you already have an EC2 environment that is connected to an Amazon EC2 instance running Amazon Linux or Ubuntu Server\. If you have a different type of environment or operating system, you might need to adapt this sample's instructions to set up related tools\. See [Creating an Environment in AWS Cloud9](create-environment.md) for details\.
+  **You have the AWS Cloud9 IDE for the existing environment already open\.** When you open an environment, AWS Cloud9 opens the IDE for that environment in your web browser\. See [Opening an Environment in AWS Cloud9](open-environment.md) for details\.

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

1. Start the MySQL command\-line client as the root user by running the following command\. When prompted, type the root user's password that you set earlier, and then press `Enter`\. \(The prompt changes to `mysql>` while you are in the MySQL command\-line client\.\)

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

1. Exit the MySQL command\-line client by running the following command\. \(The prompt changes back to `$`\.\)

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

## Step 4: Clean Up<a name="sample-wordpress-clean-up"></a>

To prevent ongoing charges to your AWS account after you're done using this sample, you should delete the environment\. For instructions, see [Deleting an Environment in AWS Cloud9](delete-environment.md)\.