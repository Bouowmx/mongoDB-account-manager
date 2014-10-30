from flask import Flask, render_template, request
import hashlib
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/login/")
def login():
	
	username = request.form.get("username")
	password = request.form.get("password")
	return render_template("login.html")

@app.route("/register/", methods=["GET", "POST"])
def register():
	username = request.form.get("username")
	password = request.form.get("password")
	password_confirm = request.form.get("password_confirm")
	if ((username is None) and (password is None) and (password_confirm is None)):
		return render_template("register.html", password_confirm = True)
	if (password != password_confirm):
		return render_template("register.html", password_confirm = False, username = username)
	accounts = MongoClient()["accounts"]["accounts"]
	accounts.insert({username: username, password: hashlib.sha512(password)})
	return "<html><head><title>Registration successful</title></head><body><h2>Registration successful.</h2></body></html>"

if (__name__ == "__main__"):
	app.run(debug = True)

