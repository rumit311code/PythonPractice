"""
Module to define API clients.
"""
import logging
import requests

from model.exception import RequestError
from model.request import Request
from model.response import Response

logger = logging.getLogger(__name__)


class APIClient:
    """
    Base client for the API.
    """
    def __init__(self, base_url: str = ""):
        """
        Constructor.
        :param base_url: base url of the API client.
        """
        self.base_url = base_url

    # base method to call the API.
    def _send_request(self, api_request: Request) -> Response:
        """
        Send a request to the API.
        :param api_request: the request to send.
        :return: a response from the API.
        """
        url = f"{self.base_url}/{api_request.api_path}"
        try:
            logger.info(f"sending request to |{url}| with data: |{api_request.data}|.")
            res = requests.get(url=url, params=api_request.data)
            logger.info(f"received response |{res}|.")
            res.raise_for_status()
            return Response(status_code=res.status_code, data=res.json())
        except requests.RequestException as e:
            raise RequestError(f"Error during request to |{url}|.") from e


class HackerNewsAPIClient(APIClient):
    def __init__(self, api_version: str = "v0"):
        super().__init__(base_url='https://hacker-news.firebaseio.com/' + api_version)

    # API methods for HackerNewsAPIClient.
    def get_top_stories(self) -> Response:
        """
        Gets top stories from HackerNews API.
        :return: the top stories returned from the HackerNewsAPI.
        """
        return self._send_request(Request(api_path='topstories.json'))

    def get_item(self, item_id: int) -> Response:
        """
        Get an item from the HackerNews API.
        :param item_id: id of the item to get.
        :return: an item from the HackerNewsAPI.
        """
        return self._send_request(Request(api_path=f'item/{item_id}.json'))

    # add more APIs here for HackerNewsAPIClient.

# add more API client classes and their methods for other APIs.
