import requests

API_KEY = 'your_api_key_here' # visiting user please go get individual api's for usage to do important data privacy!
NY_ASSEMBLY_ENDPOINT = 'https://api.assembly.ny.gov/bills'
NY_SENATE_ENDPOINT = 'https://api.senate.ny.gov/bills'

def get_bills(endpoint, session, params=None):
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = session.get(endpoint, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def main():
    with requests.Session() as session:
        assembly_bills = get_bills(NY_ASSEMBLY_ENDPOINT, session, params={'type': 'passed'})
        print("Assembly Bills:", assembly_bills)

        senate_bills = get_bills(NY_SENATE_ENDPOINT, session, params={'type': 'passed'})
        print("Senate Bills:", senate_bills)

if __name__ == "__main__":
    main()

     

