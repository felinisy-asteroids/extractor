from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    URL: str = "https://api.nasa.gov/neo/rest/v1/feed?start_date={0}&end_date={1}&api_key={2}"
    PROJECT_ID: str = "cloud-project-workflow"
    BUCKET_NAME: str = "asteroids-etl"

    model_config = SettingsConfigDict(env_file="../.env")


settings = Settings()
