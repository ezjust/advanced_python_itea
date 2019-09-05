from marshmallow import Schema, fields
from


class EmployeeSchema(Schema):
    class Meta:
        model = Employee
        fields = ('name', 'surname')
