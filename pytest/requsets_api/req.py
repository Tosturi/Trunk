import json
import requests
import allure
from pydantic import BaseModel


class ApiCommands:

    def __init__(self, base_url):
        self._base_url = base_url

    @allure.step("Get request from {path}")
    def get(self, path, params=None) -> requests.Response:
        if params is None:
            params = []
        url = self._base_url + path
        return requests.get(url, params)

    @allure.step("Post request to {path}")
    def post(self, path, data=None):
        if data is None:
            data = {}
        url = self._base_url + path
        return requests.post(url, json=json.dumps(data))

    @allure.step("Validate result data")
    def validate_data(self, result: object, model: BaseModel):
        return model.model_validate(result)
