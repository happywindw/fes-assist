# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from settings import pro_db


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
        res = self.session.execute("select tran_date, count(1), sum(total_amt) from fes_online_detail where "
                                   "settle_type='%s' and tran_date='%s' and is_check='%s' and org_nick_name='%s' "
                                   "group by tran_date" % (settle_type, tran_date, is_check, org_nick_name))
        return res.fetchone()

    def get_settle_date(self, tran_date, settle_type, org_nick_name):
        res = self.session.execute("select t.settle_date from fes_online_detail t where t.settle_type='%s' and "
                                   "t.tran_date='%s' and t.is_check='1' and org_nick_name='%s' and rownum<=1" %
                                   (settle_type, tran_date, org_nick_name))
        return res.fetchone()[0]

    def settle_check(self):
        pass

    def confirm_check(self, tran_date, settle_type, org_nick_name):
        res = self.session.execute("select t.tran_amt, t.status, t.is_check, t.* from fes_fund_log t where "
                                   "settle_log_id in (select settle_log_id from fes_settle_log  where settle_log_id "
                                   "in (select settle_log_id from fes_online_detail where settle_type='%s' and "
                                   "tran_date='%s' and is_check='1' and org_nick_name='%s'))" %
                                   (settle_type, tran_date, org_nick_name))
        return res.fetchall()

    def execute_sql(self, sql):
        return self.session.execute(sql)


# test
# dba = DataBaseApi()
# rrr = dba.account_check('5', '20180416', '1', 'GHPOS')
# for i in rrr:
#     print(i)
