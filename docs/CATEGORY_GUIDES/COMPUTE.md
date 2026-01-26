# Compute Services Overview

## Overview

Compute services provide the processing power for your applications. From traditional virtual machines to modern serverless functions, compute services form the backbone of cloud applications.

## Service Types

### Virtual Machines (IaaS)
Traditional server instances with full OS control.

**Key Services:**
- AWS EC2: 750 hours/month t2.micro (12 months)
- GCP Compute Engine: f1-micro instances ($300 credit)
- Azure VMs: B1s instances ($200 credit)
- Oracle Always Free: 2 AMD-based VMs (always)

**Best For:** Full control, legacy applications, custom configurations

### Containers
Application containerization with orchestration.

**Key Services:**
- AWS Fargate: Serverless containers (credit-based)
- GCP Cloud Run: Containerized apps (credit-based)
- Azure Container Instances: Container execution (credit-based)
- Fly.io: Container deployment (always-free shared)

**Best For:** Microservices, scalable applications, DevOps workflows

### Application Platforms (PaaS)
Managed application hosting with built-in services.

**Key Services:**
- Heroku: dyno hours (550 free)
- Railway: Full-stack hosting (512MB RAM free)
- Render: Web services (750 hours/month)
- Vercel: Frontend hosting (unlimited bandwidth)

**Best For:** Web applications, APIs, rapid development

### Serverless Functions (FaaS)
Event-driven code execution without server management.

**Key Services:**
- AWS Lambda: 1M requests/month (always)
- GCP Cloud Functions: 2M invocations/month (always)
- Azure Functions: 1M requests/month (always)
- Cloudflare Workers: 100k requests/day (always)

**Best For:** APIs, event processing, microservices

## Free Tier Comparison

### Always-Free Compute

| Service | CPU | RAM | Requests/Month | Duration |
|---------|-----|-----|----------------|----------|
| AWS Lambda | - | 128MB-3GB | 1M | Always |
| GCP Functions | - | 128MB-2GB | 2M | Always |
| Azure Functions | - | 128MB-1.5GB | 1M | Always |
| Cloudflare Workers | 10ms CPU | - | 100k/day | Always |
| Fly.io Apps | Shared CPU | 256MB | Unlimited | Always |

### Trial-Based Compute

| Service | Free Duration | Credit | Best For |
|---------|---------------|--------|----------|
| AWS EC2 | 12 months | - | Learning AWS |
| GCP Compute | 90 days | $300 | ML/AI workloads |
| Azure VMs | 30 days | $200 | Windows workloads |
| DigitalOcean | 60 days | $100 | Simple deployments |

## Selection Criteria

### Performance Requirements
- **Low Traffic:** Serverless functions, shared hosting
- **Medium Traffic:** Container platforms, PaaS
- **High Traffic:** Full VMs, dedicated instances

### Development Speed
- **Rapid Prototyping:** Vercel, Netlify, Railway
- **Custom Development:** AWS/GCP/Azure VMs
- **Event-Driven:** Lambda, Cloud Functions

### Cost Predictability
- **Always-Free:** Cloudflare Workers, Fly.io
- **Trial-Based:** AWS EC2, GCP Compute
- **Pay-Per-Use:** All serverless platforms

## Architecture Patterns

### Monolithic Applications
```
Single VM/Container + Database + Storage
```
**Services:** Railway, Render, Heroku
**Best For:** Simple applications, MVPs

### Microservices
```
API Gateway + Multiple Functions + Databases
```
**Services:** AWS Lambda + API Gateway, Cloudflare Workers
**Best For:** Scalable applications, complex systems

### Hybrid Approach
```
Frontend (Vercel) + Backend (Fly.io) + Database (PlanetScale)
```
**Services:** Multiple providers combined
**Best For:** Cost optimization, vendor diversity

## Cost Optimization

### Right-Sizing
- Start with smallest instances
- Monitor actual usage
- Scale up only when necessary

### Auto-Scaling
- Implement automatic scaling
- Set appropriate limits
- Monitor scaling events

### Multi-Region Deployment
- Deploy close to users
- Use global load balancing
- Implement failover strategies

## Common Use Cases

### Web Applications
- **Static Sites:** Vercel, Netlify, GitHub Pages
- **Dynamic Apps:** Railway, Render, Fly.io
- **High-Traffic:** AWS EC2, GCP Compute (paid scaling)

### APIs and Backends
- **REST APIs:** Cloudflare Workers, AWS Lambda
- **GraphQL:** AWS AppSync, GCP Cloud Run
- **Real-time:** WebSocket support varies by service

### Background Processing
- **Scheduled Tasks:** Cloudflare Workers, AWS Lambda
- **Queue Processing:** AWS SQS + Lambda
- **Data Processing:** GCP Dataflow (credit-based)

### Development Environments
- **Personal Dev:** GitHub Codespaces, Gitpod
- **Team Dev:** AWS Cloud9, GCP Cloud Shell
- **CI/CD:** GitHub Actions, GitLab CI

## Migration Strategies

### From Local Development
1. Containerize application (Docker)
2. Choose appropriate compute service
3. Deploy and configure environment
4. Set up monitoring and logging

### Between Providers
1. Assess application requirements
2. Choose target service features
3. Plan data migration
4. Update DNS and endpoints
5. Test thoroughly before cutover

### Scaling Up
1. Monitor current usage limits
2. Plan scaling strategy
3. Implement gradual migration
4. Optimize costs during transition

## Performance Considerations

### Cold Starts
Serverless functions have initialization delays:
- AWS Lambda: 100-500ms
- GCP Functions: 100-1000ms
- Cloudflare Workers: Minimal (<50ms)

### Resource Limits
- Memory: 128MB - 10GB+ (service dependent)
- CPU: Shared to dedicated cores
- Execution Time: 10 seconds - 15 minutes

### Network Performance
- Regional deployment impacts latency
- CDN integration improves performance
- Global distribution varies by service

## Security Best Practices

### Access Control
- Use IAM roles and policies
- Implement least privilege
- Rotate credentials regularly

### Network Security
- Configure firewalls and security groups
- Use VPCs for isolation
- Implement encryption in transit

### Compliance
- Choose services with required certifications
- Implement logging and monitoring
- Regular security updates

## Monitoring and Observability

### Application Monitoring
- Error tracking: Sentry, Rollbar
- Performance monitoring: New Relic, Datadog
- Custom metrics: CloudWatch, Cloud Monitoring

### Infrastructure Monitoring
- Resource usage: Built-in dashboards
- Health checks: Load balancer monitoring
- Alerting: Email, Slack, PagerDuty

### Logging
- Centralized logging: CloudWatch Logs, Stackdriver
- Log analysis: ELK stack, Splunk
- Retention policies: Cost-effective storage

## Getting Started

### Quick Start Guide
1. Define application requirements
2. Choose appropriate compute service
3. Set up development environment
4. Deploy minimum viable application
5. Configure monitoring and alerts
6. Plan scaling strategy

### Learning Resources
- [AWS Compute Services](https://aws.amazon.com/products/compute/)
- [GCP Compute Options](https://cloud.google.com/products/compute)
- [Azure Compute](https://azure.microsoft.com/services/#compute)
- [Serverless Framework](https://serverless.com/)

---

*Choose compute services based on your application needs, development speed requirements, and scaling plans. Start small and scale up as your application grows.*