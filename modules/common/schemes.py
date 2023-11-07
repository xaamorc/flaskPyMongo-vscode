from marshmallow import Schema, fields

class InsertedResponseSchema(Schema):
    object_id = fields.Str()
