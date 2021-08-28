
from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import model #take this out when you set up CRUD
import crud
from jinja2 import StrictUndefined
import requests
import calendar 
from calendar import HTMLCalendar
from datetime import datetime

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def show_home():

    events = model.Event.query.all()
    # res = requests.get("https://zenquotes.io/api/quotes/")
    # quotes = res.json()

    cal = HTMLCalendar().formatmonth(2021, 8)

    return render_template('home.html', events=events, cal=cal) 
    # , quotes=quotes)



@app.route('/add-event')
def show_add_event():

    return render_template('add-event.html')


@app.route('/add-event', methods=["POST"])
def add_event():

    title = request.form.get('title')
    date = request.form.get('date')
    description = request.form.get('description')
    start_time = request.form.get('start-time')
    end_time = request.form.get('end-time')

    start_datetime = date + " " + start_time #'2020-12-12 18:06'
    datetime_object = datetime.strptime(start_datetime, '%Y-%m-%d %H:%M')
    crud.create_event(title, datetime_object, description, 60)

    print("*"*20)
    print(title, date, description, start_time, end_time)
    print("*"*20)

    return redirect("/")


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)