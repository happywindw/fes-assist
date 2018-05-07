# -*- coding: utf-8 -*-
from dbapi import DataBaseApi


class FesBusi(object):
    def __init__(self):
        self.db = DataBaseApi()

    def check_account(self, tran_date, settle_type, org_nick_name):
        res = self.db.account_check(tran_date, settle_type, 0, org_nick_name)
        if res:  # 未对账
            pass
        else:
            res = self.db.account_check(tran_date, settle_type, 1, org_nick_name)
            if res:  # 已对账
                pass
            else:    # 无业务
                pass

