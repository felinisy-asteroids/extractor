from google.cloud import secretmanager

from utils.settings import settings


def access_to_api(project_id: str, secret_name: str):
    client = secretmanager.SecretManagerServiceClient()

    name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"

    response = client.access_secret_version(request={"name": name})

    return response.payload.data.decode("UTF-8")


def get_api_key():
    return access_to_api(settings.PROJECT_ID, "API_KEY")


def get_url():
    return f"{settings.URL}" + "start_date={0}&end_date={1}&api_key={2}"

