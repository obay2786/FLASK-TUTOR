from flask import Blueprint, render_template, request, flash, jsonify, send_from_directory, redirect
from flask_login import login_required, current_user
from .models import Note, Visitor,User
from . import db
import json
import base64
from sqlalchemy import asc, desc,text
import requests
from PIL import Image, ImageOps
from io import BytesIO
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

@views.route('/waiting', methods=['GET', 'POST'])
@login_required
def waiting():

    return render_template("waiting.html", user=current_user)

@views.route('/history', methods=['GET', 'POST'])
@login_required
def history():

    return render_template("history.html", user=current_user)
@views.route('/approval', methods=['GET', 'POST'])
@login_required
def approval():

    return render_template("approval.html", user=current_user)

def saveB(photo):
  
    img = Image.open(photo)
    img = ImageOps.exif_transpose(img)
    output_size = (600, 600)
    img.thumbnail(output_size)
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    
    return img_str


ROWS_PER_PAGE = 5
@views.route('/visitor',methods=['GET', 'POST'])
@login_required
def visitor():
    if request.method == 'POST':
        if request.form.get('formEdit') == 'edit':
            print(request.form)
            data ={}
            
            data['id'] = request.form.get('id')
            data['nama'] = request.form.get('nama')
            data['nik'] = request.form.get('nik')
            data['company'] = request.form.get('company')
            
            print(data)
            dataQ = Visitor.query.filter_by(id=data['id']).first()
            dataQ.nama = data['nama']
            dataQ.nik = data['nik']
            dataQ.namaVendor = data['company']
           
            db.session.commit()
            print('okeeeee')
        elif request.form.get('formEdit') == 'editPhoto':
            print(request.form)
            data ={}
            data['id'] = request.form.get('id')
            data['photo'] = saveB(request.files['photo'])
            
            
            print(data)
            dataQ = Visitor.query.filter_by(id=data['id']).first()
            dataQ.photo = data['photo']
            
            db.session.commit()
            print('okeeeee')
    page = request.args.get('page', 1, type=int)
    print(page)
    #data = Visitor.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    data = Visitor.query.order_by(text('id desc')).paginate(page=page, per_page=ROWS_PER_PAGE)
    #data.reverse()
    #data.items.reverse()
    return render_template("adminvisitordata.html", user=current_user,data=data)



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

@views.route("/kiosk/<path:path>")
def kiosk(path):
    return send_from_directory('kiosk', path)

@views.route("/kiosk/")
def kioskindex():
    return redirect("./index.html", code=302)

@views.route("/checked/<path:path>")
def cek(path):
    return send_from_directory('checked', path)

@views.route("/check-in")
def kcheckin():
    return redirect("./checked/check-in.html", code=302)

@views.route("/check-out")
def kcheckout():
    return redirect("./checked/check-out.html", code=302)

@views.route('/delstaff', methods=['POST'])
def delStaff():
    data = json.loads(request.data)
    staffID= data['id']
    print(staffID)
    staff = User.query.filter_by(id=staffID).first()
    if staff:
        db.session.delete(staff)
        db.session.commit()
    print(staff.id)
    return jsonify({})

@views.route('/getstaff', methods=['POST'])
def getStaff():
    data = json.loads(request.data)
    staffID = data['id']
    print(staffID)
    staff = User.query.filter_by(id=staffID).first()
    data = {}
    data['id'] = staff.id
    data['userName'] = staff.userName
    data['firstName'] = staff.firstName
    data['email'] = staff.email
    data['empID'] = staff.empID
    data['badgeID'] = staff.badgeID
    data['role'] = staff.role
    data['depart'] = staff.depart
    data['photo'] = staff.photo
    return jsonify(data)

@views.route('/getvisitor', methods=['POST'])
def getVisitor():
    data = json.loads(request.data)
    nik = data['nik']
    print(nik)
    visitor = Visitor.query.filter_by(nik=nik).first()
    print(visitor)
    data = {}
    data['id'] = visitor.id
    data['nik'] = visitor.nik
    data['nama'] = visitor.nama
    data['badge'] = '111'
    data['company'] = visitor.namaVendor
    data['photo'] = visitor.photo
    
    return jsonify(data)

@views.route('/delvisitor', methods=['POST'])
def delVisitor():
    data = json.loads(request.data)
    visitorID= data['id']
    print(visitorID)
    visitorD = Visitor.query.filter_by(id=visitorID).first()
    if visitorD:
        db.session.delete(visitorD)
        db.session.commit()
    
    return jsonify({})