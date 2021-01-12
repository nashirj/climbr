from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from climbr.auth import login_required

from app import db

bp = Blueprint('blog', __name__)

from climbr.models.user import User
from climbr.models.post import Post
from sqlalchemy import text


@bp.route('/')
def index():
    posts = db.session.query(Post).all()

    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        holds = [request.form[key] for key in request.form.keys() if "hold" in key]
        climbing_route = "|".join(holds)
        print(climbing_route)

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            post = Post(title=title, body=body, poster_id=g.user.id, climbing_route=climbing_route)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


def get_post(uid, check_author=True):
    post = db.session.query(Post).filter_by(poster_id=uid).first()
    
    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post.poster_id != g.user.id:
        abort(403)

    holds = []
    if post.climbing_route:
        hold_strs = post.climbing_route.split('|')
        hold_indices = [indices.split(',') for indices in hold_strs]
        holds = [[int(row),int(col)] for row, col in hold_indices]
        
    return post, holds


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post, holds = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        holds = [request.form[key] for key in request.form.keys() if "hold" in key]
        climbing_route = "|".join(holds)
        
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            post.title = title
            post.body = body
            post.climbing_route = climbing_route
            db.session.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    post, _ = get_post(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('blog.index'))


@bp.route('/<int:id>/detail', methods=('GET',))
def detail(id):
    post, holds = get_post(id, False)

    print(holds)
    return render_template('blog/detail.html', post=post, holds=holds)
