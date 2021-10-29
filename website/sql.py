from sqlalchemy import create_engine, select, table, column,text,insert
import requests
import json
import datetime
from PIL import Image, ImageOps
import base64
from io import BytesIO,StringIO
import os 
import secrets

def saveB(photo):
  
    img = Image.open(photo)
    img = ImageOps.exif_transpose(img)
    output_size = (600, 600)
    img.thumbnail(output_size)
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    
    return img_str

def saveImages(nik,photo):
    
    
    pictureFn = nik + ".jpeg"
    picturePath = os.path.join(os.getcwd(),'website/upload/visitor',pictureFn)
    img = Image.open(photo)
    img = ImageOps.exif_transpose(img)
    output_size = (600, 600)
    img.thumbnail(output_size)
    img.save(picturePath)
    return pictureFn



jfToken = '1c003a23731a647ba58829de69911ea8'

def getImage(url):
    r = requests.get(url)
    return saveB(BytesIO(r.content))
    
def delSub(id):
    r = requests.delete(f"https://api.jotform.com/submission/{id}?apiKey={jfToken}")
    print(r.text)

def insertData(data):
    engine = create_engine("mssql+pymssql://sa:Batam2021@10.89.1.50:1433/VMS",future=True)
    with engine.connect() as conn:
        
        conn.execute(
            text("INSERT INTO visitor (date, nik, nama, namaVendor, asalVendor, email, gender, jabatan, photo) VALUES (:date, :nik, :nama, :namaVendor, :asalVendor, :email, :gender, :jabatan,:photo)"),
            data
            )
        conn.commit()
        delSub(data['id'])
        print("inserttttttt")
def updateData(data):
    engine = create_engine("mssql+pymssql://sa:123456@10.89.1.50:1433/VMS",future=True)
    with engine.connect() as conn:
        
        conn.execute(
            text("UPDATE visitor SET date=:date, nik=:nik, nama=:nama, namaVendor=:namaVendor, asalVendor=:asalVendor, email=:email, gender=:gender, jabatan=:jabatan, photo=:photo WHERE nik=:nik"),
            data
            )
        conn.commit()
        delSub(data['id'])
        print('update'+data['nik']+ data['nama'])
def getJFvisitor():
    r = requests.get(f'https://api.jotform.com/form/212702351856453/submissions?apiKey={jfToken}')
    hasil = json.loads(r.text)
    print(hasil)
    
    dictJF = {}
    listJF =[]
    for data in hasil['content']:
        if data['status'] == 'ACTIVE':
            dictJF['id'] = data['id']
            print(dictJF['id'])
            dictJF['date'] = datetime.datetime.now()
            dictJF['nik'] = data['answers']['96']['answer']      
            print(data['answers']['96']['answer'])

            dictJF['nama'] = data['answers']['95']['answer'] 
            print(data['answers']['95']['answer'])
            if data['answers']['115']['answer'] == 'OTHER':

                dictJF['namaVendor'] = data['answers']['20']['answer'] 
            else:
                dictJF['namaVendor'] = data['answers']['115']['answer'] 
            print(data['answers']['115']['answer'])

            dictJF['asalVendor'] = data['answers']['117']['answer'] 
            print(data['answers']['117']['answer'])

            dictJF['email'] = data['answers']['93']['answer'] 
            print(data['answers']['93']['answer'])
            
            dictJF['gender'] = data['answers']['97']['answer'] 
            print(data['answers']['97']['answer'])

            dictJF['jabatan'] = data['answers']['98']['answer'] 
            print(data['answers']['98']['answer'])
            

            dictJF['photo'] = getImage(data['answers']['100']['answer'])
            print(data['answers']['100']['answer'])
            print('============================')
            listJF.append(dictJF.copy())

            try:
                insertData(dictJF)
            except:
                updateData(dictJF)
             
            
           
            
            
    #listJF.reverse()  
    #for hasil in listJF:
        
        #updateData(hasil)


getJFvisitor()





'''

    nik = db.Column(db.String(150),unique=True)
    nama = db.Column(db.String(150))
    namaVendor = db.Column(db.String(150))
    asalVendor = db.Column(db.String(150))
    email = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    jabatan = db.Column(db.String(150))
    photo = db.Column(db.String(250))

  '''