from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index() -> str:
    return render_template('starter-page.html')

if __name__ == '__main__':
    app.run(debug=True)