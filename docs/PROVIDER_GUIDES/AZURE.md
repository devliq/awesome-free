# Microsoft Azure Free Tier Deep Dive

## Overview

Microsoft Azure offers a $200 credit for new users with a 30-day trial period. The free tier includes 55+ always-free services, making it competitive for long-term free usage.

## Account Setup and Requirements

### Getting Started
- **Credit Card Required**: Mandatory for account creation
- **Phone Verification**: Required for account activation
- **Identity Verification**: May be requested for some services
- **Address Requirements**: Valid billing address required

### Free Tier Structure
- **Credit Amount**: $200 for new customers
- **Duration**: 30 days from account creation
- **Always-Free Services**: 55+ services with no expiration
- **Scope**: Global availability for most services

## Core Free Tier Services

### Compute

#### Virtual Machines
**Free Tier:** None (credit-based only)
**Credit Usage:** ~$10-15/month for B1s instance
**Limits:** 1 vCPU, 1GB RAM, 4GB temp storage
**Gotchas:**
- Only free for 30 days
- Storage disks cost extra
- Network bandwidth costs $0.087/GB outbound
- Windows licensing costs extra

**Best For:** Learning Azure, development environments

#### App Service
**Free Tier:** 10 web apps, 1GB storage, 1 hour/day compute
**Duration:** Always free
**Limits:** Shared infrastructure, 60 minutes/day
**Gotchas:**
- Apps sleep after inactivity
- Custom domains require paid tier
- SSL certificates cost extra
- Database connections limited

**Best For:** Small web applications, APIs, development

#### Functions
**Free Tier:** 1 million requests/month, 400,000 GB-seconds
**Duration:** Always free
**Limits:** Consumption plan, 100 concurrent executions
**Gotchas:**
- Cold start latency
- Premium plan features cost extra
- Durable Functions have execution limits

**Best For:** Event-driven processing, API backends

### Storage

#### Blob Storage
**Free Tier:** 5GB hot storage, 20,000 read operations, 10,000 write operations
**Duration:** Always free
**Limits:** Hot access tier only
**Gotchas:**
- Data retrieval costs $0.01/GB
- Inter-region transfer costs $0.02/GB
- Archive storage not free

**Best For:** File storage, backups, static content

#### Files
**Free Tier:** 5GB storage, 10,000 operations
**Duration:** Always free
**Limits:** Standard file shares
**Gotchas:**
- Premium file shares cost extra
- SMB protocol support limited

### Databases

#### SQL Database
**Free Tier:** None (credit-based)
**Credit Usage:** ~$5/month for basic tier
**Limits:** 5 DTU, 2GB storage
**Gotchas:**
- Storage costs $0.115/GB
- Backup storage costs $0.19/GB
- Geo-redundancy costs extra

**Best For:** Small applications, development databases

#### Cosmos DB
**Free Tier:** 5GB storage, 400 RU/s throughput
**Duration:** Always free
**Limits:** Single region, multiple APIs
**Gotchas:**
- Additional throughput costs $0.008/hour per 100 RU/s
- Multi-region replication costs extra
- Backup storage costs apply

**Best For:** Globally distributed applications, IoT data

### Networking

#### CDN
**Free Tier:** 5GB outbound, 50,000 transactions
**Duration:** Always free
**Limits:** Standard Microsoft CDN
**Gotchas:**
- Additional data transfer costs $0.087/GB
- Custom domains require verification
- Premium features cost extra

#### Load Balancer
**Free Tier:** 1 basic load balancer
**Duration:** Always free
**Limits:** Basic features only
**Gotchas:**
- Standard load balancer costs $0.025/hour
- Outbound data costs $0.008/GB

### AI/ML

#### Cognitive Services
**Free Tier:** Varies by service (0-1M transactions)
**Duration:** Always free
**Limits:** Service-specific limits
**Gotchas:**
- Some services have strict rate limits
- Custom models cost extra
- Training data requirements

**Examples:**
- Computer Vision: 5,000 transactions/month
- Text Analytics: 5,000 documents/month
- Translator: 2M characters/month

## Always-Free Services (55+)

### Core Services
- Azure App Service (10 apps, 1 hour/day)
- Azure Functions (1M requests/month)
- Azure Storage (5GB blob + file)
- Azure Cosmos DB (5GB, 400 RU/s)
- Azure CDN (5GB outbound)

### Developer Tools
- Azure DevOps (5 users free)
- Azure Pipelines (unlimited minutes for public projects)
- Azure Repos (unlimited private repos)
- Azure Boards (unlimited work items)

### Monitoring
- Azure Monitor (10GB logs/month)
- Azure Application Insights (5GB telemetry)
- Azure Log Analytics (5GB ingestion)

### Security
- Azure Active Directory (500,000 objects)
- Azure Key Vault (10,000 transactions)
- Azure Policy (500 policy evaluations)

### IoT
- Azure IoT Hub (8,000 messages/day)
- Azure IoT Central (2 devices free)

## Cost Traps and Avoidance

### Credit Expiration
Azure's 30-day trial is shorter than competitors. Plan migration before credit expires.

**Avoidance:**
- Monitor credit usage daily
- Set billing alerts at 50% and 80%
- Start with always-free services
- Have migration plan ready

### Service Dependencies
Many Azure services have interconnected costs. Using one service enables costs in related services.

**Avoidance:**
- Review resource group costs
- Use cost analysis tools
- Start with minimal configurations
- Monitor cross-service dependencies

### Regional Costs
Data transfer and storage costs vary by region. Some regions have higher costs.

**Avoidance:**
- Choose cost-optimized regions
- Use Azure pricing calculator
- Plan for data residency requirements

## Optimization Strategies

### Credit Management
- Track spending against $200 credit daily
- Prioritize always-free services
- Use Azure cost management tools
- Set spending limits and alerts

### Resource Organization
- Use resource groups for cost tracking
- Implement tagging strategy
- Use management groups for organization
- Monitor costs by resource group

### Multi-Provider Architecture
Combine Azure with other providers:
- Azure Functions + external databases
- Azure Storage + Cloudflare CDN
- Azure AI + external storage

## Enterprise Features

### Azure DevOps
**Free Tier:** 5 users, unlimited private repos
**Duration:** Always free
**Limits:** Basic CI/CD features
**Gotchas:**
- Self-hosted agents cost extra
- Advanced features require paid tiers

### Azure Monitor
**Free Tier:** 10GB logs, 1GB metrics
**Duration:** Always free
**Limits:** Basic monitoring features
**Gotchas:**
- Log ingestion costs $0.50/GB after free tier
- Application Insights costs vary

## Monitoring and Cost Control

### Azure Cost Management Tools
- **Cost Analysis**: Detailed spending breakdown
- **Budgets**: Spending limit alerts
- **Advisor**: Cost optimization recommendations
- **Reservations**: Save on predictable usage

### Best Practices
- Enable cost alerts immediately
- Use resource tags for cost allocation
- Review costs weekly
- Implement cost management policies

## Common Use Cases

### Web Application
```
Frontend: App Service (free)
Backend: Functions (free)
Database: Cosmos DB (free)
Storage: Blob Storage (free)
CDN: Azure CDN (free)
```

**Cost:** $0/month
**Scaling:** Upgrade to paid App Service plans

### IoT Solution
```
IoT Hub: 8,000 messages/day (free)
Stream Analytics: 1 streaming unit (credit)
Cosmos DB: 5GB storage (free)
Functions: Event processing (free)
```

**Cost:** $0/month for basic IoT
**Scaling:** Add paid streaming units

### AI Application
```
Cognitive Services: Various free tiers
Functions: Model serving (free)
Cosmos DB: Data storage (free)
Storage: Model artifacts (free)
```

**Cost:** $0/month for development
**Scaling:** Upgrade to paid Cognitive Services

## Migration and Scaling

### From Trial to Paid
- Evaluate Azure reservations
- Use Azure Hybrid Benefit
- Implement cost optimization
- Plan for enterprise features

### Multi-Cloud Strategies
- Use Azure for Windows workloads
- Combine with AWS for global reach
- Leverage Cloudflare for CDN
- Use external databases for cost control

## Getting Started Checklist

- [ ] Create Azure account with credit card
- [ ] Note 30-day trial start date
- [ ] Enable spending limits and alerts
- [ ] Start with always-free services
- [ ] Set up cost management
- [ ] Monitor credit usage daily
- [ ] Plan migration strategy
- [ ] Review regional pricing

## Resources

- [Azure Free Account](https://azure.microsoft.com/free/)
- [Azure Pricing Calculator](https://azure.microsoft.com/pricing/calculator/)
- [Azure Cost Management](https://azure.microsoft.com/services/cost-management/)
- [Azure Documentation](https://docs.microsoft.com/azure/)

---

*Azure offers excellent always-free services but a short trial period. Focus on the 55+ always-free services for long-term free usage.*