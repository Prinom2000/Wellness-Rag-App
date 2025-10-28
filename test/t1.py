import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get base URL from .env
base_url = os.getenv("BASE_URL")

# Check if base URL is loaded properly
if not base_url:
    raise ValueError("❌ BASE_URL not found in .env file")

# Construct full login URL
url = f"{base_url}/api/v1/auth/login"

# JSON payload
payload = {
    "email": "mdarmanya.h@gmail.com",
    "password": "12345678"
}

# Send POST request
response = requests.post(url, json=payload)

# Handle response
if response.status_code == 201:
    data = response.json()
    print("\n✅ Login successful!")

    # Extract data
    access_token = data["data"]["data"]["tokens"]["accessToken"]
    refresh_token = data["data"]["data"]["tokens"]["refreshToken"]
    user_id = data["data"]["data"]["userId"]

    print("\nAccess Token:", access_token)
    print("\nRefresh Token:", refresh_token)
    print("\nUser ID:", user_id)

else:
    print(f"❌ Login failed: {response.status_code}")
    print("Response:", response.text)
