# -*- coding: utf-8 -*-
import datetime
import json
import os
import requests
from settings import post_urls
from utils import sftp_download

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


# 过渡户交易明细文件下载
class FesB9999(FesRequest):
    def __init__(self, bank_code, start_date, end_date):
        super().__init__('9999')
        self.bank_code = bank_code
        self.start_date = start_date
        self.end_date = end_date
        self.acct_no = {
            '102': '3002010011200508811',
            '105': '65001610200052513865'
        }
        self.data = {
            "trans_code": "9999",
            "bank_code": self.bank_code,
            "trancode": "102",
            "acct_no": self.acct_no[bank_code],
            "start_date": start_date,
            "end_date": end_date
        }

    def post(self):
        resp = requests.post(post_urls['B9999'], data=json.dumps(self.data))
        print(resp.text)
        self.download_and_open_file()

    def download_and_open_file(self):
        file_name = '%s_%s_%s.txt' % (self.acct_no[self.bank_code], self.start_date, self.end_date)
        remote_path = '/home/fes/busi/batchdownload/%s/' % datetime.date.today().strftime('%Y%m%d')
        remote = remote_path + file_name
        local = 'C:/Users/Louis/Desktop' + file_name
        if os.path.exists(local):
            os.remove(local)
        sftp_download(remote, local)
        print('Success download file: %s' % local)
        os.startfile(local)
