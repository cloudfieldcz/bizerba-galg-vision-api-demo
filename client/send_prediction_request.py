import json
import requests

image_path = "apple.jpg"
group_param = "fruit"  # fruit, vegetable, bakery

url = "http://localhost:10003/api/v1/suggest/{name+}"

# Open image file, rb - read binary
with open(image_path, "rb") as image_file:
    image_data = image_file.read()

payload = {
    "image": image_data,
    "group": group_param
}

headers = {
    'Content-Type': 'image/jpeg',
}

response = requests.post(url, data=payload, headers=headers)

if response.status_code == 200:
    print("Image predicted successfully!")
    pretty_json = json.dumps(response.json(), indent=4)
    print(pretty_json)
else:
    print("Image upload failed. Status Code:", response.status_code, "Status message:", response.text)