import json

import requests

url = "http://localhost:10003/api/predict"

image_path = "apple.jpg"

# Open image file, rb - read binary
with open(image_path, "rb") as image_file:
    image_data = image_file.read()


headers = {
    "Content-Type": "image/jpeg",  # Replace with the appropriate content type for your image file
}


response = requests.post(url, data=image_data, headers=headers)

if response.status_code == 200:
    print("Image predicted successfully!")
    pretty_json = json.dumps(response.json(), indent=4)
    print(pretty_json)
else:
    print("Image upload failed. Status Code:", response.status_code)