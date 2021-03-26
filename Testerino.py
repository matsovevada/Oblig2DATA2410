from flask import jsonify
import requests
import json

BASE = "http://127.0.0.1:5000/api/"

print('------------------------------------------')
print('RESULT FROM GET:')
response = requests.get(BASE + "users")
print(response.json())
