# -*- coding: utf-8 -*-
import json
from flask import Flask
import requests


app = Flask(__name__)


def get_wc_msg():
    url = 'http://127.0.0.1:8123/api/states'
    headers = {
        'content-type': 'application/json',
        'X-HA-Access': 'guokr.com',
    }
    response = requests.get(url, headers=headers)
    msg = json.loads(response.text)

    r = {}
    tran = {'on': 'off', 'off': 'on'}

    tran_2 = {'on': u"使用中", 'off': u"空闲"}
    for i in msg:
        if i['attributes'].get('friendly_name') == 'MaleWC_1':
            r[u"男厕所1"] = tran.get(i['state'], 'off')
        if i['attributes'].get('friendly_name') == 'MaleWC_2':
            r[u"男厕所2"] = i['state']
    rep = {key: tran_2.get(r.get(key), u'使用中') for key in r.keys()}
    return rep


@app.route('/')
def hello_world():
    response = get_wc_msg()
    count = 0
    return response, 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
