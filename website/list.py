from sqlalchemy import create_engine, select, table, column,text,insert
import requests
import json
import datetime

jfToken = '1c003a23731a647ba58829de69911ea8'
r = requests.get(f'https://api.jotform.com/form/212702351856453/submissions?apiKey={jfToken}')
hasil = json.loads(r.text)
print(hasil)

def insertData(data):
    engine = create_engine("mssql+pymssql://sa:123456@10.89.1.50:1433/VMS",future=True)
    with engine.connect() as conn:
    
        conn.execute(
            text("INSERT INTO visitor (date, nik, nama, namaVendor, asalVendor, email, gender, jabatan, photo) VALUES (:date, :nik, :nama, :namaVendor, :asalVendor, :email, :gender, :jabatan, :photo)"),
            data
            )
        conn.commit()


listJF = []
dictJF = {}
for data in hasil['content']:
    if data['status'] == 'ACTIVE':
        
        dictJF['date'] = datetime.datetime.now()
        dictJF['nik'] = data['answers']['96']['answer']      
        print(data['answers']['96']['answer'])

        dictJF['nama'] = data['answers']['95']['answer'] 
        print(data['answers']['95']['answer'])

        dictJF['namaVendor'] = data['answers']['20']['answer'] 
        print(data['answers']['20']['answer'])

        dictJF['asalVendor'] = data['answers']['21']['answer'] 
        print(data['answers']['21']['answer'])

        dictJF['email'] = data['answers']['93']['answer'] 
        print(data['answers']['93']['answer'])
        
        dictJF['gender'] = data['answers']['97']['answer'] 
        print(data['answers']['97']['answer'])

        dictJF['jabatan'] = data['answers']['98']['answer'] 
        print(data['answers']['98']['answer'])

        dictJF['photo'] = data['answers']['100']['answer'] 
        print(data['answers']['100']['answer'])
        print('============================')

        listJF.append(dictJF) 
        
        print(dictJF)
        print('============================')
print(listJF)
print('============================')
print(dictJF)





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