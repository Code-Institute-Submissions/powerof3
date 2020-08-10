from flask import render_template,url_for,flash,request,redirect,Blueprint,abort
from flask_login import current_user,login_required
from po3 import db
from po3.models import Recipe
from po3.recipe_cards.forms import RecipeForm

recipe_cards = Blueprint('recipe_cards',__name__)

# Create recipe card

@recipe_cards.route('/add_recipe',methods=['GET','POST'])
@login_required
def add_recipe():
    form = RecipeForm()

    if form.validate_on_submit():

        recipe_card = Recipe(title=form.title.data,
                            description=form.description.data,
                            ingriedient1=form.ingriedient1.data,
                            ingriedient2=form.ingriedient2.data,
                            ingriedient3=form.ingriedient3.data,
                            smoothie_video=form.smoothie_video.data,
                            user_id=current_user.id)

        db.session.add(recipe_card)
        db.session.commit()
        flash('Recipe Card created')
        return redirect(url_for('core.index'))
    
    return render_template('add_recipe.html',form=form)

# View recipe

@recipe_cards.route('/<int:recipe_card_id>')
def recipe_card(recipe_card_id):
    recipe_card = Recipe.query.get_or_404(recipe_card_id)
    return render_template('recipe_card.html',title=recipe_card.title,
                            date=recipe_card.date,recipe=recipe_card
    )

# Edit recipe

@recipe_cards.route("/<int:recipe_card_id>/edit_recipe",methods=['GET','POST'])
@login_required
def edit_recipe(recipe_card_id):
    recipe_card = Recipe.query.get_or_404(recipe_card_id)

    if recipe_card.chef != current_user:
        abort(403)

    form = RecipeForm()

    if form.validate_on_submit():

        recipe_card.title = form.title.data
        recipe_card.description = form.description.data
        recipe_card.ingriedient1 = form.ingriedient1.data
        recipe_card.ingriedient2 = form.ingriedient2.data
        recipe_card.ingriedient3 = form.ingriedient3.data
        recipe_card.smoothie_video = form.smoothie_video.data
        recipe_card.user_id = current_user.id

        db.session.commit()
        flash('Recipe Card updated')
        return redirect(url_for('recipe_cards.recipe_card',recipe_card_id=recipe_card.id))
    
    elif request.method == 'GET':
        form.title.data = recipe_card.title
        form.description.data = recipe_card.description
        form.ingriedient1.data = recipe_card.ingriedient1
        form.ingriedient2.data = recipe_card.ingriedient2
        form.ingriedient3.data = recipe_card.ingriedient3
        form.smoothie_video.data = recipe_card.smoothie_video

    return render_template('add_recipe.html',title='Editing',form=form)


@recipe_cards.route('/<int:recipe_card_id>/delete_recipe',methods=['GET','POST'])
@login_required
def delete_recipe(recipe_card_id):
    recipe_card = Recipe.query.get_or_404(recipe_card_id)
    if recipe_card.chef != current_user:
        abort(403)

    db.session.delete(recipe_card)
    db.session.commit()
    flash('Recipe deleted')
    return redirect(url_for('core.index'))


