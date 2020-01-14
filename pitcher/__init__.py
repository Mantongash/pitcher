from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)

app.config["SECRET_KEY"] = "6b2d9404ac5ccfb7635f8bc5650b5119"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///records.db"

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from pitcher import routes