#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "范斯特罗夫斯基"
# Email: hurte@foxmail.com
# Date: 2019/3/13

import requests

import requests
# 导入requests_toolbelt库使用MultipartEncoder
from requests_toolbelt import MultipartEncoder

url = 'https://www.evisathailand.com/images/upload'
headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'Host': 'www.evisathailand.com',
    'Origin': 'https://www.evisathailand.com',
    'Referer': 'https://www.evisathailand.com/ft',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.16 Safari/537.36'
}

# :authority: www.evisathailand.com
# :method: POST
# :path: /images/upload
# :scheme: https
# accept: application/json, text/javascript, */*; q=0.01
# accept-encoding: gzip, deflate, br
# accept-language: zh-CN,zh;q=0.9
# content-length: 216352
# content-type: multipart/form-data; boundary=----WebKitFormBoundaryyU5dFkTSkAUYgDHA
# cookie: _ga=GA1.2.1400082172.1552361215; _gid=GA1.2.1881511508.1552361215; _fbp=fb.1.1552361216092.242545506; _gat_gtag_UA_60603497_10=1
# origin: https://www.evisathailand.com
# referer: https://www.evisathailand.com/ft
# user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36
# x-csrf-token: undefined
# x-requested-with: XMLHttpRequest
# name="passportphoto[]"; filename="hehua.jpg"

file_payload = {'passportphoto[]': ("timg.jpg", open('timg.jpg', 'rb'), "image/jpeg")}

# file_payload = {'name':'': open('timg.jpg', 'rb')}
# 生成可用于multipart/form-data上传的数据
m = MultipartEncoder(file_payload)
# 自动生成Content-Type类型和随机码
headers['Content-Type'] = m.content_type
# 使用data上传文件
html = requests.post(url, headers=headers, data=m)
print(html.json())

# const uploadImages = (btn, fd, fn) => {
#   $.ajax({
#     url: "/images/upload",
#     data: fd._blob ? fd._blob() : fd,
#     type: "POST",
#     processData: false,
#     contentType: false,
#     dataType: "json",
#     success: function(e) {
#       console.log(e);
#       fn(e);
#       return e;
#     },
#     error: function(e) {
#       console.dir(e);
#       showAlert("Something went wrong. Please try again.", false);
#       enableUploadBtn(btn);
#     },
#     beforeSend: function(xhr) {
#       xhr.setRequestHeader("X-CSRF-Token", $("input[name='_csrfToken']").val());
#     }
#   });
# };
