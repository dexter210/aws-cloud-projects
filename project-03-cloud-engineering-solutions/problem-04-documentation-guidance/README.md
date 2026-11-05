# Problem 04 — Lack of Documentation and Guidance

## Goal

Create a lightweight documentation system that improves onboarding, reduces repeated questions, and makes operational work more consistent.

## Problem

When documentation is incomplete or outdated, teams rely on tribal knowledge. This creates several risks:

- new engineers take longer to become productive
- incident response depends on specific individuals
- repeated tasks are performed differently each time
- troubleshooting takes longer
- important context is lost when team members are unavailable

## Documentation Strategy

A practical documentation model should include:

- runbooks for repeatable operational tasks
- onboarding checklists for new team members
- ownership for each document
- review dates
- version history
- links to related dashboards, repositories, and escalation contacts

## Runbook Standard

Every operational runbook should answer:

1. What is this procedure for?
2. When should it be used?
3. What permissions are required?
4. What steps should be followed?
5. How do I validate success?
6. What should I do if something fails?
7. Who owns this process?
8. When was this document last reviewed?

## Documentation Review Process

A simple review cycle:

```text
Create / Update Document
        ↓
Peer Review
        ↓
Publish
        ↓
Use During Real Work
        ↓
Capture Gaps
        ↓
Scheduled Review
        ↓
Update Again
```

Recommended review cadence:

- critical runbooks: monthly
- common operational procedures: quarterly
- onboarding content: quarterly
- architecture documentation: after major changes

## Knowledge Sharing

Documentation should be supported by regular knowledge sharing.

Examples:

- 15-minute weekly knowledge share
- monthly lunch-and-learn
- incident postmortem reviews
- rotating ownership of runbook walkthroughs
- pairing during unfamiliar operational tasks

## Files

```text
problem-04-documentation-guidance/
├── README.md
├── templates/
│   └── operational-runbook-template.md
├── onboarding/
│   └── cloud-engineer-onboarding-checklist.md
└── examples/
    └── high-cpu-runbook.md
```

## Desired Outcomes

- faster onboarding
- fewer repeated questions
- less dependence on individual engineers
- more consistent incident response
- easier knowledge transfer
- lower operational risk
