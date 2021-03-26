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

rooms = {0: {'name': "testerinoroom", 'users': [], 'messages': []}}


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


class User(Resource):
    
    def get(self, userID=None):
        if (userID or userID == 0): 
            abort_if_user_not_exists(userID)
            return {"status": 200, "message": "OK", "user": users[userID]}
        else:
            return {"status": 200, "message": "OK", "users": users}

    def post(self, userID=None):
        name = request.json['name']
        userID = len(users)
        users[userID] = {'name' : name}
        return {"status": 201, "message": "User successfully added", "user": users[userID]} 

    def delete(self, userID=None):
        global users
        if (userID or userID == 0):
            abort_if_user_not_exists(userID)
            user = users[userID]
            del users[userID]
            return {"status": 410, "message": "User successfully deleted", "user" : user}
        else: 
            users = {}
            return {"status": 410, "message": "All users successfully deleted"}


class Chat_room(Resource):
    def get(self, roomID=None):
        if (roomID or roomID == 0):
            abort_if_room_not_exists(roomID)
            return {'status': 200, 'message': "OK", 'room': rooms[roomID]}
        else:
            return {'status': 200, 'message': "OK", 'rooms': rooms}

    def post(self, roomID=None):
        name = request.json['name']
        roomID = len(rooms)
        users = []
        messages = []
        rooms[roomID] = {'name': name, 'users': users, 'messages': messages}
        return {'status': 201, 'message': "Room sucessfully created", 'room': roomID, 'name': name}


api.add_resource(User, "/api/users", "/api/users/<int:userID>")
api.add_resource(Chat_room, "/api/rooms", "/api/rooms/<int:roomID>")

if __name__ == "__main__":
    app.run(debug=True)
