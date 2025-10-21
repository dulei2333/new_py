import time

import execjs
import requests


def get_Signature(page):
    with open('11-广东交易平台 - Interceptor拦截器.js',encoding='utf-8-sig')as f:
        js_code = f.read()
    signature = execjs.compile(js_code).call('Signature',page,times)
    return signature

def get_content(signature,page):
    url = 'https://ygp.gdzwfw.gov.cn/ggzy-portal/search/v2/items'
    headers = {
        'content-type':'application/json',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
        'x-dgi-req-app':'ggzy-portal',
        'x-dgi-req-nonce':'pitokhnQdY5G5E6H',
        'x-dgi-req-signature':signature,
        'x-dgi-req-timestamp':str(times),

    }

    data = {
        "type": "trading-type",
        "openConvert": False,
        "keyword": "",
        "siteCode": "44",
        "secondType": "A",
        "tradingProcess": "",
        "thirdType": "[]",
        "projectType": "",
        "publishStartTime": "",
        "publishEndTime": "",
        "pageNo": page,
        "pageSize": 10
    }
    pageData = requests.post(url, headers=headers, json=data).json()['data']['pageData']
    for item in pageData:
        print(item['noticeTitle'])

if __name__ == '__main__':
    for page in range(1,10):
        times = int(time.time() * 1000)
        signature = get_Signature(page)
        get_content(signature,page)
