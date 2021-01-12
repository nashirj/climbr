from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from climbr.auth import login_required

from app import db

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
    db =  get_db()
    posts = db.execute(
        'SELECT p.id, title, body, climbing_route, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()

    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        holds = [request.form[key] for key in request.form.keys() if "hold" in key]
        # TODO: update this to parse form
        climbing_route = "|".join(holds)
        print(climbing_route)

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id, climbing_route)'
                ' VALUES (?, ?, ?, ?)',
                (title, body, g.user['id'], climbing_route)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


def get_post(uid, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, climbing_route, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (uid,)
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    holds = []
    if post['climbing_route']:
        hold_strs = post['climbing_route'].split('|')
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
        climbing_route = ""

        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?, climbing_route = ?'
                ' WHERE id = ?',
                (title, body, climbing_route, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))


@bp.route('/<int:id>/detail', methods=('GET',))
def detail(id):
    post, holds = get_post(id, False)

    print(holds)
    return render_template('blog/detail.html', post=post, holds=holds)
