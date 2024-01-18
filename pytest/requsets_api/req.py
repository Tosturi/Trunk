import requests
import allure


@allure.step("Get request from {path}")
def get(base_url, path, params=None) -> requests.Response:
    if params is None:
        params = []
    url = base_url + path
    return requests.get(url, params)


@allure.step("Post request to {path}")
def post(base_url, path, data=None) -> requests.Response:
    if data is None:
        data = {}
    url = base_url + path
    return requests.post(url, json=data)


@allure.step("Put request to {path}")
def put(base_url, path, data=None) -> requests.Response:
    if data is None:
        data = {}
    url = base_url + path
    return requests.put(url, json=data)


@allure.step("Patch request to {path}")
def patch(base_url, path, data=None) -> requests.Response:
    if data is None:
        data = {}
    url = base_url + path
    return requests.patch(url, json=data)


@allure.step("Delete data from {path}")
def delete(base_url, path) -> requests.Response:
    url = base_url + path
    return requests.delete(url)


@allure.step("Validate result data")
def validate_data(result: object, model):
    return model.model_validate(result)
