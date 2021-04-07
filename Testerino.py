from flask import jsonify
import requests
import json

BASE = "http://127.0.0.1:5000/"

print('------------------------------------------')
print('RESULT FROM POST:')
response = requests.post(BASE + "api/users", json={'name': "Peter"})
print(response.json())

print('------------------------------------------')
print('RESULT FROM GET:')
response = requests.get(BASE + "1/api/rooms")
print(response.json())

print('------------------------------------------')
print('RESULT FROM GET:')
response = requests.get(BASE + "696969/api/rooms")
print(response.json())

print('------------------------------------------')
print('RESULT FROM POST:')
response = requests.post(BASE + "1/api/rooms", json={'name': "Koserom"})
print(response.json())

print('------------------------------------------')
print('RESULT FROM POST:')
response = requests.post(BASE + "7000/api/rooms", json={'name': "Koserom"})
print(response.json())

print('------------------------------------------')
print('RESULT FROM PUT:')
response = requests.put(BASE + "rooms/1/1/messages", json={'msg': "Hei, dette fungerer"})
print(response.json())

print("STOPP ELLER?")

print('------------------------------------------')
print('RESULT FROM GET:')
response = requests.get(BASE + "1/api/rooms/1000/users")
print(response.json())



print("@@@@@@@@@@@@@@@@@@@@@@@@")

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
