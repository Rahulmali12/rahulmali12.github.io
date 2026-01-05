import os
import json
import datetime
import google.generativeai as genai

# Yahan apni API Key dalein (GitHub Secrets ka use karna behtar hai)
genai.configure(api_key="AIzaSyDJQIOJK7P_-nUWqoF6cuKdUEPNINQGL3M")

def generate_20_questions():
    model = genai.GenerativeModel('gemini-pro')
    
    # AI ko instruction
    prompt = """
    Aaj ki taaza khabron (Defense, International, Economy, Awards) ke adhaar par 
    UPSC NDA pattern ke 20 mahatvapurn Current Affairs sawal aur notes taiyar karein.
    Response sirf is JSON format mein dein:
    {
      "date": "Date here",
      "articles": [
        {"topic": "...", "notes": "...", "question": "...", "options": ["A..", "B..", "C..", "D.."], "answer": "A/B/C/D"},
        ... total 20 items
      ]
    }
    Language: Hindi Mix (Hinglish/Hindi).
    """
    
    response = model.generate_content(prompt)
    data = json.loads(response.text)
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_full_ascii=False, indent=4)

if __name__ == "__main__":
    generate_20_questions()
