"""Generate local configuration without overwriting an existing .env."""
from pathlib import Path
import secrets
target = Path(__file__).with_name(".env")
if target.exists():
    print("Existing .env preserved.")
else:
    text = Path(__file__).with_name(".env.example").read_text()
    for placeholder in ("replace-with-a-long-random-secret", "replace-with-a-random-password", "replace-with-a-different-random-password"):
        text = text.replace(placeholder, secrets.token_urlsafe(32))
    target.write_text(text)
    print("Created .env with random local credentials.")
