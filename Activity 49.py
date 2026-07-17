from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate_due():
    due_amount = 0.0
    if request.method == "POST":
        # Get numbers typed by the user
        balance = float(request.form.get("balance", 0))
        payment = float(request.form.get("payment", 0))
        
        # Calculate the total left to pay
        due_amount = balance - payment
        
    return render_template("index.html", due=due_amount)

if __name__ == "__main__":
    app.run(debug=True)