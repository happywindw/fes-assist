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
