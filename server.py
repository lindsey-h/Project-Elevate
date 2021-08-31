
from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
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


@app.route('/event-data')
def send_event_data():

    events = crud.get_all_events()
    # users = crud.get_users_by_event(event_id)

    all_events = []

    for event in events:
        users = crud.get_users_by_event(event.event_id)
        e = event.serialize()
        print("*"*20)
        print(e)
        print(users)
        e["users"] = [user.serialize() for user in users]
        all_events.append(e)
        #all_events[event[]] = [user.serialize() for user in users]

    return jsonify(all_events)

    # return jsonify([event.serialize() for event in events])


# @app.route('/users-by-event')
# def get_users_by_event():

#     event_id = int(request.args.get("index"))

#     print("*"*20)
#     print(f"eventid: {event_id}")
#     print("*"*20)

#     users = crud.get_users_by_event(event_id)
#     # print(f"users: {users}")
    
#     return jsonify([user.serialize() for user in users])


# @app.route('/eventsusers')
# def get_item_by_index():
#     items = ['apple', 'berry', 'cherry']
#     idx = int(request.args.get('index', 0))

#     return items[idx]


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