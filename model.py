"""Models for elevate app"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    """A user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    # account_owner = db.Column(db.Boolean, nullable=False)

    events = db.relationship("Event",  # The orm object we are relating to
                           secondary="users_events",  # The association table
                           backref="users")

    message = db.relationship("Message", uselist=False)

    # Needed for Flask Log In 
    def get_id(self):
        try:
            return self.user_id
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')


    def serialize(self):
        
        return { "user_id": self.user_id,
                    "fname": self.fname,
                    "lname": self.lname
                }

    def __repr__(self):
        return f"<User user_id={self.user_id} fname= {self.fname} lname={self.lname} email={self.email}>"


class Event(db.Model):
    """An event to display on a calendar"""

    __tablename__ = "events"

    event_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    title = db.Column(db.String, nullable=False)                    
    description = db.Column(db.Text)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    is_available = db.Column(db.Boolean, default=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)


    def convert_time(self, time):

        time = time.strftime("%I:%S %p")

        if time[0] == "0":
            time = time[1:]

        return time


    def serialize(self):

        start = self.convert_time(self.start_time)
        end = self.convert_time(self.end_time)
        
        # might need to change date format without time? check if it breaks calendar creation in js
        return { "id": self.event_id,
                 "name": self.title,
                 "date": self.start_time,
                 "type": "event",
                 "description": self.description,
                 "start_time": start,
                 "end_time": end,
                 "is_available": self.is_available
                }

    def __repr__(self):
        return f"<Event event_id={self.event_id} title={self.title} description={self.description}>"


class Photo(db.Model):
    """An inspiring photo of a cute animal"""

    __tablename__ = "photos"

    photo_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    url = db.Column(db.String, unique=True, nullable=False)
    animal_type = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Photo photo_id={self.photo_id} url={self.url} animal_type={self.animal_type}>"


class Quote(db.Model):
    """An inspiring quote"""

    __tablename__ = "quotes"

    quote_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    text = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Quote quote_id={self.quote_id} text={self.text}>"


class Post(db.Model):
    """Text posts for wall page"""

    __tablename__ = "posts"

    post_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)   
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    text = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    user = db.relationship("User", backref="posts")

    def __repr__(self):
        return f"<Post post_id={self.post_id} text={self.text}>"


class Contact(db.Model):
    """Contact information about a person"""

    __tablename__ = "contacts"

    contact_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)  
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False) 
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    email = db.Column(db.String,  unique=True, nullable=False)
    phone_number = db.Column(db.String,  unique=True, nullable=False)

    user = db.relationship("User", backref="contacts")

    def __repr__(self):
        return f"<Contact contact_id={self.contact_id} fname={self.fname} lname={self.lname}>"


class Message(db.Model):
    """A pre-written message used to alert contacts. One message per User instance."""

    __tablename__ = "messages"

    message_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)  
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    message = db.Column(db.String)

    def __repr__(self):
        return f"<Message message_id={self.message_id} message={self.message}>"




# ------------- Association Tables ---------------


class UserEvent(db.Model):
    """Association between User and Event"""

    __tablename__ = "users_events"

    user_event_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.ForeignKey("users.user_id"))
    event_id = db.Column(db.ForeignKey("events.event_id"))


# ------------- Connect to DB ---------------


def connect_to_db(flask_app, db_uri="postgresql:///elevate", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)