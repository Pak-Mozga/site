import sqlite3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index() -> str:
    return render_template('starter-page.html')


@app.route('/about')
def about() -> str:
    return render_template('about.html')

@app.route('/contact')
def contact() -> str:
    return render_template('contact.html')

@app.route('/service')
def service() -> str:
    return  render_template('services.html')

def create_database():
    con = sqlite3.connect('website.db')
    cur = con.cursor()

    cur.execute("""
                CREATE TABLE IF NOT EXISTS services(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                txt TEXT NOT NULL,
                id_img NOT NULL)
                """)
    cur.execute("""
                CREATE TABLE IF NOT EXISTS doc(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                txt TEXT NOT NULL,
                id_img NOT NULL)
                """)

    con.commit()
    con.close()






# 
# @app.route('/')
# def index() -> str:
#     return render_template('starter-page.html')
# 
# 
# @app.route('/')
# def index() -> str:
#     return render_template('starter-page.html')



if __name__ == '__main__':
    create_database()
    app.run(debug=True)