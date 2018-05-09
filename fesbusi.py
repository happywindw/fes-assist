# -*- coding: utf-8 -*-
from dbapi import DataBaseApi


class FesBusi(object):
    def __init__(self):
        self.db = DataBaseApi()

    def check_status(self, tran_date, settle_type, org_nick_name, total_amt):
        status_dict = {}
        is_check, check_info = self.check_account(tran_date, settle_type, org_nick_name)
        if not is_check and not check_info:
            return {'no_business': -1}
        if not is_check:
            return {'uncheck', (check_info[0], float(check_info[1]))}
        status_dict['checked'] = (check_info[0], float(check_info[1]))

        is_settle, settle_info = self.check_settle(tran_date, settle_type, org_nick_name)
        if not is_settle:
            status_dict['unsettle'] = settle_info
            return status_dict
        else:
            status_dict['settled'] = settle_info

        is_confirm, confirm_info = self.check_confirm(tran_date, settle_type, org_nick_name)
        if not is_confirm:
            status_dict['unconfirmed'] = confirm_info
        else:
            status_dict['confirmed'] = confirm_info

        return status_dict

    def check_account(self, tran_date, settle_type, org_nick_name):
        is_check = self.db.account_check(tran_date, settle_type, 1, org_nick_name)
        if not is_check:
            uncheck = self.db.account_check(tran_date, settle_type, 0, org_nick_name)
            if uncheck:  # 未对账
                return False, uncheck
            else:        # 无业务
                return False, ()
        else:            # 已对账
            return True, is_check

    def check_settle(self, tran_date, settle_type, org_nick_name):
        settle_res = self.db.settle_check(tran_date, settle_type, org_nick_name)
        if settle_res:  # 已清算
            return True, settle_res
        else:           # 未清算
            return False, ()

    def check_confirm(self, tran_date, settle_type, org_nick_name):
        confirm_res = self.db.confirm_check(tran_date, settle_type, org_nick_name)
        if confirm_res:  # 已确认到账
            return True, confirm_res
        else:            # 未确认到账
            return False, ()

