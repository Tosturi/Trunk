import requests as r

BASE_URL = 'https://reqres.in/api/users'
DATA = {"name": 'me', "job": "chill"}

put_r = r.put(BASE_URL + '/2', json=DATA)

