import requests


BASE_URL = 'https://reqres.in'


def get_api_status():
    response = requests.get(BASE_URL + '/api/users/1')
    get_json = response.json()


print(get_api_status())
