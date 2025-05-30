from flask_restful import Resource, reqparse
from server.controllers.employee_services import EmployeeController


class EmployeeResourceView(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name is required')
    parser.add_argument('email', type=str, required=True, help='Email is required')
    parser.add_argument('department', type=str, required=True, help='Department is required')
    parser.add_argument('salary', type=float, required=True, help='Salary is required')

    def get(self, employee_id=None):
        if employee_id:
            return EmployeeController.get_employee(employee_id)
        return EmployeeController.get_all_employees()

    def post(self):
        data = self.parser.parse_args()
        return EmployeeController.create_employee(data), 201

    def put(self, employee_id):
        data = self.parser.parse_args()
        return EmployeeController.update_employee(employee_id, data)

    def delete(self, employee_id):
        return EmployeeController.delete_employee(employee_id)
