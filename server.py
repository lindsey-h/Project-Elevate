
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

    events_and_users = []

    for event in events:
        users = crud.get_users_by_event(event.event_id)
        e = event.serialize()
        e["users"] = [user.serialize() for user in users]
        events_and_users.append(e)

    return jsonify(events_and_users)


@app.route('/add-user-to-event', methods=['POST'])
def add_user_to_event():

    event_id = request.form.get("event-id")
    print("*"*20)
    print(f"event id: {event_id}")
    print("*"*20)
    # send a boolean 
    # hard-coded user id for now
    # remove this when retrieving id from session 
    crud.add_user_to_event(1, event_id)

    # flash('You are added to an event')
    return "PBJ"


@app.route('/remove-user-from-event', methods=['POST'])
def remove_user_from_event():

    event_id = request.form.get("event-id")
    print("*"*20)
    print(f"event id: {event_id}")
    print("*"*20)
    # send a boolean 
    # hard-coded user id for now
    # remove this when retrieving id from session 
    crud.remove_user_from_event(1, event_id)

    # flash('You are added to an event')
    return "PBJ"



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