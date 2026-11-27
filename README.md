# David Oso — Cloud Engineering & Cloud Security Portfolio

Hands-on infrastructure, automation, observability, IAM, and security projects built to demonstrate how I approach real operational problems: **design, deploy, secure, validate, monitor, troubleshoot, and clean up**.

## Featured projects

| Project | Focus | Highlights |
| --- | --- | --- |
| [DevOps ECS Tech Challenge](https://github.com/dexter210/devops-ecs-tech-challenge) | Cloud Engineering / DevOps | ECS Fargate, Docker, Terraform, GitHub Actions, OIDC, ALB, autoscaling |
| [AWS EKS CI/CD & GitOps Tech Challenge](https://github.com/dexter210/tech-challenge-2) | Cloud Engineering / DevOps | EKS, Terraform, Helm, Jenkins, GitHub Actions, Argo CD, HPA, Cluster Autoscaler |
| [AWS Terraform & Ansible Infrastructure](https://github.com/dexter210/tech-challenge-3) | Cloud Engineering / Automation | EC2, S3, VPC, IAM, Terraform, Ansible, Nginx |
| [Microsoft Sentinel SOC Lab](https://github.com/dexter210/MS-soc-lab) | Cloud Security / Detection Engineering | Azure VM, AMA/DCR, KQL, Microsoft Sentinel, MITRE ATT&CK, incident investigation |
| [Active Directory Automation](https://github.com/dexter210/Active-Directory-) | Systems / IAM | PowerShell, AD DS, bulk user provisioning, OU management, safer credential handling |
| [Phishing Awareness Simulation](https://github.com/dexter210/Phishing-Campaign) | Security Awareness | GoPhish, controlled simulation workflow, defensive security considerations |

## AWS projects

### [01 — Legacy Application Migration to AWS](project-01-legacy-migration/README.md)

Rehosted a traditional WordPress/LAMP workload on Ubuntu EC2 and documented the complete lifecycle from provisioning through cleanup.

**Demonstrated:**
- Amazon EC2 and EBS
- Ubuntu Linux administration
- Apache, PHP, MySQL, WordPress
- security groups and SSH restriction
- CloudWatch monitoring and CPU alerting
- logs, service health, and resource validation
- credential rotation and cleanup practices

### [02 — Deploying Microservices on Amazon EKS](project-02-eks-deployment/README.md)

Built and validated a managed Kubernetes application platform on Amazon EKS using Helm, persistent EBS storage, Metrics Server, and Horizontal Pod Autoscaling.

**Status:** completed.

**Demonstrated:**
- Amazon EKS 1.36 with a two-node managed node group
- Helm-based WordPress + MariaDB deployment
- MariaDB StatefulSet with encrypted gp3 EBS persistent storage
- public application access through an AWS Load Balancer
- Kubernetes Metrics Server
- CPU-based HPA with a 50% target
- successful scale-out from **1 → 5 WordPress replicas**
- successful scale-down from **5 → 1 replica**
- troubleshooting of CloudFormation node-group rollback, Free Tier instance eligibility, Git Bash path rewriting, readiness timeouts, Helm YAML errors, and an `OOMKilled` container

### [03 — Strategic Solutions for Cloud Engineering Challenges](project-03-cloud-engineering-solutions/README.md)

Built a practical cloud-operations strategy project covering five common engineering challenges: inconsistent data, reactive monitoring, team resource constraints, weak documentation, and limited CI/CD adoption.

**Status:** completed.

**Demonstrated:**
- Python-based data transformation and schema standardization
- data-quality validation with **8/8 records passing**
- proactive monitoring across CPU, memory, disk, HTTP 5xx, latency, and availability
- alert tuning that reduced simulated alert volume from **20 → 8 (60% reduction)**
- workload prioritization using impact × urgency scoring
- workload visibility and cross-training coverage planning
- reusable operational runbook and onboarding templates
- local CI validation plus successful GitHub Actions execution
- practical mappings to AWS Glue, S3, CloudWatch, and production observability workflows


### [04 — GitOps Deployment to Amazon ECS Fargate](https://github.com/dexter210/devops-ecs-tech-challenge)

I deployed a containerized React frontend and Express backend on Amazon ECS Fargate using Terraform, then automated deployments with GitHub Actions and AWS OIDC. I validated ALB routing, investigated container logs, and tested backend autoscaling from **1 → 4 → 1 tasks**.

[View the code, architecture, deployment steps, and screenshots →](https://github.com/dexter210/devops-ecs-tech-challenge)

### [05 — AWS Three-Tier Java Application](https://github.com/dexter210/aws-3-tier-java-app)

 A three-tier Java application deployment on AWS, covering the web, application, and database layers.

**Planned focus:**
- AWS networking and security
- Java application build and deployment
- Web, application, and database tiers
- Connectivity testing and troubleshooting
- Resource cleanup and cost review

### [06 — Amazon EKS CI/CD & GitOps Tech Challenge](https://github.com/dexter210/tech-challenge-2)

Built and validated a containerized **Python/Flask application on Amazon EKS**, provisioning AWS infrastructure with Terraform and deploying Kubernetes resources with Helm. Implemented two separate delivery workflows: **Jenkins → Amazon ECR → EKS** and **GitHub Actions (OIDC) → ECR → Argo CD GitOps synchronization**.

**Demonstrated:**
- Terraform-provisioned VPC, IAM roles, Amazon ECR, Amazon EKS, and managed worker nodes
- Docker containerization and Helm deployments exposed through an Application Load Balancer
- Jenkins CI/CD automation to build, push, and deploy versioned container images
- GitHub Actions and Argo CD synchronization on the separate [`gitops` branch](https://github.com/dexter210/tech-challenge-2/tree/gitops)
- Kubernetes Horizontal Pod Autoscaler testing with memory-based scale-out from **1 → 3 replicas** and scale-down to **1**
- Cluster Autoscaler validation and documented rollout evidence

[View the code, deployment architecture, walkthrough, and screenshots →](https://github.com/dexter210/tech-challenge-2)

### [07 — AWS Infrastructure with Terraform and Ansible](https://github.com/dexter210/tech-challenge-3)

Provisioned an Amazon EC2 web server and supporting AWS infrastructure with Terraform, then used Ansible to install Nginx and deploy a Hello World page.

**Demonstrated:**
- Terraform-managed VPC, public subnet, internet gateway, route table, and security group
- Amazon EC2 and a private, encrypted Amazon S3 bucket
- An EC2 IAM role with project bucket read access and IMDSv2 enforcement
- Ansible configuration of Nginx and a repeat run with no changes
- Verification of the webpage, IAM role, and S3 access
- Terraform teardown of the lab infrastructure after validation

[View the code, architecture, deployment steps, and screenshots →](https://github.com/dexter210/tech-challenge-3)

## Core technical areas

### Cloud
- AWS
- Amazon EC2
- Amazon EBS
- Amazon EKS
- VPC / subnet / route-table concepts
- IAM
- CloudWatch

### Containers & automation
- Kubernetes
- `kubectl`
- `eksctl`
- Ansible
- Helm
- Python automation
- GitHub Actions
- PowerShell
- Terraform
- Git / GitHub

### Systems & networking
- Linux administration
- Windows Server
- Active Directory
- DNS / HTTP / TLS fundamentals
- Security Groups
- SSH

### Security & observability
- Microsoft Sentinel
- Kusto Query Language (KQL)
- Windows Security Events
- Azure Monitor Agent / DCR
- MITRE ATT&CK
- Kubernetes Metrics Server
- proactive monitoring and threshold design
- alert tuning and alert-fatigue reduction
- monitoring, alerting, and troubleshooting
- incident triage and investigation

### Data, reliability & operations
- schema standardization and data contracts
- data-quality validation
- operational runbooks and onboarding design
- workload prioritization
- cross-training and backup ownership
- CI/CD adoption strategy

## Engineering principles demonstrated across the portfolio

- **Validate, don't assume.** A successful infrastructure API call is not the same as a healthy application.
- **Security is part of deployment.** Restrict administrative access, minimize privilege, protect credentials, and verify exposure.
- **Observability matters.** Metrics, logs, alerts, and service checks are used to prove system health.
- **Troubleshooting is part of the project.** Failed deployments are documented with the same rigor as successful ones.
- **Cloud resources have a lifecycle.** Cleanup and cost verification are treated as required engineering steps.
- **Portfolio claims must be verifiable.** Project documentation distinguishes completed work from planned or in-progress work.

## Repository roadmap

- [x] Legacy application migration to AWS
- [x] Complete Amazon EKS worker-node deployment
- [x] Deploy application through Helm
- [x] Validate Kubernetes Metrics Server and HPA
- [x] Add Infrastructure as Code project
- [x] Complete cloud engineering strategy / CI validation project
- [x] Add containerized GitOps / ECS Fargate deployment project
- [x] Link Amazon EKS CI/CD and GitOps Tech Challenge 2
- [x] Link AWS Terraform and Ansible Tech Challenge 3
- [ ] Complete AWS three-tier Java application deployment
- [ ] Add disaster-recovery architecture and recovery validation

## Security note

These repositories contain learning environments and sanitized evidence. Credentials, private keys, tokens, unredacted cloud identifiers, and other secrets should never be committed to source control.

---

**Primary portfolio focus:** Cloud Engineering • Cloud Security • Systems / IAM • Observability
