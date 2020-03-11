#https://transferwise.com/gateway/v2/quotes/
import sys
import datetime
import urllib.request
import json


url = "https://transferwise.com/gateway/v2/quotes/" # 接口地址

# 消息头数据
headers = {
'Connection': 'keep-alive',
'Origin':'https://transferwise.com',
'Content-Type': 'application/json',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
'Accept': 'application/json',
'Referer': 'https://transferwise.com/us',
'Accept-Encoding': 'gzip, deflate, br',
'x-authorization-key': 'dad99d7d8e52c2c8aaf9fda788d8acdc',
'accept-language': 'en'
# ':authority': 'transferwise.com',
# ':method': 'POST',
# ':path': '/gateway/v2/quotes/',
# ':scheme': 'https'
}

payload = {"sourceAmount":4000,"sourceCurrency":"USD","targetCurrency":"JPY","preferredPayIn":"null","guaranteedTargetAmount":False,"referralCode":"tianz12"}
# verify = False 忽略SSH 验证
fdata = urllib.parse.urlencode(payload).encode(encoding='UTF8')
req = urllib.request.Request(url,headers=headers,data=fdata)
r = urllib.request.urlopen(req)
print(r.json())