from flask import Flask
from flask_restful import Api
from src.resources.auth_resources import AuthSignUp, AuthSignIn

app = Flask(__name__)
api = Api(app)
api.add_resource(AuthSignUp, "/auth/signup")
api.add_resource(AuthSignIn, "/auth/signin")

if __name__ == "__main__":
    app.run()
