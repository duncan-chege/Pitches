from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
# import the Required class validator that will prevent the user from submitting the form without Inputting a value
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')