import datetime


jf = '09/19/18 13:55'
waktu = datetime.datetime.strptime(jf, '%m/%d/%y %H:%M')

print(waktu)

jf = '8-11-2221 13:0'
waktu = datetime.datetime.strptime(jf, '%m-%d-%Y %H:%M')

print(waktu)