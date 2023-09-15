from flask_restful import Resource
from flask import request
from src.repositories.user_repository import UserRepository
from src.schemas import user_schemas

repository = UserRepository()


class AuthSignUp(Resource):

    def post(self):
        payload = user_schemas.User().load(request.json)
        response_model = user_schemas.UserNoPassword()
        response = response_model.dump(repository.insert_user(payload))
        return response, 201
    

class AuthSignIn(Resource):

    def post(self):
        payload = user_schemas.SignIn().load(request.json)
        response_model = user_schemas.SucessfulSignIn()
        response = response_model.dump(repository.authenticate_user(payload))
        return response, 200
