from flask import Flask, render_template, request, redirect
import pyodbc
from pyodbctest import MSDBconnection

app = Flask(__name__)


nwind = MSDBconnection()
results = nwind.sql_query("SELECT * FROM books")

columns=["ID","Title","Author","Pages","Language","Date Published"]
posts = [
    {
        'author': 'Ashraf Mohamud ',
        'title': 'HTML & CSS engineer, design, SCRUM board',
        'content': 'Responsable for CSS layout, create logo for company and SCRUM board management',
        'date_posted': '18 June, 2020'
    },
    {
        'author': 'Hussain Ali Khan',
        'title': 'Database management, HTML & CSS engineer: list e-books page',
        'content': 'Responsible for creating database and creating list of e-books page',
        'date_posted': '21 June, 2020'
    },
    {
        'author': 'Fahad Khisaf',
        'title': 'Database tester, HTML & CSS engineer: Homepage',
        'content': 'Responsible for testing database and creating homepage',
        'date_posted': '21 June, 2020'
    },
    {
        'author': 'Stefan Okolo',
        'title': 'Documentation, HTML & CSS engineer: add e-books page',
        'content': 'Responsible for documentation and creating add e-books page',
        'date_posted': '21 June, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    nwind = MSDBconnection()
    results = nwind.sql_query("SELECT * FROM books")
    return render_template("homepage.html",posts=posts,list = results)

@app.route('/about')
def about():

    return render_template('about.html', title = 'About')

@app.route('/book-list')
def bookList():
    nwind = MSDBconnection()
    results = nwind.sql_query("SELECT * FROM books")
    return render_template("book-list.html", list=results,columns=columns)

@app.route('/add-book')
def add_book():
    return render_template("add-book.html")


@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/book-added', methods = ['POST'])
def book_added():
    nwind = MSDBconnection()
    book_title = request.form['book-title']
    first_name = request.form['first-name']
    last_name = request.form['last-name']
    pub_year = request.form['pub-year']
    author = first_name + " " + last_name
    nwind.sql_query(f"""INSERT INTO books
                        (title, author, published_date)
                        VALUES
                        ('{book_title}', '{author}', '{pub_year}') """)
    return redirect('/')


if( __name__ == '__main__'):
    app.run(host='127.0.0.1')