# Step 6: Run the AWS SDK Code<a name="tutorial-ruby-sdk-run"></a>

\(Previous step: [Step 5: Add AWS SDK Code](tutorial-ruby-sdk-code.md)\)

1. In the AWS Cloud9 IDE, on the menu bar, choose **Run**, **Run Configurations**, **New Run Configuration**\.

1. In the **\[New\] \- Idle** tab, choose **Runner: Auto**, and then choose **Ruby**\.

1. For **Command**, type `s3.rb YOUR_BUCKET_NAME THE_AWS_REGION`, where:
   + `YOUR_BUCKET_NAME` is the name of the bucket you want to create and then delete\.

     Amazon S3 bucket names must be globally unique across AWS, not just within your AWS account\.
   + `THE_AWS_REGION` is the ID of the AWS Region you want to create the bucket in\.

     For example, for the US East \(Ohio\) Region, use `us-east-2`\. For more IDs, see [Amazon Simple Storage Service \(Amazon S3\)](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) in the *Amazon Web Services General Reference*\.

1. Choose the **Run** button\. Your output should be similar to the following\.

   ```
   My buckets now are:
   
   Creating a new bucket named 'my-test-bucket'...
   
   My buckets now are:
   
   my-test-bucket
   
   Deleting the bucket named 'my-test-bucket'...
   
   My buckets now are:
   ```

## Next Step<a name="tutorial-ruby-sdk-run-next"></a>

[Step 7: Clean Up](tutorial-ruby-clean-up.md)