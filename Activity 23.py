from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    input_text = ""
    
    if request.method == "POST":
        input_text = request.form.get("text_to_check")
        if input_text:
            # Check if all characters are alphabetic
            is_alpha = input_text.isalpha()
            if is_alpha:
                result = f'"{input_text}" contains ONLY alphabets!'
            else:
                result = f'"{input_text}" contains numbers, spaces, or symbols.'
        else:
            result = "Please enter some text."
            
    return render_template("index.html", result=result, input_text=input_text)

if __name__ == "__main__":
    app.run(debug=True)
