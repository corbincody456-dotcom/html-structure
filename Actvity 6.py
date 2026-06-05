import json
import os

DATA_FILE = "birthdays.json"

def load_birthdays():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            try: return json.load(file)
            except json.JSONDecodeError: return {}
    return {}

def save_birthdays(birthdays):
    with open(DATA_FILE, "w") as file:
        json.dump(birthdays, file, indent=4)

def add_birthday(birthdays):
    name = input("Name: ").strip().title()
    date = input("Date (e.g., MM/DD): ").strip()
    if name and date:
        birthdays[name] = date
        save_birthdays(birthdays)
        print("✅ Saved!")

def main():
    birthdays = load_birthdays()
    while True:
        print("\n1. Add, 2. View, 3. Exit")
        choice = input("Choice: ")
        if choice == "1": add_birthday(birthdays)
        elif choice == "2": print(birthdays)
        elif choice == "3": break

if __name__ == "__main__":
    main()
