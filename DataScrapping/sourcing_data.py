import requests
from bs4 import BeautifulSoup
import os

# create directory if it doesn't exist
save_dir = r'C:\Users\rctuh\Desktop\minor projects\Vgg16_Image_Classifier\DataScrapping\dogs_google'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# URL of the page to be scraped
url = 'https://www.pexels.com/search/dogs/'

# send a GET request to the URL
response = requests.get(url)

# parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# find all image tags and download the images
count = 0
for img in soup.find_all('img'):
    img_url = img['src']
    if 'https://images.pexels.com/photos/15286' in img_url:
        response = requests.get(img_url)
        with open(os.path.join(save_dir, f"dog_{count}.jpg"), "wb") as f:
            f.write(response.content)
        count += 1
        if count == 189:
            break
print(f"Downloaded {count} images to {save_dir}")
