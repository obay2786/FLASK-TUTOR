process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';

const crypto = require('crypto');
const https = require('https');
const uuid = require('uuid');
const axios = require('axios');

class HikOpenapi {
  constructor({ baseUrl, appKey, appSecret, debug = false }) {
    this.baseUrl = baseUrl;
    this.appKey = appKey;
    this.appSecret = appSecret;
    this.debug = debug;
  }

  post(url, data) {
    const timestamp = new Date().valueOf();
    const uid = uuid.v4();
    const message = `POST
*/*
application/json
x-ca-key:${this.appKey}
x-ca-nonce:${uid}
x-ca-timestamp:${timestamp}
${url}`;

    const signature = crypto.createHmac('sha256', this.appSecret).update(message, 'utf8').digest('base64');

    const headers = {
      Accept: '*/*',
      'Content-Type': 'application/json',
      'x-ca-timestamp': timestamp,
      'x-ca-nonce': uid,
      'x-ca-key': this.appKey,
      'x-ca-signature-headers': 'x-ca-key,x-ca-nonce,x-ca-timestamp',
      'x-ca-signature': signature
    };

    const agent = new https.Agent({
      rejectUnauthorized: false
    });

    if (this.debug) {
      log('message', message);
      log('signature', signature);
      //log('header', JSON.stringify(headers));
    }

    /*return axios.post(this.baseUrl + url, data, {
      headers,
      timeout: 5 * 1000,
      httpsAgent: agent
    });*/
    return 0
  }
};

function log(label, data) {
  //console.log('==========' + label + '==========');
  console.log(data);
  //console.log('==========' + label + '==========');
  //console.log('\n');
}


const appKey = '24020018';
const appSecret = '0iQIxRvSrg3KtVoZN2Ow';
const baseUrl = 'https://10.89.1.7';
const openApi = new HikOpenapi({ appKey, appSecret, baseUrl, debug: true});
process.env["NODE_TLS_REJECT_UNAUTHORIZED"] = 1;

const apiUrl = '/artemis/api/resource/v1/person/single/delete';
const postData = {
};
openApi.post(apiUrl, postData)
