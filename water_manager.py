from datetime import datetime

from config import DATE_FORMAT
from storage import (
    load_records,
    save_records,
    load_settings,
    save_settings
)
from utils import (
    get_positive_integer,
    get_date,
    current_date,
    current_time
)


def generate_record_id(records):
    highest = 0

    for record in records:
        record_id = record.get("record_id", "")

        if record_id.startswith("WTR"):
            try:
                highest = max(highest, int(record_id[3:]))
            except ValueError:
                continue

    return f"WTR{highest + 1:04d}"


def set_daily_goal():
    settings = load_settings()

    print("\n--- Set Daily Water Goal ---")
    print(f"Current goal: {settings.get('daily_goal', 2000)} ml")

    goal = get_positive_integer("Enter new daily goal in ml: ")

    settings["daily_goal"] = goal
    save_settings(settings)

    print(f"Daily water goal updated to {goal} ml.")


def add_water_intake():
    records = load_records()

    print("\n--- Add Water Intake ---")

    amount = get_positive_integer(
        "Enter water consumed in ml: "
    )

    record = {
        "record_id": generate_record_id(records),
        "date": current_date(),
        "time": current_time(),
        "amount": amount
    }

    records.append(record)
    save_records(records)

    print("\nWater intake recorded successfully!")
    print(f"Record ID: {record['record_id']}")
    print(f"Amount: {amount} ml")

    show_daily_progress()


def get_daily_total(target_date):
    records = load_records()

    return sum(
        record.get("amount", 0)
        for record in records
        if record.get("date") == target_date
    )


def show_daily_progress():
    settings = load_settings()
    goal = settings.get("daily_goal", 2000)

    today = current_date()
    total = get_daily_total(today)

    remaining = max(0, goal - total)
    percentage = (total / goal) * 100 if goal else 0

    print("\n========== DAILY WATER PROGRESS ==========")
    print(f"Date             : {today}")
    print(f"Daily Goal       : {goal} ml")
    print(f"Water Consumed   : {total} ml")
    print(f"Remaining        : {remaining} ml")
    print(f"Goal Completed   : {percentage:.1f}%")

    if total >= goal:
        print("Congratulations! Daily goal achieved.")
    else:
        print("Keep tracking your intake throughout the day.")

    print("=" * 43)


def view_records():
    records = load_records()

    print("\n--- Water Intake History ---")

    if not records:
        print("No water intake records found.")
        return

    records.sort(
        key=lambda item: (item.get("date", ""), item.get("time", "")),
        reverse=True
    )

    for record in records:
        print("-" * 35)
        print(f"Record ID : {record.get('record_id')}")
        print(f"Date      : {record.get('date')}")
        print(f"Time      : {record.get('time')}")
        print(f"Amount    : {record.get('amount')} ml")

    print("-" * 35)
    print(f"Total entries: {len(records)}")


def search_records_by_date():
    records = load_records()

    target_date = get_date(
        "Enter date (YYYY-MM-DD): "
    )

    results = [
        record for record in records
        if record.get("date") == target_date
    ]

    if not results:
        print("No records found for this date.")
        return

    total = 0

    print(f"\n--- Water Records for {target_date} ---")

    for record in results:
        print(
            f"{record['record_id']} | "
            f"{record['time']} | "
            f"{record['amount']} ml"
        )
        total += record["amount"]

    print(f"Total consumption: {total} ml")


def delete_intake_record():
    records = load_records()

    record_id = input("Enter record ID to delete: ").strip().upper()

    for record in records:
        if record.get("record_id", "").upper() == record_id:
            print(
                f"Date: {record['date']} | "
                f"Amount: {record['amount']} ml"
            )

            confirm = input(
                "Are you sure you want to delete this record? (y/n): "
            ).strip().lower()

            if confirm == "y":
                records.remove(record)
                save_records(records)
                print("Record deleted successfully.")
            else:
                print("Deletion cancelled.")

            return

    print("Record ID not found.")
