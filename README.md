# David Oso — Cloud Engineering & Cloud Security Portfolio

Hands-on infrastructure, automation, observability, IAM, and security projects built to demonstrate how I approach real operational problems: **design, deploy, secure, validate, monitor, troubleshoot, and clean up**.

## Featured projects

| Project | Focus | Highlights |
| --- | --- | --- |
| [AWS Cloud Engineering Projects](https://github.com/dexter210/aws-cloud-projects) | Cloud Engineering | EC2, ECS Fargate, ECR, ALB, Terraform, IAM, CloudWatch, EKS, Kubernetes autoscaling, Python automation, GitHub Actions, OIDC |
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


### [04 — GitOps Deployment to Amazon ECS Fargate](project-04-ecs-fargate-gitops/README.md)

Built and validated a containerized React + Express application platform on Amazon ECS Fargate using Terraform and GitHub Actions GitOps.

**Status:** completed.

**Demonstrated:**
- Dockerized React frontend and Express backend
- Amazon ECR image repositories
- ECS Fargate task definitions and services
- Application Load Balancer path routing for `/` and `/api/*`
- CloudWatch logging and deployment troubleshooting
- CPU-based ECS Service Auto Scaling from **1 → 4 → 1 tasks**
- Terraform Infrastructure as Code
- GitHub Actions CI/CD with commit-SHA image tagging
- GitHub OIDC authentication using short-lived AWS credentials
- end-to-end deployment validation with healthy ALB targets and HTTP 200 responses

### [05 — AWS Three-Tier Java Application](project-05-aws-three-tier-java/README.md)

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
- [ ] Complete AWS three-tier Java application deployment
- [ ] Add disaster-recovery architecture and recovery validation

## Security note

These repositories contain learning environments and sanitized evidence. Credentials, private keys, tokens, unredacted cloud identifiers, and other secrets should never be committed to source control.

---

**Primary portfolio focus:** Cloud Engineering • Cloud Security • Systems / IAM • Observability
