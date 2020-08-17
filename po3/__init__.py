import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Message, Mail

mail = Mail()
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = 'monster1energy2'

##########################
# DATABASE CONFIG ########
##########################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
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
from po3.recipe_cards.views import recipe_cards
from po3.contact.views import contact
app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(recipe_cards)
app.register_blueprint(contact)

##########################
# ERROR HANDLING #########
##########################


##########################
# FLASK-MAIL CONFIG ######
##########################

mail_settings = {
    'MAIL_SERVER' : 'smtp.gmail.com',
    'MAIL_PORT' : '465',
    'MAIL_USE_TLS' : False,
    'MAIL_USE_SSL' : True,
    #'MAIL_DEBUG' : True,
    'MAIL_USERNAME' : 'powof333@gmail.com',
    'MAIL_PASSWORD' : 'kronkron',
    'MAIL_DEFAULT_SENDER' : 'powerof333@yahoo.com',
    'MAIL_MAX_EMAILS' : None,
    'MAIL_SUPPRESS_SEND' : False,
    #'MAIL_ASCII_ATTACHMENTS' : False
}
app.config.update(mail_settings)
mail.init_app(app)