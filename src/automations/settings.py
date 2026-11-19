# src/automations/settings.py
import os
from pathlib import Path

# settings.py -> automations/ -> src/ -> project root
ROOT_DIR = Path(__file__).resolve().parents[2]

# Can be overridden with the DOWNLOAD_DIR environment variable (e.g. in Docker/CI).
# Not resolved on purpose: a relative value is rejected by set_download_default_dir.
DOWNLOAD_DIR = Path(os.getenv("DOWNLOAD_DIR", ROOT_DIR / "downloads"))
