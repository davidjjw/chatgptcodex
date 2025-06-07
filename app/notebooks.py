from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import db, Notebook


notebook_bp = Blueprint('notebooks', __name__, url_prefix='/notebooks')


@notebook_bp.route('/')
@login_required
def list_notebooks():
    notebooks = Notebook.query.filter_by(user_id=current_user.id).all()
    return render_template('notebooks/list.html', notebooks=notebooks)


@notebook_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_notebook():
    if request.method == 'POST':
        title = request.form['title']
        nb = Notebook(title=title, user_id=current_user.id)
        db.session.add(nb)
        db.session.commit()
        return redirect(url_for('notebooks.list_notebooks'))
    return render_template('notebooks/form.html')


@notebook_bp.route('/<int:nb_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_notebook(nb_id):
    nb = Notebook.query.filter_by(id=nb_id, user_id=current_user.id).first_or_404()
    if request.method == 'POST':
        nb.title = request.form['title']
        db.session.commit()
        return redirect(url_for('notebooks.list_notebooks'))
    return render_template('notebooks/form.html', notebook=nb)


@notebook_bp.route('/<int:nb_id>/delete', methods=['POST'])
@login_required
def delete_notebook(nb_id):
    nb = Notebook.query.filter_by(id=nb_id, user_id=current_user.id).first_or_404()
    db.session.delete(nb)
    db.session.commit()
    return redirect(url_for('notebooks.list_notebooks'))
