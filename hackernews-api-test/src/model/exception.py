"""
Error and Exception Classes.
"""

class ClientError(Exception):
    """Base exception class for API Client errors."""
    pass

class RequestError(ClientError):
    """Exception raised for errors in the request execution."""
    pass

class ResponseError(ClientError):
    """Exception raised for errors in the response execution."""
    pass
