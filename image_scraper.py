import requests
from bs4 import BeautifulSoup
import os

def scrape_images(url, folder):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    if not os.path.exists(folder):
        os.makedirs(folder)
    img_tags = soup.find_all('img')

    for img in img_tags:

        img_url = img.get('data-src') or img.get('data-url')

        try:
            img_response = requests.get(img_url, stream=True)
            img_name = os.path.basename(img_url)
            img_path = os.path.join(folder, img_name)
            with open(img_path, 'wb') as f:
                for chunk in img_response.iter_content(1024):
                    f.write(chunk)
            print(f"Downloaded: {img_url}")
        except Exception as e:
            print(f"Download Error: {img_url}")
            print(str(e))
