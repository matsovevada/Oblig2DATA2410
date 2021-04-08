from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
import json
import requests
import random
import socket
import threading

app = Flask(__name__)
api = Api(app)

#Server socket
PORT = 5001
SERVER = 'localhost'
ADDR = (SERVER, PORT)

connections = []


def server():
    print("SERVER LISTENING...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(ADDR)

    while True:
        server.listen()
        conn, addr = server.accept()
        connections.append(conn)
        print("Connected")


def notify(alert):
    if alert:
        msg = "Halloi"
        for conn in connections:
            conn.send(msg.encode("utf-8"))


thread = threading.Thread(target=server)
thread.start()

users = {}

# 1: {'name': "testerinoroom", 'users': [{'username' : "Testerino 2" , 'userID' : 1}], 'messages': []}
rooms = {}


def abort_if_user_not_exists(userID):
    if userID not in users:
        abort(404, message="Your userID is not registered in the system...")


def abort_if_target_user_not_exists(target_userID):
    if target_userID not in users:
        abort(404, message="Could not find targeted user...")


def abort_if_room_not_exists(roomID):
    if roomID not in rooms:
        abort(404, message="Could not find room...")


def abort_if_room_exists(roomID):
    if roomID in rooms:
        abort(404, message="Room already exists...")


def user_in_room(roomID, userID):
    #[{'name': 'Testerino'}]
    user_in_room = False
    for user in rooms[roomID]['users']:
        if user['userID'] == userID:
            user_in_room = True

    return user_in_room


class User(Resource):

    def get(self, target_userID=None):
        userID = request.json['userID']
        abort_if_user_not_exists(userID)
        # get a specific user
        if (target_userID):
            abort_if_target_user_not_exists(target_userID)
            return {"status": 200, "message": "OK", "user": users[target_userID]}

        # get all users
        else:
            return {"status": 200, "message": "OK", "users": users}

    def post(self):
        name = request.json['name']
        userID = random.randint(1,10000)
        while userID in users:
            userID = random.randint(1,10000)
        users[userID] = {'name' : name}
        return {"status": 201, "message": "User successfully added", "user": users[userID], "userID": userID} 

    def delete(self, target_userID=None):
        global users
        userID = request.json['userID']
        abort_if_user_not_exists(userID)
        # delete a specific user
        if (target_userID):
            abort_if_target_user_not_exists(target_userID)
            user = users[target_userID]
            del users[target_userID]
            return {"status": 410, "message": "User successfully deleted", "user" : user}

        # delete all users
        else: 
            users = {}
            return {"status": 410, "message": "All users successfully deleted"}


class Chat_room(Resource):

    def get(self, roomID=None):
        userID = request.json['userID']
        abort_if_user_not_exists(userID)

        # get a specific chat room
        if (roomID):
            abort_if_room_not_exists(roomID)
            return {'status': 200, 'message': "OK", 'room': rooms[roomID]}

        # get all chat rooms
        else:
            return {'status': 200, 'message': "OK", 'rooms': rooms}

    def post(self):
        userID = request.json['userID']
        abort_if_user_not_exists(userID)
        name = request.json['name']
        roomID = random.randint(1,1000)
        while roomID in rooms:
            roomID = random.randint(1,1000)
        users = []
        messages = []
        rooms[roomID] = {'name': name, 'users': users, 'messages': messages}
        return {'status': 201, 'message': "Room sucessfully created", 'room': roomID, 'name': name}

class Chat_room_users(Resource):
    
    # get all users in a room
    def get(self, roomID):
        userID = request.json['userID']
        abort_if_user_not_exists(userID)
        abort_if_room_not_exists(roomID) 
        return {"status": 200, "message": "OK", "Room users": rooms[roomID]['users']}

    def put(self, roomID):
        abort_if_room_not_exists(roomID)
        userID = request.json['userID']
        abort_if_user_not_exists(userID)
        if user_in_room(roomID, userID):
             abort(404, message="User is already in room")
        
        user = users[userID]
        rooms[roomID]['users'].append({'Username': user, 'userID' : userID})
        return {"status": 200, "message": "Successfully added user to room " + rooms[roomID]['name'], "Room users": rooms[roomID]['users']}

class Messages(Resource):

    # Gets messsages from user if userID is defined, gets all messages if not defined 
    def get(self, roomID, target_userID=None):
        abort_if_room_not_exists(roomID)
        userID = request.json['userID']
        abort_if_user_not_exists(userID)
        if not user_in_room(roomID, userID):
            abort(404, message="User not in room")
        # Return all messages from specific user
        if (target_userID):
            msgs = []
            abort_if_target_user_not_exists(target_userID)
            for msg in rooms[roomID]['messages']:
                if (msg['userID'] == target_userID):
                    msgs.append(msg)
            return {"status": 200, "message": "OK", "User-messages: ": msgs}
        # Return all messages in given room
        else:
            msgs = []
            for msg in rooms[roomID]['messages']:
                    msgs.append(msg)
            return {"status": 200, "message": "OK", "All messages: ": msgs}

        # Send message, check if user is in room and appened to messages in room
    def put(self, roomID):
        abort_if_room_not_exists(roomID)
        userID = request.json['userID']
        abort_if_user_not_exists(userID)
        if not user_in_room(roomID, userID):
            abort(404, message="User not in room")

        msg = {'userID' : userID, 'msg_content' : request.json['msg']}
        rooms[roomID]['messages'].append(msg)
        #notify 
        alert = "string"
        notify(alert)

        return {"status": 401, "message": "Message sent"}


api.add_resource(User, "/api/users", "/api/users/<int:target_userID>")
api.add_resource(Chat_room, "/api/rooms", "/api/rooms/<int:roomID>")
api.add_resource(Chat_room_users, "/api/rooms/<int:roomID>/users")
api.add_resource(Messages, "/api/rooms/<int:roomID>/messages",
                 "/api/rooms/<int:roomID>/<int:target_userID>/messages")

if __name__ == "__main__":
    app.run(debug=True)
