# !/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import datetime
import urllib.request
import json
#http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=lof&rs=&gs=0&sc=zzf&st=desc&sd=2019-03-11&ed=2020-03-11&qdii=&tabSubtype=,,,,,&pi=1&pn=50
#http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=lofpi=1&pn=300


res = urllib.request.urlopen("http://fundgz.1234567.com.cn/js/162703.js")
zfc1=res.read().decode('utf-8')[8:-2]
print(zfc1)
resp=json.loads(zfc1)
print(resp["gsz"])
print(resp["gszzl"])
print(resp["gztime"][0:-6])
print(resp["gztime"][-5:])
print(resp["fundcode"])
print(resp["name"])
print(resp["dwjz"])


# res2 = urllib.request.urlopen("http://fund.eastmoney.com/js/fundcode_search.js")
# zfc2=res2.read().decode('utf-8')[8:-1]
# print(zfc2)
# resl=json.loads(zfc2)
# print(resl)


res3= urllib.request.urlopen("http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=lof&pi=1&pn=300")
zfc3=res3.read().decode('utf-8')[22:-158]
print(zfc3)
