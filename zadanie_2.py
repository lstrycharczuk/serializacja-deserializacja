import json
from marshmallow import Schema, fields

class ProductSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.Str(required=True)
    price = fields.Number(required=True)
    producer_mail = fields.Email(required=True)

json = {
        "id": 2,
        "name": "Madra ksiazka 1",
        "price": 3.23,
        "producer_mail": "fds@fds.com"
}
    
result = ProductSchema().load(json)

print(result)