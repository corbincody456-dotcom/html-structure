import calendar
import datetime


def show_current_month():
  # Get today's year and month
  now = datetime.datetime.now()
  year = now.year
  month = now.month

  # Print nice header and calendar
  print(f"\nToday is: {now.strftime('%B %d, %Y')}\n")
  print(calendar.month(year, month))


def show_custom_calendar():
  try:
    y = int(input("Enter year (e.g., 2026): "))
    m = int(input("Enter month (1-12): "))
    print("\n" + calendar.month(y, m))
  except ValueError:
    print("Please enter valid numbers for year and month.")


if __name__ == "__main__":
  show_current_month()
  print("-" * 28)
  choice = input("Do you want to see a different month? (y/n): ").lower()
  if choice == "y":
    show_custom_calendar()