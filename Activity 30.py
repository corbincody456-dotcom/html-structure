def power_calculator():
    print(" Power Calculator ")
    
    # Get the base number
    while True:
        try:
            base = float(input("Enter the base number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Get the exponent
    while True:
        try:
            exponent = float(input("Enter the exponent (power): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Handle the math exception: 0 raised to a negative power
    if base == 0 and exponent < 0:
        print("Error: Zero cannot be raised to a negative power (division by zero).")
        return

    # Handle the math exception: Negative base with a fractional exponent
    if base < 0 and not exponent.is_integer():
        # Using complex numbers to correctly handle complex results (e.g., square root of -4)
        result = complex(base) ** exponent
        print(f"\nResult: {base} ^ {exponent} = {result}")
    else:
        # Standard floating-point or integer calculation
        result = base ** exponent
        
        # Format output to remove trailing decimals if it's a whole number
        if result.is_integer():
            result = int(result)
            
        print(f"\nResult: {int(base) if base.is_integer() else base} ^ {int(exponent) if exponent.is_integer() else exponent} = {result}")

# Run the calculator
if __name__ == "__main__":
    power_calculator()