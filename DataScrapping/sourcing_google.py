import requests
import os

# create directory if it doesn't exist
save_dir = 'C:/Users/rctuh/Desktop/minor projects/Vgg16_Image_Classifier/DataScrapping/dogs_sourced'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# URL of the page to be scraped
url = 'https://www.pexels.com/search/dog/'

# send a GET request to the URL
response = requests.get(url)

# extract the JSON data from the response
json_data = response.json()

# download the images
count = 0
for photo in json_data['photos']:
    img_url = photo['src']['large']
    response = requests.get(img_url)
    with open(os.path.join(save_dir, f"dog_{count}.jpg"), "wb") as f:
        f.write(response.content)
    count += 1
    if count == 200:
        break

print(f"Downloaded {count} images to {save_dir}")
