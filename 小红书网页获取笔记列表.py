import requests
from xs算法 import get_xs
import time
import hashlib
import requests
import time
import urllib3
import random
# from xs算法 import get_xs
import execjs
urllib3.disable_warnings()
import pandas as pd




with open('x-s-common.js',encoding='utf8') as f:
    ctx = execjs.compile(f.read())
with open('xsxt.js',encoding='utf8') as f:
    xsxt = execjs.compile(f.read())
ip = None
if ip:
    proxies = {
        'http': ip,
        'https': ip
    }
else:
    proxies = {
    }
    
cookies = {
    'xhsTrackerId': 'd2feb607-75bc-42aa-875a-afd712eaf421',
    'xhsTrackerId.sig': 'p7FzWVW6E7R8_ncsjf7emjNygxpox6lLbjy6Sf7-Ofk',
    'a1': '187848726b6sgnofd3fcay4a6ocpjl6v9z8jcqhs350000159320',
    'webId': 'cb95431ea175bbeb9bf26c2411feaca3',
    'gid': 'yYWY4YWJ00j2yYWY4YWJKuAxDKMkIlifqiS0YMqv40KlSV28UV1KhS888y2jqJ88jSK8jqJq',
    'gid.sign': 'c4gFgOREwI6avj7J9pckR1KRpt8=',
    'smidV2': '20230310142744c93de1dd90a7cef8e6dbce354fe048dd00378a8d0a6ff29b0',
    'xsecappid': 'xhs-pc-web',
    'xhsTracker': 'url=explore&searchengine=baidu',
    'xhsTracker.sig': 'u1cFYHAwm89lKbFLL1Y8vp9JcskioXWTa56RKaAB2ys',
    'webBuild': '2.5.2',
    'websectiga': '59d3ef1e60c4aa37a7df3c23467bd46d7f1da0b1918cf335ee7f2e9e52ac04cf',
    'sec_poison_id': '3c9be063-3620-4a8e-99fe-22ab0e1f42a2',
    'acw_tc': '756273fe00ee345fa0c828768937f12f81d85d277784baf713f991715b4b520a',
    'web_session': '040069b091d272d4767053616b364b9b6b7bd6',
}

headers = {
    'authority': 'edith.xiaohongshu.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://www.xiaohongshu.com',
    'referer': 'https://www.xiaohongshu.com/',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'x-b3-traceid': '688b23fcf72971f7',
}

session = requests.session()
session.cookies.update(cookies)
session.proxies = proxies
idlist = []
desclist = []
likelist = []
titlelist = []
timelist = []
userlist = []
useridlist = []
typelist = []
keyword = "林渡暖村"
for page in range(1,50):
    json_data = {
        'keyword': keyword,
        'page':page,
        'page_size': 20,
        'search_id': '2bnjkr48t0yra1s332yu0',
        'sort': 'general',
        'note_type': 0,
    }
    url = '/api/sns/web/v1/search/notes'
    info = get_xs(url, json_data)
    data = info['data']
    headers['x-t'] = info['X-t']
    headers['x-s'] = info['X-s']
    a1 = cookies['a1']
    x_s_common = ctx.call('get_common', info,a1)
    headers['x-s-common'] = x_s_common # 必须要
    r = session.post(
        'https://edith.xiaohongshu.com/api/sns/web/v1/search/notes',
        cookies=cookies,
        headers=headers,
        data=data,
        proxies=proxies
    )
    print(r.text)
    time.sleep(2)
    dic = r.json()
    if dic['success'] == True:
        if "note_card" in r.text:
            if dic['data']['items'] != []:
                for n in range(len(dic['data']['items'])):
                    if "https://www.xiaohongshu.com/discovery/item/"+str(dic['data']['items'][n]['id']) not in idlist:
                        idlist.append("https://www.xiaohongshu.com/discovery/item/"+str(dic['data']['items'][n]['id']))
                        print("https://www.xiaohongshu.com/discovery/item/"+str(dic['data']['items'][n]['id']))
                        userlist.append(dic['data']['items'][n]['note_card']['user']['nickname'])
                        useridlist.append(dic['data']['items'][n]['note_card']['user']['user_id'])
                        try:
                            titlelist.append(dic['data']['items'][n]['note_card']['display_title'])
                        except:
                            titlelist.append("----")
                        likelist.append(dic['data']['items'][n]['note_card']['interact_info']['liked_count'])
                        typelist.append(dic['data']['items'][n]['note_card']['type'])
                        
                print(len(idlist))
            else:
                break
        else:
            break
    else:
        break

        

newdic = {"链接":idlist,
          "用户名":userlist,
          "用户id":useridlist,
          "标题":titlelist,
          "点赞数":likelist,
          "类型":typelist
    }
df = pd.DataFrame(newdic)
df.to_excel(keyword+'.xlsx', index=False)
