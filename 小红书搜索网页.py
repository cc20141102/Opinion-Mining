import requests
import pandas as pd
import re
import time


cookie = 'abRequestId=043ad4ea-c3a9-5765-8174-f60838a18e50; xsecappid=xhs-pc-web; a1=18aad3990b1hop0y548f8szmdbqfp2rm40lxs3bk150000446956; webId=973e6c719cfb61440fc17cd2a37bc958; gid=yY00fqjjYd4YyY00fqjj88qDDyxlU8v24YiY1TyMu6fDAC28iUJF6M88844Kj2K80Y2SJS82; web_session=040069b32f3d1f12d333aad323374b28367e51; webBuild=3.10.6; unread={%22ub%22:%2264f48cc6000000001e02ef97%22%2C%22ue%22:%2265116606000000001f034d9d%22%2C%22uc%22:29}; websectiga=634d3ad75ffb42a2ade2c5e1705a73c845837578aeb31ba0e442d75c648da36a; sec_poison_id=05d82c6b-6f4a-4dd3-a054-170b724c1f25'
proxy = ''
def search_notes(proxy,cookie,keyword,page,sort):
    url = 'http://xxxxxx/index/search_notes'
    json_data = {
            'cookie':cookie,
            'note_type':0,
            'page': page,
            'keyword': keyword,
            'page_size':20,
            'sort': sort,
            'proxy_ip':proxy,
        }
    r = requests.post(url,json=json_data)

    return r

    
idlist = []
desclist = []
likelist = []
titlelist = []
timelist = []
userlist = []
useridlist = []
typelist = []

keyword = "洛阳牡丹节"

for page in range(1,20):
    page = str(page)
    dic = search_notes(proxy,cookie,keyword,page,"popularity_descending").json()
    if dic['success'] == True:
        if 'items' in dic['data'].keys():
            if dic['data']['items'] != []:
                for n in range(len(dic['data']['items'])):
                    if "https://www.xiaohongshu.com/discovery/item/"+str(dic['data']['items'][n]['id']) not in idlist and len(str(dic['data']['items'][n]['id'])) == 24:
                        try:
                            idlist.append("https://www.xiaohongshu.com/discovery/item/"+str(dic['data']['items'][n]['id']))
                        except:
                            idlist.append("----")
                        try:
                            userlist.append(dic['data']['items'][n]['note_card']['user']['nick_name'])
                        except:
                            userlist.append("----")
                        try:
                            useridlist.append(dic['data']['items'][n]['note_card']['user']['user_id'])
                        except:
                            useridlist.append("----")
                        try:
                            titlelist.append(dic['data']['items'][n]['note_card']['display_title'])
                        except:
                            titlelist.append("----")
                        try:
                            likelist.append(dic['data']['items'][n]['note_card']['interact_info']['liked_count'])
                        except:
                            likelist.append("----")
                        try:
                            typelist.append(dic['data']['items'][n]['note_card']['type'])
                        except:
                            typelist.append("----")

                if dic['data']['has_more'] != True:
                    break
        else:
            break

    print(len(idlist))

newdic = {"链接":idlist,
          "用户名":userlist,
          "用户id":useridlist,
          "标题":titlelist,
          #"简介":desclist,
          "点赞数":likelist,
          #"时间":timelist,
          "类型":typelist
    }
df = pd.DataFrame(newdic)
df.to_excel(keyword+'.xlsx', index=False)
