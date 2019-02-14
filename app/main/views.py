from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import  User,Pitch
from .forms import UpdateProfile, PitchForm
from ..import db,photos

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

# Input! the flask_login decorator '@login_required' that will intercept a request and check if 
# the user is authenticated and if not the user will be redirected to the login page.

@main.route('/user/<uname>',methods = ['GET','POST'])
@login_required
def profile(uname):
    form = UpdateProfile()
    user = User.query.filter_by(username = uname).first()
    
    pitches = Pitch.query.filter_by(user_id = user.id).all()

    if user is None:
        abort(404)

    if form.validate_on_submit():
            user.bio = form.bio.data

            db.session.add(user)
            db.session.commit()

            return redirect(url_for('.profile',uname=user.username))

    return render_template("profile/profile.html", user = user, form = form, pitches = pitches)

@main.route('/user/pitch/<uname>',methods = ['GET','POST'])
@login_required
def new_pitch(uname):

    pform = PitchForm()
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    if pform.validate_on_submit():
        category = pform.category.data
        pitch = pform.pitch.data

        new_pitch = Pitch(mycategory=category, mypitch= pitch, user_id = user.id)

         # Updated pitch instance
        new_pitch.save_pitch()

        return redirect(url_for('main.profile', uname = uname))

    return render_template('new_pitch.html', pitch_form = pform)

@main.route('/pitches', methods = ['GET','POST'])
def pitches():
    pitches = Pitch.query.all()

    return render_template('pitches.html', pitches = pitches)

