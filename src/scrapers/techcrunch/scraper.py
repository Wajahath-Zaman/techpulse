from bs4 import BeautifulSoup

from scrapers.common.article import Article
from scrapers.common.article_enricher import ArticleEnricher
from scrapers.common.base_scraper import BaseScraper
from scrapers.common.rss import get_article_urls

from .parser import TechCrunchParser
from scrapers.common.logger import get_logger

logger = get_logger("TechCrunch Scraper")


class TechCrunchScraper(BaseScraper):
    '''
    Scraper responsible for collecting and parsing techcrunch articles.
    '''

    SOURCE_METADATA = {
        "source_name": "TechCrunch",
        "website_url": "https://techcrunch.com",
        "rss_feed_url": "https://techcrunch.com/feed/",
        "country": None,
        "language": "en" 
    }


    def __init__(self):
        super().__init__()

        self.parser = TechCrunchParser()
        self.enricher = ArticleEnricher()

    def scrape(self) -> list[Article]:
        """
        Scrape all articles from the TechCrunch RSS feed
        Returns: A list of Article Objects.
        """
        logger.info("Starting TechCrunch scraping Pipeline.")

        articles = []

        logger.info("Discovering article URLS from TechCrunch RSS feed.")

        article_urls = get_article_urls(self.SOURCE_METADATA["rss_feed_url"])

        logger.info("Found %d article urls", len(article_urls))

        for url in article_urls:

            response = self.fetch(url)

            if response is None:
                logger.warning("Failed to fetch article: %s", url)
                continue

            soup = BeautifulSoup(response.text, "html.parser")

            try:
                article = self.parser.parse(
                    soup = soup,
                    article_url = url
                )

                article = self.enricher.enrich(article)

                articles.append(article)
            
            except Exception as e:

                logger.exception(
                    'Failed to parse acticle %s : %s', url, e)
            
        logger.info("Successfully scraped %d articles.", len(articles))

        return articles