import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE+ 'helloworld/bh')

print(response.json())

# response = requests.post(BASE+ 'helloworld')

# print(response.json())