from flask import Flask, redirect, render_template, request,session,flash
from flask_bcrypt import Bcrypt
from controllers.queries import Query
from controllers.cca_gdpr import California, Europe, TopPeaksDevelopment
from controllers.login_process import User_config, User_info
from config.grab_data import Data
from config.grab_data import *
from datetime import date, datetime
from datetime import date
import re


app = Flask(__name__)
bcrypt = Bcrypt(app)

t = datetime.now()
app.secret_key = str(t) + "Secret Key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process-cca-gdpr", methods=['POST'])
def process_policy():
    try:
        data = {
            "cca" : request.form["california"],
            "gdpr" : request.form["europe"],
            "tpd" : request.form["top_peaks"],
            "ip_address" : "test"
        }
        try:
            California.send(data)
        except:
            pass

        try:
            Europe.send(data)
        except:
            pass
        try:
            TopPeaksDevelopment.send(data)
        except:
            pass
    except:
        return ""

    session["session_id"] = str(t) + "session_key"
    return redirect("/Dashboard")
   




@app.route("/Dashboard")
def dashboard():
    if "session_id" in session:
        comm = Data.get_commodities()
        newsAlRa = Data.get_alra()
        newsAlJa = Data.get_alja()
        newsBBC = Data.get_bbc()
        newsCNN = Data.get_cnn()
        newsSKY = Data.get_sky()
        cve = SecurityCVE.cve()
        all = Data.get_all_a_title()

        secEx = SecurityExchange.securitexchangepressrelease();
        secFil = SecurityExchangeFiling.securitexchangefiling();
        weather = Weather.weather();
        wh = WhiteHouse.whitehouse()
        house = House.house()
        sen = Senate.senate()

        p = "f"#session["username"]
        if p != " ":
            session["date"] = date.today()
            return render_template("dashboard.html" 
            , comm = comm 
            , alra = newsAlRa
            , alja = newsAlJa
            , bbc = newsBBC
            , cnn = newsCNN
            , sky = newsSKY
            , t = datetime.now()
            , all = all
            , vul = cve

            , secEx = secEx
            , secFil = secFil
            , weather = weather
            , wh = wh
            , house = house
            , sen = sen
            )
        else:
            return redirect("/")
    
    else:
        return redirect("/")
pass

@app.route("/Dashboard_=%&")
def dashboardtt():
        
        return redirect("/")
pass

@app.route("/Login_=&%")
def dashboardt():
        return render_template("/login.html")
pass


@app.route("/log-in-process", methods=['POST'])
def login_process():
    data = {
        "uname" : request.form["uname"],
        "pword" : request.form["pword"]
    }
    verification = {
        "uname" : request.form["uname"],
        "pword" : request.form["pword"]
    }
    """
        xTake in Uname or Email, PWord, Salt
            xSELECT Uname,Email,Id FROM user WHERE uname = Uname
                xIf SelectUname = True or SelectEmail = True
                xSELECT pword FROM user_config WHERE user_id = id
                    xIf pword = PWord
                    xSELECT salt FROM user_config WHERE user_id = id
                        xsession["uname"] == Uname
                        xsalt["salt"] == Salt
                        xreturn redirect("/Balancesheet")
                    xelse:
                        xretun redirect("/")
                
        
    """
    
    user = User_info.get_user_info(data)
    data = {
        "id" : user.id
    }
    user_config = User_config.get_user_config_info(data)
    if user_config.pword == bcrypt.generate_password_hash(verification["pword"]):
        session['id'] = user_config.user_id
        session['key'] = ""
        return redirect("/balance_sheet")
    else:
        flash("Password, Email or Salt Wrong")
        return redirect("/")

@app.route("/logout-success")
def logout():
    session.clear()
    return redirect('/')

@app.route("/register")
def register():
    
    return render_template("register.html")

@app.route("/register_process", methods=['POST'])
def register_user():
    data = {
        "uname" : request.form["uname"],
        "pword" : request.form["pword"],
        "pword2" : request.form["pword2"],
        "email" : request.form["email"],
        "email2" : request.form["email2"],
        "weather" : "Nothing for now"
    }

    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    """
        if passwords dont match
            if email not in correct format
                if emails dont match
                    if uname is not in use
                        Then Regiester

    """
    if data["pword"] == data["pword2"]:
        if len(data["pword"]) >=2 :
            if re.match(regex, data['email']):
                    if data["email"] == data["email2"]:
                        if 1 == 1 :
                            data2 = {
                                "uname" : data["uname"],
                                "email" : data["email"]
                            }
                            User_info.register(data2)
                            data3 = {
                                "weather" : "Nothing for now",
                                "pword" : bcrypt.generate_password_hash(data["pword"]),
                                "salt" : " "
                            }
                            User_config.register_user_config_info(data3) 
                            session["uname"] = data["uname"]  
                            return redirect("/balance_sheet")
                        else:
                            flash('Email already in use.')
                            return redirect("/register")
                    else:
                        flash('Email does not match')
                        return redirect("/register")
            else:
                flash('Email is not the corret format')
                return redirect("/register")
        else:
            flash('Password too short')
            return redirect("/register")
    else:
        flash('Password do not match')
        return redirect("/register")

@app.route("/balance_sheet")
def success():
    
    if "uname" in session:
        return render_template("balance_sheet.html")
    else:
        return redirect("/register")












"""

@app.route("/xend")
def index():

    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.lower()

    # In your templates directory, create a mobile version of your site (mobile.index.html).
    # Likewise, add your desired desktop template as well (desktop.index.html).

    if "iphone" in user_agent:
        return render_template('mobile.index.html')
    elif "android" in user_agent:
        return render_template('mobile.index.html')
    else:
        session["username"] = " "
        session["password"] = ""
        session["key"] = ""
        return render_template("login.html")
pass
"""
"""

"""
@app.route("/Messages")
def messages():
    p = session["username"]
    if p != " ":
        session["date"] = date.today()
        return render_template("messages.html")
    else:
        return redirect('/')
pass

@app.route("/display_project_conversation&name=")
def display_project_messages():
    projects = Query.retrieve_project()
    messages = Query.retrieve_messages()
    return render_template(" display_project_messages.html", all_messages = messages, projects = projects)
pass

@app.route("/send-message", methods=['POST'])
def send_message():
    data = {
        "username" : 'test',
        "message" : request.form['message']
    }
    Query.send_message(data)
    return redirect('/')
pass

if __name__ == "__main__":
    app.run(debug = True,
    port = 5001)
 