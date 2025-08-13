---
title: Architecture
nav_order: 2
---
# Architecture (High-level)

```
┌──────────┐       HTTP       ┌───────────────┐
│  Client  │  ───────────▶    │   FastAPI     │
└──────────┘                  │  /health, /hash
                              │   uses sha256_hex()
                              └───────────────┘
                                         │
                                         │ import
                                         ▼
                                  ┌────────────┐
                                  │  utils.py  │
                                  └────────────┘
```

- The API is a minimal FastAPI app (`/src/service/app.py`).
- Business-logic helper lives in `/src/lib/utils.py`.
- Tests in `/tests`.
- See also the [Docker Compose basics](devops/docker-compose-basics.md).

**Code links**
- [Service README]({{ site.github.repository_url }}/blob/main/src/service/README.md)
- [utils.py]({{ site.github.repository_url }}/blob/main/src/lib/utils.py)
