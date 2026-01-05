import json
from datetime import datetime

def generate_content():
    # यह डेटा हर रोज अपडेट होगा
    today_data = {
        "date": datetime.now().strftime("%d %B %Y"),
        "topic": "ब्रह्मोस मिसाइल निर्यात समझौता",
        "notes": "भारत ने फिलीपींस को ब्रह्मोस सुपरसोनिक क्रूज मिसाइलों की पहली खेप सौंपी है। यह भारत के रक्षा निर्यात के लिए एक बड़ा मील का पत्थर है। ब्रह्मोस को भारत (DRDO) और रूस ने मिलकर बनाया है।",
        "question": "ब्रह्मोस मिसाइल को किन दो देशों ने संयुक्त रूप से विकसित किया है?",
        "options": ["A. भारत और इजराइल", "B. भारत और अमेरिका", "C. भारत और रूस", "D. भारत और फ्रांस"],
        "answer": "C"
    }
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(today_data, f, ensure_full_ascii=False, indent=4)

if __name__ == "__main__":
    generate_content()
