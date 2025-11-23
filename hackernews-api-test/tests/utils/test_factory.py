import pytest

from model.api_client import HackerNewsAPIClient
from utils.factory import create_api_client


def test_create_api_client_valid_type():
    client = create_api_client()
    assert isinstance(client, HackerNewsAPIClient)

def test_create_api_client_invalid_type():
    with pytest.raises(ValueError):
        create_api_client('invalid_client_type')