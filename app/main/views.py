from flask import render_template
from . import main
from flask_login import login_required

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

# Input! the flask_login decorator '@login_required' that will intercept a request and check if 
# the user is authenticated and if not the user will be redirected to the login page.
