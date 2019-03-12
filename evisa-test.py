#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "范斯特罗夫斯基"
# Email: hurte@foxmail.com
# Date: 2019/3/12

import requests

img_resp = {
    "passportphoto": ["passportphoto_5c87658b007419.05683553.jpeg", "passportphoto_5c87658b01fa54.35958703.jpeg"]}
base_url = 'https://www.evisathailand.com'
thailind_url = base_url + '/ft'
pay_url = 'https://paygate.ktc.co.th/ktc/eng/merchandize/payment/payForm.jsp'

# contApPaymentBtn.click(function() {
#  location.href = "/ap-payment/" + $(this).attr("data-transaction");

pay_info = """

merchantId: 991300369
amount: 525
orderRef: VOA2019030102355
currCode: 764
successUrl: https://www.evisathailand.com/ap-success/68c79f14159a69e3835b7ad26f66d8c660c47d53
failUrl: https://www.evisathailand.com/ap-failed/68c79f14159a69e3835b7ad26f66d8c660c47d53
cancelUrl: https://www.evisathailand.com/ap-cancel/68c79f14159a69e3835b7ad26f66d8c660c47d53
payType: N
lang: E
TxType: Retail
payMethod: ALIPAY
remark: 1|991300379|
"""

#
# r = requests.post(thailind_url,
#                   data={'nationality': 'chn', 'airport': 'BKK - Suvarnabhumi International Airport', 'arrivaldate': '',
#                         'accepttc': 'true'})
#
# flag = True
# with open('pass.txt') as f:
#     while flag:
#         temp = f.readline()
#         if temp:
#             s = temp.strip().split(':')
#             if len(s) == 2:
#                 print("\"" + s[0] + "\":\"" + s[1].strip() + "\",")
#             else:
#                 print("\"" + s[0] + "\":\"\",")
#         else:
#             flag = False

regist_data = {

    "p[0][_id]": "1",
    "p[0][nationality]": "chn",
    "p[0][passport_type]": "ordinary",
    "p[0][airport]": "bkk",
    "p[0][salutation]": "mr",
    "p[0][lastName]": "fan",
    "p[0][middleName]": "",
    "p[0][firstName]": "siji",
    "p[0][gender]": "male",
    "p[0][birthDate]": "17/08/2018",
    "p[0][email]": "hr@foxmail.com",
    "p[0][mobileNumCountry]": "cn",
    "p[0][mobileNum]": "+8613123456789",
    "p[0][passportNum]": "E1342342",
    "p[0][passportDateIssue]": "04/03/2019",
    "p[0][passportDateExpiry]": "04/03/2024",
    "p[0][arrivalDate]": "31/03/2019",
    "p[0][arrivalTime]": "",
    "p[0][arrivalNum]": "2423",
    "p[0][departureDate]": "10/04/2019",
    "p[0][departureTime]": "",
    "p[0][departureNum]": "23423",
    "p[0][imagesUploaded][passportphoto][]": "passportphoto_5c87766920eef0.45117421.jpeg",
    "p[0][imagesUploaded][passportphoto][]": "passportphoto_5c87766922a094.66561145.jpeg",
    "p[0][imagesUploaded][ticketphoto][]": "ticketphoto_5c8776699da396.59918846.jpeg",
    "p[0][imagesUploaded][ticketphoto][]": "ticketphoto_5c8776699ee7e1.10483854.jpeg",
    "p[0][imagesUploaded][accomodationphoto][]": "accomodationphoto_5c87766adb85f7.49267151.jpeg",
    "p[0][accomodation][posType]": "hotel",
    "p[0][accomodation][posName]": "fdfg",
    "p[0][accomodation][posProvince]": "Chiang Mai",
    "p[0][accomodation][posDistrict]": "Mae Taeng",
    "p[0][accomodation][posSubDistrict]": "",
    "p[0][accomodation][posStreetAddress]": "",
    "p[0][accomodation][posPostCode]": "50150,50330",
    "p[0][residentialAddress]": "gety",
    "p[0][referenceNameAddr]": "",
    "p[0][minorInfo]": "",
}
# # 提交注册信息
# r = requests.post(thailind_url, data=regist_data)
# # 获取支付码
# transaction = r.json().get('transaction')
# # 支付地址
# url = base_url + "/ap-payment/" + transaction
url = 'https://www.evisathailand.com/ap-payment/67abdafd4058bafbac0d9fdc5302aaa5a2279202'
print(url)
# 访问支付地址
# r = requests.get(url)
# print(r.text)
# response.xpath('//form/input[@value != ""]')[2].attrib
from lxml import etree

req = requests.get(url)
req.encoding = 'utf8'
# 将request.content 转化为 Element
root = etree.HTML(req.content)
# 选取 ol/li/div[@class="item"] 不管它们在文档中的位置
items = root.xpath('//form/input[@value]')
# 获取支付参数
for i in items:
    tem = i.attrib
    print("\"" + i.get('name') + "\":\"" + i.get('value') + "\",")

{
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

pay_action = "payALIPAYONL.jsp"
u = "https://paygate.ktc.co.th/ktc/eng/merchandize/payment/payForm.jsp"

u1 = "https://paygate.ktc.co.th/ktc/eng/merchandize/payment/payALIPAYONL.jsp"
