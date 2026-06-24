from datetime import date

def calculate_age(birth_date):
    """Calculates age correctly by accounting for the current month and day."""
    today = date.today()
    # Subtract 1 if the current calendar day is before the birth calendar day
    birthday_has_passed = (today.month, today.day) >= (birth_date.month, birth_date.day)
    age = today.year - birth_date.year - (0 if birthday_has_passed else 1)
    return age

def main():
    print("===  Age Checking ===")
    
    while True:
        try:
            # Gather birthday components from user input
            year = int(input("Enter birth year : "))
            month = int(input("Enter birth month (1-12): "))
            day = int(input("Enter birth day (1-31): "))
            
            # This line will raise a ValueError if the date is physically impossible
            user_birthday = date(year, month, day)
            
            # Check if the birth date entered is in the future
            if user_birthday > date.today():
                print("Error: Birth date cannot be in the future! Please try again.\n")
                continue
                
            break  # Exit the loop if date creation is successful
            
        except ValueError:
            print("Invalid input! Please ensure you enter real numbers and a valid date calendar combo.\n")

    # Calculate exact age
    exact_age = calculate_age(user_birthday)
    print("\n" + "="*30)
    print(f"Your Birthday: {user_birthday.strftime('%B %d, %Y')}")
    print(f"Calculated Age: {exact_age} years old")
    print("="*30)

    # Check age milestones/eligibility rules
    if exact_age >= 18:
        print("Status: You are an adult. ")
    elif exact_age >= 13:
        print("Status: You are a teenager. ")
    else:
        print("Status: You are a child. ")

if __name__ == "__main__":
    main()