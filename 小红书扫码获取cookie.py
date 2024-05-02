import requests
import base64
from PIL import Image
from io import BytesIO
import qrcode
import time

proxy = ''



def get_03ck():
    params = {
        'proxy_ip':'',
    }
    response = requests.get('xxxxx', params=params)
    dic = response.json()

    return dic['data']




def decode_base64(data):
    missing_padding = len(data) % 4
    if missing_padding:
        data += '=' * (4 - missing_padding)
    return base64.b64decode(data)



def get_code(cookie):

    params = {
        'cookie':cookie,
        'proxy_ip':proxy
    }

    r = requests.get('xxxxxx/login/qrcode', params=params)
    dic = r.json()
    
    decoded_data = dic['data']['img'].replace('data:image/png;base64,','')
    print(decoded_data)
    decoded_data = decode_base64(decoded_data)
    image = Image.open(BytesIO(decoded_data))
    image.show()  # 显示解码后的图片（可选）

    return dic['data']['qr_id'],dic['data']['code']

def get_cookie(qr_id,code):
    params = {
    'cookie':cookie,
    'proxy_ip':proxy
    }

    r = requests.get(
        f'xxxxxxxx{qr_id}/{code}',
        params=params
    )
    print(r.text)
    dic = r.json()
    session = dic['data']['login_info']['session']
    str = f"web_session={session}"
    params = cookie.split(';')
    for i in range(len(params)):
        if "web_session" in params[i]:
            params[i] = str
            
    result = ';'.join(params)

    return result

while True:
    try:
        cookie = get_03ck()
    except:
        print("获取cookie失败")
        continue
    print(cookie)
    try:
        qr_id,code = get_code(cookie)
        print(qr_id,code)
        a = input("按回车获取cookie")
    except:
        print("获取二维码失败")
        continue
    try:
        cookies = get_cookie(qr_id,code)
        print("#########################################################")
        print(cookies)
        a = input("回车进入下一次扫码")
    except:
        print("获取cookie失败，请重新扫码")
        time.sleep(2)
