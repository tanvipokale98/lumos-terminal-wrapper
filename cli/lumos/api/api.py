import requests
import os
from dotenv import load_dotenv
load_dotenv()

class APIClient:
    def __init__(self):
        self.base_url = os.getenv("API_BASE_URL")

    def analyse(self, payload:dict)->dict:
        url = f"{self.base_url}/analyse"
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()

api=APIClient()    