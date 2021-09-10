"""Seed database with set of test data"""

import os
import json
from random import choice, randint 
from datetime import datetime 
import crud, model, server

# remove #
os.system('dropdb #elevate')
os.system('createdb #elevate')

model.connect_to_db(server.app)
model.db.create_all()


##### Create Users #####

# for line in txt file
line_list = string split at | 
fname, lname, email, password = line 
# for line in txt file
# fname, lname, email, password = line 
# crud.create_user(fname, lname, email, password)

Pam | Beasley | pbandj@dunder.com | beets
Jim | Halpert | jimhalps@dunder.com | beets
Dwight | Schrutte | dwight@dunder.com | beets
Michael | Scoott | worldsbestboss@dunder.com | beets
Toby | Flenderson | tobysad@dunder.com | beets

#crud get all users


# ---------------- Create Events ----------------- # 

def date_to_object(date_string):

    # String formate is 2021-09-09 18:00
    datetime_object = datetime.strptime('date_string', '%Y-%m-%d %H:%M')

events_file = open('events.txt')

author_id = model.User.query.filter_by(fname="Pam").first()
author_id_2 = model.User.query.filter_by(fname="Jim").first()

for line in events_file:
    
    line = line.rstrip()
    title, description, start_time, end_time = line.split(" | ")
    
    create_event(title, description, date_to_object(start_time), date_to_object(end_time), author_id)

create_event("Go for a walk", "Presidio", date_to_object("2021-08-22 15:00"), date_to_object("2021-08-22 17:00"), author_id_2)
create_event("Go for a walk", "Presidio", date_to_object("2021-08-23 15:00"), date_to_object("2021-08-23 17:00"), author_id_2)
create_event("Go for a walk", "Presidio", date_to_object("2021-08-24 15:00"), date_to_object("2021-08-24 17:00"), author_id_2)


##### Link Users with Events #####

# list = Query all users
# list = Query all events
# For every user add rand(1-3) events 
# 
add_user_to_event(1, 1, True)





