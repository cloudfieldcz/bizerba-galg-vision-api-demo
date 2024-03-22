import json
from datetime import datetime

import requests

url = "http://localhost:10003/api/transaction_post"

headers = {
    "Content-Type": "application/json",  # Replace with the appropriate content type for your image file
}

# Get the current datetime in the desired format
current_time = datetime.now().strftime('%Y%m%d%H%M')

json_data = {
    "sell_id": "123456",
    "device_id": "abc123",
    "suggestion_id": "123456",
    "time": current_time,
    "sold_assortment": "101", # chodi PLU
    "duration": 0.60
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
