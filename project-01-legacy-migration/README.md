# Migrating a Legacy Application to AWS

## Project Overview

This project demonstrates the migration of a traditional web application environment to Amazon Web Services using a rehost, or lift-and-shift, migration approach.

I provisioned an Ubuntu EC2 instance and recreated a LAMP-based application stack using Apache, PHP, MySQL, and WordPress. I then secured the environment, validated application functionality, reviewed logs and system resources, implemented CloudWatch monitoring, and removed the AWS resources after completing the project.

The goal was not only to deploy a working application, but to understand the complete migration lifecycle:

**Provision → Configure → Secure → Deploy → Validate → Monitor → Optimize → Clean Up**

---

## Architecture

![AWS Legacy Migration Architecture](images/aws-legacy-migration-architecture.png)

### Architecture Overview

The migration environment used a single Ubuntu EC2 instance to host the complete application stack.

* **Amazon EC2** provided the compute infrastructure.
* **Ubuntu Linux** served as the operating system.
* **Apache** handled incoming HTTP requests.
* **PHP** provided the runtime required by WordPress.
* **WordPress** served as the migrated application.
* **MySQL** stored the application's persistent data.
* **Amazon EBS** provided persistent storage for the EC2 instance.
* **AWS Security Groups** controlled inbound network traffic.
* **SSH** administrative access was restricted to my public IP address.
* **Amazon CloudWatch** provided infrastructure monitoring and CPU alerting.

This single-server architecture was intentionally used as the initial migration baseline. Later in the project, I evaluated how the workload could be redesigned for a more production-ready environment.

---

## Technologies Used

| Technology        | Purpose                               |
| ----------------- | ------------------------------------- |
| Amazon EC2        | Cloud compute                         |
| Ubuntu Linux      | Server operating system               |
| Apache            | Web server                            |
| PHP               | Application runtime                   |
| MySQL             | Relational database                   |
| WordPress         | Web application                       |
| Amazon EBS        | Persistent block storage              |
| Security Groups   | Network access control                |
| SSH               | Secure remote administration          |
| Amazon CloudWatch | Monitoring and alerting               |
| Linux CLI         | Administration and troubleshooting    |
| SQL               | Database configuration and validation |

---

# 1. Provisioning the EC2 Server

I provisioned an Ubuntu EC2 instance to serve as the cloud-based replacement for the legacy server.

The instance hosted the complete application stack and was assigned:

* a public IPv4 address for external access
* a private IPv4 address for internal AWS networking
* an EBS root volume for persistent storage
* an EC2 security group for network access control

### Network Rules

I configured the security group with:

```text
HTTP
TCP 80
Source: 0.0.0.0/0

SSH
TCP 22
Source: My Public IP
```

Restricting SSH to my IP reduced unnecessary administrative exposure.

### Evidence

![EC2 Instance](images/01-ec2-instance-running.png)

![Security Group](images/02-security-group-rules.png)

---

# 2. Connecting Securely with SSH

I connected to the EC2 instance using SSH and the private key associated with the server.

```bash
ssh -i "legacy-migration-key.pem" ubuntu@EC2_PUBLIC_IP
```

I verified that I was connected to the remote Ubuntu server using:

```bash
whoami
hostname
hostname -I
```

This confirmed that the remote EC2 instance was successfully reachable and that key-based authentication was functioning.

### Evidence

![SSH Connection](images/03-ssh-connection.png)

---

# 3. Updating and Patching Ubuntu

Before deploying application services, I patched the operating system.

```bash
sudo apt update
sudo apt upgrade -y
```

Updating the server before installation helped establish a more secure baseline and ensured that the latest available package updates were installed.

### Evidence

![Ubuntu Patching](images/04-ubuntu-patching.png)

---

# 4. Installing Apache

I installed Apache to provide the HTTP web-server layer.

```bash
sudo apt install apache2 -y
```

I verified that Apache was running:

```bash
sudo systemctl status apache2
```

I then opened the EC2 public IPv4 address in a browser and confirmed that the Apache default page loaded successfully.

This validated end-to-end connectivity between:

```text
Browser
   ↓
Internet
   ↓
Security Group
   ↓
EC2
   ↓
Apache
```

### Evidence

![Apache Browser Test](images/06-apache-browser-test.png)

---

# 5. Installing and Validating PHP

WordPress requires PHP to execute application code.

I installed PHP along with the Apache and MySQL integration packages:

```bash
sudo apt install php libapache2-mod-php php-mysql -y
```

I verified PHP:

```bash
php -v
```

I then created a temporary PHP test page:

```bash
echo '<?php phpinfo(); ?>' | sudo tee /var/www/html/info.php
```

I accessed the page through the EC2 public IP to confirm Apache was successfully processing PHP.

After validation, I removed the diagnostic page:

```bash
sudo rm /var/www/html/info.php
```

This prevented unnecessary server information from remaining publicly exposed.

### Evidence

![PHP Validation](images/07-php-validation.png)

---

# 6. Installing MySQL

I installed MySQL to provide the persistent database layer required by WordPress.

```bash
sudo apt install mysql-server -y
```

I verified that the service was running:

```bash
sudo systemctl status mysql
```

I also enabled MySQL to start automatically when the server boots:

```bash
sudo systemctl enable mysql
```

I validated the database engine using:

```bash
sudo mysql
```

and:

```sql
SHOW DATABASES;
```

### Evidence

![MySQL Validation](images/09-mysql-databases.png)

---

# 7. Hardening MySQL

I ran the MySQL security configuration utility:

```bash
sudo mysql_secure_installation
```

The hardening process included:

* stronger password requirements
* removal of anonymous users
* restriction of remote root access
* removal of the default test database
* reloading of privilege settings

This reduced unnecessary default database exposure.

---

# 8. Creating the WordPress Database

I created a dedicated WordPress database:

```sql
CREATE DATABASE wordpress_db;
```

I then created a dedicated application account:

```sql
CREATE USER 'wordpress_user'@'localhost'
IDENTIFIED BY '<REDACTED>';
```

I granted access only to the WordPress database:

```sql
GRANT ALL PRIVILEGES
ON wordpress_db.*
TO 'wordpress_user'@'localhost';

FLUSH PRIVILEGES;
```

I verified the permissions using:

```sql
SHOW GRANTS FOR 'wordpress_user'@'localhost';
```

Using a dedicated application account instead of the MySQL root account reduced unnecessary privilege.

### Evidence

![Database Permissions](images/12-database-permissions.png)

---

# 9. Deploying WordPress

I downloaded WordPress directly onto the EC2 instance:

```bash
wget https://wordpress.org/latest.tar.gz
```

I extracted the application:

```bash
tar -xvzf latest.tar.gz
```

I removed the Apache default landing page:

```bash
sudo rm -f /var/www/html/index.html
```

I copied WordPress into Apache's web root:

```bash
sudo cp -r wordpress/. /var/www/html/
```

I then configured ownership:

```bash
sudo chown -R www-data:www-data /var/www/html
```

I configured directories with `755` permissions and files with `644` permissions.

```bash
sudo find /var/www/html -type d -exec chmod 755 {} \;
sudo find /var/www/html -type f -exec chmod 644 {} \;
```

### Evidence

![WordPress Files](images/13-wordpress-files.png)

---

# 10. Connecting WordPress to MySQL

I created the active WordPress configuration file:

```bash
sudo cp /var/www/html/wp-config-sample.php /var/www/html/wp-config.php
```

I configured the database connection:

```php
define( 'DB_NAME', 'wordpress_db' );
define( 'DB_USER', 'wordpress_user' );
define( 'DB_PASSWORD', '<REDACTED>' );
define( 'DB_HOST', 'localhost' );
```

Because WordPress and MySQL were hosted on the same EC2 instance, `localhost` was used as the database host.

I restarted Apache:

```bash
sudo systemctl restart apache2
```

Successfully reaching the WordPress installation page confirmed that WordPress could communicate with MySQL.

### Evidence

![WordPress Installer](images/15-wordpress-installer.png)

---

# 11. Completing and Validating WordPress

I completed the WordPress installation and logged into the administration dashboard.

I then connected directly to the database:

```bash
mysql -u wordpress_user -p
```

I selected the WordPress database:

```sql
USE wordpress_db;
```

and verified the application schema:

```sql
SHOW TABLES;
```

WordPress had automatically created tables including:

```text
wp_posts
wp_users
wp_options
wp_comments
wp_terms
```

This confirmed that the application was successfully persisting data in MySQL.

I also created and published a test WordPress post to verify the complete write-and-read application workflow.

### Evidence

![WordPress Dashboard](images/16-wordpress-dashboard.png)

![WordPress Database Tables](images/17-wordpress-database-tables.png)

![Working WordPress Site](images/18-working-wordpress-site.png)

---

# 12. Post-Migration Validation

I performed several operational checks instead of relying only on the website loading successfully.

## HTTP Validation

```bash
curl -I http://localhost
```

## Apache Access Logs

```bash
sudo tail -n 20 /var/log/apache2/access.log
```

## Apache Error Logs

```bash
sudo tail -n 20 /var/log/apache2/error.log
```

## Memory Utilization

```bash
free -h
```

## Disk Utilization

```bash
df -h
```

## Service Health

```bash
systemctl is-active apache2
systemctl is-active mysql
```

## Startup Configuration

```bash
systemctl is-enabled apache2
systemctl is-enabled mysql
```

These checks validated application availability, resource utilization, logging, and service health.

### Evidence

![HTTP Validation](images/19-http-validation.png)

![Apache Logs](images/20-apache-access-logs.png)

![Resource Utilization](images/21-resource-utilization.png)

![Service Health](images/22-service-health.png)

---

# 13. Security Review and Hardening

After validating functionality, I reviewed the environment from a security perspective.

## Network Exposure

The final security group allowed:

```text
HTTP 80 → Internet
SSH 22 → My IP
```

I did not expose MySQL port `3306` publicly.

## Listening Ports

I reviewed active network listeners:

```bash
sudo ss -tulpn
```

This allowed me to compare Linux-level listening services with AWS security-group rules.

## Credential Rotation

A database password became visible during troubleshooting.

I treated the credential as exposed and rotated it rather than continuing to use it.

I updated:

* the MySQL `wordpress_user` password
* the corresponding password inside `wp-config.php`

## Protecting `wp-config.php`

Because `wp-config.php` contains database credentials, I restricted its permissions:

```bash
sudo chmod 440 /var/www/html/wp-config.php
```

I verified the permissions:

```bash
ls -l /var/www/html/wp-config.php
```

## Post-Hardening Validation

After applying the changes, I verified that the application was still healthy:

```bash
systemctl is-active apache2
systemctl is-active mysql
curl -I http://localhost
```

### Evidence

![Final Security Group](images/23-final-security-group.png)

![Listening Ports](images/24-listening-ports.png)

![WP Config Permissions](images/25-wp-config-permissions.png)

---

# 14. Monitoring and Alerting

I used Amazon CloudWatch to review EC2 infrastructure metrics including:

* CPU utilization
* network traffic
* EC2 status checks

I also created a CloudWatch CPU alarm:

```text
Alarm: legacy-migration-high-cpu
Metric: CPUUtilization
Threshold: > 80%
```

This demonstrated proactive infrastructure alerting rather than relying only on manual server inspection.

I also learned an important observability concept:

```text
Healthy EC2 infrastructure ≠ Healthy application
```

An EC2 instance can be healthy while Apache, MySQL, or WordPress is unavailable.

For this reason, I combined CloudWatch metrics with application-level and operating-system validation.

### Evidence

![CloudWatch Monitoring](images/27-cloudwatch-monitoring.png)

![CloudWatch CPU Alarm](images/28-cloudwatch-cpu-alarm.png)

---

# 15. Production Architecture Improvements

The single-server architecture successfully demonstrated the migration but would not be my preferred design for a critical production workload.

A more production-ready architecture could include:

* Application Load Balancer
* multiple EC2 instances
* Auto Scaling
* Amazon RDS
* private subnets
* HTTPS
* AWS Certificate Manager
* AWS Secrets Manager
* AWS WAF
* centralized logging
* automated backups
* Multi-AZ deployment

## Proposed Production Architecture

```text
Internet
   ↓
Route 53 / DNS
   ↓
Application Load Balancer
   ↓
Private EC2 Application Tier
   ↓
Amazon RDS MySQL
   ↓
Automated Backups
```

Separating the application and database tiers would improve:

* availability
* scalability
* failure isolation
* backup capability
* security
* maintainability

---

# 16. Cost Management

Before deleting the environment, I reviewed the AWS resources that could generate charges.

Primary cost drivers included:

* EC2 compute
* EBS storage
* public IPv4 usage
* CloudWatch resources

I reviewed:

```text
EC2 Instances
EBS Volumes
CloudWatch Alarms
Elastic IP Addresses
Snapshots
Load Balancers
RDS
NAT Gateways
```

This reinforced an important cloud cost principle:

```text
Stopping an EC2 instance does not necessarily remove all billable resources.
```

---

# 17. Resource Cleanup

After completing the migration, validation, security review, monitoring, and documentation, I terminated the EC2 instance.

I then verified that no unnecessary resources remained.

The cleanup process included:

```text
EC2 instance → terminated
EBS volume → removed if no longer needed
CloudWatch alarm → deleted
Elastic IP → none remaining
Snapshots → none remaining
Load Balancer → none
RDS → none
NAT Gateway → none
```

### Evidence

![EC2 Terminated](images/31-ec2-terminated.png)

---

# Challenges and Troubleshooting

## SSH Authentication Failure

During the initial SSH connection, I encountered:

```text
Permission denied (publickey)
```

The EC2 instance was reachable, but the correct SSH key was not being used.

I resolved the issue by explicitly specifying the correct private key:

```bash
ssh -i "legacy-migration-key.pem" ubuntu@EC2_PUBLIC_IP
```

This demonstrated the difference between network connectivity and authentication.

---

## MySQL Password Policy

MySQL initially rejected weak passwords because the configured validation policy required stronger credentials.

Instead of weakening the policy, I created a password that satisfied the required complexity.

---

## No Database Selected

When running:

```sql
SHOW TABLES;
```

I initially received:

```text
ERROR 1046: No database selected
```

I resolved the issue by selecting:

```sql
USE wordpress_db;
```

before querying the database.

---

## Credential Exposure

A database password became visible during troubleshooting.

I treated the password as compromised and rotated it.

This reinforced an important security lesson:

**Exposed credentials should be rotated, not ignored.**

---

# Migration Validation Summary

| Layer            | Validation                                      |
| ---------------- | ----------------------------------------------- |
| Infrastructure   | EC2 and CloudWatch                              |
| Network          | Security Groups and listening ports             |
| Operating System | Linux resource checks                           |
| Web Server       | Apache service and HTTP validation              |
| Runtime          | PHP execution                                   |
| Application      | WordPress dashboard and public site             |
| Database         | MySQL tables and persistence                    |
| Logging          | Apache access and error logs                    |
| Monitoring       | CloudWatch metrics                              |
| Alerting         | CPU utilization alarm                           |
| Security         | SSH restriction, DB permissions, file hardening |
| Cost             | Resource review and cleanup                     |

---

# Key Lessons Learned

This project reinforced that a cloud migration involves much more than moving an application onto a virtual machine.

I gained practical experience with:

* EC2 provisioning
* Linux administration
* SSH troubleshooting
* Apache configuration
* PHP deployment
* MySQL administration
* SQL permissions
* WordPress deployment
* application-to-database integration
* filesystem permissions
* cloud networking
* security-group configuration
* server monitoring
* log analysis
* CloudWatch
* alerting
* credential management
* cost awareness
* AWS resource cleanup

Most importantly, I learned to evaluate a migration across multiple areas:

```text
Does it work?
Is it secure?
Can I monitor it?
Can I troubleshoot it?
Can it scale?
Is the data protected?
Is access restricted?
Is cost controlled?
```

---

# Final Result

The project successfully demonstrated the migration of a traditional LAMP-based web application architecture to AWS.

The final environment included:

```text
Amazon EC2
Ubuntu Linux
Apache
PHP
WordPress
MySQL
Amazon EBS
Security Groups
SSH
Amazon CloudWatch
CloudWatch Alerting
```

I validated the migration across infrastructure, networking, operating system, application, database, logging, monitoring, security, and cost before safely removing the temporary AWS resources.

---

## Project Status

**Migration:** Completed ✅
**Application Validation:** Completed ✅
**Database Validation:** Completed ✅
**Security Review:** Completed ✅
**Monitoring:** Completed ✅
**Cost Review:** Completed ✅
**Cleanup:** Completed ✅
