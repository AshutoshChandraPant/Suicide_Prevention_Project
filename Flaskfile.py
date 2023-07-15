import Flask from flask

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("portfolio.html")

@app.rout("/blog")

def blog():
    return render_template("blog.html")


if __name__ == "__main__":
    app.run(debug=True)