import logging

from extractor.extractor import Extractor
from gcp_client.gcs_manager import GCSManager


def main(request):
    raw_body = request.get_json()
    date_list = raw_body.get("dates", [])
    logging.info(f"Dates: {date_list}")

    if not date_list:
        logging.error("No dates")
        return {"message": "No dates"}, 400

    extractor = Extractor()

    all_data = extractor.extract_all(date_list)
    gcs = GCSManager()
    if all_data:
        gcs.upload_data(all_data)

    return {"status": "success", "records": len(all_data), "bucket": gcs.get_bucket_name()}, 200
