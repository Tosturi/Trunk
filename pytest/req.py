import requests


BASE_URL = 'https://reqres.in'


def get_api():
    response = requests.get(BASE_URL + '/api/users/1')
    return response
