import execjs

js = execjs.compile(open(r'./static/info.js', 'r', encoding='utf-8').read())
def decodedUniChars(url):
    decodedUniChars = url.encode('utf-8').decode("unicode_escape")
    return decodedUniChars


def get_headers():
    return {
        "authority": "edith.xiaohongshu.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://www.xiaohongshu.com",
        "referer": "https://www.xiaohongshu.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188",
        "x-s": "",
        "x-t": ""
    }

def get_note_data(note_id):
    return {
        "source_note_id": note_id,
        "image_scenes": [
            "CRD_PRV_WEBP",
            "CRD_WM_WEBP"
        ]
    }



def get_profile_data(user_id,cursor):
    return {
        "num": 30,
        "cursor": cursor,
        "user_id": user_id,
        "image_formats": [
            "jpg",
            "webp",
            "avif"
        ]
    }
