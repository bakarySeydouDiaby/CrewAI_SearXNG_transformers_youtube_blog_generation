import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# SearXNG API endpoint
searxng_url = os.getenv('SEARXNG_URL', 'http://localhost:8080/search')

# API key
api_key = os.getenv('SEARXNG_API_KEY')

# Search query
query = "AI"

# Parameters
params = {
    'q': query,
    'format': 'json',
    'apikey': api_key
}

# Make the request
response = requests.get(searxng_url, params=params)

# Check the response
if response.status_code == 200:
    print("API key is correct. Here are the search results:")
    print(response.json())
else:
    print("Failed to fetch search results. Status code:", response.status_code)
    print("Response:", response.text)