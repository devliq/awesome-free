# Evaluation Criteria: How We Evaluate "Free"

## Overview

Not all "free" services are created equal. Awesome-Free uses a rigorous evaluation framework to classify and document free offerings, ensuring users understand exactly what they're getting—and what they might owe later.

## Free Tier Classification System

### 1. Always-Free
Services with no time-based expiration. Free forever, subject only to usage limits.

**Characteristics:**
- No trial period countdown
- No credit expiration
- Usage-based limits only
- May require account activity to maintain

**Examples:**
- AWS Lambda: 1M requests/month (always)
- Cloudflare CDN: Unlimited bandwidth (always)
- GitHub Actions: 2,000 minutes/month (always)

**Evaluation Criteria:**
- Must have clear, documented usage limits
- No "trial" or "beta" designations
- Service remains free indefinitely
- May have account age or activity requirements

### 2. Time-Limited Trial
Free for a specific duration, then converts to paid service.

**Characteristics:**
- Fixed trial period (days/months)
- Automatic conversion to paid tier
- May offer full feature access during trial
- Often requires credit card for signup

**Examples:**
- AWS EC2: 750 hours free for 12 months
- GCP Compute Engine: 90-day trial with $300 credit
- Azure VMs: 30-day trial with $200 credit

**Evaluation Criteria:**
- Clear trial duration stated
- Transparent conversion terms
- Credit card requirement documented
- Post-trial pricing clearly explained

### 3. Credit-Based
New account bonus credits that expire after time or usage.

**Characteristics:**
- Monetary credit amount ($X value)
- Time-based expiration (typically 30-90 days)
- Applies to any service usage
- May have minimum spend requirements

**Examples:**
- DigitalOcean: $200 credit for new accounts
- Linode: $100 credit for 60 days
- Vultr: $100 credit for new users

**Evaluation Criteria:**
- Exact credit amount specified
- Clear expiration terms
- Applicable services documented
- No hidden minimums or restrictions

### 4. Mixed/Free with Paid Upgrade
Always-free tier exists alongside paid tiers.

**Characteristics:**
- Free tier never expires
- Paid upgrades available for higher limits
- Feature restrictions on free tier
- Clear upgrade path documented

**Examples:**
- MongoDB Atlas: 512MB free cluster (always)
- PlanetScale: 1 database, 1GB storage (always)
- Neon: 512MB PostgreSQL (always)

**Evaluation Criteria:**
- Free tier clearly distinguished from paid
- Upgrade process transparent
- Feature limitations documented
- No forced migration requirements

## Quality Assessment Framework

### Accuracy Score (1-5)
How well the free tier delivers on its promises.

**Factors:**
- Documentation clarity
- Limit enforcement consistency
- Billing transparency
- Support quality during free usage

### Completeness Score (1-5)
How comprehensive the service is for real use cases.

**Factors:**
- Feature coverage vs paid tier
- Integration capabilities
- Scalability within limits
- Production readiness

### Cost Risk Score (1-5)
Likelihood of unexpected charges.

**Factors:**
- Hidden cost traps
- Automatic scaling risks
- Data egress charges
- Service interdependency costs

### Vendor Lock-in Score (1-5)
Difficulty migrating away from the service.

**Factors:**
- Data export capabilities
- API standardization
- Alternative service compatibility
- Proprietary technology usage

## Inclusion/Exclusion Criteria

### Must Include
- Active service with current free tier
- Official documentation available
- Accessible without extraordinary requirements
- Real production value for developers
- Community or commercial support

### May Exclude
- Abandoned projects (no updates >2 years)
- Services requiring illegal/unethical access
- Purely promotional/marketing offers
- Services with deceptive "free" claims
- Region-locked to inaccessible areas

### Automatic Exclusion
- No free tier whatsoever
- Requires payment for any usage
- Illegal or pirated software
- Services promoting spam/scams
- Dark web or anonymous access required

### Examples of Exclusions

#### Heroku Free Tier (Discontinued 2022)
- **Decision**: Not included due to discontinuation
- **Reason**: Heroku ended their free tier in November 2022
- **Evaluation**: Originally evaluated in historical records
- **Alternative**: Consider Railway, Render, or Fly.io

#### Firebase Spark Plan Limitations
- **Decision**: Limited inclusion due to restrictive quotas
- **Reason**: Daily limits too low for practical development use
- **Evaluation**: Reviewed for potential inclusion with updated limits
- **Status**: Under review for future consideration

## Documentation Standards

### Required Fields for Every Service

#### Free Tier Details
```yaml
free_tier:
  type: "always-free|time-limited-trial|credits|mixed"
  always_free:
    included: true|false
    limits: ["Specific limits with units"]
    duration: "Unlimited" or "X months from signup"
  time_limited:
    included: true|false
    duration_days: 30
    description: "Trial terms"
  credits:
    included: true|false
    amount: "$100"
    duration_days: 30
    description: "Credit terms"
```

#### Gotchas and Limitations
Every service must document:
- Usage limit enforcement
- Regional restrictions
- Account requirements
- Billing surprises
- Service dependencies
- Performance limitations

#### Cost Projections
- Current free tier cost: $0
- Typical cost after free expires
- Scaling cost trajectory
- Hidden cost categories

### Verification Requirements

#### Source Citations
- Official documentation links
- Pricing page references
- Terms of service excerpts
- Recent blog posts/announcements

#### Freshness Tracking
- Last verified date
- Verification source
- Change history notes
- Community update flags

## Risk Assessment Categories

### Low Risk Services
- Always-free with generous limits
- Transparent pricing
- Easy migration path
- Standard technology stack

**Examples:** GitHub Actions, Cloudflare CDN, Fly.io shared CPU

### Medium Risk Services
- Time-limited trials
- Moderate usage limits
- Some vendor lock-in
- Learning curve required

**Examples:** AWS EC2, GCP Cloud Functions, Azure VMs

### High Risk Services
- Complex pricing models
- High vendor lock-in
- Easy to exceed limits
- Hidden cost traps

**Examples:** AWS with cross-service dependencies, GCP with egress costs

## Community Validation Process

### Automated Checks
- Schema validation on all entries
- Link freshness monitoring
- YAML syntax verification
- Cross-reference validation

### Manual Review
- Peer review of new submissions
- Accuracy verification against sources
- Completeness assessment
- Risk factor evaluation

### Ongoing Maintenance
- Monthly freshness audits
- Community issue tracking
- Automated update notifications
- Changelog maintenance

## Ethical Considerations

### Transparency First
We document limitations even when they make services less attractive. Better to know upfront than face billing surprises.

### No False Advertising
Services are classified based on official terms, not marketing claims. If documentation contradicts marketing, we follow documentation.

### User Protection
Every entry includes "not for" recommendations to prevent users from choosing inappropriate services for their use cases.

### Commercial Neutrality
No sponsor preferences or affiliate relationships. Services included based on merit and user value, not business arrangements.

## Updating Evaluation Criteria

### When to Reassess
- Major service policy changes
- New free tier announcements
- Billing incident reports
- Community feedback patterns

### Process for Changes
- Document rationale for changes
- Update affected service entries
- Communicate changes to community
- Maintain backward compatibility

---

*Our evaluation framework ensures users can make informed decisions. Free should mean free—not "free until it costs you unexpectedly".*