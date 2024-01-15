import allure
from Users_Data.User import User


@allure.suite('Test API')
class TestApi:

    BASE_URL = "https://reqres.in"

    @allure.sub_suite('Check status code')
    def test_status_code(self, api_client):
        result = api_client.get("/api/users/2")
        assert result.status_code == 200

    @allure.sub_suite('Validate user data')
    def test_json_validate(self, api_client):
        result = api_client.get("/api/users/2")
        obj = result.json()
        assert api_client.validate_data(obj, User)
