from flask import Blueprint, render_template, request, flash, jsonify, send_from_directory
from flask_login import login_required, current_user
from .models import Note, Visitor
from . import db
import json
from sqlalchemy import asc, desc
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

ROWS_PER_PAGE = 5
@views.route('/visitor',methods=['GET', 'POST'])
@login_required
def visitor():
    
    page = request.args.get('page', 1, type=int)
    print(page)
    #data = Visitor.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    data = Visitor.query.order_by('id').paginate(page=page, per_page=ROWS_PER_PAGE)
    #print(data.reverse())
    return render_template("adminvisitordata.html", user=current_user,data=data)

@views.route('/staff', methods=['GET', 'POST'])
@login_required
def staff():
    if current_user.role == 'Admin':
        return render_template("staff.html", user=current_user)
    else:
        return render_template("login.html", user=current_user)

@views.route('/report')
@login_required
def report():
    if current_user.role == 'Admin' or current_user.role == 'Security':
        return render_template("report.html", user=current_user)
    else:
        return render_template("login.html", user=current_user)
@views.route('/nama')
@login_required
def namadelete_note():
    nama = {"nama":"novel martin harianto"}
    return jsonify(nama)

@views.route("/assets/<path:path>")
def css(path):
    return send_from_directory('assets', path)