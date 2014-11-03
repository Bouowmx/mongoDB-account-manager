from flask import Flask, render_template, request, session
import hashlib
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/login/", methods=["GET", "POST"])
def login():
	username = request.form.get("username")
	password = request.form.get("password")
        users = MongoClient("mongodb://Bouowmx:ReimuHakurei@ds047440.mongolab.com:47440/account-manager")["account-manager"]["users"]
        if users.find({"username": username, "password": password}).count() == 0:
                return render_template("login.html", login_failed = True)
        session["username"] = username
	return redirect(url_for("profile"))

@app.route("/register/", methods=["GET", "POST"])
def register():
	username = request.form.get("username")
	password = request.form.get("password")
        password_confirm = request.form.get("password_confirm")
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        age = request.form.get("age")
        email = request.form.get("email")
        phone = request.form.get("phone")
        address = request.form.get("address")
	if ((username is None) and (password is None) and (password_confirm is None)):
		return render_template("register.html", password_confirm = True)
	if (password != password_confirm):
		return render_template("register.html", password_confirm = False, username = username)
	accounts = MongoClient("cslab1-30", 1340)["users"]["users"]
	accounts.insert({username: username, password: hashlib.sha256(password).hexdigest()})
	return render_template("registersuccess.html", fname = fname, lname = lname);

@app.route("/about/")
def about():
        return render_template("about.html")

@app.route("/profile/")
def profile():
        pass

if (__name__ == "__main__"):
	app.run(debug = True, port = 9001)

app.secret_key = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
