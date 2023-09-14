from marshmallow import Schema, fields


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Str()
    password = fields.Str()


class UserDisplaySchema(Schema):
    name = fields.Str()
    email = fields.Str()
