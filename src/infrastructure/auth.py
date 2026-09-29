import hashlib
import json
import secrets
from pathlib import Path

AUTH_PATH = Path("config/auth.json")

def set_password(password):
    salt = secrets.token_bytes(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100_000,
    )

    config = {
        "salt": salt.hex(),
        "password_hash": password_hash.hex(),
    }

    with AUTH_PATH.open("w") as file:
        json.dump(config, file)

def verify_password(password):
    with AUTH_PATH.open() as file:
        config = json.load(file)

    salt = bytes.fromhex(config["salt"])

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100_000,
    )

    return secrets.compare_digest(
        password_hash.hex(),
        config["password_hash"],
    )        