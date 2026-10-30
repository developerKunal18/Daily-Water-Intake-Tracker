from storage import initialize_storage

from water_manager import (
    set_daily_goal,
    add_water_intake,
    show_daily_progress,
    view_records,
    search_records_by_date,
    delete_intake_record
)

from report_manager import (
    weekly_report,
    monthly_report,
    average_intake_report,
    goal_completion_report
)

from utils import pause


def show_menu():
    print("\n" + "=" * 46)
    print("        DAILY WATER INTAKE TRACKER")
    print("=" * 46)
    print("1. Set Daily Water Goal")
    print("2. Add Water Intake")
    print("3. View Today's Progress")
    print("4. View All Intake Records")
    print("5. Search Records by Date")
    print("6. Delete Intake Record")
    print("7. Weekly Water Report")
    print("8. Monthly Water Report")
    print("9. Average Intake Report")
    print("10. Goal Completion Report")
    print("0. Exit")
    print("=" * 46)


def main():
    initialize_storage()

    actions = {
        "1": set_daily_goal,
        "2": add_water_intake,
        "3": show_daily_progress,
        "4": view_records,
        "5": search_records_by_date,
        "6": delete_intake_record,
        "7": weekly_report,
        "8": monthly_report,
        "9": average_intake_report,
        "10": goal_completion_report
    }

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Thank you for using Daily Water Intake Tracker!")
            break

        action = actions.get(choice)

        if action:
            try:
                action()
            except (OSError, ValueError, KeyError, TypeError) as error:
                print(f"An error occurred: {error}")

            pause()

        else:
            print("Invalid choice. Select a number from 0 to 10.")
            pause()


if __name__ == "__main__":
    main()
