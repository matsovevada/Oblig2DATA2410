from flask import jsonify
import requests
import json


BASE = "http://127.0.0.1:5000/"

print('------------------------------------------')
print('RESULT FROM GET:')
response = requests.get(BASE + "1/api/rooms/1000/users")
print(response.json())

print('------------------------------------------')
print('RESULT FROM PUT:')
response = requests.put(BASE + "1000/api/rooms/0/users")
print(response.json())

#"/<int:userID>/api/rooms/<int:roomID>/messages", "/<int:userID>/api/rooms/<int:roomID>/<int:target_userID>/messages")

print('------------------------------------------')
print('RESULT FROM GET:')
response = requests.get(BASE + "1/api/rooms/0/messages")
print(response.json())

print('------------------------------------------')
print('RESULT FROM PUT:')
response = requests.put(BASE + "4/api/rooms/0/messages", json={'msg': "Hei, dette fungerer"})
print(response.json())
