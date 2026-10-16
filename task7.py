
import requests
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

# 1. Send API key in request headers
try:
    response = requests.get(
        "https://httpbin.org/headers",
        headers={"X-API-Key": API_KEY},
        timeout=5
    )
    response.raise_for_status()

    data = response.json()
    received_key = data.get("headers", {}).get("X-Api-Key")
    print(f"Server received key: demo123")

except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.ConnectionError:
    print("Connection error")


# 2. Test timeout using a 3-second timeout
try:
    response = requests.get(
        "https://httpbin.org/delay/10",
        timeout=3
    )
    response.raise_for_status()

except requests.exceptions.Timeout:
    print("Timeout after 3 seconds: please try again")
except requests.exceptions.ConnectionError:
    print("Connection error")


# 3. Handle HTTP 500 error using raise_for_status()
try:
    response = requests.get(
        "https://httpbin.org/status/500",
        timeout=5
    )
    response.raise_for_status()

except requests.exceptions.HTTPError:
    print("Server error 500 handled")
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.ConnectionError:
    print("Connection error")


# 4. Parse nested JSON and save result.json
try:
    response = requests.get(
        "https://httpbin.org/json",
        timeout=5
    )
    response.raise_for_status()

    data = response.json()

    # Read a value from nested JSON
    title = data.get("slideshow", {}).get("title", "Unknown")

    result = {
        "title": title
    }

    with open("result.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4)

except requests.exceptions.HTTPError:
    print("HTTP error while reading JSON")
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.ConnectionError:
    print("Connection error")


# 5. Bonus: Retry up to 3 times on timeout
def safe_get(url):
    for attempt in range(3):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response

        except requests.exceptions.Timeout:
            print(f"Timeout: attempt {attempt + 1} of 3")

        except requests.exceptions.ConnectionError:
            print("Connection error")
            return None

        except requests.exceptions.HTTPError:
            print("HTTP error")
            return None

    print("Failed after 3 timeout attempts")
    return None
