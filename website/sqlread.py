import sqlalchemy as db
import json


dbpana = "mssql+pymssql://sa:Batam2021@103.142.240.134:1433/VMS"

def readsql():
    engine = db.create_engine(dbpana)
    connection = engine.connect()
    metadata = db.MetaData()
    census = db.Table('permit', metadata, autoload=True, autoload_with=engine)

    #Equivalent to 'SELECT * FROM census'
    query = db.select([census])

    ResultProxy = connection.execute(query)

    ResultSet = ResultProxy.fetchall()


    dictDb = {}
    listDb =[]
    for i in ResultSet:
        dictDb['no'] = list(i)[0]


        dictDb['subDate'] = list(i)[1]

        dictDb['namaVendor'] = list(i)[2]
        dictDb['startDate'] = list(i)[3]
        dictDb['endDate'] = list(i)[4]
        dictDb['purpose'] = list(i)[5]
        dictDb['location'] = list(i)[6]
        dictDb['supplyBarang'] = list(i)[7]
        dictDb['permitNo'] = list(i)[8]
        dictDb['desk'] = list(i)[9]
        dictDb['anggota'] = list(i)[10]
        dictDb['email'] = list(i)[11]
        dictDb['barangBawaan'] = list(i)[12]
        dictDb['sign'] = list(i)[13]




        listDb.append(dictDb.copy())

    print(listDb)



def findDatapermit(cari):
    engine = db.create_engine(dbpana)
    connection = engine.connect()
    metadata = db.MetaData()
    census = db.Table('permit', metadata, autoload=True, autoload_with=engine)

    #Equivalent to 'SELECT * FROM census'
    query = db.select([census])

    ResultProxy = connection.execute(query)

    ResultSet = ResultProxy.fetchall()
    permitNo = []
    for i in ResultSet:
        permitNo.append(i[8])
    noData = permitNo.index(cari)

    print(list(ResultSet[noData]))

# readsql()

findDatapermit('545466791')

