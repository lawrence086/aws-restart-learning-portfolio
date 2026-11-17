# Load balancing and Auto Scaling

I used a web-server image with an Application Load Balancer and an Auto Scaling group spread across two Availability Zones. The group started with two instances, a minimum of two and a maximum of four. A CPU target of 50% and a stress workload let me observe the group scale to three and then four instances.

When a target group was missing from the expected list, I checked its VPC and recreated it in the correct one.

The application remained available through the load balancer after I removed the original standalone web server.

[Back to AWS labs](README.md)
