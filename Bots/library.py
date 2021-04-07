from flask import jsonify
import requests
import json

BASE = "http://127.0.0.1:5000/"

#USER

# get a specific user
def get_specific_user(userID):
    response = requests.get(BASE + "api/users")
    return response.json()

# get all users

# register user
def register_user(name):
    response = requests.post(BASE + "api/users", json={'name': name})
    return response.json()

# delete a specific user 

# delete all users 

# CHAT_ROOM
    
# get a specific chat room

# get all chat rooms
def get_all_rooms(userID):
    response = requests.get(BASE + f"{userID}/api/rooms")
    return response.json()

# create a room

# CHAT_ROOM_USERS
    
# get all users in a room

# join a room
def join_room(userID, roomID):
    response = requests.put(BASE + f"{userID}/api/rooms/{roomID}/users")
    return response.json()

# MESSAGES

# Get messsages from a specicif user in a specific room

# Get all messages in a specific room

# send a message
def send_message(userID, roomID, msg):
    response = requests.get(BASE + f"{userID}/api/rooms/{roomID}/messages", json={"msg": msg})
    return response.json()


