"""
Example of a test setup where fixtures and tests are written in the same module. Non-modular approach.
"""
import pytest
import requests

BASE_URL = 'https://hacker-news.firebaseio.com/v0'

@pytest.fixture
def get_top_stories():
    resp = requests.get(f'{BASE_URL}/topstories.json')
    assert resp.status_code == 200
    return resp.json()

@pytest.fixture
def get_item():
    def _get_item(item_id):
        resp = requests.get(f'{BASE_URL}/item/{item_id}.json')
        assert resp.status_code == 200
        return resp.json()
    return _get_item

def test_top_stories(get_top_stories):
    assert isinstance(get_top_stories, list)
    assert len(get_top_stories) > 0

def test_first_top_story(get_top_stories, get_item):
    item = get_item(get_top_stories[0])
    assert item['id'] == get_top_stories[0]

def test_top_story_first_comment(get_top_stories, get_item):
    item = get_item(get_top_stories[0])
    if 'kids' in item and item['kids']:
        comment = get_item(item['kids'][0])
        assert comment['parent'] == item['id']
    else:
        pytest.skip("No comments for this story")

@pytest.mark.parametrize('invalid_item_id', [-1, 0, 999999999])
def test_invalid_item(get_item, invalid_item_id):
    resp = requests.get(f'{BASE_URL}/item/{invalid_item_id}.json')
    assert resp.status_code == 200
    assert resp.json() is None
