import time

import requests

from utils.helper import get_url, get_api_key
from utils.logger import logger

class Extractor:
    def __init__(self):
        self.url = get_url()
        self.api_key = get_api_key()
        # self.all_data = []
        self.session = requests.Session()

    def _fetch_single(self, date):
        url = self.url.format(date, date, self.api_key)
        for attempt in range(3):
            try:
                r = self.session.get(url, timeout=15)
                r.raise_for_status()
                return r.json()
            except requests.RequestException as e:
                if attempt == 2:
                    logger.error(f"Failed to fetch data for {date} after 3 attempts: {e}")
                    raise
                time.sleep(2 ** attempt)

    def _parse_response(self, data):
        records = []
        neos = data.get("near_earth_objects", {})
        for date_key, objects in neos.items():
            for neo in objects:
                record = {
                    "asteroid_id": neo['id'],
                    'neo_reference_id': neo['neo_reference_id'],
                    'name': neo['name'],
                    'absolute_magnitude_h': neo['absolute_magnitude_h'],
                    'is_potentially_hazardous_asteroid': neo['is_potentially_hazardous_asteroid'],
                    'is_sentry_object': neo['is_sentry_object'],
                    'export_date': date_key
                }
                records.append(record)
        return records

    def extracted_data(self, date):
        data = self._fetch_single(date)
        return self._parse_response(data)

    def extract_all(self, date_list):
        all_data = []
        for date in date_list:
            records = self.extracted_data(date)
            all_data.extend(records)
        return all_data
