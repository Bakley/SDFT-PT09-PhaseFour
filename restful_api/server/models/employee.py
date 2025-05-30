from sqlalchemy_serializer import SerializerMixin
from .db import db

class Employee(db.Model, SerializerMixin):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    department = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Employee {self.id} {self.name}>"
