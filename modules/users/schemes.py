from marshmallow import Schema,fields
from bson import ObjectId

class UsersSchema(Schema):
    _id = fields.Str(dump_only=True)
    name = fields.Str()
    email = fields.Str()
    password = fields.Str()
    tasks = fields.Str()

Schema.TYPE_MAPPING[ObjectId] = fields.String
