---
title: HTTP Status Codes (Quick Guide)
nav_order: 10
---
# HTTP Status Codes — Quick Guide

A rapid reference for common HTTP codes you’ll see when building APIs.
See also: [REST API Versioning](rest-api-versioning.md).

## 2xx — Success
- **200 OK** — Successful request.
- **201 Created** — New resource created (often with `Location` header).
- **204 No Content** — Success with no response body.

## 3xx — Redirects
- **301 Moved Permanently** — Use the new URL for future requests.
- **302 Found** — Temporary redirect.
- **307/308** — Like 302/301 but *preserve* HTTP method.

## 4xx — Client Errors
- **400 Bad Request** — Malformed input.
- **401 Unauthorized** — Missing/invalid auth.
- **403 Forbidden** — Authenticated, but not allowed.
- **404 Not Found** — Resource doesn’t exist.
- **409 Conflict** — Resource state conflict (e.g., version mismatch).
- **422 Unprocessable Entity** — Validation failed.

## 5xx — Server Errors
- **500 Internal Server Error** — Catch-all server error.
- **502 Bad Gateway** — Upstream service failed.
- **503 Service Unavailable** — Temporary overload or maintenance.

---
**Next:** [REST API Versioning](rest-api-versioning.md) · **Back:** [Home](../index.md)
