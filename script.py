import os
import json
import datetime
import google.generativeai as genai

# Security: GitHub Secrets से API Key उठाएगा
api_key = os.getenv("AIzaSyDVVKHllpddYD-hkXVwWWeK53AyIfGm0CE")
genai.configure(api_key=api_key)

def generate_content():
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = """
    Create 20 high-quality UPSC NDA level Current Affairs questions for today.
    For each, provide: 1. Topic 2. Short Study Notes (2-3 lines) 3. MCQ Question 4. 4 Options 5. Correct Option Letter.
    Language: Hindi. 
    Format: Strict JSON only.
    Structure: {"date": "...", "articles": [{"topic": "...", "notes": "...", "question": "...", "options": ["A..", "B..", "C..", "D.."], "answer": "A"}]}
    """
    
    response = model.generate_content(prompt)
    # JSON साफ करना (कभी-कभी AI markdown लगा देता है)
    raw_text = response.text.replace("```json", "").replace("```", "").strip()
    data = json.loads(raw_text)
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_full_ascii=False, indent=4)

if __name__ == "__main__":
    generate_content()
