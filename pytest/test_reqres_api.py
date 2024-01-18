import allure
import requsets_api.req as r
from Users_Data.User import UserData, SingleUser, Support, UserList, CreateData, UpdateData

BASE_URL: str = "https://reqres.in"


@allure.title('Check GET request (Single user)')
@allure.tag('GET')
@allure.severity(allure.severity_level.CRITICAL)
def test_get_single_user():
    result_user = r.get(BASE_URL, "/api/users/2", "")
    obj = result_user.json()
    with allure.step('Checking status code'):
        assert result_user.status_code == 200
    with allure.step('Checking single user data'):
        assert r.validate_data(obj, SingleUser)
        assert r.validate_data(obj["data"], UserData)
        assert r.validate_data(obj["support"], Support)


@allure.title('Check GET request (List users)')
@allure.tag('GET')
@allure.severity(allure.severity_level.NORMAL)
def test_get_user_list():
    result_list = r.get(BASE_URL,"/api/users", {"page": 1})
    obj = result_list.json()
    with allure.step('Checking status code'):
        assert result_list.status_code == 200
    with allure.step('Checking user list data'):
        assert r.validate_data(obj, UserList)


@allure.title('Check POST request')
@allure.tag('POST')
@allure.severity(allure.severity_level.CRITICAL)
def test_post(create_user_data):
    user_data = create_user_data
    result_create = r.post(BASE_URL, '/api/users', user_data)
    obj = result_create.json()
    with allure.step('Checking status code'):
        assert result_create.status_code == 201
    with allure.step('Checking created data'):
        assert r.validate_data(obj, CreateData)
        if len(user_data) > 0:
            assert obj['name'] == user_data['name']
            assert obj['job'] == user_data['job']


@allure.title('Check PUT request')
@allure.tag('PUT')
@allure.severity(allure.severity_level.CRITICAL)
def test_put(create_user_data):
    user_data = create_user_data
    result_put = r.put(BASE_URL, '/api/users/2', user_data)
    obj = result_put.json()
    with allure.step('Checking status code'):
        assert result_put.status_code == 200
    with allure.step('Checking updated data'):
        assert r.validate_data(obj, UpdateData)
        if len(user_data) > 0:
            assert obj['name'] == user_data['name']
            assert obj['job'] == user_data['job']


@allure.title('Check PATCH request')
@allure.tag('PATCH')
@allure.severity(allure.severity_level.NORMAL)
def test_patch(create_user_data):
    user_data = create_user_data
    result_patch = r.patch(BASE_URL, '/api/users/2', user_data)
    obj = result_patch.json()
    with allure.step('Checking status code'):
        assert result_patch.status_code == 200
    with allure.step('Checking updated data'):
        assert r.validate_data(obj, UpdateData)
        if len(user_data) > 0:
            assert obj['name'] == user_data['name']
            assert obj['job'] == user_data['job']


@allure.title('Check DELETE request')
@allure.tag('DELETE')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete():
    result_delete = r.delete(BASE_URL, '/api/users/2')
    obj = result_delete.text
    with allure.step('Checking status code'):
        assert result_delete.status_code == 204
    with allure.step('Checking that there is no data'):
        assert len(obj) == 0
