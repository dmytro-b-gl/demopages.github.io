---
title: Docker Compose Basics
nav_order: 20
---
# Docker Compose Basics

Minimal patterns for `docker-compose.yml`. See also: [Kubernetes Probes](kubernetes-probes.md).

## Example
```yaml
version: "3.9"
services:
  api:
    image: ghcr.io/acme/api:latest
    ports:
      - "8080:8080"
    environment:
      - DATABASE_URL=postgresql://app:pass@db:5432/app
    depends_on:
      - db
  db:
    image: postgres:16
    environment:
      POSTGRES_USER: app
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: app
    volumes:
      - dbdata:/var/lib/postgresql/data
volumes:
  dbdata: {}
```

## Quick notes
- Use **named volumes** for persistent data.
- Keep **secrets** out of the file; inject via environment or secret store.
- Health checks:
```yaml
healthcheck:
  test: ["CMD-SHELL", "curl -fsS http://localhost:8080/health || exit 1"]
  interval: 10s
  timeout: 2s
  retries: 5
```

---
**Prev:** [REST API Versioning](../web/rest-api-versioning.md) · **Next:** [Kubernetes Probes](kubernetes-probes.md) · **Back:** [Home](../index.md)
