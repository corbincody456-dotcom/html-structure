import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DB_NAME = "library.db"

def init_db():
    """Creates the database and adds sample books if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            isbn TEXT UNIQUE NOT NULL,
            is_available INTEGER DEFAULT 1
        )
    ''')
    
    # Insert sample data if the table is empty
    cursor.execute("SELECT COUNT(*) FROM books")
    if cursor.fetchone()[0] == 0:
        sample_books = [
            ("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 1),
            ("To Kill a Mockingbird", "Harper Lee", "9780446310789", 1),
            ("1984", "George Orwell", "9780451524935", 0),
            ("The Hobbit", "J.R.R. Tolkien", "9780547928227", 1)
        ]
        cursor.executemany(
            "INSERT INTO books (title, author, isbn, is_available) VALUES (?, ?, ?, ?)", 
            sample_books
        )
        conn.commit()
    conn.close()

@app.route('/')
def home():
    """Displays all books in the library."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    all_books = cursor.fetchall()
    conn.close()
    return render_template('index.html', books=all_books)

@app.route('/search', methods=['GET'])
def search():
    """Filters books by title or author based on user query."""
    query = request.args.get('query', '').strip()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", 
        (f"%{query}%", f"%{query}%")
    )
    results = cursor.fetchall()
    conn.close()
    return render_template('search.html', books=results, query=query)

@app.route('/toggle/<int:book_id>', methods=['POST'])
def toggle_status(book_id):
    """Simulates checking a book out or returning it."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET is_available = 1 - is_available WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
    return redirect(request.referrer or url_for('home'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)