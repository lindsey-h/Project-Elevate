"""CRUD operations."""

from model import db, User, Event, Photo, Quote, Post, Contact, UserEvent, connect_to_db


def create_user(fname, lname, email, password):
    """Create and return a new user."""

    user = User(fname=fname, lname=lname, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def get_all_users():

    return User.query.all()


def add_user_to_event(user_id, event_id):
    """Creates association between User instance and Event instance"""

    user_event = UserEvent(user_id=user_id, event_id=event_id)

    db.session.add(user_event)
    db.session.commit()


def create_event(title, date, description, duration_in_minutes, is_available=True):
    """Create and return a new event with a User instance."""

    event = Event(title=title, date=date, 
                  description=description, 
                  duration_in_minutes=duration_in_minutes, 
                  is_available=is_available)

    db.session.add(event)
    db.session.commit()

    return event


def get_all_events():

    return Event.query.all()


def create_photo(url, animal_type):
    """Create and return a new photo."""

    photo = Photo(url=url, animal_type=animal_type)

    db.session.add(photo)
    db.session.commit()

    return photo


def get_all_photos():

    return Photo.query.all()


def create_quote(text, author):
    """Create and return a new quote."""

    quote = Quote(text=text, author=author)

    db.session.add(quote)
    db.session.commit()

    return quote


def get_all_quotes():

    return Quote.query.all()


def create_post(user_id, text, date):
    """Create and return a new post with a User instance."""

    post = Post(user_id=user_id, date=date)

    db.session.add(post)
    db.session.commit()

    return post


def get_all_posts():

    return Post.query.all()


def create_contact(user_id, fname, lname, email, phone_number):
    """Create and return a new contact with a User instance."""

    contact = Contact(user_id=user_id, fname=fname,
                      email=email, phone_number=phone_number)

    db.session.add(contact)
    db.session.commit()

    return contact


def get_all_contacts():

    return Contact.query.all()

# remove this after testing done 
if __name__ == "__main__":
    
    from server import app
    connect_to_db(app)