from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(8000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


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