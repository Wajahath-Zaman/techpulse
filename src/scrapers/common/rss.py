import logging
from typing import List, Dict

import feedparser

logger = logging.getLogger(__name__)

def get_article_urls(rss_url: str) -> List[str]:
    
    feed = feedparser.parse(rss_url)

    if feed.bozo:
        logger.warning(
            "RSS feed contains parsing errors: %s",
            getattr(feed, "bozo_exception", "Unknown error")
        )

    article_urls = []
    seen_urls = []

    for entry in feed.entries:
        url = entry.get("link")

        if not url:
            continue

        if url in seen_urls:
            continue

        seen_urls.append(url)
        article_urls.append(url)

    logger.info(
        "Discovered %d articles URLs from RSS feed.", 
        len(article_urls)
    )

    return article_urls
