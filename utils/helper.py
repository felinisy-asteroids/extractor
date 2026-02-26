from google.cloud import secretmanager

from utils.settings import settings


def get_secret_value(project_id: str, secret_name: str):
    client = secretmanager.SecretManagerServiceClient()

    name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"

    response = client.access_secret_version(request={"name": name})

    return response.payload.data.decode("UTF-8")


def get_api_key():
    return get_secret_value(settings.PROJECT_ID, "API_KEY")
