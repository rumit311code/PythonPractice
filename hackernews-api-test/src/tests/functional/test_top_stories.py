"""
Test class to validate Top Stories API.
"""
import logging
import pytest


@pytest.mark.top_stories
class TestTopStories:
    ### couple of options to write the tests.

    ##### Option1: don't use fixtures to call the apis
    #
    # def test_retrieve_top_stories(self, api_client):
    #     resp = api_client.get_top_stories()
    #     assert resp.status_code == 200
    #     stories = resp.json_data
    #     assert isinstance(stories, list)
    #     assert len(stories) > 0
    #
    # def test_edge_case_empty_response(self, monkeypatch, api_client):
    #     # Mock the send_request method to simulate empty list response
    #     def mock_send_request(api_request):
    #         return Response(200, {})
    #
    #     monkeypatch.setattr(api_client, 'send_request', mock_send_request)
    #     resp = api_client.get_top_stories()
    #     assert resp.status_code == 200
    #     assert resp.json_data == []


    #####  Option2: use pytest fixtures to call the apis.
    #
    # this is useful to abstract api calling code when test does more stuff with the returned data
    # than just doing basic checks. See TestItems class for example where the same code repeats in each test.
    @pytest.mark.regression
    def test_happy_path(self, get_top_stories):
        assert len(get_top_stories) > 0

    @pytest.mark.negative_tests
    def test_empty_response(self, hacker_news_api_client, mock_empty_top_stories):
        mock_empty_top_stories(hacker_news_api_client)  # apply monkeypatch mock
        logging.info(f"Mock Response |{hacker_news_api_client.get_top_stories().data}|")
        assert not hacker_news_api_client.get_top_stories().data
