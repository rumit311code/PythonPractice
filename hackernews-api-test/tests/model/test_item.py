import pytest
from model.item import Item


def test_item_creation_valid():
    item = Item(
        id=1,
        deleted=True,
        type='story',
        by='author',
        time=1234567890,
        text='Some text',
        dead=False,
        parent=10,
        poll=5,
        kids=[100, 101],
        url='http://example.com',
        score=10,
        title='Test title',
        parts='part1,part2',
        descendants=3
    )
    assert item.id == 1
    assert item.deleted is True
    assert item.type == 'story'
    assert item.by == 'author'
    assert item.time == 1234567890
    assert item.text == 'Some text'
    assert item.dead is False
    assert item.parent == 10
    assert item.poll == 5
    assert item.kids == [100, 101]
    assert item.url == 'http://example.com'
    assert item.score == 10
    assert item.title == 'Test title'
    assert item.parts == 'part1,part2'
    assert item.descendants == 3

def test_item_to_dict():
    item = Item(id=1, score=5)
    d = item.to_dict()
    # Check keys present
    assert 'id' in d
    assert 'score' in d
    assert d['id'] == 1
    # Values match
    assert d['score'] == 5

def test_item_invalid_id():
    with pytest.raises(ValueError, match="id must be positive."):
        Item(id=0)

def test_item_negative_score():
    with pytest.raises(ValueError, match="score cannot be negative."):
        Item(id=1, score=-1)
