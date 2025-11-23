from typing import List, Callable

import pytest

from model.item import Item
from model.api_client import HackerNewsAPIClient
from model.response import Response
from utils.factory import create_api_client


@pytest.fixture(scope='session', name='hacker_news_api_client')
def get_hacker_news_api_client() -> HackerNewsAPIClient:
    """
    Fixture to create and provide a singleton HackerNews API client instance for all tests in the session.
    """
    client = create_api_client('hackernews')
    return client

@pytest.fixture(scope='function')
def get_top_stories(hacker_news_api_client) -> List[int]:
    """
    Get story id for the top 500 stories from HackerNews API.
    :return: List of the ids for the top 500 stories returned from the HackerNewsAPI.
    """
    return hacker_news_api_client.get_top_stories().data

@pytest.fixture
def mock_empty_top_stories(monkeypatch):
    """
    Fixture to mock get_top_stories API to return an empty list of top stories.
    """
    def mock_send_request(api_request):
        return Response(200, {})

    def _apply_mock(api_client):
        monkeypatch.setattr(api_client, '_send_request', mock_send_request)

    return _apply_mock

# Does not work.
# @pytest.fixture(scope='function')
# def get_item(hacker_news_api_client, item_id: int) -> Item:
#     """
#     Get an item from the HackerNews API.
#     :param hacker_news_api_client: an object of the HackerNews API client.
#     :param item_id: id of the item to get.
#     :return: an object of the Item class.
#     """
#     return Item(**hacker_news_api_client.get_item(item_id=item_id).data)

@pytest.fixture
def get_item_factory(hacker_news_api_client) -> Callable[[int], Item]:
    def _get_item(item_id: int):
        return Item(**hacker_news_api_client.get_item(item_id).data)
    return _get_item

# Add more hooks, plugin etc. here as needed.
