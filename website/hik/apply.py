import subprocess
import requests



class Apply:
  @staticmethod 
  def apply():
    baseUrl = 'https://10.89.1.7'


    url = '/artemis/api/visitor/v1/auth/reapplication'
    p = subprocess.Popen(['node', 'apply.js'], stdout=subprocess.PIPE)
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
        
    }

    r = requests.post(baseUrl+url,json=data,headers=headers,verify=False)
    print(headers)
    print(r.content.decode('utf-8'))
