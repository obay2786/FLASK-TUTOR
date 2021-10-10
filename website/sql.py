from sqlalchemy import create_engine
import pandas as pd
import pyodbc
server = "10.89.1.50"
database = "VMS"
driver = "ODBC Driver 17 for SQL Server"


engine = create_engine('mssql+pymssql://sa:123456@10.89.1.50:1433/VMS')

conn = engine.connect()
data = pd.read_sql_query("SELECT cobaTransaksi.idTransaksi, cobaTransaksi.kegiatan, cobaUser.nama FROM cobaTransaksi INNER JOIN cobaUser ON cobaTransaksi.idPerson = cobaUser.idPerson; ",conn)

print(data)