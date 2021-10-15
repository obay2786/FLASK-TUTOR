import subprocess
import requests
from apply import Apply
baseUrl = 'https://10.89.1.7'

class Delete:
  @staticmethod 
  def delete(path,id):
      url = '/artemis/api/resource/v1/person/single/delete'
      p = subprocess.Popen(['node', 'delete.js'], stdout=subprocess.PIPE)
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
          "personId": id
      }
      l = requests.post(baseUrl+url,json=data,headers=headers,verify=False)
      r = requests.post(baseUrl+url,json=data,headers=headers,verify=False)
      print(headers)
      print(r.content.decode('utf-8'))

      Apply.apply()