# Attack Demonstration

## Project Summary
This lab demonstrates how Broken Access Control / IDOR-style issues can appear in a simple API and how they can be mitigated with authentication and authorization checks.

## Vulnerable Endpoint
GET /users/{user_id}

## Vulnerable Behavior
In the vulnerable version, any user record can be accessed directly by changing the `user_id` in the URL.

Examples:
- /users/1
- /users/2
- /users/3

No authentication or ownership validation is performed.

## Security Risk
This allows unauthorized access to sensitive user account data.

## Secure Behavior
In the secure version, the API requires an `X-User-Id` header to simulate authentication.

The API then checks whether the requested `user_id` matches the authenticated user.

## Test Results

### Allowed request
```bash
curl -H "X-User-Id: 1" http://127.0.0.1:8000/users/1