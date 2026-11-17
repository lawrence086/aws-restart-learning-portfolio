# CloudWatch and SNS

I created an SNS topic, confirmed the email subscription and connected it to a CloudWatch CPU alarm. The lab alarm used a threshold above 60%, one evaluation point and a one-minute period. I applied a stress workload for roughly 400 seconds and observed the alarm move from OK to Alarm, followed by the notification. I also worked with a dashboard.

This gave me a practical connection between a metric, a rule and a notification. I needed to check the subscription as well as the alarm settings when looking for the email.

[Back to AWS labs](README.md)
