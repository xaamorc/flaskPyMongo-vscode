from marshmallow import Schema, fields
from bson import ObjectId

class TaskSchema(Schema):
    _id = fields.String(dump_only=True)
    task = fields.Str()
    is_completed = fields.Boolean()
    due_date = fields.DateTime()

Schema.TYPE_MAPPING[ObjectId] = fields.String


