from flask import Blueprint, render_template, request, flash, jsonify, send_from_directory
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)



@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
   
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/history', methods=['GET', 'POST'])
@login_required
def history():

    return render_template("history.html", user=current_user)


@views.route('/visitor', methods=['GET', 'POST'])
@login_required
def adminIndex():

    return render_template("adminvisitordata.html", user=current_user)

@views.route('/staff', methods=['GET', 'POST'])
@login_required
def staff():
    if current_user.role == 'Admin':
        return render_template("addaccount.html", user=current_user)
    else:
        return render_template("login.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route("/assets/<path:path>")
def css(path):
    return send_from_directory('assets', path)