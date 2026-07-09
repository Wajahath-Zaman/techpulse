from bs4 import BeautifulSoup

from scrapers.common.article import Article
from scrapers.common.helpers import (
    clean_text,
    parse_datetime
)


class ArsTechnicaParser:
    '''
    Parser responsible for extracting structured data from an Ars Technica Article page.
    '''

    SOURCE_NAME = "ArsTechnica"

    def parse(self, soup: BeautifulSoup, article_url: str) -> Article:
        """
        Parse an Ars Technica article page into an Article Object.
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
        Extract the complete article text.
        """

        article_sections = soup.find_all(
            "div",
            class_="post-content"
        )

        if not article_sections:
            return ""

        paragraphs = []

        for section in article_sections:

            for paragraph in section.find_all("p"):

                # Skip paragraphs inside non-article containers
                if paragraph.find_parent(
                    class_="ars-interlude-container"
                ):
                    continue

                text = clean_text(
                    paragraph.get_text(" ", strip=True)
                )

                if not text:
                    continue

                paragraphs.append(text)

        return "\n\n".join(paragraphs)

    def _extract_authors(self, soup: BeautifulSoup) -> list[str]:

        authors = []

        for author in soup.find_all("a", href=True):

            href = author.get("href")

            if "/author/" not in href:
                continue

            name = clean_text(author.get_text())

            if name and name not in authors:
                authors.append(name)

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