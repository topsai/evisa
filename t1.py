#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "范斯特罗夫斯基"
# Email: hurte@foxmail.com
# Date: 2019/3/13

import requests

u1 = "https://paygate.ktc.co.th/ktc/eng/merchandize/payment/payALIPAYONL.jsp"
data = {
    "merchantId": "991300369",
    "amount": "525",
    "orderRef": "VOA2019030102396",
    "currCode": "764",
    "successUrl": "https://www.evisathailand.com/ap-success/67abdafd4058bafbac0d9fdc5302aaa5a2279202",
    "failUrl": "https://www.evisathailand.com/ap-failed/67abdafd4058bafbac0d9fdc5302aaa5a2279202",
    "cancelUrl": "https://www.evisathailand.com/ap-cancel/67abdafd4058bafbac0d9fdc5302aaa5a2279202",
    "payType": "N",
    "lang": "E",
    "TxType": "Retail",
    "payMethod": "ALIPAY",
    "remark": "1|991300379|",
}
r = requests.post(u1, data=data)
print(dir(r))
print(r.content)
