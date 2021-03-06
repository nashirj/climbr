import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from app import db

from werkzeug.security import check_password_hash, generate_password_hash

from climbr.models.user import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

# change this to emails and do email verification
approved_users=['alden', 'nashir', 'evan']

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        print(f"uname: {username}")

        if not username:
            error = 'Username is required.'
        elif username not in approved_users:
            error = 'Sorry, you are not currently approved to sign up for this app.'
        elif not password:
            error = 'Password is required.'
        elif db.session.query(User).filter_by(username=username).first() is not None:
            error = f'User {username} is already registered.'
        
        if error is None:
            user = User(username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()

            flash("Sign up successful - please log in.")

            return redirect(url_for('auth.login'))

        flash(error)

    # this line executed if request.method == 'GET' or there was an error in POST
    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        user = db.session.query(User).filter_by(username=username).first()

        if user is None:
            error = 'No user with that username.'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user.uid
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = db.session.query(User).filter_by(uid=user_id).first()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view