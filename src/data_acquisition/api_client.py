import requests

API_ENDPOINT = 'https://api.legislation.gov/bills'

def fetch_bills():
    response = requests.get(API_ENDPOINT)
    return response.json()
