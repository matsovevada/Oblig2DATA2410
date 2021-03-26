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

rooms = {1: {'name': "testerinoroom"}}


def abort_if_not_exists(userID):
    if userID not in users:
        abort(404, message="Could not find User...")


def abort_if_exists(userID):
    if userID in users:
        abort(404, message="User already exists...")

class User(Resource):
    
    def get(self, userID=None):
        if (userID): 
            abort_if_not_exists(userID)
            return users[userID]
        else: return users

    def post(self, userID=None):
        name = request.json['name']
        userID = len(users)
        users[userID] = {'name' : name}
        return users[userID], 201 

    def delete(self, userID):
        pass


class Chat_room(Resource):
    def abort_if_not_exists(roomID):
        if roomID not in rooms:
            abort(404, message="Could not find room...")

    def abort_if_exists(roomID):
        if roomID in rooms:
            abort(404, message="Room already exists...")


api.add_resource(User, "/api/users", "/api/users/<int:userID>")
api.add_resource(Chat_room, "/api/room")

if __name__ == "__main__":
    app.run(debug=True)
