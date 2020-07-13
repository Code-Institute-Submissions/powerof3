from flask import render_template,Blueprint,request,url_for

core = Blueprint('core',__name__)


@core.route('/')
def index():
    return render_template('index.html')

@core.route('/about')
def about():
    return render_template('about.html')

@core.route('/contact')
def contact():
    return render_template('contact.html')
