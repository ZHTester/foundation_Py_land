# coding=utf-8
__author__ = 'landing'
__data__ = '2019/5/3  14:47'
"""
鹏鹏娱乐城聊天室彩票投注

"""
import requests
import re
import random
from websocket import create_connection
import json

r = requests.session()  # 保持session
random_num = random.randint(0, 9)  # 生成随机数


def request_login():
    """
    登录接口方法
    :return:
    """
    login_data = {
        "username": "jingdian500",
        "password": "aa123123"
    }
    login_url = "http://10.10.0.3/modelzhu2/php/action.php?action=login"
    login_r = r.post(url=login_url, data=login_data).json()
    login_oid = login_r['data']['oid']
    login_username = login_r['data']['username']
    return login_oid, login_username


def request_param():
    """
    获取param r encrypt
    :return:
    """
    login_oid, login_username = request_login()
    param_url = 'http://10.10.0.3/modelzhu2/php/login.php?' \
                'action=lotto&username={username}&oid={oid}'.format(username=login_username, oid=login_oid)
    param_r = r.get(param_url).text

    res_encrypt = "<input type='hidden' name='encrypt' value=.*?>"  # 正则表达式提取html数据
    encrypt_tr = re.findall(res_encrypt, param_r)  # 正则表达式提取出param
    encrypt = encrypt_tr[0].split('=')[3].split('/')[0].split("'")[1]

    res_param = "<input type='hidden' name='param' value=.*?>"  # 正则表达式提取html数据
    param_tr = re.findall(res_param, param_r)  # 正则表达式提取出encrypt
    param = param_tr[0].split('=')[3].split("'")[1] + '='

    res_r = "<input type='hidden' name='r' value=.*?>"  # 正则表达式提取html数据
    r_tr = re.findall(res_r, param_r)  # 正则表达式提取出r
    rr = r_tr[0].split('=')[3].split('/')[0].split("'")[1]
    return param, encrypt, rr


def request_cookie(param1, encrypt1, rr1):
    cookie_curl = 'http://vuewebapp.dt-lotto-debugfight.com/Default/IndexNew'
    cookie_data = {
        "param": param1,
        "encrypt": encrypt1,
        "ip": "10.0.1.182",
        "r": rr1,
        "lid": 1,
        "platformURL": "http://10.10.0.3/modelzhu2"
    }
    cookie_request = r.post(url=cookie_curl, data=cookie_data, allow_redirects=False)
    SetCookie = cookie_request.headers['Set-Cookie']
    # print(SetCookie)   # 得到cookie 保持登录状态
    return SetCookie


def requests_pankou(param1, encrypt1, rr1):
    """
    获取盘口
    :return:
    """

    pankou_url = 'http://vuewebapp.dt-lotto-debugfight.com/member' \
                 '/PositionForWebApp?v={0}557{0}2410221{0}'.format(random_num)
    headers = {"cookie": request_cookie(param1, encrypt1, rr1)}
    pankou_get = r.get(pankou_url, headers=headers)
    print(pankou_get.json())


def requests_GetChatRoomToken(param1, encrypt1, rr1):
    """
    获取房间token
    :param param1:
    :param encrypt1:
    :param rr1:
    :return:
    """
    ChatRoom_url = 'http://vuewebapp.dt-lotto-debugfight.com/Infos/GetAccessToken?lid=46'
    headers = {
        "cookie": request_cookie(param1, encrypt1, rr1)
    }
    ChatRoom_get = r.get(ChatRoom_url, headers=headers)
    room_token = ChatRoom_get.text
    return room_token


def requests_GotoRoom(param1, encrypt1, rr1):
    Go_token = requests_GetChatRoomToken(param1, encrypt1, rr1)
    Go_token = json.loads(Go_token)
    Room_url = "http://10.10.248.95:6006/Api/Message/negotiate?accessToken={token}".format(token=Go_token)
    connectionId = r.post(Room_url).json()['connectionId']  # 获取id
    connectionId = Go_token + "&id=" + connectionId  # 拼接token和id

    Room_url_ws = 'ws://10.10.248.95:6006/Api/Message?accessToken={token}'.format(token=connectionId)
    ws = create_connection(Room_url_ws)  # 进入房间房间
    frist_data = '{"protocol":"json","version":1}'
    send_data = ws.send(frist_data)
    print(send_data.bit_length())
    print("创建连接成功")


def run_main():
    param1, encrypt1, rr1 = request_param()
    requests_GotoRoom(param1, encrypt1, rr1)


if __name__ == "__main__":
    run_main()
