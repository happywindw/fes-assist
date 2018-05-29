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
    """所有请求类的基类"""
    def __init__(self, trans_code):
        self.trans_code = trans_code
        self.data = {}

    def post(self):
        try:
            logger.info('Send request B%s to %s with msg: %s' %
                        (self.trans_code, post_urls[self.trans_code], self.data))
            resp = requests.post(post_urls[self.trans_code], data=json.dumps(self.data))
            logger.info('Received response msg: %s' % resp.text)
            if resp.status_code != 200:
                raise self.FesSeverException('Response status is not 200.')
        except Exception as e:
            logger.error('Exception: %s' % e)
            raise
        return json.loads(resp.content, encoding=resp.encoding)

    class FesSeverException(BaseException):
        def __init__(self, error_msg):
            BaseException().with_traceback(error_msg)


class FesB2301(FesRequest):
    """联机交易对账请求类"""
    def __init__(self, tran_date, org_nick_name):
        super().__init__("2301")
        self.data = {
            "trans_code": "2301",
            "check_date": tran_date,
            "org_nick_name": org_nick_name,
            "task_en_name": "CHECKFILE"
        }


class FesB2304(FesRequest):
    """联机交易生成清算数据请求类"""
    def __init__(self, settle_date, org_nick_name):
        super().__init__("2304")
        self.data = {
            "trans_code": "2304",
            "settle_date": settle_date,
            "org_nick_name": org_nick_name
        }


class FesB2306(FesRequest):
    """生成联机交易退款文件请求类"""
    def __init__(self):
        super().__init__('2306')
        self.data = {"trans_code": "2306"}


class FesB2211(FesRequest):
    """联机交易回写业务请求类"""
    def __init__(self):
        super().__init__('2211')
        self.data = {"trans_code": "2211"}


class FesB9999(FesRequest):
    """下载过渡户交易明细请求类"""
    def __init__(self, bank_account, start_date, end_date):
        super().__init__('9999')
        self.bank_account = bank_account
        self.start_date = start_date
        self.end_date = end_date
        self.data = {
            "trans_code": "9999",
            "bank_code": self.bank_account[0],
            "trancode": "102",
            "acct_no": self.bank_account[1],
            "start_date": start_date,
            "end_date": end_date
        }

    def download_file(self):
        file_name = '%s_%s_%s.txt' % (self.bank_account[1], self.start_date, self.end_date)
        remote_path = '/home/fes/busi/batchdownload/%s/' % datetime.date.today().strftime('%Y%m%d')
        remote = remote_path + file_name
        # 下载文件到临时目录下
        if not os.path.exists('./temp'):
            os.mkdir('./temp')
        local = './temp/' + file_name
        if os.path.exists(local):
            os.remove(local)

        result = sftp_download(remote, local)
        if result[0]:
            # 将下载的文件复制到桌面
            desktop = os.path.join(get_desktop(), file_name)
            if os.path.exists(desktop):
                os.remove(desktop)
            shutil.copy(local, desktop)
            return True, desktop
        else:
            return result
