# Project 02 — Deploying Applications on Amazon EKS

## Status

**In progress.** The first provisioning attempt created the EKS control plane but the managed node group did not complete successfully. No successful WordPress/Helm deployment or HPA test is claimed yet.

## Goal

Build a managed Kubernetes environment on Amazon EKS and use Helm to deploy an application, then validate networking, observability, and autoscaling behavior.

## Planned stack

- Amazon EKS
- EC2 managed node groups
- Kubernetes
- `eksctl`
- `kubectl`
- Helm
- WordPress container image
- Kubernetes Service of type `LoadBalancer`
- Horizontal Pod Autoscaler
- Metrics Server
- load-generation tooling

## Local tooling verified

The following tools were installed and verified on Windows:

- AWS CLI
- `eksctl`
- `kubectl`
- Helm

AWS authentication was validated with STS, and `us-east-1` was selected as the lab region.

## Initial cluster plan

The first cluster configuration used:

- cluster name: `enterprise-cluster`
- Kubernetes: 1.36
- region: `us-east-1`
- availability zones: `us-east-1a`, `us-east-1b`
- managed node group: `standard-workers`
- instance type: `t3.medium`
- desired nodes: 2
- minimum nodes: 2
- maximum nodes: 3
- NAT Gateway: disabled for this short-lived lab
- SSH: disabled

See [cluster-config.yaml](cluster-config.yaml).

## What happened during the first attempt

The `eksctl create cluster` operation timed out while waiting for the managed node-group CloudFormation stack.

Troubleshooting showed:

1. The EKS control plane reached `ACTIVE`.
2. `kubectl` could connect to the cluster.
3. `kubectl get nodes -o wide` returned no registered nodes.
4. The managed node-group stack eventually entered `ROLLBACK_COMPLETE`.
5. No EKS worker EC2 instances remained visible after rollback.
6. The EKS cluster was later absent from `aws eks list-clusters`, confirming control-plane cleanup.

## Troubleshooting workflow

```bash
aws eks describe-cluster \
  --name enterprise-cluster \
  --region us-east-1

aws eks describe-nodegroup \
  --cluster-name enterprise-cluster \
  --nodegroup-name standard-workers \
  --region us-east-1

aws eks update-kubeconfig \
  --region us-east-1 \
  --name enterprise-cluster

kubectl get nodes -o wide

aws cloudformation describe-stacks \
  --stack-name eksctl-enterprise-cluster-nodegroup-standard-workers \
  --region us-east-1
```

## Engineering lessons

- A successful EKS control plane does not mean worker nodes are healthy.
- `kubectl get nodes` is a critical post-provisioning validation.
- CloudFormation stack status is essential when `eksctl` reports a timeout.
- HPA scales **pods**, not EC2 nodes.
- A node group's `maxSize` does not install Cluster Autoscaler or Karpenter.
- Failed deployments still require explicit cost and cleanup verification.

## Next attempt checklist

Before retrying:

- identify the specific node-group `CREATE_FAILED` event if retained in CloudFormation history
- verify subnet routing and public IP behavior
- verify node IAM role and EKS authentication
- confirm EC2 capacity for the selected instance type/AZs
- create the cluster
- verify both nodes reach `Ready`
- install/verify Metrics Server before HPA testing
- deploy the application with Helm
- validate the LoadBalancer endpoint
- test scaling
- clean up all AWS resources

## Cost control

This lab can generate charges for the EKS control plane, EC2, EBS, public IPv4 addresses, load balancing, and networking. A budget alert was configured, NAT Gateway creation was disabled for the initial lab design, and cleanup is treated as a required project phase.
