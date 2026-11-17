# VPC and connectivity practice

I created a custom VPC with a public subnet, internet gateway and route table, then worked with a design containing public and private subnets across two Availability Zones. The later work used NAT and separate routing for the private subnets.

I checked subnet associations, routes and security-group rules when an instance or website was unreachable. I used ping, traceroute, connection-listing tools, curl and wget to investigate different parts of the connection.

An Elastic IP exercise showed the associated public address staying the same through a stop/start test.

When a web server is unreachable, I check the route, the public address, the traffic rules and the port the service is listening on.

[Back to AWS labs](README.md)
