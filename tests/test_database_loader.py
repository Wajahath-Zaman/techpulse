from src.scrapers.common.database_loader import DatabaseLoader
from src.scrapers.common.database import Database

from datetime import datetime, timezone, timedelta
from src.scrapers.common.article import Article   # assuming you saved your dataclass in article_model.py


def main():
    # Create Article dataclass object instead of dict
    article = Article(
        article_url="https://techcrunch.com/2026/07/07/savis-app-aims-to-protect-consumers-from-realistic-ai-scams-like-kidnappers-demanding-ransom/",
        source_name="TechCrunch",
        title="Savi’s app aims to protect consumers from realistic AI scams like kidnappers demanding ransom",
        summary="Brothers Patrick and Ryan Coughlin, each with impressive careers in the tech industry...",
        content="Full article content here...",
        authors=["Julie Bort"],
        category="AI",
        tags=["AI", "AI scams", "fraud detection", "Savi", "Security", "Startups"],
        companies=[],
        technologies=[],
        published_at=datetime(2026, 7, 7, 5, 0, tzinfo=timezone(timedelta(days=-1, seconds=61200))),
        word_count=937,
        reading_time=5,
        content_hash="632a3f3d2f2c423ea3f0e3f6c1d2dd0b2f8b8af76af8068165f62e395d8639ef",
        scraped_at=datetime(2026, 7, 7, 12, 21, 15, 99423)
    )

    SOURCE_METADETA = {
        "source_name": "TechCrunch",
        "website_url": "https://techcrunch.com",
        "rss_feed_url": "https://techcrunch.com/feed/",
        "country": None,
        "language": "en"
    }

    db = Database()
    db.connect()
    loader = DatabaseLoader(db)

    try:
        hey = loader.load_articles([article], SOURCE_METADETA)
        print(hey)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
