from bs4 import BeautifulSoup

from scrapers.common.article import Article
from scrapers.common.helpers import (
    clean_text,
    parse_datetime
)


class VentureBeatParser:
    '''
    Parser responsible for extracting structured data from a VentureBeat Article page.
    '''

    SOURCE_NAME = "VentureBeat"

    def parse(self, soup: BeautifulSoup, article_url: str) -> Article:
        """
        Parse a VentureBeat article page into an Article Object.
        """

        return Article(
            article_url=article_url,
            source_name=self.SOURCE_NAME,
            title=self._extract_title(soup),
            summary=self._extract_summary(soup),
            content=self._extract_content(soup),
            authors=self._extract_authors(soup),
            category=self._extract_category(article_url),
            tags=[],
            companies=[],
            technologies=[],
            published_at=self._extract_published_at(soup)
        )

    def _extract_title(self, soup: BeautifulSoup) -> str:

        title = soup.find("h1")

        if title:
            return clean_text(title.get_text())

        return ""

    def _extract_summary(self, soup: BeautifulSoup) -> str:

        summary = soup.find(
            "meta",
            attrs={"name": "description"}
        )

        if summary:
            return clean_text(
                summary.get("content", "")
            )

        return ""

    def _extract_content(self, soup: BeautifulSoup) -> str:
        """
        Extract the main article text content and return clean article text.
        """

        article_body = soup.find(
            "div",
            class_="article-body"
        )

        if not article_body:
            return ""

        paragraphs = []

        for paragraph in article_body.find_all("p"):

            text = clean_text(
                paragraph.get_text(" ", strip=True)
            )

            if not text:
                continue

            paragraphs.append(text)

        return "\n\n".join(paragraphs)

    def _extract_authors(self, soup: BeautifulSoup) -> list[str]:

        authors = []

        for author in soup.find_all(
            "a",
            rel="author"
        ):

            authors.append(
                clean_text(author.get_text())
            )

        return authors

    def _extract_category(self, article_url: str) -> str:

        try:

            category = article_url.rstrip("/").split("/")[3]

            return category.replace("-", " ").title()

        except IndexError:

            return ""

    def _extract_published_at(self, soup: BeautifulSoup):

        published = soup.find("time")

        if not published:
            return None

        datetime_value = published.get("datetime")

        if not datetime_value:
            return None

        return parse_datetime(datetime_value)