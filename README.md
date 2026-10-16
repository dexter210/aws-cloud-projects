# David Oso — Cloud Engineering & Cloud Security Portfolio

Hands-on infrastructure, automation, observability, IAM, and security projects built to demonstrate how I approach real operational problems: **design, deploy, secure, validate, monitor, troubleshoot, and clean up**.

## Featured projects

| Project | Focus | Highlights |
| --- | --- | --- |
| [AWS Cloud Engineering Projects](https://github.com/dexter210/aws-cloud-projects) | Cloud Engineering | EC2, Linux, networking, IAM, CloudWatch, application migration, EKS learning |
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

### [02 — Deploying Applications on Amazon EKS](project-02-eks-deployment/README.md)

Amazon EKS learning project focused on managed Kubernetes, worker-node provisioning, Helm, and autoscaling.

**Current status:** in progress.

The first provisioning attempt successfully created the EKS control plane, but the managed node group failed to complete. The project documents the troubleshooting path through `kubectl`, EKS node-group status, CloudFormation rollback, EC2/Auto Scaling checks, and cleanup rather than claiming a successful deployment that did not occur.

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
- PowerShell
- Terraform fundamentals
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
- monitoring, alerting, and troubleshooting
- incident triage and investigation

## Engineering principles demonstrated across the portfolio

- **Validate, don't assume.** A successful infrastructure API call is not the same as a healthy application.
- **Security is part of deployment.** Restrict administrative access, minimize privilege, protect credentials, and verify exposure.
- **Observability matters.** Metrics, logs, alerts, and service checks are used to prove system health.
- **Troubleshooting is part of the project.** Failed deployments are documented with the same rigor as successful ones.
- **Cloud resources have a lifecycle.** Cleanup and cost verification are treated as required engineering steps.
- **Portfolio claims must be verifiable.** Project documentation distinguishes completed work from planned or in-progress work.

## Repository roadmap

- [x] Legacy application migration to AWS
- [ ] Complete Amazon EKS worker-node deployment
- [ ] Deploy application through Helm
- [ ] Validate Kubernetes Metrics Server and HPA
- [ ] Add Infrastructure as Code project
- [ ] Add CI/CD and container security project
- [ ] Add disaster-recovery architecture and recovery validation

## Security note

These repositories contain learning environments and sanitized evidence. Credentials, private keys, tokens, unredacted cloud identifiers, and other secrets should never be committed to source control.

---

**Primary portfolio focus:** Cloud Engineering • Cloud Security • Systems / IAM • Observability
