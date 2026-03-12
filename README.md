# Secure API Security Lab

A small hands-on API security project demonstrating a Broken Access Control / IDOR-style vulnerability and its remediation using basic authentication and authorization checks in FastAPI.

## Project Scope

This lab includes:
- a vulnerable API version
- a remediated API version
- curl-based security testing
- screenshots of authorization test results

## Disclaimer

This project is a personal learning lab created to demonstrate API security concepts such as Broken Access Control and authorization checks.

All data, users, and scenarios are simulated and do not represent any real system or organization.

## Security Tests

### Authorization Tests

The secure API was tested using curl commands to verify authentication and authorization controls.

### Successful request, access denied, and missing header

![Security Test](screenshots/security-tests-main.png)

### Invalid header values

![Invalid Header Test](screenshots/security-tests-invalid-header.png)