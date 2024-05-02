import json
from hashlib import md5
import time
import requests


def r(a):
    q = 'A4NjFqYu5wPHsO0XTdDgMa2r1ZQocVte9UJBvk6/7=yRnhISGKblCWi+LpfE8xzm3'
    b,d = '',0
    while d < len(a):
        c = ord(a[d])
        d += 1
        _0x1d9f9c = ord(a[d])
        d += 1
        _0x465aba = ord(a[d]) if d < len(a) else 0
        d += 1
        _0x37a25a = c >> 0x2
        _0x3582e7 = (c & 0x3) << 0x4 | _0x1d9f9c >> 0x4
        _0x16cbc3 = (_0x1d9f9c & 0xf) << 0x2 | _0x465aba >> 0x6
        _0xb06a7e = _0x465aba & 0x3f
        if not _0x1d9f9c:
            _0x16cbc3 = _0xb06a7e = 0x40
        elif not _0x465aba:
            _0xb06a7e = 0x40
        b += q[_0x37a25a] + q[_0x3582e7] + q[_0x16cbc3] + q[_0xb06a7e]
    return b

def get_xs(url,data=None):
    u = str(int(time.time()*1000))
    t = 'test'
    data = json.dumps(data,separators=(',',':')) if data else ''
    return {
        'X-s': r(md5(''.join([u, t, url, data]).encode()).hexdigest()),
        'X-t': u,
        'data':data
    }

if __name__ == '__main__':
    cookies = {'a1': '1874cce341chrx3nix10ml4ld6um7xw4zjxuko9ve00005193007', 'extra_exp_ids': 'yamcha_0327_exp,h5_1208_exp3,ques_exp2', 'extra_exp_ids.sig': 'tP-EUqmkBBQjAxiuz_uTOZ2UHKu0CJkOe3bWvplEOns', 'gid': 'yYW4SSdq2yuYyYW4SSdq4VljySxFCqI3Cy86Chd141fK77886WCE4T882yjq88W848Dqi4jY', 'gid.sign': 'L7JaZhR4NZiD9Ij4xiijJ+jiw5k=', 'webId': 'd8421e552a2f2f0dfa700bc968fbf07d', 'web_session': '040069b2c8b722ccff3b707519364b54d7c5e6', 'xhsTrackerId': 'b6798cd4-d6da-4458-8e9d-abfa1076ba8e', 'xhsTrackerId.sig': 'I9_iuDo8bGf0BqAFmNdLcaAyew3_W2NwsiijIPaMeEc'}

    headers = {
        'authority': 'edith.xiaohongshu.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://www.xiaohongshu.com',
        'pragma': 'no-cache',
        'referer': 'https://www.xiaohongshu.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        # 'x-b3-traceid': '90aeb126b0726eff',
        # 'x-s': '1gakZBwJ12spslV6OjdJ1Bc+1BTGsjUUsgZUsBaB0gs3',
        # 'x-t': '1678778130077',
    }

    node_id = '6411bd58000000000800ed73'

    print('文章ID', node_id)

    # 点赞
    json_data = {
        'note_oid': node_id,
    }
    url = '/api/sns/web/v1/note/like'
    print('点赞', url)
    info = get_xs( url, json_data)
    print(info)
    headers['x-t'] = info['X-t']
    headers['x-s'] = info['X-s']
    data = info['data']
    res = requests.post('https://edith.xiaohongshu.com' + url, cookies=cookies, headers=headers, data=data, ).json()
    print(res)


    # # 收藏
    # json_data = {
    #     'note_id': node_id,
    # }
    # url = '/api/sns/web/v1/note/collect'
    # print('收藏', url)
    # info = get_xs( url, json_data)
    # print(info)
    # headers['x-t'] = info['X-t']
    # headers['x-s'] = info['X-s']
    # data = info['data']
    # res = requests.post('https://edith.xiaohongshu.com' + url, cookies=cookies, headers=headers, data=data, ).json()
    # print(res)
    #
    # # 评论
    # json_data = {
    #     'note_id': node_id,
    #     'content': 'test666',
    #     'at_users': [],
    # }
    # url = '/api/sns/web/v1/comment/post'
    # print('评论', url)
    # info = get_xs( url, json_data)
    # print(info)
    # headers['x-t'] = info['X-t']
    # headers['x-s'] = info['X-s']
    # data = info['data']
    # res = requests.post('https://edith.xiaohongshu.com' + url, headers=headers, data=data.encode(),cookies=cookies).json()
    # print(res)
