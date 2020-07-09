from flask import Flask

app = Flask(__name__)


##########################
# DATABASE SETTINGS ######
##########################



##########################
# BLUEPRINTS #############
##########################
from po3.core.views import core
app.register_blueprint(core)