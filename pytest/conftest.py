import pytest
import requests
import time

BASE_URL = 'https://reqres.in'


@pytest.fixture(scope='session')
def get_api(request):
    start_tests = time.time()
    yield requests.get(BASE_URL + '/api/users/1')
    end_tests = time.time()
    final_time = end_tests - start_tests
    print("\n", final_time)