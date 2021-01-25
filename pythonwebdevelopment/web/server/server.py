from flask import Flask,render_template
app = Flask(__name__)
print(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/<string:page_name>')
def index(page_name=None):
    return render_template(page_name)
