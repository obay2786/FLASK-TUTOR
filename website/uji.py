import datetime


# jf = '09/19/18 13:55'
# waktu = datetime.datetime.strptime(jf, '%m/%d/%y %H:%M')

# print(waktu)

# jf = '8-11-2221 13:0'
# waktu = datetime.datetime.strptime(jf, '%m-%d-%Y %H:%M')

# print(waktu)


# sumber = {1:"laptop",2:"hp",3:"tablet",4:"kamera"}
# banding = ["laptop", "kamera"]

# data = []
# for i in sumber:
# 	for j in banding:
# 		data.append(sumber[i])
# 		# x = data.index(j)
# 		# print(x)


# sumber = {1:"laptop",2:"hp",3:"tablet",4:"kamera"}
# banding = ["laptop", "kamera"]

# for b in banding:
#   x = list(sumber.keys())[list(sumber.values()).index(b)]
#   print(x)

hasil = set()
sumber = {21:'Personal Computer / Laptop',22:'Camera (Digital or analogue)',23:'Mobilephone with camera / video',24:'Tablet with camera / video',25:'Digital Video Recorder',26:'Thumbdrive / Pendrive storage unit',27:'Memory Cards (SD/CF/MMC etc.)',28:'Audio Tape Recorder',29:'CDRW / CDR / HDD',30:'Others (pls state)'}
banding = ["Thumbdrive / Pendrive storage unit",'Camera (Digital or analogue)','Camera (Digital or analogue)']
for b in banding:
    for key, value in sumber.items():
            if b == value:
                hasil.add(key)
                # print(key)
# print(hasil)

datas = ["a","b","c","d"]

for i in range(3,7):
	x = dict.fromkeys(str(i),datas[i-3])
	print(x)
# 	