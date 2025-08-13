from src.lib.utils import sha256_hex

def test_sha256_hex():
    assert sha256_hex("a") == "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb"
