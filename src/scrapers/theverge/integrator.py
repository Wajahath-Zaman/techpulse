from scrapers.common.database import Database
from scrapers.common.database_loader import DatabaseLoader
from scrapers.common.logger import get_logger
from scrapers.theverge.scraper import TheVergeScraper

logger = get_logger("TheVerge Integrator")


class TheVergeIntegrator:
    """
    Orchestrates the complete The Verge ETL pipeline.

    Pipeline:
    1. Scrape articles from The Verge.
    2. Load the scraped articles into the database.
    """

    def run(self):

        logger.info("Starting The Verge integration pipeline.")

        scraper = TheVergeScraper()

        logger.info("Scraping articles from The Verge.")
        articles = scraper.scrape()

        db = Database()
        db.connect()

        try:
            logger.info("Loading scraped articles into the database.")

            loader = DatabaseLoader(db)
            loader.load_articles(articles, scraper.SOURCE_METADATA)

            logger.info(
                "The Verge integration pipeline completed successfully."
            )

        except Exception:
            logger.exception("The Verge integration pipeline failed.")
            raise

        finally:
            logger.info("Closing database connection.")
            db.close()