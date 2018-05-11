# -*- coding: utf-8 -*-
from dbapi import DataBaseApi
from fesrequests import FesB2301, FesB2304


class FesBusi(object):
    def __init__(self):
        self.db = DataBaseApi()

    def check_status(self, tran_date, settle_type, org_nick_name):
        status_dict = {}
        # 对帐查询
        is_check, check_info = self.check_account(tran_date, settle_type, org_nick_name)
        if not is_check and not check_info:  # 无业务
            return {'no_business': -1}
        if not is_check:                     # 未成功对帐
            ra = self.db.get_repeat_aae076(tran_date, org_nick_name)
            if ra:  # 存在重复的aae076
                status_dict['repeat_aae076'] = ra
                print(ra[0])
            status_dict['unchecked'] = [(check_info[0], check_info[1])]
            return status_dict
        else:                                # 已对帐
            cd = self.db.get_diff(tran_date, org_nick_name)
            if cd:  # 存在单边帐
                status_dict['check_diff'] = cd
            status_dict['checked'] = [(check_info[0], check_info[1])]

        # 清算查询
        is_settle, settle_info = self.check_settle(tran_date, settle_type, org_nick_name)
        if not is_settle:
            status_dict['unsettled'] = settle_info
            return status_dict
        else:
            status_dict['settled'] = settle_info

        # 确认到账查询
        is_confirm, confirm_info = self.check_confirm(tran_date, settle_type, org_nick_name)
        if not is_confirm:
            status_dict['unconfirmed'] = confirm_info
        else:
            status_dict['confirmed'] = confirm_info

        return status_dict

    def check_account(self, tran_date, settle_type, org_nick_name):
        """
        查询对账状态
        :param tran_date:
        :param settle_type:
        :param org_nick_name:
        :return:
        """
        is_check = self.db.account_check(tran_date, settle_type, 1, org_nick_name)
        if not is_check:
            uncheck = self.db.account_check(tran_date, settle_type, 0, org_nick_name)
            if uncheck:  # 未对账
                return False, uncheck
            else:        # 无业务
                return False, ()
        else:            # 已对账
            return True, is_check

    def deal_aae076(self):
        pass

    def check_settle(self, tran_date, settle_type, org_nick_name):
        """
        查询清算状态
        :param tran_date:
        :param settle_type:
        :param org_nick_name:
        :return:
        """
        settle_res = self.db.settle_check(tran_date, settle_type, org_nick_name)
        if settle_res:  # 已清算
            return True, settle_res
        else:           # 未清算
            return False, -1

    def check_confirm(self, tran_date, settle_type, org_nick_name):
        """
        查询到账状态
        :param tran_date:
        :param settle_type:
        :param org_nick_name:
        :return:
        """
        confirm_res = self.db.confirm_check(tran_date, settle_type, org_nick_name)
        if confirm_res:  # 已确认到账
            return True, confirm_res
        else:            # 未确认到账
            return False, -1

    def post_check_account(self, tran_date, org_nick_name):
        req_2301 = FesB2301(tran_date, org_nick_name)
        req_2301.post()

    def post_check_settle(self, tran_date, settle_type, org_nick_name):
        is_settle, settle_info = self.check_settle(tran_date, settle_type, org_nick_name)
        if is_settle:  # 避免重复清算
            return

        settle_date = self.db.get_settle_date(tran_date, settle_type, org_nick_name)
        req_2304 = FesB2304(settle_date, org_nick_name)
        req_2304.post()

