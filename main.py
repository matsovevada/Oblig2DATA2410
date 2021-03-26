from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
import json
import requests


app = Flask(__name__)
api = Api(app)

users = {1: {'name': "Testerino"}}

rooms = {1: {'name': "testerinoroom"}}


def abort_if_not_exists(userID):
    if userID not in users:
        abort(404, message="Could not find User...")


def abort_if_exists(userID):
    if userID in users:
        abort(404, message="User already exists...")

class User(Resource):
    BASE = "/api/users"

    @app.route(BASE + "/<userID>")
    def get(self, userID):
        abort_if_not_exists(userID)
        return users[userID]

    def post(self):
        pass

    def delete(self, userID):
        pass


class Chat_room(Resource):
    def abort_if_not_exists(roomID):
        if roomID not in rooms:
            abort(404, message="Could not find room...")

    def abort_if_exists(roomID):
        if roomID in rooms:
            abort(404, message="Room already exists...")


api.add_resource(User, "/api/users")
api.add_resource(Chat_room, "/api/room")

if __name__ == "__main__":
    app.run(debug=True)
