import requests
import json

# Replace with your actual deployed URL
url = "https://tds-assignments-v47vansh-7002-v47vansh-gmailcoms-projects.vercel.app/telemetry"

# Sample POST data
payload = {
    "regions": ["emea", "amer"],
    "threshold_ms": 176
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print("Status code:", response.status_code)
try:
    print("Response JSON:")
    print(json.dumps(response.json(), indent=4))
except Exception as e:
    print("Failed to parse JSON:", e)
    print("Raw response text:", response.text)
