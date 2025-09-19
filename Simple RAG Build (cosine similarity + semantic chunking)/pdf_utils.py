import pdfplumber

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf: # Open het PDF-bestand
        text = "" # Initialiseer een lege string voor de tekst
        for page in pdf.pages: # Loop door alle pagina's in het PDF-bestand
            text += page.extract_text() + "\n" # Voeg de tekst van elke pagina toe, gevolgd door een nieuwe regel
    return text 
