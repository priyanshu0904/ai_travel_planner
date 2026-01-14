import os
import requests

#my huggingface api key
HF_API_KEY = os.getenv("HF_API_KEY")

#huggingface api url
API_URL = "https://router.huggingface.co/v1/chat/completions"

#authentication header
HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

def ask_ai(user_query):
    if not user_query:
        return "❌ Empty prompt sent to AI. Write something to experience the best planning for your next amazing trip."

    data = {
        "model": "meta-llama/Llama-3.1-8B-Instruct",
        "messages": [
            {"role": "user", "content": str(user_query)}
        ]
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=data)

        if response.status_code != 200:
            return "❌ API Error. Try again later."

        result = response.json()
        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"❌ Exception: {str(e)}"
