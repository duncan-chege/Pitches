from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from flask_wtf.file import FileField, FileAllowed
# import the Required class validator that will prevent the user from submitting the form without Inputting a value
from wtforms.validators import InputRequired,Length
# from flask_login import current_user 

class UpdateProfile(FlaskForm):
    bio = TextAreaField('How are you feeling today?',validators = [InputRequired(), Length(min=5, max=20)])
    # picture= FileField('Update Profile Picture', validators= [FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

class PitchForm(FlaskForm):
    category= StringField('Category title',validators=[InputRequired()], render_kw={"placeholder": "Enter indusrty related fields e.g technology, agriculture, entertainment, etc"})
    pitch= TextAreaField('Input your pitch', validators=[InputRequired(), Length(min=10, max=100)], render_kw={"placeholder": "Your pitch should not exceed 100 characters"})
    submit = SubmitField('Submit')
