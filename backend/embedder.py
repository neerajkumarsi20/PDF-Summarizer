from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import textwrap

# Load embedding model once
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

def chunk_text(text, chunk_size=500, overlap=100):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

def get_top_k_chunks(text_chunks, question, k=1):
    chunk_embeddings = embed_model.encode(text_chunks)
    question_embedding = embed_model.encode([question])[0]
    
    similarities = cosine_similarity([question_embedding], chunk_embeddings)[0]
    top_k_indices = similarities.argsort()[-k:][::-1]
    
    top_chunks = [text_chunks[i] for i in top_k_indices]
    return top_chunks[0], top_k_indices[0]  # return best chunk and its index

