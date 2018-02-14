from flask import Flask, render_template, url_for, redirect, request, session
from app import app, db
from app.models import User
from app.forms import RegisterForm

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
	form = RegisterForm(request.form)
	if request.method == "POST" and form.validate_on_submit():
		username = request.form["username"]
		password = request.form["password"]
		masukan = User(username=username, password=password)
		db.session.add(masukan)
		db.session.commit()
		return redirect(url_for('success'))
	return render_template("index.html", form=form, title="Register")

@app.route("/success")
def success():
	return render_template("success.html", title="Success")
	
	