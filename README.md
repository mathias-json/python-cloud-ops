# python-cloud-ops

*I created this repository to understand the meanings around Infrastructure-as-Code in cloud computing. I started this small project, alongside developing my python fluency, to see how the application of these concepts and cloud tools create the infrastructure. Some of the things I've come to learn that are key to building these environments so far are:*


- data structures, in how the cloud addresses and describes hardware
- control flow, for how engineers are able to audit and fix this hardware automatically


*These are all important elements which contribute to the provisioning of the cloud's infrastructure.*

*I am applying my understanding of the python language to create different scripts that are essential in the formation of a cloud's environment from start to finish; all these scripts will then be include together within the complete code profile.*


## 📜 Scripts


### 'server_config.py'
*I have given the server a name; an instance type which specifies the amount of resources in terms of compute, memory, storage, etc; a region for where the server will be based — the ‘is_encrypted’ is in reference to the server’s hard drive
Now that I have coded in the configuration for the server, as a security measure, I need to encrypt the hard drive rather than leave it open — I add to the dictionary to change the value from false to true and this will encrypt the drive; I also added a a HTTPS port.*

fundamental python use of: Dictionaries

### 'security_group.py'
*I have now added firewall rules to the code for the security group — the code removes the less-secure HTTP port 80 and added a port for monitoring network communication flow, along with enabling SSH and HTTPS.*

fundamental python use of: Lists, within Dictionaries

### 'remediate_bucket.py'
*The code I have added now implements 2 cloud storage folders that can be used to store and organize data — in this scenario, I have public assets and customer records. the issue here though is that customer records isin’t something that should be public facing so I have revoked access to customer records as this can result in a data leak in real environments.*

fundamental python use of: Lists of Dictionaries

### 'iam_audit.py'
*this section of the code adds myself as a user; the code checks that I, as an administrative IAM user, has multi-factor authentication is disabled; this would flag up as a security alert so include within the code to update the dictionary so that it enforces MFA.*

fundamental python use of: Conditionals

### 'audit_s3_loop.py'
*what this code does is inspects a list of s3 buckets where there buckets that are open buckets for public access and a singular one which isin’t. I create a for loop to scan each bucket in the list and identify which buckets are open and lock them down so that there is no public access to them. the script is to serve as a security remediation script.*

fundamental python use of: For Loops

### 'audit_ec2_loop.py'
*this piece of code I have added scans the multiple servers and identifies any production instance that have open SSH ports — the code then closes the ports automatically and prints the updated state. — this is significant to GRC as running this loop across multiple servers instantly reduces attack surfaces and produce logs to verify compliance.*

fundamental python use of: Logical Operators


