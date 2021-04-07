from flask import jsonify
import requests
import json

BASE = "http://127.0.0.1:5000/"

#USER

# get a specific user
def get_specific_user(userID):
    response = requests.get(BASE + f"api/users/{userID}")
    return response.json()

# get all users
def get_all_users():
    response = requests.get(BASE + "api/users")
    return response.json()

# register user
def register_user(name):
    response = requests.post(BASE + "api/users", json={'name': name})
    return response.json()

# delete a specific user
def delete_user(userID):
    response = requests.delete(BASE + f"api/users/{userID}")
    return response.json()

# delete all users 
def delete_all_users():
    response = requests.delete(BASE + "api/users")
    return response.json()

# CHAT_ROOM
    
# get a specific chat room
def get_room(userID, roomID):
    response = requests.get(BASE + f"{userID}/api/rooms/{roomID}")
    return response.json()


# get all chat rooms
def get_all_rooms(userID):
    response = requests.get(BASE + f"{userID}/api/rooms")
    return response.json()

# create a room
def create_room(userID, name):
    response = requests.post(BASE + f"{userID}/api/rooms", json={'name': name})
    return response.json()

# CHAT_ROOM_USERS

# join a room
def join_room(userID, roomID):
    response = requests.put(BASE + f"{userID}/api/rooms/{roomID}/users")
    return response.json()
    
# get all users in a room
def get_all_users_in_room(userID, roomID):
    response = requests.get(BASE + f"{userID}/api/rooms/{roomID}/users")
    return response.json()


# MESSAGES

# Get messsages from a speific user in a specific room
def get_messages_user(userID, target_userID, roomID):
    response = requests.get(BASE + f"{userID}/api/rooms/{roomID}/{target_userID}/messages")
    return response.json()

# Get all messages in a specific room
def get_messages_in_room(userID, roomID):
    response = requests.get(BASE + f"{userID}/api/rooms/{roomID}/messages")
    return response.json()

# send a message
def send_message(userID, roomID, msg):
    response = requests.put(BASE + f"{userID}/api/rooms/{roomID}/messages", json={"msg": msg})
    return response.json()


