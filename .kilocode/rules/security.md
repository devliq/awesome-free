# Security Rules for Awesome-Free Project

This document outlines comprehensive security guidelines for the awesome-free project. These rules ensure the protection of sensitive data, secure handling of user information, and safe evaluation of free services. The guidelines are tailored to the project's focus on curating legitimate free services while preventing scams, data breaches, and other security risks.

## Restricted Files and Sensitive Data Handling

### Restricted Files
- **Never access or modify files containing sensitive information**:
  - `.env` files and environment configuration
  - `config/secrets.yml` or similar credential files
  - Private keys (`*.pem`, `*.key`, `id_rsa`, etc.)
  - Database connection strings with credentials
  - API keys and tokens
  - User-submitted data files (e.g., `user_data.json`, `submissions/` directory)

### Security Best Practices for File Handling
- Use environment variables for all sensitive configuration
- Never commit secrets, passwords, or API keys to version control
- Implement proper input validation and sanitization for all data inputs
- Use secure defaults for all configuration options
- Follow principle of least privilege for file permissions
- Encrypt sensitive data at rest and in transit

### Examples
- Store API keys in `.env` files and load them via `python-dotenv` in Python scripts
- Use `os.environ.get('API_KEY')` instead of hardcoding keys in code
- Validate file uploads to prevent malicious file types (e.g., only allow YAML/JSON for service definitions)

## Security Best Practices for Code and Data Handling

### Code Security
- Implement proper error handling to avoid information leakage
- Use parameterized queries to prevent SQL injection
- Validate and sanitize all user inputs before processing
- Avoid logging sensitive information (passwords, tokens, PII)
- Implement rate limiting to protect against abuse
- Use secure coding practices (OWASP guidelines)

### Data Handling
- Encrypt sensitive data in databases and files
- Implement access controls and authentication for data operations
- Regularly audit data access logs
- Use secure communication protocols (HTTPS, TLS 1.3+)
- Implement data retention policies for temporary data

### Examples
- In Python: Use `psycopg2` with parameterized queries: `cursor.execute("SELECT * FROM services WHERE id = %s", (service_id,))`
- In JavaScript: Use `helmet` middleware for security headers in Express.js apps
- Validate service URLs with regex: `^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$`

## Service Evaluation Security

### Verifying Service Legitimacy
- **Always verify service authenticity** before inclusion:
  - Check official website and documentation
  - Cross-reference with multiple trusted sources
  - Verify domain ownership and SSL certificates
  - Review service terms of service for hidden costs or data collection policies
  - Test service functionality in isolated environments

### Avoiding Scams and Malicious Services
- Flag services with suspicious patterns:
  - Services requiring payment for "verification" or "activation"
  - Services promising unrealistic features or unlimited resources
  - Services with poor documentation or no contact information
  - Services hosted on free subdomains (e.g., `service.freehost.com`)
  - Services with recent domain registrations (< 6 months)

### Evaluation Process
1. Initial domain and SSL verification
2. Manual testing of free tier functionality
3. Review of privacy policy and data handling practices
4. Community feedback and usage reports
5. Automated security scanning of service endpoints

### Examples
- Use `whois` command to check domain registration date: `whois example.com | grep "Creation Date"`
- Test SSL certificates: `openssl s_client -connect example.com:443 -servername example.com`
- Flag services requiring credit card for "free" signup as potential scams

## Data Protection for User-Submitted Information

### User Data Handling
- **Minimize data collection**: Only collect necessary information for service evaluation
- Implement GDPR/CCPA compliance for user data
- Use anonymization techniques for sensitive submissions
- Provide clear data usage policies in forms and documentation
- Allow users to request data deletion

### Secure Storage and Transmission
- Store user data in encrypted databases
- Use secure APIs for data transmission
- Implement proper session management
- Regular security audits of data storage systems

### Examples
- Use `bcrypt` for hashing user emails if needed: `hashed_email = bcrypt.hashpw(email.encode(), bcrypt.gensalt())`
- Implement CORS policies in web applications to restrict data access
- Use `https` for all user-facing forms and APIs

## Tools for Security Scanning

### Static Application Security Testing (SAST)
- Use `bandit` for Python security linting
- Integrate `eslint-security` for JavaScript/TypeScript
- Run `gosec` for Go code security analysis

### Dependency Scanning
- Implement `safety` for Python dependency vulnerability checks
- Use `npm audit` for JavaScript dependencies
- Integrate `trivy` for container and dependency scanning

### Dynamic Application Security Testing (DAST)
- Use `OWASP ZAP` for automated security testing
- Implement `sqlmap` for SQL injection testing
- Run `nikto` for web server vulnerability scanning

### CI/CD Integration
- Integrate security scans in GitHub Actions or GitLab CI
- Set up automated dependency updates with `dependabot`
- Implement pre-commit hooks for security checks
- Require security review for all pull requests

### Examples
- GitHub Actions workflow:
  ```yaml
  - name: Security Scan
    uses: github/super-linter/slim@v4
    env:
      DEFAULT_BRANCH: main
      GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      VALIDATE_PYTHON_BLACK: true
      VALIDATE_PYTHON_FLAKE8: true
      VALIDATE_PYTHON_ISORT: true
  ```
- Pre-commit hook: `pre-commit install && pre-commit run --all-files`

## Legal and Compliance

- Comply with relevant security standards (ISO 27001, SOC 2)
- Maintain security incident response procedures
- Conduct regular security training for contributors
- Document security features and known limitations
- Report security vulnerabilities through responsible disclosure

## Best Practices Summary

- **Defense in Depth**: Implement multiple layers of security controls
- **Zero Trust**: Verify all access requests regardless of source
- **Regular Updates**: Keep dependencies and systems up-to-date
- **Monitoring**: Implement logging and alerting for security events
- **Training**: Educate team members on security awareness

These security rules ensure the awesome-free project maintains high security standards while curating legitimate free services. Regular reviews and updates to this document are recommended as security threats evolve.