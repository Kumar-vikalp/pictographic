import requests
import json

headers = {
    'sec-ch-ua-platform': '"Windows"',
    'Referer': 'https://www.pictographic.io/',
    'User-Agent': 'Mozilla/5.0',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'Content-Type': 'application/json',
    'sec-ch-ua-mobile': '?0',
}

json_data = {
    'prompt': 'apple',
    'email': '',
    'type': 'slow-1',
    'skip_credit_check': True,
}

response = requests.post(
    "https://icon-generation.pictographic.ai/icon-prompt",
    headers=headers,
    json=json_data
)

data = response.json()

print(json.dumps(data, indent=4))
