import pytest
from req import ApiCommands


@pytest.fixture(scope="class")
def api_client(request):
    base_url = getattr(request.cls, "BASE_URL")
    return ApiCommands(base_url)
