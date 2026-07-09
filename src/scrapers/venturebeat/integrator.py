from scrapers.common.database import Database
from scrapers.common.database_loader import DatabaseLoader
from scrapers.common.logger import get_logger
from scrapers.venturebeat.scraper import VentureBeatScraper

logger = get_logger("VentureBeat Integrator")


class VentureBeatIntegrator:
    """
    Orchestrates the complete VentureBeat ETL pipeline.

    Pipeline:
    1. Scrape articles from VentureBeat.
    2. Load the scraped articles into the database.
    """

    def run(self):

        logger.info("Starting VentureBeat integration pipeline.")

        scraper = VentureBeatScraper()

        logger.info("Scraping articles from VentureBeat.")
        articles = scraper.scrape()

        db = Database()
        db.connect()

        try:
            logger.info("Loading scraped articles into the database.")

            loader = DatabaseLoader(db)
            loader.load_articles(articles, scraper.SOURCE_METADATA)

            logger.info(
                "VentureBeat integration pipeline completed successfully."
            )

        except Exception:
            logger.exception("VentureBeat integration pipeline failed.")
            raise

        finally:
            logger.info("Closing database connection.")
            db.close()