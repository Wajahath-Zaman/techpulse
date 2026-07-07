

from scrapers.techcrunch.scraper import TechCrunchScraper

def main():
    scraper = TechCrunchScraper()

    articles = scraper.scrape()

    if len(articles) <=0:
        print("No articles scraped.")

    print(f"Successfully scraped {len(articles)} articles. \n")

    if articles:
        article = articles[0]

        print("=" * 80)
        print(f"Title          : {article.title}")
        print(f"URL            : {article.article_url}")
        print(f"Author(s)      : {article.authors}")
        print(f"Category       : {article.category}")
        print(f"Published At   : {article.published_at}")
        print(f"Word Count     : {article.word_count}")
        print(f"Reading Time   : {article.reading_time} min")
        print(f"Tags           : {article.tags}")
        print(f"Content Hash   : {article.content_hash}")
        print("\nSummary:")
        print(article.summary)
        print("\nContent Preview:")
        print(article.content[:500])
        print("=" * 80)
    
    print(articles[0])


if __name__ == '__main__':
    main()
    
