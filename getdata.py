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
    cookie_str = 'abRequestId=c1073d69-ffbf-5d6d-842b-8f79ea55e9a3; a1=18c902db3449n1jhfvfmxscznidmxikelqj3609ce50000599719; webId=95b02d83e58a19bf362fa4e9d21d7e25; gid=yYSj8JfDJ81fyYSj8JfDqA8j44jIyVxihi6CVSdMSuI3fq286C3TdK8882jjWyj84dJ00W0j; web_session=040069b75d8d407d5bcf40861c344bf86db5de; unread={%22ub%22:%226603ef4e000000001202057c%22%2C%22ue%22:%226620d61c0000000003023f1c%22%2C%22uc%22:33}; acw_tc=649231a02f3a34a5505ce5973e8069bb0934c26669080c43a0a6efae0389f347; websectiga=3633fe24d49c7dd0eb923edc8205740f10fdb18b25d424d2a2322c6196d2a4ad; sec_poison_id=c359f5fb-ef40-4f08-9b1c-dbc83800c960; webBuild=4.14.0; xsecappid=xhs-pc-web'
    



    cookies = trans_cookies(cookie_str)
    one_note = OneNote(cookies)
    url ='https://www.xiaohongshu.com/explore/64356527000000001303282b'
    res = one_note.get_one_note_info(url)
    print(res.text)

