from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

def check_pin_safety(pin):
    """Evaluates the safety of a given PIN code."""
    if not pin.isdigit():
        return False, "PIN must contain only numbers."
    
    length = len(pin)
    if length < 4 or length > 8:
        return False, "PIN must be between 4 and 8 digits long."

    # Rule 1: Repeating identical digits (e.g., 1111, 999999)
    if len(set(pin)) == 1:
        return False, "Too weak! Avoid repeating the same number."

    # Rule 2: Sequential ascending/descending digits (e.g., 1234, 8765)
    ascending = "0123456789"
    descending = "9876543210"
    if pin in ascending or pin in descending:
        return False, "Too weak! Avoid sequential numbers."

    # Rule 3: Common easily guessed combinations
    common_pins = [
        "1212", "2020", "1999", "2000", "2001", "2002", "1004", "4321", 
        "1122", "12345", "123456", "1234567", "12345678", "654321"
    ]
    if pin in common_pins:
        return False, "Too weak! This is a highly common and easily guessed PIN."

    return True, "Strong PIN! This looks safe to use."

# Combined HTML/CSS Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PIN Safety Checker</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f7f6; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); width: 100%; max-width: 400px; text-align: center; }
        input[type="password"] { width: 90%; padding: 12px; margin: 15px 0; border: 2px solid #ccc; border-radius: 5px; font-size: 18px; text-align: center; letter-spacing: 5px; }
        button { background-color: #007bff; color: white; border: none; padding: 12px 20px; font-size: 16px; border-radius: 5px; cursor: pointer; width: 100%; }
        button:hover { background-color: #0056b3; }
        #result { margin-top: 20px; font-weight: bold; font-size: 16px; padding: 10px; border-radius: 5px; display: none; }
        .success { background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
        .error { background-color: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
    </style>
</head>
<body>
    <div class="card">
        <h2>PIN Safety Checker</h2>
        <p>Test your PIN strength instantly. Your data never leaves your device.</p>
        <form id="pinForm">
            <input type="password" id="pinInput" maxlength="8" placeholder="Enter PIN" required autocomplete="off">
            <button type="submit">Check Safety</button>
        </form>
        <div id="result"></div>
    </div>

    <script>
        document.getElementById('pinForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const pin = document.getElementById('pinInput').value;
            const resultDiv = document.getElementById('result');
            
            const response = await fetch('/check', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ pin: pin })
            });
            
            const data = await response.json();
            resultDiv.style.display = 'block';
            resultDiv.textContent = data.message;
            
            if (data.safe) {
                resultDiv.className = 'success';
            } else {
                resultDiv.className = 'error';
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    pin = data.get('pin', '')
    is_safe, message = check_pin_safety(pin)
    return jsonify({'safe': is_safe, 'message': message})

if __name__ == '__main__':
    app.run(debug=True)