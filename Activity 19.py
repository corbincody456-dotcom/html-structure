import random
import time
from datetime import datetime

def show_menu():
    print("\n" + "="*40)
    print("    SUMMER TIMES ")
    print("="*40)
    print("1. Calculate Beach Packing & Budget")
    print("2. Generate Random Summer Activity")
    print("3. Start Summer Countdown Timer")
    print("4. Exit")
    print("="*40)

def beach_budget_planner():
    print("\n---  BEACH BUDGET & PACKING PLANNER ---")
    try:
        funds = float(input("Enter your total summer vacation budget ($): "))
        hotel_cost = float(input("Enter total hotel cost ($): "))
        days = int(input("How many days will your trip last? "))
        
        remaining = funds - hotel_cost
        
        if remaining < 0:
            print(" Warning: Your hotel costs exceed your budget!")
            return
            
        daily_allowance = remaining / days
        print(f"\n Total Remaining Funds: ${remaining:.2f}")
        print(f" Your Daily Spending Limit: ${daily_allowance:.2f} per day.")
        
        # Quick packing recommendation
        print("\n Quick Packing Checklist:")
        checklist = ["Sunscreen (SPF 50+)", "Swimwear", "Sunglasses", "Beach Towel", "Water Bottle"]
        for item in checklist:
            print(f"  [ ] {item}")
            
    except ValueError:
        print(" Invalid input. Please enter numbers only.")

def get_random_activity():
    print("\n--- SUMMER ACTIVITY GENERATOR ---")
    activities = [
        "Go to the beach and build a giant sandcastle.",
        "Host an outdoor backyard BBQ with friends.",
        "Visit a local ice cream shop and try a completely new flavor.",
        "Go on a late-night stargazing walk.",
        "Take a scenic road trip or hike nearby.",
        "Have a water balloon fight to cool down."
    ]
    chosen = random.choice(activities)
    print(f"Your summer activity for today: \n {chosen}")

def countdown_timer():
    print("\n--- ⏱  MINI SUMMER COUNTDOWN ---")
    print("Simulating a short 5-second countdown to the ultimate beach trip...")
    # Uses time.sleep to simulate a real-time countdown clock
    for i in range(5, 0, -1):
        print(f" {i} seconds left before vacation...")
        time.sleep(1) # Pauses code execution for 1 second
    print("pack your bags! Summer vacation has officially started! ")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            beach_budget_planner()
        elif choice == "2":
            get_random_activity()
        elif choice == "3":
            countdown_timer()
        elif choice == "4":
            print("\nStay cool and enjoy the summer! Goodbye! ")
            break
        else:
            print(" Invalid option. Please type 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
