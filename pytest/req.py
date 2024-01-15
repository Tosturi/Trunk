import requests
import allure
from pydantic import BaseModel


class ApiCommands:

    def __init__(self, base_url):
        self._base_url = base_url

    @allure.step("Get request from {path}")
    def get(self, path):
        url = self._base_url + path
        return requests.get(url)

    @allure.step("Validate result data")
    def validate_data(self, result: object, model: BaseModel):
        return model.model_validate(result)
