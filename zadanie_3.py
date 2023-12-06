from marshmallow import Schema, fields, validate, ValidationError
from pprint import pprint
import json

class ProductSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    producer_mail = fields.Email(required=True)
    type = fields.Str(required=True, validate=validate.OneOf(["nowy", "uzywany"]))

json = {
        "id":2,
        "name": "Madra ksiazka 1",
        "price": 3.23,
        "producer_mail": "fds@fds.com",
        "type": "nowy",
}
    
try:
    result  = ProductSchema().load(json)
    print(result)
except ValidationError as err:
    pprint(err.messages)
