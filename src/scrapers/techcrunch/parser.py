from bs4 import BeautifulSoup

from scrapers.common.article import Article
from scrapers.common.helpers import (clean_text, parse_datetime)


class TechCrunchParser:
    '''
    Parser responsible for extracting structured data from a TechCrunch Article page.
    '''

    SOURCE_NAME = 'TechCrunch'

    def parse(self, soup:BeautifulSoup, article_url:str) -> Article:
        """
        Parse A techcrunch article page into an Article Object
        """

        return Article(
            article_url=article_url,
            source_name=self.SOURCE_NAME,
            title=self._extract_title(soup),
            summary=self._extract_summary(soup),
            content=self._extract_content(soup),
            authors=self._extract_authors(soup),
            category=self._extract_category(soup),
            tags=self._extract_tags(soup),
            companies=[],
            technologies=[],
            published_at=self._extract_published_at(soup)
        )
    

    def _extract_title(self, soup=BeautifulSoup) -> str:
        title = soup.select_one("h1.article-hero__title")

        if title:
            return clean_text(title.get_text())
        
        return ""

    def _extract_summary(self, soup=BeautifulSoup) -> str | None:
        summary = soup.select_one("#speakable-summary")

        if summary:
            return clean_text(summary.get_text())
        
        return ""

    def _extract_content(self, soup=BeautifulSoup) -> str:
        """
        Extract the main article text content and return Clean Article text
        """

        content_div = soup.select_one(".entry-content")

        if not content_div:
            return ""

        paragraphs = []

        for paragraph in content_div.find_all("p"):

            classes = paragraph.get("class", [])

            if "affiliate-disclaimer-text" in classes:
                continue

            text = clean_text(paragraph.get_text(" ", strip=True))

            if not text:
                continue

            paragraphs.append(text)

        return "\n\n".join(paragraphs)
    

    def _extract_authors(self, soup=BeautifulSoup) -> list[str]:
        authors = []

        for author in soup.select(".wp-block-tc23-author-card-name a"):
            authors.append(
                clean_text(author.get_text())
            )

        return authors

    def _extract_category(self, soup:BeautifulSoup) -> str | None:
        category = soup.select_one(".article-hero__category a")

        if category:
            return clean_text(category.get_text())
        
        return ""

    def _extract_tags(self, soup:BeautifulSoup) -> list[str]:

        tags = []

        for tag in soup.select('.tc23-post-relevant-terms__terms a'):
            tags.append(
                clean_text(tag.get_text())
            )

        return tags
    
    def _extract_published_at(self, soup:BeautifulSoup): 

        published = soup.select_one(".article-hero__date time")

        if not published:
            return None

        return parse_datetime(
            published.get("datetime")
        )
