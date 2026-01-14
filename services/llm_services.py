import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# my huggingface api key
HF_API_KEY = os.getenv("HF_API_KEY")

# huggingface api url
API_URL = "https://router.huggingface.co/v1/chat/completions"

# authentication header
HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

# the query used by the model
def ask_ai(user_query):
    if not user_query:
        return "❌ Empty prompt sent to AI. Write something to experience the best planning for your next amazing trip."

    if not HF_API_KEY:
        return "❌ API Key not found. Please check your .env file."

    data = {
        "model": "meta-llama/Llama-3.1-8B-Instruct:novita",
        "messages": [
            {"role": "user", "content": str(user_query)}
        ]
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=data)

        # DEBUG (so you can see real error in terminal)
        print("STATUS:", response.status_code)
        print("RAW RESPONSE:", response.text)

        if response.status_code != 200:
            return "❌ API Error: " + response.text

        result = response.json()
        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"❌ Exception: {str(e)}"
