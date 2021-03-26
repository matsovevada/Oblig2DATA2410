from flask import jsonify
import requests
import json

BASE = "http://127.0.0.1:5000/api/"
print('------------------------------------------')
print('RESULT FROM GET:')
response = requests.get(BASE + "rooms/0/messages")
print(response.json())

print('------------------------------------------')
print('RESULT FROM PUT:')
response = requests.put(BASE + "rooms/0/users/0")
print(response.json())

print('------------------------------------------')
print('RESULT FROM PUT:')
response = requests.put(BASE + "rooms/0/0/messages", json={'msg': "Hei, dette fungerer"})
print(response.json())

print('------------------------------------------')
print('RESULT FROM GET:')
response = requests.get(BASE + "rooms/0/messages")
print(response.json())



# print('------------------------------------------')
# print('RESULT FROM GET:')
# response = requests.get(BASE + "users")
# print(response.json())
#
# print('------------------------------------------')
# print('RESULT FROM POST:')
# response = requests.post(BASE + "users", json={'name': "Peter"})
# print(response.json())
#
# print('------------------------------------------')
# print('RESULT FROM GET:')
# response = requests.get(BASE + "users/2")
# print(response.json())
#
# print('------------------------------------------')
# print('RESULT FROM DELETE:')
# response = requests.delete(BASE + "users/1")
# print(response.json())
#
# print('------------------------------------------')
# print('RESULT FROM GET:')
# response = requests.get(BASE + "users/1")
# print(response.json())
#
# print('------------------------------------------')
# print('RESULT FROM DELETE:')
# response = requests.delete(BASE + "users")
# print(response.json())
#
# print('------------------------------------------')
# print('RESULT FROM GET:')
# response = requests.get(BASE + "users/0")
# print(response.json())
#
# print('------------------------------------------')
# print('RESULT FROM GET:')
# response = requests.get(BASE + "users")
# print(response.json())
