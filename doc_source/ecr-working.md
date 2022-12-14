# Working with the Amazon Elastic Container Registry service in AWS Cloud9<a name="ecr-working"></a>

You can access the Amazon Elastic Container Registry \(Amazon ECR\) service directly from the AWS Explorer in AWS Cloud9 IDE\. You can use Amazon ECR to push a program image to an Amazon ECR repository\. To get started, follow these steps:

1. Create a Dockerfile that contains the information necessary to build an image\.

1. Build an image from that Dockerfile and tag the image for processing\.

1. Create a repository that's inside of your Amazon ECR instance\. 

1. Push the tagged image to your repository\.

**Topics**
+ [Prerequisites](#prereqs-vscode-ecr)
+ [1\. Creating a Dockerfile](#dockerfile-ecr-cloud9toolkit)
+ [2\. Building your image from your Dockerfile](#build-docker-image)
+ [3\. Creating a new repository](#create-repository)
+ [4\. Pushing, pulling, and deleting images](#push-image)

## Prerequisites<a name="prereqs-vscode-ecr"></a>

Before you can use the Amazon ECR feature of the AWS Toolkit for AWS Cloud9, make sure that you meet these [prerequisites](ecr.md#prereqs-awstoolkit-vscode-ecr) first\. These prerequisites are pre\-installed in the AWS Cloud9 IDE for AWS Cloud9 Amazon EC2 environments and are required to access Amazon ECR\.

## 1\. Creating a Dockerfile<a name="dockerfile-ecr-cloud9toolkit"></a>

Docker uses a file that's called a Dockerfile to define an image that can be pushed and stored on a remote repository\. Before you can upload an image to an ECR repository, create a Dockerfile and then build an image from that Dockerfile\.

**Creating a Dockerfile**

1. To navigate to the directory where you want to store your Dockerfile, choose **Toggle Tree** option in the left navigation bar within your AWS Cloud9 IDE\.

1. Create a new file named **Dockerfile**\.
**Note**  
AWS Cloud9 IDE might prompt you to select a file type or file extension\. If this occurs, select **plaintext**\. AWS Cloud9 IDE has a "dockerfile" extension\. However, we don't recommend you use it\. This is because the extension might cause conflicts with certain versions of Docker or other associated applications\.

**Editing your Dockerfile using AWS Cloud9 IDE**

If your Dockerfile has a file extension, open the context \(right\-click\) menu for the file and remove the file extension\. A Dockerfile with extensions might cause conflicts with certain versions of Docker or other associated applications\.

After the file extension is removed from your Dockerfile:

1. Open the empty Dockerfile directly in AWS Cloud9 IDE\.

1. Copy the contents of the following example into your Dockerfile\.  
**Example Dockerfile image template**  

   ```
   FROM ubuntu:18.04
   
   # Install dependencies
   RUN apt-get update && \
    apt-get -y install apache2
   
   # Install apache and write hello world message
   RUN echo 'Hello World!' > /var/www/html/index.html
   
   # Configure apache
   RUN echo '. /etc/apache2/envvars' > /root/run_apache.sh && \
    echo 'mkdir -p /var/run/apache2' >> /root/run_apache.sh && \
    echo 'mkdir -p /var/lock/apache2' >> /root/run_apache.sh && \ 
    echo '/usr/sbin/apache2 -D FOREGROUND' >> /root/run_apache.sh && \ 
    chmod 755 /root/run_apache.sh
   
   EXPOSE 80
   
   CMD /root/run_apache.sh
   ```

   This is a Dockerfile that uses an Ubuntu 18\.04 image\. The **RUN** instructions update the package caches\. Install software packages for the web server, and then write the "Hello World\!" content to the document root of the web server\. The **EXPOSE** instruction exposes port 80 on the container, and the **CMD** instruction starts the web server\.

1. Save your Dockerfile\.

## 2\. Building your image from your Dockerfile<a name="build-docker-image"></a>

The Dockerfile that you created contains the necessary information to build an image for a program\. Before you can push that image to your Amazon ECR instance, first build the image\.

**Building an image from your Dockerfile**

1. To navigate into the directory that contains your Dockerfile, use the Docker CLI or a CLI that's integrated with your instance of Docker\.

1. To build the image that's defined in your Dockerfile, run the **Docker build** command from the same directory as the Dockerfile\.

   ```
             docker build -t hello-world
   ```

1. To verify that the image was created correctly, run the **Docker images** command\.

   ```
   docker images --filter reference=hello-world
   ```  
**Example**  

   The output is as follows\.

   ```
   REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
   hello-world         latest              e9ffedc8c286        4 minutes ago       241MB
   ```

1. To run the newly built image based on Ubuntu 18\.04, use the **echo** command\.
**Note**  
This step isn't necessary to create or push your image\. However, you can see how the program image works when it's run\.

   ```
   FROM ubuntu:18.04
   CMD ["echo", "Hello from Docker in Cloud9"]
   ```

   Then, run and build the dockerfile\. You must run this command from the same directory as the dockerfile\.

   ```
   docker build -t hello-world .
   docker run --rm hello-world
   ```  
**Example**  

   The output is as follows\.

   ```
   Hello from Docker in Cloud9
   ```

   For more information about the **Docker run** command, see [Docker run reference](https://docs.docker.com/engine/reference/run/) on the Docker website\.

## 3\. Creating a new repository<a name="create-repository"></a>

To upload your image into your Amazon ECR instance, create a new repository where it can be stored in\.

**Creating a new Amazon ECR repository**

1. From the AWS Cloud9 IDE navigation bar, choose the **AWS Toolkit icon**\.

1. Expand the AWS Explorer menu\.

1. Locate the default AWS Region that's associated with your AWS account\. Then, select it to see a list of the services that are through the AWS Cloud9 IDE\.

1. Open the context \(right\-click\) menu for the **ECR** option to start the **Create new repository** process\. Then, select **Create Repository**\.

1. To complete the process, follow the prompt\.

1. After the process is complete, you can access your new repository from the **ECR** section of the AWS Explorer menu\.

## 4\. Pushing, pulling, and deleting images<a name="push-image"></a>

After you built an image from your Dockerfile and created a repository, you can push your image into your Amazon ECR repository\. Additionally, using the AWS Explorer with Docker and the AWS CLI, you can do the following:
+ Pull an image from your repository\.
+ Delete an image that's stored in your repository\.
+ Delete your repository\.

**Authenticating Docker with your default registry**

Authentication is required to exchange data between Amazon ECR and Docker instances\. To authenticate Docker with your registry:

1. Open a terminal within your AWS Cloud9 IDE\. 

1. Use the **get\-login\-password** method to authenticate to your private ECR registry\.

   ```
   aws ecr get-login-password --region region | docker login --username AWS --password-stdin AWS_account_id.dkr.ecr.region.amazonaws.com
   ```
**Important**  
In the preceding command, replace **region** and the **AWS\_account\_id** with information that's specific to your AWS account\. A valid **region** value is *us\-east\-1*\.

**Tagging and pushing an image to your repository**

After you authenticated Docker with your instance of AWS, push an image to your repository\.

1. Use the **docker images** command to view the images that you stored locally and identify the one you want to tag\.

   ```
   docker images
   ```  
**Example**  

   The output is as follows\.

   ```
   REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
   hello-world         latest              e9ffedc8c286        4 minutes ago       241MB
   ```

1. Tag your image with the **Docker tag** command\.

   ```
   docker tag hello-world:latest AWS_account_id.dkr.ecr.region.amazonaws.com/hello-world:latest
   ```

1. Push the tagged image to your repository with the **Docker push** command\.
**Important**  
Make sure that name of your local repository is the same as your AWS Amazon EC2 repository\. In this example, both repositories must be called `hello-world`\. For more information about pushing images with docker, see [Pushing a Docker image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html)\.

   ```
   docker push AWS_account_id.dkr.ecr.region.amazonaws.com/hello-world:latest
   ```  
**Example**  

   The output is as follows\.

   ```
   The push refers to a repository [AWS_account_id.dkr.ecr.region.amazonaws.com/hello-world] (len: 1)
   e9ae3c220b23: Pushed
   a6785352b25c: Pushed
   0998bf8fb9e9: Pushed
   0a85502c06c9: Pushed
   latest: digest: sha256:215d7e4121b30157d8839e81c4e0912606fca105775bb0636b95aed25f52c89b size: 6774
   ```

After your tagged image is successfully uploaded to your repository, refresh the AWS Toolkit by choosing **Refresh Explorer** from the AWS Explorer tab\. It's then visible in the AWS Explorer menu in AWS Cloud9 IDE\.

**Pulling an image from Amazon ECR**
+ You can pull an image to your local instance of **Docker tag** command\.

  ```
  docker pull AWS_account_id.dkr.ecr.region.amazonaws.com/hello-world:latest
  ```  
**Example**  

  The output is as follows\.

  ```
  azonaws.com/hello-world:latest
  latest: Pulling from hello-world
  Digest: sha256:e02c521fd65eae4ef1acb746883df48de85d55fc85a4172a09a124b11b339f5e
  Status: Image is up to date for 922327013870.dkr.ecr.us-west-2.amazonaws.com/hello-world.latest
  ```

**Deleting an image from your Amazon ECR repository**

There are two methods for deleting an image from AWS Cloud9 IDE\. The first method is to use the AWS Explorer\.

1. From the AWS Explorer, expand the **ECR** menu\.

1. Expand the repository that you want to delete an image from\.

1. Open the context \(right\-click\) menu for the image tag that's associated with the image that you want to delete\.

1. To delete all the stored images that are associated with that tag, choose **Delete Tag\.\.\.**\.

**Deleting an image using the AWS CLI**
+ You can also delete an image from your repository with the **AWS ecr batch\-delete\-image** command\.

  ```
  aws ecr batch-delete-image \
        --repository-name hello-world \
        --image-ids imageTag=latest
  ```  
**Example**  

  The output is as follows\.

  ```
  {
      "failures": [],
      "imageIds": [
          {
              "imageTag": "latest",
              "imageDigest": "sha256:215d7e4121b30157d8839e81c4e0912606fca105775bb0636b95aed25f52c89b"
          }
      ]
  }
  ```

**Deleting a repository from your Amazon ECR instance**

There are two methods for deleting a repository from AWS Cloud9 IDE\. The first method is to use the AWS Explorer:

1. From the AWS Explorer, expand the **ECR** menu\.

1. Open the context \(right\-click\) menu for the repository that you want to delete\.

1. Choose **Delete Repository\.\.\.**\.

**Deleting an Amazon ECR repository from the AWS CLI**
+ You can delete a repository with the **AWS ecr delete\-repository** command\.
**Note**  
You normally can't delete a repository without first deleting the images that are contained in it\. However, if you add the **\-\-force** flag, you can delete a repository and all of its images in one step\.

  ```
          aws ecr delete-repository \
        --repository-name hello-world \
        --force
  ```  
**Example**  

  The output is as follows\.

  ```
  --repository-name hello-world --force
  {
      "repository": {
          "repositoryUri": "922327013870.dkr.ecr.us-west-2.amazonaws.com/hello-world", 
          "registryId": "922327013870", 
          "imageTagMutability": "MUTABLE", 
          "repositoryArn": "arn:aws:ecr:us-west-2:922327013870:repository/hello-world", 
          "repositoryName": "hello-world", 
          "createdAt": 1664469874.0
      }
  }
  ```