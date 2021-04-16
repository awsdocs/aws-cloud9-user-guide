# Step 2: Add code<a name="tutorial-ruby-code"></a>

\(Previous step: [Step 1: Install required tools](tutorial-ruby-install.md)\)

1. In the AWS Cloud9 IDE, create a new file \(**File**, **New File** on the menu bar\)\.

1. Add the following code\.

   ```
   puts "Hello, World!"
   
   puts "The sum of 2 and 3 is 5."
   
   argv0 = ARGV[0]
   argv1 = ARGV[1]
   sum = argv0.to_i + argv1.to_i
   
   puts "The sum of #{argv0} and #{argv1} is #{sum}."
   ```

1. Save the file with the name `hello.rb` \(**File**, **Save**\)\.

## Next Step<a name="tutorial-ruby-code-next"></a>

[Step 3: Run the code](tutorial-ruby-run.md)