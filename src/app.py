from flask import Flask, render_template, request, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Farmer_MiddleMan.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
db = SQLAlchemy(app)


"""*************************************************************************************************
                                FARMER TABLE IN DATABASE
**************************************************************************************************"""


class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    contact_no = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)
    land = db.Column(db.String(200), nullable=False)
    street = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    state = db.Column(db.String(200), nullable=False)
    crop = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return f"{self.first_name} - {self.land} - {self.crop}"


"""*************************************************************************************************
                                MIDDLEMAN TABLE IN DATABASE
**************************************************************************************************"""


class Middleman(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    contact_no = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=True, nullable=False)
    interest_rate = db.Column(db.String(200), nullable=False)
    street = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    state = db.Column(db.String(200), nullable=False)
    crops = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return f"{self.first_name} - {self.contact_no} - {self.interest_rate} "


"""*************************************************************************************************
                                    FUNCTION TO ROUTE ON HOME PAGE
**************************************************************************************************"""


@app.route("/")
def home():
    print("hey")
    return render_template("HTML/home.html")


"""*************************************************************************************************
                                    FUNCTION FOR LOGIN
**************************************************************************************************"""


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["Email"]
        password = request.form["password"]

        print(f"Email: {email}")
        print(f"Password: {password}")

        farmer = Farmer.query.filter_by(email=email, password=password).first()
        middleman = Middleman.query.filter_by(email=email, password=password).first()

        # print(f"Farmer: {farmer}")
        # print(f"Middleman: {middleman}")

        if farmer:
            session["user_id"] = farmer.id
            session["user role"] = "farmer"
            return render_template("HTML/farmer_dashboard.html", farmer=farmer)
        elif middleman:
            session["user_id"] = middleman.id
            session["user role"] = "middleman"
            return render_template("HTML/middleman_dashboard.html", middleman=middleman)
        else:
            return render_template("HTML/register.html")
    return render_template("HTML/login.html")


"""*************************************************************************************************
                                FUNCTION TO ROUTE ON REGISTER PAGE
**************************************************************************************************"""


@app.route("/register")
def register():
    return render_template("HTML/register.html")


"""*************************************************************************************************
                                FUNCTION TO REGISTER AS A FARMER
**************************************************************************************************"""


@app.route("/register/farmer", methods=["POST"])
def farmer_register():
    first_name = request.form["Fname"]
    last_name = request.form["Lname"]
    contact_no = request.form["PhoneNo"]
    email = request.form["email"]
    password = request.form["pass"]
    land = request.form["land"]
    street = request.form["street"]
    city = request.form["city"]
    state = request.form["state"]
    crop = request.form["crops"]

    new_farmer = Farmer(
        first_name=first_name,
        last_name=last_name,
        contact_no=contact_no,
        email=email,
        password=password,
        land=land,
        street=street,
        city=city,
        state=state,
        crop=crop,
    )
    db.session.add(new_farmer)
    db.session.commit()
    # flash('Farmer registered successfully!', 'success')
    return render_template("HTML/farmer_dashboard.html", farmer=new_farmer)


"""*************************************************************************************************
                                FUNCTION TO REGISTER AS A MIDDLEMAN
**************************************************************************************************"""


@app.route("/register/middleman", methods=["POST"])
def middleman_register():
    first_name = request.form["FnameMiddleman"]
    last_name = request.form["LnameMiddleman"]
    contact_no = request.form["PhoneNoMiddelMan"]
    email = request.form["emailMiddleman"]
    password = request.form["passMiddleman"]
    interest_rate = request.form["interset"]
    street = request.form["streetMiddleman"]
    city = request.form["cityMiddleman"]
    state = request.form["stateMiddleman"]
    crops = request.form["cropsMiddleman"]

    new_middleman = Middleman(
        first_name=first_name,
        last_name=last_name,
        contact_no=contact_no,
        email=email,
        password=password,
        interest_rate=interest_rate,
        street=street,
        city=city,
        state=state,
        crops=crops,
    )
    db.session.add(new_middleman)
    db.session.commit()
    # flash('Farmer registered successfully!', 'success')
    return render_template("HTML/middleman_dashboard.html", middleman=new_middleman)


"""*************************************************************************************************
                                ROUTING TO FARMER DASHBOARD
**************************************************************************************************"""


@app.route("/farmer_dashboard")
def farmer_dashboard():
    return render_template("HTML/Farmer_dashboard.html")


"""*************************************************************************************************
                                ROUTING TO MIDDLEMAN DASHBOARD
**************************************************************************************************"""


@app.route("/middleman_dashboard")
def middleman_dashboard():
    return render_template("HTML/middleman_dashboard.html")


"""*************************************************************************************************
                                RUNNING APP
**************************************************************************************************"""
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
