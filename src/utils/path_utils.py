from pathlib import Path
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

def get_local_dvc_path() -> Path:
    """Returns Path object for LOCAL_DVC_PATH from .env, cross-platform safe"""
    raw_path = os.getenv("LOCAL_DVC_PATH")
    return Path(raw_path).expanduser().resolve() if raw_path else None

def get_data_path(subfolder: str = "") -> Path:
    """Returns data folder (e.g. data/raw or data/processed)"""
    base = Path("data")
    return (base / subfolder).resolve() if subfolder else base.resolve()

def ensure_path(path: Path):
    """Create folder if it doesn't exist"""
    path.mkdir(parents=True, exist_ok=True)
