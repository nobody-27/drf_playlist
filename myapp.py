import requests
# __url = "http://127.0.0.1:8000/api/student_api/"
# r = requests.get(url=__url)
# data = r.json()
# print(data)
import json
__url = "http://127.0.0.1:8000/api/student_create/"

data = {
    "name":"neeraj12",
    "roll":127,
    "city":"radfsa"
}

json_data = json.dumps(data)
r = requests.post(url= __url,data = json_data)
print(r.status_code)
print(r.text)

