# Runbook — High CPU Alert

## Purpose

Provide a consistent response procedure when a server or application reports sustained high CPU utilization.

## When to Use

Use this runbook when CPU remains above the configured warning or critical threshold for the required alert duration.

## Prerequisites

- monitoring platform access
- host or cloud-console access
- application ownership information
- recent deployment/change history

## Procedure

1. Confirm the alert is still active.
2. Check CPU usage over the last 15–30 minutes.
3. Identify the highest-consuming process or workload.
4. Check whether a deployment or configuration change occurred recently.
5. Review application logs for errors or traffic spikes.
6. Check memory, disk, and network metrics for correlated symptoms.
7. Determine whether the condition is expected, transient, or abnormal.
8. If capacity is insufficient, follow the approved scaling procedure.
9. If a process is unhealthy, follow the application recovery procedure.
10. Document the findings in the incident or ticket.

## Validation

The issue is considered resolved when:

- CPU returns below the alert threshold
- application health checks are passing
- error rate is normal
- latency returns to baseline
- no related critical alerts remain

## Rollback / Recovery

If the issue started after a recent deployment, use the approved rollback process.

Do not terminate processes or instances without confirming application ownership and impact.

## Escalation

Escalate when:

- CPU remains critical after remediation
- customer-facing impact is present
- scaling fails
- the root cause is unknown
- the issue repeatedly returns

## Ownership

**Owner:** Cloud Operations  
**Backup Owner:** Platform Engineering  
**Last Reviewed:** 2026-11-05  
