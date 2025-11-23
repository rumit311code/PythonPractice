from model.request import Request


def test_api_request_class_initialization():
    req = Request('topstories.json', {'param': 'value'})
    assert req.api_path == 'topstories.json'
    assert req.data == {'param': 'value'}