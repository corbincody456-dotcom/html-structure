import csv
import os
from datetime import datetime

class DailyDataHelper:
    def __init__(self, filename="daily_data.csv"):
        self.filename = filename
        self._initialize_file()

    def _initialize_file(self):
        """Creates the CSV file with headers if it does not exist."""
        if not os.path.exists(self.filename):
            with open(self.filename, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["date", "category", "value", "notes"])

    def add_entry(self, category, value, notes=""):
        """Adds a new row of data with the current date."""
        current_date = datetime.now().strftime("%Y-%m-%d")
        with open(self.filename, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([current_date, category, value, notes])
        print("Entry added successfully.")

    def get_todays_entries(self):
        """Returns all entries recorded today."""
        current_date = datetime.now().strftime("%Y-%m-%d")
        entries = []
        if not os.path.exists(self.filename):
            return entries
            
        with open(self.filename, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["date"] == current_date:
                    entries.append(row)
        return entries

# Example usage:
# helper = DailyDataHelper()
# helper.add_entry("Water", "2 Liters", "Drank during morning walk")
# print(helper.get_todays_entries())