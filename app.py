import re
from datetime import datetime


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home(): return render_template("home.html")

@app.route("/about")
def about(): return render_template("about.html")

@app.route("/contact")
def contact(): return render_template("contact.html")

@app.route("/hello")
@app.route("/hello/<name>") # The identifier inside < and > in the route defines a variable that is passed to the function and can be used in your code.
def hello_there(name = "Matteo"): return render_template( "hello_there.html", name=name, date=datetime.now() )   

@app.route("/api/data") 
def get_data():
    return app.send_static_file("data.json")
