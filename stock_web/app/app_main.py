from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from home import home_page_process


app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/')
def home_page():
    return home_page_process()

@app.route('/data')
def data_process():
    return render_template("data.html")

@app.route('/test')
def test_process():
    return "dsfadsfasdf"


if __name__ == '__main__':
    app.run()