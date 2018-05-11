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

    def get_repeat_aae076(self, tran_date, settle_type, org_nick_name):
        """
        查询重复的aae076
        :param tran_date:
        :param settle_type:
        :param org_nick_name:
        :return:
        """
        res = self.session.execute("select aae076,count(1) from fes_online_detail where settle_type='%s' and "
                                   "tran_date='%s' and is_check='0' and org_nick_name='%s' group by aae076 "
                                   "having count(1)>1" % (settle_type, tran_date, org_nick_name))
        return res.fetchall()

    def delete_repeat_aae076(self, aae076):
        """
        删除重复的aae076记录
        :param aae076:
        :return:
        """
        repeats = self.session.execute("select id, settle_code from fes_online_detail t where aae076='%s'"
                                       % aae076).fetchall()
        if len(repeats) <= 1:
            return
        else:
            delete_id = repeats[0][0]
            for record in repeats:
                if record[0] > delete_id:
                    delete_id = record[0]
            self.session.execute("delete from fes_online_detail where id='%s'" % delete_id)
            self.session.commit()

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

