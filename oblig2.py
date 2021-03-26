from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
import json
import requests


app = Flask(__name__)
api = Api(app)



class User(Resource):
    BASE = "/api/users/"

    @app.route(BASE)
    def get(self):
        pass

    @app.route(BASE + "<userID>")
    def get(self, userID):
        pass

    def post(self):
        pass

    def delete(self, userID):
        pass


class Chat_room(Resource):
    pass


api.add_resource(User, "/api/users")
api.add_resource(Chat_room, "/api/room")
