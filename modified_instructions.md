AWESOME-FREE: Complete Setup & KiloCode Instructions
Repo Name & Metadata
GitHub Repository: awesome-free

Description: A comprehensive, community-curated catalog of free tier services, always-free offerings, and free software tools across all categories. Resources for developers, creators, and builders.

Topics: awesome, awesome-list, free-tier, free-software, saas, paas, iaas, open-source, resources, curated-list

Directory Structure (Production-Ready)
text
awesome-free/
├── README.md                          # Main entry point, overview, table of contents
├── CONTRIBUTING.md                    # Contribution guidelines & standards
├── CODE_OF_CONDUCT.md                 # Community standards
├── LICENSE                            # MIT or similar
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── service-addition.md        # Template for adding new service
│   │   ├── service-update.md          # Template for updating service info
│   │   └── broken-link.md             # Template for reporting dead links
│   ├── PULL_REQUEST_TEMPLATE.md       # PR template with checklist
│   ├── workflows/
│   │   ├── validate.yml               # Validate YAML/JSON schema on PR
│   │   ├── link-checker.yml           # Check for broken links weekly
│   │   └── freshness-check.yml        # Flag outdated entries (> 6 months)
│   └── dependabot.yml                 # Auto-update dependencies in tools/
│
├── docs/                              # Guides and documentation
│   ├── OVERVIEW.md                    # Philosophy & structure of awesome-free
│   ├── HOW_TO_USE.md                  # Guide for finding services
│   ├── EVALUATION_CRITERIA.md         # How we evaluate "free" (always-free vs trial vs credits)
│   ├── OPTIMIZATION_STRATEGIES.md     # How to stack free tiers effectively
│   ├── COST_AVOIDANCE.md              # Common cost traps & how to avoid them
│   ├── PROVIDER_GUIDES/
│   │   ├── AWS.md                     # AWS free tier deep dive
│   │   ├── GCP.md                     # Google Cloud free tier deep dive
│   │   ├── AZURE.md                   # Azure free tier deep dive
│   │   ├── CLOUDFLARE.md              # Cloudflare free tier deep dive
│   │   ├── FLY_IO.md                  # Fly.io free tier deep dive
│   │   └── [other major providers].md
│   ├── CATEGORY_GUIDES/
│   │   ├── COMPUTE.md                 # Compute services overview
│   │   ├── DATABASES.md               # Database services overview
│   │   ├── STORAGE.md                 # Storage services overview
│   │   ├── CDN_EDGE.md                # CDN & Edge computing overview
│   │   ├── SERVERLESS.md              # Serverless & FaaS overview
│   │   ├── DEVTOOLS.md                # Development tools overview
│   │   └── [other categories].md
│   └── RESEARCH_SOURCES.md            # Master list of sources & links
│
├── services/                          # Machine-readable service catalog (YAML)
│   ├── compute/
│   │   ├── aws-ec2.yaml
│   │   ├── aws-lambda.yaml
│   │   ├── gcp-compute-engine.yaml
│   │   ├── gcp-cloud-functions.yaml
│   │   ├── azure-vm.yaml
│   │   ├── oracle-always-free.yaml
│   │   ├── fly-io.yaml
│   │   ├── render.yaml
│   │   ├── railway.yaml
│   │   ├── vercel.yaml
│   │   ├── netlify.yaml
│   │   ├── cloudflare-workers.yaml
│   │   └── [more compute services].yaml
│   │
│   ├── databases/
│   │   ├── aws-dynamodb.yaml
│   │   ├── aws-rds.yaml
│   │   ├── gcp-firestore.yaml
│   │   ├── gcp-cloud-sql.yaml
│   │   ├── azure-cosmosdb.yaml
│   │   ├── mongodb-atlas.yaml
│   │   ├── planetscale.yaml
│   │   ├── neon.yaml
│   │   ├── railway-postgres.yaml
│   │   ├── supabase.yaml
│   │   ├── firebase-realtime.yaml
│   │   └── [more db services].yaml
│   │
│   ├── storage/
│   │   ├── aws-s3.yaml
│   │   ├── gcp-cloud-storage.yaml
│   │   ├── azure-blob.yaml
│   │   ├── cloudflare-r2.yaml
│   │   ├── b2-backblaze.yaml
│   │   ├── contabo.yaml
│   │   └── [more storage services].yaml
│   │
│   ├── cdn-edge/
│   │   ├── cloudflare-cdn.yaml
│   │   ├── aws-cloudfront.yaml
│   │   ├── bunny-cdn.yaml
│   │   └── [more cdn services].yaml
│   │
│   ├── devtools/
│   │   ├── github.yaml
│   │   ├── gitlab.yaml
│   │   ├── jfrog-artifactory.yaml
│   │   ├── sentry.yaml
│   │   ├── datadog.yaml
│   │   ├── grafana-cloud.yaml
│   │   ├── statuscake.yaml
│   │   └── [more dev tools].yaml
│   │
│   ├── communication/
│   │   ├── sendgrid.yaml
│   │   ├── mailgun.yaml
│   │   ├── twilio.yaml
│   │   ├── discord-api.yaml
│   │   └── [more comms services].yaml
│   │
│   ├── ai-ml/
│   │   ├── huggingface-spaces.yaml
│   │   ├── replicate.yaml
│   │   ├── together-ai.yaml
│   │   ├── ollama.yaml
│   │   └── [more ai/ml services].yaml
│   │
│   └── [additional-categories]/
│       └── [services].yaml
│
├── stacks/                            # Reference architectures (combining services)
│   ├── serverless-api/
│   │   ├── fly-io-postgres-redis.yaml
│   │   ├── aws-lambda-dynamodb-s3.yaml
│   │   └── cloudflare-workers-d1.yaml
│   │
│   ├── full-stack-app/
│   │   ├── vercel-firebase-supabase.yaml
│   │   ├── netlify-functions-mongodb-atlas.yaml
│   │   └── fly-io-custom-db-cdn.yaml
│   │
│   ├── static-site-cdn/
│   │   ├── github-pages-cloudflare.yaml
│   │   ├── netlify-builtins.yaml
│   │   └── vercel-edge-functions.yaml
│   │
│   ├── monitoring-observability/
│   │   ├── prometheus-grafana-cloud.yaml
│   │   ├── sentry-datadog-statuscake.yaml
│   │   └── updown-io-free.yaml
│   │
│   └── [other stacks].yaml
│
├── tools/                             # Utility scripts & automation
│   ├── schema/
│   │   ├── service.schema.json        # JSON Schema for service YAML validation
│   │   ├── stack.schema.json          # JSON Schema for stack YAML validation
│   │   └── README.md                  # Schema documentation
│   │
│   ├── python/
│   │   ├── requirements.txt           # Python dependencies
│   │   ├── validate.py                # Validate all YAML against schema
│   │   ├── compare.py                 # Compare providers side-by-side
│   │   ├── export_csv.py              # Export services to CSV
│   │   ├── export_json.py             # Export services to JSON
│   │   ├── link_checker.py            # Check for broken links
│   │   ├── generate_markdown.py       # Generate markdown from YAML
│   │   └── freshness_check.py         # Flag stale entries (> 6 months)
│   │
│   ├── bash/
│   │   ├── validate.sh                # Bash wrapper for validation
│   │   ├── update_readme.sh           # Auto-generate README from services
│   │   └── check_syntax.sh            # Quick syntax checker
│   │
│   └── README.md                      # Tools documentation & usage guide
│
├── data/                              # Generated exports (for easy browsing)
│   ├── services.csv                   # All services in CSV format
│   ├── services.json                  # All services in JSON format
│   ├── comparison.md                  # Auto-generated comparison table
│   └── GENERATED.md                   # Note that these are auto-generated
│
└── archive/                           # Historical changes & sunset services
    ├── discontinued.yaml              # Services no longer free (with sunset date)
    ├── CHANGELOG.md                   # Major changes to service offerings
    └── HISTORICAL.md                  # Links to old evaluation decisions
Awesome-Free Service Schema (YAML)
Every service entry follows this standardized schema:

text
# services/[category]/[service-name].yaml

service:
  id: "aws-ec2"                         # Unique identifier (provider-service)
  name: "EC2"                           # Display name
  provider: "AWS"                       # Provider name
  category: "compute"                   # compute, database, storage, cdn-edge, serverless, devtools, etc.
  url: "https://aws.amazon.com/ec2/"   # Official service page
  
  free_tier:
    type: "always-free"                 # always-free | time-limited-trial | credits | mixed
    
    # Always-free details
    always_free:
      included: true
      limits:
        - "750 hours/month t2.micro or t3.micro"
        - "1 year from account creation"
        - "30 GB/month EBS (gp2 or io1)"
        - "15 GB/month outbound data transfer (first year)"
      duration: "12 months, then billable"
    
    # Time-limited trial
    time_limited:
      included: false
      duration_days: null
      description: null
    
    # Free credits (new account incentive)
    credits:
      included: true
      amount: "$200"
      duration_days: 30
      description: "New customer credit, expires in 30 days"
  
  # Region availability for always-free
  regions:
    always_free:
      - "us-east-1"
      - "us-west-1"
      - "us-west-2"
      - "eu-west-1"
      - "ap-southeast-1"
    note: "Check regional availability; some services region-locked"
  
  # Comprehensive gotchas & cost traps
  gotchas:
    - "Only free during first 12 months from account creation"
    - "Must stay under 750 hrs/month to avoid overage charges"
    - "Outbound data transfer to internet costs $0.09/GB after 15GB/month"
    - "Public IP costs $0.005/hour if detached from running instance"
    - "t2.micro not available in all regions; check before launch"
  
  # Perfect use cases for this service
  best_for:
    - "Small production API or web server"
    - "Database server (MySQL, PostgreSQL, etc.)"
    - "Dev/test/staging Linux or Windows environment"
    - "Learning cloud infrastructure"
  
  # What NOT to use this for (under free tier)
  not_for:
    - "High-traffic production app (will exceed free tier quickly)"
    - "Video encoding or media processing"
    - "Scientific computing or modeling"
  
  # Services that work well together (stack-friendly)
  complementary_services:
    - service_id: "aws-rds"
      notes: "Managed database; RDS free tier works with EC2"
    - service_id: "aws-s3"
      notes: "Object storage; complements EC2 apps"
    - service_id: "aws-lambda"
      notes: "Serverless alternative to EC2 for small workloads"
    - service_id: "cloudflare-cdn"
      notes: "CDN for static assets to reduce EC2 bandwidth"
  
  # Estimated monthly cost breakdown
  cost:
    under_free_tier: "$0"
    typical_after_free: "$10-50 (depending on compute & data)"
    scaling_trajectory: "Linear; pay per hour of compute + data transfer"
  
  # Authentication & prerequisites
  requirements:
    credit_card: true
    phone_verification: false
    identity_verification: false
    minimum_age: 18
    geography_restrictions: "Must have valid address in supported country"
  
  # Documentation & learning
  resources:
    official_docs: "https://docs.aws.amazon.com/ec2/"
    free_tier_page: "https://aws.amazon.com/free/"
    tutorial: "https://aws.amazon.com/getting-started/"
    community: "https://stackoverflow.com/questions/tagged/amazon-ec2"
  
  # When was this info last verified?
  metadata:
    last_verified: "2026-01-26"
    verified_by: "github_username"
    source: "AWS official docs, AWS pricing page"
    notes: "t2 vs t3: t3 is newer, may offer better performance"
  
  # Flags for automation
  flags:
    time_sensitive: true              # Needs frequent verification
    cost_risk: high                   # Easy to accidentally incur charges
    vendor_lock_in: medium            # AWS-specific APIs
    learning_curve: medium             # Requires cloud knowledge
    setup_time: 10                    # Minutes to get first instance running
KiloCode / AI Assistant Comprehensive Prompt
Save this as .kilocode-instructions.md or .github/copilot-instructions.md:

text
# awesome-free: AI-Assisted Development Prompt

You are KiloCode, assisting in building and maintaining **awesome-free**, a comprehensive, open-source catalog of free tier services, open-source software, and free offerings across all categories (cloud computing, databases, development tools, creative software, etc.).

## Project Philosophy & Goals

### Core Mission
Provide a single source of truth for developers, creators, and builders to discover and strategically combine free offerings into production-grade systems without vendor lock-in or unexpected costs.

### Core Values
1. **Accuracy** - Only cite official docs or credible sources < 6 months old
2. **Completeness** - Include gotchas, regional constraints, and cost traps (not just benefits)
3. **Usability** - Services organized by category, easy to search and compare
4. **Currency** - Flag outdated entries; automated weekly freshness checks
5. **Community** - Welcoming contributions; clear guidelines for additions/updates
6. **No Ads/Affiliates** - Pure curation, no sponsor preference or affiliate links

### What We Cover
- **Infrastructure**: Compute, databases, storage, networking (AWS, GCP, Azure, Oracle, Cloudflare, Fly.io, Railway, etc.)
- **Application Platforms**: Web hosting, serverless, FaaS (Vercel, Netlify, Render, Fly.io, Heroku alternatives)
- **Developer Tools**: CI/CD, monitoring, testing, security scanning (GitHub Actions, Sentry, Datadog, etc.)
- **Communication**: Email, SMS, chat APIs (SendGrid, Mailgun, Twilio, Discord)
- **AI/ML**: Model hosting, inference, fine-tuning (Hugging Face Spaces, Replicate, Together AI)
- **Creative Tools**: Open-source software with free tiers (Blender, GIMP, Krita, etc.)
- **Web3/Blockchain**: If applicable (IPFS, Arweave, etc.)

### What We DON'T Cover
- Services with no free tier whatsoever
- Illegal or pirated software
- Services requiring Darkweb access
- Spam/scam services
- Abandoned projects (no updates > 2 years)

## KiloCode Modes

KiloCode operates in different modes for specialized tasks:

- **Architect mode**: Use for planning, designing system architecture, or strategizing solutions.
- **Code mode**: Use for writing, modifying, or refactoring code.
- **Ask mode**: Use for explanations, documentation, or answering technical questions.
- **Debug mode**: Use for troubleshooting issues, investigating errors, or diagnosing problems.
- **Orchestrator mode**: Use for complex, multi-step projects that require coordination across different specialties.

When performing tasks, delegate to the appropriate mode using KiloCode's delegation mechanism. For example, if a task requires planning before implementation, first use Architect mode to design, then switch to Code mode for implementation.

---

## Data Schema & Standards

### Service Entry Structure (YAML)

Every service is defined in `services/[category]/[service-id].yaml`:

```yaml
service:
  id: "provider-service"              # Unique identifier (kebab-case)
  name: "Human-Readable Name"
  provider: "Company Name"
  category: "compute|database|storage|cdn-edge|serverless|devtools|communication|ai-ml|creative|web3"
  url: "https://official-service-url"
  
  free_tier:
    type: "always-free|time-limited|credits|mixed"
    
    always_free:
      included: true|false
      limits:
        - "Specific limit with units (e.g., '5GB storage/month', '1M requests/month')"
        - "Add multiple limits"
      duration: "Unlimited" or "12 months from signup"
    
    time_limited:
      included: true|false
      duration_days: 30
      description: "Trial period, then paid"
    
    credits:
      included: true|false
      amount: "$100"
      duration_days: 30
      description: "New account incentive"
  
  regions:
    always_free: ["region-1", "region-2"]
    note: "Any regional constraints"
  
  gotchas:
    - "Cost trap or limitation that users should know"
    - "Billing surprise or unexpected charge"
    - "Service pauses/shuts down under certain conditions"
    - "Data egress costs extra"
    - "Regional availability limited"
  
  best_for:
    - "Specific use case where this service excels"
    - "Production API servers"
  
  not_for:
    - "Use case where free tier is inadequate"
    - "High-traffic apps"
  
  complementary_services:
    - service_id: "other-service-id"
      notes: "Why these services work together"
  
  cost:
    under_free_tier: "$0"
    typical_after_free: "$5-20/month"
    scaling_trajectory: "Linear, logarithmic, or exponential"
  
  requirements:
    credit_card: true|false
    phone_verification: false
    identity_verification: false
    minimum_age: 18
    geography_restrictions: "Description of regional availability"
  
  resources:
    official_docs: "https://..."
    free_tier_page: "https://..."
    tutorial: "https://..."
    community: "https://..."
  
  metadata:
    last_verified: "YYYY-MM-DD"
    verified_by: "github_username"
    source: "Official docs, pricing page, blog post"
    notes: "Any additional context"
  
  flags:
    time_sensitive: true              # Needs verification every month
    cost_risk: "low|medium|high"      # Likelihood of accidental charges
    vendor_lock_in: "low|medium|high" # How easy to migrate away
    learning_curve: "low|medium|high" # Difficulty to get started
    setup_time: 5                     # Minutes to get first instance/project
Stack Entry Structure (YAML)
Stacks in stacks/[category]/[stack-name].yaml show how to combine services:

text
stack:
  name: "Full-Stack Serverless API"
  category: "serverless-api"
  description: "Production-ready REST API with database, caching, and CDN"
  
  services:
    - service_id: "fly-io"
      role: "API server"
      config: "3 x shared-cpu-1x, 256MB RAM"
      free_estimate: "Always free"
    
    - service_id: "fly-io-postgres"
      role: "Primary database"
      config: "3GB storage, 1 shared connection"
      free_estimate: "Always free"
    
    - service_id: "fly-io-redis"
      role: "Cache layer"
      config: "1GB shared instance"
      free_estimate: "Always free"
    
    - service_id: "cloudflare-cdn"
      role: "CDN for static assets"
      config: "Unlimited bandwidth"
      free_estimate: "Always free"
  
  total_monthly_cost: "$0"
  estimated_capacity: "10k-100k requests/day"
  
  pros:
    - "Global distribution out of the box"
    - "No vendor lock-in (all major frameworks supported)"
    - "Scales affordably when traffic increases"
  
  cons:
    - "Shared CPU under sustained load"
    - "Need to manage multiple services (complexity)"
    - "Learning curve for Fly deployment"
  
  alternatives:
    - name: "AWS Lambda + DynamoDB + CloudFront"
      cost: "$0-50/month"
      pros: "Industry standard, lots of docs"
      cons: "Vendor lock-in, egress costs add up"
  
  getting_started:
    - "Create Fly.io account"
    - "Deploy sample Node.js API"
    - "Provision Postgres database"
    - "Set up Cloudflare as DNS + CDN"
    - "Monitor with Fly.io built-in metrics"
  
  resources:
    - "https://fly.io/docs/getting-started/"
    - "https://example-tutorial.com"
Code Generation & Maintenance Tasks
When I Ask You to...
"Add service [name]"
Use Code mode for this task. Generate a complete YAML service entry in services/[category]/[service-id].yaml following the schema exactly. Include all required fields, cite official docs or < 6-month-old sources, mark any uncertain info with [NEEDS VERIFICATION], list all gotchas, even if they seem obvious, include complementary services that work well together.

Example prompt: "Add AWS Lambda free tier service following the schema. Include: 1M requests/month free tier, Lambda@Edge limits, cold start gotchas, and complementary services (API Gateway, S3, DynamoDB)."

"Update service [name]"
Use Code mode for this task. Identify what changed (pricing, limits, regions, gotchas), update relevant YAML fields, update last_verified date, add note to metadata.notes about what changed, flag if change affects complementary services.

"Create stack [name]"
Use Architect mode for this task. Generate a complete stack YAML in stacks/[category]/[stack-name].yaml, list all component services with their free tier configs, calculate realistic total monthly cost, include pros/cons for this specific combination, list 2-3 alternative stacks with cost comparison, provide step-by-step getting-started guide.

"Generate Python validation script"
Use Code mode for this task. Create a script that loads all YAML files from services/ and stacks/, validates against JSON Schema in tools/schema/, checks for required fields (all must be present), validates date formats (YYYY-MM-DD), warns if last_verified is > 180 days old, checks for broken links (HEAD request to url field), validates YAML syntax, reports missing complementary service references, outputs color-coded results (green=valid, yellow=warning, red=error).

"Generate comparison CSV/JSON from services"
Use Code mode for this task. Create a script that reads all service YAML files, extracts key fields: name, provider, free_tier.type, limits, cost, best_for, exports to CSV or JSON, sorts by category, then provider, adds convenience columns (setup_time, learning_curve, cost_risk).

"Generate markdown from services"
Use Code mode for this task. Create a script that reads all service YAML files, generates markdown tables grouped by category, includes comparison columns, adds links to official pages, outputs to data/comparison.md (auto-updated).

"Suggest a stack for [use case]"
Use Architect mode for this task. Analyze the use case, then recommend 2-3 service combinations that fit, estimate total cost for each, list pros/cons of each approach, explain why services work together, provide setup steps and gotchas, suggest learning resources.

"Update README"
Use Code mode for this task. Regenerate README with project overview and philosophy, quick-start guide (finding a service), auto-generated table of contents by category, stats (total services, providers, categories), links to guides (optimization, cost avoidance), call-to-action for contributions, license and attribution.

Quality Standards & Validation
Required for Every Service Entry
 Unique ID in kebab-case (provider-service)

 Official URL (links to landing page, not docs)

 Free tier type clearly stated (always-free vs trial vs credits)

 All limits with units (KB, GB, requests, hours, etc.)

 At least 2-3 gotchas (cost traps, limitations, surprises)

 Best use cases (realistic, not marketing-speak)

 Complementary services listed

 Estimated cost breakdown

 Last verified date within 180 days

 Source cited (official docs preferred)

Accuracy Standards
Never invent numbers - If you don't have exact limits, mark as [NEEDS VERIFICATION]

Cite sources - Every fact traceable to official docs or credible blog (< 6 months old)

Note date of verification - Services change frequently; flag anything old

Include caveats - "This is correct as of [date]" or "Check official docs for current pricing"

Completeness Standards
List ALL gotchas - Cost traps, regional limits, bandwidth charges, account freezes, etc.

Don't hide negatives - Users expect balanced evaluation, not sales pitch

Explain why - "Why is egress expensive?" not just "egress is expensive"

Suggest alternatives - Include competing services in the gotchas/alternatives section

Currency Standards
Validate age - Any entry > 180 days old should be re-verified

Automated checks - Python script checks last_verified and warns

CI/CD validation - GitHub Actions runs on every PR to validate schema

Community oversight - Ask contributors to flag stale entries they know about

File Organization Rules
One service = one YAML file (don't combine multiple services)

File naming = [provider]-[service].yaml in lowercase (aws-ec2.yaml, not AWS-EC2.yaml)

Directory by category = services/compute/, services/database/, etc.

Consistent indentation = 2 spaces, no tabs

No trailing whitespace

Contribution Workflow
When you generate issues or PR templates for contributors:

New Service:

Link to schema

Checklist of required fields

Example YAML entry

Link to provider's free tier page

Request: "Create services/[category]/[service-id].yaml"

Update Service:

What changed (limits, pricing, regions)?

Updated YAML fields

New last_verified date

Note in metadata about change

Request: "Update services/[category]/[service-id].yaml"

Broken Link:

Which service/link is broken?

When did you last verify it worked?

Suggested fix

Documentation Standards
When generating markdown files:

Use clear headings - H1 for section, H2 for subsections

Add examples - Show real URLs, actual limits, real use cases

Link extensively - Every service should link to official docs

Include TOC - Table of contents for long docs

Consistent formatting - Code blocks for commands, bold for emphasis

Avoid jargon - Explain cloud terms in plain English

Automation & Scripts
When asked to generate tools:

Validation (validate.py):

Load all YAML

Validate against schema

Check date freshness

Verify links (optional, expensive)

Report errors with line numbers

Comparison (compare.py):

Side-by-side provider comparison

Filter by category, cost, features

Output formatted table (markdown, CSV, JSON)

Export (export_csv.py, export_json.py):

Convert services to portable formats

Include all fields, flatten nested objects

Sort by category

GitHub Actions (.github/workflows/):

Validate schema on every PR

Run scheduled checks (weekly for freshness)

Output nice formatting (comment on PR with results)

Cache dependencies to speed up runs

Use standard actions (actions/checkout, actions/setup-python)

YAML Files
2-space indentation (not tabs)

Consistent key ordering (id, name, provider, category, etc.)

No trailing whitespace

Comments explaining non-obvious fields

ISO 8601 dates (YYYY-MM-DD)

When Uncertain
Mark with [NEEDS_VERIFICATION]

Cite the source (even if you're unsure)

Flag in metadata for community review

Ask for official documentation link

Don't guess on limits or pricing

Check the service's official pricing page first

Success Criteria
A successful awesome-free repo will:

Contain 200+ services within 6 months (all major cloud providers + common tools)

Have < 5% broken links (validated weekly)

Keep 95% of entries fresh (last_verified within 180 days)

Support 10+ categories (compute, database, storage, cdn, serverless, devtools, comms, ai/ml, creative, web3)

Enable users to build production systems on free tiers alone

Provide clear cost comparison (always-free vs credits vs trials)

Highlight gotchas more than benefits (balanced evaluation)

Be automated (CI/CD validates, links check, exports generate)

Be community-driven (clear contribution process, responsive reviews)

Remain vendor-neutral (no affiliate links, no sponsor bias)

Final Notes
This project serves developers, creators, and builders who want to:

Explore free offerings without hidden costs

Combine free tiers into production systems

Avoid vendor lock-in

Understand the cost trajectory before scaling

Your job is to keep this catalog accurate, complete, and actionable.

text

***

## GitHub Governance Files

Create these in the root:

### `CONTRIBUTING.md`

```markdown
# Contributing to awesome-free

Thanks for your interest in improving awesome-free! This document explains how to contribute.

## Adding a New Service

1. **Check if it exists** - Search `services/` to avoid duplicates
2. **Create YAML entry** - Use `.yaml` (not `.yml`) following the schema
3. **File naming** - `services/[category]/[provider-service].yaml` (lowercase)
4. **Use the template** - Copy from an existing entry in same category
5. **Cite sources** - Link to official docs or < 6-month-old sources
6. **Test validation** - Run `python tools/validate.py` to check schema
7. **Open a PR** - Include which fields you verified (not just copy-paste)

## Updating an Existing Service

1. **Verify the change** - Check official docs; don't rely on rumors
2. **Update relevant fields** - Only change what actually changed
3. **Update last_verified** - Set to today's date
4. **Add metadata note** - Explain what changed
5. **Test validation** - Run `python tools/validate.py`
6. **Open a PR** - Cite the source of the change

## Questions / Issues

- **Broken link** - Open an issue with link and when you discovered it
- **Service removed free tier** - Mark in YAML and add to `archive/discontinued.yaml`
- **Wrong information** - Open an issue with correct info + source

## Code of Conduct

Be respectful. We value accuracy over speed. We prioritize users over companies.
CODE_OF_CONDUCT.md
text
# Code of Conduct

## Our Commitment

awesome-free is committed to providing a welcoming and inclusive environment for all contributors, regardless of background or identity.

## Our Standards

**Examples of behavior that creates a positive environment:**
- Using welcoming and inclusive language
- Being respectful of differing opinions
- Accepting constructive criticism gracefully
- Focusing on what is best for the community
- Showing empathy towards other community members

**Examples of unacceptable behavior:**
- Harassment or discrimination
- Trolling or insulting/derogatory comments
- Spam or promotional content
- Publishing private information without consent
- Other conduct which could reasonably be considered inappropriate in a professional setting

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported to the maintainers. All complaints will be reviewed and investigated. Repeated violations will result in removal from the project.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant](https://www.contributor-covenant.org/).
.gitignore
text
# Python
__pycache__/
*.py[cod]
*$py.class
*.egg-info/
dist/
build/
venv/
env/

# Generated files
data/services.csv
data/services.json
data/comparison.md

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# KiloCode
.kilocode-instructions.md
Quick Start for Repository Initialization
bash
# 1. Create the repo
git init awesome-free
cd awesome-free

# 2. Create directory structure
mkdir -p services/{compute,database,storage,cdn-edge,serverless,devtools,communication,ai-ml,creative}
mkdir -p stacks/{serverless-api,full-stack-app,static-site-cdn,monitoring-observability}
mkdir -p docs/{PROVIDER_GUIDES,CATEGORY_GUIDES}
mkdir -p tools/{schema,python,bash}
mkdir -p data
mkdir -p .github/{ISSUE_TEMPLATE,workflows}
mkdir -p archive

# 3. Create initial files
touch README.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE
touch .gitignore .github/PULL_REQUEST_TEMPLATE.md
touch docs/OVERVIEW.md docs/HOW_TO_USE.md docs/EVALUATION_CRITERIA.md
touch tools/schema/service.schema.json tools/schema/stack.schema.json

# 4. Copy kilocode-instructions.md to root or .github/
cp kilocode-instructions.md .kilocode-instructions.md

# 5. Initialize git
git add .
git commit -m "Initial commit: directory structure and documentation templates"
Summary
Repo Name: awesome-free

Philosophy: Comprehensive, accurate, balanced curation of free services with emphasis on gotchas, cost traps, and realistic use cases.

Structure:

Machine-readable YAML catalog in services/ (by category)

Reference stacks in stacks/

Guides in docs/

Validation & export tools in tools/

Auto-generated comparisons in data/

KiloCode Integration: KiloCode prompt guides generation of service entries, stacks, validation scripts, and documentation while maintaining schema consistency and accuracy standards.

Best Practices:

Weekly freshness validation (flag entries > 180 days old)

Schema validation on every PR

Broken link detection

Community contribution guidelines

Balanced evaluation (gotchas ≥ benefits)