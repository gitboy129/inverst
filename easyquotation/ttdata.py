# !/usr/bin/python
# -*- coding: utf-8 -*-
import time
import datetime
import glob
import urllib3
import json
import sys
import re

class ttApi():
    def get_allfund(self):
        http=urllib3.PoolManager()
        response_all_funds = http.request('GET','http://fund.eastmoney.com/js/fundcode_search.js')
        fundstr = response_all_funds.data.decode()[9:-1]
        #print(fundstr)
        fundjson=json.loads(fundstr)
        #print(fundjson)
        return fundjson

    def get_fund_detail(self):
        return 1

# ttApi1=ttApi()
# ttApi1.get_allfund()