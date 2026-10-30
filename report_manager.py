import calendar
from datetime import date, timedelta

from storage import load_records, load_settings
from config import DATE_FORMAT


def weekly_report():
    records = load_records()
    today = date.today()

    start_date = today - timedelta(days=6)

    weekly_records = [
        record for record in records
        if start_date <= datetime_date(record["date"]) <= today
    ]

    total = sum(record["amount"] for record in weekly_records)
    daily_goal = load_settings().get("daily_goal", 2000)

    print("\n========== WEEKLY WATER REPORT ==========")
    print(f"Period: {start_date} to {today}")
    print(f"Total consumption: {total} ml")
    print(f"Daily average: {total / 7:.2f} ml")
    print(f"Daily goal: {daily_goal} ml")

    print("\nDaily breakdown:")

    for offset in range(7):
        current = start_date + timedelta(days=offset)
        current_string = current.strftime(DATE_FORMAT)

        amount = sum(
            record["amount"]
            for record in weekly_records
            if record["date"] == current_string
        )

        print(f"{current_string}: {amount} ml")

    print("=" * 42)


def monthly_report():
    records = load_records()
    today = date.today()

    monthly_records = [
        record for record in records
        if datetime_date(record["date"]).year == today.year
        and datetime_date(record["date"]).month == today.month
    ]

    total = sum(record["amount"] for record in monthly_records)
    days_in_month = calendar.monthrange(today.year, today.month)[1]

    active_days = len(set(
        record["date"] for record in monthly_records
    ))

    print("\n========== MONTHLY WATER REPORT ==========")
    print(f"Month: {today.strftime('%B %Y')}")
    print(f"Total consumption: {total} ml")
    print(f"Average per calendar day: {total / days_in_month:.2f} ml")
    print(f"Days with recorded intake: {active_days}")
    print("=" * 43)


def average_intake_report():
    records = load_records()

    if not records:
        print("No water intake records available.")
        return

    daily_totals = {}

    for record in records:
        record_date = record["date"]
        daily_totals[record_date] = (
            daily_totals.get(record_date, 0)
            + record["amount"]
        )

    total = sum(daily_totals.values())
    number_of_days = len(daily_totals)
    average = total / number_of_days

    print("\n========== AVERAGE INTAKE REPORT ==========")
    print(f"Total consumption: {total} ml")
    print(f"Recorded days: {number_of_days}")
    print(f"Average daily intake: {average:.2f} ml")
    print("=" * 43)


def goal_completion_report():
    records = load_records()
    daily_goal = load_settings().get("daily_goal", 2000)

    if not records:
        print("No water intake records available.")
        return

    daily_totals = {}

    for record in records:
        record_date = record["date"]
        daily_totals[record_date] = (
            daily_totals.get(record_date, 0)
            + record["amount"]
        )

    completed_days = sum(
        1 for amount in daily_totals.values()
        if amount >= daily_goal
    )

    recorded_days = len(daily_totals)
    percentage = completed_days / recorded_days * 100

    print("\n========== GOAL COMPLETION REPORT ==========")
    print(f"Daily goal: {daily_goal} ml")
    print(f"Recorded days: {recorded_days}")
    print(f"Goal achieved: {completed_days} day(s)")
    print(f"Goal completion rate: {percentage:.2f}%")
    print("=" * 44)


def datetime_date(value):
    return date.fromisoformat(value)
