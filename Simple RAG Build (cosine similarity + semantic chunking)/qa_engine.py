import textwrap 
import re
import numpy as np
import openai

def split_text(text, max_chars=1000): 
    return textwrap.wrap(text, max_chars) # Deel tekst op in stukken van max_chars tekens

def semantic_chunk_text(text, max_chars=1000):
    sentences = re.split(r'(?<=[.!?])\s+', text)  # Split op zinsgrenzen
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 <= max_chars:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

openai.api_key = "API_KEY_HERE"  # Zet hier je OpenAI API key

def get_embedding(text, model="text-embedding-3-small", dimensions=None):
    client = openai.OpenAI(api_key=openai.api_key)
    params = {
        "model": model,
        "input": text
    }
    if dimensions:
        params["dimensions"] = dimensions
    response = client.embeddings.create(**params)
    return np.array(response.data[0].embedding)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def find_relevant_chunks_cosine(chunks, question, top_k=10):
    question_emb = get_embedding(question, model="text-embedding-3-small")
    chunk_scores = []
    for chunk in chunks:
        chunk_emb = get_embedding(chunk, model="text-embedding-3-small")
        score = cosine_similarity(question_emb, chunk_emb)
        chunk_scores.append((score, chunk))
    chunk_scores.sort(key=lambda x: x[0], reverse=True)
    relevant = chunk_scores[:top_k]  # lijst van (score, chunk)
    return relevant

def answer_question(chunks, question):
    relevant_chunks = find_relevant_chunks_cosine(chunks, question, top_k=10)
    context = "\n\n".join([chunk for score, chunk in relevant_chunks])
    prompt = f"""
Gebruik de onderstaande tekst om de vraag te beantwoorden. Als je het antwoord niet zeker weet, geef dan je beste gok.

Tekst:
{context}

Vraag: {question}
Antwoord:""" 
    
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content.strip(), relevant_chunks
