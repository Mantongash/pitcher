from datetime import datetime
from flask import Flask, render_template, redirect, flash,url_for
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SECRET_KEY"] = "6b2d9404ac5ccfb7635f8bc5650b5119"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///records.db"

db = SQLAlchemy(app)