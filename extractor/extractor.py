import time

import requests

from utils.helper import get_api_key
from utils.logger import logger
from utils.settings import settings


class Extractor:
    def __init__(self):
        self.url = settings.URL
        self.api_key = get_api_key()
        self.session = requests.Session()

    def fetch_data_for_date(self, date: str) -> dict:
        url = self.url.format(date, date, self.api_key)

        response = self.session.get(url, timeout=15)
        response.raise_for_status()

        logger.info(f"Successfully fetched data for {date}")

        return response.json()

    def extract_all(self, date_list: list) -> list:
        all_data = []
        for date in date_list:
            raw = self.fetch_data_for_date(date)
            all_data.append(raw)
            logger.info(f"Collected raw data for {date}")
        return all_data
