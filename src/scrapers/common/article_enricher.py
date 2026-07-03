from .article import Article
from .helpers import (
    clean_text,
    calculate_reading_time,
    calculate_word_count,
    generate_content_hash
)


class ArticleEnricher:
    '''
    Enriches an Article Object by calculating derived field.

    Responsibilities:
        - Clean Article text
        - Calculate word count
        - Estimate reading time
        - Generate content hash
    '''

    def enrich(self, article: Article) -> Article:
        '''
        Enriches an article with calculated metadata.

        Args:
            article: Parsed Article Object.

        Returns:
            Enriched Article Object.
        '''

        # Calculate derived fields
        article.word_count = calculate_word_count(article.content)

        article.reading_time = calculate_reading_time(
            article.word_count
        )

        article.content_hash = generate_content_hash(
            article.content
        )

        return article
    
    