from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

employees = {}


def abort_if_not_exists(employee_id):
    if employee_id not in employees:
        abort(404, message="Could not find employee...")


def abort_if_exists(employee_id):
    if employee_id in employees:
        abort(404, message="Employee already exists...")


class Employee(Resource):

    def get(self, employee_id):
        return

    def post(self, employee_id):
        return

    def put(self, employee_id):
        return

    def delete(self, employee_id):
        return


api.add_resource(Employee, "/employee/<int:employee_id>")

if __name__ == "__main__":
    app.run(debug=True)