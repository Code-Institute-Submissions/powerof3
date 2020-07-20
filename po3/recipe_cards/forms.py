from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,FileField
from wtforms.validators import DataRequired


class RecipeForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    description = TextAreaField('Description',validators=[DataRequired()])
    ingriedient1 = StringField('Ingridient 1 of 3',validators=[DataRequired()])
    ingriedient2 = StringField('Ingridient 2 of 3',validators=[DataRequired()])
    ingriedient3 = StringField('Ingridient 3 of 3',validators=[DataRequired()])
    smoothie_image = StringField('Smoothie',validators=[DataRequired()])
    submit = SubmitField('Post')

    

    
