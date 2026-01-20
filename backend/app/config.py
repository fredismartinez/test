from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
VAULTS_DIR = DATA_DIR / "vaults"


DEFAULT_CONFIG = {
    "theme": "light",
    "editor": {
        "fontSize": 14,
        "lineHeight": 1.6,
    },
}
