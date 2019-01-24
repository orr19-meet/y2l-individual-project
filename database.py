from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_event(nameOfEvent,date,email, discription, nameOfCreater, phoneNumber, numberOfVolunteers, requirements, pic):
    print("You added an event!")
    event = Event(nameOfEvent=nameOfEvent,date=date, email=email, discription=discription, nameOfCreater=nameOfCreater,phoneNumber=phoneNumber,numberOfVolunteers=numberOfVolunteers,requirements=requirements, pic=pic)
    session.add(event)
    session.commit()

def get_all_events():
    events = session.query(Event).all()
    return events

def get_all_events_by_name(nameOfEvent):
	return session.query(Event).filter_by(nameOfEvent=nameOfEvent).all()

def get_all_events_by_id(idOfEvent):
	return session.query(Event).filter_by(id = idOfEvent).first()


def volunteer(nameOfEvent):
	event=session.query(Event).filter_by(nameOfEvent=nameOfEvent).first()
	event.numberOfVolunteers=event.numberOfVolunteers-1
	session.commit()



print(get_all_events())
