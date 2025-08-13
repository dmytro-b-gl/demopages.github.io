---
title: REST API Versioning
nav_order: 11
---
# REST API Versioning

A few pragmatic approaches to versioning APIs. Related: [HTTP Status Codes](http-status-codes.md).

## Options
1. **URI versioning**: `/v1/orders` → clear but leaks version into links.
2. **Header versioning**: `Accept: application/vnd.acme.v1+json` → clean URLs, more setup.
3. **Query param**: `/orders?version=1` → easy, but blends with filtering.
4. **Resource evolution**: Avoid breaking changes; add fields, never remove/repurpose.

## Tips
- Use **semantic versions** internally; expose **simple major versions** to clients.
- Deprecate loudly: response headers (`Deprecation`, `Link: sunset`) and docs.
- Guarantee **backward compatibility** within a major version.

---
**Prev:** [HTTP Status Codes](http-status-codes.md) · **Next:** [Docker Compose Basics](../devops/docker-compose-basics.md) · **Back:** [Home](../index.md)
