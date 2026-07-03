# Set up page configurations
st.set_page_config(
    page_title="Number Reversal Center",
    
    layout="centered"
)

# Custom tit Number Reversal Center")
st.write("Enter a single integer or a comma-separated list of numbers to reverse them instantly!")

# Section 1: Reverse the digits of a single number
st.header("Option 1: Reverse Digits of a Number")
single_input = st.text_input("Enter a single number (e.g., -12345):", value="12345")

if single_input:
    # Remove whitespace
    clean_input = single_input.strip()
    
    # Validation logic to ensure it's a valid integer
    is_negative = clean_input.startswith('-')
    check_str = clean_input[1:] if is_negative else clean_input
    
    if check_str.isdigit():
        # Core Python Slicing logic [::-1] to reverse strings/digits
        reversed_digits = check_str[::-1]
        
        # Re-apply the negative sign if applicable
        final_number = f"-{reversed_digits}" if is_negative else reversed_digits
        
        st.success(f"**Original:** {clean_input}  |  **Reversed Digits:** {final_number}")
    else:
        st.error("Please enter a valid whole number.")

st.markdown("---")

# Section 2: Reverse the sequence order of a list of numbers
st.header("Option 2: Reverse a List of Numbers")
list_input = st.text_input("Enter multiple numbers separated by commas (e.g., 10, 20, 30, 40):", value="10, 20, 30, 40")

if list_input:
    try:
        # Convert the string input into a native Python list of floats/ints
        original_list = [float(num.strip()) for num in list_input.split(",") if num.strip()]
        
        # Clean up display (convert floats to ints if they are whole numbers)
        formatted_list = [int(x) if x.is_integer() else x for x in original_list]
        
        # Core Python slicing to reverse list order efficiently
        reversed_list = formatted_list[::-1]
        
        st.success(f"**Original Order:** {formatted_list}")
        st.success(f"**Reversed Order:** {reversed_list}")
    except ValueError:
        st.error("Please ensure the list contains only numbers separated by commas.")