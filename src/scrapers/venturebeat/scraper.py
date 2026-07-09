"""
VentureBeat Scraper

Responsible for collecting VentureBeat articles from the RSS feed.

Responsibilities:
- Fetch article URLs from the RSS feed.
- Download article HTML.
- Parse articles into Article objects.
- Return a list of Article objects.
"""

from bs4 import BeautifulSoup

from scrapers.common.article import Article
from scrapers.common.article_enricher import ArticleEnricher
from scrapers.common.base_scraper import BaseScraper
from scrapers.common.rss import get_article_urls

from .parser import VentureBeatParser


class VentureBeatScraper(BaseScraper):
    """
    Scraper responsible for collecting and parsing VentureBeat articles.
    """

    SOURCE_METADATA = {
        "source_name": "VentureBeat",
        "website_url": "https://venturebeat.com",
        "rss_feed_url": "https://venturebeat.com/feed/",
        "country": None,
        "language": "en",
    }

    def __init__(self):
        super().__init__()

        self.parser = VentureBeatParser()
        self.enricher = ArticleEnricher()

    def scrape(self) -> list[Article]:
        """
        Scrape all articles from the VentureBeat RSS feed.

        Returns:
            list[Article]
        """

        self.logger.info("Starting VentureBeat scraper.")

        articles = []

        article_urls = get_article_urls(
            self.SOURCE_METADATA["rss_feed_url"]
        )

        self.logger.info(
            "Found %d article URLs.",
            len(article_urls)
        )

        for url in article_urls:

            response = self.fetch(url)

            if response is None:
                self.logger.warning(
                    "Failed to fetch article: %s",
                    url,
                )
                continue

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            try:

                article = self.parser.parse(
                    soup=soup,
                    article_url=url,
                )

                article = self.enricher.enrich(article)

                articles.append(article)

            except Exception:

                self.logger.exception(
                    "Failed to parse article: %s",
                    url,
                )

        self.logger.info(
            "Successfully scraped %d articles.",
            len(articles),
        )

        return articles