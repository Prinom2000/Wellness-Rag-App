import requests
import os
from dotenv import load_dotenv
from t1 import user_id
from t1 import access_token
# Load environment variables from .env
load_dotenv()

# Get base URL from .env
base_url = os.getenv("BASE_URL")

user_id= user_id

# API endpoint
# emotion_url  = f"{base_url}/api/v1/emotions/user/cmvgvt55oe0001fsxgxtgle5a"
emotion_url  = f"{base_url}/api/v1/emotions/user/{user_id}"

# Your access token (copied from login response)
access_token = access_token

# Set authorization header
headers = {
    "Authorization": f"Bearer {access_token}"
}

# Send GET request
response = requests.get(emotion_url , headers=headers)

# Handle response
if response.status_code == 200:
    data = response.json()
    print("\n✅ Request successful!\n")
    print(data)
    print("\n")
else:
    print(f"❌ Request failed with status {response.status_code}")
    print(response.text)
