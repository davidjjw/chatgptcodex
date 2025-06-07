from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import db, Notebook, Section, Note

notes_bp = Blueprint(
    'notes', __name__, url_prefix='/notebooks/<int:nb_id>/sections/<int:sec_id>/notes'
)


def get_notebook_section_or_404(nb_id, sec_id):
    nb = Notebook.query.filter_by(id=nb_id, user_id=current_user.id).first_or_404()
    sec = Section.query.filter_by(id=sec_id, notebook_id=nb.id).first_or_404()
    return nb, sec


@notes_bp.route('/')
@login_required
def list_notes(nb_id, sec_id):
    nb, sec = get_notebook_section_or_404(nb_id, sec_id)
    notes = Note.query.filter_by(section_id=sec.id).all()
    return render_template('notes/list.html', notebook=nb, section=sec, notes=notes)


@notes_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_note(nb_id, sec_id):
    nb, sec = get_notebook_section_or_404(nb_id, sec_id)
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        note = Note(title=title, body=body, section_id=sec.id)
        db.session.add(note)
        db.session.commit()
        return redirect(url_for('notes.list_notes', nb_id=nb.id, sec_id=sec.id))
    return render_template('notes/form.html', notebook=nb, section=sec)


@notes_bp.route('/<int:note_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_note(nb_id, sec_id, note_id):
    nb, sec = get_notebook_section_or_404(nb_id, sec_id)
    note = Note.query.filter_by(id=note_id, section_id=sec.id).first_or_404()
    if request.method == 'POST':
        note.title = request.form['title']
        note.body = request.form['body']
        db.session.commit()
        return redirect(url_for('notes.list_notes', nb_id=nb.id, sec_id=sec.id))
    return render_template('notes/form.html', notebook=nb, section=sec, note=note)


@notes_bp.route('/<int:note_id>/delete', methods=['POST'])
@login_required
def delete_note(nb_id, sec_id, note_id):
    nb, sec = get_notebook_section_or_404(nb_id, sec_id)
    note = Note.query.filter_by(id=note_id, section_id=sec.id).first_or_404()
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('notes.list_notes', nb_id=nb.id, sec_id=sec.id))
