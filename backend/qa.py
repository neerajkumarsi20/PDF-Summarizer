import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

def answer_question(context: str, question: str, model: str = "deepset/roberta-base-squad2") -> str:
    API_URL = f"https://api-inference.huggingface.co/models/{model}"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    payload = {
        "inputs": {
            "question": question,
            "context": context[:3000],  # limit context to avoid API overload
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json().get("answer", "No answer found.")
    else:
        return f"Error: {response.status_code} - {response.text}"
