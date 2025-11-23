"""
Test class to validate Items API.
"""
import logging
import pytest

from model.item import Item


logger = logging.getLogger(__name__)


@pytest.mark.items
class TestItems:
    @pytest.mark.regression
    ### option1: def test_retrieve_top_story_item(self, hacker_news_api_client, get_top_stories):
    ### option2: @pytest.mark.parametrize("get_item", get_top_stories[0], indirect = True) -> does NOT work.
    ### option3: use the factory fixture for the "get_items"
    def test_retrieve_top_story_item(self, get_top_stories, get_item_factory):
        #### code below is needed without using get_item and get_top_stories fixtures.
        # top_stories_res = hacker_news_api_client.get_top_stories()
        # top_stories = top_stories_res.json_data
        # if not top_stories:
        #     pytest.skip("Skip test: No top stories available")
        # top_story_id = top_stories[0]
        #
        # item_res = hacker_news_api_client.get_item(top_story_id)
        # item = item_res.json_data
        ## this can be a test for any story.
        # item = Item(**hacker_news_api_client.get_item(get_top_stories[0]).data)

        # this can be an assert on any other data of the item.
        item_id = get_top_stories[0]
        item = get_item_factory(item_id)
        assert item.id == get_top_stories[0]

    @pytest.mark.regression
    ### option1: def test_retrieve_first_comment_of_top_story(self, hacker_news_api_client):
    ### option2: @pytest.mark.parametrize("get_item", get_top_stories[0], indirect=True) -> does NOT work.
    ### option3: use the factory fixture for the "get_items"
    def test_retrieve_first_comment_of_top_story(self, get_top_stories, get_item_factory):
        #### code below is needed without using get_item and get_top_stories fixtures.
        # top_stories_res = hacker_news_api_client.get_top_stories()
        # top_stories = top_stories_res.json_data
        # if not top_stories:
        #     pytest.skip("Skip test: No top stories available")
        # top_story_id = top_stories[0]
        #
        # item_res = hacker_news_api_client.get_item(top_story_id)
        # item = item_res.json_data

        # replace 'get_item' with 'item' if not using conftest fixtures for get_item.

        item_id = get_top_stories[0] # current top story.
        item = get_item_factory(item_id)
        logging.info(f"item: |{item}|, get_top_stories[0]: |{get_top_stories[0]}|")
        if not item.kids:
            pytest.skip("Skip test: No comments for the top story.")

        # this can be a test for any kid.
        first_comment_id = item.kids[0] # first comment of the current top story.
        # comment = Item(**hacker_news_api_client.get_item(first_comment_id).data) -> if using option1 or 2.
        comment = get_item_factory(first_comment_id)
        logging.info(f"comment: |{comment}|.")

        # this can be an assert on any other data of the comment.
        assert comment.parent == get_top_stories[0]

    # The following method shows how to call the API in the test method instead of using a fixture from the conftest.
    @pytest.mark.negative_tests
    def test_invalid_item_id(self, hacker_news_api_client): # use client created in the conftest.
        invalid_id = -1
        res = hacker_news_api_client.get_item(invalid_id)
        # HackerNews API returns null for invalid items, JSON decoded as None
        assert res.status_code == 200
        assert res.data is None
