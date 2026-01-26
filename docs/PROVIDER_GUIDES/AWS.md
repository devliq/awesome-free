# AWS Free Tier Deep Dive

## Overview

Amazon Web Services (AWS) offers one of the most comprehensive free tiers, but it's also one of the most complex with significant cost traps. The free tier is designed for learning and experimentation, with time-limited trials for most services.

## Account Setup and Requirements

### Getting Started
- **Credit Card Required**: Mandatory for account creation
- **Phone Verification**: Required for account activation
- **Identity Verification**: Government ID may be requested for some services
- **Address Requirements**: Valid billing address in supported country

### Free Tier Period
- **Duration**: 12 months from account creation date
- **Scope**: Applies to most services, but not all
- **Extensions**: Some services offer extended free tiers

## Core Free Tier Services

### Compute

#### EC2 (Elastic Compute Cloud)
**Free Tier:** 750 hours/month of t2.micro or t3.micro instances
**Duration:** 12 months from account creation
**Limits:** Linux/Windows, any region, any AMI
**Gotchas:**
- Only free for first 12 months
- EBS storage costs extra ($0.10/GB-month)
- Public IP costs $0.005/hour if not attached to running instance
- Data transfer costs $0.09/GB outbound

**Best For:** Learning AWS, small web applications, development environments

#### Lambda (Serverless Functions)
**Free Tier:** 1 million requests/month, 400,000 GB-seconds compute time
**Duration:** Always free (no expiration)
**Limits:** 3.2 million seconds/month compute time
**Gotchas:**
- Cold start latency for infrequently used functions
- VPC access removes some free tier benefits
- CloudWatch logs cost extra after basic free tier

**Best For:** API backends, event processing, scheduled tasks

#### Elastic Beanstalk
**Free Tier:** 750 hours/month of t1.micro instances
**Duration:** 12 months
**Limits:** Single environment, basic features
**Gotchas:** Application load balancer costs extra

### Storage

#### S3 (Simple Storage Service)
**Free Tier:** 5GB storage, 20,000 GET requests, 2,000 PUT requests
**Duration:** 12 months
**Limits:** Standard storage class only
**Gotchas:**
- Data transfer costs $0.09/GB outbound
- Requests beyond free tier cost $0.004 per 1,000 requests
- Storage costs $0.023/GB-month after free tier

**Best For:** Static website hosting, file storage, backups

#### EBS (Elastic Block Storage)
**Free Tier:** 30GB total across all EBS volumes
**Duration:** 12 months
**Limits:** gp2, io1, or st1 volumes
**Gotchas:**
- Only free when attached to running EC2 instances
- Snapshots cost $0.05/GB-month
- I/O costs for provisioned IOPS

### Databases

#### RDS (Relational Database Service)
**Free Tier:** 750 hours of db.t2.micro instances
**Duration:** 12 months
**Limits:** MySQL, PostgreSQL, MariaDB, Oracle, SQL Server
**Gotchas:**
- Storage costs $0.10/GB-month
- Backup storage costs $0.095/GB-month
- Multi-AZ deployment not free

**Best For:** Small applications, development databases

#### DynamoDB (NoSQL Database)
**Free Tier:** 25GB storage, 200 million requests/month
**Duration:** Always free
**Limits:** On-demand throughput
**Gotchas:**
- Global tables cost extra
- Streams and backups have separate pricing
- DAX (caching) costs $0.122/hour

**Best For:** High-scale applications, user session data, metadata

### Networking

#### CloudFront (CDN)
**Free Tier:** 1TB outbound data transfer, 10,000,000 requests
**Duration:** 12 months
**Limits:** HTTP/HTTPS delivery
**Gotchas:**
- Regional data transfer costs vary
- Lambda@Edge costs $0.60 per 1M requests
- Custom SSL certificates cost $600/year

**Best For:** Global content delivery, static asset distribution

#### API Gateway
**Free Tier:** 1 million API calls/month
**Duration:** 12 months
**Limits:** REST APIs, WebSocket APIs
**Gotchas:**
- Data transfer costs $0.09/GB outbound
- Custom domains cost $36/month
- Usage plans and throttling have limits

### Developer Tools

#### CloudWatch
**Free Tier:** Basic monitoring metrics, 10 custom metrics, 1,000 API requests
**Duration:** Always free for basic features
**Limits:** 5-minute granularity for basic metrics
**Gotchas:**
- Detailed monitoring costs $0.30/GB ingested
- Logs cost $0.50/GB ingested after 5GB
- Alarms cost $0.10/alarm/month

**Best For:** Basic monitoring, alerting, logging

#### CodePipeline, CodeBuild, CodeDeploy
**Free Tier:** 1 active pipeline, 100 build minutes/month
**Duration:** Always free
**Limits:** AWS services only
**Gotchas:**
- External integrations may cost extra
- Artifact storage costs apply

## Advanced Services with Free Tiers

### Machine Learning

#### SageMaker
**Free Tier:** 250 hours of t2.medium notebooks, 5GB storage
**Duration:** 12 months
**Limits:** Jupyter notebooks, basic ML tools
**Gotchas:** Model training costs extra, complex pricing

### Analytics

#### Athena
**Free Tier:** 1TB data scanned/month
**Duration:** Always free
**Limits:** SQL queries on S3 data
**Gotchas:** Data transfer costs from S3

### IoT

#### IoT Core
**Free Tier:** 250,000 messages/month, 250,000 registry operations
**Duration:** 12 months
**Limits:** Basic IoT functionality
**Gotchas:** Device Shadow operations count toward limits

## Cost Traps and Avoidance

### Data Transfer Costs
AWS charges for data leaving their network. Always use CloudFront or other CDNs to minimize egress costs.

### Service Coupling
Using EC2 doesn't make EBS free. Each service has separate pricing. Plan storage costs separately.

### Region Selection
Some free tier services are region-specific. US East (N. Virginia) offers the most comprehensive free tier.

### Account Age Requirements
Advanced services like SageMaker require 12+ months account age. Create accounts early.

## Optimization Strategies

### EC2 Optimization
- Use t2/t3.micro for development
- Stop instances when not in use
- Use spot instances for non-critical workloads
- Implement auto-scaling carefully

### Storage Optimization
- Use S3 for most storage needs
- Implement lifecycle policies
- Use CloudFront for data delivery
- Compress data before storage

### Multi-Service Architecture
Combine AWS free tiers with other providers:
- AWS Lambda + DynamoDB + Cloudflare CDN
- EC2 + S3 + external databases
- API Gateway + Lambda + external storage

## Migration and Scaling

### From Free to Paid
- Monitor usage with Cost Explorer
- Set up billing alerts
- Use Reserved Instances for predictable workloads
- Implement cost allocation tags

### Multi-Cloud Strategies
- Use AWS for compute, other providers for storage
- Implement data export capabilities
- Design for portability from day one

## Monitoring and Cost Control

### AWS Cost Management Tools
- **Cost Explorer**: Analyze spending patterns
- **Budgets**: Set spending limits and alerts
- **Cost Allocation Tags**: Track costs by project
- **Savings Plans**: Commit to usage for discounts

### Best Practices
- Enable billing alerts at account creation
- Review costs weekly during free tier period
- Use cost calculators for scaling projections
- Implement resource tagging from day one

## Common Use Cases

### Web Application
```
Frontend: S3 + CloudFront
Backend: Lambda + API Gateway
Database: DynamoDB
Monitoring: CloudWatch
```

**Cost:** $0/month for 12 months
**Scaling:** Add EC2 instances when Lambda limits exceeded

### API Service
```
Compute: Lambda
Database: RDS (free tier)
Cache: ElastiCache (limited free tier)
CDN: CloudFront
```

**Cost:** $0/month for 12 months
**Scaling:** Upgrade to provisioned throughput

### Data Processing
```
Storage: S3
Processing: Lambda
Analytics: Athena
Monitoring: CloudWatch
```

**Cost:** $0/month for 12 months
**Scaling:** Add Glue ETL jobs for complex processing

## Getting Started Checklist

- [ ] Create AWS account with credit card
- [ ] Enable billing alerts
- [ ] Set up Cost Explorer
- [ ] Note account creation date
- [ ] Choose US East (N. Virginia) region
- [ ] Start with Lambda and S3 for minimal risk
- [ ] Monitor usage weekly
- [ ] Plan migration strategy before free tier expires

## Resources

- [AWS Free Tier Page](https://aws.amazon.com/free/)
- [AWS Pricing Calculator](https://calculator.aws/)
- [AWS Cost Explorer](https://console.aws.amazon.com/cost-management/home)
- [AWS Documentation](https://docs.aws.amazon.com/)

---

*AWS free tier is powerful but complex. Start small, monitor closely, and plan your exit strategy before the 12-month free tier expires.*