
from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from flask_login import LoginManager, login_required, login_user, logout_user, current_user, UserMixin
from model import connect_to_db
import model #take this out when you set up CRUD
import crud
from jinja2 import StrictUndefined
import requests
import calendar 
from calendar import HTMLCalendar
from datetime import datetime
import sms
import os

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/login"

@login_manager.user_loader
def load_user(user_id):
    return crud.get_user_by_id(user_id)

@app.route('/')
@login_required
def show_home():

    events = model.Event.query.all()
    # res = requests.get("https://zenquotes.io/api/quotes/")
    # quotes = res.json()
    cal = HTMLCalendar().formatmonth(2021, 8)


    return render_template('home.html', events=events, cal=cal) 
    # , quotes=quotes)


@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'GET':
        return render_template('login.html')

    # get email and password from form
    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email)

    if user:
        if user.password == password:
            login_user(user)
            return redirect('/')
        else:
            flash("Incorrect username or password. Please try again.")
            return redirect('/login')
    else:
        flash("Incorrect username or password. Please try again.")
        return redirect('/login')



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/login")


@app.route('/event-data')
def send_event_data():

    events = crud.get_all_events_by_author(current_user.user_id)
    print("*-"*20)
    print(events)
    print("*-"*20)

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
    print(current_user.user_id)
    print("*"*20)
    # send a boolean 
    # hard-coded user id for now
    # remove this when retrieving id from session 
    print(current_user.user_id)
    crud.add_user_to_event(current_user.user_id, event_id)

    # flash('You are added to an event')
    return f"{current_user.fname} {current_user.lname}"


@app.route('/remove-user-from-event', methods=['POST'])
def remove_user_from_event():

    event_id = request.form.get("event-id")
    print("*"*20)
    print(f"event id: {event_id}")
    print("*"*20)


    crud.remove_user_from_event(current_user.user_id, event_id)

    # flash('You are added to an event')
    return f"{current_user.fname} {current_user.lname}"


@app.route('/is-user-on-event', methods=['POST'])
def is_user_on_event():

    event_id = int(request.form.get("event-id"))
    print("&"*20)
    print(f'js sent event id: {event_id}')
    print("&"*20)

    # also check that they are not the author

    for event in current_user.events:
        print(f'In the loop server id: {event.event_id}')
        if event_id == event.event_id:
            return "true"

    return "false"


@app.route("/sms", methods=['POST', 'GET'])
def send_sms():

    # Get these from the server for the current user
    receiver = "4158575066"
    sender = "16824631868"
    message = "Hi hello hay is for horses"

    sms.send_sms(receiver, sender, message)
    flash("Your message has been sent to your contacts.")

    return redirect('/')


# @app.route('/users-by-event')
# def get_users_by_event():

#     event_id = int(request.args.get("index"))

#     print("*"*20)
#     print(f"eventid: {event_id}")
#     print("*"*20)

#     users = crud.get_users_by_event(event_id)
#     # print(f"users: {users}")
    
#     return jsonify([user.serialize() for user in users])



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

    start_datetime = date + " " + start_time #'2020-12-12 18:00'
    end_datetime = date + " " + end_time #'2020-12-12 19:00'
    start_datetime_object = datetime.strptime(start_datetime, '%Y-%m-%d %H:%M')
    end_datetime_object = datetime.strptime(end_datetime, '%Y-%m-%d %H:%M')
    
    crud.create_event(title, description, start_datetime_object, end_datetime_object, current_user.user_id)

    return redirect("/")


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)