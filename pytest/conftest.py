import allure
import pytest
from time import time
from random import choice

PROFESSIONS = ('Architect', 'Biologist', 'Chemist', 'Dentist', 'Engineer', 'Space marine')
NAMES = ('Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Alex', 'Gabriel Angelos')


@allure.step('Generate user data')
@pytest.fixture()
def create_user_data():
    name = choice(NAMES)
    job = choice(PROFESSIONS)
    return {"name": name, "job": job}