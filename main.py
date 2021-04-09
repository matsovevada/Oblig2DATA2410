from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
import json
import requests
import random
import socket
import threading
import pickle
import library as lib

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

        # recieve id from bot when it has registered and appned it to connections-list
        bot_id = conn.recv(1024).decode()
        connections.append((conn, int(bot_id)))

        print(f"Bot with ID {bot_id} Connected")


def notify(roomID, sender_id):
    if roomID:
        print("got roomID")
        room_name = rooms[roomID]['name']
        response = {'msg' : f"Message received in {room_name}!", 'roomID' : roomID}

        # send push notification only to users connected to the room the message was sent in and don't send back to the sender
        for user in rooms[roomID]['users']:
            if user['userID'] != sender_id:

                for conn in connections:
                    if conn[1] == user['userID']:
                        conn[0].send(pickle.dumps(response))
                        
users = {
    1: {'name': "Bob"}
}

# default chat rooms, new rooms are appended to this dictionary
rooms = {
    1: {'name': "General", 'users': [], 'messages': []},
    2: {'name': "Kosegruppa", 'users': [], 'messages': []},
    3: {'name': "Lørdagspils", 'users': [], 'messages': []},
    4: {'name': "Breakoutroom", 'users': [], 'messages': []}
    }


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

        if name == 'Quiz-master':
            userID = 1
        
        else:
            userID = random.randint(2,10000)
            while userID in users:
                userID = random.randint(2,10000)
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
        
        user = users[userID]['name']
        rooms[roomID]['users'].append({'Username': user, 'userID' : userID})
        # rooms[roomID]['users'].append({'user': user})
        return {"status": 200, "message": "Successfully added user to room " + rooms[roomID]['name'], "Room users": rooms[roomID]['users'], "Room name": rooms[roomID]['name']}

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
            return {"status": 200, "message": "OK", "All messages:": msgs}

        # Send message, check if user is in room and appened to messages in room
    def put(self, roomID):
        abort_if_room_not_exists(roomID)
        userID = request.json['userID']
        abort_if_user_not_exists(userID)

        if userID != 1 and not user_in_room(roomID, userID): # userID 1 is reserved for the quiz master and quiz master is allowed to send messages in rooms it is not a part of
            abort(404, message="User not in room")

        # Adds message to room, msgID is used to keep track of messages for printing to the client
        msgID = len(rooms[roomID]['messages']) + 1
        msg = {'userID' : userID, 'msg_content' : request.json['msg'], 'msgID' : msgID}
        rooms[roomID]['messages'].append(msg)

        #Notify client when a messages is received in room 
        notify(roomID, userID)

        return {"status": 401, "message": "Message sent"}


if __name__ == "__main__":
    
    api.add_resource(User, "/api/users", "/api/users/<int:target_userID>")
    api.add_resource(Chat_room, "/api/rooms", "/api/rooms/<int:roomID>")
    api.add_resource(Chat_room_users, "/api/rooms/<int:roomID>/users")
    api.add_resource(Messages, "/api/rooms/<int:roomID>/messages",
                    "/api/rooms/<int:roomID>/<int:target_userID>/messages")

    thread = threading.Thread(target=server)
    thread.start()

    app.run(debug=False)    
   
