from flask import Blueprint, render_template, request, flash, redirect, url_for,current_app, jsonify
import secrets
import json
import os
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from PIL import Image, ImageOps
import base64
from io import BytesIO
from .hik import hik
from sqlalchemy import asc, desc,text
auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    if request.method == 'POST':
        userName = request.form.get('userName')
        password = request.form.get('password')

        user = User.query.filter_by(userName=userName).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('username does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

def saveImages(photo):
    randomHex = secrets.token_hex(8)
    _, file_ex = os.path.splitext(photo.filename)
    pictureFn = randomHex + file_ex
    picturePath = os.path.join(current_app.root_path,'upload/staff',pictureFn)
    img = Image.open(photo)
    img = ImageOps.exif_transpose(img)
    output_size = (700, 700)
    img.thumbnail(output_size)
    img.save(picturePath)
    return pictureFn
def uploadImages(photo):
  
    img = Image.open(photo)
    img = ImageOps.exif_transpose(img)
    output_size = (700, 700)
    img.thumbnail(output_size)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue())
    
    return img_str

def saveB(photo):
  
    img = Image.open(photo)
    img = ImageOps.exif_transpose(img)
    output_size = (600, 600)
    img.thumbnail(output_size)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue())
    
    return img_str

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        userName = request.form.get('userName')
        firstName = request.form.get('firstName')
        role = request.form.get('role')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        data = request.form
        
        print(data)
        user = User.query.filter_by(userName=userName).first()
        if user:
            flash('Username already exists.', category='error')
        elif len(userName) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif role == '':
            flash('Role Wajib dipilih.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            phName = saveImages(request.files['photo'])
            new_user = User(userName=userName, firstName=firstName,role=role, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)

ROWS_PER_PAGE = 5
@auth.route('/staff', methods=['GET', 'POST'])
@login_required
def staff():
    if current_user.role == 'Admin':
        if request.method == 'POST':
            if request.form.get('formEdit') == 'edit':
                print(request.form)
                data ={}
                data['userName'] = request.form.get('userNamee')
                
                data['name'] = request.form.get('name')
                data['email'] = request.form.get('email')
                data['empID'] = request.form.get('empID')
                data['badgeID'] = request.form.get('badgeID')
                data['depart'] = request.form.get('depart')
                data['role'] = request.form.get('role')
                print(data)
                dataQ = User.query.filter_by(userName=data['userName']).first()
                dataQ.firstName = data['name']
                dataQ.email = data['email']
                dataQ.empID = data['empID']
                dataQ.badgeID = data['badgeID']
                dataQ.depart = data['depart']
                dataQ.role = data['role'] 
                db.session.commit()
                print('okeeeee')
            elif request.form.get('formEdit') == 'editPhoto':
                print(request.form)
                data ={}
                data['userName'] = request.form.get('userNamee')
                data['photo'] = saveB(request.files['photo'])
                
                
                print(data)
                dataQ = User.query.filter_by(userName=data['userName']).first()
                dataQ.photo = data['photo']
                
                db.session.commit()
                print('okeeeee')
            elif request.form.get('formEdit') == 'editPass':
                print(request.form)
                data ={}
                data['userName'] = request.form.get('userNamee')
                data['pass'] = request.form.get('password')
                data['pass1'] = request.form.get('password1')
                
                
                print(data)
                user = User.query.filter_by(userName=data['userName']).first()
                if data['pass'] != data['pass1']:
                    
                    flash('Passwords don\'t match.', category='error')
                else:
                    user.password = password=generate_password_hash(
                    data['pass'], method='sha256')
                    db.session.commit()
                    print('okeeeee')
            else:

                userName = request.form.get('userName')
                password = request.form.get('password')
                password1 = request.form.get('password1')
                name = request.form.get('name')
                email = request.form.get('email')
                empID = request.form.get('empID')
                badgeID = request.form.get('badgeID')
                depart = request.form.get('depart')
                role = request.form.get('role')
                photo = request.files['photo']
                print(request.form)
                print(photo.content_length)

                user = User.query.filter_by(userName=userName).first()
                if user:
                    flash('Username already exists.', category='error')
                elif len(email) < 4:
                    flash('Email must be greater than 3 characters.', category='error')
                elif len(name) < 2:
                    flash('Name must be greater than 1 character.', category='error')
                elif password != password1:
                    flash('Passwords don\'t match.', category='error')
                elif role == '':
                    flash('Role Wajib dipilih.', category='error')
                elif len(empID) < 6:
                    flash('Employee ID must be greater than 3 characters.', category='error')
                elif len(badgeID) < 6:
                    flash('Badge ID must be greater than 3 characters.', category='error')
                elif len(depart) < 2:
                    flash('Department must be greater than 3 characters.', category='error')
                elif photo.content_length == 1:
                    flash('Photo harus diisi', category='error')
                else:
                    photo = saveB(request.files['photo'])
                    new_user = User(userName=userName, firstName=name, email=email,role=role,empID=empID,badgeID=badgeID,depart=depart,photo=photo, password=generate_password_hash(
                    password, method='sha256'))
                    db.session.add(new_user)
                    db.session.commit()
                    flash('Account created!', category='success')
                    return redirect(url_for('auth.staff'))
        
            
        page = request.args.get('page', 1, type=int)
        print(page)
       
        #data = Visitor.query.paginate(page=page, per_page=ROWS_PER_PAGE)
        data = User.query.order_by(text('id desc')).paginate(page=page, per_page=ROWS_PER_PAGE)
        #data.reverse()
        
        return render_template("staff.html", user=current_user,data=data)
    else:
        return render_template("login.html", user=current_user)
#ujiii
@auth.route('/gambar', methods=['GET', 'POST'])
def gambar():
    if request.method == 'POST':
        phname= saveImages(request.files['photo'])
        return('berhasil')
    return render_template("gambar.html", user=current_user)
''''
@auth.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        personID = hik.List.list(current_app.root_path+'/hik/')
        #hik.Delete.delete(current_app.root_path+'/hik/',ok)

        if personID['data']['total'] == 0:
            pass
        else:
            for perid in personID['data']['list']:
                hik.Delete.delete(current_app.root_path+'/hik/',perid['personId'])
                hik.Apply.apply(current_app.root_path+'/hik/')
                print(perid['personId'])
        ok = uploadImages(request.files['photo'])
        
        hik.Add.add(current_app.root_path+'/hik/',ok)
        hik.Apply.apply(current_app.root_path+'/hik/')
        #return(ok)
    else:
        personID = hik.List.list(current_app.root_path+'/hik/')
        #hik.Delete.delete(current_app.root_path+'/hik/',ok)

        if personID['data']['total'] == 0:
            pass
        else:
            for perid in personID['data']['list']:
                hik.Delete.delete(current_app.root_path+'/hik/',perid['personId'])
                hik.Apply.apply(current_app.root_path+'/hik/')
                print(perid['personId'])
    return render_template("gambar.html", user=current_user)
'''

@auth.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        print('tesssssssssssssss')
        data = json.loads(request.data)
        photo= data['photo']
        nama = data['nama']
        personID = hik.List.list(current_app.root_path+'/hik/')
        #hik.Delete.delete(current_app.root_path+'/hik/',ok)

        if personID['data']['total'] == 0:
            pass
        else:
            for perid in personID['data']['list']:
                hik.Delete.delete(current_app.root_path+'/hik/',perid['personId'])
                hik.Apply.apply(current_app.root_path+'/hik/')
                print(perid['personId'])
        
        
        hik.Add.add(current_app.root_path+'/hik/',photo,nama)
        hik.Apply.apply(current_app.root_path+'/hik/')

    return jsonify({})

@auth.route('/sukses', methods=['GET', 'POST'])
def sukses():
    if request.method == 'POST':
        print('tesssssssssssssss')

        data = json.loads(request.data)
        print(data)
        permitId = data['id']

        badge = Badge.query.order_by(id=data['id']).first()
        badge.status = 'used'
        
        transaksi = Transaksi.query.filter_by(id=permitId).first()
        transaksi.namaVisitor = data['namaVisitor']
        transaksi.nik = data['nik']
        transaksi.purpose = data['purpose']
        transaksi.vendor = data['vendor']
        transaksi.host = data['host']
        transaksi.timeCheckin = datetime.datetime.now()
        transaksi.timeCheckot = datetime.datetime.now()
        transaksi.statusPermit = data['statusPermit']
        transaksi.badge = data['badge']
        transaksi.status = data['status']


    
        db.session.commit()
   
        personID = hik.List.list(current_app.root_path+'/hik/')
        #hik.Delete.delete(current_app.root_path+'/hik/',ok)

        if personID['data']['total'] == 0:
            pass
        else:
            for perid in personID['data']['list']:
                hik.Delete.delete(current_app.root_path+'/hik/',perid['personId'])
                hik.Apply.apply(current_app.root_path+'/hik/')
                print(perid['personId'])
        
        

    return jsonify({})


@auth.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':           
        
        print(request.form)
        data ={}
        data['userName'] = request.form.get('userName')
        data['pass'] = request.form.get('password')
        data['pass1'] = request.form.get('password1')
        
        
        print(data)
        user = User.query.filter_by(userName=data['userName']).first()
        if data['pass'] != data['pass1']:
            
            flash('Passwords don\'t match.', category='error')
        else:
            user.password = password=generate_password_hash(
            data['pass'], method='sha256')
            db.session.commit()
            print('okeeeee')
    
            return redirect(url_for('auth.settings'))

    return render_template("settings.html", user=current_user)
