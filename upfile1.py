#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "范斯特罗夫斯基"
# Email: hurte@foxmail.com
# Date: 2019/3/13

import requests
import json
import base64
import socket
from requests_toolbelt import MultipartEncoder

url = 'https://www.evisathailand.com/images/upload'

headers = {
    'Cookie': '_ga=GA1.2.1400082172.1552361215; _gid=GA1.2.1881511508.1552361215; _fbp=fb.1.1552361216092.242545506; _gat_gtag_UA_60603497_10=1',
    'Host': 'www.evisathailand.com',
    'Origin': 'https://www.evisathailand.com',
    'Referer': 'https://www.evisathailand.com/ft',
    'dataType': "json",
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.16 Safari/537.36'
}


# 首先将图片读入
# 由于要发送json，所以需要对byte进行str解码
def getByte(path):
    with open(path, 'rb') as f:
        img_byte = base64.b64encode(f.read())
    img_str = img_byte.decode('ascii')
    return img_str


img_str = getByte('timg.jpg')
data = {'dataType': "json", 'passportphoto[]': img_str, }
m = MultipartEncoder(data)
# 自动生成Content-Type类型和随机码
headers['Content-Type'] = m.content_type
json_mod = json.dumps(data)
res = requests.post(url=url, data=json_mod, headers=headers)
print(res.content)
print(res.text)
# 如果服务器没有报错，传回json格式数据
print(eval(res.text))
