"""Models for elevate app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user"""

    __tablename__ == "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    # account_owner = db.Column(db.Boolean, nullable=False)


class CalendarEvent(db.Model):
    """An event"""

    __tablename__ == "events"

    event_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    title = db.Column(db.String, nullable=False)                    
    date = db.Column(db.DateTime, nullable=False)
    description = lname = db.Column(db.Text)
    duration_in_minutes = db.Column(db.Integer)
    is_available = db.Column(db.Boolean, default=True, nullable=False)


class Photo(db.Model):
    """An inspiring photo of a cute animal"""

    __tablename__ == "photos"

    photo_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    url = db.Column(db.String, unique=True, nullable=False)
    animal_type = db.Column(db.String, nullable=False)


class Quote(db.Model):
    """An inspiring quote"""

    __tablename__ == "quotes"

    quote_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    quote_text = db.Column(db.String, unique=True, nullable=False)


class Post(db.Model):
    """Text posts for wall page"""

    __tablename__ == "posts"

    post_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)   
    post_text = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)


class Contact(db.Model):
    """Contact information about a person"""

    __tablename__ == "contacts"

    contact_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)   
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    email = db.Column(db.String,  unique=True, nullable=False)
    phone_number = db.Column(db.String,  unique=True, nullable=False)