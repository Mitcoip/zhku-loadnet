
import requests
from subprocess import run, PIPE
import os
import datetime

def load():
    userId = ''
    passwd = ''
    Url = 'http://1.1.1.1:8888/webauth.do?wlanacip=192.16.99.2&wlanacname=zkbras1&wlanuserip=10.40.180.95&mac=60:18:95:46:08:7d&vlan=3856&url=http://1.1.1.1'

    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
    }

    data = {
    'hostIp': 'http://127.0.0.1:8082/',
    'loginType': '',
    'auth_type': '0',
    'isBindMac1':' 0',
    'pageid': '1',
    'templatetype': '1',
    'listbindmac': '0',
    'recordmac': '0',
    'isRemind': '0',
    'loginTimes':'' ,
    'groupId': '',
    'distoken': '',
    'echostr': '',
    'url': 'http://1.1.1.1',
    'isautoauth': '',
    'notice_pic_loop2': '/portal/uploads/pc/demo2/images/bj.png',
    'notice_pic_loop1': '/portal/uploads/pc/demo2/images/logo.png',
    'userId': '',
    'passwd': ''
    }

    data['userId'] = userId
    data['passwd'] = passwd

    while(1):
        r = run('ping www.baidu.com',
                stdout=PIPE,
                stderr=PIPE,
                stdin=PIPE,
                shell=True)
        if r.returncode:
            #无网络
            requests.post(url=Url,data=data)
            try:
                os.mkdir(r'C:\tmp')
                file = open(r'C:\tmp\tmp.txt','a')
            except:
                file = open(r'C:\tmp\tmp.txt', 'a')
                times = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
                file.write(f'\n成功连接,时间为{times}')
        else:
            #正常联网
            break



if __name__ == '__main__':
    load()

