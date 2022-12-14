# Installing WordPress for AWS Cloud9<a name="sample-wordpress"></a>

This sample enables you to run WordPress within an AWS Cloud9 development environment\. WordPress is an open\-source content management system \(CMS\) that's widely used for the delivery web content\. 

**Note**  
Creating this sample might result in charges to your AWS account\. These include possible charges for services such as Amazon Elastic Compute Cloud \(Amazon EC2\)\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/)\.

## Prerequisites<a name="sample-wordpress-prereqs"></a>

Before you use this sample, make sure your setup meets the following requirements:
+  **You must have an existing AWS Cloud9 EC2 development environment\.** This sample assumes you already have an EC2 environment that is connected to an Amazon EC2 instance running Amazon Linux or Ubuntu Server\. If you have a different type of environment or operating system, you might need to adapt this sample's instructions to set up related tools\. See [Creating an environment in AWS Cloud9](create-environment.md) for details\.
+  **You have the AWS Cloud9 IDE for the existing environment already open\.** When you open an environment, AWS Cloud9 opens the IDE for that environment in your web browser\. See [Opening an environment in AWS Cloud9](open-environment.md) for details\.
+ **You have an up\-to\-date EC2 instance with all the latest software packages**\. In the AWS Cloud9 IDE terminal window, you can run `yum update` with the `-y` option to install updates without asking for confirmation\. If you would like to examine the updates before installing, you can omit this option\. 

  ```
  sudo yum update -y
  ```

## Installation overview<a name="task-overview"></a>

Installing WordPress on your environment's EC2 instance involves the following steps:

1. Installing and configuring MariaDB Server, which is an open\-source relational database that stores information for WordPress installations 

1. Installing and configuring WordPress, which includes editing the `wordpress.conf` configuration file

1. Configuring the Apache server that hosts the WordPress site

1. Previewing the WordPress web content that's hosted by the Apache server

## Step 1: Installing and configuring MariaDB Server<a name="wp-install-configure-mariadb"></a>

1. In the AWS Cloud9 IDE, choose **Window**, **New Terminal** and enter the following commands to install and start a MariaDB Server installation:

   ```
   sudo yum install -y mariadb-server
   sudo systemctl start mariadb
   ```

1. Next, run the `mysql_secure_installation` script to improve the security of your MariaDB Server installation\. 

   When providing responses to the script, press **Enter** for the first question to keep the root password blank\. Press **n** for `Set root password?` and then **y** for each of the rest of the security options\.

   ```
   mysql_secure_installation
   ```

1. Now create a database table to store WordPress information using the MariaDB client\.

   \(Press **Enter** when asked for your password\.\)

   ```
   sudo mysql -u root -p
   MariaDB [(none)]> create database wp_test;
   MariaDB [(none)]> grant all privileges on wp_test.* to wp_user@localhost identified by 'YourSecurePassword';
   ```

1. To log out of the MariaDB client, run the `exit` command\.

## Step 2: Installing and configuring WordPress<a name="wp-install-configure-wordpress"></a>

1. In the IDE terminal window, navigate to the `environment` directory and then create the directories `config` and `wordpress`\. Then run the `touch` command to create a file called `wordpress.conf` in the `config` directory:

   ```
   cd /home/ec2-user/environment
   mkdir config wordpress
   touch config/wordpress.conf
   ```

1. Use the IDE editor or vim to update `wordpress.conf` with host configuration information that allows the Apache server to serve WordPress content:

   ```
   # Ensure that Apache listens on port 80
   Listen 8080
   <VirtualHost *:8080>
       DocumentRoot "/var/www/wordpress"
       ServerName www.example.org
       # Other directives here
   </VirtualHost>
   ```

1. Now run the following commands to retrieve the required archive file and install WordPress: 

   ```
   cd /home/ec2-user/environment
   wget https://wordpress.org/latest.tar.gz
   tar xvf latest.tar.gz
   ```

1. Run the `touch` command to create a file called `wp-config-sample.php` in the `environment/wordpress` directory:

   ```
   touch wordpress/wp-config-sample.php
   ```

1. Use the IDE editor or vim to update `wp-config-sample.php` to `wp-config.php` then replace the sample data with your setup: 

   ```
   // ** MySQL settings - You can get this info from your web host ** //
   /** The name of the database for WordPress */
   define( 'DB_NAME', 'wp_test' );
   
   /** MySQL database username */
   define( 'DB_USER', 'wp_user' );
   
   /** MySQL database password */
   define( 'DB_PASSWORD', 'YourSecurePassword' );
   
   /** MySQL hostname */
   define( 'DB_HOST', 'localhost' );
   
   /** Database Charset to use in creating database tables. */
   define( 'DB_CHARSET', 'utf8' );
   
   /** The Database Collate type. Don't change this if in doubt. */
   define( 'DB_COLLATE', '' );
   
   define('FORCE_SSL', true);
   
   if ($_SERVER['HTTP_X_FORWARDED_PROTO'] == 'https') $_SERVER['HTTPS'] = 'on';
   ```

## Step 3: Configuring your Apache HTTP Server<a name="wp-install-configure-apache"></a>

1. In the AWS Cloud9 IDE terminal window, make sure that you have Apache installed: 

   ```
   httpd -v
   ```

   If the Apache server isn't installed, run the following command:

   ```
   sudo yum install -y httpd 
   ```

1. Navigate to the `/etc/httpd/conf.d` directory, which is the location for Apache's virtual host configuration files\. Then use the `ln` command to link the `wordpress.conf` you created earlier to the current working directory \(`/etc/httpd/conf.d`\):

   ```
   cd /etc/httpd/conf.d
   sudo ln -s /home/ec2-user/environment/config/wordpress.conf
   ```

1. Now navigate to `/var/www` directory, which is the default root folder for Apache servers\. And use the `ln` command to link the `wordpress` directory you created earlier to the current working directory \(`/var/www`\): 

   ```
   cd /var/www
   sudo ln -s /home/ec2-user/environment/wordpress
   ```

1. Run the `chmod` command to allow the Apache server to run content in the `wordpress` subdirectory:

   ```
   sudo chmod +x /home/ec2-user/
   ```

1. Now restart the Apache server to allow it to detect the new configurations: 

   ```
   sudo service httpd restart
   ```

## Step 4: Previewing WordPress web content<a name="wp-preview-wordpress"></a>

1. Using the AWS Cloud9 IDE, create a new file called `index.html` in the following directory: `environment/wordpress`\.

1. Add HTML\-formatted text to `index.html`\. For example:

   ```
   <h1>Hello World!</h1>
   ```

1. In the **Environment** window, choose the `wordpress` folder , and then choose **Preview**, **Preview Running Application**\.

   The web page, which displays the *Hello World\!* message, appears in the application preview tab\. To view the web content in your preferred browser, choose **Pop Out Into a New Window**\.

   If you delete the `index.html` file and refresh the application preview tab, the WordPress configuration page is displayed\. 

## Managing mixed content errors<a name="wp-allow-mixed"></a>

Web browsers display mixed content errors for a WordPress site if it's loading HTTPS and HTTP scripts or content at the same time\. The wording of error messages depends on the web browser that you're using, but you're informed that your connection to a site is insecure or not fully secure\. And your web browser blocks access to the mixed content\.

**Important**  
By default, all web pages that you access in the application preview tab of the AWS Cloud9 IDE automatically use the HTTPS protocol\. If a page's URI features the insecure `http` protocol, it's automatically replaced by `https`\. And you can't access the insecure content by manually changing `https` back to `http`\.  
For guidance on implementing HTTPS for your web site, see the [WordPress documentation](https://wordpress.org/support/article/https-for-wordpress/)\.