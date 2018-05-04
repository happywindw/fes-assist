from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from settings import test_db


class DataBaseApi(object):
    # 创建对象的基类:
    Base = declarative_base()
    # 初始化数据库连接:
    engine = create_engine('oracle+cx_oracle://%(username)s:%(password)s@%(host)s:%(port)s/%(sid)s' % test_db)
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    def __init__(self):
        self.session = self.DBSession()

    def execute_sql(self, sql):
        return self.session.execute(sql)


# test
dba = DataBaseApi()
res = dba.session.execute(r"select * from fes_online_detail where rownum<=5")
for i in res:
    print(i)
