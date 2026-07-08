from scrapers.common.database import Database
from scrapers.common.database_loader import DatabaseLoader
from scrapers.common.logger import get_logger
from scrapers.techcrunch.scraper import TechCrunchScraper

logger = get_logger("TechCrunch Integrator")


class TechCrunchIntegrator:
    """
    Orchestrates the complete TechCrunch ETL pipeline.

    Pipeline:
    1. Scrape articles from TechCrunch.
    2. Load the scraped articles into the database.
    """

    def run(self):

        logger.info("Starting TechCrunch integration pipeline.")

        scraper = TechCrunchScraper()

        logger.info("Scraping articles from TechCrunch.")
        articles = scraper.scrape()

        db = Database()
        db.connect()

        try:
            logger.info("Loading scraped articles into the database.")

            loader = DatabaseLoader(db)
            loader.load_articles(articles, scraper.SOURCE_METADATA)

            logger.info(
                "TechCrunch integration pipeline completed successfully."
            )

        except Exception:
            logger.exception("TechCrunch integration pipeline failed.")
            raise

        finally:
            logger.info("Closing database connection.")
            db.close()