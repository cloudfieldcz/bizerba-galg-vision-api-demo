import json

import requests

url = "http://localhost:10003/api/transaction_post"


headers = {
    "Content-Type": "application/json",  # Replace with the appropriate content type for your image file
}

json_data = {
    "sell_id": "123456",
    "device_id": "abc123",
    "time": "202402091200",
    "neural_version": "v1.0",
    "success": True,
    "sold_assortment": "apple_jonaprice",
    "success_position": 1,
    "position_1_percent": 25.5,
    "position_2_percent": 5.0,
    "position_3_percent": 07.25,
    "position_4_percent": 0.99,
    "position_5_percent": 0.25,
    "position_1_assortment": "apple_jonaprice",
    "position_2_assortment": "tomato_organic",
    "position_3_assortment": "peach_organic",
    "position_4_assortment": "pear",
    "position_5_assortment": "grapefruit",
    "duration": 60
}

response = requests.post(url, json=json_data, headers=headers)
print(str(response))

if response.status_code == 200:
    print("Transaction logged successfully!")
    response_from_server = response.json()
    pretty_json = json.dumps(response_from_server, indent=4)
    print(pretty_json)
else:
    print("Transaction logged. Status Code:", response.status_code, "Status message:", response.text)