"""
Model class to store HackerNews API's Item object.
"""
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, field, asdict


@dataclass()
class Item:
    id: int = field(default=False, metadata={"description": "The item's unique id."})
    deleted: Optional[bool] = field(default=False, metadata={"description": "true if the item is deleted."})
    type: Optional[str] = field(default=None, metadata={"description": "The type of item. One of 'job', 'story', 'comment', 'poll', or 'pollopt'."})
    by: Optional[str] = field(default=None, metadata={"description": "The username of the item's author."})
    time: Optional[int] = field(default=None, metadata={"description": "Creation date of the item, in Unix Time."})
    text: Optional[str] = field(default=None, metadata={"description": "The comment, story or poll text. HTML."})
    dead: Optional[bool] = field(default=False, metadata={"description": "true if the item is dead."})
    parent: Optional[int] = field(default=None, metadata={"description": "The comment's parent: either another comment or the relevant story."})
    poll: Optional[int] = field(default=None, metadata={"description": "The pollopt's associated poll."})
    kids: Optional[List[int]] = field(default=None, metadata={"description": "The ids of the item's comments, in ranked display order."})
    url: Optional[str] = field(default=None, metadata={"description": "The URL of the story."})
    score: Optional[int] = field(default=None, metadata={"description": "The story's score, or the votes for a pollopt."})
    title: Optional[str] = field(default=None, metadata={"description": "The title of the story, poll or job. HTML."})
    parts: Optional[str] = field(default=None, metadata={"description": "A list of related pollopts, in display order."})
    descendants: Optional[int] = field(default=None, metadata={"description": "In the case of stories or polls, the total comment count."})

    def __post_init__(self):
        if self.id <= 0:
            raise ValueError("id must be positive.")
        # Add validation for other fields here as needed.

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
