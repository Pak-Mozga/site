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
    app.run(debug=True)