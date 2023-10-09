from flask import Blueprint, render_template, request, redirect, url_for, session
from .models import Destination, User
from . import db

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    destinations = db.session.scalars(db.select(Destination)).all()    
    # Get the user from the database
    if '_user_id' in session:
        user = db.session.scalar(db.select(User).where(User.id==session['_user_id']))
        print(user)
        return render_template('index.html', destinations=destinations, user=user.name)
    
    return render_template('index.html', destinations=destinations)
@mainbp.route('/search')
def search():
    if request.args['search'] and request.args['search'] != "":
        print(request.args['search'])
        query = "%" + request.args['search'] + "%"
        destinations = db.session.scalars(db.select(Destination).where(Destination.description.like(query)))
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))