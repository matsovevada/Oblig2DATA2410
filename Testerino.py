from flask import jsonify
import requests
import json

BASE = "http://127.0.0.1:5000/api/"

print('------------------------------------------')
print('RESULT FROM GET:')
response = requests.get(BASE + "users")
print(response.json())

print('------------------------------------------')
print('RESULT FROM POST:')
response = requests.post(BASE + "users", json={'name': "Peter"})
print(response.json())

print('------------------------------------------')
print('RESULT FROM GET:')
response = requests.get(BASE + "users/2")
print(response.json())
