import datetime
import smtplib

def kirim():
    gmail_user = 'info@siberkolosis.com'
    gmail_password = 'grunge75'

    sent_from = gmail_user
    to = ['blgr182@gmail.com', 'awnzky@gmail.com']
    subject = 'Lorem ipsum dolor sit amet'
    body = 'consectetur adipiscing elit'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('mail.privateemail.com', 465)
        smtp_server.ehlo()
        # smtp_server.starttls()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)


# kirim()





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

# hasil = set()
# sumber = {21:'Personal Computer / Laptop',22:'Camera (Digital or analogue)',23:'Mobilephone with camera / video',24:'Tablet with camera / video',25:'Digital Video Recorder',26:'Thumbdrive / Pendrive storage unit',27:'Memory Cards (SD/CF/MMC etc.)',28:'Audio Tape Recorder',29:'CDRW / CDR / HDD',30:'Others (pls state)'}
# banding = ["Thumbdrive / Pendrive storage unit",'Camera (Digital or analogue)','Camera (Digital or analogue)']
# for b in banding:
#     for key, value in sumber.items():
#             if b == value:
#                 hasil.add(key)
#                 # print(key)
# # print(hasil)

# datas = ["a","b","c","d"]

# for i in range(3,7):
# 	x = dict.fromkeys(str(i),datas[i-3])
# 	print(x)
# # 	

def qrGen(id,nik,nama):
    qr = f'https://chart.apis.google.com/chart?chl={id}:{nik}&chs=150x150&cht=qr&chld=H%7C0'
    
    return {nama:qr}

anggota = [{"Nama": "Novel", "Jabatan": "Komisaris", "NIK": "83423849028", "Register": "tidak", "Covid": "tidak"},{"Nama": "Novel", "Jabatan": "Komisaris", "NIK": "83423849028", "Register": "tidak", "Covid": "tidak"},{"Nama": "Novel", "Jabatan": "Komisaris", "NIK": "83423849028", "Register": "tidak", "Covid": "tidak"},{"Nama": "Novel", "Jabatan": "Komisaris", "NIK": "83423849028", "Register": "tidak", "Covid": "tidak"},{"Nama": "Novel", "Jabatan": "Komisaris", "NIK": "83423849028", "Register": "tidak", "Covid": "tidak"},{"Nama": "Novel", "Jabatan": "Komisaris", "NIK": "83423849028", "Register": "tidak", "Covid": "tidak"},{"Nama": "Novel", "Jabatan": "Komisaris", "NIK": "83423849028", "Register": "tidak", "Covid": "tidak"},{"Nama": "Novel", "Jabatan": "Komisaris", "NIK": "83423849028", "Register": "tidak", "Covid": "tidak"},{"Nama": "Novel", "Jabatan": "Komisaris", "NIK": "83423849028", "Register": "tidak", "Covid": "tidak"},{"Nama": "Novel", "Jabatan": "Komisaris", "NIK": "83423849028", "Register": "tidak", "Covid": "tidak"}, {"Nama": "Faris", "Jabatan": "Manager", "NIK": "982982897873", "Register": "tidak", "Covid": "tidak"}]
listQR =[]
for person in anggota:
    listQR.append(qrGen('124',person['NIK'],person['Nama']))


tableQR = []
    
for QR in listQR:
    for key in QR:
        tableQR.append(f"""<td class="column" style="mso-table-lspace:0;mso-table-rspace:0;font-weight:400;text-align:left;vertical-align:top;border-bottom:2px solid #fff;border-left:2px solid #fff;border-right:2px solid #fff;border-top:2px solid #fff" width="33.333333333333336%">
                                                <table class="image_block" role="presentation" style="mso-table-lspace:0;mso-table-rspace:0" width="100%" cellspacing="0" cellpadding="0" border="0">
                                                    <tbody><tr>
                                                        <td style="width:100%;padding-right:0;padding-left:0;padding-top:5px">
                                                            <div style="line-height:10px" align="center"><img src="{QR[key]}" style="display:block;height:auto;border:0;width:183px;max-width:100%" alt="Hospital Icon" title="Hospital Icon" width="183"></div>
                                                        </td>
                                                    </tr>
                                                </tbody></table>
                                                <table class="text_block" role="presentation" style="mso-table-lspace:0;mso-table-rspace:0;word-break:break-word" width="100%" cellspacing="0" cellpadding="10" border="0">
                                                    <tbody><tr>
                                                        <td>
                                                            <div style="font-family:Tahoma,Verdana,sans-serif">
                                                                <div style="font-size:12px;font-family:Lato,Tahoma,Verdana,Segoe,sans-serif;mso-line-height-alt:14.399999999999999px;color:#087200;line-height:1.2">
                                                                    <p style="margin:0;font-size:16px;text-align:center">
                                                                        <strong>{key}</strong></p>
                                                                </div>
                                                            </div>
                                                        </td>
                                                    </tr>
                                                </tbody></table>
                                                <table class="divider_block" role="presentation" style="mso-table-lspace:0;mso-table-rspace:0" width="100%" cellspacing="0" cellpadding="10" border="0">
                                                    <tbody><tr>
                                                        <td>
                                                            <div align="center">
                                                                <table role="presentation" style="mso-table-lspace:0;mso-table-rspace:0" width="100%" cellspacing="0" cellpadding="0" border="0">
                                                                    <tbody><tr>
                                                                        <td class="divider_inner" style="font-size:1px;line-height:1px;border-top:1px solid #bbb">
                                                                            <span> </span></td>
                                                                    </tr>
                                                                </tbody></table>
                                                            </div>
                                                        </td>
                                                    </tr>
                                                </tbody></table>
                                                <table class="text_block" role="presentation" style="mso-table-lspace:0;mso-table-rspace:0;word-break:break-word" width="100%" cellspacing="0" cellpadding="0" border="0">
                                                    <tbody><tr>
                                                        <td style="padding-bottom:15px;padding-left:10px;padding-right:10px;padding-top:10px">
                                                            <div style="font-family:Tahoma,Verdana,sans-serif">
                                                                <div style="font-size:12px;font-family:Lato,Tahoma,Verdana,Segoe,sans-serif;mso-line-height-alt:18px;color:#000;line-height:1.5">
                                                                    <p style="margin:0;font-size:14px;text-align:center;mso-line-height-alt:24px">
                                                                        <span style="font-size:16px">Lorem ipsum
                                                                            dolor sit amet,</span><br><span style="font-size:16px">consectetur
                                                                            adipiscing elit</span></p>
                                                                </div>
                                                            </div>
                                                        </td>
                                                    </tr>
                                                </tbody></table>
                                            </td>""")
#print(tableQR[0])
rowPertama = ''
rowKedua = ''
rowKetiga = ''
rowKeempat = ''
rowKelima = ''
rowKeenam = ''
rowKetujuh = ''

listQrMail = []
for t in range(len(tableQR)):
    if t < 3:
        rowPertama += tableQR[t]
        
    elif t < 6:
        rowKedua += tableQR[t]
    elif t < 9:
        rowKetiga += tableQR[t]
    elif t < 12:
        rowKeempat += tableQR[t]
    elif t < 15:
        rowKelima += tableQR[t]
    elif t < 18:
        rowKeenam += tableQR[t]
    else:
        rowKetujuh += tableQR[t]

#print(rowPertama)
tableRow =[rowPertama,rowKedua,rowKetiga,rowKeempat,rowKelima,rowKeenam,rowKetujuh]
tableRowFinish = []
for i in tableRow:
    tableRowFinish.append(f"""<table class="row row-4" role="presentation" style="mso-table-lspace:0;mso-table-rspace:0" width="100%" cellspacing="0" cellpadding="0" border="0" align="center">
                            <tbody>
                                <tr>
                                    <td>
                                        <table class="row-content stack" role="presentation" style="mso-table-lspace:0;mso-table-rspace:0;background-color:#fff;color:#000;width:680px" width="680" cellspacing="0" cellpadding="0" border="0" align="center">
                                            <tbody>
                                                <tr>
                                                {i}
                                                </tr>
                                            </tbody>
                                            
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>""")

print("".join(tableRowFinish))