from main import app

client = app.test_client()


class TestUsers:

    def test_sign_up_user_correctly_returns_201(self):
        response = client.post("/auth/signup", json={
            "name": "fernando",
            "email": "fernando@gmail.com",
            "password": "senha"
        })

        assert response.status_code == 201

    def test_sign_up_user_with_existing_email_returns_400(self):
        response = client.post("/auth/signup", json={
            "name": "fernando",
            "email": "fernando@gmail.com",
            "password": "senha"
        })

        assert response.status_code == 400

    def test_sign_up_user_with_password_longer_than_14_returns_400(self):
        response = client.post("/auth/signup", json={
            "name": "fernando",
            "email": "fernando1@gmail.com",
            "password": "senha1111111111"
        })

        assert response.status_code == 400

    def test_sign_in_correctly_returns_200(self):
        response = client.post("/auth/signin", json={
            "email": "fernando@gmail.com",
            "password": "senha"
        })

        assert response.status_code == 200

    def test_sign_in_correctly_returns_a_token(self):
        response = client.post("/auth/signin", json={
            "email": "fernando@gmail.com",
            "password": "senha"
        })

        assert response.json["access_token"] is not None

    def test_sign_in_with_wrong_credentials_returns_400(self):
        response = client.post("/auth/signin", json={
            "email": "wrong_email",
            "password": "wrong_password"
        })

        assert response.status_code == 400

    def test_me_route_returns_200_when_a_valid_token_is_passed_in_headers(self):
        response = client.get("/auth/me", headers={
            "Authorization": ""
        })

        assert response.status_code == 200

    def test_me_route_returns_401_when_a_invalid_token_is_passed_in_headers(self):
        response = client.get("/auth/me", headers={
            "Authorization": "123"
        })

        assert response.status_code == 401

    def test_me_route_returns_401_when_no_token_is_passed_in_headers(self):
        response = client.get("/auth/me")

        assert response.status_code == 401
