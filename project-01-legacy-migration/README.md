# Migrating a Legacy Application to AWS

## Project Overview

This project demonstrates the migration of a traditional web application environment to Amazon Web Services using a rehost, or lift-and-shift, migration approach.

I provisioned an Ubuntu EC2 instance and recreated a LAMP-based application stack using Apache, PHP, MySQL, and WordPress. I then configured network access, secured the database and server, validated application functionality, reviewed logs and resource utilization, implemented CloudWatch monitoring, and cleaned up the AWS resources after completing the project.

The goal was not only to deploy a working application, but to understand the full cloud migration lifecycle:

**Provision → Configure → Secure → Deploy → Validate → Monitor → Optimize → Clean Up**

---

## Key Technologies

`AWS EC2` `Ubuntu Linux` `Apache` `PHP` `MySQL` `WordPress` `Security Groups` `SSH` `Amazon CloudWatch` `EBS`

---

## Architecture

![AWS Legacy Migration Architecture](images/Aws-legacy-migration-architecture.png)
