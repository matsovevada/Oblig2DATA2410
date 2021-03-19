from flask import jsonify
import requests
import json

BASE = "http://127.0.0.1:5000/"

print('------------------------------------------')
print('RESULT FROM POST:')
response = requests.post(BASE + "employee/1", {'name': "Julia Hendricks", 'age': 32, 'position': "doggy"})
print(response)
print('------------------------------------------')
print('RESULT FROM GET:')
response = requests.get(BASE + "employee/1")
print(response.json())
print('------------------------------------------')
print('RESULT FROM PUT:')
response = requests.put(BASE + "employee/1", {'name': "Julia Jo", 'age': 27, 'position': "doggy"})
print(response.json())
print('------------------------------------------')
print('RESULT FROM GET:')
response = requests.get(BASE + "employee/1")
print(response.json())
print('------------------------------------------')
print('RESULT FROM DELETE:')
response = requests.delete(BASE + "employee/1")
print(response.json())
print('------------------------------------------')
print('RESULT FROM GET:')
response = requests.get(BASE + "employee/1")
print(response.json())
