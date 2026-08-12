import os
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return '''
    <!doctype html>
    title>Student Record Cleaner</title>
    <h1>Upload Student CSV File</h1>
    <form action="/clean" method="post" enctype="multipart/form-data">
        <input type="file" name="file" accept=".csv">
        <input type="submit" value="Clean Records">
    </form>
    '''

@app.route('/clean', methods=['POST'])
def clean_data():
    file = request.files['file']
    if file and file.filename.endswith('.csv'):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        
        # Read and clean using pandas
        df = pd.read_csv(filepath)
        df.drop_duplicates(inplace=True)
        df.dropna(how='all', inplace=True)
        
        # Strip string whitespace across object columns
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].str.strip()
            
        cleaned_path = os.path.join(UPLOAD_FOLDER, 'cleaned_' + file.filename)
        df.to_csv(cleaned_path, index=False)
        
        return f"<h3>Cleaned Data Preview:</h3>" + df.to_html(classes='data', header="true")
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)