import requests
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()


def get_cat_images(api_key, breed_id='beng', limit=10):
    url = f"https://api.thecatapi.com/v1/images/search?limit={limit}&breed_ids={breed_id}&api_key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

api_key = os.getenv('CAT_API_KEY')
images = get_cat_images(api_key)

if images:
    for image in images:
        print(image['url'])  # Print the URL of each image
else:
    print("Failed to fetch cat images.")