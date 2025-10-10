import requests
from lxml import etree
import execjs


def playId(pages):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
    }
    cookies = {
        "P_INFO": "17671848634|1756795926|1|phoenix_client|00&99|null&null&null#CN&null#10#0|&0||17671848634",
        "NTES_CMT_USER_INFO": "1227282430%7C%E6%9C%89%E6%80%81%E5%BA%A6%E7%BD%91%E5%8F%8B199Jv_%7Chttp%3A%2F%2Fcms-bucket.nosdn.127.net%2F2018%2F08%2F13%2F078ea9f65d954410b62a52ac773875a1.jpeg%7Cfalse%7CeWQuMTRkOWI1ZGEwNmI3NGNhMGJAMTYzLmNvbQ%3D%3D",
        "vinfo_n_f_l_n3": "9a6decec10aac860.1.0.1757042986705.0.1757044613361",
        "_ntes_nnid": "1e75a3c5a05e547783d3045372edf70b,1759714881177",
        "_ntes_nuid": "1e75a3c5a05e547783d3045372edf70b",
        "NMTID": "00O7oWJoQ87yd8D20u4ohhapBaKzDQAAAGZty4vwQ",
        "WEVNSM": "1.0.0",
        "WNMCID": "rxnfvu.1759714884491.01.0",
        "WM_TID": "JLpkpWWdEW5EUAQUFVLHx8prGPkPrlFz",
        "ntes_utid": "tid._.BCdMs6f7NP1FE1UVEFOCh98uDPx0cZ9R._.0",
        "sDeviceId": "YD-obLCIpfykW9BEhURBRLCg54%2BGLx1cd5B",
        "__snaker__id": "WXoe6CxNo5L5kscI",
        "_iuqxldmzr_": "32",
        "__csrf": "1cc4b019568021e0494e33045b36c0c0",
        "MUSIC_U": "004A40F9006CEA301CCC1CE7CD4D526B7A828AF35C6E6F71BDF3ED32B30678AB35D104CB52E5359A29A61C7BA16B755CFFFBDE3EFF31957DEBB6AEA4ECD85892C0BE3896B42609C03CC7D69F2644C19A0201E56451A3A0F02E38E1FA44D4FCA21FBE0DD1E24350D1ECB027A483CEA2FAC3FA02E6E0273DE43AB0B7FA9A90941CF69B24F500B4288583C33A465037E457D110CC813F7765FA028992A0939713D4241FD73660226FBE5F7D68C336268983408B1FCA8D44A1DF451FD7F73698BAE7922F4A0267D0C0DEFDFA51F813CCE299C0E13E2C1DD7E089D54A1BACF4572C91B943D177AEBC2B59F41E9D499CB5A248487C93CFE3ED45F6C5F36685E611E97EE25E4EA9AAEDBC9165DFF01AAE9C1388420878EDAF9DA903EFB17E9B0769965388F827D0C39182C74D357C31F48F4576271DE9DF741817379921BAB325151D6254DFE09281E98D3F5A60D5DE5B6B886700FF176A5A6EF6922F18123B69E047364AD2AA5884F03E1C191894496E2D7DEFD4635A327AC0148803AC8814FBBBED9BE9AFB5F48E36C77D248512B7C416390C36",
        "ntes_kaola_ad": "1",
        "gdxidpyhxdE": "yriDy%2B5drUIg3m2qt2zk3KZMZAOnBxGP0VwsH%2FJp1hOdoIO7T6CcB2e7lDn6k%2FaOcgOkWnciX810RKJ14o3XEXmC0Q4uNwbv8o4c8EIjmO0tIpCbdf0r0PCnkw%2F3XkhuCo9YXfnEdmKh7vi6dZvobkL2o6BjlY%2B9iqezN17qQq8eRNMl%3A1759815661290",
        "WM_NI": "mwfjRt%2BALReXL5UNNKK1MyjJuDjAqYi6KkRiK72rLJwStFbRqLUqOxewtbaR3%2BR66wPX%2BRPXc06aLDu6IbWtgdPjoWomGRpi5z8XHV8FJmRKP%2FUzxZu17xj2wu7HggfkbEw%3D",
        "WM_NIKE": "9ca17ae2e6ffcda170e2e6ee8bf97ef3b4bebbf850a6ac8bb3d45f868b8e86d77db68bfb8bd1399bb49e92ed2af0fea7c3b92aafa9aa8bd180e99f84b3e85490eb9bafcd4189ef839ae942b79ca6a2f453abea858cd16389e9fe93cf42b58dbca7e15ab3949b92ce74a7a9bc83e45af1f59ed7b57d9488e5b3d354a1f0fa82cf50b7ea8783d680a5bca08bee5dadb389b3f363f7a6f8b9cb5efc9a868ed14194f19b9bfb52b7eff999e93ab5abf9a9e66da6b5aea6f637e2a3",
        "JSESSIONID-WYYY": "5wVse%2FAuMXdSeDm3%2Fw3umrUu1O9s3JUIXza%5Cv9HwcCnGCfllHDFRTuDtGOK6TarcBa%2FRVpouNMajHv%5CORbdUaXXU3VunBqdrvR4JBa8dAMsXs5uVy%2FCltwokTJ28msZRabM18ydPCvSJUy1wDRE5QyEAHo43k4%2FVsH18fzYzcB2pYfKD%3A1759979453795"
    }
    if pages == 0:
        url = "https://music.163.com/discover/playlist" + f"?order=hot&cat=全部&limit=35&offset={pages}"
    else:
        pages = pages + 35
        url = "https://music.163.com/discover/playlist" + f"?order=hot&cat=全部&limit=35&offset={pages}"

    response = requests.get(url, headers=headers, cookies=cookies)
    # print(response.text)
    r = etree.HTML(response.text)
    # 爬取数据
    ul = r.xpath('//ul[@id="m-pl-container"]/li')
    for li in ul:
        large_collection = "https://music.163.com/" + li.xpath('./div/a/@href')[0]
        print(large_collection)
        # https: // music.163.com /  # /playlist?id=3114158828
        small_collection = requests.get(large_collection, headers=headers, cookies=cookies)
        # print(small_collection.text)
        collection = etree.HTML(small_collection.text)
        # print(collection)

        table = collection.xpath('//ul[@class="f-hide"]/li')
        for tr in table:
            song_id = tr.xpath('.//@href')[0].split('=')[-1]
            # print(song_id)

            cursor = '-1'
            for page in range(1, 10):
                cursor = wangyi(page, cursor, song_id)
                print(f'第{page}页')


def wangyi(page, cursor, song_id):
    with open('5-网易云评论.js', 'r', encoding='utf-8-sig') as f:
        js_code = f.read()
    d = '{"rid":"R_SO_4_' + song_id + '","threadId":"R_SO_4_' + song_id + '","pageNo":"%d","pageSize":"20","cursor":"%s","offset":"0","orderType":"1","csrf_token":"1cc4b019568021e0494e33045b36c0c0"}' % (
        page, cursor)
    e = "010001"
    f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    g = "0CoJUm6Qyw8W8jud"
    data = execjs.compile(js_code).call('dd', d, e, f, g)
    # print(data)
    # return data

    url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
    # data = {
    #     'params':'smfrudjLSauZ/gqjrFg8437NmLPwV0cZwnsBMZPCMGJsncOEsd5CAdYAuU39Ipvq5yFuAKWlSvI9FbCLClZTu/vlw/RuiZXCpCud6ZEBs3ixN7f/WC1t0wdrGM+IQFer0egohMa+Lrm/7MWN423Lkly6CgcazsVUF7jIRljoKlI5lkHWcQrlRdTnf7FcCWunv1wUGHrvIDfInvFuYEYdFw9DxovPALElKU+tlZo2MgvT09T4m6Y76T97JXLSgNOXlBk2tebJKT7D+yR+YPtmR4xp+mMwSYWnv0rxGxkkcDJSi3F6Lk0xneS+b2z9myQZy5ZfGWoJEs+rD0DLYHr70XCgHTek2ZJ3LJLSE4tgXZA=',
    #     'encSecKey':'125c19fa4cf3f07ec0f7a639d9446cad177a2c30b324315494e638634082aaa412c67247b795ec8a3f5a7426bab53c9bc174f3a2e1dfdcbb65c979c8357807b2c8b531ee0c5355736738973d1039fa2abd9bcb7c252f7574eec93ccd6c6e53f1000815b4776eec1fb2df093d8df9859e177378968ebd12155b5db9ca5eb674e2'
    # }
    data = data
    # 拿数据
    r = requests.post(url, data).json()
    comments = r['data']['comments']
    for comment in comments:
        content = comment['content']
        print(content)

    # 拿下一个js需要用到的值
    cursor = r['data']['cursor']
    return cursor


if __name__ == '__main__':
    for pages in range(1,10):
        playId(pages)
