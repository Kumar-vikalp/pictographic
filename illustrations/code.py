import requests
import time

SUBMIT_URL = "https://app.pictographic.io/submit_prompt"
FIREBASE_URL = "https://pictographic-54d58-default-rtdb.firebaseio.com"
STYLES = [
    "oldschool", "notion", "lined", "purple", "isometric-modern", "flat-modern",
    "inkmodern", "flatcool", "cartoon-cute", "cartoon-black-white",
    "isometric-sketch", "minimal-line", "black-and-white-line"
]
PROMPT = "fly emirates jersey"
STYLE = "oldschool"
DIMENSION = "1:1 square 1024x1024"
EMAIL = "test@example.com"

headers = {
    "Content-Type": "application/json",
    "Origin": "https://www.pictographic.io",
    "Referer": "https://www.pictographic.io/"
}

payload = {
    "style": STYLE,
    "prompt": PROMPT,
    "dimension": DIMENSION,
    "email": EMAIL
}

# ⏱ Start timer
start_time = time.time()

print("Submitting prompt...")

# 1️⃣ Submit prompt
resp = requests.post(SUBMIT_URL, json=payload, headers=headers)
data = resp.json()

prompt_id = data["prompt_key"]
print("Prompt key:", prompt_id)

firebase_url = f"{FIREBASE_URL}/prompts/{prompt_id}.json"

print("Watching generation status...\n")

images = {}

# 2️⃣ Wait for images
while True:
    r = requests.get(firebase_url)
    data = r.json()

    if not data:
        time.sleep(2)
        continue

    for i in range(1, 5):

        key = f"image_{i}"

        if key in data and key not in images:

            img_url = data[key]["url"]

            print(f"Image {i} generated:")
            print(img_url, "\n")

            images[key] = img_url

    if len(images) == 4:
        end_time = time.time()
        total_time = end_time - start_time

        print("✅ All images generated.")
        print(f"⏱ Total time taken: {total_time:.2f} seconds")

        break

    time.sleep(2)
