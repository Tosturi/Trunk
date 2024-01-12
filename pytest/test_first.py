

def test_status_code(get_api):
    assert get_api.status_code == 200


def test_json_data(get_api):
    assert "data" in get_api.json()
