from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    URL: str = "https://api.nasa.gov/neo/rest/v1/feed?"
    PROJECT_ID: str = "cloud-project-workflow"
    BUCKET_NAME:str = "asteroids-etl"

    model_config = SettingsConfigDict(env_file="../.env")


settings = Settings()
