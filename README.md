# Daily Water Intake Tracker

A simple Python application for recording daily water consumption, monitoring intake goals, and generating weekly and monthly reports.

## Features

- Set a daily water intake goal
- Record water consumption in millilitres
- Generate automatic record IDs
- View daily water intake progress
- Calculate remaining water intake
- View complete consumption history
- Search records by date
- Delete incorrect intake records
- Generate weekly and monthly reports
- Calculate average daily water consumption
- Track daily goal completion percentage
- Store records using JSON

## Technologies Used

- Python 3
- JSON
- datetime
- calendar

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Daily-Water-Intake-Tracker.git
```

### 2. Open the project directory

```bash
cd Daily-Water-Intake-Tracker
```

### 3. Run the application

```bash
python main.py
```

No external packages are required.

## Project Structure

```text
Daily-Water-Intake-Tracker/
├── main.py
├── config.py
├── storage.py
├── utils.py
├── water_manager.py
├── report_manager.py
├── requirements.txt
├── .gitignore
├── README.md
└── data/
    ├── water_records.json
    └── settings.json
```

## How to Use

1. Set your daily water intake goal.
2. Record water consumption throughout the day.
3. View your daily progress.
4. Check remaining intake against your configured goal.
5. Review weekly and monthly reports.
6. Track your goal completion percentage.

## Example

If the daily goal is 2,000 ml and the recorded consumption is 1,500 ml:

- Daily goal: 2,000 ml
- Water consumed: 1,500 ml
- Remaining: 500 ml
- Goal completed: 75%

## Learning Outcomes

- Python functions and modules
- JSON file handling
- Date and time handling
- Lists and dictionaries
- Data filtering and calculations
- Report generation
- Menu-driven application development

## Future Improvements

- Add a graphical user interface
- Integrate SQLite or MySQL
- Add water intake charts
- Add desktop notifications
- Export reports to CSV
- Add multiple user profiles

## Author

Python Project Challenge

## License

Free to use for educational and personal learning purposes.
