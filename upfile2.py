#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "范斯特罗夫斯基"
# Email: hurte@foxmail.com
# Date: 2019/3/14

import requests
# 导入requests_toolbelt库使用MultipartEncoder
from requests_toolbelt import MultipartEncoder


url = 'https://afo.xiaojukeji.com/v2/mgrApi/car/car/mis/manage/pic/upload'
headers = {
    'Cookie': '_ga=GA1.2.1129292549.1536032342; _gid=GA1.2.420614154.1536808513; access_token=5c524351-f27a-48c0-a902-eea42d8284cc; JSESSIONID=14EA319C98E4FA91C74B44A066D49431',
    'Host': 'afo.xiaojukeji.com',
    'Origin': 'https://afo.xiaojukeji.com',
    'Referer': 'https://afo.xiaojukeji.com/v2/home.html',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.16 Safari/537.36'
    }
# file_payload = {'file': open('timg.jpg', 'rb')}
file_payload = {'file': ("timg.jpg", open('timg.jpg', 'rb'), "image/png")}
# 生成可用于multipart/form-data上传的数据
m = MultipartEncoder(file_payload)
# 自动生成Content-Type类型和随机码
headers['Content-Type'] = m.content_type
# 使用data上传文件
html = requests.post(url, headers=headers, data=m)
print(html.json())