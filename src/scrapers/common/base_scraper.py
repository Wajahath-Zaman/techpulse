from .logger import get_logger
import time 
from abc import ABC
from typing import Optional

import requests
from requests import Response

class BaseScraper(ABC):
    def __init__(self, timeout: int = 15, retries: int = 3, delay: int = 2):
        self.timeout = timeout
        self.retries = retries
        self.delay = delay

        self.headers = {
            'User-Agent': (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/138.0 Safari/537.36"
            )
        }
        
        self.session = requests.Session()
        self.session.headers.update(self.headers)

        

        self.logger = get_logger(self.__class__.__name__)

    def fetch(self, url: str) -> Optional[Response]:
        for attempt in range(1, self.retries + 1):

            try:

                response = self.session.get(url, timeout=self.timeout) # This will do everything in one session rather than making many requests for each url.
                response.raise_for_status()
                self.logger.info("Fetched article: %s", url)

                return response

            except requests.RequestException as e:

                self.logger.warning(
                    f"Attempt {attempt} failed: {e}"
                )

                if attempt < self.retries:
                    time.sleep(self.delay)

        
        self.logger.error(f"Failed to fetch {url}")

        return None
