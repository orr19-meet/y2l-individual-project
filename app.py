from flask import Flask,render_template,request
from database import *
app = Flask(__name__)

@app.route('/add_event',methods=["POST","GET"])
def addevent():
	if request.method=="POST":
		nameOfEvent = request.form['nameOfEvent']
		date = request.form['date']
		discription=request.form['discription']
		email=request.form['email']
		nameOfCreater=request.form['nameOfCreater']
		requirements=request.form['requirements']
		phoneNumber=request.form['phoneNumber']
		numberOfVolunteers=request.form['numberOfVolunteers']
		pic=request.form['pic']
		add_event(nameOfEvent,date,email, discription, nameOfCreater, phoneNumber, numberOfVolunteers, requirements, pic)
		return render_template("addevent.html")


	else:
		return render_template("addevent.html")

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/events')
def events():
	events=get_all_events()
    return render_template("events.html",events=events)
if __name__ == '__main__':
    app.run(debug=True)

