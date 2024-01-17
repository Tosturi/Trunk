import json
import requests
import allure
from random import choice
from pydantic import BaseModel


class ApiCommands:

    def __init__(self, base_url):
        self._base_url = base_url
        self._user_name = (
    "Alexander", "Ekaterina", "Mikhail", "Anna", "Dmitry",
    "Olga", "Artem", "Natalia", "Ivan", "Elena",
    "Sergei", "Maria", "Andrei", "Yulia", "Pavel",
    "Tatiana", "Alexey", "Victoria", "Vladimir", "Ksenia",
    "Nikolai", "Irina", "Konstantin", "Anastasia", "Gleb",
    "Oksana", "Denis", "Evgenia", "Stanislav", "Svetlana",
    "Grigory", "Yuliana", "Igor", "Eva", "Valentin",
    "Lyudmila", "Roman", "Nina", "Vasiliy", "Alina",
    "Valery", "Larisa", "Arthur", "Sophia", "Valeria",
    "Vladislav", "Margaret", "Peter", "Vera", "Alena"
        )
        self._user_job = (
    'Architect', 'Biologist', 'Chemist', 'Dentist', 'Engineer',
    'Farmer', 'Geologist', 'Horticulturist', 'Interpreter', 'Journalist',
    'Kinesiologist', 'Linguist', 'Mathematician', 'Nutritionist', 'Optometrist',
    'Pharmacist', 'Quantum physicist', 'Radiologist', 'Statistician', 'Technician',
    'Urban planner', 'Veterinarian', 'Web developer', 'Xenobiologist', 'Yoga instructor',
    'Zoologist', 'Animator', 'Botanist', 'Counselor', 'Dermatologist', 'Epidemiologist',
    'Forensic scientist', 'Geneticist', 'Hematologist', 'Immunologist', 'Jeweler',
    'Kinesiotherapist', 'Landscape architect', 'Meteorologist', 'Neurologist', 'Obstetrician',
    'Paleontologist', 'Quantum engineer', 'Robotics engineer', 'Social worker', 'Translator',
    'Urologist', 'Virologist', 'Welder',
        )


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

    @allure.step("Generate user data")
    def create_data(self):
        name = choice(self._user_name)
        job = choice(self._user_job)
        return {"name": name, "job": job}

    @allure.step("Validate result data")
    def validate_data(self, result: object, model: BaseModel):
        return model.model_validate(result)
