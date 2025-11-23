"""
Base class for API Request.
"""

# this can be converted to a @dataclass.
class Request:
    def __init__(self, api_path: str, data: dict = None):
        """
        :param api_path: API endpoint path relative to base URL.
        :param data: Dictionary of payload data or query parameters to send to API.
        """
        self.api_path = api_path
        self.data = data

    # can use subclasses that derive from this class to create API specific requests if needed.
