from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Badge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rfid = db.Column(db.String(100))
    status = db.Column(db.String(100))
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100))
    
class Transaksi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timeCheckin = db.Column(db.DateTime, default=func.now())
    timeCheckout = db.Column(db.DateTime, default=func.now())
    badge = db.Column(db.String(150))
    nik = db.Column(db.String(150))
    status = db.Column(db.String(150))

class Permit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subDate = db.Column(db.DateTime())
    namaVendor = db.Column(db.String(150))
    startDate = db.Column(db.DateTime())
    endDate = db.Column(db.DateTime())
    purpose = db.Column(db.String(100))
    location = db.Column(db.String(100))
    supplyBarang = db.Column(db.String(500)) #dict
    permitNo = db.Column(db.String(150))
    desk = db.Column(db.String(150))
    anggota = db.Column(db.String(1000)) #dict
    email = db.Column(db.String(150))
    host = db.Column(db.String(150))
    bawaBarang = db.Column(db.String(150)) #Apakah membawa media penyimpanan?   
    barangBawaan = db.Column(db.String(1000)) #dict
    sign = db.Column(db.Text())
    permitStatus = db.Column(db.String(150))
    statusGenerate = db.Column(db.String(150))
    dataUpload = db.Column(db.Text())

    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    role = db.Column(db.String(150))
    email = db.Column(db.String(150))
    empID = db.Column(db.String(150),unique=True)
    badgeID = db.Column(db.String(150))
    depart = db.Column(db.String(150))
    photo = db.Column(db.Text())
    

class Visitor(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(), default=func.now())
    nik = db.Column(db.String(150),unique=True)
    nama = db.Column(db.String(150))
    namaVendor = db.Column(db.String(150))
    asalVendor = db.Column(db.String(150))
    email = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    jabatan = db.Column(db.String(150))
    photo = db.Column(db.Text())
  
class Covid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nik = db.Column(db.String(150),unique=True)
    nama = db.Column(db.String(150))
    q1 = db.Column(db.String(10))
    q2 = db.Column(db.String(10))
    q3 = db.Column(db.String(10))
    q3b = db.Column(db.String(200)) #link jotform
    q4 = db.Column(db.String(10))
    q5 = db.Column(db.String(10))
    q6 = db.Column(db.String(10))
    sign = db.Column(db.Text())
