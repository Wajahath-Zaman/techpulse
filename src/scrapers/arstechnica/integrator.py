from scrapers.common.database import Database
from scrapers.common.database_loader import DatabaseLoader
from scrapers.common.logger import get_logger
from scrapers.arstechnica.scraper import ArsTechnicaScraper

logger = get_logger("ArsTechnica Integrator")


class ArsTechnicaIntegrator:
    """
    Orchestrates the complete Ars Technica ETL pipeline.

    Pipeline:
    1. Scrape articles from Ars Technica.
    2. Load the scraped articles into the database.
    """

    def run(self):

        logger.info("Starting Ars Technica integration pipeline.")

        scraper = ArsTechnicaScraper()

        logger.info("Scraping articles from Ars Technica.")
        articles = scraper.scrape()

        db = Database()
        db.connect()

        try:
            logger.info("Loading scraped articles into the database.")

            loader = DatabaseLoader(db)
            loader.load_articles(articles, scraper.SOURCE_METADATA)

            logger.info(
                "Ars Technica integration pipeline completed successfully."
            )

        except Exception:
            logger.exception("Ars Technica integration pipeline failed.")
            raise

        finally:
            logger.info("Closing database connection.")
            db.close()