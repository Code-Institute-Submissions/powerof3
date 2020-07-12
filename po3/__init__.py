import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
bcrypt = Bcrypt(app)


##########################
# DATABASE CONFIG ########
##########################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

##########################
# LOGIN MGR ##############
##########################

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

##########################
# BLUEPRINTS #############
##########################

from po3.core.views import core
from po3.error_pages.errors import error_pages
from po3.users.views import users
app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)

##########################
# ERROR HANDLING #########
##########################
