def get_positive_float(prompt):
    """Safely gets a positive number from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Please enter a number greater than or equal to 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number (e.g., 49.99).")

def calculate_shopping_discount():
    print("--- 🛍️ Welcome to the Shopping Discount Calculator 🛍️ ---")
    
    # 1. Get original price and discount percentage safely
    original_price = get_positive_float("Enter the original item price ($): ")
    discount_percentage = get_positive_float("Enter the discount percentage (0-100%): ")
    
    # Cap the discount percentage at 100% to avoid negative final costs
    if discount_percentage > 100:
        print("\n⚠️ Note: The discount cannot exceed 100%. Setting discount to 100%.")
        discount_percentage = 100.0

    # 2. Math Calculations
    discount_amount = original_price * (discount_percentage / 100)
    final_price = original_price - discount_amount

    # 3. Print the receipt details rounded to 2 decimal places
    print("\n================ RECEIPT ================")
    print(f"Original Price:     ${original_price:,.2f}")
    print(f"Discount Applied:   {discount_percentage:.1f}%")
    print(f"Total Money Saved:  ${discount_amount:,.2f}")
    print("-----------------------------------------")
    print(f"Final Price to Pay: ${final_price:,.2f}")
    print("=========================================")

# Run the calculator
if __name__ == "__main__":
    calculate_shopping_discount()