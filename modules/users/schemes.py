from marshmallow import Schema,fields
from bson import ObjectId

class TaskSchema(Schema):
    id = fields.Str(dump_only=True)
    description = fields.Str()

class UsersSchema(Schema):
    _id = fields.Str(dump_only=True)
    name = fields.Str()
    email = fields.Str()
    password = fields.Str()
    tasks = fields.Nested(TaskSchema(many=True))

Schema.TYPE_MAPPING[ObjectId] = fields.String
