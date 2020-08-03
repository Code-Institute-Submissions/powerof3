from po3.models import Recipe
from flask import render_template,Blueprint,request,url_for

core = Blueprint('core',__name__)


@core.route('/')
def index():
    page = None
    recipe_cards = Recipe.query.order_by(Recipe.date.desc()).paginate(page=page,per_page=3)
    return render_template('index.html',recipe_cards=recipe_cards)

@core.route('/about')
def about():
    return render_template('about.html')

@core.route('/contact')
def contact():
    return render_template('contact.html')

@core.route('/all_recipes.html')
def all_recipes():
    page = None
    recipe_cards = Recipe.query.order_by(Recipe.date.desc()).paginate(page=page,per_page=3)
    return render_template('all_recipes.html',recipe_cards=recipe_cards)
