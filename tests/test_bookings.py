from main import app

client = app.test_client()
booking_schema = {}
booking_unexisting_hotel_schema = {}
headers = {"Authorization": ""}
headers_person_with_no_bookings = {"Authorization": ""}
wrong_headers = {"Authorization": "123"}


class TestBookings:

    def test_booking_existing_hotel_correctly_and_authenticated_returns_201(self):
        response = client.post("/bookings", json=booking_schema,
                               headers=headers)

        assert response.status_code == 201

    def test_booking_unexisting_hotel_correctly_and_authenticated_returns_400(self):
        response = client.post("/bookings", json=booking_unexisting_hotel_schema,
                               headers=headers)

        assert response.status_code == 400

    def test_booking_hotel_with_invalid_token_returns_401(self):
        response = client.post("/bookings", json=booking_schema,
                               headers=wrong_headers)

        assert response.status_code == 401

    def test_booking_hotel_with_no_token_returns_400(self):
        response = client.post("/bookings", json=booking_schema)

        assert response.status_code == 400

    def test_listing_bookings_correctly_and_authenticated_returns_200_when_the_current_user_has_at_least_one_booking(self):
        response = client.get("/bookings", headers=headers)

        assert response.status_code == 200

    def test_listing_bookings_correctly_and_authenticated_returns_204_when_the_current_user_has_no_bookings(self):
        response = client.get("/bookings", headers=headers_person_with_no_bookings)

        assert response.status_code == 204

    def test_listing_bookings_with_invalid_token_returns_401(self):
        response = client.get("/bookings", headers=wrong_headers)

        assert response.status_code == 401

    def test_listing_bookings_with_no_token_returns_400(self):
        response = client.get("/bookings")

        assert response.status_code == 400

    def test_updating_existing_bookings_correctly_and_authenticated_returns_200(self):
        response = client.post("/bookings/1", json=booking_schema,
                               headers=headers)

        assert response.status_code == 200

    def test_updating_unexisting_bookings_correctly_and_authenticated_returns_400(self):
        response = client.post("/bookings/1", json=booking_unexisting_hotel_schema,
                               headers=headers)

        assert response.status_code == 400

    def test_updating_bookings_with_invalid_token_returns_401(self):
        response = client.post("/bookings/1", json=booking_schema,
                               headers=wrong_headers)

        assert response.status_code == 401

    def test_updating_bookings_with_no_token_returns_400(self):
        response = client.post("/bookings/1", json=booking_schema)

        assert response.status_code == 400

    def test_canceling_existing_bookings_correctly_and_authenticated_returns_204(self):
        response = client.delete("/bookings/1", headers=headers)

        assert response.status_code == 204
    
    def test_canceling_unexisting_bookings_correctly_and_authenticated_returns_400(self):
        response = client.delete("/bookings/0", headers=headers)

        assert response.status_code == 400

    def test_canceling_bookings_with_invalid_token_returns_401(self):
        response = client.delete("/bookings/1", headers=wrong_headers)

        assert response.status_code == 401

    def test_canceling_bookings_with_no_token_returns_400(self):
        response = client.delete("/bookings/1")

        assert response.status_code == 400
