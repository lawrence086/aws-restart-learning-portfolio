# Lab and exercise index

## Python

| Exercise | What I practised |
| --- | --- |
| Hello world | Running a script and printing output |
| Numeric data | Numbers, booleans, types and conversions |
| Strings | Input, concatenation and formatting |
| Categorising values | Identifying types in mixed data |
| Collections | Lists, tuples and dictionaries |
| Conditionals | Making decisions with branches |
| For loops | Repeating a task over a range |
| While loops | Repeating a task while a condition holds |
| Insulin strings | Counting characters in a sequence and working with their counts |
| Net charge | Using dictionaries to calculate charge at different pH values |
| [Analysing insulin sequences](python/insulin_sequences.py) | Reading, cleaning, validating, splitting and saving sequence data |
| [Vehicle inventory](python/fleet_inventory.py) | Reading CSV rows into dictionaries and converting numeric values |
| JSON files and weight calculations | Reading JSON, handling errors and reusing functions across modules |
| [Caesar cipher](python/caesar_cipher.py) | Using functions, parameters and return values to shift letters |
| Caesar cipher debugging | Working through four debugging exercises. The [cipher tests](python/test_exercises.py) check the portfolio example. |
| Python debugger | Working through basic `pdb` commands |
| System administration | Calling system commands with `os` and `subprocess` |
| Prime-number challenge | Using loops and divisibility to identify prime numbers |

## Linux

| Exercise | What I practised |
| --- | --- |
| Linux and SSH | Connecting to an EC2 instance, using manual pages and exploring system files |
| Command line | Checking the current user, host, uptime, time zone and command history |
| Users and groups | Creating accounts and groups, checking shared access and reading authentication logs |
| Editing files | Editing in Vim and nano, saving changes and handling a session timeout |
| Files and directories | Creating nested directories and moving, copying and removing files |
| Archives and logs | Compressing files with `gzip` and `tar`, writing a log with `sudo` and `tee`, and moving archives |
| Permissions and ownership | Using symbolic and numeric `chmod` and correcting a `chown` command that used the wrong username |
| Text processing | Using `tee`, `sort`, `grep`, `cut` and `sed` |
| Processes and scheduling | Inspecting processes with `ps` and `top`, then setting an hourly audit job in cron |
| [Bash backup script](linux/backup_folder.sh) | Building on the file backup lab by creating and checking a compressed archive |

The [Linux write-up](linux/README.md) includes the backup commands and the cron example.

## AWS and databases

| Lab | What I worked on |
| --- | --- |
| [AWS CLI](aws-labs/cli.md) | Installed the CLI, configured access and investigated an invalid-token error |
| [EC2](aws-labs/ec2.md) | Launched instances, checked the AMI region, corrected an HTTP port rule and investigated the startup script |
| [VPC networking](aws-labs/networking.md) | Built a VPC, worked with public and private subnets, tested connectivity and checked an Elastic IP through a stop/start |
| [Load balancing and Auto Scaling](aws-labs/scaling.md) | Used a load balancer and watched the group scale under CPU load |
| [S3 website](aws-labs/s3-website.md) | Edited CSS in Vim and used a Bash script to upload the changes |
| [Systems Manager](aws-labs/systems-manager.md) | Used inventory, Run Command, Parameter Store and Session Manager, and checked patch compliance on Linux and Windows |
| [IAM](aws-labs/iam.md) | Assigned users to groups and tested what each group could do |
| [KMS](aws-labs/kms.md) | Encrypted and decrypted a file with AWS Encryption CLI and a KMS key |
| [RDS and Aurora](aws-labs/databases.md) | Connected from EC2 to MySQL, queried the world dataset and used an address book backed by Multi-AZ RDS |
| [SQL](aws-labs/sql.md) | Created and changed records, restored the world dataset and practised filters, grouping and window functions |
| [CloudWatch and SNS](aws-labs/monitoring.md) | Configured a CPU alarm, triggered an email notification under load and worked with a dashboard |
| [Network Firewall](aws-labs/network-firewall.md) | Worked with stateless forwarding and used HTTP requests to test URI patterns |

See [Programme coverage](learning-map.md) for the weekly topics and scheduled activities.
