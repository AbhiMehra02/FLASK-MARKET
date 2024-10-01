from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///C:/Users/abhis/Desktop/program/flask_project/FlaskMarket/market/market.db'
app.config['SECRET_KEY']='fe959aa397932cd16840fc18'
db = SQLAlchemy(app)

bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view="login_page"
login_manager.login_message_category="info"

from market import routes


