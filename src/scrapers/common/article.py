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
    authors : List[str] = field(default_factory=List)
    category : Optional[str] = None
    tags : List[str] = field(default_factory=List)
    companies : Optional[str] = None
    technologies : List[str] = field(default_factory=List)
    published_at : Optional[datetime] = None
    scraped_at : datetime = field(default_factory=datetime.utcnow)


