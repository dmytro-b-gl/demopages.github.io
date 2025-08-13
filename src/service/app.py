from fastapi import FastAPI, Query
from src.lib.utils import sha256_hex

app = FastAPI(title="Mini API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hash")
def hash_text(text: str = Query(..., min_length=1, max_length=2048)):
    return {"algo": "sha256", "text": text, "hash": sha256_hex(text)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
