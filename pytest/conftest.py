import allure
import pytest
from random import choice

PROFESSIONS: tuple = ('Architect', 'Biologist', 'Chemist', 'Dentist', 'Engineer', 'Space marine')
NAMES: tuple = ('Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Alex', 'Gabriel Angelos')


@allure.step('Generate user data')
@pytest.fixture()
def create_user_data():
    name = choice(NAMES)
    job = choice(PROFESSIONS)
    return {"name": name, "job": job}
