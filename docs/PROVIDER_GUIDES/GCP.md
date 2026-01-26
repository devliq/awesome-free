# Google Cloud Platform (GCP) Free Tier Deep Dive

## Overview

Google Cloud Platform offers a $300 credit for new users, making it one of the most generous trial periods. However, the free tier is more limited than AWS, with fewer always-free services.

## Account Setup and Requirements

### Getting Started
- **Credit Card Required**: Mandatory for account creation
- **Phone Verification**: Required for account activation
- **Billing Account**: Automatic creation with credit application
- **Address Requirements**: Valid billing address required

### Free Tier Structure
- **Credit Amount**: $300 for new customers
- **Duration**: 90 days from account creation
- **Scope**: Applies to most Google Cloud services
- **Always-Free Services**: Limited but perpetual free offerings

## Core Free Tier Services

### Compute

#### Compute Engine
**Free Tier:** None (credit-based only)
**Credit Usage:** ~$5-10/month for f1-micro instance
**Limits:** 0.2 vCPU, 0.6GB RAM per instance
**Gotchas:**
- No always-free compute instances
- Sustained use discount requires 25%+ utilization
- Boot disk costs extra
- Network egress costs $0.12/GB

**Best For:** Learning GCP, small development environments

#### Cloud Functions
**Free Tier:** 2 million invocations/month, 400,000 GB-seconds
**Duration:** Always free
**Limits:** 100 concurrent executions, 100MB memory
**Gotchas:**
- Cold start latency
- VPC connector costs extra
- Pub/Sub triggers count toward limits

**Best For:** Event-driven applications, API backends

#### App Engine
**Free Tier:** 28 instance hours/day, 5GB storage
**Duration:** Always free
**Limits:** Standard environment only
**Gotchas:**
- Traffic bursts may exceed free tier
- Outbound network costs apply
- Custom domains require SSL certificates

### Storage

#### Cloud Storage
**Free Tier:** 5GB regional storage, 5,000 Class A operations, 50,000 Class B operations
**Duration:** Always free
**Limits:** Regional storage class
**Gotchas:**
- Data retrieval costs $0.12/GB
- Inter-region transfer costs $0.12/GB
- Archive storage not free

**Best For:** Static website hosting, file storage, backups

#### Persistent Disk
**Free Tier:** None (credit-based)
**Credit Usage:** $0.04/GB-month for SSD, $0.02/GB-month for HDD
**Limits:** Regional PD only
**Gotchas:**
- Only free when attached to running instances
- Snapshots cost $0.026/GB-month

### Databases

#### Cloud SQL
**Free Tier:** None (credit-based)
**Credit Usage:** ~$10-15/month for shared CPU instance
**Limits:** MySQL, PostgreSQL, SQL Server
**Gotchas:**
- Storage costs $0.054/GB-month
- Backup storage costs $0.08/GB-month
- High availability costs extra

**Best For:** Managed database needs

#### Firestore
**Free Tier:** 1GB storage, 50,000 reads/day, 20,000 writes/day
**Duration:** Always free
**Limits:** Document database operations
**Gotchas:**
- Network egress costs $0.12/GB
- Complex queries count as multiple reads
- Real-time listeners limited

**Best For:** Real-time applications, user data, configuration

#### BigQuery
**Free Tier:** 1TB queries/month, 10GB storage
**Duration:** Always free
**Limits:** Analysis queries
**Gotchas:**
- Streaming inserts cost $0.01/200MB
- Long-term storage costs after 90 days
- Data transfer costs apply

### Networking

#### Cloud Load Balancing
**Free Tier:** None (credit-based)
**Credit Usage:** $0.025/hour per forwarding rule
**Limits:** HTTP(S) load balancing
**Gotchas:**
- SSL certificates cost $600/year for custom domains
- Global load balancing requires premium tier

#### Cloud CDN
**Free Tier:** 5GB-1TB egress free (region-dependent)
**Duration:** Always free
**Limits:** HTTP/HTTPS caching
**Gotchas:**
- Cache fill costs $0.04/GB
- Cache lookup costs $0.0075/10,000 requests
- Custom origins may incur costs

### AI/ML

#### AI Platform
**Free Tier:** Limited training and prediction
**Duration:** Credit-based
**Limits:** CPU-only training
**Gotchas:**
- GPU training costs $0.45/hour
- Model deployment costs vary
- Data storage costs apply

#### AutoML
**Free Tier:** None
**Credit Usage:** $20-50 for basic model training
**Limits:** Vision, NLP, Translation
**Gotchas:**
- Training data requirements
- Model hosting costs

## Always-Free Services

### App Engine
- 28 instance hours/day
- 5GB Cloud Storage
- 1GB mail/day

### Cloud Functions
- 2M invocations/month
- 400K GB-seconds/month
- 5GB outbound network

### Cloud Storage
- 5GB regional storage
- 5K Class A operations/month
- 50K Class B operations/month

### BigQuery
- 1TB query processing/month
- 10GB storage

### Cloud Pub/Sub
- 10GB messages/month
- 1K connections/minute

### Cloud Logging
- 50GB logs/month
- Basic log analysis

## Cost Traps and Avoidance

### Egress Costs
GCP charges $0.12/GB for data leaving their network. This is one of the highest egress costs among cloud providers.

**Avoidance:**
- Use Cloud CDN for content delivery
- Deploy applications in user's regions
- Minimize data export operations
- Use multi-region storage strategically

### Sustained Use Discounts
GCP offers discounts for continuous usage, but this can create unexpected costs if usage patterns change.

**Avoidance:**
- Monitor commitment discounts
- Use preemptible instances for non-critical workloads
- Plan for usage pattern changes

### Service Dependencies
Many GCP services have interconnected pricing. Using one service often enables costs in related services.

**Avoidance:**
- Review service dependencies before starting
- Use cost calculators for complex architectures
- Start with minimal service combinations

## Optimization Strategies

### Credit Management
- Track credit usage daily during 90-day trial
- Set billing alerts at 50% and 80% credit usage
- Prioritize always-free services over credit-dependent ones

### Regional Selection
- Choose regions with free egress allowances
- Consider data sovereignty requirements
- Balance latency vs cost trade-offs

### Multi-Provider Architecture
Combine GCP with other providers to minimize costs:
- GCP Cloud Functions + external databases
- GCP AI Platform + Cloudflare storage
- GCP BigQuery + external data sources

## Machine Learning Optimization

### AI Platform Strategy
- Use always-free BigQuery for data analysis
- Start with pre-trained models
- Use AutoML for small datasets
- Implement cost monitoring for training jobs

### Data Processing
- Use Dataflow for batch processing (credit-based)
- Implement cost controls for long-running jobs
- Use BigQuery for analytical workloads
- Optimize data storage lifecycle

## Monitoring and Cost Control

### GCP Cost Management Tools
- **Billing Reports**: Detailed cost breakdown
- **Budgets and Alerts**: Spending limit notifications
- **Cost Explorer**: Usage analysis and forecasting
- **Commitment Tracker**: Discount utilization monitoring

### Best Practices
- Enable billing export to BigQuery
- Set up cost alerts immediately
- Use labels for cost allocation
- Review costs weekly during trial period

## Common Use Cases

### Data Analytics Platform
```
Storage: Cloud Storage (free tier)
Processing: BigQuery (free tier)
Visualization: Data Studio (free)
Orchestration: Cloud Composer (credit-based)
```

**Cost:** $0/month for basic analytics
**Scaling:** Add Dataflow for complex ETL

### ML Application
```
Data: BigQuery (free)
Training: AI Platform (credit-based)
Serving: Cloud Functions (free)
Storage: Cloud Storage (free)
```

**Cost:** $0/month for serving, variable for training
**Scaling:** Use preemptible instances for training

### Web Application
```
Frontend: App Engine (free)
Backend: Cloud Functions (free)
Database: Firestore (free)
Storage: Cloud Storage (free)
CDN: Cloud CDN (free)
```

**Cost:** $0/month
**Scaling:** Upgrade to Compute Engine when needed

## Migration and Scaling

### From Trial to Paid
- Evaluate committed use discounts
- Consider Anthos for multi-cloud
- Implement cost optimization tools
- Plan for sustained usage patterns

### Multi-Cloud Strategies
- Use GCP for AI/ML capabilities
- Combine with AWS for compute-heavy workloads
- Leverage Cloudflare for global CDN
- Use external databases for cost control

## Getting Started Checklist

- [ ] Create GCP account with credit card
- [ ] Note 90-day trial start date
- [ ] Enable billing alerts and budgets
- [ ] Start with always-free services (BigQuery, Cloud Storage)
- [ ] Monitor credit usage daily
- [ ] Set up cost export to BigQuery
- [ ] Plan migration before trial expires
- [ ] Review regional data transfer costs

## Resources

- [GCP Free Tier](https://cloud.google.com/free)
- [GCP Pricing Calculator](https://cloud.google.com/products/calculator)
- [GCP Cost Management](https://cloud.google.com/cost-management)
- [GCP Documentation](https://cloud.google.com/docs)

---

*GCP offers generous credits but high ongoing costs. Focus on always-free services and monitor credit usage closely during the 90-day trial.*