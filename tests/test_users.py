from src.main import app

client = app.test_client()


class TestUsers:

    def test_sign_up_user_correctly_returns_201(self):
        response = client.post("/users/signup", json={
            "name": "fernando",
            "email": "fernando@gmail.com",
            "password": "senha"
        })

        assert response.status_code == 201

    def test_sign_up_user_with_existing_email_returns_400(self):
        response = client.post("/users/signup", json={
            "name": "fernando",
            "email": "fernando@gmail.com",
            "password": "senha"
        })

        assert response.status_code == 400

    def test_sign_up_user_with_password_longer_than_14_returns_400(self):
        response = client.post("/users/signup", json={
            "name": "fernando",
            "email": "fernando1@gmail.com",
            "password": "senha1111111111"
        })

        assert response.status_code == 400

    def test_sign_in_correctly_returns_200(self):
        response = client.post("/users/signin", data={
            "email": "fernando@gmail.com",
            "password": "senha"
        })

        assert response.status_code == 200

    def test_sign_in_correctly_returns_a_token(self):
        response = client.post("/users/signin", data={
            "email": "fernando@gmail.com",
            "password": "senha"
        })

        assert "access_token" in response.json()

    def test_sign_in_with_wrong_email_returns_400(self):
        response = client.post("/users/signin", data={
            "email": "fernandooow@gmail.com",
            "password": "senha"
        })

        assert response.status_code == 400

    def test_sign_in_with_wrong_password_returns_400(self):
        response = client.post("/users/signin", data={
            "email": "fernando@gmail.com",
            "password": "senhaaaa"
        })

        assert response.status_code == 400

    def test_me_route_returns_200_when_a_valid_token_is_passed_in_headers(self):
        response = client.get("/users/me", headers={
            "Authorization": ""
        })

        assert response.status_code == 200

    def test_me_route_returns_401_when_a_invalid_token_is_passed_in_headers(self):
        response = client.get("/users/me", headers={
            "Authorization": "123"
        })

        assert response.status_code == 401

    def test_me_route_returns_401_when_no_token_is_passed_in_headers(self):
        response = client.get("/users/me")

        assert response.status_code == 401