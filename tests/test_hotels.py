from main import app
from typing import List, Any

client = app.test_client()
headers = {"Authorization": ""}
wrong_headers = {"Authorization": "123"}


class TestHotels:

    def test_listing_hotels_correctly_and_authenticated_returns_200(self):
        response = client.get("/hotels", headers=headers)

        assert response.status_code == 200

    def test_listing_hotels_correctly_and_authenticated_returns_a_list(self):
        response = client.get("/hotels", headers=headers)

        assert response.json == {List[Any]}

    def test_listing_hotels_with_invalid_token_returns_401(self):
        response = client.get("/hotels", headers=wrong_headers)

        assert response.status_code == 401

    def test_listing_hotels_with_no_token_returns_401(self):
        response = client.get("/hotels")

        assert response.status_code == 401

    def test_searching_hotels_by_an_existing_name_correctly_and_authenticated_returns_200(self):
        response = client.get("/hotels?name=ibis%20hotel%20santos", headers=headers)

        assert response.status_code == 200

    def test_searching_hotels_by_an_unexisting_name_correctly_and_authenticated_returns_404(self):
        response = client.get("/hotels?name=ibis%20hotel%20guaianases", headers=headers)

        assert response.status_code == 404

    def test_searching_hotels_by_rating_correctly_and_authenticated_returns_200(self):
        response = client.get("/hotels?minRating=4%2E0", headers=headers)

        assert response.status_code == 200

    def test_searching_hotels_by_daily_rate_correctly_and_authenticated_returns_200(self):
        response = client.get("/hotels?minDailyRate=300", headers=headers)

        assert response.status_code == 200

    def test_searching_hotels_with_invalid_token_returns_401(self):
        response = client.get("/hotels?name=ibis%20hotel%20santos", headers=wrong_headers)

        assert response.status_code == 401

    def test_searching_hotels_with_no_token_returns_401(self):
        response = client.get("/hotels?name=ibis%20hotel%20santos")

        assert response.status_code == 401
