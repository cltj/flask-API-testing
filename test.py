import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/8", {"name": "Not a Shithole", "views":1000, "likes":150})
print(response.json())
input()
response = requests.get(BASE + "video/8")
print(response.json())
input()
response = requests.patch(BASE + "video/8", {"views":4300, "likes":2200})
print(response.json())
input()
response = requests.delete(BASE + "video/8")
print(response)
