from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :

class Event(Base):
	__tablename__ = 'events'
	id = Column(Integer, primary_key=True)
	nameOfEvent = Column(String)
	date=Column(String)
	email=Column(String)
	discription=Column(String)
	phoneNumber=Column(Integer)
	requirements=Column(String)
	nameOfCreater=Column(String)
	pic=Column(String)
	numberOfVolunteers=Column(Integer)


	# def __repr__(self):
	# 	return ("Donator id: {}\n"
	# 			"Name of event: {} \n"
	# 			"Date: {} \n "
	# 			"email: {} \n "
	# 			"discription: {} \n "
	# 			"phone number: {} \n "
	# 			"requirments: {} \n "
	# 			"nameOfCreater: {} \n "
	# 			"numberOfVolunteers: {} \n ").format(
	# 				self.id,
	# 				self.nameOfEvent,
	# 				self.date,
	# 				self.email,
	# 				self.discription,
	# 				self.phoneNumber,
	# 				self.requirments,
	# 				self.nameOfCreater
	# 				self.numberOfVolunteers)

