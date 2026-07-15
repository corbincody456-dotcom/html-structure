from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def billing_tool():
    if request.method == 'POST':
        # Get data from the HTML form
        item_name = request.form['item_name']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])
        
        # Calculations
        subtotal = price * quantity
        tax = subtotal * 0.12  # 12% standard tax
        total = subtotal + tax
        
        # Send results back to the web page
        return render_template('index.html', 
                               item_name=item_name, 
                               price=price, 
                               quantity=quantity, 
                               subtotal=subtotal, 
                               tax=tax, 
                               total=total)
                               
    return render_template('index.html', subtotal=None)

if __name__ == '__main__':
    app.run(debug=True)