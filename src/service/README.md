# Service (FastAPI)

A tiny FastAPI app with a health endpoint and a `/hash` helper route.

## Run locally

```bash
uvicorn src.service.app:app --port 8080 --reload
```

Try:
- http://localhost:8080/health
- http://localhost:8080/hash?text=hello
