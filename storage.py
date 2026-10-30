import json
from config import (
    DATA_DIR,
    RECORDS_FILE,
    SETTINGS_FILE,
    DEFAULT_DAILY_GOAL
)


def initialize_storage():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not RECORDS_FILE.exists():
        with RECORDS_FILE.open("w", encoding="utf-8") as file:
            json.dump([], file, indent=4)

    if not SETTINGS_FILE.exists():
        settings = {
            "daily_goal": DEFAULT_DAILY_GOAL
        }

        with SETTINGS_FILE.open("w", encoding="utf-8") as file:
            json.dump(settings, file, indent=4)


def load_json(file_path, default):
    initialize_storage()

    try:
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    except (OSError, json.JSONDecodeError) as error:
        print(f"Could not read {file_path.name}: {error}")
        return default


def save_json(file_path, data):
    initialize_storage()

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_records():
    data = load_json(RECORDS_FILE, [])

    return data if isinstance(data, list) else []


def save_records(records):
    save_json(RECORDS_FILE, records)


def load_settings():
    data = load_json(SETTINGS_FILE, {
        "daily_goal": DEFAULT_DAILY_GOAL
    })

    if not isinstance(data, dict):
        return {"daily_goal": DEFAULT_DAILY_GOAL}

    return data


def save_settings(settings):
    save_json(SETTINGS_FILE, settings)
