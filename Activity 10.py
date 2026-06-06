def print_congrats_banner(name, event):
    message = f"🌟 CONGRATULATIONS, {name}! 🌟"
    sub_message = f"Success looks good on you. Cheers to your {event}!"
    
    # Calculate box width based on the longest sentence
    width = max(len(message), len(sub_message)) + 4
    
    # Print the stylized box
    print("✨" * (width // 2 + 2))
    print(f"║ {message.center(width)} ║")
    print(f"║ {sub_message.center(width)} ║")
    print("✨" * (width // 2 + 2))

# Run the function
print_congrats_banner("Corbin", "Coding")