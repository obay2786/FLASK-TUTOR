from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(8000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Transaksi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timeCheckin = db.Column(db.DateTime(timezone=True), default=func.now())
    timeCheckout = db.Column(db.DateTime(timezone=True), default=func.now())
    badge = db.Column(db.String(150))
    nik = db.Column(db.String(150))
    status = db.Column(db.String(150))

class Permit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subDate = db.Column(db.DateTime(timezone=True))
    namaVendor = db.Column(db.String(150))
    startDate = db.Column(db.DateTime(timezone=True))
    endDate = db.Column(db.DateTime(timezone=True))
    purpose = db.Column(db.String(100))
    location = db.Column(db.String(100))
    supplyBarang = db.Column(db.String(500)) #dict
    permitNo = db.Column(db.String(150))
    desk = db.Column(db.String(150))
    anggota = db.Column(db.String(1000)) #dict
    email = db.Column(db.String(150))
    host = db.Column(db.String(150))
    bawaBarang = db.Column(db.String(150)) #Apakah membawa media penyimpanan?   
    barangBawaan = db.Column(db.String(500)) #dict
    sign = db.Column(db.Text())
    

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
    notes = db.relationship('Note')

class Visitor(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
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
    nama = db.Column(db.String(150),unique=True)
    q1 = db.Column(db.String(10),unique=True)
    q2 = db.Column(db.String(10),unique=True)
    q3 = db.Column(db.String(10),unique=True)
    q3b = db.Column(db.String(200),unique=True) #link jotform
    q4 = db.Column(db.String(10),unique=True)
    q5 = db.Column(db.String(10),unique=True)
    q6 = db.Column(db.String(10),unique=True)
