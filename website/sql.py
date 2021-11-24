from sqlalchemy import create_engine, select, table, column,text,insert
import requests
import json
import datetime
from PIL import Image, ImageOps
import base64
from io import BytesIO,StringIO
import os 
import secrets

engineLocal = create_engine("mssql+pymssql://sa:Batam2021@103.142.240.134:1433/VMS",future=True)
# proxypana = '10.77.8.70:8080'
prox = {"http":"http://47.74.152.29:8888"}



def saveB(photo):
  
    img = Image.open(photo)
    img = ImageOps.exif_transpose(img)
    output_size = (600, 600)
    img.thumbnail(output_size)
    buffered = BytesIO()
    # img.save(buffered, format="JPEG")
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue())
    
    return img_str
'''
def saveImages(nik,photo):
    
    
    pictureFn = nik + ".jpeg"
    picturePath = os.path.join(os.getcwd(),'website/upload/visitor',pictureFn)
    img = Image.open(photo)
    img = ImageOps.exif_transpose(img)
    output_size = (600, 600)
    img.thumbnail(output_size)
    img.save(picturePath)
    return pictureFn
'''


jfToken = '75f10c2850b81307489bac1d4fc7ad54'

def getImage(url):
    r = requests.get(url)
    return saveB(BytesIO(r.content))
    
def delSub(id):
    # r = requests.delete(f"https://api.jotform.com/submission/{id}?apiKey={jfToken}")
    r = requests.delete(f"https://api.jotform.com/submission/{id}?apiKey={jfToken}",proxies=prox)
    print(r.text)

def insertData(data):
    engine = engineLocal
    with engine.connect() as conn:
        
        conn.execute(
            text("INSERT INTO visitor (date, nik, nama, namaVendor, asalVendor, email, gender, jabatan, photo) VALUES (:date, :nik, :nama, :namaVendor, :asalVendor, :email, :gender, :jabatan,:photo)"),
            data
            )
        conn.commit()
        # delSub(data['id'])
        print("visitor inserted")


def updateData(data):
    engine = engineLocal
    with engine.connect() as conn:
        
        conn.execute(
            text("UPDATE visitor SET date=:date, nik=:nik, nama=:nama, namaVendor=:namaVendor, asalVendor=:asalVendor, email=:email, gender=:gender, jabatan=:jabatan, photo=:photo WHERE nik=:nik"),
            data
            )
        conn.commit()
        # delSub(data['id'])
        print('update'+data['nik']+ data['nama'])

def insertPermit(data):
    engine = engineLocal
    with engine.connect() as conn:
        
        conn.execute(
            text("INSERT INTO permit (subDate, namaVendor, startDate, endDate, purpose, location, supplyBarang, permitNo, desk, anggota, email, host, bawaBarang, barangBawaan, sign, status) VALUES (:subDate, :namaVendor, :startDate, :endDate, :purpose, :location, :supplyBarang, :permitNo,:desk,:anggota,:email,:host,:bawaBarang,:barangBawaan,:sign, :status)"),
            data
            )
        conn.commit()
        # delSub(data['id'])
        print("permit inserted")

def insertCovid(data):
    engine = engineLocal
    with engine.connect() as conn:
        
        conn.execute(
            text("INSERT INTO covid (nik, nama, q1, q2, q3, q3b, q4, q5 , q6, sign ) VALUES (:nik, :nama, :q1, :q2, :q3, :q3b, :q4, :q5 , :q6, :sign)"),
            data
            )
        conn.commit()
        # delSub(data['id'])
        print("data inserted")

def updateCovid(data):
    engine = engineLocal
    with engine.connect() as conn:
        
        conn.execute(
            text("UPDATE covid SET nik=:nik, nama=:nama, q1=:q1, q2=:q2, q3=:q3, q3b=:q3b, q4=:q4, q5=:q5, q6=:q6, sign=:sign WHERE nik=:nik"),
            data
            )
        conn.commit()
        # delSub(data['id'])
        print('update '+data['nik']+" : "+ data['nama'])

def insertTransaksi():
    engine = engineLocal
    with engine.connect() as conn:
        
        conn.execute(
            text("INSERT INTO transaksi (timeCheckin, timeCheckout, badge, nik, status ) VALUES (:timeCheckin, :timeCheckout, :badge, :nik, :status)"),
            data
            )
        conn.commit()
        # delSub(data['id'])
        print("data Transaksi inserted")


def getJFvisitor():
    r = requests.get(f'https://api.jotform.com/form/213273805198460/submissions?apiKey={jfToken}',proxies=prox)
    hasil = json.loads(r.text)
    print(hasil)
    
    dictJF = {}
    listJF =[]
    for data in hasil['content']:
        if data['status'] == 'ACTIVE':
            dictJF['id'] = data['id']
    
            dictJF['date'] = datetime.datetime.now()
            
            dictJF['nik'] = data['answers']['96']['answer']      

            dictJF['nama'] = data['answers']['95']['answer'] 

            if data['answers']['115']['answer'] == 'OTHER':
                dictJF['namaVendor'] = data['answers']['20']['answer'] 
            else:
                dictJF['namaVendor'] = data['answers']['115']['answer'] 


            dictJF['asalVendor'] = data['answers']['117']['answer'] 
 

            dictJF['email'] = data['answers']['93']['answer'] 

            
            dictJF['gender'] = data['answers']['97']['answer'] 


            dictJF['jabatan'] = data['answers']['98']['answer'] 
          

            dictJF['photo'] = getImage(data['answers']['100']['answer'])

            listJF.append(dictJF.copy())

            try:
                insertData(dictJF)
            # except Exception as e:
            #     print(e)
            except:
                updateData(dictJF)
             

            
def getJFpermit():
    r = requests.get(f'https://api.jotform.com/form/213273981895469/submissions?apiKey={jfToken}')
    hasil = json.loads(r.text)
    dictJF = {}
    listJF =[]

    for data in hasil["content"]:
        if data['status'] == 'ACTIVE':
            dictJF['id'] = data['id']

            dictJF['subDate'] = data['created_at']
            
            if data['answers']['59']['answer'] == 'WORKING' or data['answers']['59']['answer'] == 'OVERTIME':
                dictJF['permitNo'] = data['answers']['15']['answer'] 
                dictJF['desk'] = data['answers']['16']['answer'] 
            else:
                dictJF['permitNo'] = ""
                dictJF['desk'] = ""

            dictJF['email'] = data['answers']['28']['answer'] 

            dictJF['startDate'] = datetime.datetime.strptime(data['answers']['46']['prettyFormat'], '%d-%m-%Y %H:%M') 

            dictJF['sign'] = data['answers']['47']['answer'] 

            anggota = json.loads(data['answers']['51']['answer'])

            listAnggota = []
            for a in anggota:
                
                dataDbVisitor = getDbVisitor(a['NIK'])
                if "nik" in dataDbVisitor:
                    a['Register'] = 'ya'
                # if a['NIK'] == dataDbVisitor['nik']:
                else:
                    a['Register'] = 'tidak'
                
                dataDbCovid = getDbCovid(a['NIK'])
                if "nik" in dataDbCovid:
                    a['Covid'] = 'ya'
                # if a['NIK'] == dataDbVisitor['nik']:
                else:
                    a['Covid'] = 'tidak'

                listAnggota.append(a)

            dictJF['anggota'] = json.dumps(listAnggota)

            dictJF['bawaBarang'] = data['answers']['54']['answer'] 

            if data['answers']['54']['answer'] == "YA":
                dictJF['barangBawaan'] = data['answers']['55']['answer'] 
            else:
                dictJF['barangBawaan'] = ""

            dictJF['endDate'] = datetime.datetime.strptime(data['answers']['56']['prettyFormat'], '%d-%m-%Y %H:%M') #data['answers']['56']['prettyFormat'] 

            dictJF['purpose'] = data['answers']['59']['answer'] 

            dictJF['namaVendor'] = data['answers']['63']['answer'] 
            
            dictJF['host'] = []
            namaHost = data['answers']['66']['answer']
            EmpId = data['answers']['71']['answer']
            host = f"{namaHost}:{EmpId}"
            dictJF['host'] = host

            if data['answers']['59']['answer'] == 'SUPPLY':
                dictJF['location'] = data['answers']['64']['answer']
                dictJF['supplyBarang'] = data['answers']['65']['answer']
                dictJF['status'] = "approved" 
            elif data['answers']['59']['answer'] == 'MEETING':
                dictJF['status'] = "waitinghost"
                dictJF['location'] = ""
                dictJF['supplyBarang'] = ''
            else:               
                dictJF['status'] = "waitingadmin"
                dictJF['location'] = ""
                dictJF['supplyBarang'] = ''


            insertPermit(dictJF)
           
            
      
def getJFcovid():
    r = requests.get(f'https://api.jotform.com/form/213274129635456/submissions?apiKey={jfToken}')
    hasil = json.loads(r.text)
    
    dictJF = {}
    listJF =[]
    for data in hasil["content"]:
        if data['status'] == 'ACTIVE':
            dictJF['id'] = data['id']
            
            dictJF['nama'] = data['answers']['2']['answer'] 
            
            dictJF['nik'] = data['answers']['3']['answer'] 

            dictJF['q1'] = data['answers']['23']['answer'] 

            dictJF['q2'] = data['answers']['24']['answer'] 
            
            dictJF['q3'] = data['answers']['25']['answer'] 

            if data['answers']['25']['answer']  == "YA":
                dictJF['q3b'] = data['answers']['16']['answer']
            else:
                dictJF['q3b'] = ""
            
            dictJF['q4'] = data['answers']['26']['answer'] 
            
            dictJF['q5'] = data['answers']['27']['answer'] 
            
            dictJF['q6'] = data['answers']['28']['answer']

            dictJF['sign'] = data['answers']['15']['answer'] 

            try:
                insertCovid(dictJF)
            #except Exception as e:
                #print(e)
            except:
                updateCovid(dictJF)
            
            
            # listJF.append(dictJF.copy())

    # print(listJF)

    

def getDbVisitor(nik):
    nikVisitor = {}
    engine = engineLocal
    with engine.connect() as conn:
        
        hasil = conn.execute(text(f"SELECT nik FROM visitor WHERE nik='{nik}'"))

        for h in hasil:
            nikVisitor = dict(h)

    return nikVisitor

def getDbCovid(nik):
    nikVisitor = {}
    engine = engineLocal
    with engine.connect() as conn:
        
        hasil = conn.execute(text(f"SELECT nik FROM covid WHERE nik='{nik}'"))

        for h in hasil:
            nikVisitor = dict(h)

    return nikVisitor
            


# getJFvisitor()

getJFcovid()

# getJFpermit()


