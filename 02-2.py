import requests
import json
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

dict_1=json.loads(response.text)
print(dict_1)
print(type(dict_1))
data=response.json()
print(data)
print(type(data))
print(data['title'])
params = {
    'userId' : '5',
    'completed' : 'true'
}

url = "https://jsonplaceholder.typicode.com/todos"

params = {
    "userId": "3",
    "completed": "true"
}

response = requests.get(url, params=params)

print(response.url)
print(response.status_code)
data = response.json()

print(data)
print(type(data))
for i in data:
    print(i['id'],i['title'])
data = [
    {"id": 1, "severity": "HIGH"},
    {"id": 2, "severity": "LOW"},
    {"id": 3, "severity": "CRITICAL"},
    {"id": 4, "severity": "MEDIUM"}
]
for i in data:
    if i["severity"] == "HIGH" or i["severity"] == "CRITICAL":
        print(i["id"])