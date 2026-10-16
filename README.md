# AWS Cloud Engineering Portfolio

Hands-on cloud infrastructure labs focused on deploying, securing, validating, monitoring, and cleaning up AWS workloads.

**Focus:** AWS • Linux • Networking • IAM • Observability • Infrastructure lifecycle management

## Projects

| Project | What I worked on | Status |
| --- | --- | --- |
| [01 — Legacy Application Migration to AWS](project-01-legacy-migration/README.md) | Hosted a WordPress/LAMP application on Ubuntu EC2, configured network access, validated the application and database, reviewed system logs, implemented CloudWatch CPU alerting, and documented cleanup. | Documented |
| 02 — Deploying Applications on Amazon EKS | Planned an EKS cluster and validated an `eksctl` configuration; encountered a managed-node-group provisioning failure and investigated CloudFormation rollback and Kubernetes node registration. | In progress — deployment not completed |

> **Accuracy note:** Project 02 is a work in progress. The existing evidence does **not** demonstrate a successful WordPress deployment, Helm rollout, or Horizontal Pod Autoscaler test on EKS.

## Demonstrated technologies

- **Compute and operating systems:** Amazon EC2, Ubuntu Linux, Apache, PHP
- **Networking and security:** VPC concepts, EC2 security groups, SSH access restrictions, IAM
- **Data and applications:** MySQL, WordPress, EBS
- **Observability and operations:** Amazon CloudWatch, logs, service-health checks, troubleshooting
- **Kubernetes learning in progress:** Amazon EKS, `eksctl`, `kubectl`, Helm, managed node groups

## How to explore this repository

Start with the [legacy migration project](project-01-legacy-migration/README.md) for the architecture, configuration commands, validation evidence, security controls, and lessons learned.

Project reports distinguish **completed work** from **planned exercises**. Screenshots and commands are intended to document hands-on learning, not to imply that every component is production-ready.

## Security and cost considerations

These projects are learning environments. Avoid committing credentials, private keys, tokens, or unredacted account identifiers. AWS resources can incur charges while running, and cleanup should always include checking related EC2, EBS, CloudFormation, networking, and load-balancing resources.

## Next improvements

- Finish diagnosing the EKS node-group failure before retrying cluster provisioning.
- Deploy an application with Helm only after worker nodes are healthy.
- Validate metrics availability before testing Horizontal Pod Autoscaling.
- Add architecture diagrams, reusable configuration files, validation commands, and explicit cleanup verification to future labs.
