from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
import json
import requests


app = Flask(__name__)
api = Api(app)

users = {
    0: {'name': "Testerino"},
    1: {'name': "Testerino 2"},
    }

rooms = {0: {'name': "testerinoroom", 'users': [{'username' : "Test" , 'userID' : 4}], 'messages': []}}

def abort_if_user_not_exists(userID):
    if userID not in users:
        abort(404, message="Could not find User...")


def abort_if_user_exists(userID):
    if userID in users:
        abort(404, message="User already exists...")


def abort_if_room_not_exists(roomID):
    if roomID not in rooms:
        abort(404, message="Could not find room...")


def abort_if_room_exists(roomID):
    if roomID in rooms:
        abort(404, message="Room already exists...")

def abort_if_user_not_in_room(roomID, userID):
    #[{'name': 'Testerino'}]
    user_in_room = False
    for user in rooms[roomID]['users']:
        if user['userID'] == userID:
            user_in_room = True

    if not user_in_room:
        abort(404, message="Not allowed, user not in room...")

class User(Resource):
    
    def get(self, userID=None):

        # get a specific user
        if (userID or userID == 0): 
            abort_if_user_not_exists(userID)
            return {"status": 200, "message": "OK", "user": users[userID]}

        # get all users
        else:
            return {"status": 200, "message": "OK", "users": users}

    def post(self, userID=None):
        name = request.json['name']
        userID = len(users)
        users[userID] = {'name' : name}
        return {"status": 201, "message": "User successfully added", "user": users[userID]} 

    def delete(self, userID=None):
        global users

        # delete a specific user
        if (userID or userID == 0):
            abort_if_user_not_exists(userID)
            user = users[userID]
            del users[userID]
            return {"status": 410, "message": "User successfully deleted", "user" : user}

        # delete all users
        else: 
            users = {}
            return {"status": 410, "message": "All users successfully deleted"}


class Chat_room(Resource):
    def get(self, roomID=None):

        # get a specific chat room
        if (roomID or roomID == 0):
            abort_if_room_not_exists(roomID)
            return {'status': 200, 'message': "OK", 'room': rooms[roomID]}

        # get all chat rooms
        else:
            return {'status': 200, 'message': "OK", 'rooms': rooms}

    def post(self, roomID=None):
        name = request.json['name']
        roomID = len(rooms)
        users = []
        messages = []
        rooms[roomID] = {'name': name, 'users': users, 'messages': messages}
        return {'status': 201, 'message': "Room sucessfully created", 'room': roomID, 'name': name}

class Chat_room_users(Resource):
    
    # get all users in a room
    def get(self, roomID):
        abort_if_room_not_exists(roomID) 
        return {"status": 200, "message": "OK", "Room users": rooms[roomID]['users']}

    def put(self, roomID, userID):
        abort_if_room_not_exists(roomID)
        abort_if_user_not_exists(userID)
        user = users[userID]
        rooms[roomID]['users'].append({'Username': user, 'userID' : userID})
        return {"status": 200, "message": "Successfully added user to room " + rooms[roomID]['name'], "Room users": rooms[roomID]['users']}

class Messages(Resource):

    # Gets messsages from user if userID is define, gets all messages if not defined 
    def get(self, roomID, userID = None):
        abort_if_room_not_exists(roomID)
        # Return all messages from specific user
        if (userID or userID == 0):
            abort_if_user_not_exists(userID)
            abort_if_user_not_in_room(roomID, userID)
            msgs = []
            for msg in rooms[roomID]['messages']:
                if (msg['userID'] == userID):
                    msgs.append(msg)
            return {"status": 200, "message": "OK", "User-messages: ": msgs}
        # Return all messages in given room
        else:
            msgs = []
            for msg in rooms[roomID]['messages']:
                    msgs.append(msg)
            return {"status": 200, "message": "OK", "All messages: ": msgs}

        # Send message, check if user is in room and appened to messages in room
    def put(self, roomID, userID):
        abort_if_room_not_exists(roomID)
        abort_if_user_not_in_room(roomID, userID)
        msg = {'user' : userID, 'msg_content' : request.json['msg']}
        rooms[roomID]['messages'].append(msg)
        return {"status": 401, "message": "Message sent"}

api.add_resource(User, "/api/users", "/api/users/<int:userID>")
api.add_resource(Chat_room, "/api/rooms", "/api/rooms/<int:roomID>")
api.add_resource(Chat_room_users, "/api/rooms/<int:roomID>/users", "/api/rooms/<int:roomID>/users/<int:userID>")
api.add_resource(Messages, "/api/rooms/<int:roomID>/messages", "/api/rooms/<int:roomID>/<int:userID>/messages")

if __name__ == "__main__":
    app.run(debug=True)
