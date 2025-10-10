import requests
import json
import execjs


def get_js_code(page):
    with open('3-优志愿.js', 'r', encoding='utf-8-sig') as f:
        js_code = f.read()
    t = {
        "keyword": "",
        "provinceNames": [],
        "natureTypes": [],
        "eduLevel": "",
        "categories": [],
        "features": [],
        "pageIndex": page,
        "pageSize": 20,
        "sort": 11
    }
    key = execjs.compile(js_code).call("get_sign", t)
    print(key)
    return key

name_list = []
def daxue(page, key):
    headers = {
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://pv4y-pc.youzy.cn",
        "Pragma": "no-cache",
        "Referer": "https://pv4y-pc.youzy.cn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
        "agent": "objectId:;provinceId:;provinceCode:;userPermissionId:;score:0;",
        "deviceId": "c7e1db7a76009e36521d4277169dbe27",
        "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Google Chrome\";v=\"140\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "u-sign": key,
        "u-token;": ""
    }
    url = "https://uwf7de983aad7a717eb.youzy.cn/youzy.dms.basiclib.api.college.query"
    data = {
        "keyword": "",
        "provinceNames": [],
        "natureTypes": [],
        "eduLevel": "",
        "categories": [],
        "features": [],
        "pageIndex": page,
        "pageSize": 20,
        "sort": 11
    }
    data = json.dumps(data, separators=(',', ':'))
    items = requests.post(url, headers=headers, data=data).json()['result']['items']
    for item in items:
        # cnName = item['cnName']
        cnName = item.get('cnName')
        belong = item.get('belong')
        provinceName = item.get('provinceName')
        print(cnName,belong,provinceName)
        # 保存数据
        with open('3-优志愿.csv', 'a', encoding='utf-8') as f:
            f.write(cnName + '\t' + belong + '\t' + provinceName + '\n')
    print('保存成功'.format(page))

if __name__ == '__main__':
    for page in range(1,10):
        key = get_js_code(page)
        daxue(page, key)
    # daxue()
