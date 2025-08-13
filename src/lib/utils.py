import hashlib

def sha256_hex(text: str) -> str:
    """Return hex SHA-256 of `text`."""
    h = hashlib.sha256()
    h.update(text.encode("utf-8"))
    return h.hexdigest()
