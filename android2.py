import requests
import json
# URL = "http://127.0.0.1:8000/model_serilizers/model_serilizers_curd_operation/"

URL = "http://127.0.0.1:8000/function/function_based/"

def get_data(id = None):
    data = {} 
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {
        'content-Type':'application/json'
    }
    r = requests.get(url=URL,headers=headers,data=json_data)
    data = r.json()
    print(data)

get_data()

def post_data():
    data = {
        'name':"323423",
        'roll':2000,
        'city':"Dhanbad"
    }
    headers = {
        'content-Type':'application/json'
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL,headers=headers,data=json_data)
    data = r.json()
    print(data)

# post_data()

def update_data():
    data = {
        'id':34,
        'name':"same",
        'roll':1211,
        'city':"Dhanbad"
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL,data=json_data)
    data = r.json()
    print(data,"update data")

# update_data()


def delete_data():
    data = {
        'id':4
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL,data=json_data)
    data = r.json()
    print(data)

# delete_data()