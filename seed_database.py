"""Seed database with set of test data"""

import os
import json
from random import choice, randint, choices
from datetime import datetime 
import crud, model, server

os.system('dropdb elevate')
os.system('createdb elevate')

model.connect_to_db(server.app)
model.db.create_all()


# ---------------- Create Users ----------------- # 

users_file = open('users.txt')

for line in users_file:
    
    line = line.rstrip()
    fname, lname, email, password = line.split(" | ")
    print("-*"*20)
    print(f"{fname} {lname} {email} {password}")
    print("-*"*20)
    
    crud.create_user(fname, lname, email, password)



# ---------------- Create Events ----------------- # 

def date_to_object(date_string):

    # String formate is 2021-09-09 18:00
    datetime_object = datetime.strptime(date_string, '%Y-%m-%d %H:%M')
    return datetime_object

events_file = open('events.txt')

author_id = model.User.query.filter_by(fname="Pam").first().user_id
author_id_2 = model.User.query.filter_by(fname="Jim").first().user_id

for line in events_file:
    
    line = line.rstrip()
    title, description, start_time, end_time = line.split(" | ")
    print("-*"*20)
    print(f"{title} {description} {start_time} {end_time}")
    print("-*"*20)
    
    event = crud.create_event(title, description, date_to_object(start_time), date_to_object(end_time), author_id)
    # ?? crud.add_user_to_event(author_id, event.event_id)

crud.create_event("Go for a walk", "Presidio", date_to_object("2021-09-22 15:00"), date_to_object("2021-09-22 17:00"), author_id_2)
crud.create_event("Go for a walk", "Presidio", date_to_object("2021-09-23 15:00"), date_to_object("2021-09-23 17:00"), author_id_2)
crud.create_event("Go for a walk", "Presidio", date_to_object("2021-09-24 15:00"), date_to_object("2021-09-24 17:00"), author_id_2)



# ---------------- Link Events and Users ----------------- # 

# list = Query all users
# list = Query all events
# For every user add rand(1-3) events 
# Query if user != author 
users = model.User.query.all()
events = model.Event.query.all()

for user in users:
    for event in choices(events, k = randint(1,4)):
        if user.user_id != event.author_id:
            crud.add_user_to_event(user.user_id, event.event_id)






