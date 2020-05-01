# Managing access using policies<a name="sec-auth-with-identities"></a>

You can have valid credentials to authenticate your requests, but unless you have permissions, you cannot create or access AWS Cloud9 resources\. For example, you must have permissions to create, share, or delete an AWS Cloud9 development environment\.

Every AWS resource is owned by an AWS account, and permissions to create or access a resource are governed by permissions policies\. An account administrator can attach permissions policies to IAM identities \(that is, users, groups, and roles\)\.

When you grant permissions, you decide who is getting the permissions, the resources they can access, and the actions that can be performed on those resources\.