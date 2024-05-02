import json
import requests
from xhs_utils.xhs_util import get_headers, js, get_note_data
from xhs_utils.cookie_util import trans_cookies
class OneNote:
    def __init__(self, cookies):
        self.cookies = cookies
        self.feed_url = 'https://edith.xiaohongshu.com/api/sns/web/v1/feed'
        self.detail_url = 'https://www.xiaohongshu.com/explore/'
        self.headers = get_headers()

    # 单个视频
    def get_one_note_info(self, url):
        note_id = url.split('/')[-1]
        data = get_note_data(note_id)
        data = json.dumps(data, separators=(',', ':'))
        ret = js.call('get_xs', '/api/sns/web/v1/feed', data, self.cookies['a1'])
        self.headers['x-s'], self.headers['x-t'] = ret['X-s'], str(ret['X-t'])

        response = requests.post(self.feed_url, headers=self.headers, cookies=self.cookies, data=data)
        #res = response.text
        print(self.feed_url)
        print(self.headers)
        print(self.cookies)
        print(data)
        return response


if __name__ == '__main__':
    cookie_str = ''



    cookies = trans_cookies(cookie_str)
    one_note = OneNote(cookies)
    url ='https://www.xiaohongshu.com/explore/64356527000000001303282b'
    res = one_note.get_one_note_info(url)
    print(res.text)

