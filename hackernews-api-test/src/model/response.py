"""
Base class for API Response.
"""
from typing import Any


# this can be converted to a @dataclass.
class Response:
    def __init__(self, status_code: int, data: Any):
        """
        :param status_code: HTTP response code returned by the API.
        :param data: json data returned by the API.
        """
        self.status_code = status_code
        self.data = data
