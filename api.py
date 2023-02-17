import os
import requests
from dotenv import load_dotenv
load_dotenv()

class API:
    """
    A class that represents an API client.

    Attributes:
        api_key (str): The API key to use for making requests.
        api_base_url (str): The base URL for the API.
    """

    def __init__(self):
        # Initialize the API client with the API key and base URL from environment variables.
        self.api_key = os.environ.get('API_KEY')
        self.base_url = "<Your API's Base URL (Example: https://api.google.com/)"

    def make_request(self, endpoint):
        # Send a GET request to the specified API endpoint and return the JSON response.
        url = self.base_url + endpoint
        try:
            response = requests.get(url)
        except:
            print('Error with API request!')
            return None
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error with API request. Status code: {response.status_code}")
            return None

    def api_call(self, variable):
        # Send a request to the API with the specified variable and return the JSON response.
        endpoint = f"example_endpoint?key={self.api_key}&variable={variable}&json"
        return self.make_request(endpoint)

# Mainly created to utilize one API but you can create multiple classes for multiple APIs