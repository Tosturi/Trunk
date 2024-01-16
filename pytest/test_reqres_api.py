import allure
from Users_Data.User import SingleUser, UserList, UserData, Support


@allure.suite('Test API')
class TestApi:

    BASE_URL = "https://reqres.in"

    @allure.sub_suite('Check status code')
    def test_status_code(self, api_client):
        result = api_client.get("/")
        assert result.status_code == 200

    @allure.sub_suite('Validate single user data')
    def test_single_user_validate(self, api_client):
        result = api_client.get("/api/users/2", "")
        obj = result.json()
        assert api_client.validate_data(obj, SingleUser)
        assert api_client.validate_data(obj["data"], UserData)
        assert api_client.validate_data(obj["support"], Support)

    @allure.sub_suite('Validate user list')
    def test_user_list_validate(self, api_client):
        result = api_client.get("/api/users", {"page": 1})
        obj = result.json()
        assert api_client.validate_data(obj, UserList)
