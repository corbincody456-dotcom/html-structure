from flask import Flask, render_template, request, session
import secrets
import string

app = Flask(__name__)
# Set a secret key to use session variables securely
app.secret_key = secrets.token_hex(16)

def generate_challenge():
    """Generates a random challenge scenario and its correct password."""
    # Randomly choose a length between 8 and 14
    length = secrets.choice(range(8, 15))
    
    # Pools of characters
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*"
    
    # Mandate at least one of each required type to meet modern standards
    pw_chars = [
        secrets.choice(lower),
        secrets.choice(upper),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]
    
    # Fill the rest of the password length with a mix of all characters
    all_combined = lower + upper + digits + symbols
    for _ in range(length - 4):
        pw_chars.append(secrets.choice(all_combined))
        
    # Shuffle the characters using a secure mechanism
    secrets.SystemRandom().shuffle(pw_chars)
    correct_password = "".join(pw_chars)
    
    challenge_data = {
        "length": length,
        "must_have_upper": True,
        "must_have_lower": True,
        "must_have_digit": True,
        "must_have_symbol": True,
        "correct_password": correct_password
    }
    return challenge_data

@app.route("/", methods=["GET", "POST"])
def index():
    message = None
    message_class = None
    
    if request.method == "POST":
        # Check if the user is submitting a password guess
        user_guess = request.form.get("user_guess", "").strip()
        correct_password = session.get("correct_password")
        
        if user_guess == correct_password:
            message = " Correct! Your Python logic successfully cracked the challenge!"
            message_class = "success"
        else:
            message = f" Incorrect. Try adjusting your code. (Hint: The expected length was {session.get('length')})"
            message_class = "error"
            
    # Generate a brand new challenge for the user on GET request or after an evaluation
    challenge = generate_challenge()
    session["correct_password"] = challenge["correct_password"]
    session["length"] = challenge["length"]
    
    return render_template("index.html", challenge=challenge, message=message, message_class=message_class)

if __name__ == "__main__":
    app.run(debug=True)