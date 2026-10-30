from datetime import date, datetime
from config import DATE_FORMAT


def get_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")


def get_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt).strip())

            if number > 0:
                return number

            print("Enter a number greater than zero.")

        except ValueError:
            print("Enter a valid whole number.")


def get_date(prompt):
    while True:
        value = input(prompt).strip()

        try:
            parsed = datetime.strptime(value, DATE_FORMAT).date()

            if parsed.strftime(DATE_FORMAT) != value:
                raise ValueError

            if parsed > date.today():
                print("Future dates are not allowed.")
                continue

            return value

        except ValueError:
            print("Enter a valid date in YYYY-MM-DD format.")


def current_date():
    return date.today().strftime(DATE_FORMAT)


def current_time():
    return datetime.now().strftime("%H:%M:%S")


def pause():
    input("\nPress Enter to continue...")
