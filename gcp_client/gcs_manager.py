import json
from datetime import datetime

from google.cloud import storage

from utils.settings import settings
from utils.logger import logger



class GCSManager:
    def __init__(self):
        self.client = storage.Client()
        self.bucket = self.client.bucket(settings.BUCKET_NAME)

    def get_filename(self):
        return f"raw_data/{datetime.now().date()}.json"

    def upload_data(self, all_data):
        filename = self.get_filename()
        try:
            blob = self.bucket.blob(filename)
            blob.upload_from_string(
                data=json.dumps(all_data, indent=2),
                content_type='application/json'
            )
            logger.info(f"Uploaded {len(all_data)} records to gs://{self.bucket.name}/{filename}")
            return filename
        except Exception as e:
            logger.error(f"Failed to upload to GCS: {e}")
            raise


