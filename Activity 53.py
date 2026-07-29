import random
import time

def fun_calculator():
    print("✨ Welcome to the Mischievous Random Calculator! ✨")
    
    try:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
    except ValueError:
        print("That is not a number! You broke the math.")
        return

    print("\nChoose an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    print("Calculating...")
    time.sleep(1) # Dramatic pause

    # Real calculation logic
    if choice == '1':
        real_ans = num1 + num2
        op = "+"
    elif choice == '2':
        real_ans = num1 - num2
        op = "-"
    elif choice == '3':
        real_ans = num1 * num2
        op = "*"
    elif choice == '4':
        if num2 == 0:
            print("Error: Cannot divide by zero! The universe almost imploded.")
            return
        real_ans = num1 / num2
        op = "/"
    else:
        print("Invalid choice! Try again.")
        return

    # Random fun twist: 30% chance the calculator gets sassy and changes the answer
    is_pranked = random.random() < 0.3
    
    if is_pranked:
        fake_ans = real_ans + random.choice([-10, -5, 5, 10, 42])
        print(f"\nMath says: {num1} {op} {num2} = {real_ans}")
        print(f"👻 BUT my mood says the answer is actually {fake_ans}. Deal with it!")
    else:
        print(f"\nCorrect Result: {num1} {op} {num2} = {real_ans}")
        print("Wow, boring! The math actually worked normally this time.")

if __name__ == "__main__":
    fun_calculator()