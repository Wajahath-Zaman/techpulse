from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

@dataclass
class Article:
    article_url : str
    source_name : str
    title : str
    summary : Optional[str]
    content : str
    authors : List[str] = field(default_factory=list)
    category : Optional[str] = None
    tags : List[str] = field(default_factory=list)
    companies : List[str] = field(default_factory=list)
    technologies : List[str] = field(default_factory=list)
    published_at : Optional[datetime] = None
    word_count : Optional[int] = None
    reading_time : Optional[int] = None
    content_hash : Optional[str] = None
    scraped_at : datetime = field(default_factory=datetime.utcnow)


