from marshmallow import Schema, fields
from datetime import datetime
from pprint import pprint
import json

class AddressSchema(Schema):
    kod_pocztowy = fields.Str(required=True)
    miasto = fields.Str(required=True)
    ulica = fields.Str(required=True)
    nr_domu = fields.Str(required=True)
    nr_mieszkania = fields.Str()

class UczenSchema(Schema):
    id = fields.UUID(required=True)
    imie = fields.Str(required=True)
    nazwisko = fields.Str(required=True)
    mail = fields.Email(required=True)
    data_urodzenia = fields.Date(required=True)
    adres = fields.Nested(AddressSchema, required=True)

student1 = dict(
    id=1,
    imie='Laura',
    nazwisko='Strycharczuk',
    mail='u21_laustr_lbn@technischools.com',
    data_urodzenia='2008-02-19',
    adres={
        'kod_pocztowy': '00-000',
        'miasto': 'Lublin',
        'ulica': 'Xyz',
        'nr_domu': '123',
        'nr_mieszkania': '45'
    }
)

student1['data_urodzenia'] = datetime.strptime(student1['data_urodzenia'], '%Y-%m-%d').date()

schema = UczenSchema(exclude=("id", "mail"))
result = schema.dump(student1)

pprint(result, indent=2)

with open(f'{student1["imie"]}_{student1["nazwisko"]}.json', 'w') as f:
    json.dump(result, f)
