"""
Factory to create API clients.
"""

from model.api_client import HackerNewsAPIClient


def create_api_client(client_type: str = 'hackernews') -> HackerNewsAPIClient:
    if client_type == 'hackernews':
        return HackerNewsAPIClient()
    raise ValueError(f"Unknown client type: {client_type}")