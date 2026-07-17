import os
import sys
from flask import Flask, render_template_string

app = Flask(__name__)

# The HTML for the website
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Shutdown Portal</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 100px; }
        .btn { padding: 20px 40px; font-size: 24px; color: white; background-color: red; 
               border: none; border-radius: 10px; cursor: pointer; }
        .btn:hover { background-color: darkred; }
    </style>
</head>
<body>
    <h1>Computer Control Panel</h1>
    <form action="/shut" method="POST">
        <button class="btn" type="submit">SHUT DOWN COMPUTER</button>
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/shut', methods=['POST'])
def shutdown():
    # This shuts down a Windows PC
    # For Mac/Linux, change to: os.system("sudo shutdown now")
    os.system("shutdown /s /t 1") 
    return "<h1>Computer is shutting down...</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)