import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

def summarize_text(text: str, model: str) -> str:
    API_URL = f"https://api-inference.huggingface.co/models/{model}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    payload = {"inputs": text[:2048]}  # Limit size to avoid long input errors

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()[0].get("summary_text", "No summary returned.")
    else:
        return f"Error: {response.status_code} - {response.text}"
