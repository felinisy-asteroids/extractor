import logging

from extractor.extractor import Extractor
from gcp_client.gcs_manager import GCSManager

def main(request):
    raw_body = request.get_json()
    date_list = raw_body.get("dates",[])
    logging.info(f"Dates: {date_list}")

    if not date_list:
        logging.error("No dates")
        return {"message": "No dates"},400

    extractor = Extractor()

    all_data = extractor.extract_all(date_list)
    if all_data:
        gcs = GCSManager()
        try:
            gcs.upload_data(all_data)
            return {"status": "success", "records": len(all_data)}, 200
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500

    return {"status": "no_data", "records": 0}, 200

# if __name__ == "__main__":
#     class MockRequest:
#         def get_json(self):
#             return {
#                 "dates": ["2024-01-01", "2024-01-02"]
#             }
#
#     response, status = main(MockRequest())
#     print(f"Status: {status}")
#     print(f"Response: {response}")