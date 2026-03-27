from functools import lru_cache

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
   auth0_domain: str
   auth0_api_audience: str

   class Config:
       env_file = ".env"

@lru_cache()
def get_settings():
   return Settings()




settings = get_settings()
auth0 = Auth0FastAPI(
   domain=settings.auth0_domain,
   audience=settings.auth0_api_audience
)