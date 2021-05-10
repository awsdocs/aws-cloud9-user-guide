# Docker sample for AWS Cloud9<a name="sample-docker"></a>

This sample shows you how to connect an AWS Cloud9 SSH development environment to a running Docker container inside of an Amazon Linux instance in Amazon EC2\. This enables you to use the AWS Cloud9 IDE to work with code and files inside of a Docker container and to run commands on that container\. For information about Docker, see [What is Docker](https://www.docker.com/what-docker) on the Docker website\.

Creating this sample might result in charges to your AWS account\. These include possible charges for services such as Amazon EC2\. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/)\.

**Topics**
+ [Prerequisites](#sample-docker-prereqs)
+ [Step 1: Install and run Docker](#sample-docker-install)
+ [Step 2: Build the image](#sample-docker-build)
+ [Step 3: Run the container](#sample-docker-run)
+ [Step 4: Create the environment](#sample-docker-env)
+ [Step 5: Run the code](#sample-docker-code)
+ [Step 6: Clean up](#sample-docker-clean-up)

## Prerequisites<a name="sample-docker-prereqs"></a>
+  **You should have an Amazon EC2 instance running Amazon Linux or Ubuntu Server\.** This sample assumes you already have an Amazon EC2 instance running Amazon Linux or Ubuntu Server in your AWS account\. To launch an Amazon EC2 instance, see [Launch a Linux Virtual Machine](https://aws.amazon.com/getting-started/tutorials/launch-a-virtual-machine/)\. In the **Choose an Amazon Machine Image \(AMI\)** page of the wizard, choose an AMI whose display name starts with **Amazon Linux AMI** or **Ubuntu Server**\.
+  **If the Amazon EC2 instance runs within an Amazon VPC, there are additional requirements\.** See [VPC settings for AWS Cloud9 Development Environments](vpc-settings.md)\.
+  **The Amazon EC2 instance should have at least 8 to 16 GB of free disk space available\.** This sample uses Docker images that are over 3 GB in size and can use additional increments of 3 GB or more of disk space to build images\. If you try to run this sample on a disk that has 8 GB of free space or less, we've found that the Docker image might not build or the Docker container might not run\. To check the instance's free disk space, you can run a command such as ** `df -h` ** \(for "disk filesystem information in human\-readable format"\) on the instance\. To increase an existing instance's disk size, see [Modifying a Volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modify-volume.html) in the *Amazon EC2 User Guide for Linux Instances*\.

## Step 1: Install and run Docker<a name="sample-docker-install"></a>

In this step, you check if Docker is installed on the Amazon EC2 instance, and install Docker if it isn't already installed\. After you install Docker, you run it on the instance\.

1. Connect to the running Amazon EC2 instance by using an SSH client such as the ** `ssh` ** utility or PuTTY\. To do this, see "Step 3: Connect to Your Instance" in [Launch a Linux Virtual Machine](https://aws.amazon.com/getting-started/tutorials/launch-a-virtual-machine/)\.

1. Check if Docker is installed on the instance\. To do this, run the ** `docker` ** command on the instance with the ** `--version` ** option\.

   ```
   docker --version
   ```

   If Docker is installed, the Docker version and build number are displayed\. In this case, skip ahead to step 5 later in this procedure\.

1. Install Docker\. To do this, run the ** `yum` ** or ** `apt` ** command with the ** `install` ** action, specifying the ** `docker` ** or ** `docker.io` ** package to install\.

   For Amazon Linux:

   ```
   sudo yum install -y docker
   ```

   For Ubuntu Server:

   ```
   sudo apt install -y docker.io
   ```

1. Confirm that Docker is installed\. To do this, run the ** `docker --version` ** command again\. The Docker version and build number are displayed\.

1. Run Docker\. To do this, run the ** `service` ** command with the ** `docker` ** service and the ** `start` ** action\.

   ```
   sudo service docker start
   ```

1. Confirm Docker is running\. To do this, run the ** `docker` ** command with the ** `info` ** action\.

   ```
   sudo docker info
   ```

   If Docker is running, information about Docker is displayed\.

## Step 2: Build the image<a name="sample-docker-build"></a>

In this step, you use a Dockerfile to build a Docker image onto the instance\. This sample uses an image that includes Node\.js and a sample chat server application\.

1. On the instance, create the Dockerfile\. To do this, with the SSH client still connected to the instance, in the `/tmp` directory on the instance, create a file named `Dockerfile`\. For example, run the ** `touch` ** command as follows\.

   ```
   sudo touch /tmp/Dockerfile
   ```

1. Add the following contents to the `Dockerfile` file\.

   ```
   # Build a Docker image based on the Amazon Linux 2 Docker image.
   FROM amazonlinux:2
   
   # install common tools
   RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
   RUN yum update -y
   RUN yum install -y sudo bash curl wget git man-db nano vim bash-completion tmux  gcc gcc-c++ make tar
   
   # Enable the Docker container to communicate with AWS Cloud9 by
   # installing SSH.
   RUN yum install -y openssh-server
   
   # Ensure that Node.js is installed.
   RUN yum install -y nodejs
   
   # Create user and enable root access
   RUN useradd --uid 1000 --shell /bin/bash -m --home-dir /home/ubuntu ubuntu && \
       sed -i 's/%wheel\s.*/%wheel ALL=NOPASSWD:ALL/' /etc/sudoers && \
       usermod -a -G wheel ubuntu
   
   # Add the AWS Cloud9 SSH public key to the Docker container.
   # This assumes a file named authorized_keys containing the
   # AWS Cloud9 SSH public key already exists in the same
   # directory as the Dockerfile.
   RUN mkdir -p /home/ubuntu/.ssh
   ADD ./authorized_keys /home/ubuntu/.ssh/authorized_keys
   RUN chown -R ubuntu /home/ubuntu/.ssh /home/ubuntu/.ssh/authorized_keys && \
   chmod 700 /home/ubuntu/.ssh && \
   chmod 600 /home/ubuntu/.ssh/authorized_keys
   
   # Update the password to a random one for the user ubuntu.
   RUN echo "ubuntu:$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)" | chpasswd
   
   # pre-install Cloud9 dependencies
   USER ubuntu
   RUN curl https://d2j6vhu5uywtq3.cloudfront.net/static/c9-install.sh | bash
   
   USER root
   # Start SSH in the Docker container.
   CMD ssh-keygen -A && /usr/sbin/sshd -D
   ```

   To add the preceding contents to the `Dockerfile` file, you could use the ** `vi` ** utility on the instance as follows\.

   1. Use ** `vi` ** to open the `/tmp/Dockerfile` file\.

      ```
      sudo vi /tmp/Dockerfile
      ```

   1. Paste the preceding contents into the `Dockerfile` file\. If you're not sure how to do this, see your SSH client's documentation\.

   1. Switch to command mode\. To do this, press the `Esc` key\. \(`-- INSERT --` disappears from the bottom of the window\.\)

   1. Type `:wq` \(to write to the `/tmp/Dockerfile` file, save the file, and then exit ** `vi` **\), and then press `Enter`\.
**Note**  
You can access a frequently updated list of Docker images from AWS CodeBuild\. For more information, see [Docker images provided by CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available.html) in the *AWS CodeBuild User Guide*\.

1. On the instance, create a file that contains the AWS Cloud9 SSH public key for the Docker container to use\. To do this, in the same directory as the `Dockerfile` file, create a file named `authorized_keys`, for example, by running the ** `touch` ** command\.

   ```
   sudo touch /tmp/authorized_keys
   ```

1. Add the AWS Cloud9 SSH public key to the `authorized_keys` file\. To get the AWS Cloud9 SSH public key, do the following:

   1. Open the AWS Cloud9 console at [https://console\.aws\.amazon\.com/cloud9/](https://console.aws.amazon.com/cloud9/)\.

   1. In the AWS navigation bar, in the AWS Region selector, choose the AWS Region where you'll want to create the AWS Cloud9 development environment later in this topic\.

   1. If a welcome page is displayed, for **New AWS Cloud9 environment**, choose **Create environment**\. Otherwise, choose **Create environment**\.

   1. On the **Name environment** page, for **Name**, type a name for the environment\. \(The name doesn't matter here\. You'll choose a different name later\.\)

   1. Choose **Next step**\.

   1. For **Environment type**, choose **Connect and run in remote server \(SSH\)**\.

   1. Expand **View public SSH key**\.

   1. Choose **Copy key to clipboard**\. \(This is between **View public SSH key** and **Advanced settings**\.\)

   1. Choose **Cancel**\.

   1. Paste the contents of the clipboard into the `authorized_keys` file, and then save the file\. For example, you can use the ** `vi` ** utility, as described earlier in this step\.

1. Build the image by running the ** `docker` ** command with the ** `build` ** action, adding the tag `cloud9-image:latest` to the image and specifying the path to the `Dockerfile` file to use\.

   ```
   sudo docker build -t cloud9-image:latest /tmp
   ```

   If successful, the last two lines of the build output display `Successfully built` and `Successfully tagged`\.

   To confirm that Docker successfully built the image, run the ** `docker` ** command with the `image ls` action\.

   ```
   sudo docker image ls
   ```

   If successful, the output displays an entry where the `REPOSITORY` field is set to `cloud9-image` and the `TAG` field is set to `latest`\.

1. Make a note of the Amazon EC2 instance's public IP address\. You'll need it for [Step 4: Create the environment](#sample-docker-env)\. If you're not sure what the public IP address of the instance is, you can run the following command on the instance to get it\.

   ```
   curl http://169.254.169.254/latest/meta-data/public-ipv4
   ```

## Step 3: Run the container<a name="sample-docker-run"></a>

In this step, you run a Docker container on the instance\. This container is based on the image you built in the previous step\.

1. To run the Docker container, run the ** `docker` ** command on the instance with the ** `run` ** action and the following options\.

   ```
   sudo docker run -d -it --expose 9090 -p 0.0.0.0:9090:22 --name cloud9 cloud9-image:latest
   ```
   +  `-d` runs the container in detached mode, exiting whenever the root process that is used to run the container \(in this sample, the SSH client\) exits\.
   +  `-it` runs the container with an allocated pseudo\-TTY and keeps STDIN open, even if the container is not attached\.
   +  `--expose` makes the specified port \(in this sample, port `9090`\) available from the container\.
   +  `-p` makes the specified port available internally to the Amazon EC2 instance over the specified IP address and port\. In this sample, port `9090` on the container can be accessed internally through port `22` on the Amazon EC2 instance\.
   +  `--name` is a human\-readable name for the container \(in this sample, `cloud9`\)\.
   +  `cloud9-image:latest` is the human\-readable name of the built image to use to run the container\.

   To confirm that Docker is successfully running the container, run the ** `docker` ** command with the `container ls` action\.

   ```
   sudo docker container ls
   ```

   If successful, the output displays an entry where the `IMAGE` field is set to `cloud9-image:latest` and the `NAMES` field is set to `cloud9`\.

1. Log in to the running container\. To do this, run the ** `docker` ** command with the ** `exec` ** action and the following options\.

   ```
   sudo docker exec -it cloud9 bash
   ```
   +  `-it` runs the container with an allocated pseudo\-TTY and keeps STDIN open, even if the container isn't attached\.
   +  `cloud9` is the human\-readable name of the running container\.
   +  `bash` starts the standard shell in the running container\.

   If successful, the terminal prompt changes to display the logged\-in user's name for the container and the ID of the container\.
**Note**  
If you ever want to log out of the running container, run the ** `exit` ** command\. The terminal prompt changes back to display the logged\-in user's name for the instance and the private DNS of the instance\. The container should still be running\.

1. For the directory on the running container that you want AWS Cloud9 to start from after it logs in, set its access permissions to ** `rwxr-xr-x` **\. This means read\-write\-execute permissions for the owner, read\-execute permissions for the group, and read\-execute permissions for others\. For example, if the directory's path is `~`, you can set these permissions on the directory by running the ** `chmod` ** command in the running container as follows\.

   ```
   sudo chmod u=rwx,g=rx,o=rx ~
   ```

1. Make a note of the path to the directory on the running container that contains the Node\.js binary, as you'll need it for [Step 4: Create the environment](#sample-docker-env)\. If you're not sure what this path is, run the following command on the running container to get it\.

   ```
   which node
   ```

## Step 4: Create the environment<a name="sample-docker-env"></a>

In this step, you use AWS Cloud9 to create an AWS Cloud9 SSH development environment and connect it to the running Docker container\. After AWS Cloud9 creates the environment, it displays the AWS Cloud9 IDE so that you can start working with the files and code in the container\.

1. Sign in to the AWS Cloud9 console as follows:
   + If you're the only individual using your AWS account or you are an IAM user in a single AWS account, go to [https://console\.aws\.amazon\.com/cloud9/](https://console.aws.amazon.com/cloud9/)\.
   + If your organization uses AWS Single Sign\-On \(SSO\), see your AWS account administrator for sign\-in instructions\.
   + If you're using an AWS Educate Starter Account, see [Use an AWS Educate Starter Account to sign in to the AWS Cloud9 console](setup-student.md#setup-student-sign-in-ide) in *Individual Student Signup*\.
   + If you're a student in a classroom, see your instructor for sign\-in instructions\.

1. In the AWS navigation bar, in the AWS Region selector, choose the AWS Region where you want to create the SSH environment\.

1. If a welcome page is displayed, for **New AWS Cloud9 environment**, choose **Create environment**\. Otherwise, choose **Create environment**\.

1. On the **Name environment** page, for **Name**, type a name for the environment\.

1. To add a description to the environment, type it in **Description**\.

1. Choose **Next step**\.

1. For **Environment type:**, choose **Connect and run in remote server \(SSH\)**\.

1. For **User**, type `ubuntu`\.

1. For **Host**, type the public IP address of the Amazon EC2 instance, which you noted earlier\.

1. For **Port**, type `9090`\.

1. Expand **Advanced settings**\.

1. For **Environment path**, type the path to the directory on the running container that you want AWS Cloud9 to start from after it logs in\.

1. For **Node\.js binary path**, type the path to the directory on the running container that contains the Node\.js binary, which you noted earlier\.

1. Choose **Next step**\.

1. Choose **Create environment**\.

1. When the **AWS Cloud9 Installer** dialog box appears, choose **Next**\.

1. In the list of components to be installed, clear the **c9\.ide\.lambda\.docker** check box, and then choose **Next**\. This is because AWS Cloud9 cannot run Docker inside of Docker\.

1. When the **AWS Cloud9 Installer** dialog box displays **Installation Completed**, choose **Next**, and then choose **Finish**\. The AWS Cloud9 IDE appears for the running container, and you can start working with the container's files and code\.

**Note**  
If the container stops running, you can no longer use the IDE to access the container until you start running the container again\. To do this, go back to [Step 3: Run the container](#sample-docker-run)\.

## Step 5: Run the code<a name="sample-docker-code"></a>

In this step, you use the AWS Cloud9 IDE to run a sample application inside the running Docker container\.

1. With the AWS Cloud9 IDE displayed for the running container, start the sample chat server\. To do this, in the **Environment** window, right\-click the sample `workspace/server.js` file, and then choose **Run**\.

1. Preview the sample application\. To do this, in the **Environment** window, open the the `workspace/client/index.html` file\. Then, on the menu bar, choose **Tools, Preview, Preview Running Application**\.

1. On the application preview tab, for **Your Name**, type your name\. For **Message**, type a message\. Then choose **Send**\. The chat server adds your name and message to the list\.

## Step 6: Clean up<a name="sample-docker-clean-up"></a>

In this step, you delete the environment and remove AWS Cloud9 and Docker support files from the Amazon EC2 instance\. Also, to prevent ongoing charges to your AWS account after you're done using this sample, you should terminate the Amazon EC2 instance that is running Docker\.

### Step 6\.1: Delete the environment<a name="step-6-1-delete-the-envtitle"></a>

To delete the environment, see [Deleting an environment in AWS Cloud9](delete-environment.md)\.

### Step 6\.2: Remove AWS Cloud9 support files from the container<a name="step-6-2-remove-ac9-support-files-from-the-container"></a>

After you delete the environment, some AWS Cloud9 support files still remain in the container\. If you want to keep using the container but no longer need these support files, delete the `.c9` folder from the directory on the container that you specified AWS Cloud9 to start from after it logs in\. For example, if the directory is `~`, run the ** `rm` ** command with the ** `-r` ** option as follows\.

```
sudo rm -r ~/.c9
```

### Step 6\.3: Remove Docker support files from the instance<a name="step-6-3-remove-docker-support-files-from-the-instance"></a>

If you no longer want to keep the Docker container, the Docker image, and Docker on the Amazon EC2 instance, but you want to keep the instance, you can remove these Docker support files as follows\.

1. Remove the Docker container from the instance\. To do this, run the ** `docker` ** command on the instance with the ** `stop` ** and ** `rm` ** stop actions and the human\-readable name of the container\.

   ```
   sudo docker stop cloud9
   sudo docker rm cloud9
   ```

1. Remove the Docker image from the instance\. To do this, run the ** `docker` ** command on the instance with the ** `image rm` ** action and the image's tag\.

   ```
   sudo docker image rm cloud9-image:latest
   ```

1. Remove any additional Docker support files that might still exit\. To do this, run the ** `docker` ** command on the instance with the ** `system prune` ** action\.

   ```
   sudo docker system prune -a
   ```

1. Uninstall Docker\. To do this, run the ** `yum` ** command on the instance with the ** `remove` ** action, specifying the ** `docker` ** package to uninstall\.

   For Amazon Linux:

   ```
   sudo yum -y remove docker
   ```

   For Ubuntu Server:

   ```
   sudo apt -y remove docker
   ```

   You can also remove the `Dockerfile` and `authorized_keys` files you created earlier\. For example, run the ** `rm` ** command on the instance\.

   ```
   sudo rm /tmp/Dockerfile
   sudo rm /tmp/authorized_keys
   ```

### Step 6\.4: Terminate the instance<a name="step-6-4-terminate-the-instance"></a>

To terminate the Amazon EC2 instance, see [Terminate Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html) in the *Amazon EC2 User Guide for Linux Instances*\.