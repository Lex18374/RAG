from pdf_utils import extract_text_from_pdf
from qa_engine import semantic_chunk_text, answer_question

def main():
    file_path = "sample.pdf" # Pad naar PDF-bestand
    text = extract_text_from_pdf(file_path)
    chunks = semantic_chunk_text(text)  # semantisch chunken

    question = input("Stel een vraag over het document: ")
    answer, relevant_chunks = answer_question(chunks, question)

    print("\n--- Geselecteerde Chunks met Similarity Score ---")
    for i, (score, chunk) in enumerate(relevant_chunks, 1):
        print(f"\nChunk {i} (score: {score:.4f}):\n{chunk}\n{'-'*40}")

    print("\n--- Antwoord van LLM ---")
    print(answer)

if __name__ == "__main__":
    main() # Voer de main functie uit als het script direct wordt gestart
