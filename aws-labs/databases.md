# RDS and Aurora practice

The RDS challenge connected a client on EC2 to a MySQL database. I checked the database connection and port 3306 access, then created a training table with a student identifier as its primary key and a required name field. Client/package compatibility also needed attention.

In Aurora, I queried the supplied world dataset, including country population and GNP data. A separate Multi-AZ RDS exercise used an address-book application to create, read, update and delete records.

These exercises helped me separate database provisioning, network access, client setup and SQL.

[Back to AWS labs](README.md)
