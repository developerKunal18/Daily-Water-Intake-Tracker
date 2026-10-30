from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

RECORDS_FILE = DATA_DIR / "water_records.json"
SETTINGS_FILE = DATA_DIR / "settings.json"

DATE_FORMAT = "%Y-%m-%d"
DEFAULT_DAILY_GOAL = 2000
