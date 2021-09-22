
from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify, abort)
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

    # res = requests.get("https://zenquotes.io/api/quotes/")
    # quotes = res.json()

    uid = current_user.user_id
    return redirect(f'/{uid}') 

@app.route('/<user_id>')
def user_logged_in_home(user_id):

    #if user_id not in database
    # abort(404)
    try: 
        user_id=int(user_id)
        if not crud.get_user_by_id(user_id):
            abort(404)
    except ValueError:
        abort(404)

    return render_template('home.html')


@app.route('/users/<user_id>')
def show_user_details(user_id):
    
    user = crud.get_user_by_id(user_id)

    return render_template('public_user.html', user=user)




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
            return redirect('/' + str(user.user_id))
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


@app.route('/event-data/<user_id>')
def send_event_data(user_id):

    events = crud.get_all_events_by_author(int(user_id))
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
    crud.add_user_to_event(current_user.user_id, event_id)

    return f"{current_user.fname} {current_user.lname}"


@app.route('/remove-user-from-event', methods=['POST'])
def remove_user_from_event():

    event_id = request.form.get("event-id")
    crud.remove_user_from_event(current_user.user_id, event_id)

    return f"{current_user.fname} {current_user.lname}"


@app.route('/is-user-on-event', methods=['POST'])
def is_user_on_event():

    event_id = int(request.form.get("event-id"))

    for event in current_user.events:
        print(f'In the loop server id: {event.event_id}')
        if event_id == event.event_id:
            return "true"

    return "false"


@app.route('/delete-event', methods=['POST', 'GET'])
def delete_event():

    event_id = int(request.form.get("event-id"))
    crud.delete_event(event_id)

    return redirect("/")


@app.route("/sms", methods=['POST', 'GET'])
def send_sms():

    # Get these from the server for the current user
    receiver = os.environ["RECIPIENT_PHONE"]
    sender = os.environ["SENDER_PHONE"]
    message = f"Hi, from the Elevate App. Your friend, {current_user.fname} {current_user.lname}, needs some company. Please sign up for a slot if you want to offer support. http://localhost:5000/users/2"

    sms.send_sms(receiver, sender, message)
    flash("Your message has been sent to your contacts.")

    return redirect("/")


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


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)