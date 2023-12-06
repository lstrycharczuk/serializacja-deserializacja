from marshmallow import Schema, fields, ValidationError
from datetime import datetime
from pprint import pprint
import json

class UczenSchema(Schema):
    id = fields.UUID(required=True)
    imie = fields.Str(required=True)
    nazwisko = fields.Str(required=True)
    mail = fields.Email(required=True)
    data_urodzenia = fields.Date(required=True)

student1 = dict(id=1, imie="Laura", nazwisko="Strycharczuk", mail="u21_laustr_lbn@technischools.com", data_urodzenia='2008-02-19')
student1['data_urodzenia'] = datetime.strptime(student1['data_urodzenia'], '%Y-%m-%d').date()

schema = UczenSchema(exclude=("id", "mail"))

try:
    result = schema.load(student1)
    pprint(result, indent=2)

    with open(f'{student1["imie"]}_{student1["nazwisko"]}.json', 'w') as f:
        json.dump(result, f)

except ValidationError as err:
    pprint(err.messages, indent=2)

    result = schema.load(student1)
    pprint(result, indent=2)

    with open(f'{student1["imie"]}_{student1["nazwisko"]}_poprawiony.json', 'w') as f:
        json.dump(result, f)
