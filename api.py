import requests

def get_cat_images(api_key, breed_id='beng', limit=10):
    url = f"https://api.thecatapi.com/v1/images/search?limit={limit}&breed_ids={breed_id}&api_key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Use the function and print the image URLs
api_key = "live_5jLUuQorNc5pXKkVJVBwFM546S2piyobYHTDPvdneungCXNDVGr8d6ALPacTojkd"
images = get_cat_images(api_key)

if images:
    for image in images:
        print(image['url'])  # Print the URL of each image
else:
    print("Failed to fetch cat images.")