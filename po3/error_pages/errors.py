from flask import Blueprint,render_template

error_pages = Blueprint('error_pages',__name__)

@error_pages.app_errorhandler(404)
def error404(error):
    return render_template('error_templates/404.html'), 404

@error_pages.app_errorhandler(404)
def error403(error):
    return render_template('error_templates/403.html'), 403