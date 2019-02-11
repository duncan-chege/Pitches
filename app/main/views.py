from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import  User

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

# Input! the flask_login decorator '@login_required' that will intercept a request and check if 
# the user is authenticated and if not the user will be redirected to the login page.

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)