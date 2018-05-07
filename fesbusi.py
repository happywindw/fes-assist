# -*- coding: utf-8 -*-
from dbapi import DataBaseApi


class FesBusi(object):
    def __init__(self):
        self.db = DataBaseApi()

    def check_account(self, tran_date, settle_type, org_nick_name):
        is_check = self.db.account_check(tran_date, settle_type, 1, org_nick_name)
        if not is_check:
            uncheck = self.db.account_check(tran_date, settle_type, 0, org_nick_name)
            if uncheck:
                print('未对账：', is_check)
                pass
            else:
                print('无业务')
        else:
            print('yi对账：', is_check)
            settle_date = self.db.get_settle_date(tran_date, settle_type, org_nick_name)
            print('settle date:', settle_date)
            pass

