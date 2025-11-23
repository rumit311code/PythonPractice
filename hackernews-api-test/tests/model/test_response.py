from model.response import Response


def test_api_response_class():
    data = {'id': 100, 'title': 'Test'}
    resp = Response(200, data)
    assert resp.status_code == 200