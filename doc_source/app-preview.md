# Previewing running applications in the AWS Cloud9 Integrated Development Environment \(IDE\)<a name="app-preview"></a>

You can use the AWS Cloud9 IDE to preview a running application from within the IDE\.

**Topics**
+ [Run an application](#app-preview-run-app)
+ [Preview a running application](#app-preview-preview-app)
+ [Reload an application preview](#app-preview-app-reload)
+ [Change the application preview type](#app-preview-app-preview-type)
+ [Open an application preview in a separate web browser tab](#app-preview-app-open-tab)
+ [Switch to a different preview URL](#app-preview-url-switch)
+ [Share a running application over the internet](#app-preview-share)

## Run an application<a name="app-preview-run-app"></a>

Before you can preview your application from within the IDE, it must be running in the AWS Cloud9 development environment using HTTP over port `8080`, `8081`, or `8082` with the IP of `127.0.0.1`, `localhost`, or `0.0.0.0`\.

**Note**  
You don't have to run using HTTP over port `8080`, `8081`, or `8082` with the IP of `127.0.0.1`, `localhost`, or `0.0.0.0`\. However, you won't be able to preview your running application from within the IDE\.

To write the code to run your application on a specific port and IP, see your application's documentation\.

To run your application, see [Run Your Code](build-run-debug.md#build-run-debug-run)\.

To test this behavior, for example you could add the following JavaScript code to a file with a name such as `server.js` in the root of your environment\. This code runs a server using Node\.js\.

**Note**  
The code below indicates that `text/html` is the `Content-Type` of the returned content\. Specify a different `Content-Type` to return content in another format \(`text/css` for a CSS file, for example\)\.

```
var http = require('http');
var fs = require('fs');
var url = require('url');

http.createServer( function (request, response) {
  var pathname = url.parse(request.url).pathname;
  console.log("Trying to find '" + pathname.substr(1) + "'...");

  fs.readFile(pathname.substr(1), function (err, data) {
    if (err) {
      response.writeHead(404, {'Content-Type': 'text/html'});
      response.write("ERROR: Cannot find '" + pathname.substr(1) + "'.");
      console.log("ERROR: Cannot find '" + pathname.substr(1) + "'.");
    } else {
      console.log("Found '" + pathname.substr(1) + "'.");
      response.writeHead(200, {'Content-Type': 'text/html'});
      response.write(data.toString());
    }
    response.end();
  });
}).listen(8080, 'localhost'); // Or 8081 or 8082 instead of 8080. Or '127.0.0.1' instead of 'localhost'.
```

Or you could add the following Python code to a file with a name such as `server.py` in the root of your environment\. This code runs a server using Python, as follows\.

```
import os
import http.server
import socketserver

ip = 'localhost' # Or '127.0.0.1' instead of 'localhost'.
port = '8080' # Or '8081' or '8082' instead of '8080'.
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer((ip, int(port)), Handler)
httpd.serve_forever()
```

Next, add the following HTML code to a file with a name such as `index.html` in the root of your environment\.

```
<html>
  <head>
    <title>Hello Home Page</title>
  </head>
  <body>
    <p style="font-family:Arial;color:blue">Hello, World!</p>
  </body>
</html>
```

To see this file's HTML output on the application preview tab, run `server.js` with Node\.js or `server.py` file with Python\. Then follow the instructions in the next procedure to preview it\. On the application preview tab, add `/index.html` to the end of the URL, and then press `Enter`\.

## Preview a running application<a name="app-preview-preview-app"></a>

With your application already running using HTTP over port `8080`, `8081`, or `8082` with the IP of `127.0.0.1`, `localhost`, or `0.0.0.0` in the environment, and with the corresponding application code file open and active in the AWS Cloud9 IDE, choose one of the following on the menu bar:
+  **Preview, Preview Running Application** 
+  **Tools, Preview, Preview Running Application** 

This opens an application preview tab within the environment, and then displays the application's output on the tab\.

If the application preview tab displays an error or is blank, try following the troubleshooting steps in [Application preview tab displays an error or is blank](troubleshooting.md#troubleshooting-app-preview)\.

To enable others to preview the running application outside of the IDE, see [Share a running application over the internet](#app-preview-share)\.

**Note**  
If the application is not already running, you will see an error on the application preview tab\. Run or restart the application, and then choose the menu bar command again\.  
If your application cannot run on any of the preceding ports or IPs, or if your application must run on more than one of these ports at the same time \(for example, your application must run on ports `8080` and `3000` at the same time\), the application preview tab might display an error or might be blank\. This is because the application preview tab within the environment works only with the preceding ports and IPs, and it works with only a single port at a time\.  
We don't recommend sharing the URL in the application preview tab with others\. \(The URL displays using the format `https://12a34567b8cd9012345ef67abcd890e1.vfs.cloud9.us-east-2.amazonaws.com/`, where `12a34567b8cd9012345ef67abcd890e1` is the ID that AWS Cloud9 assigns to the environment, and `us-east-2` is the ID of the AWS Region for the environment\.\) This URL works only when the IDE for the environment is open and the application is running in the same web browser\.  
If you try to go to the IP of `127.0.0.1`, `localhost`, or `0.0.0.0` by using the application preview tab in the IDE or in a separate web browser tab outside of the IDE, the default built\-in behavior of the AWS Cloud9 IDE is that this will attempt to go to your local computer, instead of attempting to go the instance or your own server that is connected to the environment\.

## Reload an application preview<a name="app-preview-app-reload"></a>

On the application preview tab, choose the **Refresh** button \(the circular arrow\)\.

**Note**  
This command does not restart the server\. It just refreshes the contents of the application preview tab\.

## Change the application preview type<a name="app-preview-app-preview-type"></a>

On the application preview tab, choose one of the following in the preview type list:
+  **Browser**: Previews the output in a web browser format\.
+  **Raw Content \(UTF\-8\)**: Attempts to preview the output in Unicode Transformation Format 8\-bit \(UTF\-8\) format, if applicable\.
+  **Markdown**: Attempts to preview the output in Markdown format, if applicable\.

## Open an application preview in a separate web browser tab<a name="app-preview-app-open-tab"></a>

On the application preview tab, choose **Pop Out Into New Window**\.

**Note**  
The application preview will not be displayed in a separate web browser tab unless the AWS Cloud9 IDE is also running in at least one other tab in the same web browser\.

## Switch to a different preview URL<a name="app-preview-url-switch"></a>

On the application preview tab, type the path to a different URL in the address bar\. The address bar is located between the **Refresh** button and the preview type list\.

## Share a running application over the internet<a name="app-preview-share"></a>

After you preview your running application, you can make it available to others over the internet\.

To do this, if an Amazon EC2 instance is connected to your environment, follow these steps\. Otherwise, see your server's documentation\.

**Topics**
+ [Step 1: Get the ID and the IP address of the instance](#app-preview-share-get-metadata)
+ [Step 2: Set up the security group for the instance](#app-preview-share-security-group)
+ [Step 3: Set up the subnet for the instance](#app-preview-share-subnet)
+ [Step 4: Share the running application URL](#app-preview-share-url)

### Step 1: Get the ID and the IP address of the instance<a name="app-preview-share-get-metadata"></a>

In this step, you note the instance ID and public IP address for the Amazon EC2 instance that is connected to the environment\. You need the instance ID in a later step to allow incoming application requests\. Then you give the public IP address to others so that they can access the running application\.

1. Get the Amazon EC2 instance's ID\. To get this, do one of the following:
   + In a terminal session in the AWS Cloud9 IDE for the environment, run the following command to get the Amazon EC2 instance's ID\.

     ```
     curl http://169.254.169.254/latest/meta-data/instance-id
     ```

     The instance ID will look similar to this: `i-12a3b456c789d0123`\. Make a note of this instance ID\.
   + In the IDE for the environment, on the menu bar, choose your user icon, and then choose **Manage EC2 Instance**\.  
![\[Choosing to manage the instance from the AWS Cloud9 IDE\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/console-manage-instance.png)

     In the Amazon EC2 console that displays, make a note of the instance ID that displays in the **Instance ID** column\. The instance ID will look similar to this: `i-12a3b456c789d0123`\.

1. Get the Amazon EC2 instance's public IP address\. To get this, do one of the following:
   + In the IDE for the environment, on the menu bar, choose **Share**\. In the **Share this environment** dialog box, make a note of the public IP address in the **Application** box\. The public IP address will look similar to this: `192.0.2.0`\.
   + In a terminal session in the IDE for the environment, run the following command to get the Amazon EC2 instance's public IP address\.

     ```
     curl http://169.254.169.254/latest/meta-data/public-ipv4
     ```

     The public IP address will look similar to this: `192.0.2.0`\. Make a note of this public IP address\.
   + In the IDE for the environment, on the menu bar, choose your user icon, and then choose **Manage EC2 Instance**\. In the Amazon EC2 console that displays, on the **Description** tab, make a note of the public IP address for the **IPv4 Public IP** field\. The public IP address will look similar to this: `192.0.2.0`\.
**Note**  
The instance's public IP address might change anytime the instance restarts\. To prevent this IP address from changing, one solution is to allocate an Elastic IP address and then assign that address to the running instance\. For instructions, see [Allocating an Elastic IP Address](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html#using-instance-addressing-eips-allocating) and [Associating an Elastic IP Address with a Running Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html#using-instance-addressing-eips-associating) in the *Amazon EC2 User Guide for Linux Instances*\. Note also that allocating an Elastic IP address might result in charges to your AWS account\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/)\.

### Step 2: Set up the security group for the instance<a name="app-preview-share-security-group"></a>

In this step, you use the Amazon EC2 console to set up the Amazon EC2 security group for the instance that is connected to the environment, to allow incoming HTTP requests over port 8080, 8081, or 8082\.

**Note**  
You don't have to run using HTTP over port `8080`, `8081`, or `8082`\. If you are running on a different protocol or port, substitute it throughout this step\. You won't be able to preview your running application from within the IDE until you switch back to running using HTTP over one of the ports and IPs as described in [Preview a running application](#app-preview-preview-app)\.  
For an additional layer of security, you can also set up a network access control list \(ACL\) for a subnet in a virtual private cloud \(VPC\) that the instance can use\. For more information about security groups and network ACLs, see the following:  
 [Step 3: Set up the subnet for the instance](#app-preview-share-subnet) 
 [Security](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html) in the *Amazon VPC User Guide*
 [Security Groups for Your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) in the *Amazon VPC User Guide*
 [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_ACLs.html) in the *Amazon VPC User Guide*

1. In the IDE for the environment, on the menu bar, choose your user icon, and then choose **Manage EC2 Instance**\. Then skip ahead to step 3 in this procedure\.

1. If choosing **Manage EC2 Instance** or other steps in this procedure display errors, we recommend you sign in to the Amazon EC2 console using credentials for an IAM administrator user in your AWS account, and then complete the following instructions\. If you cannot do this, check with your AWS account administrator\.

   1. Sign in to the AWS Management Console, if you are not already signed in, at [https://console\.aws\.amazon\.com/](https://console.aws.amazon.com/)\.

   1. Open the Amazon EC2 console\. To do this, in the AWS navigation bar, choose **Services**\. Then choose **EC2**\.

   1. In the AWS navigation bar, choose the AWS Region where the environment is located\.

   1. If the **EC2 Dashboard** is displayed, choose **Running Instances**\. Otherwise, in the service navigation pane, expand **Instances** if it is not already expanded, and then choose **Instances**\.

   1. In the list of instances, select the instance where the **Instance ID** matches the instance ID you noted earlier\.

1. In the **Description** tab for the instance, choose the security group link next to **Security groups**\.

1. With the security group displayed, look on the **Inbound** tab\. If a rule already exists where **Type** is set to **Custom TCP Rule** and **Port Range** is set to **8080**, **8081**, or **8082**, choose **Cancel**, and skip ahead to [Step 3: Set up the subnet for the instance](#app-preview-share-subnet)\. Otherwise, choose **Edit**\.

1. In the **Edit inbound rules** dialog box, choose **Add Rule**\.

1. For **Type**, choose **Custom TCP Rule**\.

1. For **Port Range**, type `8080`, `8081`, or `8082`\.

1. For **Source**, choose **Anywhere**\.
**Note**  
Choosing **Anywhere** for **Source** allows incoming requests from any IP address\. To restrict this to specific IP addresses, choose **Custom** and then type the IP address range, or choose **My IP** to restrict this to requests from your IP address only\.

1. Choose **Save**\.

### Step 3: Set up the subnet for the instance<a name="app-preview-share-subnet"></a>

In this step, you use the consoles for Amazon EC2 and Amazon Virtual Private Cloud \(Amazon VPC\) to set up the subnet for the Amazon EC2 instance that is connected to the environment, to also allow incoming HTTP requests over port 8080, 8081, or 8082\.

**Note**  
You don't have to run using HTTP over port `8080`, `8081`, or `8082`\. If you are running on a different protocol or port, substitute it throughout this step\. You won't be able to preview your running application from within the IDE until you switch back to running using HTTP over the ports and IPs as described in [Preview a running application](#app-preview-preview-app)\.  
This step describes how to set up a network ACL for a subnet in an Amazon VPC that the instance can use\. This step is not required\. However, it adds an additional layer of security when compared to just using security groups\. For more information about network ACLs, see the following:  
 [Security](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html) in the *Amazon VPC User Guide*
 [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_ACLs.html) in the *Amazon VPC User Guide*

1. With the Amazon EC2 console already open from the previous step, in the service navigation pane, expand **Instances** if it is not already expanded, and then choose **Instances**\.

1. In the list of instances, select the instance where the **Instance ID** matches the instance ID you noted earlier\.

1. In the **Description** tab for the instance, note the value of **Subnet ID**\. It should look similar to this: `subnet-1fab8aEX`\.

1. Open the Amazon VPC console\. To do this, in the AWS navigation bar, choose **Services**\. Then choose **VPC**\.

   For this step, we recommend you sign in to the Amazon VPC console using credentials for an IAM administrator user in your AWS account\. If you cannot do this, check with your AWS account administrator\.

1. If the **VPC Dashboard** is displayed, choose **Subnets**\. Otherwise, in the service navigation pane, choose **Subnets**\.

1. In the list of subnets, select the subnet where the **Subnet ID** value matches the one you noted earlier\.

1. On the **Summary** tab, choose the network ACL link next to **Network ACL**\.

1. In the list of network ACLs, select the network ACL\. \(There is only one network ACL\.\)

1. Look on the **Inbound Rules** tab for the network ACL\. If a rule already exists where **Type** is set to **HTTP\* \(8080\)**, **HTTP\* \(8081\)**, or **HTTP\* \(8082\)**, skip ahead to [Step 4: Share the running application URL](#app-preview-share-url)\. Otherwise, choose **Edit**\.

1. Choose **Add another rule**\.

1. For **Rule \#**, type a number for the rule \(for example, `200`\)\.

1. For **Type**, choose **Custom TCP Rule**\.

1. For **Port Range**, type `8080`, `8081`, or `8082`\.

1. For **Source**, type the range of IP addresses to allow incoming requests from\. For example, to allow incoming requests from any IP address, type `0.0.0.0/0`\.

1. With **Allow / Deny** set to **ALLOW**, choose **Save**\.

### Step 4: Share the running application URL<a name="app-preview-share-url"></a>

With the application running, give to others the public IP address you noted earlier\. Be sure to start the URL with the correct protocol, and add the port number if it is not the default for that protocol \(for example, `http://192.0.2.0:8080/index.html` using HTTP over port 8080\)\.

If the resulting web browser tab displays an error, or the tab is blank, try following the troubleshooting steps in [Cannot display your running application outside of the IDE](troubleshooting.md#troubleshooting-app-sharing)\.

**Note**  
The instance's public IP address might change anytime the instance restarts\. To prevent this IP address from changing, one solution is to allocate an Elastic IP address and then assign that address to the running instance\. For instructions, see [Allocating an Elastic IP Address](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html#using-instance-addressing-eips-allocating) and [Associating an Elastic IP Address with a Running Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html#using-instance-addressing-eips-associating) in the *Amazon EC2 User Guide for Linux Instances*\. Note also that allocating an Elastic IP address might result in charges to your AWS account\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/)\.  
You don't have to run using HTTP over port `8080`, `8081`, or `8082`\. However, you won't be able to preview your running application from within the IDE until you switch back to running using HTTP over one of the ports and IPs as described in [Preview a running application](#app-preview-preview-app)\.  
If users make requests to the preceding URL, and those requests originate from a virtual private network \(VPN\) that blocks traffic over the requested protocol or port, those requests might fail\. Those users must use a different network that allows traffic over the requested protocol and port\. For more information, see your network administrator\.  
We don't recommend sharing the URL in the application preview tab in the IDE with others\. \(The URL displays using the format `https://12a34567b8cd9012345ef67abcd890e1.vfs.cloud9.us-east-2.amazonaws.com/`, where `12a34567b8cd9012345ef67abcd890e1` is the ID that AWS Cloud9 assigns to the environment, and `us-east-2` is the ID of the AWS Region for the environment\.\) This URL works only when the IDE for the environment is open and the application is running in the same web browser\.