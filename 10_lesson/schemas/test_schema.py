from marshmallow import Schema, fields


class Category(Schema):
    name = fields.String(required=True)


class Item(Schema):
    name = fields.String(required=True)
    description = fields.String()
    category = fields.Nested(Category)

