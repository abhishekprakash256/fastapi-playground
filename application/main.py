"""
The fast api main app 


"""

from fastapi import FastAPI
from fastapi_plugin.fast_api_client import Auth0FastAPI
from application.config import get_settings

app = FastAPI()

@app.get("/api/public")
def public():

   result = {
       "status": "success",
       "msg": ("Hello from a public endpoint! You don't need to be "
               "authenticated to see this.")
   }
   return result