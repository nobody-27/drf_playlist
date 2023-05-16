import requests

__url = "http://127.0.0.1:8000/api/student_api/"

r = requests.get(url=__url)

data = r.json()
print(data)