import subprocess
import requests


class List:
  @staticmethod 
  def list(path):
      baseUrl = 'https://192.168.100.20'


      url = '/artemis/api/resource/v1/person/personList'
     
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
          
    "pageNo": 1,
    "pageSize": 6
}
      

      r = requests.post(baseUrl+url,json=data,headers=headers,verify=False)
      print(headers)
      print(r.content.decode('utf-8'))

 