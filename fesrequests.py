import json
import requests

data = {
  "trans_code": "2301",
  "check_date": "20180502",
  "org_nick_name": "GHPOS",
  "task_en_name": "CHECKFILE"
}

rep = requests.post('http://10.200.24.47:6080/fes-service/busi-api/2301', data=json.dumps(data))
print(rep.text)


class FesRequest(object):
    def __init__(self, trans_code):
        self.trans_code = trans_code

    def post(self, msg):
        pass


# 联机交易对账请求
class FesB2301(FesRequest):
    def __init__(self, check_date, org_nick_name):
        super().__init__("2301")
        self.check_date = check_date
        self.org_nick_name = org_nick_name

    def post(self, msg):
        print(msg)
        pass
