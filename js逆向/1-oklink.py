import requests
# 导入js
import execjs


def get_js_result():
    with open('1-oklink.js', 'r', encoding='utf-8-sig') as f:
        js_code = f.read()
    apikey = execjs.compile(js_code).call("getApiKey")
    print(apikey)
    return apikey


def oklink(page,apikey):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0",
        "x-apikey": apikey,
    }

    url = "https://www.oklink.com/api/explorer/v1/btc/transactionsNoRestrict"
    params = {
        "offset": page * 20,
        "limit": "20",
        "needBigField": "false",
        "t": "1759652750682"
    }
    response = requests.get(url, headers=headers, params=params).json()['data']['hits']
    for i in response:
        title = i.get('hash')
        index = i.get('index')
        # title = i.get('hash')
        # title = i.get('hash')
        print(title,index)
    # print(apikey)

if __name__ == '__main__':
    for page in range(10):
        # oklink(page)
        apikey = get_js_result()
        oklink(page,apikey)