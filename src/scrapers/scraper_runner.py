""""
Scraper Runner

Application entry point for the Ingestion Pipelines

Responsibilities:
- Execute all configured source integrators.
- Continue executing remaining integrators even if one fails.
- Log the overall execution progress.

This module contains no scraping or database logic.
"""

from scrapers.common.logger import get_logger
from scrapers.techcrunch.integrator import TechCrunchIntegrator
from scrapers.theverge.integrator import TheVergeIntegrator
from scrapers.venturebeat.integrator import VentureBeatIntegrator
from scrapers.arstechnica.integrator import ArsTechnicaIntegrator

logger = get_logger("Scraper Runner")

class ScraperRunner():
    """
    Runs all available source integration pipelines.
    """

    def __init__(self):

        self.integrators = [
            TechCrunchIntegrator(),
            TheVergeIntegrator(),
            VentureBeatIntegrator(),
            ArsTechnicaIntegrator()
        ]

    def run(self):

        logger.info("=" * 60)
        logger.info("TechPulse Scraper Runner Started")
        logger.info("=" * 60)

        self.successful = 0
        self.failed = 0

        for integrator in self.integrators:

            logger.info("Running %s ...", (integrator.__class__.__name__))

            try:
                integrator.run()
                self.successful = +1

                logger.info("%s completed successfully.", integrator.__class__.__name__)

            except Exception:
                
                self.failed = +1

                logger.exception(
                    "$s failed."
                    , integrator.__class__.__name__
                )

        logger.info("=" * 60)
        logger.info("Scraper Runner Summary")
        logger.info("Total Integrators : %d", len(self.integrators))
        logger.info("Successful        : %d", self.successful)
        logger.info("Failed            : %d", self.failed)
        logger.info("=" * 60)

        logger.info("TechPulse Scraper Runnner Finished.")


def main():

    runner = ScraperRunner()
    runner.run()


if __name__ == '__main__':
    main()