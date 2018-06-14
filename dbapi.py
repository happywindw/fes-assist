# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from feslogs import logger
from settings import pro_db, bank_dict


class DataBaseApi(object):
    # 创建对象的基类:
    Base = declarative_base()
    # 初始化数据库连接:
    engine = create_engine('oracle+cx_oracle://%(username)s:%(password)s@%(host)s:%(port)s/%(sid)s' % pro_db)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    def __init__(self, exception_thread):
        try:
            self.session = self.DBSession()
            self.et = exception_thread
        except Exception as e:
            logger.error('Database Error: %s' % e)

    def reconnect(self):
        try:
            self.session.close()
        except Exception as e:
            logger.error('Session close exception: %s' % e)
            return False

        try:
            self.session = self.DBSession()
            return True
        except Exception as e:
            logger.error('Create session exception: %s' % e)
            return False

    def account_check(self, tran_date, settle_type, is_check, org_nick_name):
        """
        查询是否已对账及(待)对账总金额、笔数
        :param tran_date:
        :param settle_type:
        :param is_check: 是否已对账
        :param org_nick_name:
        :return:
        """
        try:
            res = self.session.execute("select sum(total_amt), count(1) from fes_online_detail where settle_type='%s' "
                                       "and tran_date='%s' and is_check='%s' and org_nick_name='%s' group by tran_date"
                                       % (settle_type, tran_date, is_check, org_nick_name))
            return res.fetchone()
        except Exception as e:
            logger.error('DatabaseError: %s' % e)
            self.et.show_exception(('DatabaseError', e))
            return []

    def get_repeat_aae076(self, tran_date, org_nick_name):
        """
        查询同行重复的aae076
        :param tran_date:
        :param org_nick_name:
        :return:
        """
        try:
            bank_code = bank_dict.get(org_nick_name)[1]
            repeats = []
            for k, v in bank_dict.items():
                if bank_code == v[1]:
                    res = self.session.execute("select aae076,count(1) from fes_online_detail where settle_type='%s' "
                                               "and tran_date='%s' and is_check='0' and org_nick_name='%s' group by "
                                               "aae076 having count(1)>1" % (v[0], tran_date, k)).fetchall()
                    if res:
                        for r in res:
                            repeats.append((k, r[0], r[1]))
            return repeats
        except Exception as e:
            self.et.show_exception(('DatabaseError', e))
            self.et.show_exception(e)
            return []

    def get_aae076_detail(self, aae076):
        """
        查询指定aae076的详细信息
        :param aae076:
        :return:
        """
        try:
            res = self.session.execute("select t.aae076, t.trans_status, t.fund_status, t.id, t.total_amt from "
                                       "fes_online_detail t where aae076='%s' order by t.id" % aae076)
            return res.fetchall()
        except Exception as e:
            self.et.show_exception(('DatabaseError', e))
            self.et.show_exception(e)
            return []

    def delete_repeat_aae076(self, delete_id):
        """
        根据指定ID删除aae076重复的记录
        :param delete_id:
        :return:
        """
        try:
            sql = "delete from fes_online_detail where id='%s'" % delete_id
            logger.debug('Execute SQL: %s' % sql)
            self.session.execute(sql)
            self.session.commit()
        except Exception as e:
            self.et.show_exception(('DatabaseError', e))
            return [('exception', e)]
        return False

    def get_diff(self, tran_date, org_nick_name):
        """
        查询是否存在单边账
        :param tran_date:
        :param org_nick_name:
        :return:
        """
        try:
            res = self.session.execute("select * from fes_check_file_diff t where t.org_nick_name='%s' and "
                                       "t.check_date='%s'" % (org_nick_name, tran_date))
            return res.fetchall()
        except Exception as e:
            self.et.show_exception(('DatabaseError', e))
            self.et.show_exception(e)
            return []

    def get_settle_date(self, tran_date, settle_type, org_nick_name):
        """
        查询清算日期
        :param tran_date:
        :param settle_type:
        :param org_nick_name:
        :return:
        """
        try:
            res = self.session.execute("select t.settle_date from fes_online_detail t where t.settle_type='%s' and "
                                       "t.tran_date='%s' and t.is_check='1' and org_nick_name='%s' and rownum<=1" %
                                       (settle_type, tran_date, org_nick_name))
            return res.fetchone()[0]
        except Exception as e:
            self.et.show_exception(('DatabaseError', e))
            self.et.show_exception(e)
            return ''

    def settle_check(self, tran_date, settle_type, org_nick_name):
        """
        清算后查询资金流向状态
        :param tran_date:
        :param settle_type:
        :param org_nick_name:
        :return:
        """
        try:
            res = self.session.execute("select t.settle_amt, t.is_confirmed, t.settle_status, t.current_direction from "
                                       "fes_settle_log t where t.settle_log_id in (select settle_log_id from "
                                       "fes_online_detail where settle_type='%s' and tran_date='%s' and  is_check='1' "
                                       "and org_nick_name='%s')" % (settle_type, tran_date, org_nick_name))
            return res.fetchall()
        except Exception as e:
            self.et.show_exception(('DatabaseError', e))
            self.et.show_exception(e)
            return []

    def confirm_check(self, tran_date, settle_type, org_nick_name):
        """
        查询是否已经确认到账及到账详情
        :param tran_date:
        :param settle_type:
        :param org_nick_name:
        :return:
        """
        try:
            res = self.session.execute("select t.tran_amt, t.status, t.is_check, t.current_direction from fes_fund_log "
                                       "t where settle_log_id in (select settle_log_id from fes_settle_log  where "
                                       "settle_log_id in (select settle_log_id from fes_online_detail where "
                                       "settle_type='%s' and tran_date='%s' and is_check='1' and org_nick_name='%s'))"
                                       % (settle_type, tran_date, org_nick_name))
            return res.fetchall()
        except Exception as e:
            self.et.show_exception(('DatabaseError', e))
            self.et.show_exception(e)
            return []

    def get_write_back_list(self, set_date, file_type):
        try:
            res = self.session.execute("select t.ctrast_no 对账关联号,t.bank_code 银行码,u.itemval 银行名称,"
                                       "t.aae036 入库时间,t.tran_date 报盘给银行时间,t.hp_date 回盘时间, "
                                       "decode(t.bankstatus,'2','成功','3','失败') 扣款结果,count(1) 笔数,sum(t.total_amt)"
                                       " 金额 from fes_sumbusi_detail t left join sys_dict_item u on "
                                       "t.bank_code=u.itemkey and u.dict='bank_code' where t.res_busi_seq in "
                                       "(select t.file_name from fes_file_log t where t.request_type='2' and "
                                       "t.set_date='%s' and t.file_type='%s') group by t.ctrast_no,t.bank_code,"
                                       "u.itemval,t.aae036,t.tran_date,t.hp_date,t.bankstatus "
                                       "order by t.bank_code,t.bankstatus" % (set_date, file_type))
            return res.fetchall()
        except Exception as e:
            print(e)

    def get_write_failed_c(self, tran_date):
        try:
            set_date = tran_date[:-2] + '%'
            res = self.session.execute("select t.ctrast_no 对账关联号,t.bank_code 银行码,u.itemval 银行名称,"
                                       "decode(t.writeback_status,'W1','未回写','W2','已回写') 回写状态,"
                                       "t.bankstatus 交易状态码,v.itemval 交易状态,count(1) 笔数,sum(t.total_amt) 金额,"
                                       "t.tran_date 报盘给银行时间 from fes_sumbusi_detail t  left join sys_dict_item u "
                                       "on t.bank_code=u.itemkey and u.dict='bank_code' left join sys_dict_item v on "
                                       "t.bankstatus=v.itemkey and v.dict='bankstatus' where t.req_busi_seq in "
                                       "(select t.file_name from fes_file_log t where t.set_date like '%s' and "
                                       "t.tran_date!='%s' and t.file_type='C' and t.request_type='1') and "
                                       "t.writeback_status='W1' and t.bankstatus not in ('13','16') and "
                                       "t.bankstatus<>'0' group by t.ctrast_no,t.bank_code,u.itemval,t.writeback_status,"
                                       "t.bankstatus,t.tran_date,v.itemval order by t.ctrast_no,t.bank_code,u.itemval,"
                                       "t.writeback_status,t.bankstatus" % (set_date, tran_date))
            return res.fetchall()
        except Exception as e:
            print(e)

    def get_write_failed_d(self, tran_date):
        try:
            set_date = tran_date[:-2] + '%'
            res = self.session.execute("select t.ctrast_no 对账关联号,u.itemval 银行名称,t.bank_code 银行码,"
                                       "t.yad050_in 收款银行码,t.yad050_out 付款银行码,t.aae036 入库时间,"
                                       "t.check_datetime 审批时间,t.tran_date 报盘给银行时间,t.hp_date 回盘时间,"
                                       "decode(t.writeback_status,'W1','未回写','W2','已回写') 回写状态,"
                                       "v.itemval 交易状态,count(1) 笔数,sum(t.total_amt) 金额 from fes_sumbusi_detail t "
                                       "left join sys_dict_item u on t.bank_code=u.itemkey and u.dict='bank_code' left "
                                       "join sys_dict_item v on t.bankstatus=v.itemkey and v.dict='bankstatus' where "
                                       "t.req_busi_seq in (select t.file_name from fes_file_log t where t.set_date "
                                       "like '%s' and t.file_type='D' and t.request_type='1') and "
                                       "t.writeback_status='W1' and t.bankstatus not in ('13','16') and "
                                       "t.bankstatus<>'0' and t.tran_date<>'%s' group by t.ctrast_no,u.itemval,"
                                       "t.writeback_status,v.itemval,t.bank_code,t.yad050_in,t.yad050_out,t.aae036,"
                                       "t.check_datetime,t.tran_date,t.hp_date order by t.ctrast_no,t.check_datetime,"
                                       "t.tran_date,t.hp_date,u.itemval,t.bank_code,t.writeback_status,t.aae036;" %
                                       (set_date, tran_date))
            return res.fetchall()
        except Exception as e:
            print(e)

    def get_send_bank(self, tran_date):
        try:
            res = self.session.execute("select t.batch_no 报银行批次号,u.itemval  ,decode(t.is_entrust,'1','委托',"
                                       "'非委托') 是否委托, decode(t.is_cbs,'1','CBS代扣','非CBS代扣')是否CBS代扣,"
                                       "decode(t.file_type,'C','代收','代发') 收付类型,t.tran_date 报盘日期,"
                                       "t.tran_time 报盘时间, decode(t.batch_status,'11','报盘成功','12','回盘成功','13',"
                                       "'报盘失败') 批次状态,t.total_amt 总金额,t.total_num 总笔数,t.usage 用途 from "
                                       "fes_sendbankfile_log t left join sys_dict_item u on t.bank_code=u.itemkey and "
                                       "u.dict='bank_code' where t.tran_date='%s' order by t.file_type,"
                                       "t.tran_date,t.tran_time,t.batch_no;" % tran_date)
            return res.fetchall()
        except Exception as e:
            print(e)

    def get_online_detail(self, tran_date_list):
        try:
            if len(tran_date_list) == 1:
                tran_str = '=' + tran_date_list[0]
            else:
                tran_str = 'in ('
                for td in tran_date_list:
                    tran_str += td + ','
                    pass
                tran_str = tran_str[:-1] + ')'
            res = self.session.execute("select decode(t.org_nick_name,'CCBAPP','建行APP','CCBPOS','建行POS','GHAPP',"
                                       "'工行APP','GHIMAC','工行一体机','GHPOS','工行POS','ZHPOS','招行POS') 联机类型,"
                                       "t.tran_date 交易日期,decode(t.is_check,'1','正常','0','单边')是否单边业务,"
                                       "count(1) 笔数,sum(t.total_amt) 金额 from fes_online_detail t where "
                                       "t.tran_date'%s' and t.org_nick_name is not null group by "
                                       "t.org_nick_name,t.tran_date,t.is_check order by t.org_nick_name;" % tran_str)
            return res.fetchall()
        except Exception as e:
            print(e)

    def get_e2e_detail(self, tran_date):
        try:
            res = self.session.execute("select t.yad107 业务批次号,t.aae036 提交FES时间,t.check_datetime 审批时间,"
                                       "t.tran_date 报盘给银行时间,decode(t.bankstatus,'2','成功','3','失败','其他') "
                                       "转账状态,count(1) 笔数,sum(t.total_amt) 金额 from fes_e2e_detail t where "
                                       "t.tran_date='%s' group by t.yad107,t.aae036,t.check_datetime,t.tran_date,"
                                       "t.bankstatus order by t.yad107,t.aae036,t.check_datetime,t.tran_date,"
                                       "t.bankstatus" % tran_date)
            return res.fetchall()
        except Exception as e:
            print(e)

    def execute_sql(self, sql):
        return self.session.execute(sql).fetchall()

