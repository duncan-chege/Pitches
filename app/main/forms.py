from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from flask_wtf.file import FileField, FileAllowed
# import the Required class validator that will prevent the user from submitting the form without Inputting a value
from wtforms.validators import Required,Length
# from flask_login import current_user 

class UpdateProfile(FlaskForm):
    bio = TextAreaField('How are you feeling today?',validators = [Required(), Length(max=20)])
    # picture= FileField('Update Profile Picture', validators= [FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')

