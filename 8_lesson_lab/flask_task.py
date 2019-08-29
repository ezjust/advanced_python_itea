from flask import Flask, request
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = "EZ"
    return f"""
    <html>
        <header>
        <title> Our page </title>
        </header>
        <body>
        <h1> Hello world, I'm {name} </h1>
        <h2> first one task at flask </h2>
        <a href=https://google.com> go to google </a>
        </body>
    </html>
    """


students = {'Vasya': 5, 'EZ': 5, 'Anna': 5, 'Misha': 4}


@app.route("/testid<int:id>")
def test_id(id):
    print(id)
    return 'haha'


@app.route("/form")
def form_insertion():
    return render_template("form_example.html")


@app.route("/new_route")
def new_route():
    title = 'Students list with marks'
    return render_template("index.html", students=students, title=title)


@app.route('/index', methods=["GET", "POST"])
def index_page():
    print(dict(request.get_json()))
    print(request.user_agent)
    return 'form approved'


if __name__ == "__main__":
    app.run(debug=True)

