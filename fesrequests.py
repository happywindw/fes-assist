# -*- coding: utf-8 -*-
import datetime
import json
import os
import requests
import shutil
from feslogs import logger
from settings import post_urls
from utils import sftp_download, get_desktop


class FesRequest(object):
    def __init__(self, trans_code):
        self.trans_code = trans_code
        self.data = {}

    def post(self):
        logger.info('Post request B%s to %s with msg: %s' % (self.trans_code, post_urls[self.trans_code], self.data))
        resp = requests.post(post_urls[self.trans_code], data=json.dumps(self.data))
        logger.info('Receive response msg: %s' % resp.text)


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


# 联机交易清算请求
class FesB2304(FesRequest):
    def __init__(self, settle_date, org_nick_name):
        super().__init__("2304")
        self.data = {
            "trans_code": "2304",
            "settle_date": settle_date,
            "org_nick_name": org_nick_name
        }


# 联机交易生成退款文件请求
class FesB2306(FesRequest):
    def __init__(self):
        super().__init__('2306')
        self.data = {"trans_code": "2306"}


# 联机交易回写请求
class FesB2211(FesRequest):
    def __init__(self):
        super().__init__('2211')
        self.data = {"trans_code": "2211"}


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

    def download_file(self):
        file_name = '%s_%s_%s.txt' % (self.acct_no[self.bank_code], self.start_date, self.end_date)
        remote_path = '/home/fes/busi/batchdownload/%s/' % datetime.date.today().strftime('%Y%m%d')
        remote = remote_path + file_name
        # 下载文件到临时目录下
        if not os.path.exists('./temp'):
            os.mkdir('./temp')
        local = './temp/' + file_name
        if os.path.exists(local):
            os.remove(local)
        msg = sftp_download(remote, local)
        if msg[0]:
            # 将下载的文件复制到桌面
            desktop = os.path.join(get_desktop(), file_name)
            if os.path.exists(desktop):
                os.remove(desktop)
            shutil.copy(local, desktop)
            return True, desktop
        else:
            return msg
