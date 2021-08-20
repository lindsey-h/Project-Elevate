
from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import model #take this out when you set up CRUD
import crud
from jinja2 import StrictUndefined
import requests

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def show_home():

    events = model.Event.query.all()
    # res = requests.get("https://zenquotes.io/api/quotes/")
    # quotes = res.json()

    return render_template('home.html', events=events) 
    # , quotes=quotes)


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)