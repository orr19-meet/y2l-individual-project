from flask import Flask,render_template,request, redirect,url_for
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
    return redirect(url_for("events"))

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/events')
def events():
	events=get_all_events()
	return render_template("events.html",events=events)

@app.route('/viewevent/<int:event_id>')
def viewevent(event_id):
	event=get_all_events_by_id(event_id)
	return render_template("viewevent.html",event=event)

@app.route('/volunform/<int:event_id>', methods=["POST"])
def volunform(event_id):
	event = get_all_events_by_id(event_id)
	volunteer(event.nameOfEvent)
	return redirect(url_for("viewevent",event_id=event_id))
if __name__ == '__main__':
    app.run(debug=True)

