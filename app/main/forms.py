from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required



class ReviewForm(FlaskForm):

    title = StringField('Review title',validators = [Required()])
    review = TextAreaField('Movie review', validators = [Required()])
    submit = SubmitField('Submit')

#We then import StringField,TextAreaField and SubmitField field classes.These will help us create a text field, a text Area field and a submit button
#we import the Required class validator that will prevent the user from submitting the form without Inputting a value.
#We then create the ReviewForm class that inherits from the FlaskFormclass. 
# We Initialize the Field types by passing in two parameters. 
# The first is the label and the second is a list of Validators where we initialize the Required validator.