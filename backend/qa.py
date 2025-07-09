import os
import requests
from dotenv import load_dotenv
from embedder import chunk_text, get_top_k_chunks

load_dotenv()
API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

def answer_question(context: str, question: str, model: str = "deepset/roberta-base-squad2") -> str:
    try:
        chunks = chunk_text(context)
        relevant_context = get_top_k_chunks(chunks, question, k=1)

        API_URL = f"https://api-inference.huggingface.co/models/{model}"
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        payload = {
            "inputs": {
                "question": question,
                "context": relevant_context[:3000],
            }
        }

        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json().get("answer", "No answer found.")
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error during retrieval: {str(e)}"
