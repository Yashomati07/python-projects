import os
import json
from google.auth.credentials import AnonymousCredentials
from google.cloud import language_v1

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path_to_your_credentials.json'

def analyze_text(text):
    client = language_v1.LanguageServiceClient(credentials=AnonymousCredentials())
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = client.analyze_sentiment(request={'document': document})
    sentiment_score = response.document_sentiment.score
    return sentiment_score

def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        sentiment_score = analyze_text(user_input)
        if sentiment_score >= 0:
            print("Google Assistant: That sounds positive!")
        else:
            print("Google Assistant: That sounds negative.")

if _name_ == "_main_":
    main()