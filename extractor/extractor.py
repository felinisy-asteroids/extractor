import time

import requests

from utils.helper import get_url, get_api_key
from utils.logger import logger


class Extractor:
    def __init__(self):
        self.url = get_url()
        self.api_key = get_api_key()
        self.session = requests.Session()

    def _fetch_single(self, date):
        url = self.url.format(date, date, self.api_key)
        for attempt in range(3):
            try:
                r = self.session.get(url, timeout=15)
                r.raise_for_status()
                logger.info(f"Successfully fetched data for {date}")
                return r.json()
            except requests.RequestException as e:
                if attempt == 2:
                    logger.error(f"Failed to fetch data for {date} after 3 attempts: {e}")
                    raise
                logger.warning(f"Attempt {attempt + 1} failed for {date}, retrying...")
                time.sleep(2 ** attempt)
        return None

    def extract_all(self, date_list):
        all_data = []
        for date in date_list:
            raw = self._fetch_single(date)
            all_data.append(raw)
            logger.info(f"Collected raw data for {date}")
        return all_data