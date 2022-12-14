# Overview of the CodeWhisperer for AWS Cloud9<a name="codewhisperer-overview"></a>

This overview contains a list of CodeWhisperer user actions and common ways for you to utilize CodeWhisperer while coding in AWS Cloud9\.

**Topics**
+ [User actions](#codewhisperer-user-actions)
+ [Use cases](#codewhisperer-user-cases)

## User actions<a name="codewhisperer-user-actions"></a>

When you're coding in AWS Cloud9, these user actions are associated with the CodeWhisperer\.


| Action | Keyboard shortcut | 
| --- | --- | 
|  Manually trigger CodeWhisperer  |  MacOS: Option \+ C Windows: Alt \+ C Linux: Alt \+ C  | 
|  Accept a recommendation  |  Tab, enter, or click\.  | 
|  Reject a recommendation  |  ESC, backspace, or keep typing and the recommendation will disappear as soon as there is a character mismatch\.  | 

## Use cases<a name="codewhisperer-user-cases"></a>

Here are common ways for you to utilize CodeWhisperer while working in AWS Cloud9 projects\.

### Example: Single\-line code completion<a name="codewhisperer-user-cases"></a>

When you start typing out single lines of code, CodeWhisperer makes suggestions based on your current and previous inputs\.

In the example below, in Java, a user enters the string `public` into an existing class\.

Based on the input, CodeWhisperer generates a suggestion for the signature of the main method\. 

![\[An example of the single-line completion feature.\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/cw-c9-single-line-completion.gif)

### Example: Block completion<a name="codewhisperer-user-cases-block"></a>

Block completion is used to complete your `if/for/while/try` code blocks\.

In the example below, in Java, a user enters the signature of an `if` statement\. The body of the statement is a suggestion from CodeWhisperer\.

![\[An example of the block completion feature.\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/cw-c9-block-completion.gif)

### Example: Full function generation from a comment<a name="codewhisperer-user-cases-functions"></a>

CodeWhisperer can generate an entire function based on a comment that you've written\. As you finish your comment CodeWhisperer will suggest a function signature\. If you accept the suggestion, CodeWhisperer automatically advances your cursor to the next part of the function and makes a suggestion\. Even if you enter an additional comment or line of code in between suggestions, CodeWhisperer will refactor based on your input\.

The following list contains examples of how CodeWhisperer makes suggestions and advances you through the entire process of creating a function\.

1. In the example below, in Java, a user inputs a comment\. CodeWhisperer suggests a function signature\.

   After the user accepts that suggestion, CodeWhisperer suggests a function body\.  
![\[An example of a function generated from a comment.\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/cw-c9-function-from-comment.gif)

1. In the image below, a user inputs a comment in the body of the function prior to accepting a suggestion from CodeWhisperer\. On the following line, CodeWhisperer generates a suggestion based on the comment\.  
![\[An example of a function generated from a comment inside an existing block of code.\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/cw-c9-function-from-comment-within-block.gif)

### Example: Single\-line comment completion<a name="codewhisperer-user-cases-comment"></a>

In the example below, in Java, the user starts to input a comment, and CodeWhisperer generates a suggestion to complete the comment\.

![\[An example of comment completion.\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/cw-c9-comment-completion.gif)

### Example: Docstring and Javadoc completion<a name="codewhisperer-user-cases-docstring"></a>

The following example is adapted from [an example on the Oracle website](https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html)\.

In the example below, in Java, the user enters a docstring\. CodeWhisperer suggests a function to process the docstring\.

![\[An example of code completion based on a Javadoc.\]](http://docs.aws.amazon.com/cloud9/latest/user-guide/images/cw-c9-javadoc.gif)

### Code reference tracking<a name="codewhisperer-origin-tracker"></a>

CodeWhisperer learns, in part, from open\-source projects\. Sometimes, a suggestion it's giving you may be similar to a specific piece of training data\. Keeping this box checked allows CodeWhisperer to offer suggestions in such cases\. CodeWhisperer will also provide references, so that you can learn more about where the training data comes from\. Unchecking this box will cause CodeWhisperer to hide recommendations that have references associated with them\.

### Supported programming languages<a name="codewhisperer-supported-languages"></a>

CodeWhisperer supports the following languages:
+ Python
+ Java
+ JavaScript
+ C\#
+ TypeScript