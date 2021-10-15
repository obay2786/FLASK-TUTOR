from flask import Blueprint, render_template, request, flash, redirect, url_for,current_app
import secrets
import os
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from PIL import Image, ImageOps
import base64
from io import BytesIO
from .hik import hik
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
    img.save(buffered, format="JPEG")
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

#ujiii
@auth.route('/gambar', methods=['GET', 'POST'])
def gambar():
    if request.method == 'POST':
        phname= saveImages(request.files['photo'])
        return('berhasil')
    return render_template("gambar.html", user=current_user)

@auth.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        ok = uploadImages(request.files['photo'])
        
        hik.Add.add(current_app.root_path+'/hik/',ok)
        
        #return(ok)
    else:
        personID = hik.List.list(current_app.root_path+'/hik/')
        #hik.Delete.delete(current_app.root_path+'/hik/',ok)
        
        if personID['data']['total'] == 0:
            pass
        else:
            for perid in personID['data']['list']:
                hik.Delete.delete(current_app.root_path+'/hik/',perid['personId'])
                print(perid['personId'])
    return render_template("gambar.html", user=current_user)