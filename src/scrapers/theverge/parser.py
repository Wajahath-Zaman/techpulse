import json
import html

from bs4 import BeautifulSoup

from scrapers.common.article import Article
from scrapers.common.helpers import clean_text, parse_datetime


class TheVergeParser:
    """
    Parser responsible for extracting structured data from
    an individual The Verge article page.
    """

    SOURCE_NAME = "TheVerge"

    def parse(self, soup: BeautifulSoup, article_url: str) -> Article:

        data = self._extract_json_ld(soup)

        return Article(
            article_url=article_url,
            source_name=self.SOURCE_NAME,
            title=self._extract_title(data),
            summary=self._extract_summary(data),
            content=self._extract_content(data),
            authors=self._extract_authors(data),
            category=self._extract_category(data),
            tags=self._extract_tags(data),
            companies=[],
            technologies=[],
            published_at=self._extract_published_at(data),
        )

    ####################################################################
    # JSON-LD
    ####################################################################

    def _extract_json_ld(self, soup: BeautifulSoup) -> dict:
        """
        Extract the NewsArticle JSON-LD block.
        """

        scripts = soup.find_all(
            "script",
            attrs={"type": "application/ld+json"}
        )

        for script in scripts:

            try:
                data = json.loads(script.string)

                if data.get("@type") == "NewsArticle":
                    return data

            except Exception:
                continue

        return {}

    ####################################################################
    # Fields
    ####################################################################

    def _extract_title(self, data: dict) -> str:

        return clean_text(
            html.unescape(
                data.get("headline", "")
            )
        )

    def _extract_summary(self, data: dict) -> str:

        return clean_text(
            html.unescape(
                data.get("description", "")
            )
        )

    def _extract_content(self, data: dict) -> str:

        return clean_text(
            html.unescape(
                data.get("articleBody", "")
            )
        )

    def _extract_authors(self, data: dict) -> list[str]:

        authors = []

        for author in data.get("author", []):

            name = author.get("name")

            if name:
                authors.append(clean_text(name))

        return authors

    def _extract_tags(self, data: dict) -> list[str]:

        return [
            clean_text(tag)
            for tag in data.get("keywords", [])
        ]

    def _extract_category(self, data: dict) -> str:

        return clean_text(
            data.get("articleSection", "")
        )

    def _extract_published_at(self, data: dict):

        published = data.get("datePublished")

        if not published:
            return None

        return parse_datetime(published)