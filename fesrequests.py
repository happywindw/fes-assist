# -*- coding: utf-8 -*-
import json
import requests
from settings import post_urls

# data = {
#   "trans_code": "2301",
#   "check_date": "20180502",
#   "org_nick_name": "GHPOS",
#   "task_en_name": "CHECKFILE"
# }
#
# rep = requests.post('http://10.200.24.47:6080/fes-service/busi-api/2301', data=json.dumps(data))
# print(rep.text)


class FesRequest(object):
    def __init__(self, trans_code):
        self.trans_code = trans_code

    def post(self):
        pass


# 联机交易对账请求
class FesB2301(FesRequest):
    def __init__(self, tran_date, org_nick_name):
        super().__init__("2301")
        self.data = {
            "trans_code": "2301",
            "check_date": tran_date,
            "org_nick_name": org_nick_name,
            "task_en_name": "CHECKFILE"
        }

    def post(self):
        resp = requests.post(post_urls['B2301'], data=json.dumps(self.data))
        print(resp.text)


# 联机交易清算请求
class FesB2304(FesRequest):
    def __init__(self, settle_date, org_nick_name):
        super().__init__("2304")
        self.data = {
            "trans_code": "2304",
            "settle_date": settle_date,
            "org_nick_name": org_nick_name
        }

    def post(self):
        resp = requests.post(post_urls['B2304'], data=json.dumps(self.data))
        print(resp.text)


# 联机交易生成退款文件请求
class FesB2306(FesRequest):
    def __init__(self):
        super().__init__('2306')
        self.data = {"trans_code": "2306"}

    def post(self):
        resp = requests.post(post_urls['B2306'], data=json.dumps(self.data))
        print(resp.text)


# 联机交易回写请求
class FesB2211(FesRequest):
    def __init__(self):
        super().__init__('2211')
        self.data = {"trans_code": "2211"}

    def post(self):
        resp = requests.post(post_urls['B2211'], data=json.dumps(self.data))
        print(resp.text)

