from flask import Flask

app = Flask(__name__)


##########################
# DATABASE SETTINGS ######
##########################



##########################
# BLUEPRINTS #############
##########################

from po3.core.views import core
from po3.error_pages.errors import error_pages
app.register_blueprint(core)
app.register_blueprint(error_pages)

##########################
# ERROR HANDLING #########
##########################
