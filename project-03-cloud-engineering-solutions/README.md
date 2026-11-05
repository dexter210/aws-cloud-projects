# Project 03 — Strategic Solutions for Cloud Engineering Challenges

## Status

**In progress.** This project focuses on solving common cloud engineering operational problems through practical design, automation, observability, documentation, and CI/CD improvements.

## Problem 1 — Data Source Variability

### Goal

Demonstrate how inconsistent source data can be standardized into a common schema before downstream analytics or applications consume it.

### Scenario

Three source teams provide customer data in different formats:

- CRM exports CSV with `customer_id`, `name`, and `created_at`
- Marketing exports CSV with different field names and date formatting
- Support emits JSON with nested/alternate naming

The transformation layer converts each source into one common record structure:

```json
{
  "customer_id": "string",
  "full_name": "string",
  "email": "string|null",
  "source_system": "string",
  "created_at": "ISO-8601 UTC",
  "schema_version": "1.0"
}
```

### Architecture

```mermaid
flowchart LR
    A[CRM CSV] --> R[Raw Data Layer]
    B[Marketing CSV] --> R
    C[Support JSON] --> R
    R --> V[Schema Validation]
    V --> T[Transformation]
    T --> S[Standardized JSON]
    S --> C2[Curated Data Layer]
    C2 --> Q[Athena / Redshift / BI]
```

### Files

```text
problem-01-data-variability/
├── raw/
│   ├── crm_customers.csv
│   ├── marketing_customers.csv
│   └── support_customers.json
├── schema/
│   └── common-customer-schema.json
├── scripts/
│   └── standardize_customers.py
└── output/
    └── standardized-customers.json
```

### What This Demonstrates

- schema standardization
- data contracts
- source-to-target field mapping
- timestamp normalization
- null handling
- basic validation
- separating raw data from curated data
- designing a transformation step that could later be moved into AWS Glue

### AWS Mapping

A production AWS version could use:

```text
S3 Raw
  ↓
AWS Glue ETL
  ↓
Schema / Data Quality Validation
  ↓
S3 Curated (Parquet)
  ↓
Athena / Redshift / BI
```

The local Python exercise is intentionally small so the transformation logic can be understood before introducing managed AWS services.
