import requests
import os
from decouple import config

API_KEY = config('KEY', cast=str)

class CivicApi():
    def voter_query():
        url = f"https://www.googleapis.com/civicinfo/v2/voterinfo?key={API_KEY}&electionId=2000&address=9701 royal lytham drive plano tx 75025"
        payload={}
        files={}
        headers = {
            f'{API_KEY}': f'{API_KEY}'
        }

        json_response = requests.request("GET", url, headers=headers, data=payload, files=files)
        return json_response.json()
CivicApi.voter_query()