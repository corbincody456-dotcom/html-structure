from flask import Flask, redirect, render_template_string, request, url_for

app = Flask(__name__)

# Menu items and prices in Philippine Pesos (PHP)
menu = {
    "Banana Cue": 15.00,
    "Puto Cheese": 10.00,
    "Juice Drink": 12.00,
    "Sandwich": 20.00,
}

# HTML template with embedded CSS styling
html_template = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>School Snack Counter</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f9; margin: 0; padding: 20px; color: #333; }
        .container { max-width: 600px; margin: auto; background: white; padding: 25px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        h1, h2 { color: #2c3e50; text-align: center; }
        .menu-item { display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid #eee; }
        input[type="number"] { width: 60px; padding: 5px; }
        button { display: block; width: 100%; background: #27ae60; color: white; border: none; padding: 12px; font-size: 16px; border-radius: 4px; cursor: pointer; margin-top: 20px; }
        button:hover { background: #219653; }
        .total-box { margin-top: 25px; padding: 15px; background: #e8f8f5; border-radius: 5px; text-align: center; font-size: 18px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>School Snack Counter</h1>
        <form method="POST">
            <h2>Menu</h2>
            {% for item, price in menu.items() %}
            <div class="menu-item">
                <span><strong>{{ item }}</strong> - ₱{{ "%.2f"|format(price) }}</span>
                <input type="number" name="{{ item }}" value="0" min="0">
            </div>
            {% endfor %}
            <button type="submit">Calculate Total</button>
        </form>

        {% if total is not none %}
        <div class="total-box">
            <strong>Total Amount Due: ₱{{ "%.2f"|format(total) }}</strong>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
  total = None
  if request.method == "POST":
    total = 0.0
    for item, price in menu.items():
      qty_str = request.form.get(item, "0")
      qty = int(qty_str) if qty_str.isdigit() else 0
      total += price * qty
  return render_template_string(html_template, menu=menu, total=total)


if __name__ == "__main__":
  app.run(debug=True)