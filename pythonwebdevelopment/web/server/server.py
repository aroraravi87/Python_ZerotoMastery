from flask import Flask,render_template
app = Flask(__name__)
print(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/<username>')
def index(username=None):
    if username=="home":
        return render_template("index.html")
    elif username == "about":
        return render_template("about.html")
    elif username == "news":
        return render_template("news.html")

# @app.route('/about')
# def about():
#      return render_template("about.html")


# @app.route('/news')
# def news():
#     return render_template("news.html")