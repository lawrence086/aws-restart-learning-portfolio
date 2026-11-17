# Troubleshooting an EC2 web server

I launched training instances, worked through a compute challenge and investigated web-server setup problems.

One launch failed with `InvalidAMIID.NotFound`. I checked the selected region and used the matching image. When I checked web access, I found that the launch script allowed port 8080 and the web server listened on port 80. I corrected the security group rule.

I also checked the bootstrap script, where the application files were placed, and whether Apache/PHP services had started. A package command written for a different Amazon Linux version was another source of trouble.

I learned to check the web server and its listening port separately from the EC2 instance status.

[Back to AWS labs](README.md)
