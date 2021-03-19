from flask import jsonify
import requests
import json

BASE = "http://127.0.0.1:5000/"

print('------------------------------------------')
print('RESULT FROM GET:')
response = requests.get(BASE + "employee/2")
print(response.json())

print('------------------------------------------')
print('RESULT FROM POST:')
response = requests.post(BASE + "employee/2", json={'name': "Mats Ove", 'age': 23, 'position': "69"})
print(response.json())

print('------------------------------------------')
print('RESULT FROM GET:')
response = requests.get(BASE + "employee/2")
print(response.json())

print('------------------------------------------')
print('RESULT FROM PUT:')
response = requests.put(BASE + "employee/2", json={'name': "Mats Ove Vada", 'age': 27, 'position': "Mijsonær"})
print(response.json())

print('------------------------------------------')
print('RESULT FROM GET:')
response = requests.get(BASE + "employee/2")
print(response.json())

print('------------------------------------------')
print('RESULT FROM DELETE:')
response = requests.delete(BASE + "employee/2")
print(response.json())

print('------------------------------------------')
print('RESULT FROM GET:')
response = requests.get(BASE + "employee/2")
print(response.json())
