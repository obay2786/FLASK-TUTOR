user = [{"nama":"novel","nik":"1223"},{"nama":"frs","nik":"sds3"}]

#cara 1
hasil = [[k['nama'],k['nik']] for k in user]
#cara 2
hasil2 = [[k for k in k.values()] for k in user]

print(hasil)
print(hasil2)
