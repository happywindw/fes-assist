# -*- coding: utf-8 -*-
from dbapi import DataBaseApi


class FesBusi(object):
    def __init__(self):
        self.db = DataBaseApi()

    def check_account(self, tran_date, settle_type, org_nick_name):
        uncheck = self.db.account_check(tran_date, settle_type, 0, org_nick_name)
        if uncheck:  # 未对账
            print('未对账：', uncheck)
            pass
        else:
            check = self.db.account_check(tran_date, settle_type, 1, org_nick_name)
            if check:  # 已对账
                print('yi对账：', check)
                pass
            else:    # 无业务
                print('无业务')
                pass

