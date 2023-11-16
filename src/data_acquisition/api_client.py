import requests

# Replace 'API_KEY' and 'API_ENDPOINT' with your actual key and endpoint URLs
API_KEY = 'your_api_key_here'
NY_ASSEMBLY_ENDPOINT = 'https://api.assembly.ny.gov/bills'
NY_SENATE_ENDPOINT = 'https://api.senate.ny.gov/bills'

def get_assembly_bills(session, params=None):
    """
    Fetches bill data from the New York Assembly API.
    """
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = session.get(NY_ASSEMBLY_ENDPOINT, headers=headers, params=params)
    response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
    return response.json()

def get_senate_bills(session, params=None):
    """
    Fetches bill data from the New York Senate API.
    """
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = session.get(NY_SENATE_ENDPOINT, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def main():
    # Use a session for connection pooling and reusing the TCP connection
    with requests.Session() as session:
        # Example usage: Fetching bills from the Assembly API
        assembly_bills = get_assembly_bills(session, params={'type': 'passed'})
        print("Assembly Bills:", assembly_bills)

        # Example usage: Fetching bills from the Senate API
        senate_bills = get

