---
title: Kubernetes Probes
nav_order: 21
---
# Kubernetes Probes — Liveness vs Readiness vs Startup

- **Liveness**: *Should this container be restarted?* Detects deadlocks/crashes.
- **Readiness**: *Can this pod receive traffic?* Gates Services before the app is ready.
- **Startup**: Slow starters? Use this to delay other probes.

## Example
```yaml
livenessProbe:
  httpGet: { path: /healthz, port: 8080 }
  initialDelaySeconds: 10
  periodSeconds: 10

readinessProbe:
  httpGet: { path: /ready, port: 8080 }
  initialDelaySeconds: 5
  periodSeconds: 5
```

**Tip:** Tie readiness to dependencies (DB, cache).

---
**Prev:** [Docker Compose Basics](docker-compose-basics.md) · **Next:** [PostgreSQL Indexing 101](../database/postgres-indexing.md) · **Back:** [Home](../index.md)
