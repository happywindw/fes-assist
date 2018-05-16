# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from settings import pro_db, bank_dict


class DataBaseApi(object):
    # 创建对象的基类:
    Base = declarative_base()
    # 初始化数据库连接:
    engine = create_engine('oracle+cx_oracle://%(username)s:%(password)s@%(host)s:%(port)s/%(sid)s' % pro_db)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    def __init__(self):
        self.session = self.DBSession()

    def account_check(self, tran_date, settle_type, is_check, org_nick_name):
        """
        查询是否已对账及(待)对账总金额、笔数
        :param tran_date:
        :param settle_type:
        :param is_check: 是否已对账
        :param org_nick_name:
        :return:
        """
        res = self.session.execute("select sum(total_amt), count(1) from fes_online_detail where settle_type='%s' "
                                   "and tran_date='%s' and is_check='%s' and org_nick_name='%s' group by tran_date"
                                   % (settle_type, tran_date, is_check, org_nick_name))
        return res.fetchone()

    def get_repeat_aae076(self, tran_date, org_nick_name):
        """
        查询同行重复的aae076
        :param tran_date:
        :param org_nick_name:
        :return:
        """
        bank_code = bank_dict.get(org_nick_name)[1]
        repeats = []
        for k, v in bank_dict.items():
            if bank_code == v[1]:
                res = self.session.execute("select aae076,count(1) from fes_online_detail where settle_type='%s' and "
                                           "tran_date='%s' and is_check='0' and org_nick_name='%s' group by aae076 "
                                           "having count(1)>1" % (v[0], tran_date, k)).fetchall()
                if res:
                    for r in res:
                        repeats.append((k, r[0], r[1]))
        return repeats

    def get_aae076_detail(self, aae076):
        """
        查询指定aae076的详细信息
        :param aae076:
        :return:
        """
        res = self.session.execute("select t.aae076, t.trans_status, t.fund_status, t.id, t.total_amt from "
                                   "fes_online_detail t where aae076='%s'" % aae076)
        return res.fetchall()

    def delete_repeat_aae076(self, delete_id):
        """
        根据指定ID删除aae076重复的记录
        :param delete_id:
        :return:
        """
        try:
            self.session.execute("delete from fes_online_detail where id='%s'" % delete_id)
            self.session.commit()
        except Exception as e:
            print(e)
            return False
        return True

    def get_diff(self, tran_date, org_nick_name):
        """
        查询是否存在单边账
        :param tran_date:
        :param org_nick_name:
        :return:
        """
        res = self.session.execute("select * from fes_check_file_diff t where t.org_nick_name='%s' and "
                                   "t.check_date='%s'" % (org_nick_name, tran_date))
        return res.fetchall()

    def get_settle_date(self, tran_date, settle_type, org_nick_name):
        """
        查询清算日期
        :param tran_date:
        :param settle_type:
        :param org_nick_name:
        :return:
        """
        res = self.session.execute("select t.settle_date from fes_online_detail t where t.settle_type='%s' and "
                                   "t.tran_date='%s' and t.is_check='1' and org_nick_name='%s' and rownum<=1" %
                                   (settle_type, tran_date, org_nick_name))
        return res.fetchone()[0]

    def settle_check(self, tran_date, settle_type, org_nick_name):
        """
        清算后查询资金流向状态
        :param tran_date:
        :param settle_type:
        :param org_nick_name:
        :return:
        """
        res = self.session.execute("select t.settle_amt, t.is_confirmed, t.settle_status, t.current_direction from "
                                   "fes_settle_log t where t.settle_log_id in (select settle_log_id from "
                                   "fes_online_detail where settle_type='%s' and tran_date='%s' and  is_check='1' and "
                                   "org_nick_name='%s')" % (settle_type, tran_date, org_nick_name))
        return res.fetchall()

    def confirm_check(self, tran_date, settle_type, org_nick_name):
        """
        查询是否已经确认到账及到账详情
        :param tran_date:
        :param settle_type:
        :param org_nick_name:
        :return:
        """
        res = self.session.execute("select t.tran_amt, t.status, t.is_check, t.current_direction from fes_fund_log t "
                                   "where settle_log_id in (select settle_log_id from fes_settle_log  where "
                                   "settle_log_id in (select settle_log_id from fes_online_detail where "
                                   "settle_type='%s' and tran_date='%s' and is_check='1' and org_nick_name='%s'))"
                                   % (settle_type, tran_date, org_nick_name))
        return res.fetchall()

    def execute_sql(self, sql):
        return self.session.execute(sql)

