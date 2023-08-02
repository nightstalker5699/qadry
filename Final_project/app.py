import os
from cs50 import SQL
from flask import Flask, redirect, request, render_template, session
from flask_session import Session
from flask_wtf import FlaskForm
from wtforms import StringField,DateField,PasswordField,SubmitField,SelectField,RadioField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
from flask_wtf.file import FileRequired,FileField,FileAllowed
from helpers import apology, login_required
from werkzeug.security import check_password_hash, generate_password_hash
app = Flask("__name__")

class form_web(FlaskForm):
    pic = FileField("picture of the dog",validators=[FileRequired(),FileAllowed(["jpg","png"],"images only"),])
    birthdays = DateField(label="birthday",format="%Y-%m-%d")
    name = StringField(label = "username",validators=[DataRequired()])
    password = PasswordField(label ="password", validators=[DataRequired()])
    confirm = PasswordField(label = "password again (for confirmation)",validators=[DataRequired()])
    submit = SubmitField("register")
    img = FileField(label = "picture of the dog", validators=[FileRequired(),FileAllowed(['png','jpg'],"Images only ")])
    type = SelectField("dog type",choices=[("golden Retriever","golden Retriever"),("Retriever","Retriever"),("French Bulldog","French Bulldog"),("Bulldog","Bulldog"),("husky","husky"),("Poodle","Poodle"),("Beagle","Beagle"),("Rottweiler","Rottweiler"),("German Shorthaired Pointer","German Shorthaired Pointer"),("Dachshund","Dachshund"),("Pembroke Welsh Corgi","Pembroke Welsh Corgi"),("Australian Shepherd","Australian Shepherd"),("Yorkshire Terrier","Yorkshire Terrier"),("boxer","Boxer")],validate_choice=True)
    gender = RadioField("dog gender",choices=[("male","Male"),("female","Female")],validate_choice=True)
@app.after_request
def after_request(response):
    response.headers["Cache-Control"]="no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "bomb5699"
Session(app)
db = SQL("sqlite:///adopt.db")

@app.route("/")
@login_required
def index():
    animal = db.execute("SELECT * FROM animal")
    return render_template("home.html",animal = animal)

@app.route("/login",methods = ["POST", "GET"])
def login():
    form = form_web()
    if request.method == "POST":
        data = db.execute("SELECT * FROM users")
        if form.validate_on_submit:
           if not form.name.data or not form.password.data:
               return apology("put username and password please",400)
           for i in data:
              if form.name.data ==i["username"] and check_password_hash(i["password_hash"],form.password.data):
                  session["user_id"] = i["person_id"]
                  return redirect("/")
        return apology("wrong username or password",400)         
    else:
        return render_template("login.html", form=form )

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/register",methods = ["POST","GET"])
def register():
    form = form_web()
    if request.method == "POST":
        if form.validate_on_submit:
            if not form.password.data == form.confirm.data:
                return apology("wrong confirmation",400)
            name_check = db.execute("SELECT * FROM users")
            for i in name_check:
                if i["username"]==form.name.data:
                    return apology("username is already taken",400)
            db.execute("INSERT INTO users (username,password_hash) VALUES (?, ?)",form.name.data , generate_password_hash(form.password.data,method='pbkdf2:sha256', salt_length=8))
            user_id = db.execute("SELECT * FROM users WHERE username = ?",form.name.data)
            session["user_id"] = user_id[0]["person_id"]
            return redirect("/")
        else:
            return apology("make sure to put the data",400)
    else :
        return render_template("register.html",form = form)


@app.route("/donate", methods = ["POST", "GET"] )
@login_required
def donate():
    form = form_web()
    if request.method =="POST":
        if form.validate_on_submit or request.form.get("birthday")or request.form.get("email") or request.form.get("address"):
            f = form.pic.data
            filename = secure_filename(f.filename)
            db.execute("INSERT INTO animal (name, type, gender, birthday,image,email,address) VALUES(?, ?, ?, ?, ?,?,?)",form.name.data ,form.type.data , form.gender.data , request.form.get("birthday"),filename,request.form.get("email"),request.form.get("address"))
            f.save(os.path.join(f"static/images/", filename))
            return redirect("/")
        else: return apology("put data",400)
    else:
        return render_template("donate.html",form=form)

@app.route("/Adopt",methods = ["POST", "GET"])
@login_required
def adopt():
    animal_id = request.args.get("id")
    name1=db.execute("SELECT * FROM animal WHERE animal_id =?",animal_id)
    filename = name1[0]["image"]
    os.remove(os.path.join("static/images/", filename))
    db.execute("DELETE FROM animal WHERE animal_id =?",animal_id)
    return render_template("adopt.html",name=name1)

@app.route("/change",methods = ["POST", "GET"])
def change():
    if request.method == "POST":
        base = db.execute("SELECT * FROM users WHERE person_id =?",session["user_id"])
        old = request.form.get("old")
        new = request.form.get("new")
        confirm = request.form.get("confirm")
        if not old or not new or not new == confirm:
            return apology("retry",4000)
        if check_password_hash(base[0]["password_hash"],old):
            db.execute("UPDATE users SET password_hash = ? WHERE person_id = ?", generate_password_hash(new,method='pbkdf2:sha256', salt_length=8),session["user_id"])
            return redirect("/")
        
    else :
        return render_template("change.html")