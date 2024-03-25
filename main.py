from flask import Flask
from flask_restful import Api
from src.resources.auth_resources import AuthSignUp, AuthSignIn, AuthMe
import src.utils.pycharm_flask_debug_patch

app = Flask(__name__)
api = Api(app)
api.add_resource(AuthSignUp, "/auth/signup")
api.add_resource(AuthSignIn, "/auth/signin")
api.add_resource(AuthMe, "/auth/me")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
