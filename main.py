from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
import json


app = Flask(__name__)
api = Api(app)
BASE = "/"

employees = {}


def abort_if_not_exists(employee_id):
    if employee_id not in employees:
        abort(404, message="Could not find employee...")


def abort_if_exists(employee_id):
    if employee_id in employees:
        abort(404, message="Employee already exists...")


class Employee(Resource):

    @app.route(BASE + "employee/<employee_id>")
    def get(self, employee_id):
        abort_if_not_exists(employee_id)
        return employees[employee_id]

    @app.route(BASE + "employee/<employee_id>", methods=['POST'])
    def post(self, employee_id):
        abort_if_exists(employee_id)
        name = request.json['name']
        age = request.json['age']
        pos = request.json['position']
        employees[employee_id] = {'name': name, 'age': age, 'position': pos}
        return jsonify("Post-result (200): " + str(employees[employee_id]))

    def put(self, employee_id):
        return

    def delete(self, employee_id):
        return


api.add_resource(Employee, "/employee/<int:employee_id>")

if __name__ == "__main__":
    app.run(debug=True)