import subprocess
import requests

baseUrl = 'https://10.89.1.7'
class Add:
  @staticmethod 
  def add(path,photo):


      url = '/artemis/api/resource/v1/person/single/add'
     
      p = subprocess.Popen(['node',path +'add.js'], stdout=subprocess.PIPE)
      hasilList = []
      for i in range(8):
        hasilList.append(p.stdout.readline().decode('utf-8').rstrip('\n'))

      message = "".join(hasilList[0:7])

      signature = hasilList[7]
      print(message)
      print(signature)


      headers ={
              'Accept':'*/*',
            'Content-Type':'application/json',
            'x-ca-timestamp': hasilList[5][15:],
            'x-ca-nonce':hasilList[4][11:],
            'x-ca-key':hasilList[3][9:],
            'x-ca-signature-headers':'x-ca-key,x-ca-nonce,x-ca-timestamp',
            'x-ca-signature':signature
          }





      data = {
          "personCode": "213123",
          "personFamilyName": "subi",
          "personGivenName": "darma",
          "gender": 1,
          "orgIndexCode": "1",
          "remark": "Grunge",
          "phoneNo": "123456",
          "email": "novel@qq.com",
          "faces": [
              {
                  "faceData": photo
              }
          ],
          "beginTime": "2020-05-26T15:00:00+08:00",
          "endTime": "2030-05-26T15:00:00+08:00"
      }

      r = requests.post(baseUrl+url,json=data,headers=headers,verify=False)
      print(headers)
      print(r.content.decode('utf-8'))

 