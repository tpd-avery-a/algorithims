from ast import If
from flask import Flask, redirect, render_template, request,session,flash
from flask_bcrypt import Bcrypt
from controllers.Query import Users, Shows
from datetime import date, datetime
import re


app = Flask(__name__)
bcrypt = Bcrypt(app)

t = datetime.now()
app.secret_key = str(t) + "Secret Key"

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

@app.route("/")
def index():
    """
    Populate Login/Reg
    """
    session["username"] = "test"
    return render_template("index.html")

@app.route("/logout")
def logout():
    session.clear()
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    """
    Show All shows
    """
    shows = Shows.get_shows()
    return render_template("dashboard.html", shows = shows)

@app.route("/new")
def new():
    """
    Populate Form to add new show
    """
    return render_template("new.html")

@app.route("/show/<int:id>")
def show(id):
    """
        Grab all information FROM shows where ID = id
    """
    show = Shows.get_show(id)
    return render_template("show.html", show = show)

@app.route("/edit/<int:id>")
def edit(id):
    """
        Grab and Display show information
    """
    show = Shows.get_show(id)
    return render_template("edit.html", show = show)

@app.route("/login_process", methods=["POST"])
def login_process():
    salt = "okvensokvnokrenc"
    """
        Grab information where email = email
            If pword == bcrypt.requestform
                session["username"] = request.form["uname"]
                session["user_id] = 
                return redirect("/dashboard")
            else:
                flash("")
                return redirect("/")
    """
    email = request.form["email"]
    user_in_db =""
    user_in_db = Users.get_user(email)
    if user_in_db == "":
        flash("Not in DB")
        return redirect("/")
    #session["username"] = user["email"]
    pw = request.form["pword"]
    try:
        if bcrypt.check_password_hash(user_in_db.pword, pw):
                session["username"] = user_in_db.fname +" " + user_in_db.lname
                return redirect("/dashboard")
        else:
            flash("Invalid Email/Password")
            return redirect("/")
    except:
            flash("Invalid Email/Password")
            return redirect("/")

    
@app.route("/register_process",methods=["POST"])
def register_process():
    
  
    """
        Check if email Exists
            Check Email Regex
                Check if pwords match
                    bcrypt pword
                    INSERT INTO DB

    """
    pw = request.form["pword"]
    pw2 = request.form["p2"]
    print(pw)
    print(pw2)
    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
        "e2" : request.form["e2"],
        "pword" : pw,
        "p2" : pw2,
    }
    if data["pword"] == "":
        flash("Passwords cant be empty")
        return redirect("/")
    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
        "pword" : bcrypt.generate_password_hash(data["pword"]),
        "e2" : request.form["e2"]
    }
 
    if re.match(regex, data['email']):
        if data['email'] == data["e2"]:
            if len(pw) >= 4 :
                if pw == pw2:
                    if pw == "":
                        flash("Pword cant be empty")
                        return redirect("/")
                    else:
                        Users.insert_user(data)
                        session["username"] = data["fname"] + " " + data["lname"] 
                        return redirect("/dashboard")
                else:
                    flash("Passwords must match")
                    return redirect("/")
                    pass
            else:
                flash("Password must be greater than 3")
                return redirect("/")
                pass
        else:
            flash("Emails must match")
            return redirect("/")
            pass
    else:
        flash("Email must be formatted correctly")
        return redirect("/")



@app.route("/new_process", methods=["POST"])
def new_process():
    """
    insert insert shows %data
    """
    data = {
        "title" : request.form["title"],
        "network" : request.form["network"],
        "release_date" : request.form["release_date"],
        "description" : request.form["description"],
        "created_by" : session["username"]
    }
    if data["title"] == "":
        flash("Title cant be empy")
        return redirect("/dashboard")
    if data["network"] == "":
        flash("Netowrk cant be empy")
        return redirect("/dashboard")
    if data["release_date"] == "":
        flash("Release Date cant be empy")
        return redirect("/dashboard")
    if data["description"] == "":
        flash("Desription cant be empy")
        return redirect("/dashboard")
    else:
        Shows.insert_shows(data)
        return redirect("/dashboard")

@app.route("/show_process/", methods=["POST"])
def show_process():
    
    return redirect("/dashboard")

@app.route("/edit_process", methods=["POST"])
def edit_process():
    data = {
        "title" : request.form["title"],
        "network" : request.form["network"],
        "release_date" : request.form["release_date"],
        "description" : request.form["description"],
        "created_by" : session["username"]
    }
    if data["title"] == "":
        flash("Title cant be empy")
        return redirect("/dashboard")
    if data["network"] == "":
        flash("Netowrk cant be empy")
        return redirect("/dashboard")
    if data["release_date"] == "":
        flash("Release Date cant be empy")
        return redirect("/dashboard")
    if data["description"] == "":
        flash("Desription cant be empy")
        return redirect("/dashboard")
    else:
        Shows.insert_shows(data)
        return redirect("/dashboard")
                    


@app.route("/delete/<int:id>")
def delete(id):
    Shows.delete_show(id)
    return redirect("/dashboard")


if __name__ == "__main__":
    app.run(debug = True)

    

    

    

    

