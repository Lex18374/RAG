# RAG PDF ANALYSER
Een eenvoudige PDF-analyzer die vragen over documenten kan beantwoorden met behulp van GPT-4.

## Functionalitijd
- Extractie van tekst uit PDF-bestanden
- Semantisch chunken van text
- Cosine similarity (chunks tov. vraag)
- Vraagbeantwoording via de OpenAI GPT-4 API

## Installatie
pip install streamlit pdfplumber openai

## Voorbeeld
Stel een vraag over het document: wat zijn stereotypes? wat is de definitie volgens dit document?

--- Geselecteerde Chunks met Similarity Score ---
Chunk 1 (score: 0.5572):
I.Introduction
The Oxford English Dictionary defines a stereotype as a
‘‘widely held but fixed and oversimplified image or idea of a par-
ticular type of person or thing.’’ ...
----------------------------------------

Chunk 2 (score: 0.4920):
Hilton and Von Hippel (1996) define stereotypes as
‘‘mental representations ofreal differences between groups [. . .]
allowing easier and more efficient processing of information. Stereotypes are selective, however, in that they are localized
...

--- Antwoord van LLM ---
Volgens dit document definieert het Oxford English Dictionary een stereotype als een "wijdverbreid maar vast en vereenvoudigd beeld of idee van een bepaald type persoon of ding". Stereotypen zijn overal aanwezig en kunnen betrekking hebben op raciale groepen, politieke groepen, geslachten, demografische groepen en situaties. Hilton en Von Hippel (1996) definiëren stereotypen als "mentale voorstellingen van echte verschillen tussen groepen [...] die een gemakkelijkere en efficiëntere verwerking van informatie mogelijk maken". Stereotypen zijn selectief, ze zijn gelokaliseerd rond groepskenmerken die het meest onderscheidend zijn, die de grootste differentiatie tussen groepen bieden en die de minste variatie binnen de groep vertonen.

## Opmerkingen
- Je hebt een OpenAI API key nodig. Zet deze in qa_engine.py.
- Voor grote PDF-bestanden kan het langer duren om antwoorden te genereren.