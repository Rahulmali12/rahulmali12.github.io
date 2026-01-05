import os
import json
import datetime
import google.generativeai as genai

# GitHub Secrets से API Key लेगा
api_key = os.getenv("AIzaSyDVVKHllpddYD-hkXVwWWeK53AyIfGm0CE")
genai.configure(api_key=api_key)

def generate_content():
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = """
        Create 20 high-quality UPSC NDA level Current Affairs questions for today in Hindi.
        Provide response in STRICT JSON format with this structure:
        {"date": "Current Date", "articles": [{"topic": "...", "notes": "...", "question": "...", "options": ["A. x", "B. y", "C. z", "D. w"], "answer": "Letter"}]}
        Ensure notes are informative and questions are competitive.
        """
        
        response = model.generate_content(prompt)
        # Markdown रिमूव करना
        clean_text = response.text.replace("```json", "").replace("```", "").strip()
        data = json.loads(clean_text)
        
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_full_ascii=False, indent=4)
        print("Success: data.json has been updated.")
        
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    generate_content()
