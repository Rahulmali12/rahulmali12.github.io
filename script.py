import json
import datetime
import feedparser # इसे चलाने के लिए 'pip install feedparser' चाहिए होगा

def get_live_news():
    # Google News RSS for Defense and India News
    feed = feedparser.parse("https://news.google.com/rss/search?q=Indian+Defense+UPSC&hl=hi&gl=IN&ceid=IN:hi")
    articles = []
    
    # टॉप 5 खबरें चुनना
    for entry in feed.entries[:5]:
        articles.append({
            "topic": entry.title,
            "notes": "विस्तृत जानकारी के लिए आज के समाचार पत्र पढ़ें। यह समाचार रक्षा/यूपीएससी के लिए महत्वपूर्ण है।",
            "question": "उपरोक्त समाचार किस क्षेत्र से संबंधित है?",
            "options": ["A. रक्षा", "B. खेल", "C. नियुक्तियां", "D. पुरस्कार"],
            "answer": "A"
        })
    
    return {
        "date": str(datetime.date.today()),
        "articles": articles
    }

data = get_live_news()
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_full_ascii=False, indent=4)
