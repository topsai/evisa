#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import base64
import time
import json
from urllib.request import urlparse
# from urlparse import urlparse
from com.aliyun.api.gateway.sdk import client
from com.aliyun.api.gateway.sdk.http import request
from com.aliyun.api.gateway.sdk.common import constant
import traceback
# import urllib2
import base64


def get_img_base64(img_file):
    with open(img_file, 'rb') as infile:
        s = infile.read()
        return base64.b64encode(s).decode()


def predict(url, app_key, app_secret, img_base64, kv_configure):
    statTime = time.time()
    cli = client.DefaultClient(app_key=app_key, app_secret=app_secret)
    param = {}
    print(type(img_base64))
    param['image'] = img_base64
    if kv_configure is not None:
        param['configure'] = json.dumps(kv_configure)
    print(type(param))
    body = json.dumps(param)
    url_ele = urlparse(url)
    host = 'http://' + url_ele.hostname
    path = url_ele.path
    headers = {}
    req_post = request.Request(host=host, protocol=constant.HTTP, url=path, headers=headers, method="POST",
                               time_out=6000)
    req_post.set_body(bytearray(source=body, encoding="utf8"))
    req_post.set_content_type(constant.CONTENT_TYPE_STREAM)
    stat, header, content = cli.execute(req_post)
    endTime = time.time()

    return stat, dict(header) if header is not None else {}, content


def demo():
    app_key = '25820460'
    app_secret = 'f20b7de68e73148d9485368a653dbfa7'
    url = 'http://dm-51.data.aliyun.com/rest/160601/ocr/ocr_idcard.json'
    img_file = 'pass.jpg'
    configure = {'side': 'face'}
    # 如果没有configure字段，configure设为None
    # configure = None

    img_base64data = get_img_base64(img_file)
    stat, header, content = predict(url, app_key, app_secret, img_base64data, configure)
    if stat != 200:
        print('Http status code: ', stat)
        print('Error msg in header: ', header['x-ca-error-message'] if 'x-ca-error-message' in header else '')
        print('Error msg in body: ', content)
        exit()
    result_str = content

    print(result_str)
    # result = json.loads(result_str)


if __name__ == '__main__':
    demo()
