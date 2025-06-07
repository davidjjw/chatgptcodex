from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import db, Notebook, Section

sections_bp = Blueprint(
    'sections', __name__, url_prefix='/notebooks/<int:nb_id>/sections'
)

def get_notebook_or_404(nb_id):
    return Notebook.query.filter_by(id=nb_id, user_id=current_user.id).first_or_404()

@sections_bp.route('/')
@login_required
def list_sections(nb_id):
    nb = get_notebook_or_404(nb_id)
    sections = Section.query.filter_by(notebook_id=nb.id, parent_id=None).all()
    return render_template('sections/list.html', notebook=nb, sections=sections)

@sections_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_section(nb_id):
    nb = get_notebook_or_404(nb_id)
    parent_id = request.args.get('parent_id')
    if request.method == 'POST':
        title = request.form['title']
        parent = request.form.get('parent_id') or None
        sec = Section(title=title, notebook_id=nb.id, parent_id=parent)
        db.session.add(sec)
        db.session.commit()
        return redirect(url_for('sections.list_sections', nb_id=nb.id))
    parents = Section.query.filter_by(notebook_id=nb.id).all()
    return render_template('sections/form.html', notebook=nb, parents=parents, parent_id=parent_id)

@sections_bp.route('/<int:sec_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_section(nb_id, sec_id):
    nb = get_notebook_or_404(nb_id)
    sec = Section.query.filter_by(id=sec_id, notebook_id=nb.id).first_or_404()
    if request.method == 'POST':
        sec.title = request.form['title']
        sec.parent_id = request.form.get('parent_id') or None
        db.session.commit()
        return redirect(url_for('sections.list_sections', nb_id=nb.id))
    parents = Section.query.filter(Section.notebook_id==nb.id, Section.id!=sec.id).all()
    return render_template('sections/form.html', notebook=nb, section=sec, parents=parents, parent_id=sec.parent_id)

@sections_bp.route('/<int:sec_id>/delete', methods=['POST'])
@login_required
def delete_section(nb_id, sec_id):
    nb = get_notebook_or_404(nb_id)
    sec = Section.query.filter_by(id=sec_id, notebook_id=nb.id).first_or_404()
    db.session.delete(sec)
    db.session.commit()
    return redirect(url_for('sections.list_sections', nb_id=nb.id))
