from marshmallow import Schema, fields


class User(Schema):
    name = fields.Str()
    email = fields.Str()
    password = fields.Str()


class UserNoPassword(Schema):
    name = fields.Str()
    email = fields.Str()


class SignIn(Schema):
    email = fields.Str()
    password = fields.Str()


class SucessfulSignIn(Schema):
    message = fields.Str(default="Sucessfully logged in!")
    access_token = fields.Str(default="Bearer fake_token")
    email = fields.Str()
