# Problem 03 — Resource Constraints

## Goal

Design practical ways for a small cloud engineering team to handle competing priorities, reduce single points of failure, and automate repetitive work.

## Scenario

A small cloud team is responsible for incidents, monitoring, deployments, access requests, maintenance, documentation, and cloud cost reviews. When several tasks arrive at the same time, engineers can become overloaded and critical work can be delayed.

This exercise focuses on three improvements:

- workload prioritization
- cross-training and coverage
- automation of repetitive tasks

## 1. Workload Assessment

Typical work for a small cloud team may include:

| Work Type | Example | Risk if Delayed |
|---|---|---|
| Production incident | Application unavailable | Critical |
| Security issue | Exposed credential | Critical |
| Monitoring alert | High CPU / disk | High |
| Deployment request | Application release | Medium |
| Access request | IAM permission change | Medium |
| Documentation | Runbook update | Low |
| Cost review | Unused resources | Medium |

A common problem is treating every request as equally urgent. That causes context switching and makes it harder to protect time for high-impact work.

## 2. Prioritization Model

I use a simple impact/urgency model:

| Priority | Description |
|---|---|
| P1 | Critical production or security impact; immediate response |
| P2 | High operational impact; same-day response |
| P3 | Normal planned work; schedule into available capacity |
| P4 | Low-risk maintenance or improvement work |

The included prioritization script scores sample tasks using impact and urgency so the team can work from highest to lowest risk.

## 3. Cross-Training and Coverage

A small team becomes fragile when only one person knows a system.

Example coverage model:

| Area | Primary | Secondary |
|---|---|---|
| AWS / Infrastructure | Engineer A | Engineer B |
| Monitoring / Observability | Engineer B | Engineer C |
| CI/CD | Engineer C | Engineer A |
| IAM / Access | Engineer A | Engineer C |
| Documentation / Runbooks | Shared | Shared |

The goal is not for everyone to be an expert in everything. The goal is to make sure there is at least one backup for critical responsibilities.

## 4. Automation Opportunities

Good automation targets are repetitive, rule-based tasks with low ambiguity.

Examples:

- daily resource health checks
- stale EC2/EBS discovery
- standard IAM access reports
- log cleanup
- ticket creation from alerts
- scheduled backup verification
- environment inventory collection

The sample automation in this folder generates a daily workload summary from a CSV task queue.

## Files

```text
problem-03-resource-constraints/
├── README.md
├── examples/
│   └── team-workload.csv
├── config/
│   └── team-coverage.json
└── scripts/
    ├── prioritize_work.py
    └── daily_workload_summary.py
```

## Desired Outcomes

- reduce context switching
- protect response time for critical work
- improve backup coverage
- reduce repetitive manual effort
- make workload visible to the whole team
